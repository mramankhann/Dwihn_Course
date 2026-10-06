"""Create accurate static previews of four possible DWIHN course formats."""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = Path(__file__).parent
W, H = 1600, 1000
NAVY = "#0B1D36"
NAVY_2 = "#142D4D"
TEAL = "#0F8C92"
TEAL_DARK = "#08747A"
BLUE = "#2476A5"
BG = "#F3F7FA"
LINE = "#DCE6ED"
TEXT = "#183047"
MUTED = "#53687B"
PALE = "#E7F4F3"
WHITE = "#FFFFFF"
ORANGE = "#D68035"

FONTDIR = Path("C:/Windows/Fonts")
FONTFILES = {
    "regular": FONTDIR / "segoeui.ttf",
    "semibold": FONTDIR / "seguisb.ttf",
    "bold": FONTDIR / "segoeuib.ttf",
}


def f(size, weight="regular"):
    return ImageFont.truetype(str(FONTFILES[weight]), size)


def box(draw, rect, fill, radius=0, outline=None, width=1):
    draw.rounded_rectangle(rect, radius=radius, fill=fill, outline=outline, width=width)


def txt(draw, xy, value, size=24, color=TEXT, weight="regular", anchor=None):
    draw.text(xy, value, font=f(size, weight), fill=color, anchor=anchor)


def para(draw, xy, value, max_width, size=23, color=TEXT, weight="regular", gap=8):
    x, y = xy
    words = value.split()
    lines = []
    current = ""
    for word in words:
        candidate = (current + " " + word).strip()
        if current and draw.textbbox((0, 0), candidate, font=f(size, weight))[2] > max_width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    line_h = size + gap
    for line in lines:
        txt(draw, (x, y), line, size, color, weight)
        y += line_h
    return y


def pill(draw, rect, label, fill=PALE, fg=TEAL_DARK, size=18):
    box(draw, rect, fill, radius=(rect[3] - rect[1]) // 2)
    txt(draw, ((rect[0] + rect[2]) / 2, (rect[1] + rect[3]) / 2), label,
        size, fg, "semibold", anchor="mm")


def icon_circle(draw, x, y, n, fill=TEAL):
    box(draw, (x, y, x + 48, y + 48), fill, radius=24)
    txt(draw, (x + 24, y + 24), str(n), 21, WHITE, "bold", anchor="mm")


def brand(draw, x, y, light=False):
    box(draw, (x, y, x + 38, y + 38), TEAL, radius=9)
    txt(draw, (x + 19, y + 19), "AI", 17, WHITE, "bold", anchor="mm")
    txt(draw, (x + 54, y + 2), "DWIHN AI Readiness", 25,
        WHITE if light else NAVY, "bold")


def save(img, name):
    path = OUT / name
    img.save(path, optimize=True)
    print(path)
    return path


def lms():
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    box(d, (0, 0, W, 76), NAVY)
    brand(d, 34, 20, True)
    txt(d, (1205, 26), "Course dashboard", 21, "#C9D7E4", "semibold")
    pill(d, (1430, 17, 1565, 59), "PREVIEW", fill="#D7EFEA", fg=TEAL_DARK)

    box(d, (0, 76, 296, H), WHITE)
    d.line((296, 76, 296, H), fill=LINE, width=2)
    txt(d, (32, 112), "MY LEARNING PATH", 18, MUTED, "bold")
    txt(d, (32, 159), "Foundations & safe use", 23, NAVY, "semibold")
    modules = [
        ("01", "What AI Is — and Isn't"),
        ("02", "Approved Tools & HIPAA"),
        ("03", "Data Classification"),
        ("04", "Prompting Skills"),
        ("05", "Daily DWIHN Work"),
    ]
    y = 218
    for num, label in modules:
        if num == "02":
            box(d, (16, y - 9, 280, y + 56), PALE, radius=12)
            box(d, (16, y - 9, 22, y + 56), TEAL, radius=3)
        txt(d, (32, y + 4), num, 21, TEAL if num == "02" else MUTED, "bold")
        para(d, (76, y), label, 190, 20, NAVY if num == "02" else TEXT,
             "semibold" if num == "02" else "regular", 4)
        y += 84
    d.line((24, 684, 270, 684), fill=LINE, width=2)
    txt(d, (32, 710), "Next: Lumenore practice", 19, MUTED, "semibold")
    para(d, (32, 750), "Session 5 opens after the safety modules are complete.", 235, 18, MUTED)

    box(d, (326, 108, 1235, 300), WHITE, radius=20, outline=LINE, width=2)
    pill(d, (355, 133, 596, 170), "WEEK 2  ·  SESSION 2", fill=PALE)
    txt(d, (355, 187), "Approved Tools & HIPAA Safety", 43, NAVY, "bold")
    txt(d, (355, 252), "Make a safe tool choice before entering any data.", 23, MUTED)
    txt(d, (1050, 145), "LESSON PROGRESS", 16, MUTED, "bold")
    box(d, (1048, 185, 1190, 198), "#DFE9EE", radius=6)
    box(d, (1048, 185, 1133, 198), TEAL, radius=6)
    txt(d, (1049, 216), "3 of 5 steps", 18, TEAL_DARK, "semibold")

    box(d, (326, 322, 1235, 668), WHITE, radius=20, outline=LINE, width=2)
    txt(d, (356, 348), "The 3-check decision", 29, NAVY, "bold")
    para(d, (356, 395), "Before opening an AI tool, decide what the task needs and what data it would expose.", 810, 21, MUTED)
    steps = [
        ("Classify", "Is it public, internal, confidential, or restricted?"),
        ("Check the catalog", "Is this exact tool and workspace approved for that tier?"),
        ("Review", "Verify the output before sharing or acting on it."),
    ]
    sx = 356
    for i, (title, body) in enumerate(steps, 1):
        x = sx + (i - 1) * 284
        box(d, (x, 477, x + 266, 650), "#F7FAFB", radius=14, outline=LINE, width=2)
        icon_circle(d, x + 18, 495, i)
        txt(d, (x + 18, 551), title, 22, NAVY, "bold")
        para(d, (x + 18, 577), body, 226, 17, MUTED, gap=3)

    box(d, (326, 690, 1235, 970), WHITE, radius=20, outline=LINE, width=2)
    pill(d, (355, 714, 526, 747), "PRACTICE CHECK", fill="#E7EEF8", fg=BLUE, size=17)
    txt(d, (355, 763), "A care coordinator needs to summarize a member record.", 26, NAVY, "semibold")
    txt(d, (355, 807), "What should happen first?", 21, MUTED)
    box(d, (355, 850, 759, 920), WHITE, radius=12, outline=LINE, width=2)
    txt(d, (376, 868), "A  Paste it into any AI chat", 19, TEXT)
    box(d, (780, 850, 1198, 920), PALE, radius=12, outline=TEAL, width=3)
    txt(d, (801, 866), "B  Check classification and", 19, NAVY, "semibold")
    txt(d, (830, 891), "approved destination", 19, NAVY, "semibold")

    box(d, (1260, 108, 1572, 510), WHITE, radius=20, outline=LINE, width=2)
    txt(d, (1287, 139), "Quick reference", 25, NAVY, "bold")
    d.line((1287, 187, 1545, 187), fill=LINE, width=2)
    txt(d, (1287, 218), "Never guess approval", 21, TEAL_DARK, "bold")
    para(d, (1287, 254), "Use the current DWIHN tool catalog and your organization's data rules.", 251, 20, TEXT)
    box(d, (1287, 368, 1545, 472), "#FFF5E9", radius=12)
    para(d, (1303, 385), "Training cases use synthetic data only.", 220, 19, "#86531F", "semibold")
    box(d, (1260, 530, 1572, 970), WHITE, radius=20, outline=LINE, width=2)
    txt(d, (1287, 561), "Session resources", 25, NAVY, "bold")
    for j, label in enumerate(["Desk card: data tiers", "Tool-choice worksheet", "5-question quiz", "Ask the trainer"]):
        yy = 615 + j * 72
        d.line((1287, yy + 49, 1545, yy + 49), fill=LINE, width=2)
        txt(d, (1287, yy), label, 19, BLUE, "semibold")
        txt(d, (1532, yy), ">", 22, BLUE, "bold")
    return save(im, "01-interactive-lms.png")


def pdf_manual():
    im = Image.new("RGB", (W, H), "#DCE3E9")
    d = ImageDraw.Draw(im)
    box(d, (0, 0, W, 66), "#273647")
    txt(d, (34, 19), "DWIHN_AI_Readiness_Manual.pdf", 23, WHITE, "semibold")
    txt(d, (1370, 20), "Sample page", 21, "#D5E1EA")
    box(d, (204, 94, 1396, 962), "#AEBBC5", radius=3)
    box(d, (194, 84, 1386, 952), WHITE, radius=2)
    box(d, (194, 84, 1386, 98), NAVY)
    txt(d, (252, 129), "DWIHN AI READINESS  /  LEARNER & INSTRUCTOR MANUAL", 18, TEAL_DARK, "bold")
    d.line((252, 171, 1328, 171), fill=LINE, width=2)
    pill(d, (252, 201, 517, 239), "MODULE 2  ·  SESSION 2", fill=PALE)
    txt(d, (252, 263), "Approved Tools &", 47, NAVY, "bold")
    txt(d, (252, 321), "HIPAA Safety", 47, NAVY, "bold")
    para(d, (252, 393), "Learning outcome: select a permitted AI workflow, explain why it is permitted, and stop when the data or tool status is unclear.", 1030, 23, MUTED)

    d.line((790, 493, 790, 795), fill=LINE, width=2)
    txt(d, (252, 500), "TEACH THE CONCEPT", 20, TEAL_DARK, "bold")
    txt(d, (252, 542), "Approval is task-specific", 29, NAVY, "bold")
    para(d, (252, 590), "An approved product name does not authorize every account, feature, data type, or use. Check the current catalog for the exact workspace and intended task.", 495, 22, TEXT)
    box(d, (252, 735, 744, 807), "#FDEFE7", radius=10)
    para(d, (270, 748), "If approval is uncertain, stop and ask the designated owner.", 455, 19, "#8B4B2B", "semibold", 5)

    txt(d, (831, 500), "PRACTICE CASE", 20, TEAL_DARK, "bold")
    txt(d, (831, 542), "Member summary request", 29, NAVY, "bold")
    para(d, (831, 590), "A coordinator wants an AI draft of a case summary. The source includes a name, appointment history, and care notes. What is the data tier? Which catalog entry permits the task? What will you review?", 478, 22, TEXT)
    box(d, (831, 751, 1328, 807), PALE, radius=10)
    txt(d, (850, 768), "Write your decision before the demo.", 20, TEAL_DARK, "semibold")

    d.line((252, 843, 1328, 843), fill=LINE, width=2)
    txt(d, (252, 864), "INSTRUCTOR CUE", 18, MUTED, "bold")
    para(d, (252, 893), "Ask what would change if the record were de-identified.", 740, 19, TEXT)
    txt(d, (1294, 890), "18", 22, NAVY, "bold")
    return save(im, "02-pdf-manual.png")


def vitepress():
    im = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(im)
    box(d, (0, 0, W, 72), WHITE)
    d.line((0, 71, W, 71), fill=LINE, width=2)
    brand(d, 33, 17)
    box(d, (1042, 14, 1320, 57), "#F4F7F9", radius=10, outline=LINE, width=2)
    txt(d, (1063, 24), "Search course...", 19, MUTED)
    txt(d, (1400, 24), "Resources", 20, MUTED, "semibold")

    box(d, (0, 72, 315, H), "#F8FAFB")
    d.line((315, 72, 315, H), fill=LINE, width=2)
    txt(d, (28, 108), "COURSE GUIDE", 17, MUTED, "bold")
    txt(d, (28, 158), "Overview", 21, TEXT, "semibold")
    txt(d, (28, 208), "Month 1: Foundations", 21, NAVY, "bold")
    txt(d, (52, 258), "S1  What AI Is", 19, TEXT)
    box(d, (16, 297, 296, 350), PALE, radius=9)
    txt(d, (52, 310), "S2  Tools & HIPAA Safety", 18, TEAL_DARK, "bold")
    txt(d, (52, 367), "S2  Data Classification", 19, TEXT)
    txt(d, (52, 419), "S3  Prompting Skills", 19, TEXT)
    txt(d, (52, 471), "S4  Daily DWIHN Work", 19, TEXT)
    d.line((29, 525, 286, 525), fill=LINE, width=2)
    txt(d, (28, 550), "Month 2: Applied AI", 21, NAVY, "bold")
    for k, t in enumerate(["S5–S7  Lumenore Impact", "S8  Genesys AI", "S9–S10  Decisions", "S11  Governance", "S12  Certification"]):
        txt(d, (52, 602 + k * 51), t, 19, TEXT)

    txt(d, (373, 109), "Foundations  /  Session 2  /  Module 2", 18, BLUE, "semibold")
    txt(d, (373, 163), "Approved Tools & HIPAA Safety", 40, NAVY, "bold")
    para(d, (373, 225), "Use the approved AI environment for the right task and data tier. This lesson gives you a repeatable decision process.", 823, 23, MUTED)
    d.line((373, 312, 1220, 312), fill=LINE, width=2)
    txt(d, (373, 342), "The safe-use decision", 30, NAVY, "bold")
    para(d, (373, 395), "Start with the information, not the tool. A familiar product may have several accounts and features with different permissions. The current DWIHN catalog is the authority for each permitted workflow.", 835, 22, TEXT)
    for i, (title, desc) in enumerate([
        ("Classify the information", "Identify the highest data tier present in the source."),
        ("Confirm the destination", "Find the exact approved tool, tenant, feature, and data allowance."),
        ("Review the result", "Check facts, scope, tone, and any disclosure before use."),
    ], 1):
        y = 526 + (i - 1) * 77
        icon_circle(d, 373, y, i, fill=TEAL_DARK)
        txt(d, (438, y - 1), title, 23, NAVY, "bold")
        txt(d, (438, y + 33), desc, 20, MUTED)
    box(d, (373, 778, 1220, 887), "#EAF5F4", radius=11)
    box(d, (373, 778, 380, 887), TEAL, radius=3)
    txt(d, (400, 794), "Practice prompt", 21, TEAL_DARK, "bold")
    para(d, (400, 828), "Which approved workflow could summarize a synthetic care note? Record the catalog entry and your review steps.", 780, 20, TEXT)
    txt(d, (373, 931), "← Previous: What AI Is", 18, BLUE, "semibold")
    txt(d, (967, 931), "Next: Data Classification →", 18, BLUE, "semibold")

    d.line((1250, 112, 1250, 879), fill=LINE, width=2)
    txt(d, (1278, 121), "ON THIS PAGE", 17, MUTED, "bold")
    for j, label in enumerate(["Learning outcome", "Safe-use decision", "Classify the data", "Confirm the tool", "Practice prompt", "Knowledge check"]):
        txt(d, (1278, 169 + j * 46), label, 18, TEAL_DARK if j == 1 else MUTED,
            "semibold" if j == 1 else "regular")
    return save(im, "03-vitepress-site.png")


def powerpoint():
    im = Image.new("RGB", (W, H), "#E4E8EC")
    d = ImageDraw.Draw(im)
    box(d, (0, 0, W, 65), "#F8FAFC")
    txt(d, (29, 17), "DWIHN AI Readiness  ·  Instructor Deck", 23, NAVY, "semibold")
    txt(d, (1436, 19), "Sample slide", 19, MUTED)
    box(d, (0, 65, 230, 840), "#F3F5F7")
    d.line((230, 65, 230, 840), fill="#CCD5DC", width=2)
    for i, label in enumerate(["Module 2", "Decision path", "Practice case", "Recap"], 1):
        y = 104 + (i - 1) * 169
        box(d, (28, y, 201, y + 104), NAVY if i != 2 else "#13385D", radius=4,
            outline=TEAL if i == 2 else None, width=4 if i == 2 else 1)
        txt(d, (46, y + 21), label, 17, WHITE, "semibold")
        if i == 2:
            d.line((46, y + 60, 181, y + 60), fill=TEAL, width=4)
        txt(d, (12, y + 41), str(i + 6), 15, MUTED, "semibold")

    # slide stage
    box(d, (265, 96, 1565, 828), "#B5C2CA", radius=2)
    box(d, (255, 86, 1555, 818), NAVY, radius=2)
    box(d, (255, 86, 1555, 99), TEAL)
    txt(d, (315, 141), "MODULE 2   •   APPROVED TOOLS & HIPAA SAFETY", 20, "#77D2D0", "bold")
    txt(d, (315, 198), "Which tool can see this data?", 48, WHITE, "bold")
    txt(d, (315, 277), "Use the same three checks for every AI task.", 27, "#CBD8E4")
    names = [("01", "CLASSIFY", "What is the highest data tier?"),
             ("02", "CHECK CATALOG", "Is this exact workflow allowed?"),
             ("03", "REVIEW", "Can a person verify the output?")]
    for i, (num, title, body) in enumerate(names):
        x = 315 + i * 409
        box(d, (x, 370, x + 370, 637), "#17365A", radius=18, outline="#3E6684", width=2)
        box(d, (x + 24, 394, x + 84, 454), TEAL, radius=30)
        txt(d, (x + 54, 424), num, 20, WHITE, "bold", anchor="mm")
        txt(d, (x + 24, 489), title, 25, WHITE, "bold")
        para(d, (x + 24, 536), body, 324, 23, "#CBD8E4")
        if i < 2:
            txt(d, (x + 380, 486), ">", 35, "#78CFCF", "bold")
    d.line((315, 691, 1494, 691), fill="#36506A", width=2)
    txt(d, (315, 723), "If any check fails, pause and ask the DWIHN owner.", 26, "#C9EEEA", "semibold")
    txt(d, (1417, 755), "08", 22, "#8EB2C7", "bold")

    box(d, (0, 841, W, H), WHITE)
    d.line((0, 841, W, 841), fill="#CBD5DD", width=2)
    txt(d, (28, 864), "SPEAKER NOTES", 18, MUTED, "bold")
    para(d, (28, 899), "Ask learners to classify the synthetic member-summary case before showing the answer. Confirm the catalog entry in the live DWIHN environment; do not assume a product is approved for PHI.", 1500, 21, TEXT)
    return save(im, "04-powerpoint-deck.png")


def overview(paths):
    scale = 0.66
    tw, th = int(W * scale), int(H * scale)
    gap, margin, label_h, head_h = 42, 54, 68, 142
    ow = margin * 2 + tw * 2 + gap
    oh = head_h + (th + label_h) * 2 + gap + margin
    im = Image.new("RGB", (ow, oh), "#EAF0F4")
    d = ImageDraw.Draw(im)
    txt(d, (margin, 34), "Choose how your DWIHN course feels", 47, NAVY, "bold")
    txt(d, (margin, 92), "Four visual previews using the same Module 2 lesson", 25, MUTED)
    labels = ["1  Interactive LMS / web", "2  PDF training manual",
              "3  VitePress course website", "4  PowerPoint trainer deck"]
    for i, (path, label) in enumerate(zip(paths, labels)):
        col, row = i % 2, i // 2
        x = margin + col * (tw + gap)
        y = head_h + row * (th + label_h + gap)
        preview = Image.open(path).resize((tw, th), Image.Resampling.LANCZOS)
        box(d, (x - 4, y - 4, x + tw + 4, y + th + 4), "#B9C7D0", radius=4)
        im.paste(preview, (x, y))
        txt(d, (x, y + th + 20), label, 28, NAVY, "semibold")
    return save(im, "00-all-formats-overview.png")


if __name__ == "__main__":
    paths = [lms(), pdf_manual(), vitepress(), powerpoint()]
    overview(paths)

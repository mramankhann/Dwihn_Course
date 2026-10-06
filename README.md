# DWIHN AI Readiness — VitePress course

This repository contains a complete 12-session, 10-module training course based on `DWIHN_AI_Training_Handbook.docx` and `Netlink_DWIHN_AI_Training_Proposal 6.pdf`. The handbook supplies forty detailed learning points, examples, labs, checks, and recaps; the proposal supplies the live session schedule. Each page in `docs/modules/` follows **topic introduction → four detailed points with examples → key takeaways → practical scenario and exercise**. The visual schedule spans **nine weeks**; Session 2 covers Modules 2 and 3, and Sessions 5–7 cover Module 6.

## Run locally

Node.js 22 or newer is required.

```powershell
npm install
npm run docs:dev
```

Open the local address printed by VitePress. To verify production output:

```powershell
npm run docs:build
npm run docs:preview
```

## Before live delivery

The course uses synthetic practice cases and labels policy or product details that require confirmation. DWIHN must supply the current approved AI tool catalog, four-tier data classification definitions and allowed destinations, Lumenore and Genesys access/features, incident contacts and process, and certificate criteria. The public website contains the assessment questions but no answer key. The instructor answer key is in `instructor/assessment-key.md` outside the published `docs` directory.

See [the course architecture](COURSE_ARCHITECTURE.md) and [instructor guide](docs/course/instructor-guide.md).

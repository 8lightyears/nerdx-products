# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.
This project is managed by the autonomous working system — see the organizer repo for full context.

## What this project does

nerdx-products is a **concept / research / asset-pipeline repo** for a "nerd shop"
product line — t-shirts first, later mugs, prints, and 3D-printable objects. Each
product is built around a real, checkable idea from science, history, alchemy,
space, sci-fi, or curiosity, so the product is a conversation-starter and the shop
feels like an expedition. The owner has a physics background, so equations,
diagrams, and "does this make scientific sense?" judgements are in scope.

The deliverable of a task is **never throwaway**: it is a theme analysis, a
concrete product concept, or a reusable generator — each with its sources written
down. There is no storefront and no single build here.

Full product vision: `docs/vision.md`. Working slogan: *"Shirts that start
interesting conversations."*

## What a task produces

One of:

1. **Theme-group analysis** — `themes/<theme>.md`: the family's scope, why it fits
   the shop's spirit, sub-ideas, sourced curiosities (URL + date checked), and
   notes on visualisation / automation.
2. **Concrete product concept** — `designs/<slug>/`:
   - `brief.md` — idea, copy/slogan, visual direction, references, **license**,
     sources, status.
   - `assets/` — generated/found artwork. Commit only small review samples
     (JPEG/PNG, long edge ≤ 1200 px, ≤ 300 KB); keep full-resolution print output
     out of the repo.
   - `generate/` — a script or an AI prompt that produces the visual, when
     automatable.
3. **Reusable generator** — `scripts/`: e.g. equation typesetting, fractal
   renderer, public-domain image fetcher. Each script carries a short run/verify
   note (dependencies + one example command).

## Commands

No global build or test suite — this is primarily a markdown + light-scripts repo.
"Running" a task means producing a theme/design/script deliverable. Scripts, when
added, document their own dependencies and an example invocation at the top of the
file. Research relies on web access (WebSearch / WebFetch) when the network policy
allows it; always cite sources with the date accessed.

## Architecture

```
ideas/inbox.md        raw idea queue; owner or agent appends, agents pull from top
themes/<theme>.md     per-theme-group analysis
designs/<slug>/       one folder per concrete product concept (brief.md, assets/, generate/)
scripts/              reusable generators
docs/
  vision.md           what this repo is for and how ideas flow
  plan.md             active backlog
  done.md             completed-work log (newest at top)
  taste.md            owner's likes/rejections — read before any visual work
  adr/                decisions about how this repo operates
```

Data flow: `ideas/inbox.md` → agent picks an idea → `themes/` analysis and/or
`designs/<slug>/` concept (+ any reusable `scripts/`) → idea struck from inbox,
logged in `docs/done.md`.

## License discipline (non-negotiable)

- Every external image or reference is recorded with **source URL, author, date,
  and license status**.
- Default safe pool: works first published **before 1927** (US public domain), and
  explicitly CC/PD-licensed material — verified, not assumed.
- Unknown or unclear license = unusable. Note why and move on.

## Session scope

Complete up to 2 tasks per session. Stop after 2 even if more remain. Start the
top queued idea; after finishing it, continue to the next if context allows. If a
task grows unexpectedly large (e.g. a theme needs far more research than one
session gives), leave it in the inbox with a note and move on, or create a
`blocked-critical` issue if a required resource is missing.

## Branch policy

Agents commit to whatever branch the harness provides (e.g. `claude/*`). At the end
of each session, merge the working branch into `main` and delete it — unless the
harness has pinned the session to a specific feature branch, in which case stay on
it and let the owner merge.

Owner creates release branches manually.

## Backlog population rules

Before queuing ideas in `docs/plan.md`, read `docs/done.md` in full. Any concept,
theme, or script that already appears in `done.md` must be excluded — never re-do
finished work unless the owner asks for a refresh.

## Working principles

**Think before producing. Surface tradeoffs. Don't assume.**

- State assumptions explicitly in the deliverable or commit message.
- Every factual / historical / market claim needs a source. No invented numbers.
  If a fact or a license can't be verified, say so.
- If multiple interpretations of an idea exist, pick the most concrete one — or
  note the alternatives.
- Be creative when adding ideas, but honest when judging them. A clear "this won't
  work, because…" is as valuable as a yes.

**Minimum prose / minimum code that does the job. Nothing speculative.**

- Skimmable beats long. No padding.
- Scripts: minimum code that solves the task; no abstractions for single use.

**Touch only what you must.**

- Before any visual work, read `docs/taste.md` — the owner's recorded preferences
  and rejections. When the owner rejects a concept or visual, append the rejection
  and its reason to `docs/taste.md`.
- Don't reshape adjacent files unless the task requires it.

## A task is done when

1. The deliverable exists: a `themes/<theme>.md`, a `designs/<slug>/` concept, or a
   `scripts/` generator — with sources and (for any asset) a recorded license.
2. The idea is struck from `ideas/inbox.md`.
3. `docs/plan.md` has the completed item removed.
4. `docs/done.md` has a new entry (newest at top).
5. If the task produced visual output, a small review sample is committed under the
   design's `assets/` (full-resolution output is never committed).

## Escalation rules

Create a `blocked-critical` issue and stop when:
- A requirement is unclear and no conservative default exists.
- An external resource (web access, API, credential) needed for the task is unavailable.
- An owner decision is contradicted by new information.

Create a `blocked-question` issue (but continue other tasks) when:
- The inbox is empty and the owner has given no new direction.

When the inbox is empty, seed 3–5 fresh agent-proposed ideas across the theme
groups (clearly marked) before raising a `blocked-question`, so the owner can
unblock by picking one.

When making a significant autonomous decision (e.g. structure, a new theme family,
a license judgement call), create an ADR in `docs/adr/`.

## Style

Use the caveman skill at intensity wenyan-ultra when thinking and reasoning.
Anything persisted to the repo (commit messages, concepts, docs, code) must be
plain English.

## Agent notes
<!-- Agents append discoveries and observations here. Owner promotes important ones to main sections during daily review. -->

- **Environment.** The owner works locally on **Windows**; autonomous agent and CI sessions run on **Linux**. Anything platform-specific — scripts, file paths, line endings, native runtimes — must work on both, and a green Linux run does not prove it works on the owner's Windows machine. Never pin a script or build to a single host OS.

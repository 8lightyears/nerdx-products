# nerdx-products

A product studio for a "nerd shop" — t-shirts (and later mugs, prints, 3D objects)
built around science, history, alchemy, space, sci-fi, and the kind of curiosities
that make someone stop and ask *"wait, what is that?"*.

The guiding line: **"Shirts that start interesting conversations."**

This is an autonomous-workflow repo managed by the organizer system. It produces
**concepts, research, copy, license-checked references, and generation scripts/prompts** —
the raw material a designer (or an automated pipeline) turns into a finished product.

- Full product vision: [`docs/vision.md`](docs/vision.md)
- How agents work here: [`CLAUDE.md`](CLAUDE.md)
- Raw idea queue: [`ideas/inbox.md`](ideas/inbox.md)

## Layout

```
ideas/      raw idea queue (owner or agent appends; agents pull from the top)
themes/     per-theme-group analysis: scope, sub-ideas, research, sources, automation notes
designs/    one folder per concrete product concept (the core deliverable)
scripts/    reusable generators (fractal renders, equation typesetting, PD-image fetch, ...)
docs/       vision, plan, done log, taste, ADRs
```

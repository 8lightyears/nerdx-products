# ADR 0001 — Repository structure: concept/research repo, not a storefront

Status: Accepted
Date: 2026-06-23

## Context

nerdx-products produces the *raw material* for a nerd-shop product line
(t-shirts first, later mugs/prints/3D): concepts, research, copy, license-checked
references, and generation scripts/prompts. It is not (yet) an e-commerce site,
and it is not a single code product. Work is partly research, partly creative
concepting, and partly small generators — similar in spirit to the
`easy-investment-opportunities-research` desk plus the `pi-numerology` script
toolset.

## Decision

Use a markdown + light-scripts layout:

```
ideas/inbox.md        raw idea queue; owner or agent appends, agents pull from top
themes/<theme>.md     per-theme-group analysis: scope, sub-ideas, sourced curiosities, automation notes
designs/<slug>/       one folder per concrete product concept
  brief.md            idea, copy/slogan, visual direction, references, license, sources, status
  assets/             generated/found artwork (review-size samples committed; full-res kept out of the repo)
  generate/           script or AI prompt that produces the visual, when automatable
scripts/              reusable generators (fractal render, equation typesetting, PD-image fetch, ...)
docs/                 vision, plan, done, taste, adr
```

Data flow: `ideas/inbox.md` -> agent picks an idea -> a `themes/` analysis and/or
a `designs/<slug>/` concept (and any reusable `scripts/`) -> idea struck from the
inbox, logged in `docs/done.md`.

## Consequences

- Most tasks are concept/research deliverables; some produce reusable scripts.
- No build/test suite by default. Scripts, when added, carry their own short
  run/verify notes and live under `scripts/`.
- A real storefront, if ever pursued, is a separate decision with its own ADR and
  owner sign-off.
- Full-resolution print output is never committed; only small review samples are.

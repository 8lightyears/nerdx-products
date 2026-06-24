# Vision — nerdx-products

## One line

**Shirts that start interesting conversations.**

A shop of wearable (and later printable / 3D-printable) curiosities for curious
people — where every product carries a real idea from science, history, alchemy,
space, or speculative thought, and the *shop itself feels like an expedition*: you
browse and you keep discovering things you did not know.

## Purpose

Most "nerd" merchandise is shallow — a formula slapped on a shirt with no story.
This project goes the other way: each product is backed by a genuine, checkable
idea and a short trail of sources, so the shirt is the *opening line* of a
conversation and the shop is a rabbit hole worth falling into.

The owner's background — a physics degree, programming, and an ongoing interest in
futurology and astronomy — is a deliberate asset: formulas, diagrams, and "does
this actually make scientific sense?" judgements are in scope and expected, not
avoided. We can ship things that are *correct*, not just decorative.

## What this repo produces

This is a **concept / research / asset-pipeline repo**, not a storefront and not
(yet) a heavy code product. Per task, the deliverable is one of:

1. **A theme-group analysis** (`themes/<theme>.md`) — a family of related product
   ideas, the reasoning for why they work, sub-ideas, sourced curiosities, and
   notes on how each could be visualised or automated.
2. **A concrete product concept** (`designs/<slug>/`) — a folder holding
   everything needed to actually make the design: the idea, the copy/slogan,
   the visual direction, reference images with license status, sources, and —
   where possible — a script or an AI prompt that generates the artwork.
3. **A reusable generator** (`scripts/`) — e.g. a fractal renderer, a LaTeX
   equation-typesetting helper, a public-domain image fetcher.

Everything researched gets **written down with its source**. No throwaway tabs:
if a fact, image, or reference was found, it lives in the repo with a URL and the
date it was checked.

## How we work — two layers

**Layer 1 — General proposals.** Theme groups, analysis, and discovery of new
themes. "Which families of ideas fit the shop's spirit, and why?"

**Layer 2 — Concrete products.** One folder per product, with whatever is useful
to reach a finished design: copy, visual plan, references, license notes, and
generation scripts/prompts. A product may also ship as a *setup* — the shirt plus
a curated trail (YouTube links, sources, the curiosity behind it) so the buyer
can keep exploring.

## The shop's spirit

- **Discovery, not decoration.** The visitor should feel they are *uncovering*
  something. Browsing is an adventure.
- **Real ideas.** Scientifically/historically defensible. We can render the
  equation correctly and explain it.
- **A trail to follow.** Each product can link out to the rabbit hole it came
  from.

Working slogan: **"Shirts that start interesting conversations."**

## Theme groups (initial map)

These are the seed families. The live, evolving queue is in `ideas/inbox.md`;
matured families get their own `themes/<theme>.md`.

### 1. Science
- **"17 equations that changed the world"** — a series, one per equation, each
  with a clean typeset equation and a one-line "why it changed the world."
  (Source: Business Insider summary of Ian Stewart's *17 Equations*.)
- **Emergence diagram** — a shirt built around an "emergence" concept diagram
  (inspired by a specific explainer video), with two foundational equations set
  small along the bottom. Needs original, nicely-made artwork.
- **Chemistry apparatus series** — illustrated, named pieces of lab glassware /
  instruments. Stretch goal: assemble *complete historical setups* that produced
  real discoveries.
- **"Attributes of a profession" series** — the iconic tools of each discipline
  (Chemistry: flasks, test tubes, ...; Physics: TBD; etc.).
- **"Heritage" series** — important historical diagrams / drawings, presented
  faithfully.
- **Interesting numbers & paradoxes** — curiosities from maths and physics, e.g.
  the decimal expansion of **1/89** encoding the Fibonacci sequence; famous
  paradoxes. Find/derive more.

### 2. ScienceX (adult / innuendo sub-line)
Real science paired with suggestive humour — a tasteful, double-entendre line.
- **Viscosity** — the word, a fitting visual, and the relevant equations.
- **A body-shaped curve** — a plotted function that approximates a silhouette.
Keep it clever and equation-driven rather than explicit.

### 3. Ecology
- **"Environment-saving backlog"** — the world's main problems framed as a
  developer/issue backlog.
- **"Save the world TODO" / "Optimal CO2 reduction plan"** — a checklist-style
  design, e.g.: build as much nuclear as possible; replace ~80% of coal plants
  with SMRs; build all the hydro/solar/wind we can; keep researching. Consistent
  icon set: nuclear, solar, wind, hydro, research.

### 4. "My wife is a Witch"
A humorous series on the half-joking suspicion that one's wife is quietly a witch.
- Supplement/vitamin gags — e.g. *"Honey, your vitamins"* / *"Darling, your
  supplements!"*, and the wary-husband variants ("I'm a little suspicious of the
  health supplements my wife keeps giving me").
- Hydration insistence — *"Darling, drink, you mustn't be dehydrated."*
- "My wife cooking dinner" / "my wife and mother-in-law cooking dinner."
- **"My wedding"** — a couple at the altar with the Eye of Sauron hovering over
  the spouse.

### 5. Public-domain space / sci-fi / inventions / forgotten beliefs
Work pre-1927 is in the US public domain, so it can be used freely. Mine it for
the shop's spirit.
- **H. G. Wells, *The Things that Live on Mars*** (Cosmopolitan, 1908) —
  illustrations by William Robinson Leigh; a striking PD source for both
  "life on Mars" art and the speculative-evolution angle.
- **Historical depictions of the Pleiades** across human cultures (look for CC /
  PD sources).
- **Speculative evolution** — PD illustrations of imagined alien life.
- **Alien species galleries** — alphabetical catalogues of aliens from sci-fi
  works as a reference pool (mind each item's license).

### 6. Patent drawings
Drawings from old invention patents — clean line art, strong nerd appeal.

### 7. Alchemy
Alchemical symbols and imagery; old (PD) plates; or AI-generated pieces from
crafted prompts.

### 8. Non-trivial historical curiosities
Genuinely obscure, conversation-starting facts (e.g. silphium; ancient dated
artefacts/stones). Each shirt = one little-known story.

### 9. "History of dreams"
Humanity's long-running ambitions, told as a series:
- **Dreams of robots** — e.g. the Mechanical Turk.
- **Dreams of immortality** — e.g. the philosopher's stone.
- **Dreams fulfilled** — flight; turning lead into gold (now literally possible).

> Not in scope: the **"cats as explorers"** AI-art series — the owner already has
> that one covered.

## Beyond t-shirts

The same idea engine should feed other non-trivial objects, ideally as *series*:
- **Mugs** and prints.
- **Collectable series** — planets / dwarf planets / eras of Earth.
- **3D prints** (later) — e.g. a 3D Mandelbrot/Mandelbulb object.

## Adjacent research direction — "interesting maps"

Run the same research engine toward non-trivial maps, each a product in itself:
castles of Europe; a map of dishes/cuisines; film-shooting locations; mysterious
places; monuments of technology (aircraft boneyards, old steam locomotives,
mines); the speculated location of Atlantis. Curiosity-first cartography.

## What we want to automate

The long-term aim is an idea-to-asset pipeline. Candidate automation:
- **Idea search within a theme** — expand a theme group with new, sourced ideas.
- **New-theme discovery** — surface whole new families that fit the spirit.
- **Visualisation planning** — for a given idea, plan the route to a final
  visual form (technique, tools, steps).
- **Generation** — scripts and AI prompts:
  - want a fractal shirt → a script that renders the fractal **plus** a clean
    typeset render of its equation;
  - want alchemy → crafted prompts for image AIs, **or** a search for suitably
    licensed (old / public-domain) source images.
- **Visual-quality evaluation** — research whether judging a design's visual
  appeal can be (partly) automated, and if so, build it.

## License discipline (non-negotiable)

- Every external image or reference is recorded with its **source URL, author,
  date, and license status**.
- Default safe pool: works first published **before 1927** (US public domain),
  and explicitly CC/PD-licensed material — verified, not assumed.
- When in doubt about a license, treat it as unusable and note why.

## What "good" looks like

- **A real idea, correctly rendered.** The equation is right; the history checks
  out; the source is cited.
- **Conversation-worthy.** Someone wearing it gets asked about it.
- **Production-ready hand-off.** A concept folder gives a designer (or a script)
  everything needed to produce the final artwork.
- **Legally clean.** Every asset's license is known and recorded.

## Non-goals

- Not a storefront / e-commerce platform (that may come later, with its own ADR).
- Not generic, story-less merch.
- No use of imagery whose license is unknown or unclear.
- The "cats as explorers" series is handled by the owner elsewhere.

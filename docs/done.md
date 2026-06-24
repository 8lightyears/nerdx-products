# Done log

Completed concepts, theme analyses, and scripts. Newest at top. One entry per
completed task. Agents must read this in full before queuing new work, to avoid
re-doing finished concepts.

## 2026-06-24 — ScienceX Viscosity design brief

- `designs/viscosity/brief.md`: full design concept for the Viscosity ScienceX
  shirt. Covers three slogan options (High Viscosity / Non-Newtonian / η>>0),
  verified equations in plain text and LaTeX (Newton's law of viscosity τ = η
  du/dy, kinematic viscosity, Reynolds number), visual direction (Hagen-Poiseuille
  parabolic flow profile as original code-generated line art), step-by-step
  generation path using existing `eq_render.py` + a 10-line Matplotlib snippet,
  and full license note (all equations are mathematical facts; all artwork is
  original output — no third-party license required). Source: Bird, Stewart,
  Lightfoot, *Transport Phenomena*, 2nd ed. (2002), §1.1.

## 2026-06-24 — Idea inbox seeded across all theme groups

Added 28 agent-proposed ideas to `ideas/inbox.md`, distributed across all existing
and five new theme groups:

- **ScienceX** — 3 additions: Rigid body, Specific heat capacity, Drag coefficient.
- **Patent drawings** — 4 additions: Tesla AC motor (1888), Wright brothers (1906),
  Bell telephone (1876), Babbage Difference Engine (PD plates).
- **Alchemy** — 3 additions: four transformation stages (Nigredo→Rubedo),
  Paracelsus tria prima, Robert Fludd macrocosm diagram (1617–1621, PD).
- **Historical curiosities** — 4 additions: Antikythera mechanism, Roman concrete
  recipe (Masic et al. 2023), Voynich manuscript (Yale Beinecke CC BY-NC 3.0),
  Damascus steel / carbon nanotubes (Reibold et al. 2006).
- **History of dreams** — 3 additions: Victorian electrical séances, dreams of a
  unified theory (Newton→Relativity→QM), perpetual-motion machines (PD pamphlets).
- **Thought experiments** (new group) — 5 items: Schrödinger's cat, Maxwell's
  demon, Einstein's elevator, Laplace's demon, Fermi paradox.
- **Logic and computation** (new group) — 5 items: Turing machine, Halting problem,
  Gödel's incompleteness, P≠NP, Church-Turing thesis.
- **Dead and defunct scientific theories** (new group) — 5 items: Luminiferous
  aether, Phlogiston, Ptolemaic geocentrism, Caloric theory, Spontaneous generation.
- **Space exploration history** (new group) — 4 items: Tsiolkovsky equation, Sputnik
  diagram, Voyager Golden Record cover, Apollo trajectory.
- **Mathematical structures** (new group) — 5 items: Penrose tiling, knot theory,
  Möbius strip/Klein bottle, tesseract projection, Ulam spiral.

## 2026-06-23 — Scripts and public-domain space theme

- `scripts/eq_render.py`: equation-to-PNG renderer using Matplotlib mathtext.
  Accepts any LaTeX/mathtext formula string, outputs transparent PNG at configurable
  DPI and font size (default: 300 DPI, fontsize 72, white text). No LaTeX install
  required. Dependency: `pip install matplotlib`.
- `scripts/fractal_render.py`: Mandelbrot and Julia set renderer using NumPy +
  Matplotlib. Smooth colouring (continuous escape time), configurable colourmap,
  resolution, max-iter, and Julia constant. Dependency: `pip install matplotlib numpy`.
- `themes/public-domain-space.md`: full Public-Domain Space / Sci-Fi theme analysis.
  Four catalogued asset pools with individual PD verification: (1) H.G. Wells / W.R.
  Leigh "Things That Live on Mars" four plates (Cosmopolitan 1908, LOC item
  cosmos000114 — US PD); (2) Trouvelot Astronomical Drawings 1882 (CC0, NYPL
  download); (3) Flammarion engraving ca. 1888 (US PD, Wikimedia); (4) LOC astronomy
  archive 15,000+ items. Visual direction, automation notes (ImageMagick commands for
  halftone removal / white-to-transparent), and t-shirt potential rated per asset.
  H.G. Wells inbox item struck.

## 2026-06-23 — Science family analysis + first design concept

- `themes/science.md`: full Science family analysis — 6 sub-ideas (17 equations
  shirt series, emergence diagram, chemistry apparatus, attributes of a profession,
  heritage series, interesting numbers & paradoxes); each with sourced curiosities,
  visual direction, automation notes, and license status. Key sources: Ian Stewart
  *In Pursuit of the Unknown* (2012); Philip Anderson "More is Different" (Science,
  1972); OU Math 1/89 Fibonacci curiosity; Wikipedia on Erlenmeyer/Büchner flask.
- `designs/17-equations-overview/brief.md`: concrete series framework and Maxwell's
  equations launch brief — equations in SI differential form, verified LaTeX source,
  layout spec, full series priority map, production plan through POD listing, license
  note. Recommended launch: Maxwell's equations (#11) for visual richness and
  physics-owner correctability.

## 2026-06-23 — Project onboarded

- Created the autonomous-workflow scaffolding: `docs/vision.md` (real English
  vision translated and structured from the owner's Polish draft), `CLAUDE.md`,
  docs skeleton (`plan.md`, `done.md`, `taste.md`, `adr/`), seeded
  `ideas/inbox.md`, and the `themes/` `designs/` `scripts/` layout.

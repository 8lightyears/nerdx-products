# Done log

## 2026-06-27 — Vesalius anatomy theme analysis + design brief; Philosophy theme analysis

- `themes/vesalius-anatomy.md`: full Human Anatomy / Vesalius theme group analysis — five
  sub-ideas: (1) Muscle Man series — ecorché figures posed as classical statues in Italian
  landscapes; Book II plates 3–14; Wellcome Collection CC BY 4.0 source; slogans "Every
  muscle, accounted for. Basel, 1543." and "Built like a Renaissance man."; ImageMagick
  contrast/invert pipeline. (2) Skeleton in a landscape — contemplative skeleton with shovel
  in graveyard; "Homo bulla est."; strong poster/print candidate. (3) "Galen Was Wrong" —
  typography-only two-column shirt listing specific Galen errors vs. Vesalius corrections
  (five-lobed liver → two; solid cardiac septum; single jawbone); zero illustration cost;
  slogan "1,300 years of authority. Overturned by looking." (4) Brain and ventricle plates
  from Book VII — "The Soul was here." / "Ventriculus quartus, 1543. No soul found."; more
  niche, better as a poster. (5) Frontispiece dissection theatre — "The first anatomy
  theatre. Padua, 1543."; complex composition, A2/A3 print only. Launch order: muscle man →
  Galen-corrections shirt → skeleton poster → brain ventricle. License: Wellcome Collection
  CC BY 4.0 (full commercial use, attribution required); EB Garamond SIL OFL 1.1.
- `designs/vesalius-muscle-man/brief.md`: concrete design brief for the launch product —
  Vesalius Book II plate 3 muscle-man figure on dark shirt; three copy options (minimal
  "Basel, 1543." / correction-story / anatomical-label annotation); ImageMagick processing
  pipeline documented; POD production steps listed.

- `themes/philosophy.md`: full Philosophy theme group analysis — six sub-ideas: (1) Cogito
  ergo sum (Descartes 1637, PD) — typography-only Latin or English; "I overthink, therefore
  I am" funny original variant; EB Garamond. (2) Plato's cave allegory (c. 375 BC, PD) —
  original side-view diagram (fire, object, shadow, prisoners); Matplotlib ~60 lines;
  slogan "You are looking at the shadows." (3) Zeno's paradoxes (c. 450 BC, PD) — Achilles
  and tortoise positions on a Matplotlib timeline; geometric series convergence visible;
  "Achilles never catches the tortoise. (He does.)"; resolved by Cauchy 1821. (4) Trolley
  problem (Foot 1967 — concept PD, cite only) — top-down track schematic; two-shirt set
  ("Pull the lever" / "Don't pull the lever") creates social engagement; "73% pull the
  lever" stats variant (Awad et al. 2018 Nature). (5) Occam's Razor (Ockham c. 1320, PD) —
  "Entia non sunt multiplicanda praeter necessitatem." in period type; funny modern variant
  "You probably just forgot to charge it." (6) Wittgenstein stretch goal — Tractatus §5.6
  in original German, for a logic/language sub-line. Launch order: trolley problem →
  cogito → Zeno → Plato's cave → Occam's Razor.

## 2026-06-27 — Fermi paradox + Gödel's incompleteness design briefs

- `designs/fermi-paradox/brief.md`: concrete design brief for the Fermi Paradox shirt/poster.
  Primary product: "WHERE IS EVERYBODY?" text-dominant on a procedural deep-space star field
  (Matplotlib, `generate/star_field.py`) or NASA Hubble PD image. Three copy options: stark
  one-liner (shirt), annotated data table (poster — Milky Way ~2×10¹¹ stars, detections: 0),
  attribution variant (mug). Proof-of-concept star field generator script included. Source:
  Jones (1985) LA-10311-MS (US gov PD). All original; NASA imagery PD.
- `designs/goedel-incompleteness/brief.md`: concrete design brief for the Gödel's
  Incompleteness shirt/poster. Four copy options: typography-only "This statement has no proof
  in this system. True. Unprovable. 1931." (highest viral potential, zero art cost); proof-
  structure diagram variant for poster (two contradiction arrows from the Gödel sentence);
  meta-label variant; minimal "True but unprovable. Gödel, 1931." mug variant. Uses existing
  `scripts/eq_render.py` for any mathematical expressions. Mathematical content is PD; English
  paraphrase is original wording. Sources: Gödel (1931), Monatshefte 38(1), 173–198.
- `designs/fermi-paradox/generate/star_field.py`: procedural star-field generator — ~3,000
  scattered stars with power-law brightness + 8 feature stars with Gaussian glow; 3300×3300 px
  at 300 DPI; optional text overlay commented out. Dependency: matplotlib + numpy.
- Seeded 5 fresh agent-proposed ideas in `ideas/inbox.md` (Vesalius anatomy theme, Philosophy
  theme, Chladni figures/acoustics theme, P≠NP brief, Laplace's demon brief).
- Inbox `[ ]` items (Pleiades/speculative-evolution/sci-fi alien and collectable series) noted
  as done on pinned branch `claude/friendly-babbage-n8qpqg` pending owner merge; no re-work.

## 2026-06-27 — Interesting maps theme group analysis

- `themes/interesting-maps.md`: full theme group analysis for the Interesting Maps
  product family. Covers five sub-ideas: (1) Castles of Europe — OpenStreetMap ODbL
  `historic=castle` data for a dot-density map; all of Europe in one high-density
  print; recommended title "Every Recorded Castle in Europe"; attribution in border.
  (2) World Cuisines Map — Natural Earth PD basemap + original cuisine-region annotation;
  Michelin distribution variant (no Michelin branding); differentiated by "where
  cuisines begin and end" framing. (3) Film Locations — real geographic facts only;
  LOTR New Zealand variant highest potential (150+ documented filming locations, all
  public facts); trademark caution: use real place names only. (4) Mysterious Places —
  deadpan cartographic treatment of Nazca Lines, Stonehenge, Bermuda Triangle (annotated
  "Not actually more dangerous" citing Lloyd's of London underwriting data), Crooked
  Forest, and 6 others; all Natural Earth PD basemap + original annotation layer.
  (5) Technology Monuments — AMARG boneyard (3,100+ aircraft), steam depots, open-pit
  mines, nuclear test sites, particle accelerators; all PD data (US gov, USGS, CERN
  institutional); recommended title "The Monuments We Actually Built"; zero competition
  in this exact framing. Launch order: Technology monuments → Mysterious places →
  Castles of Europe. All inbox items struck.

## 2026-06-27 — Mathematical structures theme group analysis

- `themes/mathematical-structures.md`: full theme group analysis for the Mathematical
  Structures family (agent-proposed). Covers five sub-ideas: (1) Penrose tiling (1974) —
  P3 rhombus aperiodic tiling; de Bruijn pentagrid method in ~50 lines of Python;
  no copyright on the mathematical concept; slogan "Aperiodic, 1974." (2) Knot theory
  diagrams — trefoil (3₁), figure-eight (4₁), unknot (0₁); parametric crossing diagrams
  in Matplotlib ~40 lines; history from Tait (1876) and Kelvin's vortex-atom hypothesis
  (1867) both PD. (3) Möbius strip / Klein bottle — parametric surface plots ~25–35
  lines; Möbius (1858/1868 PD), Klein (1882 PD); recommended launch piece is the
  Möbius strip; slogan "One side. No boundary." (4) Tesseract / hypercube projection —
  Schlegel diagram from 16 ±1 vertices, 4D→3D→2D projection; Hinton 1888 (PD);
  slogan "The fourth dimension, flattened for your convenience." — avoid any Dalí
  painting reference (copyrighted). (5) Ulam spiral — primes in a square spiral;
  Ulam, Stein, Wells LA-3966 1964 (US gov, PD); ~25 lines using numpy sieve; slogan
  "Stanislaw Ulam, bored in a meeting, 1963." Launch order: Ulam spiral →
  tesseract → Penrose tiling → knot theory → Möbius strip. All inbox items struck.

## 2026-06-26 — Space exploration history theme group analysis

- `themes/space-exploration-history.md`: full theme group analysis for the Space
  Exploration History family (agent-proposed). Covers four sub-ideas: (1) Tsiolkovsky
  rocket equation (1903) — Δv = v_e · ln(m₀/m_f); "The Earth is the cradle of
  humanity, but one cannot live in the cradle forever." (Tsiolkovsky letter to
  Vorobiev, 1911, PD); equation PD mathematical fact; original Matplotlib arc diagram.
  (2) Sputnik (1957) — original schematic of PS-1: 58.5 cm aluminium sphere, four
  antennas, 83.6 kg, 96.2-minute orbit; "October 4, 1957 — the sky changed"; Soviet
  technical specs are public knowledge; Matplotlib ~20-line diagram. (3) Voyager
  Golden Record (1977) — pulsar map (14 radial lines, binary distances), hydrogen
  21-cm hyperfine transition, human silhouettes; NASA PIA01481 PD (US gov work);
  recreating from scientific content avoids any Lomberg artwork attribution issues.
  (4) Apollo lunar trajectory (1969) — TLI → coast → LOI → PDI → TEI phases;
  from NASA Apollo 11 Mission Report MSC-00171 (PD US gov); "July 20, 1969 —
  1,079,840 km."; Matplotlib Bezier arc ~30 lines. Recommended launch: Tsiolkovsky
  → Voyager → Sputnik → Apollo. All inbox items struck.

## 2026-06-26 — Logic and computation theme group analysis

- `themes/logic-and-computation.md`: full theme group analysis for the Logic and
  Computation family (agent-proposed). Covers five sub-ideas: (1) Turing machine
  (1936) — tape + read-write head + state table diagram; "Universal Computation,
  1936."; source Turing 1937 PLMS paper (EU PD 2025, US PD status uncertain but
  concept uncopyrightable); Matplotlib tape + table. (2) Halting problem (1936) —
  pseudocode paradox: `if halts(D, D): loop_forever()`; "Undecidable since 1936.";
  original diagram or `eq_render.py` monospace block. (3) Gödel's incompleteness
  (1931) — "This statement cannot be proved in this system." self-referential
  typography; "True but unprovable, 1931."; Gödel died 1978 (EU PD 2049) — use
  the concept (mathematical fact) not translated text; highest viral potential of the
  group; zero illustration cost for the typography-only version. (4) P ≠ NP (1971,
  unsolved) — bold "P ≠ NP" + "$1,000,000 prize unclaimed" badge (original design,
  not CMI logo which is trademarked); Cook 1971 STOC paper in copyright but
  conjecture is PD mathematical fact. (5) Church-Turing thesis (1936) — lambda
  symbol λ alongside a Turing tape, "≡", "Two routes, one destination."; Church
  1936 *American Journal of Mathematics* + Turing 1937 same paper. Recommended
  launch: Gödel → P≠NP → Turing machine → Halting problem → Church-Turing. All
  inbox items struck.

## 2026-06-25 — History of dreams theme group analysis

- `themes/history-of-dreams.md`: full theme group analysis for the History of Dreams
  family. Covers four sub-ideas: (1) Mechanical Turk (von Kempelen 1770) — chess-playing
  "automaton" with a human chess master hidden inside; PD cross-section engraving from
  Racknitz 1789; punchline: "first AI, powered by a human." (2) Victorian electrical
  séances — the telegraph (1844) and the Fox sisters' séances (1848) emerged
  simultaneously; newspapers called it "the spiritual telegraph"; Edison 1920 *Scientific
  American* interview; mock telegram format as the design. (3) Theory of everything —
  Newton (1687) → Maxwell (1865) → Einstein (1915) → Standard Model (1970s) → String
  theory (1980s–, beta); software patch-note format showing each version as STABLE except
  v5.0 in beta; all equations PD mathematical facts. (4) Perpetual motion machines —
  Villard de Honnecourt overbalanced wheel sketch c. 1230 (BnF MS Fr 19093, Gallica
  PD-old-100); mock patent "pending since 1230"; Second Law (Clausius 1850) as the
  resolution. Recommended launch: perpetual motion (typography-only, zero illustration
  cost) then theory-of-everything (patch-note format). Cross-theme links to dead-theories.md.

## 2026-06-25 — Non-trivial historical curiosities theme group analysis

- `themes/historical-curiosities.md`: full theme group analysis for the Non-Trivial
  Historical Curiosities family. Covers five sub-ideas: (1) Silphium — only plant
  consumed to extinction; Cyrenean coin silhouette (PD); mock expiry-label variant.
  (2) Antikythera mechanism — 37-gear analogue computer c. 100 BC; gear-train diagram
  from Freeth et al. 2021 *Scientific Reports* (CC BY 4.0); de Solla Price 1974 (PD);
  do NOT use Athens museum photographs. (3) Roman concrete — pozzolan + seawater →
  tobermorite crystals; Masic et al. 2023 *Science Advances*; Vitruvius *De Architectura*
  Book II (PD); ingredient-label format is zero illustration cost. (4) Voynich manuscript
  — Yale Beinecke CC BY-NC 3.0 is NOT commercially usable; use only original
  line-art interpretation of the style. (5) Damascus steel — Reibold et al. 2006 *Nature*
  multi-wall carbon nanotubes in medieval blade; wavy damask pattern + caption; original
  schematic only, no Nature micrograph. Recommended launch: Antikythera (CC BY 4.0
  source) then Roman concrete (label format, zero illustration cost).

Completed concepts, theme analyses, and scripts. Newest at top. One entry per
completed task. Agents must read this in full before queuing new work, to avoid
re-doing finished concepts.

## 2026-06-25 — Dead and defunct scientific theories theme group analysis

- `themes/dead-theories.md`: full theme group analysis for the Dead and Defunct
  Scientific Theories family. Covers five sub-ideas: (1) Luminiferous aether —
  Michelson-Morley experiment (1887) null result; interferometer diagram from the
  original paper (PD); shirt copy "Null result, 1887." (2) Phlogiston theory —
  Stahl 1703, replaced by Lavoisier's oxygen theory 1789; Lavoisier's *Traité
  Élémentaire* apparatus diagrams (PD, Archive.org). (3) Ptolemaic geocentric model —
  Andreas Cellarius *Harmonia Macrocosmica* (1661) "Planisphaerii Ptolemaici
  Scenographia" plate; PD-old-100 on Wikimedia; spectacular as a full-chest shirt or
  print. (4) Caloric theory — heat as a weightless fluid; Lavoisier included it in his
  element table 1789; killed by Rumford 1798 and Joule 1843; *Phil. Trans.* paper PD.
  (5) Spontaneous generation — Pasteur swan-neck flask experiment (1859); *omne vivum
  ex vivo* as the shirt motto; Pasteur 1861 paper on Gallica, PD. All sources cited
  with URL and access date; all PD verified. Recommended launch: Ptolemaic diagram
  (visually spectacular, no redrawing needed), then swan-neck flask (simplest redraw).

## 2026-06-25 — Alchemy theme group analysis

- `themes/alchemy.md`: full theme group analysis for the Alchemy family. Covers four
  sub-ideas: (1) General alchemical symbols/emblems — planetary-metal glyphs, four
  classical-element triangles, Paracelsian symbols; *Atalanta Fugiens* (Maier, 1618)
  on Archive.org as source for PD engravings; clean vector reconstruction requires no
  license. (2) Four stages of transformation (Magnum Opus) — Nigredo → Albedo →
  Citrinitas → Rubedo with chemical correlates (CuO, lead oxide reduction, cinnabar);
  *Splendor Solis* (Trismosin, c. 1582) on Wikimedia (PD); or pure Matplotlib colour
  gradient, no PD dependency. (3) Tria Prima — Paracelsus (1493–1541): Mercury/Spirit,
  Sulfur/Soul, Salt/Body; *Philosophia Reformata* (Mylius, 1622) on Archive.org (PD);
  Unicode alchemical glyphs (U+1F700–U+1F77F) usable in vector form. (4) Robert Fludd
  macrocosm diagram — *Utriusque Cosmi* (1617) "Integra Naturae" plate; on Archive.org
  and Wikimedia Commons (PD-old-100); best as print or large mug. All PD sources
  verified with URL and access date. Recommended launch: Tria Prima triangle (simplest
  to produce), then Magnum Opus gradient (fully original, zero license concern).

## 2026-06-25 — Thought experiments theme group analysis

- `themes/thought-experiments.md`: full theme group analysis for the Thought Experiments
  family (agent-proposed). Covers five sub-ideas: (1) Schrödinger's cat — wavefunction
  superposition `|ψ⟩ = (1/√2)(|alive⟩ + |dead⟩)`, original diagram; note that the cat
  sub-niche is saturated so the differentiator is the equation and serious tone.
  (2) Maxwell's demon — molecule-sorting imp between hot and cold chambers; broken by
  Landauer's principle (1961); original diagram. (3) Einstein's elevator — two-panel
  comparison (acceleration vs. gravity) illustrating the equivalence principle (1907);
  original diagram. (4) Laplace's demon — clockwork universe diagram + 1814 quote; broken
  by Heisenberg (1927) and Lorenz (1963); original diagram. (5) Fermi paradox — text-
  dominant design "WHERE IS EVERYBODY?" on a star field (NASA PD or procedurally
  generated); cite Jones (1985), LA-10311-MS (US gov work, PD). All concepts PD; all
  visuals original or NASA PD. Recommended launch: Fermi paradox (lowest art cost,
  highest visual impact) and Laplace's demon (least crowded niche).

## 2026-06-25 — Patent drawings theme group analysis

- `themes/patent-drawings.md`: full theme group analysis for the Patent Drawings family.
  Covers five sub-ideas: (1) General concept — old invention drawings as a shirt series
  (USPTO/Google Patents as source, all PD). (2) Tesla polyphase AC motor, US Patent
  381,968 (1888) — PD; rotating-field frequency and synchronous-speed equations added;
  three slogan options. (3) Wright brothers flying machine, US Patent 821,393 (1906) —
  PD; "They built this in a bicycle shop." (4) Alexander Graham Bell telephone, US Patent
  174,465 (1876) — PD; 2-hour filing advantage over Gray; two variants (engineering /
  ironic). (5) Babbage's Difference Engine (1822–1834 publications, PD) — do not use
  Science Museum photos (CC BY-NC-SA); use only 19th-century originals from Internet
  Archive. All US patents are US government works, PD on publication. ImageMagick cleanup
  pipeline documented. Recommended launch: Tesla motor (dense drawing, equation hook,
  popular STEM figure) then Bell telephone (two-hours story is uniquely compelling).

## 2026-06-24 — "My wife is a Witch" theme group analysis

- `themes/my-wife-is-a-witch.md`: full theme group analysis for the relationship-humor
  sub-line. Covers four sub-ideas: (1) supplement/vitamin gags with real biochemistry
  formulas (PubChem, PD); (2) hydration insistence with H₂O physical constants (NIST);
  (3) wife cooking dinner in two variants — PD alchemical plates relabelled as recipe
  steps (Libavius 1606/Van Helmont 1648 via HathiTrust, PD) and a "periodic table of
  dinner ingredients" using real NIST elemental data; (4) "My wedding" dark-eye concept
  with explicit copyright warning against using Eye of Sauron (Tolkien Estate/New Line)
  and two safe alternatives (original dark eye or caption-only). Shop-fit assessment:
  supplements + periodic-table variants are strong (nerdy hook + real data); wedding
  dark-eye variant is high-risk.

## 2026-06-24 — Ecology theme group analysis

- `themes/ecology.md`: full theme group analysis for the Ecology family. Covers three
  concepts: (1) "Environment-saving backlog" — world crises as a GitHub Issues board
  (dark-theme, status labels); includes sourced environmental claims (NOAA ocean
  acidification, Ceballos et al. sixth extinction, WMO ozone recovery, IEA CO₂ gap);
  "Ozone layer — Closed ✓" as the punchline. (2) "Optimal CO₂ reduction plan" — a
  sourced checklist of decarbonisation actions (IPCC AR6, IRENA 2023, IEA NZE 2021,
  World Nuclear Association); nuclear + renewables as the correct answer, in checkmark
  form. (3) Three further sub-ideas (1.5°C progress bar, planetary boundaries radar
  chart, carbon-footprint grocery receipt). All content is original text; all claims
  are citable facts; no third-party imagery required.

## 2026-06-24 — ScienceX Drag Coefficient design brief

- `designs/drag-coefficient/brief.md`: full design concept for the Drag Coefficient
  ScienceX shirt. Concept: drag force `F_D = ½ρv²C_D A` — drag is literally a function
  of shape and velocity. Three slogan options (sentence + equation / equation + defiant
  punchline / longer humorous tagline). Optional Matplotlib shape-comparison diagram
  (sphere C_D ≈ 0.47 vs. streamlined body C_D ≈ 0.04). Verified equations from Munson
  et al. *Fundamentals of Fluid Mechanics* (formula PD, Rayleigh 1876). All visual output
  is original code-generated artwork; no third-party assets required.

## 2026-06-24 — ScienceX Specific Heat Capacity design brief

- `designs/specific-heat-capacity/brief.md`: full design concept for the Specific Heat
  Capacity ScienceX shirt. Concept: `c = Q / mΔT` — "It takes a lot of energy to get me
  excited." Three slogan options (human-readable sentence + equation / equation-first /
  mock certification badge). Optional material comparison bar chart (water vs. Al vs. Fe).
  Verified equations from Cengel & Boles *Thermodynamics* (formula PD, measured physical
  constants). All visual output is original code-generated artwork; no third-party assets
  required.

## 2026-06-24 — ScienceX Rigid Body design brief

- `designs/rigid-body/brief.md`: full design concept for the Rigid Body ScienceX
  shirt. Covers three slogan options (τ = Iα + "All forces accounted for" /
  definition-first with I = ∫r²dm / minimal τ = r × F), verified equations
  (Newton 1687, Euler 1765 — both PD), Matplotlib free-body diagram generation
  script (~30 lines: block + force vectors in distinct colours + torque arc),
  full license note (all equations mathematical facts; diagram is original code
  output). ScienceX plausible deniability: "rigid body" is a verbatim classical
  mechanics term.

## 2026-06-24 — ScienceX Body-Shaped Curve design brief

- `designs/body-shaped-curve/brief.md`: full design concept for the Body-Shaped
  Curve ScienceX shirt. Concept: any closed curve — including a body silhouette —
  can be represented as a sum of rotating circles (complex Fourier series,
  Fourier 1822, PD). Three slogan options ("Every figure is a sum of circles" /
  "Convergent by design" / coefficient equation). Verified equations: z(t) =
  Σ cₙ e^(2πint) and its inverse. Matplotlib generation script (~25 lines):
  uses DFT of a polar hourglass curve r = 1 + 0.4·cos(2θ) to produce an N=5
  epicycle approximation; adjust amplitude to control waist prominence. Full
  license note (Fourier theory PD; diagram is original code output).

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

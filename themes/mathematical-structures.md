# Mathematical Structures

Theme group for nerdx-products. Covers visual mathematics that doubles as wall art
or shirt design: patterns, knots, surfaces, projections, and number sequences.

All sub-ideas use PD mathematical concepts and original artwork (code-generated or
line art). No third-party images required.

---

## Why this fits the shop

Mathematics produces some of the most visually striking patterns known to science.
Penrose tilings, knot diagrams, and hypercube projections are things that mathematicians
love and non-mathematicians find genuinely beautiful without knowing why — which is
exactly the conversation-starter sweet spot. The owner's physics background means these
can be vetted for correctness.

---

## Sub-ideas

### 1. Penrose Tiling

**Concept.** An aperiodic tiling of the plane using two shapes (kite-and-dart for P2, or
two rhombi for P3). No translational symmetry — the pattern never repeats — yet it covers
the plane completely and has 5-fold rotational symmetry. Mathematically proven by Roger
Penrose (1974). Shirt copy: "No two tiles agree on the neighbourhood. Yet the whole thing
fits." or simply the equation-free visual with "Aperiodic, 1974."

**Visual direction.** Large circular or rectangular patch of P3 rhombus tiling in two
contrasting colours (e.g. black and white, or dark blue and gold). The 5-fold symmetry
is most visible from the centre. A Matplotlib script can tile a finite window and export
a high-resolution SVG or PNG.

**Generation.** Matplotlib + numpy — the de Bruijn pentagrid method produces exact
vertex coordinates in ~50 lines; no manual drawing required. Colourmap: simple two-
colour fill; no gradient needed.

**Sources / license.** Penrose's original paper: R. Penrose, "The Role of Aesthetics in
Pure and Applied Mathematical Research," *Bulletin of the Institute of Mathematics and
Its Applications* 10 (1974): 266–271. The mathematical concept (aperiodic tiling) is
not copyrightable. The specific P2/P3 terminology was trademarked by Pentaplex Ltd but
only for commercial tile products, not for mathematical exposition, shirts, or art.
All visual output is original code-generated artwork.

**License risk.** LOW. The tiling is a mathematical fact; the visual is original code
output.

**T-shirt potential.** HIGH. Visually striking, conversation-starting, nerd-credible.
Likely to attract mathematics, physics, and architecture communities.

**Recommended slogan options.**
- (A) "Aperiodic, 1974." (minimalist; equation-free)
- (B) "No repeating neighbourhood. Perfect fit." (accessible)
- (C) Full label: name + P3 rhombus tiling + Penrose 1974 citation block

---

### 2. Knot Theory Diagrams

**Concept.** Mathematical knots are closed curves in 3D space classified by their
crossing number. The trefoil (3₁), figure-eight (4₁), and unknot (0₁) are the three
simplest. Knot theory has been systematically studied since Tait (1860s) and Kelvin's
vortex-atom hypothesis. Shirt copy: "Classified since 1867. Still tangled." or "The
unknot: a circle in disguise."

**Visual direction.** Clean black line-art diagrams of the trefoil knot and figure-eight
knot, drawn as over-under crossing diagrams (standard knot projections). Arranged in a
series of three (unknot, trefoil, figure-eight) or as a standalone trefoil. Could be
combined with a table showing the knot invariant (Jones polynomial value, crossing
number).

**Generation.** Knot diagrams can be drawn parametrically from (x(t), y(t)) Lissajous-
style curves with crossings explicitly calculated and gaps inserted for the "under"
strand. Matplotlib in ~40 lines; the trefoil is the canonical test case.

**Sources / license.** Peter Guthrie Tait, "On Knots," *Trans. RSE* 28 (1876–1877):
145–190 (PD). William Thomson (Kelvin), "On Vortex Atoms," *Phil. Mag.* 34 (1867): 15–24
(PD). The mathematical classification is PD fact; all diagrams are original code output.

**License risk.** LOW. All mathematical content is PD; diagrams are original.

**T-shirt potential.** HIGH. Clean, geometric, conversation-starting. Appeals to
mathematics, topology, and climbing/outdoor communities ("knot" pun potential).

**Recommended slogan options.**
- (A) "Every knot is a closed curve. Not every closed curve is unknotted." (precise)
- (B) "Classified since 1867. Still tangled." (historical hook)
- (C) "The unknot: a circle in disguise." (accessible, ScienceX tone)

---

### 3. Möbius Strip / Klein Bottle

**Concept.** The Möbius strip (one-sided, one-edged surface) and the Klein bottle
(closed non-orientable surface without boundary) are the canonical non-orientable
surfaces. Both were described in 1882 (Möbius died 1868; Klein's bottle dates to 1882).
Shirt copy: "One side. No boundary. Still a strip." or "A bottle with no inside."

**Visual direction.** Two options:
- **(A) Möbius strip**: clean 3D-rendered wireframe or a flat unfolding diagram showing
  the half-twist. Parametric: x(u,v) = (1+v/2·cos(u/2))·cos(u), etc. Very recognisable.
- **(B) Klein bottle**: line-art schematic showing the self-intersection in 3D
  (a Klein bottle can only be embedded in 4D without self-intersection; in 3D it has a
  tube passing through itself). Less recognisable but intriguing.
- **(C) Pair**: both on one shirt — "The Möbius strip with a friend."

The Möbius strip is more iconic; recommended for the launch piece.

**Generation.** Matplotlib parametric surface plot with wireframe rendering — ~25 lines
for the Möbius strip, ~35 for the Klein bottle. Export as transparent PNG or vector SVG.

**Sources / license.** August Ferdinand Möbius, posthumous publication of surfaces, 1868
(PD). Felix Klein, *Über Riemanns Theorie der algebraischen Funktionen*, 1882 (PD). All
mathematical content is PD fact; diagrams are original code output.

**License risk.** LOW.

**T-shirt potential.** MEDIUM–HIGH. Möbius strip is widely recognisable; Klein bottle is
a nerd classic. The glass Klein bottle sold by Acme Klein Bottle (glassblowing) shows
there is a commercial market for this object.

**Recommended slogan options.**
- (A) "One side. No boundary." (clean, precise)
- (B) "A bottle with no inside." (paradox hook)
- (C) "Non-orientable since 1858." (historical; Möbius's private notes date to 1858)

---

### 4. Hypercube (Tesseract) Projection

**Concept.** A hypercube (4D analogue of a cube) cannot be perceived directly in 3D,
but its 3D shadow (Schlegel diagram) shows 8 cubical cells nested and connected. The
word "tesseract" was coined by Charles Howard Hinton in 1888. Salvador Dalí painted the
"Corpus Hypercubus" (1954) as an unfolded tesseract (this specific painting is under
copyright; do not reference it — use the mathematical concept only). Shirt copy: "The
fourth dimension, flattened for your convenience." or "8 cells. 24 faces. 0 ways to see
it whole."

**Visual direction.** Wireframe Schlegel projection of the hypercube: one cube visible
at the centre, connected to 7 surrounding cubes by visible edges, with all 32 edges
drawn. Clean black-on-white or white-on-black line art. Or: an isometric projection
rotating the tesseract in 4D (animated GIF for social media; static frame for print).

**Generation.** The 16 vertices of a hypercube are all ±1 in four coordinates. Project
onto 3D using a 4D→3D rotation matrix, then project to 2D. ~30 lines of numpy/Matplotlib.

**Sources / license.** C. H. Hinton, "What is the Fourth Dimension?," *The Scientific
Romances* (1888) (PD). Mathematical content (hypercube vertices, edges) is PD fact.
Dalí's painting is copyrighted — do not use it or reference it by name. The Schlegel
diagram is a PD mathematical construction.

**License risk.** LOW (if Dalí painting is not referenced or reproduced).

**T-shirt potential.** HIGH. One of the most iconic mathematical visuals in popular
culture. Appeals to mathematics, physics, and sci-fi communities. Strong social media
potential ("the tesseract from Avengers" is a different thing, but the word is familiar).

**Recommended slogan options.**
- (A) "The fourth dimension, flattened for your convenience." (recommended; playful)
- (B) "8 cells. 24 faces. 32 edges. 0 ways to see it whole."
- (C) "Hinton's tesseract, 1888." (historical; no Dalí association)

---

### 5. Ulam Spiral

**Concept.** In 1963, Stanislaw Ulam was doodling during a boring meeting, arranged
integers in a spiral, and circled the primes. Diagonal lines appeared — a completely
unexpected pattern suggesting that primes prefer certain polynomial paths. The observation
was published by Ulam, Stein, and Wells at Los Alamos (LA-3966, 1964). Shirt copy:
"Stanislaw Ulam, bored in a meeting, 1963. The primes are hiding something."

**Visual direction.** The classic Ulam spiral: integers arranged outward in a square
spiral, primes marked as black dots on white (or white on black). At sufficient resolution
(501×501 or larger), the diagonals are clearly visible. A cropped square patch at
1200×1200 resolution makes an excellent print. No annotation required — the visual is
self-explanatory to a mathematician and mysterious to everyone else.

**Generation.** ~25 lines of Python/numpy: generate the spiral mapping, mark primes
using a sieve of Eratosthenes, render with Matplotlib imshow. The Los Alamos LA-3966
report even includes the original Fortran code (now PD).

**Sources / license.** S. M. Ulam, M. L. Stein, and M. B. Wells, *Visual display of
some properties of the distribution of primes* (Los Alamos Scientific Laboratory,
LA-3966, 1964) — US government work, PD. The pattern itself is a mathematical observation;
all visual output is original code-generated artwork.

**License risk.** NONE. US government work; mathematical fact; original artwork.

**T-shirt potential.** HIGH. One of the most beautiful visual facts in number theory.
Beloved by the mathematics community; the story (bored meeting doodle) is irresistible.

**Recommended slogan options.**
- (A) "Stanislaw Ulam, bored in a meeting, 1963." (story-first; recommended)
- (B) "The primes are hiding something." (mysterious; works alone or with the visual)
- (C) "Not random. Not regular. Prime." (clean three-line format)

---

## Launch recommendations

| Priority | Sub-idea | Reason |
|---|---|---|
| 1 | Ulam spiral | Most visually arresting; backstory (bored meeting) is uniquely compelling; code ~25 lines |
| 2 | Tesseract projection | Culturally familiar word; clean wireframe; 4D punchline writes itself |
| 3 | Penrose tiling | Visually spectacular but requires the de Bruijn method (~50 lines); high ceiling |
| 4 | Knot theory | Clean diagrams; series potential (trefoil + figure-eight + unknot) |
| 5 | Möbius strip | Recognisable but the niche is somewhat saturated; Klein bottle is more distinctive |

---

## Cross-theme connections

- **Penrose tiling** ↔ `themes/space-exploration-history.md` — quasi-crystals (Shechtman 1982) have Penrose-like 5-fold symmetry; shared "structure that shouldn't be possible" narrative.
- **Knot theory** ↔ `themes/dead-theories.md` — Kelvin's vortex-atom hypothesis (knots as atoms) is a dead theory with a beautiful diagram.
- **Tesseract** ↔ `themes/thought-experiments.md` — 4D space as a thought experiment; Hinton's attempts to visualise the fourth dimension.
- **Ulam spiral** ↔ `themes/science.md` — the Riemann hypothesis and prime distribution are part of the unresolved 17-equations landscape.

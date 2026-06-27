# Theme group: Science

Analysed: 2026-06-23.

## Scope

Products built around real mathematical and scientific ideas — equations, diagrams,
proofs, and concepts that are both correct and genuinely surprising. The owner's
physics background is a deliberate advantage here: we can ship a shirt where the
equation is right, the explanation is accurate, and a physicist will approve of it.

The Science family is the core of the shop: every other theme group draws on it or
contrasts with it.

## Why this fits the shop's spirit

Science is the original conversation starter. The best science shirts feel like
a riddle on a stranger's chest — you see the formula, you half-recognise it, you
have to ask. The goal is never decoration: every product in this family should make
the buyer want to explain it to someone else.

Sub-goals:
- Correct equations, correctly typeset — no approximations, no decorative nonsense.
- One-line explanations that make the idea land without a textbook.
- Sourced curiosities that can be verified by the curious buyer.

## Sub-ideas

### 1. "17 equations that changed the world" — shirt series

**Concept.** One shirt per equation from Ian Stewart's *In Pursuit of the Unknown:
17 Equations That Changed the World* (2012, Basic Books). Each shirt shows the
equation typeset cleanly, its name, and a single sentence on why it mattered.

**The 17 equations:**

| # | Name | Key notation |
|---|------|-------------|
| 1 | Pythagoras's theorem | a² + b² = c² |
| 2 | Logarithms | log(xy) = log(x) + log(y) |
| 3 | Calculus | df/dt = lim(h→0) [f(t+h) − f(t)] / h |
| 4 | Newton's law of gravity | F = G·m₁m₂ / r² |
| 5 | The square root of minus one | i² = −1 |
| 6 | Euler's formula for polyhedra | F − E + V = 2 |
| 7 | Normal distribution | Φ(x) = (1/√(2π)) · e^(−x²/2) |
| 8 | Wave equation | ∂²u/∂t² = c² · ∂²u/∂x² |
| 9 | Fourier transform | f̂(ξ) = ∫ f(x) · e^(−2πixξ) dx |
| 10 | Navier-Stokes | ρ(∂v/∂t + v·∇v) = −∇p + μ∇²v + f |
| 11 | Maxwell's equations | ∇·E = ρ/ε₀ ; ∇×B = μ₀J + μ₀ε₀∂E/∂t ; … |
| 12 | Second law of thermodynamics | dS ≥ 0 |
| 13 | Relativity | E = mc² |
| 14 | Schrödinger equation | iℏ ∂Ψ/∂t = ĤΨ |
| 15 | Information theory | H = −Σ pᵢ log₂(pᵢ) |
| 16 | Chaos theory | xₙ₊₁ = k·xₙ(1 − xₙ) |
| 17 | Black-Scholes | ∂V/∂t + ½σ²S²∂²V/∂S² + rS·∂V/∂S − rV = 0 |

**Recommended launch shirt:** Maxwell's equations (#11) — four lines that unified
electricity, magnetism, and light; visually rich; physics-owner advantage. See
`designs/17-equations-overview/` for the full concept brief.

**Source:** Ian Stewart, *In Pursuit of the Unknown* (2012, Basic Books).
Wikipedia summary: https://en.wikipedia.org/wiki/In_Pursuit_of_the_Unknown
(checked 2026-06-23). World Economic Forum summary:
https://www.weforum.org/stories/2016/04/the-17-equations-that-changed-the-world/
(checked 2026-06-23).

**Automation path.** Equations → LaTeX → PDF → SVG → print-safe PNG. A short
Python script (Matplotlib or standalone LaTeX render) can typeset any equation
from the list; parametrised, so the entire series runs from a config file.
See planned `scripts/` entry for the typesetting helper.

**License.** Mathematical expressions are not copyrightable; the typeset layout
we produce is ours. The book is cited as a source, not reproduced.

---

### 2. Emergence diagram

**Concept.** A shirt built around the concept of emergence — the idea that a
system's collective behaviour cannot be predicted from its parts alone. The hero
artwork is an original diagram (not copied from any source); two foundational
equations sit small along the bottom. A short tagline: "More is different."

**The sourced idea.** Philip Anderson coined the modern framing in his 1972 *Science*
essay "More is Different": "The whole becomes not only more but very different from
the sum of its parts." The essay established emergence as a cross-disciplinary
principle in physics, biology, economics, and complex systems.
Source: Anderson, P. W. (1972). "More is Different." *Science* 177(4047): 393–396.
Available via ResearchGate:
https://www.researchgate.net/publication/308012273_More_is_different_Broken_symmetry_and_the_nature_of_the_hierarchical_structure_of_science
(checked 2026-06-23).

**Equation candidates for the footer:** could include a mean-field equation or a
phase-transition order parameter — to be finalised when the design enters
`designs/`.

**Visual note.** The diagram must be original artwork — cannot reuse an existing
diagram verbatim. Commission or generate from a detailed AI prompt with the concept
sketch. The look should feel hand-drawn-scientific rather than corporate.

**Automation path.** A crafted AI image-generation prompt, paired with an original
annotated sketch from the owner. The equation footer is LaTeX-typeset.

---

### 3. Chemistry apparatus series

**Concept.** Illustrated, accurately named pieces of lab glassware and instruments,
each on its own shirt. Clean line-art style — like a vintage scientific catalogue,
not clip art. Stretch goal: reconstruct a complete historical apparatus setup that
produced a famous discovery (e.g. Faraday's induction apparatus, Michelson-Morley
interferometer, or a distillation train).

**Sub-ideas:**
- Erlenmeyer flask — invented by Emil Erlenmeyer (1825–1909) in 1860.
  Source: https://en.wikipedia.org/wiki/Erlenmeyer_flask (checked 2026-06-23).
- Büchner funnel — designed by Ernst Wilhelm Büchner (1850–1925) in 1885 for
  vacuum filtration. Note: the flask commonly called "Büchner flask" was actually
  introduced by Shibasaburo Kitasato.
  Source: https://en.wikipedia.org/wiki/B%C3%BCchner_flask (checked 2026-06-23).
- Round-bottom flask, Liebig condenser, separating funnel, retort, burette.

**Visual direction.** Black line art on white (or reversed on black); each piece
labelled with its name in a serif typeface. Could include date of invention and
inventor's name as secondary text.

**License.** Original illustrations we produce are ours. Historical diagrams from
pre-1927 publications are public domain; verify each source individually before
use.

**Automation path.** Best done with a vector-art AI prompt or a human illustrator.
A parametrised "glassware spec → line art prompt" script is possible but speculative
at this stage.

---

### 4. "Attributes of a profession" series

**Concept.** A series of shirts, each depicting the iconic tools of one discipline,
arranged in a structured, almost taxonomic layout. Chemistry: flasks, test tubes,
burner, funnel. Physics: to be determined (candidates: metre rule, tuning fork,
cathode-ray tube schematic, oscilloscope trace). Mathematics: compass, straight
edge, chalkboard, several famous number classes.

**Why it works.** Recognisable without explanation; a physicist or chemist sees their
own discipline's vocabulary on a shirt. Works as a gift within communities.

**Visual direction.** Flat, iconographic. A clean grid of tools, each labelled.
Could be coloured or monochrome.

**License.** Original illustration, no external image dependencies.

---

### 5. "Heritage" series

**Concept.** Faithful, high-quality renditions of important historical scientific
diagrams — presented as artefacts, not decorations. Each shirt gives the diagram
with its original title or caption, the date, and the scientist's name.

**Candidate diagrams:**
- Faraday's field lines (1831 onwards) — Michael Faraday's original sketches of
  magnetic field lines; widely reproduced; originals pre-1927 → US public domain.
- Maxwell's colour triangle (1861) — his original diagram for the three-primary
  colour model used to produce the first colour photograph.
- Darwin's "I think" tree sketch from the B notebook (1837) — the first known
  evolutionary tree diagram.
- Mendeleev's periodic table draft (1869) — original hand-written table.
- Gauss's residue diagrams or Euler's polyhedral drawings.

**License discipline.** Any image used from a historical source requires:
- Source URL, author, date of original publication confirmed pre-1927.
- Specific digital reproduction's own license (some museum scans claim copyright
  over faithful reproductions — research each case before use).

**Automation path.** Sourcing and license verification is manual. Clean digital
redrawing is best done with a vector tool from a public-domain original.

---

### 6. Interesting numbers and paradoxes

**Concept.** One curiosity per shirt — a number or mathematical fact that sounds
impossible until you work through it. Each shirt: the fact, the equation or visual,
and a one-line proof hint.

**Verified curiosities with sources:**

**1/89 encodes the Fibonacci sequence.**
The decimal expansion of 1/89 begins 0.011235… — the first digits of the Fibonacci
sequence (0, 1, 1, 2, 3, 5, …). More precisely: if you write the Fibonacci numbers
as a column of decimal fractions (F₁/10, F₂/100, F₃/1000, …) and sum them, the
result converges to 1/89.
Source: OU Math, "The remarkable number 1/89":
http://www2.math.ou.edu/~dmccullough/teaching/miscellanea/miner.html (checked 2026-06-23).
Also: Hacker News discussion: https://news.ycombinator.com/item?id=653214 (checked 2026-06-23).

**Other candidate curiosities to vet:**
- The birthday paradox (50% probability of a shared birthday at 23 people).
- Benford's law (leading-digit distribution in real-world data).
- The Banach-Tarski paradox (decompose a ball, reassemble two balls of the same size).
- Ramanujan's sum 1 + 2 + 3 + … = −1/12 (requires context on analytic continuation).
- The Collatz conjecture (simple rule, no one can prove it always terminates).
- Mandelbrot set — infinite boundary complexity from a two-line iteration.

**Visual direction.** Minimal: the number or equation large, a small explanatory
line in a smaller weight. Monochrome or two-colour.

---

## Visualisation and automation notes

| Sub-idea | Best production path | Automation potential |
|---|---|---|
| 17 equations shirts | LaTeX → SVG/PNG typesetting script | High — one script covers all 17 |
| Emergence diagram | Original artwork (AI prompt + owner sketch) | Medium — prompt engineering |
| Chemistry apparatus | Vector line art (AI or illustrator) | Low at first |
| Attributes of profession | Flat iconographic illustration | Low at first |
| Heritage series | Trace/redraw from PD originals | Manual license verification |
| Numbers & paradoxes | Minimal typeset layout | High — same LaTeX pipeline |

## Priority order for execution

1. 17 equations series — highest visual value, owner competence is a hard asset,
   LaTeX automation unlocks the whole series.
2. Numbers & paradoxes — same automation path, lower design effort per shirt.
3. Emergence diagram — needs original artwork; lower priority until art pipeline
   exists.
4. Chemistry apparatus / Attributes / Heritage — secondary; revisit once the first
   series is live.

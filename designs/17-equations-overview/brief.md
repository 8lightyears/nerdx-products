# Design concept: "17 Equations" shirt series — framework and launch brief

**Slug:** `17-equations-overview`
**Status:** Concept — ready for production of first shirt (Maxwell's equations).
**Date:** 2026-06-23.

---

## Idea

A shirt series — one shirt per equation from Ian Stewart's *In Pursuit of the
Unknown: 17 Equations That Changed the World* (2012). Each shirt carries:

1. The equation, cleanly typeset.
2. The equation's name and the year it was published / formalised.
3. One sentence on why it mattered.

The series is modular: each shirt stands alone, but together they form a coherent
collection. The visual template is identical across all 17 — only the equation and
text change.

---

## Launch shirt: Maxwell's equations (#11)

**Recommended first shirt in the series**, for three reasons:
1. Four equations in one image is visually richer than a single-line formula.
2. The owner's physics background makes it trivially checkable for correctness.
3. "Maxwell unified electricity, magnetism, and light" is a powerful one-liner
   that most people have not heard but immediately find remarkable.

### The equations (SI units, differential form)

```
∇ · E = ρ / ε₀           Gauss's law
∇ · B = 0                 Gauss's law for magnetism
∇ × E = −∂B/∂t           Faraday's law
∇ × B = μ₀J + μ₀ε₀∂E/∂t  Ampère-Maxwell law
```

These four equations, published by James Clerk Maxwell in 1865, predict that light
is an electromagnetic wave — a fact Maxwell himself derived from them. The speed
of light falls directly out of the constants μ₀ and ε₀.

### The one-liner (draft)

> "Four equations. One consequence: light."

Alternative versions:
- "Maxwell wrote four equations. They predicted light. Nobody expected that."
- "In 1865, four equations explained electricity, magnetism, and light. The same
  four equations."

The owner should pick the one they would actually want to wear.

### Visual direction

**Layout (portrait, shirt-print format):**
```
[ MAXWELL'S EQUATIONS ]          ← headline, small caps or spaced serif

∇ · E  = ρ / ε₀
∇ · B  = 0
∇ × E  = − ∂B/∂t
∇ × B  = μ₀J + μ₀ε₀ ∂E/∂t

James Clerk Maxwell, 1865        ← attribution, small
─────────────────────────────
"Four equations. One consequence: light."  ← tagline
```

**Typography.** Equations in Computer Modern (LaTeX default) or a clean serif math
font — the same font the physics community uses. Attribution line in a small,
tracked weight. Tagline below a thin rule.

**Colour.** Two options:
- Black on white — clean, print-safe.
- White on black — more dramatic; lower cost on dark-fabric POD services.

**Avoid:** gradients, photographic elements, decorative frames. The equations are
the artwork.

---

## Full series map

| # | Equation | Launch priority | Notes |
|---|----------|-----------------|-------|
| 11 | Maxwell's equations | **1st** | 4-equation layout; physics strength |
| 15 | Information theory (Shannon entropy) | 2nd | H = −Σpᵢlog₂pᵢ; underpins all digital tech |
| 16 | Chaos theory | 3rd | Logistic map; fractal image as companion |
| 14 | Schrödinger equation | 4th | Quantum; iℏ notation is visually distinctive |
| 13 | Relativity (E = mc²) | 5th | Most famous; hardest to make surprising |
| 10 | Navier-Stokes | Later | Millennium Prize Problem angle is strong |
| 17 | Black-Scholes | Later | "The equation that crashed the economy" angle |
| 1–9, 12 | All others | Fill series | Standard one-equation layout |

---

## Production plan

### Step 1 — typeset the equations (scripted)
Run the typesetting helper script (`scripts/typeset_equation.py`, planned) with the
Maxwell's equations LaTeX source. Output: transparent PNG at 300 dpi, suitable for
POD upload.

LaTeX source for the four equations (requires `amsmath`):
```latex
\begin{align*}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\varepsilon_0} \\
\nabla \cdot \mathbf{B} &= 0 \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J}
                            + \mu_0 \varepsilon_0 \frac{\partial \mathbf{E}}{\partial t}
\end{align*}
```

### Step 2 — design mockup
Combine the equation PNG with the attribution and tagline in a vector layout tool
(Inkscape or Figma). Produce:
- A print-ready PNG (300 dpi, ≥ 4500 × 5400 px for a 15 × 18 inch print area).
- A review sample (JPEG, ≤ 1200 px long edge, ≤ 300 KB) → commit to `assets/`.

### Step 3 — verify
Owner checks the equations for correctness and the layout for taste. Any rejection
is noted in `docs/taste.md`.

### Step 4 — POD listing
Upload print-ready file to Merch by Amazon / Printful+Etsy / Redbubble (Redbubble
only if the 2025 fee restructure leaves acceptable margin — per the
easy-investment-opportunities-research findings, Standard tier is 50% fee for new
accounts; verify before listing).

---

## License

Mathematical expressions are not copyrightable. The typeset layout we produce is
original work. Ian Stewart's *In Pursuit of the Unknown* is cited as a source for
the conceptual framing; no text or image from the book is reproduced.

**Source:** Ian Stewart, *In Pursuit of the Unknown: 17 Equations That Changed the
World*, Basic Books, 2012. ISBN 978-0-465-08599-5.
Wikipedia: https://en.wikipedia.org/wiki/In_Pursuit_of_the_Unknown (checked 2026-06-23).
WEF summary: https://www.weforum.org/stories/2016/04/the-17-equations-that-changed-the-world/
(checked 2026-06-23).

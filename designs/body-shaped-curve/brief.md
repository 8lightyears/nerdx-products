# Design brief — Body-Shaped Curve (ScienceX sub-line)

**Status:** ready for design  
**Group:** ScienceX (adult / innuendo sub-line)  
**Slug:** `body-shaped-curve`

---

## Idea

Joseph Fourier proved in 1822 that any periodic function — including any closed
curve — can be represented exactly as a sum of rotating circles (complex
exponentials). Applied to a 2-D silhouette: trace the outline as a complex-valued
path z(t), decompose it into Fourier coefficients, and a finite sum of epicycles
(circles rotating at multiples of the base frequency) reconstructs the shape to
arbitrary precision. The shirt shows a body silhouette being drawn by just 4–6
nested rotating circles, with the equation below. The physics checks out; the
plausible deniability is structural.

---

## Copy and slogan options

**Option A (statement + equation — recommended):**

> **Every figure is a sum of circles.**
>
> z(t) = Σₙ cₙ e^(2πint)

Scientifically exact (complex Fourier series of a planar curve), visually striking
as an epicycle diagram. "Figure" does double duty.

**Option B (convergence framing):**

> **Convergent by design.**
>
> z(t) = Σₙ cₙ e^(2πint),  N → ∞

Plays on the word "design" (both deliberate construction and mathematical
approximation approaching exactness).

**Option C (minimal, equation-first):**

> cₙ = ∫₀¹ z(t) e^(−2πint) dt
>
> *The formula for your shape.*

Rewards the curious — the equation produces the coefficients that reconstruct any
outline.

---

## Equations (verified)

Complex Fourier series of a planar curve z(t) = x(t) + iy(t), parameterised on [0, 1]:

```
z(t) = Σₙ₌₋ₙ^ₙ cₙ · exp(2πint)
```

Fourier coefficients:

```
cₙ = ∫₀¹ z(t) · exp(−2πint) dt
```

Geometric interpretation: each term cₙ · e^(2πint) is a circle of radius |cₙ|
rotating at n revolutions per unit time, with initial phase arg(cₙ). The sum
of all such circles, added tip-to-tip, traces the original curve.

LaTeX for `eq_render.py`:

```latex
z(t) = \sum_{n=-N}^{N} c_n \, e^{2\pi i n t}
```

```latex
c_n = \int_0^1 z(t) \, e^{-2\pi i n t} \, dt
```

---

## Visual direction

**Primary image — epicycle construction of a body silhouette:**

A stylised human-torso outline (waist-to-shoulder, seen from the front) is shown
being drawn by 4–6 nested circles. The circles are rendered in light colours
(soft blue-white gradient) on a black background. The final traced path is white.
Only the last 3–4 revolutions of the path are shown, so the silhouette emerges
from the chain of rotating circles mid-draw. The Fourier equation sits below the
diagram in white.

Tone: mathematical, elegant, slightly surreal — in the spirit of the 3Blue1Brown
epicycle visualisations, but as static print art.

**Alternative visual — pure curve portrait:**

A single closed parametric curve with n = 8–10 terms, chosen so its outline vaguely
reads as a torso at first glance. No explicit silhouette; the resemblance is
mathematical coincidence made legible. Caption: "z(t) = Σ cₙ e^(2πint)".
Higher plausible deniability; lower "aha" moment.

---

## Generation path

1. Generate the equation PNG with the existing `scripts/eq_render.py`:

   ```bash
   python scripts/eq_render.py "z(t) = \\sum_{n=-N}^{N} c_n \\, e^{2\\pi i n t}"
   ```

2. Generate the epicycle diagram with the script below (matplotlib, ~25 lines,
   no external data):

   ```python
   import numpy as np
   import matplotlib.pyplot as plt

   # Discrete Fourier coefficients of a simple hourglass path
   N_pts = 256
   t = np.linspace(0, 2 * np.pi, N_pts, endpoint=False)
   # Hourglass silhouette in polar: r(theta) = 1 + 0.4*cos(2*theta)
   r = 1 + 0.4 * np.cos(2 * t)
   z = r * np.exp(1j * t)              # complex path

   coeffs = np.fft.fft(z) / N_pts     # DFT coefficients = Fourier cₙ
   freqs  = np.fft.fftfreq(N_pts) * N_pts

   N_terms = 5                         # keep only N_terms lowest-frequency terms
   keep = np.argsort(np.abs(freqs))[:N_terms]
   c = coeffs[keep]
   f = freqs[keep].astype(int)

   ts = np.linspace(0, 1, 2000)
   path = sum(c[k] * np.exp(2j * np.pi * f[k] * ts) for k in range(N_terms))

   fig, ax = plt.subplots(figsize=(5, 5), facecolor='black')
   ax.plot(path.real, path.imag, color='white', lw=1.5)
   ax.set_facecolor('black')
   ax.set_aspect('equal')
   ax.axis('off')
   plt.tight_layout()
   plt.savefig('body-curve.png', dpi=300, bbox_inches='tight', facecolor='black')
   ```

   Adjust `r(theta)` to taste — adding a third harmonic (0.2*cos(3*theta)) can
   make the outline read more like a torso.

3. Overlay equation PNG and curve plot in a vector editor or as a combined
   Matplotlib figure (two subplots: curve top, equation bottom).

4. Export at 300 DPI, minimum 4500 px on the long edge for DTG.

---

## License and sources

- **Fourier series:** Fourier, J.B.J., *Théorie analytique de la chaleur* (1822) —
  published 200+ years ago, fully in the public domain. All equations derived from
  it are mathematical facts, not copyrightable.
- The epicycle interpretation is standard mathematical knowledge; the specific
  diagram is original code output — no third-party asset.
- **Status: fully licensable** — no third-party artwork needed to reach print.

---

## Notes

- The "hourglass" polar curve r = 1 + A·cos(2θ) is the simplest that reads as
  body-like; the coefficient A ∈ (0, 1) controls how pronounced the waist is.
  A = 0.5 gives a clearly pinched waist without degeneration (curve stays convex).
- For the epicycle visual, animating the construction (GIF) would be striking for
  social media; the static version (final circle chain + traced path) works for print.
- "Sum of circles" framing is accessible to non-mathematicians; "Fourier series"
  framing rewards people with physics or engineering backgrounds.

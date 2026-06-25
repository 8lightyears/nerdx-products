# Design brief — Viscosity (ScienceX sub-line)

**Status:** ready for design  
**Group:** ScienceX (adult / innuendo sub-line)  
**Slug:** `viscosity`

---

## Idea

Viscosity is a fluid's resistance to deformation under shear — how hard it is to
make it flow. Honey, tar, and glass have high viscosity; water and air have low
viscosity. The word and concept carry an unmistakable double meaning when worn on
a shirt. The physics is correct, the innuendo is plausible deniability.

---

## Copy and slogan options

**Option A (statement + equation — recommended):**

> **HIGH VISCOSITY**
> *I resist flow.*
>
> τ = η (du/dy)

Clean, wearable, scientifically exact. "Resist flow" is the literal meaning
(viscous resistance to shear) and the implied one simultaneously.

**Option B (rheological framing):**

> **Non-Newtonian**
> *My viscosity changes under pressure.*

Works for shear-thinning / thickening materials (ketchup, blood, quicksand).
Pairs well with a rheogram (shear stress vs. shear rate curve showing deviation
from linearity).

**Option C (minimal):**

> **η >> 0**
> *Some things just don't flow easily.*

Mathematical, terse, owner's physics background rewarded.

---

## Equations (verified)

Newton's law of viscosity (constitutive relation for a Newtonian fluid):

```
τ = η · (du/dy)
```

where:
- τ — shear stress [Pa = N/m²]
- η — dynamic viscosity [Pa·s]
- u — fluid velocity [m/s]
- y — coordinate normal to flow [m]

LaTeX (for `eq_render.py`):

```latex
\tau = \eta \, \frac{du}{dy}
```

Kinematic viscosity (secondary, for back-of-shirt or fine print):

```
ν = η / ρ   [m²/s]
```

LaTeX:

```latex
\nu = \frac{\eta}{\rho}
```

Reynolds number (optional footnote — bridges viscosity and turbulence):

```
Re = ρ v L / η
```

LaTeX:

```latex
Re = \frac{\rho v L}{\eta}
```

---

## Visual direction

**Primary image — laminar flow profile (Hagen-Poiseuille parabolic profile):**

Cross-section of a pipe showing the parabolic velocity profile for laminar flow.
Clean line art, dark background. Velocity arrows increase from the wall (u=0,
no-slip condition) to the centreline (u_max). Caption: "No-slip condition at the
wall — just like me."

Equation underneath: τ = η (du/dy)

*This is derivable analytically — no licensed image needed. The fractal_render.py
and eq_render.py scripts already in `scripts/` can be adapted; alternatively a
simple Matplotlib plot (`plt.fill_betweenx`) produces the profile.*

**Alternative visual — honey drip (photographic mood reference only, not for print):**

High-speed photograph of honey dripping (search Unsplash / Wikimedia Commons for
CC0). Use only for mood reference; final artwork should be original line art or
AI-generated to avoid license uncertainty.

---

## Generation path

1. Run `python scripts/eq_render.py "\\tau = \\eta \\, \\frac{du}{dy}"` to produce
   the equation as a transparent white PNG.
2. Script a Matplotlib parabolic-profile plot (10 lines; no external data):

   ```python
   import numpy as np, matplotlib.pyplot as plt
   r = np.linspace(-1, 1, 400)
   u = 1 - r**2          # Hagen-Poiseuille profile, normalised
   fig, ax = plt.subplots(figsize=(4, 6), facecolor='black')
   ax.fill_betweenx(r, 0, u, color='#4fc3f7', alpha=0.85)
   ax.set_facecolor('black')
   ax.axis('off')
   plt.tight_layout()
   plt.savefig('viscosity-profile.png', dpi=300, bbox_inches='tight',
               facecolor='black')
   ```

3. Compose profile + equation in a vector editor or via Matplotlib subplots.
4. Export final artwork at 300 DPI, minimum 4500 px on the long edge (DTG print
   standard), white/light art on black shirt recommended.

---

## License and sources

- All equations are mathematical facts — not copyrightable.
- The Hagen-Poiseuille profile plot is original code output — no third-party asset.
- **Source for equations:** Bird, Stewart, Lightfoot, *Transport Phenomena*,
  2nd ed. (2002), §1.1 — standard reference for Newtonian viscosity.
  (This is a citation, not a reproduced image; no license required.)
- Status: **fully licensable** — no third-party artwork needed to reach print.

---

## Notes

- Owner's physics background: confirm sign convention for τ and axis orientation
  before final print. Convention here follows Bird et al. (positive shear stress
  in the positive-y direction).
- Do not use the word "Newtonian" in the slogan unless Option B is chosen — it
  implies a specific (linear) behaviour and the shirt should not claim the wearer
  is Newtonian unless that's the joke.
- "Kinematic viscosity" is ν (nu), visually similar to v (velocity) — if the
  equation block is small, label clearly.

# Design brief — Rigid Body (ScienceX sub-line)

**Status:** ready for design  
**Group:** ScienceX (adult / innuendo sub-line)  
**Slug:** `rigid-body`

---

## Idea

A rigid body in classical mechanics is an idealised solid object that does not
deform when forces are applied — every pair of points within it maintains a
fixed distance. Rigid body dynamics is the branch of mechanics that deals with
the rotation and translation of such objects. Newton (1687) established the
translational equations; Euler (1765) completed the rotational theory. The shirt
shows a canonical free-body diagram: a solid block with force vectors, a torque
arrow, and the rotational equation of motion. The term and its physics are
entirely genuine. The double meaning is left as an exercise for the reader.

---

## Copy and slogan options

**Option A (equation + definition — recommended):**

> **RIGID BODY**
>
> τ = Iα
>
> *All forces accounted for.*

τ = Iα is the rotational analogue of F = ma. "All forces accounted for" is the
literal requirement for a complete free-body diagram and the implied claim.

**Option B (definition-first):**

> **Rigid Body**  
> *An object that does not deform under applied forces.*  
>
> I = ∫ r² dm

Plays the definition straight; the equation (moment of inertia) rewards technical
readers. The definition sounds clinical until you think about it for a moment.

**Option C (minimal, classical mechanics framing):**

> **τ = r × F**
>
> *The torque is always at right angles to the force.*

Focuses on the cross-product torque — strictly correct, subtly geometric.
Works with or without the "Rigid Body" header.

---

## Equations (verified)

Newton's second law for rotation (Euler's equation for fixed-axis rotation):

```
τ = I · α
```

where:
- τ — net torque about the axis [N·m]
- I — moment of inertia [kg·m²]
- α — angular acceleration [rad/s²]

Torque as a cross product:

```
τ = r × F
```

where r is the position vector from the pivot to the point of force application,
F is the applied force.

Moment of inertia (integral form):

```
I = ∫ r² dm
```

For common shapes (closed-form solutions, for reference):
- Thin rod about centre: I = (1/12) m L²
- Solid cylinder about symmetry axis: I = (1/2) m R²
- Point mass at distance r: I = m r²

Angular momentum:

```
L = I · ω
```

and its time derivative gives the equation of motion: τ = dL/dt = Iα (for fixed I).

LaTeX for `eq_render.py`:

```latex
\tau = I \alpha
```

```latex
I = \int r^2 \, dm
```

```latex
\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}
```

---

## Visual direction

**Primary image — free-body diagram:**

A rectangular block (rendered as a clean technical illustration on black background)
with the following labelled vectors:

- Weight **W** = mg pointing straight down from the centre of mass
- Normal force **N** pointing upward from the contact surface
- Applied force **F** at a ~45° angle to the upper-right
- Torque arc **τ** = r × F (curved arrow about the centre of mass, shown in a
  contrasting colour, e.g. cyan or orange)
- Angular acceleration **α** arrow (for emphasis)

Labels in clean sans-serif white. Equations τ = Iα and τ = r × F beneath the diagram.

Aesthetic: engineering drawing / technical schematic — same tone as the
viscosity profile or the 17-equations series.

**Alternative visual — rotational motion spiral:**

The block in mid-rotation, with a ghost trail showing several past positions
(semi-transparent), plus the force vectors frozen at one instant. More dynamic,
less textbook, but harder to read at shirt scale. Recommended only if the static
free-body diagram reads as too small.

---

## Generation path

1. Generate equation PNGs:

   ```bash
   python scripts/eq_render.py "\\tau = I \\alpha"
   python scripts/eq_render.py "I = \\int r^2 \\, dm"
   ```

2. Generate the free-body diagram (~30 lines, matplotlib + patches):

   ```python
   import matplotlib.pyplot as plt
   import matplotlib.patches as mpatches
   from matplotlib.patches import FancyArrowPatch

   fig, ax = plt.subplots(figsize=(5, 6), facecolor='black')
   ax.set_facecolor('black')

   # Rigid body block
   body = mpatches.FancyBboxPatch((-0.6, -0.4), 1.2, 0.8,
       boxstyle='round,pad=0.05', linewidth=2,
       edgecolor='white', facecolor='#1a1a2e')
   ax.add_patch(body)
   ax.text(0, 0, 'RIGID\nBODY', color='white', ha='center', va='center',
           fontsize=9, fontfamily='monospace')

   # Weight vector
   ax.annotate('', xy=(0, -1.2), xytext=(0, -0.4),
       arrowprops=dict(arrowstyle='->', color='#ff8c69', lw=2))
   ax.text(0.12, -0.85, 'W = mg', color='#ff8c69', fontsize=9)

   # Normal force
   ax.annotate('', xy=(0, 0.9), xytext=(0, 0.4),
       arrowprops=dict(arrowstyle='->', color='#4fc3f7', lw=2))
   ax.text(0.12, 0.65, 'N', color='#4fc3f7', fontsize=9)

   # Applied force
   ax.annotate('', xy=(0.85, 0.85), xytext=(0.6, 0.4),
       arrowprops=dict(arrowstyle='->', color='#a0f0a0', lw=2))
   ax.text(0.72, 0.72, 'F', color='#a0f0a0', fontsize=9)

   # Torque arc
   import numpy as np
   theta = np.linspace(0.4, 2.0, 40)
   ax.plot(0.3 * np.cos(theta), 0.3 * np.sin(theta),
           color='#ffd700', lw=2.5)
   ax.text(0.35, 0.25, 'τ', color='#ffd700', fontsize=14)

   ax.set_xlim(-1.2, 1.4)
   ax.set_ylim(-1.5, 1.2)
   ax.set_aspect('equal')
   ax.axis('off')
   plt.tight_layout()
   plt.savefig('rigid-body-diagram.png', dpi=300, bbox_inches='tight',
               facecolor='black')
   ```

3. Add τ = Iα equation panel below diagram in a combined figure or vector editor.

4. Export at 300 DPI, minimum 4500 px on the long edge.

---

## License and sources

- **Newton's second law for rotation:** Newton, I., *Philosophiæ Naturalis Principia
  Mathematica* (1687) — published 339 years ago, fully in the public domain.
- **Euler's rotational dynamics:** Euler, L., "Du mouvement de rotation des corps
  solides autour d'un axe variable" (1765) — also public domain.
- All equations are mathematical facts — not copyrightable.
- The free-body diagram is original code output — no third-party asset.
- **Status: fully licensable.**

---

## Notes

- The term "rigid body" appears verbatim in every introductory mechanics textbook;
  plausible deniability is structurally guaranteed.
- The block can be styled as a simple rectangle, a cylinder, or a more abstract
  solid shape; a rectangle is cleanest at shirt scale.
- Colour palette for the vectors: use distinct hues so force types are
  distinguishable even in a black-and-white print preview (weight warm red,
  normal force cool blue, applied force green, torque gold).
- Consider Option A + the free-body diagram on the front, and the moment-of-inertia
  table for common shapes (rod / cylinder / sphere) as back-of-shirt fine print
  ("Know your moment of inertia").

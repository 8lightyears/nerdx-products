# Design Brief: Drag Coefficient (ScienceX)

## Concept

The drag force on any body moving through a fluid depends on the fluid density, the velocity
squared, the frontal area, and the drag coefficient — a dimensionless number encoding the
body's shape. The colloquial interpretation: drag is, by definition, a function of your shape
and how fast you move. The innuendo is in the physics, not added to it.

## Slogan options

1. **"Drag is a function of your shape and velocity."**
   — Below or alongside: `F_D = ½ρv²C_D A`
   — The sentence is literally true. The double meaning is earned.

2. **`F_D = ½ρv²C_D A` — "High C_D. Worth it."**
   — Equation first, defiant punchline second.

3. **"Coefficient of Drag: the science of looking fabulous while slowing down traffic."**
   — Longer tagline, more humour, less elegance. Works better on a mug.

**Recommended launch:** option 1 — direct, scientifically accurate, and the payoff works for
physicists and non-physicists alike.

## Equations (verified)

Drag force equation:

    F_D = ½ · ρ · v² · C_D · A

where:
- `F_D` — drag force [N]
- `ρ`   — fluid density [kg/m³] (air at sea level: 1.225 kg/m³)
- `v`   — velocity [m/s]
- `C_D` — drag coefficient [dimensionless]
- `A`   — reference (frontal) area [m²]

LaTeX:

    F_D = \tfrac{1}{2}\,\rho\,v^2\,C_D\,A

Illustrative C_D values (for optional footnote or back print):
- Sphere: C_D ≈ 0.47
- Long cylinder: C_D ≈ 0.82
- Streamlined body: C_D ≈ 0.04
- Flat plate (perpendicular): C_D ≈ 1.28

Source: Munson, Young & Okiishi, *Fundamentals of Fluid Mechanics*, 7th ed. (2012), §9.3.
Physical constants and dimensionless coefficients carry no copyright.

## Visual direction

- **Primary element:** equation `F_D = ½ρv²C_D A` typeset in white on a dark background
  (black or charcoal shirt).
- **Optional secondary element:** a clean side-profile silhouette of a sphere vs. a
  streamlined teardrop shape with their C_D values labelled — contrasting "bad" vs. "good"
  drag design. This can be generated as a minimal Matplotlib line drawing.
- **Layout:** slogan line above the equation (or centred as a single block); optional
  comparison diagram below as a footnote visual.

## Generation path

Step 1 — render the equation:

    python scripts/eq_render.py \
        r"F_D = \tfrac{1}{2}\,\rho\,v^2\,C_D\,A" \
        --dpi 300 --fontsize 72 --color white \
        --output designs/drag-coefficient/eq.png

Step 2 (optional) — generate shape comparison diagram:

```python
# drag_shapes.py — generates a ~10-line Matplotlib diagram
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(8, 3), facecolor='black')
for ax in axes:
    ax.set_facecolor('black')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')

# Sphere
circle = plt.Circle((0, 0), 0.8, color='white', fill=False, linewidth=2)
axes[0].add_patch(circle)
axes[0].text(0, -1.1, r'Sphere  $C_D \approx 0.47$', color='white',
             ha='center', fontsize=11)

# Streamlined teardrop (approximate with an ellipse)
ellipse = patches.Ellipse((0, 0), 2.4, 0.8, color='white', fill=False, linewidth=2)
axes[1].add_patch(ellipse)
axes[1].text(0, -1.1, r'Streamlined  $C_D \approx 0.04$', color='white',
             ha='center', fontsize=11)

plt.tight_layout()
plt.savefig('designs/drag-coefficient/shapes.png', dpi=150,
            bbox_inches='tight', facecolor='black')
```

    python designs/drag-coefficient/drag_shapes.py

Step 3 — compose in Canva / Inkscape: equation + optional shapes diagram on dark background,
slogan text at the top.

## License

Drag force equation is a standard result in fluid mechanics (attributed to Rayleigh 1876 and
formalised by Prandtl in the early 20th century; formula is in the public domain).
Munson et al. cited as a secondary source; no text or figures reproduced.
All visual output is original code-generated artwork.
No third-party assets required.

## Status

Draft — ready for visual composition.

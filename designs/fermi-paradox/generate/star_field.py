"""
Procedural deep-space star field for the Fermi Paradox design.

Dependencies: pip install matplotlib numpy

Run:
    python designs/fermi-paradox/generate/star_field.py

Output (NOT committed — full-res print file):
    designs/fermi-paradox/generate/star_field_3300.png

Review sample (commit this):
    designs/fermi-paradox/assets/star_field_preview.jpg
    (convert in any tool: JPEG, quality 80, long edge ≤ 1200 px)
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RNG = np.random.default_rng(42)
N_FAINT = 3000
N_BRIGHT = 8

fig, ax = plt.subplots(figsize=(11, 11), facecolor="black")
ax.set_facecolor("black")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

# Faint background stars — power-law size distribution
x = RNG.uniform(0, 1, N_FAINT)
y = RNG.uniform(0, 1, N_FAINT)
sizes = RNG.power(0.4, N_FAINT) * 3.0 + 0.2   # most very small
alphas = RNG.uniform(0.3, 1.0, N_FAINT)
ax.scatter(x, y, s=sizes, c="white", alpha=None, linewidths=0,
           zorder=2)
for xi, yi, si, ai in zip(x, y, sizes, alphas):
    ax.scatter(xi, yi, s=si, c="white", alpha=float(ai), linewidths=0, zorder=2)

# Brighter feature stars with soft glow
bx = RNG.uniform(0.05, 0.95, N_BRIGHT)
by = RNG.uniform(0.05, 0.95, N_BRIGHT)
for xi, yi in zip(bx, by):
    for glow_size, glow_alpha in [(120, 0.06), (40, 0.15), (10, 0.7), (3, 1.0)]:
        ax.scatter(xi, yi, s=glow_size, c="white", alpha=glow_alpha,
                   linewidths=0, zorder=3)

# Optional: add text overlay here
# ax.text(0.5, 0.55, "WHERE IS EVERYBODY?", color="white", fontsize=48,
#         ha="center", va="center", fontweight="bold", transform=ax.transAxes)
# ax.text(0.5, 0.44, "Fermi, Los Alamos, 1950.", color="white", fontsize=16,
#         ha="center", va="center", transform=ax.transAxes)

fig.savefig("designs/fermi-paradox/generate/star_field_3300.png",
            dpi=300, bbox_inches="tight", facecolor="black")
print("Saved: designs/fermi-paradox/generate/star_field_3300.png")

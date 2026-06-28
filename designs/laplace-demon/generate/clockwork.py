"""
Clockwork gear diagram for Laplace's demon shirt.

Dependencies: matplotlib, numpy
Example: python clockwork.py --out clockwork.svg

Outputs a gear assembly (3 nested gears) with an eye at the hub, suitable for
SVG-to-vector workflow in Inkscape or Affinity Designer.
"""
import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path
import matplotlib.patches as patches


def gear_path(cx, cy, r_pitch, n_teeth, tooth_height=None, pressure_angle=20):
    """Return (x, y) arrays for a simple gear outline (circular-arc tooth approx)."""
    if tooth_height is None:
        tooth_height = r_pitch * 0.25
    r_root = r_pitch - tooth_height * 0.6
    r_tip = r_pitch + tooth_height * 0.4
    angles = np.linspace(0, 2 * math.pi, n_teeth * 4, endpoint=False)
    pts = []
    for i, a in enumerate(angles):
        phase = i % 4
        if phase == 0:
            r = r_root
        elif phase == 1:
            r = r_tip
        elif phase == 2:
            r = r_tip
        else:
            r = r_root
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    pts.append(pts[0])
    xs, ys = zip(*pts)
    return np.array(xs), np.array(ys)


def eye_path(cx, cy, r):
    """Stylised eye (almond shape) centred at (cx, cy) with half-width r."""
    t = np.linspace(-math.pi, math.pi, 200)
    x = cx + r * np.cos(t)
    y = cy + r * 0.45 * np.sin(t)
    return x, y


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='clockwork.svg')
    args = parser.parse_args()

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')
    ax.axis('off')

    # Three gears: large centre, medium upper-right, small lower-right
    gears = [
        dict(cx=0.0,  cy=0.0,  r=2.0, n=32, lw=1.6),
        dict(cx=2.8,  cy=1.6,  r=1.2, n=20, lw=1.2),
        dict(cx=2.6, cy=-1.8,  r=0.8, n=14, lw=1.0),
    ]

    for g in gears:
        xs, ys = gear_path(g['cx'], g['cy'], g['r'], g['n'])
        ax.plot(xs, ys, 'k-', linewidth=g['lw'])
        # Hub circle
        hub = plt.Circle((g['cx'], g['cy']), g['r'] * 0.12,
                          color='white', ec='black', lw=g['lw'])
        ax.add_patch(hub)
        # Spokes (4)
        for angle in np.linspace(0, math.pi, 4, endpoint=False):
            dx = math.cos(angle) * g['r'] * 0.85
            dy = math.sin(angle) * g['r'] * 0.85
            ax.plot([g['cx'] - dx, g['cx'] + dx],
                    [g['cy'] - dy, g['cy'] + dy],
                    'k-', linewidth=g['lw'] * 0.6)

    # All-knowing eye at centre of large gear
    ex, ey = eye_path(0.0, 0.0, 0.55)
    ax.fill(ex, ey, 'white', zorder=3)
    ax.plot(ex, ey, 'k-', linewidth=1.2, zorder=4)
    # Pupil
    pupil = plt.Circle((0.0, 0.0), 0.18, color='black', zorder=5)
    ax.add_patch(pupil)
    # Iris ring
    iris = plt.Circle((0.0, 0.0), 0.28, color='white', ec='black',
                       lw=0.8, zorder=4)
    ax.add_patch(iris)

    ax.set_xlim(-3.2, 4.4)
    ax.set_ylim(-3.2, 3.2)

    fig.savefig(args.out, format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {args.out}")


if __name__ == '__main__':
    main()

"""
Trolley problem track schematic for shirt design.

Dependencies: matplotlib
Example:
  python track.py --variant A --out track_A.svg
  python track.py --variant B --out track_B.svg

Variant A: lever right (diverted), Variant B: lever left (straight).
Outputs SVG suitable for vector finishing in Inkscape or Affinity Designer.
"""
import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D


def draw_track(ax, x0, y0, x1, y1, lw=3, color='black', tie_count=6):
    """Draw two parallel rails between two points with cross-ties."""
    dx, dy = x1 - x0, y1 - y0
    length = math.hypot(dx, dy)
    nx, ny = -dy / length * 0.08, dx / length * 0.08  # rail offset (perpendicular)

    for sign in (-1, 1):
        ax.plot([x0 + sign * nx, x1 + sign * nx],
                [y0 + sign * ny, y1 + sign * ny],
                color=color, linewidth=lw, solid_capstyle='round')

    # Cross-ties
    for i in np.linspace(0.1, 0.9, tie_count):
        tx = x0 + dx * i
        ty = y0 + dy * i
        ax.plot([tx - nx * 2, tx + nx * 2],
                [ty - ny * 2, ty + ny * 2],
                color=color, linewidth=lw * 0.5, solid_capstyle='round')


def stick_figure(ax, cx, cy, scale=0.12, color='black'):
    """Draw a minimal stick figure centred at (cx, cy)."""
    head = plt.Circle((cx, cy + scale * 1.15), scale * 0.3, color=color)
    ax.add_patch(head)
    ax.plot([cx, cx], [cy + scale * 0.85, cy - scale * 0.1], color=color, lw=1.5)
    ax.plot([cx - scale * 0.4, cx + scale * 0.4], [cy + scale * 0.45, cy + scale * 0.45],
            color=color, lw=1.5)
    ax.plot([cx, cx - scale * 0.35], [cy - scale * 0.1, cy - scale * 0.7],
            color=color, lw=1.5)
    ax.plot([cx, cx + scale * 0.35], [cy - scale * 0.1, cy - scale * 0.7],
            color=color, lw=1.5)


def draw_lever(ax, cx, cy, right=True, color='black'):
    """Draw lever symbol at junction. right=True → track diverted right."""
    angle = math.radians(40 if right else -40)
    lx = cx + 0.25 * math.cos(angle)
    ly = cy + 0.25 * math.sin(angle)
    ax.plot([cx, lx], [cy, ly], color=color, linewidth=4, solid_capstyle='round')
    ax.add_patch(plt.Circle((cx, cy), 0.06, color=color, zorder=5))
    ax.add_patch(plt.Circle((lx, ly), 0.04, color='white', ec=color, linewidth=2, zorder=6))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--variant', choices=['A', 'B'], default='A',
                        help='A=lever right (diverted), B=lever left (straight)')
    parser.add_argument('--out', default='track.svg')
    args = parser.parse_args()

    fig, ax = plt.subplots(figsize=(7, 9))
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-1.5, 3.5)
    ax.set_ylim(-2.0, 3.5)

    junction_x, junction_y = 1.0, 0.5
    color = 'black'

    # Incoming track (bottom, centred)
    draw_track(ax, 1.0, -1.8, junction_x, junction_y, color=color)

    # Main (straight) track → five figures (top-right)
    draw_track(ax, junction_x, junction_y, 3.2, 2.8, color=color)

    # Side track → one figure (top-left)
    draw_track(ax, junction_x, junction_y, -0.8, 2.8, color=color)

    # Junction dot
    ax.add_patch(plt.Circle((junction_x, junction_y), 0.09, color=color, zorder=5))

    # Lever
    draw_lever(ax, junction_x + 0.25, junction_y - 0.15,
               right=(args.variant == 'A'), color=color)

    # Five figures (straight track end)
    for i, ox in enumerate(np.linspace(2.3, 3.2, 5)):
        stick_figure(ax, ox, 3.0, scale=0.11, color=color)

    # One figure (side track end)
    stick_figure(ax, -0.6, 3.0, scale=0.11, color=color)

    # Trolley (simple rectangle on incoming track)
    trolley = mpatches.FancyBboxPatch((0.55, -1.5), 0.9, 0.45,
                                       boxstyle='round,pad=0.05',
                                       facecolor='white', edgecolor=color, linewidth=2)
    ax.add_patch(trolley)
    ax.text(1.0, -1.27, 'TROLLEY', ha='center', va='center',
            fontsize=5, fontfamily='monospace', color=color)

    fig.savefig(args.out, format='svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {args.out} (variant {args.variant})")


if __name__ == '__main__':
    main()

"""
chladni_render.py — Chladni nodal-line visualiser for nerdx-products

Renders the nodal pattern of a vibrating rectangular membrane:
  u(x, y) = sin(m*pi*x) * sin(n*pi*y)
The lines where u = 0 approximate Ernst Chladni's sand-plate figures (1787).
Choose m != n for asymmetric patterns; m == n gives symmetric X patterns.

Usage:
    python scripts/chladni_render.py
    python scripts/chladni_render.py --m 3 --n 4 --output chladni_3_4.png
    python scripts/chladni_render.py --m 2 --n 5 --size 3300 --light

Examples of interesting mode pairs:
    (2, 3) — 6 regions, mild asymmetry, classic Chladni look
    (3, 4) — 12 regions, striking star pattern
    (1, 4) — 4 parallel lines, simple and bold
    (4, 5) — dense pattern, 20 regions

Dependencies:
    pip install matplotlib numpy
"""

import argparse
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def render(m: int, n: int, size: int, output: str, dark: bool) -> None:
    N = 2000  # internal grid resolution; independent of output size
    x = np.linspace(0, 1, N)
    y = np.linspace(0, 1, N)
    X, Y = np.meshgrid(x, y)
    u = np.sin(m * np.pi * X) * np.sin(n * np.pi * Y)

    bg = "#0a0a0a" if dark else "#f5f5f5"
    line_colour = "#e8e8e8" if dark else "#111111"

    dpi = 300
    fig_inches = size / dpi
    fig, ax = plt.subplots(figsize=(fig_inches, fig_inches), facecolor=bg)
    ax.set_facecolor(bg)

    # Nodal lines are the zero-contour of u.
    ax.contour(X, Y, u, levels=[0.0], colors=[line_colour], linewidths=3.0)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")

    plt.tight_layout(pad=0)
    plt.savefig(output, dpi=dpi, bbox_inches="tight", facecolor=bg, pad_inches=0.04)
    plt.close()
    print(f"Saved: {output}  (m={m}, n={n}, {size}x{size} px)")


def main() -> None:
    p = argparse.ArgumentParser(description="Render a Chladni nodal-line pattern.")
    p.add_argument("--m", type=int, default=2, help="Horizontal mode index (default 2)")
    p.add_argument("--n", type=int, default=3, help="Vertical mode index (default 3)")
    p.add_argument("--size", type=int, default=3300, help="Output image size in pixels (default 3300)")
    p.add_argument("--output", default="chladni.png", help="Output filename (default chladni.png)")
    p.add_argument("--light", action="store_true", help="Light background instead of dark")
    args = p.parse_args()

    render(args.m, args.n, args.size, args.output, dark=not args.light)


if __name__ == "__main__":
    main()

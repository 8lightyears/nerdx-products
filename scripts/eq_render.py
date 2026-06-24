# eq_render.py — Render LaTeX equations to transparent PNG using Matplotlib mathtext.
#
# Dependencies: pip install matplotlib
# Verified: matplotlib >= 3.7 (no full LaTeX installation required)
#
# Usage:
#   python scripts/eq_render.py FORMULA OUTPUT [--dpi DPI] [--fontsize FONTSIZE] [--color COLOR]
#
# Examples:
#   python scripts/eq_render.py r"$\nabla \cdot \mathbf{E} = \frac{\rho}{\varepsilon_0}$" out/gauss.png
#   python scripts/eq_render.py r"$e^{i\pi} + 1 = 0$" out/euler.png --fontsize 80 --dpi 600
#   python scripts/eq_render.py r"$F = G\frac{m_1 m_2}{r^2}$" out/newton.png --color black
#
# Output: transparent PNG, white text by default — drop onto any dark background
# without a box; use --color black for white shirts.
# For t-shirt POD: --dpi 300 at fontsize 72 yields ~3 in wide at 300 dpi.

import argparse
import pathlib

import matplotlib
matplotlib.use("Agg")  # headless; no display required
import matplotlib.pyplot as plt


def render(formula: str, output: str, dpi: int = 300,
           fontsize: int = 72, color: str = "white") -> None:
    fig = plt.figure(figsize=(8, 2), facecolor="none")
    fig.text(
        0.5, 0.5, formula,
        ha="center", va="center",
        fontsize=fontsize, color=color,
        transform=fig.transFigure,
    )
    pathlib.Path(output).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        output, dpi=dpi, transparent=True,
        bbox_inches="tight", facecolor="none", edgecolor="none",
    )
    plt.close(fig)
    print(f"Saved: {output}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Render a LaTeX / mathtext equation to a transparent PNG."
    )
    p.add_argument("formula", help='LaTeX string, e.g. r"$E = mc^2$"')
    p.add_argument("output", help="Output PNG path (parent directories created automatically)")
    p.add_argument("--dpi", type=int, default=300, help="Resolution in DPI (default 300)")
    p.add_argument("--fontsize", type=int, default=72,
                   help="Font size in points (default 72; ~6 cm wide at 300 dpi)")
    p.add_argument("--color", default="white",
                   help="Text colour — any Matplotlib name or hex code (default white)")
    args = p.parse_args()
    render(args.formula, args.output, dpi=args.dpi, fontsize=args.fontsize, color=args.color)

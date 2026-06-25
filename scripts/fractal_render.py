# fractal_render.py — Render Mandelbrot and Julia set fractals to PNG.
#
# Dependencies: pip install matplotlib numpy
# Verified: matplotlib >= 3.7, numpy >= 1.24
#
# Usage:
#   python scripts/fractal_render.py [OPTIONS]
#
# Examples:
#   python scripts/fractal_render.py --output out/mandelbrot.png
#   python scripts/fractal_render.py --mode julia --cmap inferno --output out/julia.png
#   python scripts/fractal_render.py --width 4096 --height 4096 --max-iter 512 \
#       --cmap plasma --output out/mandelbrot-hires.png
#   python scripts/fractal_render.py --mode julia --julia-c "-0.4+0.6j" \
#       --cmap magma --output out/julia-alt.png
#
# Available colormaps (for t-shirt contexts):
#   viridis, plasma, inferno, magma, cividis  — perceptually uniform, bold colours
#   twilight, hsv                              — cyclic; interesting for Julia sets
#   Full list: https://matplotlib.org/stable/gallery/color/colormap_reference.html

import argparse
import pathlib

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _mandelbrot(h: int, w: int, max_iter: int) -> np.ndarray:
    y, x = np.ogrid[-1.4:1.4:h * 1j, -2.0:0.8:w * 1j]
    c = x + y * 1j
    z = c.copy()
    escape = np.full(c.shape, float(max_iter))
    for i in range(max_iter):
        mask = np.abs(z) <= 2
        z[mask] = z[mask] ** 2 + c[mask]
        newly = mask & (np.abs(z) > 2)
        # smooth colouring: subtract log of log of modulus for continuous bands
        escape[newly] = i + 1 - np.log2(np.log2(np.abs(z[newly]).clip(1e-10)))
    return escape


def _julia(h: int, w: int, c: complex, max_iter: int) -> np.ndarray:
    y, x = np.ogrid[-1.5:1.5:h * 1j, -1.5:1.5:w * 1j]
    z = x + y * 1j
    escape = np.full(z.shape, float(max_iter))
    for i in range(max_iter):
        mask = np.abs(z) <= 2
        z[mask] = z[mask] ** 2 + c
        newly = mask & (np.abs(z) > 2)
        escape[newly] = i + 1 - np.log2(np.log2(np.abs(z[newly]).clip(1e-10)))
    return escape


def render(data: np.ndarray, output: str, cmap: str = "viridis",
           transparent: bool = False) -> None:
    fig, ax = plt.subplots(
        figsize=(data.shape[1] / 100, data.shape[0] / 100), dpi=100
    )
    ax.imshow(data, cmap=cmap, origin="lower", interpolation="bilinear")
    ax.axis("off")
    fig.subplots_adjust(0, 0, 1, 1)
    pathlib.Path(output).parent.mkdir(parents=True, exist_ok=True)
    bg = "none" if transparent else ax.get_facecolor()
    fig.savefig(output, dpi=100, transparent=transparent,
                facecolor=bg, bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    print(f"Saved: {output}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(
        description="Render a Mandelbrot or Julia set fractal to PNG."
    )
    p.add_argument("--mode", choices=["mandelbrot", "julia"], default="mandelbrot",
                   help="Fractal type (default: mandelbrot)")
    p.add_argument("--width", type=int, default=2048, help="Width in pixels (default 2048)")
    p.add_argument("--height", type=int, default=2048, help="Height in pixels (default 2048)")
    p.add_argument("--max-iter", type=int, default=256, dest="max_iter",
                   help="Max iterations — higher = more detail (default 256)")
    p.add_argument("--cmap", default="viridis",
                   help="Matplotlib colormap name (default viridis)")
    p.add_argument("--julia-c", default="-0.7+0.27j", dest="julia_c",
                   help="Julia set constant as Python complex literal (default -0.7+0.27j)")
    p.add_argument("--transparent", action="store_true",
                   help="Transparent background (use with --cmap that has black interior)")
    p.add_argument("--output", default="out/fractal.png",
                   help="Output PNG path (default out/fractal.png)")
    args = p.parse_args()

    if args.mode == "mandelbrot":
        data = _mandelbrot(args.height, args.width, args.max_iter)
    else:
        data = _julia(args.height, args.width, complex(args.julia_c), args.max_iter)

    render(data, args.output, cmap=args.cmap, transparent=args.transparent)

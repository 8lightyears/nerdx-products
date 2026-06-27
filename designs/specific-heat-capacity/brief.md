# Design Brief: Specific Heat Capacity (ScienceX)

## Concept

Specific heat capacity (c) measures how much energy a substance needs to raise its temperature
by 1 °C per unit mass. The vernacular interpretation: some materials (and people) take a lot
of energy to heat up. The innuendo is obvious, the physics is exact.

## Slogan options

1. **"It takes a lot of energy to get me excited."**
   — Below or alongside: `c = Q / mΔT`
   — Works as a standalone statement; the equation rewards those who look closer.

2. **`c = Q / mΔT` — "I have a high specific heat."**
   — Equation first, punchline second. Nerd-first layout.

3. **"High Specific Heat — resistant to temperature change since [year]."**
   — Mock certification badge format, similar to a material-data-sheet sticker.

**Recommended launch:** option 1 — the human-readable phrase lands first, equation reads as
the footnote; maximises breadth of appeal while keeping the physics accurate.

## Equations (verified)

Core relation:

    c = Q / (m · ΔT)

where:
- `c` — specific heat capacity [J / (kg·K)]
- `Q` — heat energy added [J]
- `m` — mass [kg]
- `ΔT` — temperature change [K or °C]

LaTeX:

    c = \frac{Q}{m\,\Delta T}

Reference values (for shirt footnote or back print):
- Water: c = 4 182 J/(kg·K) — highest of common substances
- Aluminium: c = 900 J/(kg·K)
- Iron: c = 450 J/(kg·K)

Source: Cengel & Boles, *Thermodynamics: An Engineering Approach*, 8th ed. (2014), §3-5.
These are measured physical constants — no copyright attaches to numerical data or formulae.

## Visual direction

- **Primary element:** the equation `c = Q / mΔT` typeset in white on dark background
  (POD: black or navy shirt).
- **Layout:** equation centred, slogan in a lighter-weight font below. Clean sans-serif
  body text; equation in LaTeX mathtext (via `eq_render.py`).
- **Optional secondary element:** small material comparison bar chart (water vs. metals)
  as a footer, labelled "for context" — adds a reference-sheet feel consistent with other
  ScienceX designs.
- No illustrations required; the equation is the visual.

## Generation path

Step 1 — render the equation:

    python scripts/eq_render.py "c = \frac{Q}{m\,\Delta T}" \
        --dpi 300 --fontsize 80 --color white \
        --output designs/specific-heat-capacity/eq.png

Step 2 — compose in Canva / Inkscape: place eq.png on a black or navy background, add
slogan text below, add optional water/aluminium/iron bar chart at the bottom.

Step 3 — export at print resolution (≥ 300 DPI, min 4500×5400 px for a standard 15×18
Printify shirt) and upload directly; do not commit the full-res file.

## License

All equations are mathematical facts and carry no copyright.
Cengel & Boles is cited as a secondary source; no text or figures from the book are reproduced.
All visual output is original (code-generated via `eq_render.py`).
No third-party assets required.

## Status

Draft — ready for visual composition.

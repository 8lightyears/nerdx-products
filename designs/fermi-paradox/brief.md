# Design brief: Fermi Paradox

**Status:** ready for production  
**Theme group:** Thought Experiments (`themes/thought-experiments.md` §5)  
**Product type:** T-shirt, poster, mug

---

## Idea

The Milky Way is ~13.6 billion years old. Even at 0.1% of the speed of light, a
spacefaring civilisation could colonise the entire galaxy in roughly 100 million
years — 1/100th of its age. Yet we have detected nothing: no signals, no
megastructures, no visitors. Enrico Fermi asked the obvious question at a Los Alamos
lunch in 1950: *"Where is everybody?"* Nobody has answered it since.

---

## Copy / slogan options

**Option A (primary — text-only, maximum impact):**  
> WHERE IS EVERYBODY?
> 
> Fermi, Los Alamos, 1950.

**Option B (data-table variant):**  
> Galaxy age: 13.6 Gyr  
> Colonisation time (0.001c): ~0.1 Gyr  
> Detections: 0
> 
> WHERE IS EVERYBODY?

**Option C (attribution with implication):**  
> The Fermi Paradox.  
> Still unanswered.

Recommendation: Option A for the shirt (stark, instantly striking). Option B for the
poster (rewards closer reading). Option C as a mug variant.

---

## Visual direction

### Primary: text-dominant on deep star field

- **Background:** Deep-space star field. Two options, both PD-safe:
  - *Option 1:* Procedurally generated (Matplotlib, see `generate/star_field.py`).
    ~3,000 white dots at random positions, brightness scaled by a power-law
    distribution to mimic the real magnitude distribution. Add 3–5 brighter stars
    (enlarged dots with a soft Gaussian glow). Black background.
  - *Option 2:* NASA Hubble Heritage image — PD as NASA/ESA US government work.
    Best choices: Hubble Deep Field (1995, HDF-N), Hubble Ultra Deep Field (2004),
    or a dense star-cluster image. Credit required: "NASA, ESA, STScI".
- **Text:** "WHERE IS EVERYBODY?" centred, large, white, clean sans-serif
  (Inter, Roboto, or Helvetica — any free font is fine; monospace is not needed
  here). All caps. Generous letter-spacing.
- **Below:** "Fermi, Los Alamos, 1950." in a smaller weight — same typeface,
  lighter weight (300 or 400 vs. 700 for the main line).
- **Tone:** Austere. No humour. The silence of the star field is the point.

### Secondary: annotated star field (Option B poster variant)

- Same background.
- Data table (right-justified, monospace, smaller text):
  - "Stars in Milky Way: ~2 × 10¹¹"
  - "Fraction with planets: > 50%"
  - "Fraction potentially habitable: ~10%"
  - "Civilisations detected: 0"
- Source for planet fraction: Dressing & Charbonneau (2015), ApJ, 807(1), 45; and
  NASA Kepler mission results (PD — government science).
- "WHERE IS EVERYBODY?" centred below the table.

---

## Generation path

`designs/fermi-paradox/generate/star_field.py` — creates a 3300 × 3300 px
transparent-background star field PNG suitable for dark-shirt POD upload.

Dependencies: `pip install matplotlib numpy`

Run: `python designs/fermi-paradox/generate/star_field.py`
Output: `designs/fermi-paradox/generate/star_field_3300.png` (full res, not committed)
Review sample: commit JPEG ≤ 300 KB to `designs/fermi-paradox/assets/`.

Text overlay is added in any design tool (Canva, Inkscape, GIMP) as a separate layer,
or rendered directly in the script by adding `ax.text()` calls after the star scatter.

---

## License

- **Concept:** PD mathematical/scientific question. No copyright.
- **Source text:** Jones (1985), LA-10311-MS is a US government work — PD on
  publication. Fermi's spoken question was never published by him.
- **Procedural star field:** Original output of original code — no license concerns.
- **NASA Hubble option:** PD as NASA/ESA US government work. Credit: "NASA, ESA, STScI".
- **Typography:** Use OFL-licensed fonts only (Inter, Source Sans Pro, Roboto, etc.).
- **No third-party artwork required.**

---

## Sources

1. Jones, E.M. (1985). "Where is everybody? An account of Fermi's question."
   LA-10311-MS. Los Alamos National Laboratory. (US government work, PD.)
   Available: [LANL technical reports archive]
2. Hart, M.H. (1975). "Explanation for the absence of extraterrestrials on Earth."
   *Quarterly Journal of the Royal Astronomical Society*, 16, 128–135.
3. Dressing, C.D. & Charbonneau, D. (2015). "The occurrence of potentially habitable
   planets orbiting M dwarfs estimated from the full Kepler dataset and an empirical
   measurement of the detection sensitivity." *ApJ*, 807(1), 45.
4. NASA Hubble Heritage: https://hubblesite.org/images/hubble-heritage (accessed 2026-06-27).

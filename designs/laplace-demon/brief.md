# Design Brief: Laplace's Demon

**Status:** draft
**Theme group:** Thought Experiments (`themes/thought-experiments.md` §4)

---

## Idea

Laplace (1814) argued that a sufficiently powerful intellect — knowing all positions and
forces in the universe at one instant — could predict every future event perfectly. The
universe as a clockwork machine; determinism made explicit. The "demon" was broken first
by Heisenberg (1927, uncertainty principle) and again by Lorenz (1963, chaos theory /
butterfly effect). Three ideas, one shirt.

---

## Quote (public domain)

> "An intellect which at a certain moment would know all forces that set nature in motion,
> and all positions of all items of which nature is composed, if this intellect were also
> vast enough to submit these data to analysis, it would embrace in a single formula the
> movements of the greatest bodies of the universe and those of the tiniest atom; for it
> nothing would be uncertain and the future just like the past would be present before its
> eyes."

— Pierre-Simon Laplace, *Essai philosophique sur les probabilités* (1814)
English translation: Truscott & Emory (1902), public domain.

---

## Slogans

1. **"An intellect vast enough…"** — 1814 — minimal, lets the quote do the work
2. **"The universe as equation. (Broken 1927.)"** — punchy, physicist-friendly
3. **"Laplace's demon. Heisenberg's ghost."** — two-liner, high conversation value

Recommended primary: option 3. Option 2 as back-print alternative.

---

## Visual direction

**Main panel — front:**
- Central: a large, intricate clockwork gear assembly (3–5 nested gears, fine-tooth
  detail). At the hub: a stylised all-knowing eye or schematic brain. Gear teeth carry
  tick marks like a ruler — implying measurement and precision.
- Below the gears: the Laplace quote in a compact serif font (2–3 lines, justified).
  Byline: "P.-S. Laplace, 1814" in small caps.
- Slogan (option 3 or 2) at top or bottom, clean sans-serif.
- Palette: black ink on white, or ivory/cream on black — engraving aesthetic fits the
  18th-century source.

**Optional second panel — back (premium variant):**
- Split: left half shows ψ|Ψ⟩ (Dirac notation, Heisenberg 1927); right half shows a
  Lorenz attractor butterfly curve (Lorenz 1963).
- Caption: "broken by uncertainty — broken again by chaos"
- This panel can be omitted for a cleaner single-sided shirt.

**Generation approach:**
- Clockwork diagram: `generate/clockwork.py` — Matplotlib, parametric gear teeth
  (involute profile approximated with circular arcs), exported as SVG for print.
- Lorenz attractor: `generate/lorenz.py` — simple Euler integration, Matplotlib,
  SVG export. (Or reference `scripts/eq_render.py` for equation typesetting.)
- Both scripts output SVG; final composition in Inkscape or Affinity Designer.

---

## License

- Laplace 1814 text: public domain (author died 1827, published 1814).
- Truscott & Emory 1902 translation: public domain (published before 1927, US).
- Clockwork diagram: original work — no IP issue.
- Lorenz attractor / Heisenberg notation: mathematical fact / equation — no copyright.
- All assets original or PD. No third-party IP.

---

## Sources

- Laplace, P.-S. (1814). *Essai philosophique sur les probabilités*. Paris: Courcier.
  English trans.: Truscott, F.W. & Emory, F.L. (1902). New York: Wiley. Public domain.
- Heisenberg, W. (1927). Über den anschaulichen Inhalt der quantentheoretischen Kinematik
  und Mechanik. *Zeitschrift für Physik*, 43, 172–198.
- Lorenz, E.N. (1963). Deterministic Nonperiodic Flow. *Journal of the Atmospheric
  Sciences*, 20(2), 130–141.
- Wikipedia: Laplace's demon — https://en.wikipedia.org/wiki/Laplace%27s_demon
  (checked 2026-06-28).

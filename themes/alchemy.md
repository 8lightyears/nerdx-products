# Theme Group: Alchemy

**Scope:** Alchemical symbols, process diagrams, and cosmological illustrations from
16th–17th-century publications. All source material pre-dates 1927 by centuries — US
public domain by publication date, and the original authors died 400+ years ago.

**Why it fits the shop:** Alchemy sits at the intersection of proto-science, mysticism,
and visual richness. The imagery is immediately striking (nested spheres, winged serpents,
cosmic diagrams) while the underlying ideas are genuinely interesting — chemistry, medicine,
and natural philosophy before modern categories existed. The "real science backstory" angle
is strong: the four stages of the Magnum Opus correspond to real colour changes in chemical
reactions; Paracelsus's Tria Prima was the first systematic attempt to classify matter by
properties rather than Aristotelian elements. These are conversation-starters, not just
decoration.

---

## Sub-idea 1: General alchemical symbols and emblems

**Concept:** A symbols-reference shirt — the major alchemical glyphs arranged as a
compact reference grid, with element/planet correspondences. Could also work as a
"periodic table before the periodic table" format.

**Key symbols:**
- Planetary metals: Sun/Gold ☉, Moon/Silver ☽, Mercury/Quicksilver ☿, Venus/Copper ♀,
  Mars/Iron ♂, Jupiter/Tin ♃, Saturn/Lead ♄
- The four classical elements: Fire △, Air △̄, Water ▽, Earth ▽̄ (with bar)
- Quintessence (⊕ or ✡), Sulfur, Mercury, Salt (Paracelsian)

**Visual direction:** Clean vector reconstruction from PD originals. The glyphs
themselves are mathematical/alchemical conventions — no copyright claim on the symbols.

**Best source for emblem plates:**
- *Atalanta Fugiens* (Michael Maier, 1618): 50 copper engravings with alchemical
  allegories + musical canons. Full scan at Internet Archive:
  https://archive.org/details/atalantafugiensh00maie (accessed 2026-06-25). Published
  Oppenheim, 1618. US PD; author died 1622.
- *Symbola Aureae Mensae* (Michael Maier, 1617): another emblem collection. Archive:
  https://archive.org/details/symbolaureaemens00maie (accessed 2026-06-25).

**License:** Symbols/glyphs = uncopyrightable conventions. PD plate engravings may be
used directly; clean-up via ImageMagick. Original vector reconstruction needs no license.

---

## Sub-idea 2: Four stages of transformation — the Magnum Opus colour sequence

**Concept:** A colour-gradient shirt with four panels or a single arc, each labelled
with the Latin stage name. Narrative: the alchemical Great Work maps onto real chemistry.

**The four stages:**
1. **Nigredo** (blackening, Latin: *nigredo*) — putrefaction; dissolution of the prima
   materia; colour black. Chemical correlate: oxidation of metals producing black oxides
   (e.g. CuO from copper). Historically associated with lead.
2. **Albedo** (whitening, Latin: *albedo*) — purification; colour white. Chemical correlate:
   reduction to silver-white (e.g. reduction of lead oxide to lead). Symbol: the White Queen.
3. **Citrinitas** (yellowing, Latin: *citrinitas*) — solar dawning; colour yellow-gold.
   Often omitted in later texts (subsumed into Rubedo). Chemical correlate: formation of
   gold-coloured sulfides or approach to the Philosopher's Stone.
4. **Rubedo** (reddening, Latin: *rubedo*) — completion; colour red. The Stone achieved.
   Chemical correlate: red mercuric sulfide (cinnabar, HgS) or red gold.

**Science hook:** Carl Jung's *Psychology and Alchemy* (1944) mapped the sequence to
psychological individuation, making it known outside occult circles. But the stages
describe real colour changes observed in wet chemical processes — documented in
*Rosarium Philosophorum* (1550) and *Splendor Solis* (c. 1582).

**Primary source for imagery:**
- *Splendor Solis* (Salomon Trismosin, c. 1582, Latin; 1598 German edition). The British
  Library holds MS Harley 3469 (c. 1582). The BL digitised version is free to use for
  non-commercial PD images; the illustrations are unambiguously PD by date. Wikimedia
  Commons hosts many plates (search "Splendor Solis"):
  https://commons.wikimedia.org/wiki/Category:Splendor_Solis (accessed 2026-06-25).
- *Rosarium Philosophorum* (1550, Francofurti). Plates reprinted in many 19th-c. editions,
  all US PD.

**Visual direction:** Either use PD plates directly (with ImageMagick cleanup) or
generate a purely original colour-gradient arc using `scripts/eq_render.py` + Matplotlib.
The gradient itself (black → white → yellow → red) is distinctive and original.

**Shirt copy:** "Nigredo. Albedo. Citrinitas. Rubedo." (Latin, four panels) — elegant,
mysterious, invites "what does that mean?"

---

## Sub-idea 3: Tria Prima — Paracelsus's three primes

**Concept:** A triangle shirt. Mercury (Spirit) — Sulfur (Soul) — Salt (Body). One of
the first systematic attempts in Western thought to classify matter by observable
properties rather than Aristotelian elements.

**Background:**
- Paracelsus (Philippus Aureolus Theophrastus Bombastus von Hohenheim, 1493–1541)
  proposed that all matter contains three principles: Mercury (volatility, fluidity),
  Sulfur (combustibility, the fire principle), and Salt (solidity, the residue after
  burning).
- This was a genuine paradigm shift: it focused on *what things do* (their properties)
  rather than *what they are made of* in the abstract Aristotelian sense. Anticipates
  phlogiston theory and, distantly, modern functional classification.
- Source: Paracelsus, *Opus Paramirum* (c. 1530, published posthumously 1562).
  *Astronomia Magna* (1537/1571). Both PD.

**Visual direction:** Equilateral triangle with the alchemical symbols:
- Mercury ☿ (Spirit) — top vertex
- Sulfur 🜍 (Soul) — bottom left
- Salt 🜔 (Body) — bottom right

The Unicode alchemical symbols (U+1F700–U+1F77F, added in Unicode 6.0, 2010) are
freely usable; they are standardised code points, not copyrightable artwork. For a
higher-fidelity design, redraw from the PD engravings in:
- *Philosophia Reformata* (Johann Daniel Mylius, 1622, Francofurti). Full scan:
  https://archive.org/details/philosophiareform00myli (accessed 2026-06-25). Author
  died c. 1642; US PD.

**Shirt copy options:**
- "Mercury. Sulfur. Salt. — Paracelsus, 1530." (minimalist triangle)
- "Spiritus. Anima. Corpus. — The three principles." (Latin)
- Triangle only, symbols only, no text — for the audience that knows.

---

## Sub-idea 4: Robert Fludd macrocosm diagram

**Concept:** Print/shirt of Fludd's *integra naturae* diagram — the nested concentric
spheres mapping minerals → plants → animals → humanity → angels → God. One of the most
visually spectacular diagrams in early modern natural philosophy.

**Background:**
- Robert Fludd (1574–1637), English physician and Rosicrucian. *Utriusque Cosmi,
  Maioris scilicet et Minoris, Metaphysica, Physica Atque Technica Historia*,
  Vol. 1 (1617, Oppenheim, published by Johann Theodor de Bry). Vol. 2 (1619–1621).
- The *integra naturae speculum artisque imago* plate (usually called the "macrocosm
  diagram"): a human figure at the centre, surrounded by concentric rings labelled with
  the spheres of the cosmos, with a chain linking the human to a central circle
  (representing the Cosmic Monkey / *simia naturae* — nature imitates God). The outermost
  ring is labelled *Deus* / *Angeli* / *Aether* / *Elementum* / *Minerale* / *Vegetabile*
  / *Sensibile* / *Homo* inward.
- The diagram appeared on the frontispiece-equivalent of Vol. 1. It is the most
  reproduced image from Fludd's work.

**PD source:**
- Archive.org scan of the 1617 edition:
  https://archive.org/details/utriusquecosmim00flud (accessed 2026-06-25).
  Published 1617, author died 1637 — unambiguously US PD.
- Wikimedia Commons: "Robert Fludd — Integra Naturae":
  https://commons.wikimedia.org/wiki/File:RobertFludd_Integra_Naturae.jpg
  (accessed 2026-06-25; file tag: PD-old-100).

**License:** PD-old-100 (author died 1637; published 1617). The Wikimedia file is tagged
as public domain. Use the Wikimedia file or the Archive.org scan; apply ImageMagick
halftone cleanup (`-morphology Erode Disk:1 -auto-level -unsharp 0x1`). The resulting
cleaned image is original artwork derived from a PD source — no license concern.

**Visual direction:**
- Full diagram as a large-format print (better suited to poster/mug than t-shirt due
  to fine detail).
- Crop the central figure + innermost rings as a shirt graphic, with title text.
- Or: redraw in clean vector from the original engraving, retaining the nested-rings
  structure but modernising the linework.

**Shirt copy:** "Integra Naturae — R. Fludd, 1617" as a discreet caption.

---

## Recommended launch order

1. **Tria Prima triangle** (Sub-idea 3) — simplest to produce (vector, no PD plate cleanup);
   clean, modern-looking; strong science hook; works on shirt without fine detail issues.
2. **Magnum Opus gradient** (Sub-idea 2) — pure original colour work; Latin labels;
   highly distinctive; no license concern whatsoever.
3. **Fludd macrocosm** (Sub-idea 4) — best as a print or large mug rather than a shirt;
   needs ImageMagick cleanup; highest visual impact once done.
4. **General symbols grid** (Sub-idea 1) — solid as a companion piece to Tria Prima;
   requires sourcing or vectorising the glyphs.

---

## Automation notes

- Tria Prima and symbol grid: `scripts/eq_render.py` can render the alchemical Unicode
  glyphs at high DPI; combine with Matplotlib for the triangle layout. No external images
  needed.
- Magnum Opus gradient: pure Matplotlib gradient arc + text labels, ~20 lines.
- Fludd diagram: download from Archive.org, run ImageMagick cleanup, crop/colour-adjust
  in Pillow or GIMP.

---

## Sources

- Paracelsus, *Opus Paramirum* (c. 1530/1562). PD.
- Michael Maier, *Atalanta Fugiens* (1618). Internet Archive https://archive.org/details/atalantafugiensh00maie. PD.
- Salomon Trismosin, *Splendor Solis* (c. 1582). Wikimedia Commons Category:Splendor_Solis. PD.
- Robert Fludd, *Utriusque Cosmi* Vol. 1 (1617). Internet Archive https://archive.org/details/utriusquecosmim00flud. PD.
- Wikimedia Commons, "Robert Fludd — Integra Naturae" (accessed 2026-06-25). PD-old-100.
- C.G. Jung, *Psychology and Alchemy* (1944), for the Jungian Magnum Opus mapping — note this book is NOT PD; only cite the idea, not the text.

# "My wife is a Witch" theme group

## Scope

A relationship-humor sub-line where ordinary domestic devotion — supplements, hydration,
cooking — is reframed through a nerd's fantasy vocabulary. The husband is wary; the wife is
quietly, competently running things. The tone is affectionate, self-deprecating, and legible
to anyone in a long-term relationship with someone health-conscious.

**Shop-fit note.** This theme sits at the edge of the shop's stated spirit ("real, checkable
idea"). The fantasy references are real cultural artefacts (Tolkien, folklore, alchemy), but
the primary driver is relationship humour, not science education. Treat as a complementary
sub-line rather than the shop's core. The products work best when they smuggle in a genuine
nerdy angle — a real alchemical symbol, a literary allusion with a checkable source, an
actual chemical formula for the supplement in question.

---

## Sub-ideas

### 1. Supplement/vitamin gags

**Concept.** "Honey, your vitamins." Text-only or minimal-illustration design. The joke: the
wife presents supplements with the same energy as an alchemist dispensing elixirs. Variants:

- Pure text: `"Honey, your vitamins."` in gothic or serif font, with a small apothecary
  label reading the actual molecular formula (e.g., "Vitamin D₃ — Cholecalciferol,
  C₂₇H₄₄O — synthesised endogenously from 7-dehydrocholesterol under UVB radiation.")
  — now the shirt is *also* correct biochemistry.
- Visual: row of supplement bottles labelled with archaic apothecary-style names and modern
  IUPAC formulas side by side.
- Slogans: *"Honey, your vitamins."* / *"Honey, it's just magnesium glycinate."* (with the
  structural formula underneath).

**The nerdy hook:** real biochemistry of the supplement. Vitamin D, magnesium, zinc — all
have verifiable structures, synthesis pathways, and metabolic roles. The formula *is* the
checkable idea; the delivery mechanism is relationship humour.

**Sources:** PubChem database (pubchem.ncbi.nlm.nih.gov) — all formula data is factual and
in the public domain (government-funded database, accessed 2026-06-24).

**Visual direction:**
- Apothecary label aesthetic: serif font, aged cream-paper background, border rules
- Or modern-minimalist: clean sans-serif, white background, structural formula rendered with
  `scripts/eq_render.py`
- Dark-academia and dark-fantasy variants both viable

**Automation.** Structural formulas can be rendered with the RDKit or rdkit2svg Python
library, or drawn manually as SVG for simple molecules. Supplement formulas are simple
enough to render with Matplotlib mathtext.

**License.** All molecular structures are factual; no copyright. Apothecary aesthetic
is a genre — no specific source needed. All text is original.

---

### 2. Hydration insistence

**Concept.** "Darling, drink — you mustn't be dehydrated." The husband's wariness; the water
glass as a portal or potion.

- Text-only: the quote in an old-fashioned serif, with a footnote: "~2 L/day recommended —
  European Food Safety Authority, 2010."
- Visual: a plain glass of water rendered in a 19th-century scientific-illustration style
  (cross-section with measurement lines, Latin label *Aqua pura*, H₂O formula)

**The nerdy hook:** H₂O is one of the most studied molecules in chemistry (hydrogen bonding,
anomalous properties). A shirt about drinking water can carry a real scientific claim: water's
high heat capacity (4.18 J/g·°C) is why life as we know it exists.

**Sources:** EFSA Journal (2010) 8(3):1459 — adequate water intake guidance; NIST Chemistry
WebBook for H₂O physical constants.

**License.** EFSA guidance is a public document (facts, not copyrightable). H₂O formula and
physical constants are facts. Any illustration must be original.

---

### 3. "My wife cooking dinner" / "my wife and mother-in-law cooking dinner"

**Concept.** The kitchen-as-alchemical-laboratory framing. Two variants:

**Variant A — Alchemical process diagram.** A 17th-century-style alchemical diagram
(genuine PD source) relabelled: instead of *Solve et Coagula* or *Vitriol*, the vessels are
labelled "olive oil," "bay leaf," and "stock." The distillation apparatus becomes a stovetop
reduction. Checkable source: genuine PD alchemical plates.

- PD source candidate: J.B. van Helmont's *Ortus Medicinae* (1648) — PD; illustrations
  available via HathiTrust and Wellcome Collection.
- Or: Libavius *Alchymia* (1606) — extensive copper-engraved alchemical apparatus diagrams;
  PD; HathiTrust scans available.

**Variant B — Periodic table of dinner ingredients.** A parody periodic table where each
element cell contains an ingredient (Na = Salt, Fe = Spinach, Zn = Pumpkin seeds) with its
actual elemental symbol and atomic mass preserved. The grid is the periodic table layout;
the content is food.

The periodic table layout is not copyrightable (it is a scientific fact). The text/design
of a specific periodic table poster may be copyrighted — but building a new layout from
scratch is fine.

**Variant C — Mother-in-law edition.** Two overlapping alchemical circles (Venn diagram)
labelled "my wife's recipe" and "my mother-in-law's recipe" — the intersection reads
"nuclear conflict."

**The nerdy hook (Variant A):** real PD alchemical illustrations with a food relabelling.
**The nerdy hook (Variant B):** real elemental data (atomic numbers, masses) in a parody
tabular layout.

**Sources:**
- Libavius *Alchymia* (1606): HathiTrust Digital Library, handle 2027/ucm.5317019 (PD)
- Van Helmont *Ortus Medicinae* (1648): Wellcome Collection, CC BY 4.0
- Periodic table element data: NIST Atomic Weights and Isotopic Compositions (facts, PD)

**License.** Alchemical plates: PD (pre-1700, well past 1927). Periodic table data: facts.
Mother-in-law Venn: entirely original.

---

### 4. "My wedding" — dark eye motif

**Concept.** A couple at an altar. Above the spouse, a stylised dark eye motif. Caption:
"And he said: I do." Sub-caption (optional): "He meant it in the Tolkien sense."

**License concern.** The *Eye of Sauron* as depicted in Peter Jackson's films is © New Line
Cinema (2001–2003). Tolkien's prose description is copyright of the Tolkien Estate. Neither
can be reproduced.

**Mitigation options:**

1. **Original dark eye** — design an original stylised eye (vertical pupil, radiating iris,
   dark colouration) that is generically menacing without reproducing the specific cinematic
   design. No copyright in the concept of an evil eye.

2. **The Nazar (evil eye)** — Turkish/Mediterranean protective amulet (blue eye bead): a
   real-world cultural artefact, ancient, not copyrightable as a concept. An original
   illustration of the nazar amulet is fully usable. Strong cross-cultural recognition.

3. **Literary quote approach** — use the phrase "One Ring to rule them all" in fine print
   beneath a ring diagram... but this is quoting copyrighted text (Tolkien Estate). Avoid.

4. **Caption-only design** — "I do. (He meant it in the Tolkien sense.)" — no visual; pure
   text. The cultural allusion is clear; the text is original; no copyright issue.

**Recommended approach:** Option 1 (original dark eye) or Option 4 (caption-only). Verify
with legal before printing if using any recognisable Eye of Sauron likeness.

**The nerdy hook:** the Tolkien allusion is recognisable to the audience; the concept of
vows-as-binding-oath is ancient. Not strong science, but legitimate cultural literacy.

---

## Shop-fit assessment

| Sub-idea | Nerd hook | Science anchor | Effort | License risk |
|---|---|---|---|---|
| Supplements / biochem | Strong (molecular formula) | High | Low | None |
| Hydration | Medium (H₂O properties) | Medium | Low | None |
| Wife cooking — alchemical | Strong (PD plates) | Medium | Medium | Low (use PD sources) |
| Wife cooking — periodic table | Strong (real element data) | High | Medium | None |
| Wedding — dark eye | Weak (pop culture, not science) | None | Medium | High (avoid Tolkien IP) |
| Wedding — caption-only | Medium (cultural literacy) | None | Low | None |

**Recommended starting points:**
1. Supplements with a real biochemistry formula (instant conversion of relationship humor →
   science shirt; uses existing `scripts/eq_render.py`)
2. "Periodic table of dinner ingredients" (parody with real elemental data; automatable)

The wedding dark-eye concept is high-risk and low-science; defer or use caption-only variant.

---

## Visual notes

- Gothic / dark-academia aesthetic fits the witch framing; ensure text remains legible at
  small print sizes.
- Apothecary label style (Variant 1 supplements) must use original artwork or PD engravings;
  no stock-photo herbs.
- See `docs/taste.md` for live owner preferences.

---

## License summary

| Asset | Source | License |
|---|---|---|
| Molecular formulas | PubChem (NCBI) | Facts — PD |
| H₂O physical constants | NIST WebBook | Facts — PD |
| Alchemical plates | Libavius 1606 / Van Helmont 1648 | PD (pre-1700) |
| Periodic table data | NIST Atomic Weights | Facts — PD |
| Eye of Sauron likeness | New Line Cinema / Tolkien Estate | © — DO NOT USE |
| Nazar eye motif | Ancient cultural symbol | PD as concept; draw original |
| All text | Original | No license required |

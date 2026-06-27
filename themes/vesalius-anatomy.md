# Vesalius Anatomy Theme Group

**Scope:** Products built around Andreas Vesalius's *De Humani Corporis Fabrica* (1543)
and the broader history of anatomical illustration — a moment when observation replaced
dogma and a single book contained both rigorous science and spectacular art.

**Why it fits the shop:** The muscle-man plates are instantly recognisable, scientifically
verifiable, aesthetically stunning at print scale, and carry a genuine story: Vesalius
proved that Galen — the dominant medical authority for 1,300 years — had never dissected
a human body. The product is a conversation-starter before the buyer even reads the copy.

---

## Asset pools and license status

**Primary source — Wellcome Collection digital library**
- URL: https://wellcomecollection.org/works (search "Vesalius")
- License: CC BY 4.0 — full commercial use permitted
- Resolution: high (suitable for print-ready output)
- Access date checked: 2026-06-27
- The Wellcome Collection holds multiple scans of Fabrica (1543 and 1555 editions) at
  high resolution. Individual images are CC BY 4.0 per Wellcome's standing policy for
  public-domain works in their collection.

**Secondary source — Internet Archive**
- URL: https://archive.org/details/andreae-vesalii-bruxellensis-dc
- License: PD (original work 1543, well within any jurisdiction's PD threshold)
- Notes: full scan available; quality varies by scan; Wellcome preferred for print work

**Original work copyright status**
- *De Humani Corporis Fabrica Libri Septem*, Basel: Oporinus, 1543
- Vesalius (1514–1564): died 1564 — EU PD (life+70 = 1634), US PD (published before 1928)
- Illustrations attributed to Jan van Calcar (d. ~1546), Titian's workshop
- PD status: unambiguous worldwide

---

## Sub-ideas

### 1. The Muscle Man series
The most iconic plates: a sequence of ecorché ("flayed") figures showing progressive
muscle dissection, posed heroically in Flemish/Italian landscape backgrounds. The poses
mimic classical sculpture — deliberate, to assert that anatomy was a noble science.

- **Shirt product:** One muscle-man figure, full chest print, dark fabric
- **Slogan options:**
  - "Every muscle, accounted for. Basel, 1543."
  - "Built like a Renaissance man."
  - "Galen had not dissected a human body. Vesalius did."
- **Visual direction:** Single ecorché figure from plate III or VII of Book II; landscape
  background retained (adds depth and historical flavour); anatomical labels removed or
  kept selectively (full-label variant for poster; label-free for shirt)
- **Production:** Wellcome scan → ImageMagick threshold/curves cleanup → white-to-transparent
  → Matplotlib or Inkscape for label layer (optional)
- **Notes:** The series of 14 progressively-stripped muscle figures is also viable as a
  mug series (one per mug) or a collector's print set

### 2. The Skeleton in a Landscape
Separate from the muscle series: a full-skeleton figure posed contemplatively — one plate
has the skeleton leaning on a shovel, in a graveyard landscape, as if meditating on
mortality. The visual is powerful with no copy needed.

- **Slogan options:**
  - "Homo bulla est." (Man is a bubble — Erasmus, contemporary proverb)
  - "Vesalius, 1543." (minimal)
  - None — image-only variant
- **Source:** Wellcome Collection, Book I skeletons (facing pages of articulated and
  disarticulated skeleton)
- **Notes:** The contemplative skeleton is a strong candidate for a poster / print; the
  "memento mori" aesthetic is commercially proven and niche-differentiated by the 1543
  provenance

### 3. "Galen Was Wrong" — the correction shirt
Vesalius discovered at least 200 errors in Galen. The corrective moment is the story.

- **Shirt concept:** Two-column layout — Galen's incorrect claim (left, struck through)
  vs. Vesalius's correction (right) — for 3–4 well-known examples
- **Examples:**
  - Galen: "Liver has five lobes" / Vesalius: "Two" (he counted — from human dissection)
  - Galen: "Septum cordis is perforated" / Vesalius: "It is solid" (challenged blood theory)
  - Galen: "Jaw is two bones" / Vesalius: "One" (Galen worked on dog jawbones)
- **Slogan:** "1,300 years of authority. Overturned by looking."
- **Source:** Vesalius himself lists the corrections in Fabrica Book VII; also O'Malley,
  *Andreas Vesalius of Brussels* (1964) for secondary summary
- **Notes:** No illustration required — typography-only variant is viable and avoids any
  art sourcing entirely; all corrections are documented historical facts

### 4. The Brain and Ventricle plates
Fabrica Book VII contains elaborate brain dissection plates — sequential slices exposing
the ventricles. Medieval theology placed the soul in the ventricles; Vesalius's plates are
directly subversive of that idea.

- **Shirt/poster concept:** One cross-section plate, labelled "The Soul was here." or
  "Ventriculus quartus, 1543. No soul found."
- **Source:** Wellcome Collection Book VII plates; high resolution available
- **License:** CC BY 4.0 (Wellcome)
- **Notes:** More niche than the muscle man; stronger for a poster or oversized print

### 5. Anatomical dissection theatre (frontispiece)
The Fabrica frontispiece shows Vesalius dissecting before a crowd in a purpose-built
theatre — a landmark image of public science replacing private mysticism.

- **Poster concept:** Full frontispiece, with copy overlaid at the margin:
  "The first anatomy theatre. Padua, 1543."
- **Source:** Wellcome Collection, same scan set
- **Notes:** Very complex composition — better as a poster (A2/A3) than a shirt; could be
  a limited-edition print

---

## Visualisation and automation notes

- **ImageMagick cleanup pipeline** (same as patent-drawings.md):
  `convert input.jpg -colorspace Gray -threshold 75% -white-threshold 90% output.png`
  then `convert output.png -fuzz 5% -transparent white output-transparent.png`
- **Label layer:** Fabrica plates already carry Latin anatomical labels. These can be
  retained (educational poster) or masked out (clean shirt print). Masking with GIMP or
  Inkscape by hand is the practical path for the first design.
- **Colour treatment:** Dark t-shirt = white-on-black inversion; poster = original sepia
  tone retained (warm aesthetic); mug = monochrome

---

## Recommended launch order

1. **Muscle man (plate III or IV, Book II)** — Wellcome CC BY 4.0 source ready, iconic,
   proven commercial appeal (anatomy + classical pose), "Every muscle, accounted for."
2. **"Galen Was Wrong" corrections shirt** — typography-only, zero illustration cost,
   high nerd-credibility
3. **Contemplative skeleton** — poster/print product, memento mori aesthetic
4. **Brain ventricle plate** — once the muscle man validates the theme

---

## Sources

- Vesalius, A. (1543). *De Humani Corporis Fabrica Libri Septem*. Basel: Oporinus.
  [Internet Archive scan: https://archive.org/details/andreae-vesalii-bruxellensis-dc]
  [Wellcome Collection: https://wellcomecollection.org/works — CC BY 4.0]
- O'Malley, C.D. (1964). *Andreas Vesalius of Brussels, 1514–1564*. Berkeley: UC Press.
  (Secondary source for the Galen-correction count and historical context; PD facts)
- Siraisi, N. (1994). "Vesalius and Human Diversity in *De Humani Corporis Fabrica*."
  *Journal of the Warburg and Courtauld Institutes*, 57, 60–88. (Scholarly context)
- Wellcome Collection CC BY 4.0 licence policy:
  https://wellcomecollection.org/pages/Wvlk4yAAAB8A3ufp (accessed 2026-06-27)

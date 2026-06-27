# Design Brief: Vesalius Muscle Man

**Status:** concept — ready for production
**Theme group:** Vesalius Anatomy (`themes/vesalius-anatomy.md`)
**Product type:** T-shirt (primary), poster (secondary)

---

## Idea

Andreas Vesalius published *De Humani Corporis Fabrica* in 1543 — the first human anatomy
atlas based on actual dissection. The ecorché (flayed) muscle-man figures are posed like
classical statues in Italian landscapes. Each figure shows progressively deeper muscle
dissection: skin gone, then superficial muscles, then deep muscles, then the skeleton
holding its own organs.

The product: one muscle-man figure on a dark shirt, with copy that tells the story.

**The hook:** Galen — the anatomical authority for 1,300 years — never dissected a human
body. He worked on apes and pigs and extrapolated. Vesalius proved this by looking.
The shirt is a monument to a man who decided to check.

---

## Copy options

**Option A — minimal, date-forward:**
```
Every muscle, accounted for.
Basel, 1543.
```

**Option B — the correction story:**
```
Galen: 1,300 years.
Vesalius: one book.
He checked.
```

**Option C — equation format:**
```
Musculus latissimus dorsi
Origin: T7–T12 spinous processes
Insertion: bicipital groove
Action: extends, adducts, medially rotates arm
[small Vesalius label-style annotation]
```
(Option C pairs well with the muscle-label variant for a more technical poster)

---

## Visual direction

**Source plate:** Book II, plate 3 or plate 4 of *De Humani Corporis Fabrica* (1543)
— the third or fourth muscle-man figure in the ecorché sequence. The third figure shows
deep superficial muscles with arms slightly raised; the fourth reveals the deeper layer.
Plate 3 is preferred: it has the most striking pose and is the most reproduced.

**Composition:**
- Full-figure, centred on chest
- Landscape background retained (low contrast — the Flemish/Italian countryside fades
  into the background on dark fabric; the figure reads as the main subject)
- Anatomical labels: removed for the shirt (clean figure only); retained for the poster
- White on black (shirt); sepia on cream (optional poster variant)

**Processing pipeline:**
1. Download high-resolution scan from Wellcome Collection (CC BY 4.0)
   → search: "Vesalius muscle man" at https://wellcomecollection.org/works
   → select Book II plate 3 or 4; download TIFF
2. GIMP or ImageMagick: boost contrast, convert to greyscale, invert (white-on-black)
   ```
   convert input.tiff -colorspace Gray -contrast-stretch 2%x2% \
     -negate output-shirt.png
   ```
3. Mask background to full black (threshold ~85%) so the figure reads clean on the shirt
4. Place copy in a matching period-style serif font (e.g. EB Garamond, SIL OFL 1.1)

**Review sample target:** long edge 1200 px, JPEG quality 80, < 300 KB

---

## License

| Asset | Source | License |
|---|---|---|
| Vesalius muscle-man plate | Wellcome Collection (CC BY 4.0) | Commercial use permitted; attribution required |
| EB Garamond typeface | Georg Mayr-Darmstadt / Google Fonts | SIL Open Font Licence 1.1 — commercial use permitted |
| Copy text | Original (this brief) | N/A |

Attribution line for print verso or product description:
> After Andreas Vesalius, *De Humani Corporis Fabrica* (Basel, 1543).
> High-resolution scan © Wellcome Collection, CC BY 4.0.

---

## Production steps

1. Retrieve Wellcome Collection TIFF for Book II plate 3
2. Process with ImageMagick pipeline above → `shirt-white-on-black.png`
3. Compose with copy in EB Garamond; save print-ready 300 DPI PNG outside repo
4. Commit review sample (≤ 1200 px long edge, ≤ 300 KB JPEG) to `assets/`
5. Upload to POD supplier (Printify / Printful) under product title:
   "Every Muscle, Accounted For — Vesalius 1543 Anatomy Shirt"

---

## Sources

- Vesalius, A. (1543). *De Humani Corporis Fabrica Libri Septem*. Basel: Oporinus.
- Wellcome Collection: https://wellcomecollection.org/works — CC BY 4.0
  (accessed 2026-06-27)
- EB Garamond: https://github.com/octaviopardo/EBGaramond12 — SIL OFL 1.1

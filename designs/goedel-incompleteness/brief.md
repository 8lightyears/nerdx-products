# Design brief: Gödel's Incompleteness

**Status:** ready for production  
**Theme group:** Logic and Computation (`themes/logic-and-computation.md` §3)  
**Product type:** T-shirt (primary), poster, mug

---

## Idea

In 1931, Kurt Gödel proved that any consistent formal system powerful enough to
express basic arithmetic contains true statements that the system cannot prove.
He did this by constructing a statement that says, in effect, "this statement has
no proof in this system" — and then showing that if the system is consistent, the
statement must be both true and unprovable. The result shattered Hilbert's programme
of finding a complete, consistent foundation for all of mathematics.

The shop angle: the self-referential structure of the proof *is* the product. No
diagram needed. The statement on the shirt *is* the theorem.

---

## Copy / slogan options

**Option A (primary — typography-only, maximum viral potential):**  
> This statement has no proof in this system.
> 
> True. Unprovable. 1931.

**Option B (attribution variant):**  
> This statement cannot be proved in this system.
> 
> Kurt Gödel, 1931.  
> Every consistent system has blind spots.

**Option C (meta-label variant — wearable self-reference):**  
> GÖDEL SENTENCE G
> 
> "This statement has no proof in this system."
> 
> — if provable: contradiction. if false: contradiction.
> System is consistent. Statement is true. Statement is unprovable. ∎

**Option D (minimal — highest Redbubble/Etsy appeal):**  
> True but unprovable.
> 
> Gödel, 1931.

Recommendation: Option A for the shirt (self-contained, instantly puzzling). Option C
for the poster (rewards reading; shows the proof structure). Option D for the mug.

---

## Visual direction

### Primary: typography-only (Option A / D)

- **Background:** White (for textbook look) or very dark navy/charcoal (for
  chalkboard look). Both work for POD.
- **Main text:** Option A or D, centred, clean serif or sans-serif.
  - Serif (e.g. EB Garamond, Libre Baskerville — free OFL): gives a "mathematical
    theorem statement" feel, matches journal typography.
  - Sans-serif (e.g. Inter, Source Sans — free OFL): cleaner, more modern.
- **Secondary text:** Year and author in lighter weight, smaller size.
- **No illustration required.** The self-referential text is the entire design.

### Secondary: proof-structure diagram (Option C poster variant)

- **Box labelled "Gödel sentence G"** containing:
  > *"This statement has no proof in this system."*
- **Two arrow paths from the box:**
  - Arrow A: "Assume G is provable" → red ✗ → "Then G is false" →
    red ✗ → "But it says it's unprovable — contradiction" →
    **"System is inconsistent."**
  - Arrow B: "Assume G is false" → red ✗ → "Then G is provable" →
    red ✗ → "But consistent systems only prove true things — contradiction" →
    **"System is inconsistent."**
- **Conclusion box:** "G is true AND unprovable. Assuming consistency. ∎"
- **Rendered with:** Matplotlib `FancyBboxPatch` + `FancyArrowPatch`, or drawn in
  Inkscape. All original artwork.

### Typographic production path

Use `scripts/eq_render.py` (already in repo) to render any mathematical expressions
as transparent PNGs, then compose in Canva / Inkscape / GIMP:

```bash
python scripts/eq_render.py "True\ but\ unprovable,\ 1931." --fontsize 60 --dpi 300
```

For the full shirt, compose in a design tool: text layer over plain background.
No special script needed for Option A — any word processor or design tool can output
a clean typeset result at 300 DPI.

---

## License

- **Mathematical concept:** PD in all jurisdictions. Mathematical theorems are facts,
  not copyrightable expression.
- **Source paper:** Gödel (1931), *Monatshefte für Mathematik und Physik*, 38(1),
  173–198. EU copyright until 2049 (Gödel died 1978). Do not quote or translate the
  German original text. Use the English-language paraphrase of the concept (a
  mathematical fact, not a translation).
- **English paraphrase used here** ("This statement has no proof in this system",
  "True but unprovable") — original wording, not a translation of any copyrighted text.
- **Typography:** Use OFL-licensed fonts only (EB Garamond, Inter, Source Sans Pro).
- **Diagram (if used):** Original artwork — no third-party IP.
- **No third-party artwork required for any option.**

---

## Sources

1. Gödel, K. (1931). "Über formal unentscheidbare Sätze der Principia Mathematica und
   verwandter Systeme I." *Monatshefte für Mathematik und Physik*, 38(1), 173–198.
   (Original paper, EU copyright until 2049; the mathematical content is a PD fact.)
2. Nagel, E. & Newman, J.R. (1958). *Gödel's Proof*. New York University Press.
   (Secondary source for accessible explanation; standard reference, not copied.)
3. Franzén, T. (2005). *Gödel's Theorem: An Incomplete Guide to its Use and Abuse*.
   A K Peters. (For verifying the precise statement of the theorem.)

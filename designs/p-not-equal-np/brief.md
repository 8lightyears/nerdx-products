# Design Brief: P ≠ NP

**Status:** ready for production
**Category:** Logic and computation
**Products:** T-shirt (primary), poster, mug

---

## The idea

The conjecture P ≠ NP (Cook, 1971) states that the class of problems *solvable*
in polynomial time (P) is strictly smaller than the class of problems whose
solutions can be *verified* in polynomial time (NP). In plain language: being
able to check an answer quickly does not mean you can find it quickly. Despite
53 years of effort by the best complexity theorists in the world, the conjecture
remains unproven. The Clay Mathematics Institute named it a Millennium Prize
Problem in 2000 with a $1,000,000 reward — unclaimed.

This is universally recognised shorthand in computer science and mathematics.
The "$1M unclaimed" angle is a strong conversation-starter; the inequality itself
(two letters, one symbol) is the most compact shirt in the entire shop.

**Key facts (all uncopyrightable):**
- Cook conjecture stated in: Cook, S.A. "The complexity of theorem-proving
  procedures." *Proc. 3rd Annual ACM Symposium on Theory of Computing (STOC)*,
  1971, 151–158. Conference paper in copyright; the conjecture is a mathematical
  statement, not copyrightable.
- Independently formalised: Levin, L.A. (Soviet Union, 1973) — parallel discovery
  of NP-completeness.
- Millennium Prize: Clay Mathematics Institute, 2000. Prize is $1,000,000 (US);
  unclaimed as of 2026-06-27.
- Most complexity theorists believe P ≠ NP, but no proof exists.

---

## Slogan options

**A — minimal (shirt):**
> *P ≠ NP*
> *Unsolved since 1971.*

**B — prize hook (shirt / mug):**
> *P ≠ NP*
> *One million dollars. Still nobody knows.*

**C — explanatory (poster):**
> *P ≠ NP*
> *Checking is easy. Finding is hard. (Probably.)*

**D — badge variant (shirt):**
> *P ≠ NP*
> *Checking is easy. Finding is hard.*
> *(Probably.)*
> ─────────────────
> *$1,000,000 PRIZE — UNCLAIMED*
> *Since 2000.*

Slogan A works best for typography-only shirts (zero art cost). Slogan D
pairs with the prize-badge layout below.

---

## Visual direction

### Option 1 — Typography only (lowest cost, highest viral potential)

- Large *P ≠ NP* centred, bold, monospace or clean sans-serif.
- Subtitle in small caps: *UNSOLVED SINCE 1971* or slogan A/B.
- White on dark shirt or black on white shirt.
- No illustration required.

### Option 2 — Two-box diagram

- *P ≠ NP* centred at top.
- Two small boxes below, side by side:

  ```
  [ P ]              [ NP ]
  solvable quickly   verifiable quickly
  ```

  with a *≠* divider between them.
- Optional: a thin arrow from NP toward P labelled *"⊄ (probably)"*.
- Monospace font throughout; clean and minimal.

### Option 3 — Prize badge (design must be original, not CMI logo)

- Bold *P ≠ NP* at centre.
- Below: a simple badge shape (hexagon or circular seal, original design —
  **do not reproduce the Clay Mathematics Institute logo or wordmark**).
- Badge text: *$1,000,000 PRIZE — UNCLAIMED — CMI, 2000*.
- Badge drawn in monospace/typewriter style to match the rest; no decorative
  elements (no laurel wreaths, no institutional imagery).

Recommended for the launch shirt: Option 1 (typography only) for instant
production, add Option 3 as a variant once the badge design is finalised.

---

## Production steps

1. Set typeface: JetBrains Mono Bold or IBM Plex Mono Bold (both SIL OFL 1.1).
2. Compose layout in a vector editor (Inkscape, free) or directly in Matplotlib
   (`fig.text` with a monospace font).
3. Export at 300 DPI, minimum 3300×3300 px for print-on-demand upload.
4. Upload to Printify (Printful alternative) → Etsy listing.
5. Pricing anchor: $24.99–$28.99 for a standard unisex tee.

### Quick Matplotlib proof-of-concept

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(11, 11), facecolor="#0a0a0a")
fig.text(0.5, 0.62, "P ≠ NP", ha="center", va="center",
         fontsize=160, color="#e8e8e8", fontfamily="monospace", fontweight="bold")
fig.text(0.5, 0.42, "Unsolved since 1971.", ha="center", va="center",
         fontsize=28, color="#aaaaaa", fontfamily="monospace")
plt.savefig("p-not-equal-np.png", dpi=300, bbox_inches="tight", facecolor="#0a0a0a")
plt.close()
```

---

## License

- Mathematical conjecture: uncopyrightable fact.
- Cook (1971) paper: ACM copyright, not reproduced.
- CMI prize: mentioned as a public fact; CMI logo and wordmark not used.
- Typeface: JetBrains Mono / IBM Plex Mono — SIL OFL 1.1, free for commercial use.
- All artwork is original output.

---

## Cross-theme connections

- Pairs with `designs/goedel-incompleteness/brief.md` — both are famous unsolved or
  "true but unknowable" results; could be a two-shirt or four-shirt logic series.
- Recommended launch order from `themes/logic-and-computation.md`: Gödel first
  (broader appeal), then P ≠ NP (strong CS hook), then Turing machine.

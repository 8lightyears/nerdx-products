# Theme: Logic and Computation

Foundational results in mathematical logic and computer science — each one a
surprise that shook the foundations of what mathematics and computing can even do.
These are shirts for people who find undecidability beautiful.

## Why this fits the shop

The 1930s produced a cluster of results that permanently redrew the map of what can
be known and computed. Gödel proved that every sufficiently powerful formal system
has true statements it cannot prove. Turing proved that no general algorithm can
decide whether an arbitrary program halts. Church and Turing arrived at the same
boundary from different directions. These aren't niche curiosities — every working
programmer and mathematician lives with their consequences daily, often without
knowing the name behind them.

The shop's spirit is discovery; these theorems *are* discoveries about the nature
of discovery itself. Visually they reduce to clean diagrams and short, precise
statements — ideal for print.

All mathematical concepts below are uncopyrightable facts. All diagrams must be
original artwork.

---

## Sub-ideas

### 1. Turing machine (1936)

**Original source:** Turing, A.M. "On Computable Numbers, with an Application to
the Entscheidungsproblem." *Proceedings of the London Mathematical Society*, s2-42,
230–265 (1937). DOI: 10.1112/plms/s2-42.1.230. Turing died 1954; EU PD 70 years
after death = 2025 (just entered PD). US: published 1937, renewal status uncertain;
the mathematical *concept* is not copyrightable regardless.

**The idea:** A theoretical machine with an infinite tape of cells (each holding a
symbol), a read-write head, and a finite state table. Despite its simplicity, it can
compute anything any modern computer can — proven by construction, not by hardware.

**Visual direction (original diagram):**
- Horizontal tape: a row of labelled cells (`…`, `0`, `1`, `B`, `1`, `0`, `…`),
  the middle cell highlighted.
- Arrow ↓ pointing at the highlighted cell, labelled "read/write head".
- State table fragment below (4–5 rows: current state, read symbol → write symbol,
  move direction, next state).
- Optional label: *"Universal Computation, 1936."*
- Monospace font throughout; white on black or black on white.

**Slogan options:**
- *"Universal Computation, 1936."*
- *"Finite rules. Infinite reach."*
- *"q₀ → q₁ → q_halt"*

**License:** Mathematical concept PD. Diagram is original artwork. No Turing
Estate / BCS materials needed.

**Automation:** Matplotlib — `patches.FancyBboxPatch` cells, `FancyArrowPatch`
head arrow, table via `matplotlib.table`.

---

### 2. The Halting Problem (1936)

**Original source:** Same Turing 1937 paper as above. The Halting Problem is a
specific result in that paper (Section 8).

**The idea:** There is no general algorithm that, given an arbitrary program and its
input, decides in finite time whether that program halts or runs forever. Turing
proved this by contradiction: assume such an algorithm H exists; build a program D
that calls H on itself and does the opposite of what H predicts; D creates a
paradox. The problem is *undecidable*.

**Visual direction (original diagram):**
- A pseudocode listing (monospace, dark-background terminal style):

  ```
  def halts(program, input): ...  # does it halt?

  def D(x):
      if halts(D, x):
          loop_forever()
      else:
          return

  D(D)  # paradox
  ```

- Annotation: `D(D)` points to a red ∞ symbol with the label *"Contradiction."*
- Alternative: a flowchart with "Does D(D) halt?" → YES branches to "then it loops
  (¬halt)" → NO branches to "then it halts" → loops back.

**Slogan options:**
- *"Undecidable since 1936."*
- *"No algorithm can answer this."*
- *"if halts(D, D): loop_forever() # paradox"* — code only

**License:** Mathematical concept PD. All code/diagrams are original.

**Automation:** `eq_render.py` can render the pseudocode block as a PNG with
monospace font. Flowchart via Matplotlib `FancyArrowPatch`.

---

### 3. Gödel's Incompleteness Theorems (1931)

**Original source:** Gödel, K. "Über formal unentscheidbare Sätze der Principia
Mathematica und verwandter Systeme I." *Monatshefte für Mathematik und Physik*,
38(1), 173–198 (1931). Gödel died 1978; EU PD 2049; US: published 1931 in Austria,
foreign work — status complex. The *mathematical content* (a theorem of logic) is not
copyrightable.

**The idea:** First theorem — in any consistent formal system strong enough to
express basic arithmetic, there exist true statements that the system cannot prove.
Second theorem — such a system cannot prove its own consistency. Gödel constructed
this by encoding "this statement cannot be proved in this system" as an arithmetic
statement (Gödel numbering).

**Visual direction (original artwork):**
- A box containing the statement:
  > *"This statement has no proof in this system."*
  — labelled *Gödel sentence G*.
- Arrows: "Assume G is provable" → contradiction ✗ → "System is inconsistent";
  "Assume G is false" → contradiction ✗ → "System is inconsistent."
- Alternative, typography-only: the statement above in large type, with
  *"True. Unprovable. 1931."* below.

**Slogan options:**
- *"True but unprovable, 1931."*
- *"This statement cannot be proved in this system."*
- *"Every consistent system has blind spots."*

**License:** Mathematical concept PD. All diagrams original. Do not quote the
German original (EU copyright until 2049); use the English-language paraphrase of
the concept (mathematical fact, not translation).

**Shop note:** Highest viral potential of the group — the self-reference is
immediately interesting even to non-mathematicians. Typography-only version has
zero illustration cost.

---

### 4. P ≠ NP (1971 — unsolved)

**Original source:** Cook, S.A. "The complexity of theorem-proving procedures."
*Proceedings of the 3rd Annual ACM Symposium on Theory of Computing (STOC)*, 1971,
151–158. Copyright status: ACM proceedings, in copyright. The *conjecture* itself
is a mathematical statement, not copyrightable. Clay Mathematics Institute named it
a Millennium Prize Problem in 2000 ($1,000,000 prize, unclaimed).

**The idea:** Problems in P can be solved efficiently (polynomial time). Problems
in NP can be *verified* efficiently but may not be *solvable* efficiently. The
conjecture P ≠ NP states that these classes are different — that being able to
check a solution quickly does not mean you can find one quickly. Unproven for 55
years; most complexity theorists believe it is true.

**Visual direction:**
- Large bold *P ≠ NP* centred.
- Below: two small boxes side by side — P: "solvable quickly" / NP: "verifiable
  quickly" — with a ≠ divider.
- Optional: a mock "$1,000,000 PRIZE UNCLAIMED" badge (original design, not the
  CMI logo — that is trademarked).
- Monospace or sans-serif; minimal.

**Slogan options:**
- *"P ≠ NP — unsolved since 1971."*
- *"One million dollars. Still nobody knows."*
- *"Checking is easy. Finding is hard. (Probably.)"*

**License:** Mathematical conjecture PD. Original badge design needed — do not
reproduce the Clay Mathematics Institute logo or wordmark.

**Shop note:** Universally known shorthand in CS/math communities. The
"$1M unclaimed" angle is a strong conversation-starter.

---

### 5. Church-Turing Thesis (1936)

**Original sources:**
- Church, A. "An Unsolvable Problem of Elementary Number Theory." *American Journal
  of Mathematics*, 58(2), 345–363 (1936). Published pre-1978; US renewal status
  unknown; mathematical concept not copyrightable.
- Turing, A.M. — same 1937 paper as above.
- Independently, both Church (via lambda calculus λ) and Turing (via the abstract
  machine) captured the same class of computable functions and arrived at the same
  boundary.

**The idea:** Any function that is intuitively computable can be computed by a Turing
machine — equivalently, by a lambda-calculus expression. Neither Church nor Turing
could formally *prove* this (it is a thesis about physical/intuitive computability,
not a theorem), but every model of computation ever proposed turns out to be
equivalent.

**Visual direction (original diagram):**
- Left column: λ-calculus (lambda symbol + a sample term: `λx. λf. f x`).
- Right column: Turing machine tape fragment.
- Centre: `≡` (identical in power).
- Caption: *"Two routes, one destination."* or *"Every model of computation,
  equivalent. 1936."*

**Slogan options:**
- *"Two routes, one destination. 1936."*
- *"λ ≡ ⊡ — every model of computation, equivalent."*
- *"Church. Turing. Same boundary, different maps."*

**License:** Mathematical concepts PD. All diagrams original.

---

## Visual direction summary

| Design | Key visual | Art cost | Appeal width |
|---|---|---|---|
| Gödel's incompleteness | Self-referential statement | Very low (typography) | Broad |
| P ≠ NP | Bold inequality + prize badge | Low | Broad (CS/math) |
| Turing machine | Tape + head + state table | Low–medium | STEM |
| Halting problem | Pseudocode paradox | Low | CS |
| Church-Turing thesis | λ ≡ tape | Low | CS/math |

**Recommended launch order:** Gödel (viral self-reference, zero illustration cost)
→ P ≠ NP ($1M hook, universally known) → Turing machine (iconic, richer diagram)
→ Halting problem (pairs with Turing) → Church-Turing (narrowest appeal).

**Colour palette:** Black on white or white on very dark grey/navy. Monospace
typeface throughout (JetBrains Mono, Source Code Pro, or similar — free OFL
licensed). Minimal.

**Cross-theme connections:** Gödel connects to thought-experiments (self-reference
paradoxes). Turing machine connects to history-of-dreams (computing machines as
dreams). P≠NP connects to dead-theories (if it ever gets proved, it transitions
from conjecture to theorem).

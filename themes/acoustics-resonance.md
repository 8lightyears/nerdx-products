# Theme: Acoustics / Resonance

Vibration made visible — standing waves, nodal patterns, and resonance phenomena
from Chladni's sand plates (1787) to the Earth's own electromagnetic heartbeat.
These are shirts for people who see geometry hiding inside sound.

## Why this fits the shop

Sound is invisible, yet it has a precise mathematical structure. When that structure
is made literal — sand collecting on nodal lines, a bridge tearing itself apart at
its own frequency, a wine glass shattering at a sung note — the physics becomes a
conversation. The owner has a physics background; the correct derivation of these
effects is within reach. All visual outputs can be generated algorithmically from
first principles, so license exposure is zero.

All mathematical concepts below are uncopyrightable facts. All diagrams must be
original artwork or procedurally generated.

---

## Sub-ideas

### 1. Chladni Figures (1787) — LAUNCH CANDIDATE

**Original source:** Chladni, E.F.F. *Entdeckungen über die Theorie des Klanges*
(Discoveries in the Theory of Sound). Leipzig: Weidmanns Erben und Reich, 1787.
Chladni died 1827; EU PD 1897; US PD (published 1787, pre-1928). The mathematical
concept (standing-wave eigenmodes) is uncopyrightable.

**The idea:** Chladni sprinkled fine sand on a metal plate and drew a violin bow
along the edge. The plate vibrated; the sand migrated away from antinodes (maximum
motion) and settled along nodal lines (zero motion), forming intricate geometric
patterns — stars, diamonds, grids, mandalas — that changed with the bowing position
and frequency. Napoleon I saw a demonstration in 1808 and is said to have offered
6,000 francs for a theory. The patterns are now understood as eigenmodes of the
biharmonic plate equation, reproducible by computation.

**Physics:** For a free rectangular plate the modes are complex (free boundary
conditions, biharmonic operator ∇⁴u = ω²ρh u/D). For a clamped rectangular membrane
they simplify to products of sine functions: u(x,y) = sin(mπx/a)·sin(nπy/b).
The nodal lines are exactly at x = ka/m and y = kb/n. These analytical solutions
give patterns visually close to Chladni's originals and are fully original artwork.

**Visual direction:**
- White or light-sand nodal lines on a black shirt.
- Or: render the pattern in sand-colour (#D4A84B) on dark navy.
- Frame option: circular crop to mimic the plate shape.
- Label option: *"Vibration made visible. Chladni, 1787."* in small type below.
- Mode (2,3) gives a 6-region asymmetric pattern; (3,4) gives a 12-region star.
  Choose modes (m,n) where m ≠ n for interesting asymmetry.
- Full-plate pattern fills the shirt chest; border-only version works on pocket.

**Slogan options:**
- *"Vibration made visible. Chladni, 1787."*
- *"Sand finds the silence. 1787."*
- *"Resonance has a shape."*

**License:** Concept and equations PD. All rendered patterns are original code
output. No Chladni estate rights; no publisher rights to the 1787 patterns.

**Automation:** `scripts/chladni_render.py` — see below. Outputs print-ready 3300×3300 px
PNG. Mode pair (m, n) is a command-line argument; ~40 lines, NumPy + Matplotlib only.

**Art cost:** Low (script-generated). Best candidate for an immediate sample commit.

---

### 2. Standing Waves on a String — "The Harmonic Series" (c. 550 BC)

**Original sources:** Pythagoras of Samos (c. 570–495 BC) established integer
ratios of string lengths to musical intervals — PD. Marin Mersenne *Harmonie
Universelle* (Paris, 1636, PD) gave the first quantitative string formula. Daniel
Bernoulli (1753, PD) derived the general superposition of modes.

**The idea:** A vibrating string fixed at both ends can only sustain wavelengths
that fit an integer number of half-waves between the endpoints. The first mode (f₁)
is the fundamental; modes 2f₁, 3f₁, 4f₁ … are overtones. Every musical instrument
(guitar, violin, piano string) produces its characteristic timbre by the mix of
these overtones. The diagram is a stack of coloured sine curves, each labelled with
its harmonic number and frequency ratio.

**Visual direction:**
- Vertical stack: 5 standing-wave snapshots (modes 1–5), each drawn as a coloured
  sinusoid between two fixed walls, labelled *n=1, f* / *n=2, 2f* / … / *n=5, 5f*.
- Minimal palette: white waves on black, or single-colour wash.
- Caption: *"Every note is a sum. Pythagoras, ~550 BC."*

**Slogan options:**
- *"Every note is a sum. ~550 BC."*
- *"Integer ratios. Pythagoras knew."*
- *"Harmonics: f, 2f, 3f, 4f, 5f, …"*

**License:** All concepts PD. Diagram is original Matplotlib output (~15 lines).

---

### 3. Schumann Resonances — "The Earth Hums"

**Original source:** Schumann, W.O. "Über die strahlungslosen Eigenschwingungen einer
leitenden Kugel, die von einer Luftschicht und einer Ionosphärenülle umgeben ist."
*Zeitschrift für Naturforschung A*, 7(2), 149–154 (1952). Schumann died 1974; EU
PD 2045. The *formula and measured values* are uncopyrightable facts.

**The idea:** The space between Earth's surface (conducting) and the ionosphere
(conducting) forms a resonant cavity for electromagnetic waves. The fundamental
frequency is approximately 7.83 Hz; harmonics at 14.3, 20.8, 27.3, 33.8 Hz. This
electromagnetic heartbeat was theoretically predicted by Schumann in 1952 and
experimentally confirmed by Balser & Wagner in 1960. The formula is:
f_n = (c/2πR) · √(n(n+1)/[1 + ionospheric corrections]) ≈ 7.83·n Hz.

**Visual direction:**
- Circular diagram of Earth with the resonance cavity sketched as concentric arcs.
- Or: a frequency spectrum showing peaks at 7.83, 14.3, 20.8 Hz labelled.
- Caption: *"The Earth resonates at 7.83 Hz. It always has."*

**Slogan options:**
- *"The Earth hums at 7.83 Hz."*
- *"Schumann resonance: 7.83 Hz — the planet's own frequency."*
- *"f = 7.83 Hz. We live inside a resonator."*

**License:** Mathematical concept PD. All diagrams original.

---

### 4. Tacoma Narrows Collapse — "Resonance Can Destroy"

**Original source:** Farquharson, F.B. et al. *Aerodynamic Stability of Suspension
Bridges*. University of Washington, 1949–1954 (US gov / university report, PD).
The bridge collapsed 7 November 1940. Early newsreel footage (Barney Elliott, 1940)
has complex copyright; **use only text-based or original-diagram designs, not
film stills or reproduction of the footage.**

**The idea:** The Tacoma Narrows Bridge oscillated at 0.2 Hz in a 40 mph wind and
collapsed within hours of sustained oscillation. Originally blamed on "resonance"
with the wind; the correct explanation is aeroelastic flutter (Scanlan & Tomko,
1971) — the bridge extracted energy from the wind flow, not a simple resonance.
Either framing is shirt-worthy: the misconception (simple resonance) is the common
story; the correction (aeroelastic flutter) is the nerd fact.

**Visual direction:**
- Text-dominant: date, wind speed, frequency.
- Or: original diagram of the bridge cross-section with oscillation arrows + wind
  direction arrows, no photograph.
- Two-shirt set: "Resonance (popular version)" / "Aeroelastic flutter (correct
  version)" — a meta-commentary on popular science.

**Slogan options:**
- *"40 mph wind. 0.2 Hz. November 7, 1940."*
- *"Not resonance. Aeroelastic flutter. (Close enough.)"*
- *"Every engineer knows this bridge."*

**License:** Facts are PD. Original diagram needed — no newsreel footage.

---

### 5. The Fourier Series — "Any Shape Is a Sum of Circles"

**Original source:** Fourier, J.-B.J. *Théorie analytique de la chaleur* (Paris,
1822). Fourier died 1830; EU and US PD. Mathematical content uncopyrightable.

**Note:** This overlaps with `designs/body-shaped-curve/brief.md` (Fourier + body
silhouette). The *acoustic* framing — any sound wave = sum of pure sine tones — is
a distinct angle and does not duplicate the existing brief.

**The idea:** Any periodic function (including a sound waveform) can be represented
as a sum of sines and cosines at integer multiples of the fundamental frequency.
An oscilloscope trace showing a complex waveform alongside the sine-wave components
that add up to it is visually striking and technically correct.

**Visual direction:**
- Square wave (bold, asymmetric) at top; below, three component sine waves in faint
  lines that sum to approximate it; label each f, 3f, 5f.
- Caption: *"Square waves are infinitely many sines. Fourier, 1822."*

**Slogan options:**
- *"Every sound is a sum. Fourier, 1822."*
- *"f(x) = a₀ + Σ (aₙcos nωx + bₙsin nωx)"*
- *"Any waveform. Any shape. Just add sines."*

**License:** Mathematical content PD. Diagram is original Matplotlib output (~20 lines).

**Cross-theme note:** Connects to `designs/body-shaped-curve/brief.md` (same Fourier
series, visual framing different).

---

## Visual direction summary

| Design | Key visual | Art cost | Appeal width | Priority |
|---|---|---|---|---|
| Chladni figures | Geometric nodal-line pattern | Very low (script) | Broad | **1** |
| Harmonic series | Stacked sine waves on string | Very low (script) | Broad | 2 |
| Schumann resonances | Earth + cavity diagram | Low | Science | 3 |
| Fourier series (acoustic) | Waveform decomposition | Very low (script) | Broad | 4 |
| Tacoma Narrows | Text + original diagram | Low | Engineering | 5 |

**Recommended launch order:** Chladni figures (script ready, visually stunning, broad
appeal, Napoleon story hook) → harmonic series (simplest to produce, every musician
gets it) → Fourier acoustic angle (pairs with existing body-shaped-curve work).

**Colour palette:** White or sand (#D4A84B) on very dark background. The Chladni
patterns benefit most from high contrast.

**Cross-theme connections:** Fourier series connects to `designs/body-shaped-curve/`
(same mathematics, visual angle differs). Tacoma Narrows connects to
`themes/historical-curiosities.md` (disasters with a science punchline).

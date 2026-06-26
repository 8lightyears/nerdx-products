# Theme: Space Exploration History

Key moments, equations, and artefacts from humanity's first steps beyond the
atmosphere — each with a precise date, a real equation or diagram, and a story
that holds up under inspection.

## Why this fits the shop

Space exploration history is the only field where the phrase "they actually did
this" applies to things that sound like science fiction. Tsiolkovsky derived the
rocket equation in 1903, before any rocket had flown. Sputnik's first beep
was picked up by amateur radio operators on October 4, 1957. The Voyager 1 record
was designed to be decoded by an alien civilisation using only physics. Armstrong
landed with 40 KB of computer memory.

These stories are exact, sourced, and visual. NASA materials are US government
works and in the public domain. The physics equations are uncopyrightable. The
visual challenge — rendering an orbital diagram, a spacecraft schematic, or the
Voyager record's cover encoding — is a Matplotlib problem, not a licensing problem.

---

## Sub-ideas

### 1. Tsiolkovsky rocket equation (1903)

**Original source:** Tsiolkovsky, K.E. "Исследование мировых пространств
реактивными приборами" [Exploration of cosmic space by means of reaction devices].
*Nauchnoye Obozreniye* [Science Review], No. 5, 1903, Moscow. Published 1903 in
Russia — PD worldwide (100+ years). English translation excerpts available via NASA
History Division (NASA SP-2000-4408), itself a US gov work (PD).

**The equation:**

Δv = v_e · ln(m₀ / m_f)

where Δv is the change in velocity, v_e is the effective exhaust velocity, m₀ is
the initial mass (fuel + spacecraft), and m_f is the final (dry) mass. The equation
tells you that doubling Δv requires squaring the mass ratio — which is why rockets
are mostly propellant and why reaching orbit is hard.

**The quote:** "The Earth is the cradle of humanity, but one cannot live in the
cradle forever." — Konstantin Tsiolkovsky, in a letter to B.N. Vorobiev, 1911
(widely cited; earliest documented source: letter collection published by the
Academy of Sciences of the USSR, 1954, PD). Attribute clearly; do not use
unverified variants of this quote.

**Visual direction (original artwork):**
- The equation in large, clean type (rendered via `eq_render.py`).
- Below: a small stylised rocket trajectory arc from planet surface curving upward.
- The quote in smaller text below the equation.
- Dark background, white/cream text.

**Slogan options:**
- *"The Earth is the cradle of humanity, but one cannot live in the cradle forever."*
  — quote only (most powerful)
- *"Δv = v_e · ln(m₀/m_f) — Tsiolkovsky, 1903"*
- *"The equation that made spaceflight possible."*

**License:** Equation: mathematical formula, PD. Quote: author died 1935, PD
worldwide. Diagram: original artwork. No third-party assets needed.

**Automation:** `eq_render.py` for the LaTeX equation; 10-line Matplotlib script
for the rocket arc.

---

### 2. Sputnik (1957)

**Original source:** The satellite's technical specifications are documented in:
Pervov, M.A. *Sputnik* (Moscow: Novosti, 1987), and in declassified Soviet
technical reports. Sputnik's orbital parameters and physical dimensions (58.5 cm
diameter aluminium sphere; four spring-loaded whip antennas, two pairs of 2.4 m and
2.9 m; mass 83.6 kg) are public knowledge, documented in NASA and Western sources
including *Journal of the British Interplanetary Society* (1957). Creating an
original schematic from these specifications raises no copyright issue.

**The date:** 4 October 1957, 19:28 UTC, Baikonur Cosmodrome. First artificial
satellite. Orbital period: 96.2 minutes. Signal: 20.005 MHz and 40.002 MHz (heard
by amateur radio operators worldwide). De-orbited 4 January 1958.

**Visual direction (original schematic):**
- Circular body (sphere shown as circle in 2-D), labelled ⌀ 58.5 cm.
- Four antennas: two pairs extending backward and downward at specific angles
  (roughly 35° and 65° from the satellite body axis).
- Radio wave arcs radiating outward (concentric partial circles).
- Label: *"PS-1 — October 4, 1957"* (PS-1 = Простейший Спутник-1,
  "Simplest Satellite 1").
- Optional: signal frequency labels *20 MHz / 40 MHz* along the wave lines.

**Slogan options:**
- *"October 4, 1957 — the sky changed."*
- *"PS-1. 83.6 kg. 96 minutes. History."*
- *"The first beep."*

**License:** Technical specifications are public facts; schematic is original
artwork. Soviet-era government publications: the USSR joined the Universal
Copyright Convention (UCC) in 1973 but pre-1973 Soviet state materials were not
protected in the US (no Berne membership at that time). In any case, this is an
original schematic based on documented dimensions — not a copy of any Soviet
publication.

**Automation:** Matplotlib — `Circle`, `FancyArrowPatch` for antennas, `Arc` for
signal waves. ~20 lines.

---

### 3. Voyager Golden Record (1977)

**Original source:** The Voyager record cover diagram was designed for NASA by a
team led by Carl Sagan, Frank Drake, Ann Druyan, and Jon Lomberg (1977). NASA
images are US government works (PD). The NASA Photojournal entry for the record
cover is PIA01481 (source: https://photojournal.jpl.nasa.gov/catalog/PIA01481,
accessed 2026-06-26). The cover image is also available from the NASA Jet Propulsion
Laboratory as a public release image.

**Complexity note:** Jon Lomberg is the primary artist for the cover diagram. As a
NASA contractor work (JPL contract), it is a US government work and PD — but this
has not been tested in court. The safest approach is to recreate only the *scientific
content* of the cover encoding as original artwork, not to reproduce Lomberg's
specific linework:
- The 21-cm hydrogen hyperfine transition (the "key" used to define the units of
  the diagram): original diagram from physics first principles.
- The pulsar map (14 pulsars with binary-coded distances from the Sun):
  the positions are astronomical facts (PD).
- The silhouetted human figures: NASA's version is PD; recreating from scratch is
  also safe.

**The encoding (what the cover shows):**
1. Binary representation of 1 using the 21-cm hydrogen hyperfine transition as a
   unit (1.42 GHz, period 0.704 ns).
2. 14 radial lines (pulsars) with binary lengths encoding the distance from the Sun
   in units of the 21-cm wavelength — a map to the Solar System's position in the
   galaxy, decodable by any civilisation that understands hydrogen.
3. Silhouettes of a man and woman (with the man's hand raised).
4. Solar System diagram (Sun + 9 planets) with a trajectory line indicating which
   planet the record came from.

**Visual direction (original recreation):**
- Recreate the pulsar map in Matplotlib: 14 radial lines from a central point, each
  with binary tick marks indicating distance. Labels optional.
- Hydrogen transition schematic: two energy levels, photon emission, wavelength
  labelled.
- Human silhouettes: use the NASA PD version (PIA01481) or create original
  silhouettes.
- Caption: *"Launched: September 5, 1977. Now 24 billion km from Earth."*
  (distance to Voyager 1 as of 2026 — update when using).

**Slogan options:**
- *"A message to the universe. 1977."*
- *"14 pulsars. One planet. Hello."*
- *"Still transmitting. 24 billion km and counting."*

**License:** NASA original cover (PIA01481): PD as US gov work; recreating from
scientific content is additionally safe. Pulsar positions: astronomical facts,
uncopyrightable.

**Source:** NASA Photojournal PIA01481
(https://photojournal.jpl.nasa.gov/catalog/PIA01481, accessed 2026-06-26); Sagan et
al., *Murmurs of Earth* (1978), Random House — in copyright, but the record's
scientific content is PD.

---

### 4. Apollo lunar trajectory (1969)

**Original source:** NASA Mission Report — *Apollo 11 Mission Report* (MSC-00171,
September 1969), NASA Technical Reports Server (NTRS), Document ID 19900066485.
PD (US gov work). https://ntrs.nasa.gov/citations/19900066485

The trajectory is also described in: Bates, J.R., Doyle, F.J., Zivney, W.J.
*Apollo Experience Report — Mission Planning for Lunar Module Descent and Ascent*
(NASA TN D-6846, 1972). PD.

**The trajectory phases:**
1. Launch (Kennedy Space Centre, 9:32 EDT, 16 July 1969).
2. Translunar injection (TLI) burn — S-IVB third stage, +3 km/s, raised apogee to
   the Moon.
3. Translunar coast — ~3 days, mid-course correction burns.
4. Lunar orbit insertion (LOI) burn — entered lunar orbit at 76 km altitude.
5. Powered descent initiation (PDI) — Eagle separated and descended.
6. Landing — 20 July 1969, 20:17 UTC, Sea of Tranquility.
7. Transearth injection (TEI), coast, atmospheric re-entry (splashdown 24 July).

Total distance: ~1,079,840 km (one way). Mission elapsed time from launch to
splashdown: 8 days 3 hours 18 minutes.

**Visual direction (original diagram):**
- Earth (circle, left) and Moon (circle, right) with labelled trajectory arc between
  them — a classical patched-conic transfer orbit approximation.
- Phase labels at key points: TLI, coast, LOI, PDI, TEI.
- Optional scale bar.
- Clean technical drawing aesthetic; white on black.

**Slogan options:**
- *"July 20, 1969 — 1,079,840 km."*
- *"Eight days. One small step."*
- *"The math worked."*

**License:** NASA technical reports: US gov PD. Trajectory shape: mathematical/
physical fact, not copyrightable. All diagrams original.

**Automation:** Matplotlib — `Circle`, `FancyArrowPatch` (curved), `annotate` for
phase labels. ~30 lines. The conic arc can be approximated with a Bezier curve.

---

## Visual direction summary

| Design | Key visual | Art cost | Appeal |
|---|---|---|---|
| Tsiolkovsky equation | Equation + quote + arc | Very low | STEM + space fans |
| Sputnik schematic | Sphere + antennas + signal | Low | History/space |
| Voyager pulsar map | Radial lines + human silhouette | Medium | Space + sci fans |
| Apollo trajectory | Orbital arc + phase labels | Low–medium | Space fans |

**Recommended launch order:** Tsiolkovsky (single equation, iconic quote, lowest
cost) → Voyager Golden Record (most recognisable, strong conversation starter) →
Sputnik (simple geometry, date hook) → Apollo trajectory (emotional resonance,
highest diagram complexity).

**Colour palette:** Near-black (#0a0a12 or similar) background; white or pale-gold
text and diagrams. Gold accent works especially well for the Voyager piece (matches
the actual gold-plated record).

**Cross-theme connections:** Tsiolkovsky connects to thought-experiments (the cradle
quote is about aspiration, not physics). Voyager pulsar map connects to
public-domain-space (the record art is NASA PD). Apollo trajectory connects to
mathematical-structures (orbital mechanics as geometry).

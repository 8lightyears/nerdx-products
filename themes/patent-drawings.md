# Theme: Patent Drawings

Original invention patent drawings as shirt graphics — clean line art, precise geometry,
and a specific date that grounds the whole design in a real moment of discovery.

## Why this fits the shop

Patent drawings are the original technical illustration: minimal, precise, annotated with
reference numbers, and completely PD once the patent is old enough. Each one is a snapshot
of the exact moment an inventor had to explain their idea to a bureaucrat — which makes it
a perfect conversation starter. "This is the actual diagram that gave us the telephone."

The aesthetic is instantly recognisable: crisp line art on white or kraft-paper beige,
Fig. 1 / Fig. 2 callouts, and a registration number in the corner. It reads as both
nerdy and vintage.

All US patents, as US government works, are in the public domain on publication. Any
patent granted before 1927 is additionally PD globally under the US PD pre-1927 rule.
The original drawings are PD regardless of when they were scanned — scans of PD 2-D
documents do not create new copyright (Bridgeman Art Library v. Corel Corp., SDNY 1999).

**Safe sources:**
- **Google Patents** (patents.google.com) — full-resolution PDF page downloads
- **USPTO Patent Full-Text and Image Database** (patft.uspto.gov) — TIFF image pages
- **Internet Archive** — scanned patent gazettes

---

## Sub-ideas

### 1. General concept — old invention patent drawings

**Concept:** A series that picks one iconic patent drawing per shirt — no common visual
template, just the philosophy that each product is "the original blueprint." The series
grows one shirt at a time; the USPTO filing number and year anchor each design.

**Visual direction:** Clean white background, dark line art, patent number and title in a
period-style serif. Optional: light kraft-paper texture behind the line art to signal
"archival." The filing date is a design element, not a footnote.

**Source:** USPTO TIFF images, Google Patents PDF pages — all PD.

---

### 2. Tesla polyphase AC motor — US Patent 381,968 (1888)

**Concept:** "The motor that runs the world." Nikola Tesla's polyphase induction motor
diagram is visually dense — rotor, stator windings, flux arrows — and instantly
recognisable to anyone who has studied electromagnetism. The AC vs. DC war of currents
is the backstory.

**Equations to add (original, PD):**
- Rotating magnetic field frequency: `f = p·n / 60` (Hz), where p = pole pairs, n = RPM
- Synchronous speed: `n_s = 120f / p`

**Visual direction:** USPTO drawing from the patent (PD), line art cleaned via
ImageMagick threshold filter, layered with the equation block in a clean sans-serif.
Optional: annotation callout matching the patent's Fig. 1 / Fig. 2 style.

**Slogan options:**
- *"The motor that ended the war."* (AC vs. DC)
- *"US Patent 381,968. The rest is electrification."*
- *"Rotating field, 1888."*

**License:** US Patent 381,968 filed 12 May 1888, granted 26 Oct 1888 — US government
work, PD on publication. Original drawings available at Google Patents and USPTO.

**Source:** Google Patents — US381968A (accessed 2026-06-25); USPTO image database.

---

### 3. Wright brothers flying machine — US Patent 821,393 (1906)

**Concept:** "They built this in a bike shop." The Wright brothers' patent drawing shows
a biplane from three angles with control-wire schematics. The gap between the drawing
and the fact that it actually flew is the entire joke.

**Visual direction:** USPTO drawing (Fig. 1 top-view, or the three-view composite),
cleaned and scaled to shirt proportions. Below: city of Kitty Hawk, NC — 17 December
1903 — 12 seconds.

**Slogan options:**
- *"They built this in a bicycle shop."*
- *"US Patent 821,393. First flight, 1903."*
- *"Kitty Hawk, NC — 12 seconds."*

**License:** US Patent 821,393 filed 23 Mar 1903, granted 22 May 1906 — US government
work, PD. Drawings available at Google Patents and USPTO.

**Source:** Google Patents — US821393A (accessed 2026-06-25).

---

### 4. Bell telephone — US Patent 174,465 (1876)

**Concept:** The first telephone patent is visually elegant — a transmitter/receiver
cross-section with current arrows. It is also culturally loaded: Alexander Graham Bell
filed 2 hours before Elisha Gray on 14 February 1876, which is perhaps the most
consequential 2-hour gap in the history of technology.

**Visual direction:** USPTO drawing, cleaned. Two variants:
- *Engineering:* plain line art + "Filed 14 February 1876, 11:00 AM"
- *Ironic:* add a ghost of Gray's caveat with "Filed 14 February 1876, 2:00 PM" in a
  muted second colour.

**Slogan options:**
- *"2 hours earlier. The first telephone."*
- *"US Patent 174,465. Filed 11 AM, 14 Feb 1876."*
- *"The one that rang."*

**License:** US Patent 174,465 granted 7 Mar 1876 — US government work, PD.

**Source:** Google Patents — US174465A (accessed 2026-06-25); USPTO.

---

### 5. Babbage's Difference Engine — published 1822–1834

**Concept:** Charles Babbage's Difference Engine is the ancestor of the computer — a
mechanical calculator proposed in 1822, partially built in the 1820s–1830s, completed
from the original drawings by the Science Museum London in 1991. The published
engineering drawings from Babbage's lifetime (1822–1834) are PD.

**Visual direction:** Babbage's own published schematic plates — dense gear-column
diagrams that look like early industrial blueprints. The density is the aesthetic.
Caption: *"Designed 1822. Completed 1991."*

**Slogan options:**
- *"Designed 1822. Completed 1991."*
- *"Mechanical computation, before electricity."*
- *"Engine No. 2 — tolerance: 0.0001 inch."*

**License:** Babbage published in *The Transactions of the Cambridge Philosophical
Society* and other venues (1822 and onwards) — pre-1927, US PD. Science Museum's 1991
completion is a new work (Science Museum Group CC BY-NC-SA 4.0 for photos) — do not use
their photos; use only the 19th-century original drawings.

**Source:**
- Charles Babbage, *Passages from the Life of a Philosopher* (1864, pre-1927 PD) — plates
  on Internet Archive (archive.org/details/passagesfromlif00babbgoog, accessed 2026-06-25)
- *Philosophical Transactions of the Royal Society* early issues — Internet Archive PD.

---

## Visual direction (series-wide)

- **Format:** One patent drawing per shirt. Landscape or portrait depending on the source.
- **Palette:** Black line art on white, or dark-blue on cream for a "blueprint" sub-line.
- **Typography:** A period-appropriate slab or condensed serif for the title / date block.
- **Resolution:** Clean the USPTO TIFF to 600 DPI minimum using ImageMagick
  (`convert input.tif -threshold 60% -resize 3300x -density 600 output.png`), then
  add the slogan and reference block in a print-ready layout tool.

---

## Shop fit

**High.** Patent drawings are:
- Immediately legible as "old technical diagram" — zero context required
- PD with easy provenance tracing
- Each is a unique story, not a generic decoration
- Physics-owner-friendly: the equations and diagrams are correct by definition

**Risk:** The line art requires manual cleaning and a print-layout step. A basic
ImageMagick pipeline handles most of it, but each drawing needs a review pass.

**Recommended launch:** Tesla polyphase motor (densest drawing, strong equation hook,
popular STEM culture figure) — then Bell telephone (two-hours story is uniquely
compelling).

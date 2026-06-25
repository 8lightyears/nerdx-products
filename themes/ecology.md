# Ecology theme group

## Scope

Products rooted in the science and politics of environmental crises. Two complementary styles:

1. **Software-metaphor humor** — the world's problems expressed in the visual language of
   GitHub Issues, Jira boards, or dev to-do lists. Deadpan. The joke is the framing, not the
   facts — and the facts are checkable.
2. **Opinion checklist** — a genuine, sourced prioritisation of what actually works (nuclear,
   renewables, electrification, sequestration research). The shirt is a stance, legible in
   three seconds.

Both appeal to the technically-literate, sustainability-aware nerd demographic that already
shops the style of this store. Both carry real, verifiable ideas.

---

## Sub-ideas

### 1. "Environment-saving backlog" (GitHub Issues board)

**Concept.** A dark-theme GitHub-style issues list titled `save-the-world`. Each row is a
real, named environmental crisis formatted as a software issue: priority label, status, and
assignee ("Humanity"). A sample board:

```
🔴 CRITICAL  ocean-acidification  Open   Assigned: Humanity   📅 1850–present
🔴 CRITICAL  6th-mass-extinction  Open   Assigned: Humanity   #biology
🟡 HIGH      CO2-reduction        In Progress (0%)
🟢 DONE      ozone-layer-recovery Closed ✓  1989–2023
```

The ozone-layer item as "Closed" is the kicker: it actually was fixed (Montreal Protocol,
1987). One issue is solvable; the rest are open. The contrast does the work.

**Sourced claims:**
- Ocean acidification ongoing — NOAA: "Since the beginning of the Industrial Revolution, the
  pH of surface ocean waters has fallen by 0.1 pH units." (noaa.gov/education/resource-
  collections/ocean-coasts/ocean-acidification, accessed 2026-06-24)
- Sixth mass extinction — Ceballos et al. (2017), *PNAS*: "The ongoing sixth mass extinction
  may be the most serious environmental threat to the persistence of civilisation."
  (doi:10.1073/pnas.1704949114, accessed 2026-06-24)
- Ozone recovery — WMO/UNEP 2022 Scientific Assessment Panel: "The ozone layer is on track
  to fully recover by around 2066." (ozone.unep.org/assessment-panels, accessed 2026-06-24)
- CO2 progress — IEA, *Net Zero by 2050* (2021): global CO2 emissions are not declining at
  the required pace; as of 2024 still at ~37 Gt/year vs. 21 Gt target by 2030.
  (iea.org/reports/net-zero-by-2050, accessed 2026-06-24)

**Visual direction:**
- Pure text design — monospace font (Fira Code, JetBrains Mono, or similar), dark background
  (#0d1117 GitHub dark), status badges in red/yellow/green
- No external imagery needed; all content is original text layout
- Width: ~75 characters (fits a t-shirt chest comfortably at 300 DPI)
- The "Closed / ✓" ozone row in muted green punctuates the otherwise red/yellow board

**Automation.** Render with Matplotlib `ax.text()` on a dark `#0d1117` canvas, or generate
SVG directly. No third-party assets; zero license concerns. A ~30-line Python script
replicates the GitHub UI text layout. Use `scripts/eq_render.py` as the starting template.

**License.** All text is original; no copyrightable third-party assets. Environmental
statistics are facts — not copyrightable.

---

### 2. "Save the world TODO" / "Optimal CO2 reduction plan"

**Concept.** A priorities checklist: the scientifically-supported, ranked actions for
decarbonisation, presented as a simple bullet list with checkboxes. Most items are unchecked;
a few easy wins are ticked. The shirt is a gentle argument.

Sample checklist:
```
Optimal CO₂ reduction plan

 ☑  Expand existing nuclear (cheapest dispatchable low-carbon)
 ☑  Grid-scale solar + wind (costs down 90% since 2010)
 ☐  Build 500+ small modular reactors (SMRs)
 ☐  Phase out coal globally by 2035
 ☐  Electrify surface transport
 ☐  Green hydrogen for hard-to-abate sectors
 ☐  Carbon capture research (not deployment — not ready)
```

**Sourced claims:**
- Nuclear as low-carbon — IPCC AR6 WG3 (2022) Table A.III.2: nuclear lifecycle emissions
  ~12 g CO₂e/kWh, similar to wind, 40× lower than unabated coal.
  (ipcc.ch/report/ar6/wg3/, accessed 2026-06-24)
- Solar/wind cost drop — IRENA (2023): utility-scale solar PV levelised cost fell 89%
  between 2010–2022. (irena.org/Publications/2023/Aug/Renewable-Power-Generation-Costs,
  accessed 2026-06-24)
- SMR potential — World Nuclear Association (2024): 80+ SMR designs in development globally;
  first commercial units expected 2030s. (world-nuclear.org/information-library/nuclear-fuel-
  cycle/nuclear-power-reactors/small-nuclear-power-reactors, accessed 2026-06-24)
- Coal phase-out target — IEA NZE (2021): no new coal plants and phase-out by 2040 in
  advanced economies required for net-zero pathway.
- Hansen et al. on nuclear — James Hansen et al., "Nuclear Power Paves the Only Viable Path
  Forward on Climate Change," *The Guardian*, 3 Dec 2015. (Referenced for attribution only;
  checklist is the author's synthesis, not a direct quote.)

**Visual direction:**
- Clean, flat, white background or dark background — two variants
- Monospace or clean sans-serif; checkbox glyphs (☑/☐) or ASCII [x]/[ ]
- The ticked items should feel like small victories; the unticked ones like a challenge
- Add a subtle CO₂ molecule label or atomic symbol to anchor it in science territory

**Automation.** Pure text; render with Matplotlib `ax.text()` or direct SVG. Existing
`scripts/eq_render.py` can render the CO₂ molecule symbol. Total effort: ~15 lines.

**License.** All text is original synthesis; IPCC/IEA figures are facts. No third-party
imagery required.

---

### 3. Further sub-ideas (inbox seeds)

- **"1.5°C left" progress bar** — a loading bar stuck at a low percentage with a label
  "Global warming progress: 1.2°C of 1.5°C limit loaded…"
- **Tipping points diagram** — nine planetary boundaries (Rockström et al., 2009, *Nature*)
  as a radar chart, showing which boundaries are already breached; clean infographic style
- **"I did my part" carbon footprint receipt** — spoof grocery receipt showing the CO₂e of
  common everyday decisions (flight: 250 kg CO₂e, beef meal: 6 kg CO₂e, etc.)

---

## Shop-fit assessment

**Strong fit.** Both core concepts anchor humour in real, verifiable science. The GitHub-
board design has strong virality potential among software developers who follow climate news.
The checklist design is a shareable opinion piece. The "ozone-layer Closed" moment is the kind
of discovery the shop's spirit is built on.

**Audience.** Tech workers, scientists, engineers, policy wonks. Overlaps with the existing
ScienceX and public-domain-space audience.

---

## Visual notes

No rejected concepts yet. See `docs/taste.md` for live preferences.

---

## License summary

| Asset | Source | License |
|---|---|---|
| Environmental statistics | IPCC AR6, IEA, NOAA, IRENA, WMO | Facts — not copyrightable |
| GitHub UI aesthetic | Inspired by, not copied from | Original artwork, no GitHub IP |
| Text layouts | Original | No license required |
| Eq symbols (CO₂, ☑, ☐) | Unicode standard | No license required |

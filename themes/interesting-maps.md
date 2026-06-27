# Interesting Maps

Theme group for nerdx-products. Covers curiosity-driven maps as printable products:
subjects that reward a longer look, reveal unexpected information, or reframe how
we think about geography.

All sub-ideas rely on original cartography, PD base data, or openly licensed data.
No third-party copyrighted maps reproduced.

---

## Why this fits the shop

Maps are among the most reliable sellers in the print-on-demand and gallery-print space:
they are decorative, informative, and conversation-starting. The nerdx shop angle is
*maps of things you wouldn't expect to be mappable* — which turns a commodity product
(a world map) into a curiosity object. The owner's physics/science background can inform
the data verification and sourcing.

---

## Product format

Maps suit wall prints (A2, A1, 18×24 in) more than t-shirts — but selected designs
could work as shirts (e.g. a minimal castles-of-Europe dot map or a simplified cuisines
map). The primary format for this theme is wall print / poster on POD (Printify + Etsy,
or Redbubble for prints specifically).

---

## Sub-ideas

### 1. Castles of Europe

**Concept.** A map of Europe with a dot or icon for every castle, fortified tower, and
defensive structure, revealing the density of medieval fortifications. France alone has
~45,000 recorded châteaux; Germany has ~20,000 Burgen und Schlösser; the British Isles
have ~1,500 castles. The map becomes a visual argument: medieval Europe was obsessed
with walls. Shirt version: a monochrome dot map of castles in one country (e.g. Germany
or UK) fits on a black shirt.

**Data source.** OpenStreetMap (ODbL licence) — tag `historic=castle` or
`building=castle`. The ODbL licence allows commercial use provided attribution is given
("Map data © OpenStreetMap contributors") and any database derivatives are also ODbL.
A derived map image (not the raw data) is the product, so ODbL attribution in the
print's border or metadata is sufficient. Wikipedia's List of castles (by country)
provides spot-check verification.

**Generation.** Python + Geopandas + Matplotlib or Folium (static export). Query
Overpass API for `historic=castle` within a bounding box, plot dots on a base map,
export at 300 DPI. ~50 lines of Python.

**License risk.** LOW-MEDIUM. OSM data requires ODbL attribution; include it in the
print border. The derived image itself is an original work.

**Print potential.** HIGH. A known niche (castle maps already exist on Etsy) but the
version covering ALL of Europe in a single high-density dot-map is differentiated.
Pair with a minimal aesthetic (black dots, white background, minimal coastline) rather
than the coloured-icon approach competitors use.

**Recommended titles.**
- "Castles of Europe" (straightforward)
- "Every Recorded Castle in Europe" (specificity is the hook)
- "The Medieval Obsession with Walls" (editorial angle)

---

### 2. World Cuisines Map

**Concept.** A map of the world colour-coded or annotated by dominant cuisine traditions,
showing regional overlaps and surprising adjacencies. The interesting insight: cuisine
boundaries do not follow political borders (Levantine food spans five countries; German
food ends sharply at the Swiss border despite political neutrality; kimchi appears far
from Korea due to diaspora). Version 2: a dot map of Michelin-starred restaurants
worldwide — nearly all are in France, Japan, and the USA, with a surprisingly dense
cluster in Hong Kong.

**Data source.**
- Regional cuisine: original research / academic sources. No single PD dataset; must
  be authored as original cartography. Base country shapes: Natural Earth
  (public domain, naturalearthdata.com). Source: Jurafsky, Dan. *The Language of Food*
  (2014) — not PD; use as a reference for verification only, not as a direct data source.
- Michelin stars: Michelin publishes annual guides; the restaurant locations are facts
  (not protected); however, the Michelin brand must not appear on the product.
  Use "world distribution of fine-dining restaurants" rather than the Michelin name.

**Generation.** Natural Earth shapefiles + Geopandas + manual annotation layer. ~60
lines of Python for the base map; cuisine regions added as polygon overlays or as
original annotation layer (text labels over country boundaries).

**License risk.** LOW (Natural Earth data is PD; original annotations are original work).
MEDIUM if using Michelin brand — avoid the name and star icon; use generic language.

**Print potential.** MEDIUM–HIGH. Cuisines is a competitive niche (food maps are
popular). Differentiator: the unexpected-adjacency angle and the minimal aesthetic.
The Michelin distribution variant has the highest "wait, really?" factor.

**Recommended titles.**
- "What the World Eats" (accessible)
- "Where Cuisines Begin and End" (geographic framing)
- "Fine Dining: A Global Map" (for the Michelin-distribution version, no Michelin branding)

---

### 3. Film Locations

**Concept.** A map showing where famous films were actually shot, with a line connecting
the fictional setting to the real location. Examples: *The Lord of the Rings* → New
Zealand; *Blade Runner 2049* → Budapest; *Dune* → Jordan (Wadi Rum) and Abu Dhabi;
*Star Wars* (Tatooine) → Tunisia (Matmata); *Fargo* → Minnesota (a few scenes) but
mostly North Dakota. The narrative: most cinematic worlds are built somewhere real.

**Variant — single-film map**: a map of New Zealand annotated with all ~150 Lord of the
Rings filming locations (publicly documented; no copyright issue), sold as a travel
guide / fan art for Middle-earth tourists.

**Data source.** Film locations are publicly documented facts (news articles, making-of
books, BFI, IMDB). No single PD dataset; original research from citable public sources.
LOTR locations: "The Lord of the Rings Location Guidebook" by Ian Brodie is a published
book (not PD, do not copy); however, the GPS coordinates of Hobbiton, Edoras, etc. are
public domain facts widely cited in travel articles.

**License risk.** MEDIUM. Film titles and fictional place names (e.g. "Middle-earth")
are trademarked or copyrighted. Use the real-world place names only ("New Zealand
filming locations of the 2001–2003 fantasy trilogy") — not character names, studio logos,
or stills. The map itself (real geographic data + original annotations) is original work.

**Print potential.** MEDIUM (general world film map) to HIGH (dedicated single-film
maps, especially LOTR). LOTR location maps already sell on Etsy at £10–£30; the
differentiated version (dense, sourced, 150+ locations, minimal aesthetic) is viable.

**Recommended titles.**
- "Where Films Are Made" (general world map)
- "New Zealand: Filming Locations of the Fantasy Trilogy" (avoids trademark)

---

### 4. Mysterious Places

**Concept.** A map of locations that science cannot fully explain or that carry
persistent mystery: Nazca Lines (Peru), Stonehenge, the Moai of Easter Island, the
Bermuda Triangle (marked with "Not actually more dangerous"), the Mariana Trench,
Roanoke Colony site, the Overtoun Bridge (dogs jump off it), Oak Island, the Plain of
Jars (Laos), the Crooked Forest (Poland — pine trees with a 90° bend at the base, cause
unknown). The tone: deadpan cartographic seriousness applied to legends.

**Data source.** All locations are publicly documented geographical facts. Brief
annotations can be sourced from academic papers, UNESCO heritage records, or
archaeological reports (all citable). "Not actually more dangerous" annotation for the
Bermuda Triangle is sourced from Lloyd's of London underwriting data (ships in the area
are not statistically more likely to sink — a verifiable fact).

**Generation.** Natural Earth basemap + manual location layer (Python or even Inkscape
for the annotation layer). ~40 lines of Python for the base + ~20 location points.

**License risk.** LOW. All locations are geographical facts; annotations are original;
basemap is PD.

**Print potential.** HIGH. The deadpan-serious tone applied to legend and mystery is
exactly the nerdx aesthetic. Most competing "mysterious places" maps use a sensational
design; a clean, cartographic treatment is differentiated.

**Recommended titles.**
- "Mysterious Places: A Cartographic Record" (deadpan)
- "Things Science Has Not Yet Explained (and a few it has)" (editorial)
- "Unexplained" with coordinate grid (minimal)

---

### 5. Technology Monuments

**Concept.** A map of locations with a remarkable concentration of obsolete,
decommissioned, or extraordinary technology: aircraft boneyards (AMARG at Davis-Monthan
AFB — 3,100+ aircraft in the Arizona desert; viewable on Google Maps); active steam
locomotive depots (China, India, Zimbabwe); open-pit mines visible from space (Bingham
Canyon, Utah; Super Pit, Kalgoorlie, Australia); nuclear test sites (Nevada, Semipalatinsk,
Bikini Atoll); submarine graveyards (Kola Peninsula); particle accelerator sites
(CERN Geneva, Fermilab, KEK Japan). Shirt copy: "The monuments we actually built."

**Data source.** All locations are publicly documented. AMARG: US Air Force (public
domain). Steam locomotive depots: Railway Gazette International (not PD, use as
verification only). Open-pit mines: USGS (PD). Nuclear test sites: Natural Resources
Defense Council database; NNSA data (US gov, PD). Particle accelerators: CERN
institutional data (openly available). All GPS coordinates are public facts.

**Generation.** Natural Earth basemap + icon layer. Icons can be category-specific
(plane silhouette, locomotive, mine, radiation symbol used abstractly). ~50 lines of
Python.

**License risk.** LOW. All locations are public facts; basemap is PD; radiation symbol
is a universal safety sign (no copyright). CERN and Fermilab names are factual — not
branded products.

**Print potential.** HIGH. This is the kind of map that engineers, aerospace enthusiasts,
and nuclear historians share on social media. Very low competition (no existing product
in this exact framing on Etsy as of 2026-06-27).

**Recommended titles.**
- "The Monuments We Actually Built" (recommended; editorial punch)
- "Technology at Rest: A World Map of Boneyards, Mines, and Accelerators"
- "Where the Machines Are" (minimalist)

---

## Launch recommendations

| Priority | Sub-idea | Reason |
|---|---|---|
| 1 | Technology monuments | Unique framing; zero competition; strong story; all PD data |
| 2 | Mysterious places | Deadpan-serious tone is the shop's voice; high viral potential |
| 3 | Castles of Europe | Known niche but density-map variant is differentiated; OSM data straightforward |
| 4 | Film locations | Highest fan-art revenue potential but trademark caution required |
| 5 | World cuisines | Competitive niche; cuisine boundaries need careful original research |

---

## Production notes

- **Base cartography**: Natural Earth 1:50m or 1:110m data (naturalearthdata.com, PD).
  Download `ne_50m_admin_0_countries.shp` for country outlines.
- **Python stack**: `geopandas`, `matplotlib`, `shapely`. All MIT/BSD-licensed.
  Dependencies: `pip install geopandas matplotlib shapely`.
- **POD format**: 18×24 in at 300 DPI = 5400×7200 px. Printify's "Art Poster" product
  accepts up to 24×36 in. Upload as PDF or PNG.
- **Etsy listing**: "custom poster" with location as a variant is the highest-earning
  format in the maps niche (Etsy search: "map poster" → 140,000+ listings).

---

## Cross-theme connections

- **Castles** ↔ `themes/historical-curiosities.md` — medieval engineering; Antikythera
  mechanism level of "how did they do that without modern tools."
- **Technology monuments** ↔ `themes/space-exploration-history.md` — launch sites
  (Baikonur, Cape Canaveral) as technology monuments.
- **Mysterious places** ↔ `themes/thought-experiments.md` — Bermuda Triangle as the
  canonical example of a narrative that feels true and isn't.
- **Film locations** ↔ `themes/public-domain-space.md` — Wadi Rum (Jordan) is both a
  Dune filming location and a real desert with Martian analogue geology.

# Signal Atlas — design notes

## Brief and audit

This profile is a second CV for Danh Duc Nguyen, focused on practical AI engineering. The previous README used a generic gradient banner, an external typing widget, badge rows, and plain project links. The redesign retains the verified contact links, the three public project repositories, UIT education, the 3LC result, and the direction toward a Fresher AI Engineer role. The prior `assets/banner.svg` remains in the repo for history and easy rollback.

## Concept study

| Direction | Art direction / palette / type | Layout and hero | Motion and portfolio treatment |
| --- | --- | --- | --- |
| **Cybernetic Laboratory** | Instrument panel; graphite, teal and signal red; narrow monospace labels | Dense modular dashboard with a central neural schematic | Traveling pulses and scan lines; skills as instrument readouts, projects as experiments |
| **Experimental Editorial** | Digital magazine; ivory, ink and coral; oversized sans serif with small metadata | Asymmetric poster headline and strong negative space | Staggered headline entrance; projects as numbered editorial spreads, skills as a process diagram |
| **Generative Universe** | Computational cartography; deep navy, warm amber and sea glass; bold sans serif with monospaced coordinates | Large name beside orbital data paths | Slow orbits, traveling traces and node pulses; projects as different visual studies, skills as connected systems |

**Selected: Signal Atlas.** It combines the legibility of editorial typography with the visual language of retrieval: a query crosses nodes, paths and documents before becoming a usable answer. The name and system graphics are original to this profile. The same grid, amber rule, numbering and signal colors link every section.

## Visual system

- **Colors:** `#08131f` background, `#eef3ff` primary text, `#e5a96d` signal accent, `#62d9cc` data accent, `#9ba9f8` supporting accent.
- **Type:** Arial/Helvetica for large headlines; Courier New for small technical labels. No remote fonts are required.
- **Composition:** 1200 unit SVG canvases scale to the README width. Important text is repeated in HTML below artwork for smaller screens and assistive technology.
- **Hero:** An oversized name on the left, orbital network on the right. The top rule, grid, coordinates and data paths establish the concept without relying on a generic gradient.
- **Tech stack:** Perception → Retrieval → Delivery mirrors the work described in the CV. All named tools come from the CV's skills section.
- **Projects:** Three linked case studies use distinct visuals: legal search contours, detection boxes, and routed source documents. Claims stay short, with the 3LC result linked to the competition.
- **Activity:** A 30 day strip generated from public GitHub Events API data. It is labeled as public events and is not presented as the GitHub contribution total. The scheduled Action updates both SVG and README image URL to avoid stale caches.
- **Signature:** The data trace resolves into a final line, “Keep following the signal.”

## Animation and compatibility

The artwork is self-contained SVG with CSS keyframes. The hero has staggered text entry, a rotating orbital layer, pulsing nodes and a flowing path. Other assets reuse the flowing trace and restrained pulses. No JavaScript, external widget service, font download or GIF is needed. Each SVG has a complete static appearance and honors `prefers-reduced-motion`.

GitHub's profile page did not display repository-relative SVG image paths in this setup, so the README uses immutable raw URLs for static artwork. The activity asset uses a `main` URL plus a timestamp query updated by the Action. Both dark and light GitHub themes show the dark self-contained canvases with readable contrast. At a narrow viewport, the images scale without horizontal overflow; the HTML captions carry the small text in a readable size.

## Maintenance

- `build_assets.py` regenerates the six static SVGs in `assets/` using Python's standard library.
- `render_activity.py` fetches public events and writes `assets/activity.svg`, then refreshes its URL in `README.md`.
- `.github/workflows/activity.yml` runs daily and can be triggered manually. It commits only when artwork or the URL changes.
- SVG files are small, have descriptive alt text in the README and remain meaningful as still images.

## Research references

- [Awesome GitHub Profile Gallery](https://github.com/nitr0yukkuri/awesome-github-profile-gallery) — breadth of profile patterns.
- [Awesome GitHub Profile](https://github.com/beydemirfurkan/awesome-github-profile) — advanced self-hosted SVG directions.
- [Readme Atelier](https://github.com/monokernn/readme-atelier) — coherent multi-card art direction and scheduled generation.
- [ryme.md](https://github.com/ryanpolasky/ryme.md) — SVG animation inside an image, as GitHub renders it.
- [README-Templates](https://github.com/Dr-At0mic/README-Templates) — theme preview approach.
- [svg-readme](https://github.com/Wenoxxxx/svg-readme) — animated standalone SVG banners.

These references informed the technique and evaluation criteria. Artwork and copy were created specifically for this profile.

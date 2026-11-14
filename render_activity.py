"""Render a 30-day public GitHub activity strip from GitHub's Events API.

The image is intentionally about public events, not a contribution count. GitHub
only exposes a bounded history through this endpoint. On API failure the script
exits without touching the previously committed SVG.
"""

import datetime as dt
import json
import os
import re
from pathlib import Path
from urllib.request import Request, urlopen

USER = "ducdanh2304"
OUT = Path(__file__).parent / "assets" / "activity.svg"
README = Path(__file__).parent / "README.md"
TODAY = dt.datetime.now(dt.timezone.utc).date()
START = TODAY - dt.timedelta(days=29)
counts = {START + dt.timedelta(days=i): 0 for i in range(30)}

headers = {"Accept": "application/vnd.github+json", "User-Agent": "signal-atlas-profile"}
if token := os.environ.get("GITHUB_TOKEN"):
    headers["Authorization"] = f"Bearer {token}"

for page in range(1, 4):
    req = Request(f"https://api.github.com/users/{USER}/events/public?per_page=100&page={page}", headers=headers)
    with urlopen(req, timeout=25) as response:
        events = json.load(response)
    if not isinstance(events, list):
        raise RuntimeError("Unexpected GitHub API response")
    for event in events:
        day = dt.date.fromisoformat(event["created_at"][:10])
        if day in counts:
            counts[day] += 1
    if len(events) < 100 or (events and dt.date.fromisoformat(events[-1]["created_at"][:10]) < START):
        break

maximum = max(max(counts.values()), 1)
total = sum(counts.values())
bars = []
for i, (day, count) in enumerate(counts.items()):
    x = 50 + i * 36
    height = max(4, round(110 * count / maximum)) if count else 4
    y = 185 - height
    color = "#e5a96d" if count >= maximum * .75 and count else "#62d9cc" if count else "#385461"
    bars.append(f'<rect x="{x}" y="{y}" width="20" height="{height}" rx="3" fill="{color}"><title>{day.isoformat()}: {count} public events</title></rect>')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="250" viewBox="0 0 1200 250" role="img" aria-label="Public GitHub activity over 30 days, updated {TODAY.isoformat()}">
<style>.bar{{animation:rise .7s ease-out both}}@keyframes rise{{from{{opacity:.2}}to{{opacity:1}}}}@media(prefers-reduced-motion:reduce){{*{{animation:none!important}}}}</style>
<rect width="1200" height="250" rx="15" fill="#0b1723"/><path d="M0 5H1200" stroke="#e5a96d" stroke-width="5"/>
<text x="40" y="48" fill="#e5a96d" font-family="Courier New,monospace" font-size="15" letter-spacing="2">04 / PUBLIC ACTIVITY</text>
<text x="40" y="86" fill="#eef3ff" font-family="Arial,sans-serif" font-size="27" font-weight="700">The last 30 days, in signals.</text>
<path d="M40 185H1150" stroke="#426c77"/>
<g class="bar">{''.join(bars)}</g>
<text x="42" y="221" fill="#9fb6c0" font-family="Courier New,monospace" font-size="13">{START.isoformat()}  →  {TODAY.isoformat()}</text>
<text x="870" y="221" fill="#9fb6c0" font-family="Courier New,monospace" font-size="13">{total} PUBLIC EVENTS · UPDATED DAILY</text>
</svg>'''
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(svg, encoding="utf-8")
if README.exists():
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M%S")
    readme = README.read_text(encoding="utf-8")
    refreshed = re.sub(
        r"(https://raw\.githubusercontent\.com/ducdanh2304/ducdanh2304/)[^/]+(/assets/activity\.svg)(?:\?asof=\d+)?",
        rf"\g<1>main\g<2>?asof={stamp}",
        readme,
    )
    if refreshed == readme:
        raise RuntimeError("Activity image URL not found in README")
    README.write_text(refreshed, encoding="utf-8")
print(f"Wrote {OUT} from {total} public events")

"""Generate self-contained, responsive Signal Atlas profile artwork."""
from pathlib import Path
from html import escape

OUT = Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)
BG, INK, MUTED, AMBER, TEAL, BLUE = "#08131f", "#f1f5f9", "#a5b7c5", "#f1b572", "#66ded0", "#9caafa"
CSS = """<style>.s{font-family:Arial,Helvetica,sans-serif}.m{font-family:'Courier New',monospace;letter-spacing:1.5px}.dash{stroke-dasharray:5 9;animation:run 14s linear infinite}.blink{animation:blink 3s ease-in-out infinite}@keyframes run{to{stroke-dashoffset:-140}}@keyframes blink{50%{opacity:.25}}@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style>"""

def t(x,y,value,size=18,color=INK,weight=400,cls="s",extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" class="{cls}" {extra}>{escape(value)}</text>'

def save(name,w,h,body):
    (OUT/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(name)}">{CSS}{body}</svg>',encoding="utf-8")

grid = ''.join(f'<path d="M{x} 0V395" stroke="#375165" opacity=".22"/>' for x in range(0,1201,60)) + ''.join(f'<path d="M0 {y}H1200" stroke="#375165" opacity=".22"/>' for y in range(0,396,60))
nodes=[(760,110),(845,190),(955,95),(1065,185),(970,300),(1120,305)]
edges=[(0,1),(0,2),(1,2),(1,4),(2,3),(3,4),(3,5),(4,5)]
hero=f'<rect width="1200" height="395" rx="16" fill="{BG}"/>{grid}<path d="M0 5H1200" stroke="{AMBER}" stroke-width="5"/>'
hero+=''.join(f'<path d="M{nodes[a][0]} {nodes[a][1]}L{nodes[b][0]} {nodes[b][1]}" stroke="{TEAL}" opacity=".33" class="dash"/>' for a,b in edges)
hero+=''.join(f'<ellipse cx="950" cy="210" rx="{r}" ry="{round(r*.48)}" transform="rotate(-25 950 210)" fill="none" stroke="{AMBER}" opacity=".18"/>' for r in (95,155,220))
hero+=''.join(f'<circle cx="{x}" cy="{y}" r="{5 if i%2 else 7}" fill="{AMBER if i%2 else TEAL}" class="blink"/>' for i,(x,y) in enumerate(nodes))
hero+=t(54,48,'SIGNAL ATLAS   /   001',14,AMBER,700,'m')+t(54,167,'DANH',102,INK,800)+t(54,260,'DUC NGUYEN',82,INK,800)
hero+=f'<path d="M54 285H570" stroke="{AMBER}" stroke-width="2"/>'+t(54,324,'AI ENGINEERING  /  VISION  /  RETRIEVAL',16,TEAL,700,'m')+t(54,362,'Building intelligent systems across vision, language & search.',18,MUTED)
hero+=t(1045,364,'DATA → SIGNAL',12,AMBER,700,'m')
save('hero-v2.svg',1200,395,hero)

nav=[('EMAIL','↗',AMBER),('LINKEDIN','↗',TEAL),('GITHUB','↗',BLUE),('PUBLICATION','↗',AMBER),('SELECTED WORK','↘',TEAL)]
for label,arrow,color in nav:
    w=204 if label in ('PUBLICATION','SELECTED WORK') else 166
    body=f'<rect width="{w}" height="48" rx="7" fill="#112536" stroke="{color}" stroke-opacity=".65"/><path d="M8 8H{w-8}" stroke="{color}" opacity=".42"/>'
    body+=f'<circle cx="25" cy="25" r="12" fill="none" stroke="{color}" opacity=".65"/>'+t(20,30,arrow,15,color,700)
    body+=t(48,30,label,13,INK,700,'m')
    save('nav-'+label.lower().replace(' ','-')+'.svg',w,48,body)

def section(name,index,title,sub):
    b=f'<rect width="1200" height="84" fill="{BG}"/><path d="M0 82H1200" stroke="#375165"/>'
    b+=f'<circle cx="14" cy="40" r="4" fill="{AMBER}" class="blink"/>'+t(31,45,index,13,AMBER,700,'m')+t(104,53,title,37,INK,700)+t(1175,47,sub,12,MUTED,600,'m','text-anchor="end"')
    save(name,1200,84,b)
section('section-stack.svg','01','Toolbox','CAPABILITIES / 2026')
section('section-work.svg','02','Selected work','THREE SIGNALS')
section('section-paper.svg','03','Research note','FIRST AUTHOR / 2026')
section('section-proof.svg','04','Recognition','SELECTED RESULTS')

from build_cards import build_cards
build_cards(OUT)

b=f'<rect width="1200" height="118" rx="8" fill="#0d1d2b"/><path d="M0 0H1200" stroke="{AMBER}" stroke-width="3"/>'
for i,(num,line,small,c) in enumerate([('01','3LC CHALLENGE','1ST PLACE',AMBER),('19','UIT DATA SCIENCE','TOP 19',TEAL),('05','HCMC AI CHALLENGE','TOP 5 / 600+ TEAMS',BLUE)]):
    x=25+i*395
    if i:b+=f'<path d="M{x-13} 20V99" stroke="#375165"/>'
    b+=t(x,73,num,56,c,800)+t(x+95,51,line,16,INK,700,'m')+t(x+95,76,small,13,MUTED,700,'m')
save('recognition-v2.svg',1200,118,b)

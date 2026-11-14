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

def diagram(name,title,metric,subtitle,steps,accent):
    b=f'<rect width="1200" height="190" rx="9" fill="#0d1d2b"/><path d="M0 1H1200" stroke="{accent}" stroke-width="3"/>'
    b+=t(29,33,title,13,accent,700,'m')+t(29,87,metric,41,INK,800)+t(29,119,subtitle,15,MUTED)
    x0=29; widths=[185,185,185,185]
    for i,s in enumerate(steps):
        x=x0+i*198
        b+=f'<rect x="{x}" y="139" width="{widths[i]}" height="33" rx="4" fill="#172d3d" stroke="{accent}" stroke-opacity=".36"/>'
        b+=t(x+10,160,s,13,INK,600,'m')
        if i<3:b+=t(x+188,161,'›',20,accent,700)
    if name.startswith('lexviet'):
        # Query fans out to documents, then converges on one ranked passage.
        b+=t(822,31,'QUERY',10,accent,700,'m')+f'<circle cx="845" cy="75" r="15" fill="none" stroke="{accent}"/>'
        for i,y in enumerate((43,68,93)):
            b+=f'<path d="M861 75L948 {y}" stroke="{accent}" opacity=".48" class="dash"/><rect x="948" y="{y-14}" width="68" height="25" rx="2" fill="none" stroke="{accent}" opacity=".55"/>'
            b+=f'<path d="M958 {y-5}h42M958 {y+2}h27" stroke="{accent}" opacity=".5"/>'
            b+=f'<path d="M1017 {y}L1080 68" stroke="{accent}" opacity=".42"/>'
        b+=f'<rect x="1080" y="50" width="86" height="36" rx="3" fill="{accent}" opacity=".17" stroke="{accent}"/>'+t(1092,73,'TOP 5',14,accent,700,'m')
    elif name.startswith('detection'):
        b+=f'<rect x="832" y="27" width="314" height="92" rx="3" fill="#162b37" stroke="#486476"/>'
        b+=f'<path d="M832 96H1146M862 96l40-69M1117 96l-40-69" stroke="#486476" opacity=".6"/>'
        for x,y,w,h in ((852,51,76,47),(948,39,92,58),(1060,54,64,41)):
            b+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{accent}" stroke-width="2" class="dash"/>'
        b+=t(1020,30,'VEHICLE / BOXES',10,accent,700,'m')
    else:
        for i in range(4):
            x=830+i*78
            b+=f'<rect x="{x}" y="42" width="68" height="58" rx="2" fill="#152b3c" stroke="{accent}" opacity=".78"/>'
            b+=f'<path d="M{x+8} 77l15-19 13 11 15-20 9 13" fill="none" stroke="{accent}" opacity=".65"/>'
            b+=f'<circle cx="{x+10}" cy="108" r="2" fill="{accent}"/><circle cx="{x+58}" cy="108" r="2" fill="{accent}"/>'
        b+=t(925,31,'VIDEO → KEYFRAMES',10,accent,700,'m')
    save(name,1200,190,b)
diagram('lexviet-v2.svg','LEGAL DOCUMENT RETRIEVAL','94.28% Recall@5','2,080 private queries  ·  596,062 legal chunks',['11 signals','WRRF fusion','LightGBM','Jina rerank'],TEAL)
diagram('detection-v2.svg','3LC MULTI-VEHICLE DETECTION','1st PLACE','0.95099 public  /  0.94052 private mAP@0.5',['Label audit','61 revisions','YOLOv8n','NMS tuning'],AMBER)
diagram('video-v2.svg','MULTIMODAL VIDEO RETRIEVAL','~600K KEYFRAMES','1,478 videos  ·  300+ hours  ·  Vietnamese retrieval',['CLIP / BEiT-3','Captions','Audio / OCR','Fusion'],BLUE)

b=f'<rect width="1200" height="118" rx="8" fill="#0d1d2b"/><path d="M0 0H1200" stroke="{AMBER}" stroke-width="3"/>'
for i,(num,line,small,c) in enumerate([('01','3LC CHALLENGE','1ST PLACE',AMBER),('19','UIT DATA SCIENCE','TOP 19',TEAL),('05','HCMC AI CHALLENGE','TOP 5 / 600+ TEAMS',BLUE)]):
    x=25+i*395
    if i:b+=f'<path d="M{x-13} 20V99" stroke="#375165"/>'
    b+=t(x,73,num,56,c,800)+t(x+95,51,line,16,INK,700,'m')+t(x+95,76,small,13,MUTED,700,'m')
save('recognition-v2.svg',1200,118,b)

"""Build the self-contained Signal Atlas SVG artwork for the profile README."""

from pathlib import Path
from html import escape

OUT = Path(__file__).parent / "assets"
OUT.mkdir(parents=True, exist_ok=True)

CSS = """
<style>
  .mono{font-family:'Courier New',monospace;letter-spacing:2px}
  .sans{font-family:Arial,Helvetica,sans-serif}
  .trace{stroke-dasharray:8 11;animation:flow 15s linear infinite}
  .pulse{animation:pulse 3s ease-in-out infinite}
  .slow{animation:orbit 24s linear infinite;transform-origin:930px 220px}
  .appear{animation:appear 1.2s ease-out both}
  .a2{animation-delay:.25s}.a3{animation-delay:.55s}
  @keyframes flow{to{stroke-dashoffset:-190}}
  @keyframes pulse{50%{opacity:.25;transform:scale(.76)}}
  @keyframes orbit{to{transform:rotate(360deg)}}
  @keyframes appear{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
  @media(prefers-reduced-motion:reduce){*{animation:none!important}}
</style>
"""

def svg(name, body, w=1200, h=400, extra_css=CSS):
    doc = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(name)}">{extra_css}{body}</svg>'
    (OUT / name).write_text(doc, encoding="utf-8")

def text(x,y,s,size=20,color="#eef3ff",weight=400,klass="sans",extra=""):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" class="{klass}" {extra}>{escape(s)}</text>'

grid = ''.join(f'<path d="M{x} 0V430" stroke="#263a50" opacity=".26"/>' for x in range(0,1201,60)) + ''.join(f'<path d="M0 {y}H1200" stroke="#263a50" opacity=".26"/>' for y in range(0,431,60))
orb = ''.join(f'<ellipse cx="930" cy="220" rx="{r}" ry="{int(r*.48)}" fill="none" stroke="#45e0ca" stroke-opacity="{.28 if r<200 else .13}" transform="rotate(-24 930 220)"/>' for r in [70,130,200,280])
nodes = [(752,184),(820,120),(952,134),(1086,85),(820,302),(964,295),(1093,339)]
edges = [(0,1),(0,4),(1,2),(1,4),(2,3),(2,5),(3,6),(4,5),(5,6)]
network = ''.join(f'<path d="M{nodes[a][0]} {nodes[a][1]}L{nodes[b][0]} {nodes[b][1]}" stroke="#68ddcf" stroke-opacity=".34"/>' for a,b in edges)
network += ''.join(f'<circle cx="{x}" cy="{y}" r="{5 if i%2 else 8}" fill="#f7c98a" class="pulse" style="animation-delay:{i*.38}s"/>' for i,(x,y) in enumerate(nodes))
hero = f'''<rect width="1200" height="430" rx="16" fill="#08131f"/>{grid}<path d="M0 0H1200V7H0Z" fill="#e5a96d"/>
<path d="M678 408Q780 130 1180 18" fill="none" stroke="#e5a96d" opacity=".27" stroke-width="2" class="trace"/>{orb}{network}
<circle cx="930" cy="220" r="31" fill="#e5a96d" opacity=".1"/><circle cx="930" cy="220" r="8" fill="#f7c98a"/>
{text(55,55,'SIGNAL ATLAS  /  001',14,'#e5a96d',700,'mono')}{text(55,177,'DANH',95,'#eef3ff',800,'sans appear')}
{text(55,271,'DUC NGUYEN',82,'#eef3ff',800,'sans appear a2')}
<path d="M55 302H505" stroke="#e5a96d" stroke-width="2"/>
{text(55,340,'COMPUTER VISION   /   RETRIEVAL   /   VIETNAMESE NLP',15,'#a8c8d3',500,'mono')}
{text(55,392,'CS STUDENT · UIT VNU-HCM',13,'#8ba1af',500,'mono')}
{text(1034,389,'DATA → SIGNAL',12,'#e5a96d',500,'mono')}
'''
svg('hero.svg',hero,h=430)

stack = '''<rect width="1200" height="420" rx="16" fill="#0b1723"/><path d="M0 7H1200" stroke="#e5a96d" stroke-width="6"/>'''
stack += text(42,55,'02 / TECHNICAL UNIVERSE',15,'#e5a96d',700,'mono')
stack += text(42,105,'From data to a working system.',36,'#eef3ff',700)
stack += '<path d="M95 251H1090" stroke="#426c77" stroke-width="3" class="trace"/>'
cols=[(78,'01','PERCEPTION','#62d9cc',['PyTorch','OpenCV','YOLO','Transformers']), (430,'02','RETRIEVAL','#e5a96d',['Python','SQL · SQLite','LightGBM','Reranking']), (782,'03','DELIVERY','#9ba9f8',['FastAPI','Docker','Git · Linux','ONNX'])]
for x,n,title,c,items in cols:
    stack+=f'<rect x="{x}" y="144" width="314" height="223" rx="10" fill="#102330" stroke="{c}" stroke-opacity=".48"/>'
    stack+=f'<circle cx="{x+26}" cy="251" r="8" fill="{c}" class="pulse"/>'
    stack+=text(x+24,184,n,18,c,700,'mono')+text(x+24,215,title,25,'#eef3ff',700)
    stack+=text(x+24,286,' / '.join(items[:2]),17,'#aec5ce')
    stack+=text(x+24,325,' / '.join(items[2:]),17,'#aec5ce')
stack+=text(44,397,'A WORKFLOW, NOT A LOGO COLLECTION',12,'#6e8994',500,'mono')
svg('stack.svg',stack,h=420)

base='<rect width="1200" height="240" rx="15" fill="#0b1723"/><path d="M0 6H1200" stroke="#e5a96d" stroke-width="5"/>'
def project(filename,num,title,tag,desc,tech,art,c):
    body=base+f'<path d="M680 20H1180V220H680Z" fill="{c}" opacity=".06"/>'
    body+=text(35,53,f'CASE STUDY / {num}',14,c,700,'mono')
    body+=text(35,111,title,45,'#eef3ff',700)
    body+=text(35,148,tag,18,c,700,'mono')
    body+=text(35,184,desc,18,'#b7cbd2')
    body+=text(35,215,tech,13,'#7997a3',500,'mono')+art
    svg(filename,body,h=240)

lexart=''.join(f'<path d="M{735+i*11} 145Q{875+i*2} {12+i*15} 1130 {75+i*9}" fill="none" stroke="#62d9cc" stroke-opacity="{.36-i*.018}"/>' for i in range(11))
lexart+='<circle cx="922" cy="91" r="52" fill="none" stroke="#e5a96d" stroke-width="2"/><path d="M957 129L1002 174" stroke="#e5a96d" stroke-width="7" stroke-linecap="round"/>'
lexart+='<circle cx="922" cy="91" r="7" fill="#e5a96d" class="pulse"/>'
project('lexviet.svg','01','LexViet','RETRIEVAL / LEGAL NLP','Finding the right passage in a sea of legal text.','HYBRID SEARCH   ·   LEARNING TO RANK   ·   RERANKING',lexart,'#62d9cc')

visionart=''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{c}" stroke-width="2" class="trace" style="animation-delay:{i*.7}s"/>' for i,(x,y,w,h,c) in enumerate([(735,55,150,92,'#e5a96d'),(905,72,110,108,'#62d9cc'),(1040,45,105,152,'#e5a96d')]))
visionart+='<path d="M705 215H1160M705 33H1160" stroke="#667f89" opacity=".5"/>'
project('detection.svg','02','Multi-Vehicle Detection','COMPUTER VISION / DATA QUALITY','Finding missing labels before improving the model.','YOLOV8N   ·   LABEL AUDIT   ·   REPRODUCIBLE INFERENCE',visionart,'#e5a96d')

ragart=''.join(f'<rect x="{740+i*73}" y="{55+(i%2)*23}" width="92" height="122" fill="#102b39" stroke="#85a7b3" stroke-opacity=".5"/>' for i in range(5))
ragart+=''.join(f'<path d="M{755+i*73} {75+(i%2)*23+j*16}h{40+j*4}" stroke="#62d9cc" opacity=".55"/>' for i in range(5) for j in range(4))
ragart+='<path d="M745 201Q925 135 1134 204" fill="none" stroke="#e5a96d" stroke-width="2" class="trace"/>'
project('rag.svg','03','Labor Law RAG','QUESTION ANSWERING / VIETNAMESE NLP','Tracing a question back to its source in the Labor Code.','QUERY REWRITING   ·   SEMANTIC ROUTING   ·   SELF-RAG',ragart,'#9ba9f8')

footer='''<rect width="1200" height="140" rx="14" fill="#0b1723"/><path d="M40 70H1140" stroke="#426c77" class="trace"/><circle cx="60" cy="70" r="7" fill="#e5a96d" class="pulse"/>'''
footer+=text(58,48,'KEEP FOLLOWING THE SIGNAL.',25,'#eef3ff',700)
footer+=text(58,108,'DANH DUC NGUYEN  /  HCMC  /  2026',13,'#9eb5bd',500,'mono')
footer+=text(1010,107,'END / ∞',13,'#e5a96d',500,'mono')
svg('footer.svg',footer,h=140)

print(*(f'{p.name}: {p.stat().st_size} bytes' for p in sorted(OUT.glob('*.svg'))),sep='\n')

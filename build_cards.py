"""Editorial project artwork for desktop and narrow GitHub profile columns."""
from html import escape
from pathlib import Path

INK = "#152330"
CREAM = "#f3f0e9"
RUST = "#c66b46"
TEAL = "#177e78"
COBALT = "#1d3454"
WHITE = "#f8f8f3"
CSS = """<style>.s{font-family:Arial,Helvetica,sans-serif}
.flow{stroke-dasharray:5 7;animation:go 12s linear infinite}@keyframes go{to{stroke-dashoffset:-120}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style>"""

def txt(x,y,value,size,color=INK,weight=400,extra=""):
    return f'<text class="s" x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(value)}</text>'

def save(out,name,w,h,body):
    (out/name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(name)}">{CSS}{body}</svg>',
        encoding="utf-8",
    )

def query_art(x=0,y=0,scale=1):
    b=f'<g transform="translate({x} {y}) scale({scale})">'
    b+=txt(20,38,"VIETNAMESE QUERY",13,TEAL,700)
    b+=f'<rect x="20" y="53" width="168" height="34" rx="17" fill="{WHITE}" stroke="{TEAL}"/>'
    b+=f'<circle cx="40" cy="70" r="7" fill="none" stroke="{TEAL}" stroke-width="2"/><path d="M45 75l7 7" stroke="{TEAL}" stroke-width="2"/>'
    b+=f'<path d="M190 70C240 70 224 122 260 122" fill="none" stroke="{TEAL}" stroke-width="2" class="flow"/>'
    for i in range(3):
        yy=92+i*39
        b+=f'<rect x="255" y="{yy}" width="90" height="28" rx="2" fill="{WHITE}" stroke="{TEAL if i==1 else "#b9c9c4"}"/>'
        b+=f'<path d="M267 {yy+9}h55M267 {yy+17}h37" stroke="{TEAL if i==1 else "#a5b5b0"}"/>'
    b+=f'<path d="M347 132h33" stroke="{TEAL}" stroke-width="2" class="flow"/>'
    b+=f'<circle cx="378" cy="132" r="12" fill="{TEAL}"/>'+txt(374,137,"1",14,WHITE,700)
    b+='</g>'
    return b

def road_art(x=0,y=0,scale=1):
    b=f'<g transform="translate({x} {y}) scale({scale})">'
    b+=f'<rect width="380" height="260" fill="#d8e3e7"/><path d="M0 250L124 0h132l124 250" fill="#b9c7ca"/>'
    b+=f'<path d="M182 18v38M182 85v44M182 158v55" stroke="#f5f5ef" stroke-width="4" stroke-dasharray="14 12"/>'
    for xx,yy,ww,hh in ((42,113,105,58),(212,80,92,65),(137,170,93,58)):
        b+=f'<rect x="{xx}" y="{yy}" width="{ww}" height="{hh}" rx="2" fill="none" stroke="{RUST}" stroke-width="3"/>'
    b+=f'<rect x="275" y="156" width="75" height="47" rx="2" fill="none" stroke="{RUST}" stroke-width="3" stroke-dasharray="6 5"/>'
    b+=f'<path d="M317 204v25h-94" fill="none" stroke="{RUST}" stroke-width="2" class="flow"/>'
    b+=txt(21,30,"PREDICT → REVIEW",14,INK,700)
    b+='</g>'
    return b

def video_art(x=0,y=0,scale=1):
    b=f'<g transform="translate({x} {y}) scale({scale})">'
    for i in range(3):
        xx=20+i*98
        b+=f'<rect x="{xx}" y="44" width="87" height="62" rx="2" fill="#375776" stroke="#a8c4dc"/>'
        b+=f'<path d="M{xx+5} 91l21-26 16 14 21-23 19 35" fill="none" stroke="#accde0" stroke-width="2"/>'
        b+=f'<path d="M{xx+8} 113h70" stroke="#7699bb" stroke-width="3" stroke-dasharray="5 5"/>'
    b+=f'<path d="M170 126v33M56 160h227" stroke="#d9b37a" stroke-width="2" class="flow"/>'
    for i,(label,col) in enumerate((("VISUAL","#9ec9df"),("TEXT","#e4b781"),("OCR","#bca9d8"),("SPEECH","#9fcab2"))):
        xx=16+(i%2)*145; yy=174+(i//2)*37
        b+=f'<rect x="{xx}" y="{yy}" width="132" height="27" rx="2" fill="{col}" opacity=".2" stroke="{col}"/>'
        b+=txt(xx+13,yy+19,label,13,WHITE,700)
    b+='</g>'
    return b

def build_cards(out: Path):
    out.mkdir(exist_ok=True)
    # Desktop: a document pipeline on warm paper, with the text in a clean right column.
    b=f'<rect width="900" height="270" fill="{CREAM}"/><path d="M0 0H900" stroke="{TEAL}" stroke-width="5"/>'
    b+=query_art(0,0,.92)+f'<path d="M380 25V245" stroke="#cbd4cd"/>'
    b+=txt(414,43,"01  /  INFORMATION RETRIEVAL",15,TEAL,700)
    b+=txt(414,91,"LexViet",43,INK,700)
    b+=txt(414,128,"0.9428 Competition Score",25,TEAL,700)
    b+=txt(414,165,"Hybrid search and learning to rank for",19,INK)
    b+=txt(414,189,"Vietnamese legal documents.",19,INK)
    b+=txt(414,223,"11 signals · Weighted RRF · LightGBM",16,"#4e626a")
    b+=txt(414,251,"EXPLORE THE REPOSITORY  ↗",16,TEAL,700)
    save(out,"lexviet-v3.svg",900,270,b)

    # Detection uses a road scene and a visibly human-verified missing box.
    b=f'<rect width="900" height="270" fill="#edf0ed"/><path d="M0 0H900" stroke="{RUST}" stroke-width="5"/>'
    b+=road_art()+f'<path d="M380 25V245" stroke="#c8d0cc"/>'
    b+=txt(414,43,"02  /  COMPUTER VISION",15,RUST,700)
    b+=txt(414,88,"Multi-Vehicle",36,INK,700)+txt(414,127,"Detection",36,INK,700)
    b+=txt(414,162,"1st Place / 97 teams",25,RUST,700)
    b+=txt(414,192,"Data-centric YOLOv8n with human-verified",18,INK)
    b+=txt(414,215,"missing-label audits. 0.94052 private mAP@0.5.",17,INK)
    b+=txt(414,251,"EXPLORE THE REPOSITORY  ↗",16,RUST,700)
    save(out,"detection-v3.svg",900,270,b)

    # Research is a midnight-blue spread with a real modality flow.
    b=f'<rect width="900" height="270" fill="{COBALT}"/><path d="M0 0H900" stroke="#a9c5de" stroke-width="5"/>'
    b+=video_art()+f'<path d="M380 25V245" stroke="#6983a0"/>'
    b+=txt(414,43,"03  /  MULTIMODAL RESEARCH",15,"#b9d4e6",700)
    b+=txt(414,88,"Video Retrieval",38,WHITE,700)
    b+=txt(414,127,"~600K Keyframes",27,"#f1c78d",700)
    b+=txt(414,160,"1,478 videos · 300+ hours · First Author",17,WHITE)
    b+=txt(414,191,"Visual, language and speech signals align",18,"#d1ddeb")
    b+=txt(414,214,"to locate moments across Vietnamese video.",18,"#d1ddeb")
    b+=txt(414,251,"READ THE SPRINGER PAPER  ↗",16,"#f1c78d",700)
    save(out,"video-v3.svg",900,270,b)

    # Mobile: stacked compositions maintain readable type inside GitHub's ~260px README column.
    for name,visual,accent,title,metric,line1,line2,link in [
        ("lexviet",query_art(4,0,.8),TEAL,"LexViet","0.9428 Competition Score","Hybrid retrieval for Vietnamese law","11 signals · ranking · six-view reranking","REPOSITORY  ↗"),
        ("detection",road_art(0,0,.84),RUST,"Multi-Vehicle Detection","1st Place / 97 teams","Human-verified missing-label audits","0.94052 private mAP@0.5","REPOSITORY  ↗"),
        ("video",video_art(5,0,.9),"#b9d4e6","Video Retrieval","~600K Keyframes","1,478 videos · 300+ hours","First-author multimodal research","SPRINGER PAPER  ↗"),
    ]:
        dark=name=="video"; bg=COBALT if dark else CREAM; fg=WHITE if dark else INK
        b=f'<rect width="480" height="390" fill="{bg}"/><path d="M0 0H480" stroke="{accent}" stroke-width="5"/>'
        b+=f'<g transform="translate(0 6)">{visual}</g>'
        b+=f'<rect y="207" width="480" height="183" fill="{bg}"/>'
        b+=txt(23,243,title,32,fg,700)+txt(23,283,metric,27,accent,700)
        b+=txt(23,316,line1,19,fg)+txt(23,340,line2,19,fg)
        b+=txt(23,374,link,17,accent,700)
        save(out,name+"-mobile.svg",480,390,b)

if __name__ == "__main__":
    build_cards(Path(__file__).parent/"assets")

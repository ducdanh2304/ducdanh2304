"""Compact editorial project covers, sized for GitHub's narrow mobile column."""
from html import escape
from pathlib import Path

INK = "#f4f6f7"
SOFT = "#c0cbd4"
TEAL = "#64d9cc"
AMBER = "#f1b572"
BLUE = "#a5b4fc"
CSS = """<style>.type{font-family:Arial,Helvetica,sans-serif}
.move{stroke-dasharray:7 10;animation:slide 15s linear infinite}
@keyframes slide{to{stroke-dashoffset:-170}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}</style>"""

def t(x,y,s,size,color=INK,weight=400,extra=""):
    return f'<text class="type" x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" {extra}>{escape(s)}</text>'

def save(out,name,body):
    (out/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="270" viewBox="0 0 600 270" role="img" aria-label="{escape(name)}">{CSS}{body}</svg>',encoding="utf-8")

def build_cards(out: Path):
    out.mkdir(exist_ok=True)
    b=f'<rect width="600" height="270" rx="7" fill="#08131f"/><path d="M0 3H600" stroke="{TEAL}" stroke-width="4"/>'
    b+=t(23,32,"01 / LEXVIET",18,TEAL,700)+t(23,74,"Vietnamese legal retrieval",31,INK,700)
    b+=t(23,146,"0.9428",72,INK,800)+t(272,143,"COMPETITION SCORE",19,TEAL,700)
    b+=t(23,175,"2,080 queries · 596,062 legal chunks",21,SOFT)
    b+=f'<path d="M23 191H577" stroke="#385361"/>'
    b+=t(23,222,"11 signals → Weighted RRF",23,INK,700)
    b+=t(23,251,"2-stage LightGBM LambdaMART · 6-view Jina",20,SOFT)
    save(out,"lexviet-v2.svg",b)

    b=f'<rect width="600" height="270" rx="7" fill="#111b23"/><path d="M0 3H600" stroke="{AMBER}" stroke-width="4"/>'
    b+=t(23,32,"02 / 3LC MULTI-VEHICLE DETECTION",18,AMBER,700)
    b+=t(23,109,"1st",79,INK,800)+t(153,105,"PLACE / 97 TEAMS",22,AMBER,700)
    b+=t(23,153,"0.94052",47,INK,800)+t(243,152,"PRIVATE mAP@0.5",19,AMBER,700)
    b+=f'<path d="M23 173H577" stroke="#665344"/>'
    b+=t(23,203,"Model flags missing labels; humans verify edits.",21,INK,600)
    b+=t(23,229,"61 dataset revisions · 21 human review loops",20,SOFT)
    b+=t(23,254,"YOLOv8n · random init · 250 epochs",20,AMBER)
    save(out,"detection-v2.svg",b)

    b=f'<rect width="600" height="270" rx="7" fill="#17273b"/><path d="M0 3H600" stroke="{BLUE}" stroke-width="4"/>'
    b+=t(23,32,"03 / FIRST-AUTHOR RESEARCH",18,BLUE,700)+t(23,72,"Multimodal video retrieval",31,INK,700)
    b+=t(23,146,"1,478",70,INK,800)+t(207,142,"VIDEOS",22,BLUE,700)
    b+=t(23,174,"300+ hours · ~600K keyframes",21,SOFT)
    b+=f'<path d="M23 191H577" stroke="#4b617d"/>'
    b+=t(23,222,"Visual embeddings + Vietnamese captions",21,INK,600)
    b+=t(23,251,"Speech · OCR · temporal alignment",20,SOFT)
    save(out,"video-v2.svg",b)

if __name__ == "__main__":
    build_cards(Path(__file__).parent/"assets")

"""Three editorial project covers for the GitHub profile."""
from html import escape
from pathlib import Path

BG = "#08131f"
INK = "#f4f6f7"
SOFT = "#bdcbd5"
TEAL = "#64d9cc"
AMBER = "#f1b572"
BLUE = "#a5b4fc"
CSS = """<style>
.type{font-family:Arial,Helvetica,sans-serif}
.move{stroke-dasharray:7 10;animation:slide 15s linear infinite}
.glow{animation:glow 3s ease-in-out infinite}
@keyframes slide{to{stroke-dashoffset:-170}}
@keyframes glow{50%{opacity:.4}}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}
</style>"""

def text(x, y, value, size, color=INK, weight=400, extra=""):
    return f'<text class="type" x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" {extra}>{escape(value)}</text>'

def save(out, name, height, body):
    (out / name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="{height}" viewBox="0 0 800 {height}" role="img" aria-label="{escape(name)}">{CSS}{body}</svg>',
        encoding="utf-8",
    )

def build_cards(out: Path):
    out.mkdir(exist_ok=True)
    # LexViet: a query becomes ranked legal passages, with the measured competition result dominant.
    b=f'<rect width="800" height="276" rx="8" fill="{BG}"/><path d="M0 4H800" stroke="{TEAL}" stroke-width="4"/>'
    b+=text(26,39,"01 / LEXVIET",17,TEAL,700)+text(26,82,"Vietnamese legal retrieval",31,INK,700)
    b+=text(26,150,"0.9428",65,INK,800)+text(267,149,"COMPETITION SCORE",18,TEAL,700)
    b+=text(26,181,"2,080 private queries  ·  596,062 legal chunks",19,SOFT)
    b+=f'<path d="M26 199H774" stroke="#36505f"/>'
    b+=text(26,231,"11-signal retrieval → Weighted RRF",19,INK,600)
    b+=text(26,257,"2-stage LightGBM LambdaMART · 6-view Jina reranking",18,SOFT)
    b+=f'<path d="M595 92H739" stroke="{TEAL}" opacity=".5" class="move"/><circle cx="740" cy="92" r="5" fill="{TEAL}" class="glow"/>'
    save(out,"lexviet-v2.svg",276,b)

    # Detection: score and rank, then the human verification loop.
    b=f'<rect width="800" height="270" rx="8" fill="#101a23"/><path d="M0 4H800" stroke="{AMBER}" stroke-width="4"/>'
    b+=f'<rect x="0" y="4" width="220" height="266" fill="#32261c"/>'
    b+=text(24,40,"02 / 3LC CHALLENGE",16,AMBER,700)+text(24,119,"1st",80,INK,800)
    b+=text(24,156,"PLACE / 97 TEAMS",20,AMBER,700)
    b+=text(243,50,"Multi-Vehicle Detection",31,INK,700)
    b+=text(243,104,"0.94052",48,INK,800)+text(491,103,"PRIVATE mAP@0.5",17,AMBER,700)
    b+=f'<path d="M243 122H771" stroke="#61513f"/>'
    b+=text(243,157,"Predictions flag missing-label candidates;",19,SOFT)
    b+=text(243,181,"humans verify every accepted correction.",19,SOFT)
    b+=text(243,222,"61 dataset revisions · 21 review iterations",17,INK,600)
    b+=text(243,248,"YOLOv8n · random init · 250 epochs",17,SOFT)
    save(out,"detection-v2.svg",270,b)

    # Research: a lighter scientific plate and a keyframe sequence distinguish it from competitions.
    b=f'<rect width="800" height="272" rx="8" fill="#152334"/><path d="M0 4H800" stroke="{BLUE}" stroke-width="4"/>'
    b+=text(26,39,"03 / FIRST-AUTHOR RESEARCH",17,BLUE,700)
    b+=text(26,79,"Multimodal video retrieval",31,INK,700)
    b+=text(26,133,"1,478",61,INK,800)+text(227,131,"VIDEOS",20,BLUE,700)
    b+=text(26,164,"300+ hours · ~600,000 keyframes",19,SOFT)
    b+=f'<path d="M26 182H774" stroke="#41566c"/>'
    b+=text(26,216,"Visual embeddings + Vietnamese captions",19,INK,600)
    b+=text(26,244,"Speech, OCR and temporal alignment",18,SOFT)
    for i in range(4):
        x=503+i*65
        b+=f'<rect x="{x}" y="96" width="53" height="43" rx="2" fill="#233c50" stroke="{BLUE}" opacity=".65"/>'
        b+=f'<path d="M{x+6} 126l11-14 10 8 10-11 9 16" fill="none" stroke="{BLUE}" opacity=".6"/>'
    save(out,"video-v2.svg",272,b)

if __name__ == "__main__":
    build_cards(Path(__file__).parent / "assets")

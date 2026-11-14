"""Electric Blue × Deep Violet. Standard-library SVG source; no build services."""
from pathlib import Path
from html import escape
import math, sys, re

ROOT = Path(__file__).parent
A = ROOT / 'assets'
A.mkdir(exist_ok=True)
WHITE, MUTED, BLUE, VIOLET, CYAN = '#E8ECFF', '#9AA6C8', '#3B82F6', '#A78BFA', '#22D3EE'

def text(x,y,s,size=24,color=WHITE,weight=400,extra=''):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(s)}</text>'

def line(x1,y1,x2,y2,color='#293451',width=1):
    return f'<path d="M{x1} {y1} L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}"/>'

def signal(d,color=CYAN,dur=6,begin=0):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-opacity=".30" stroke-width="1.5"/><circle r="3" fill="{color}"><animateMotion path="{d}" dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/></circle>'

def svg(w,h,body,title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title,quote=True)}">
<title>{escape(title)}</title><defs>
<linearGradient id="ink" x2="1" y2="1"><stop stop-color="#2563EB"/><stop offset=".6" stop-color="#6D28D9"/><stop offset="1" stop-color="#22D3EE"/></linearGradient>
<radialGradient id="halo"><stop stop-color="#6D28D9" stop-opacity=".55"/><stop offset="1" stop-color="#080B1A" stop-opacity="0"/></radialGradient>
<linearGradient id="veil" x2=".7" y2="1"><stop stop-color="#2563EB" stop-opacity="0"/><stop offset=".5" stop-color="#7C3AED" stop-opacity=".7"/><stop offset="1" stop-color="#22D3EE" stop-opacity=".12"/></linearGradient>
<filter id="soft"><feGaussianBlur stdDeviation="22"/></filter>
<pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse"><path d="M50 0 H0 V50" fill="none" stroke="#A78BFA" stroke-opacity=".055"/></pattern>
</defs><rect width="100%" height="100%" fill="#080B1A"/><g font-family="Inter, 'Space Grotesk', Arial, Helvetica, sans-serif">{body}</g></svg>'''

def save(name,w,h,b,title):
    (A/name).write_text(svg(w,h,b,title),encoding='utf-8')

def orb(cx,cy,r):
    b=f'<circle cx="{cx}" cy="{cy}" r="{r*1.8}" fill="url(#halo)"/>'
    b+=f'<g transform="translate({cx} {cy})"><g><animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="32s" repeatCount="indefinite"/>'
    for angle in (0,60,120):
        b+=f'<ellipse rx="{r}" ry="{r*.40}" transform="rotate({angle})" fill="none" stroke="url(#ink)" stroke-width="1.2"/>'
    b+='</g>'
    pts=[(math.cos(i*math.pi/3)*r*.78,math.sin(i*math.pi/3)*r*.78) for i in range(6)]
    b+='<g><animateTransform attributeName="transform" type="rotate" values="-6;6;-6" dur="14s" repeatCount="indefinite"/>'
    for i,(x,y) in enumerate(pts):
        x2,y2=pts[(i+2)%6]
        b+=signal(f'M{x:.1f} {y:.1f} Q0 0 {x2:.1f} {y2:.1f}',BLUE if i%2 else CYAN,5+i*.45,-i)
        b+=f'<circle cx="{x}" cy="{y}" r="4" fill="{VIOLET}"><animate attributeName="r" values="3;5;3" dur="{3+i*.2}s" repeatCount="indefinite"/></circle>'
    b+='</g><path d="M0 -52 C60 -60 65 30 0 55 C-65 40 -60 -45 0 -52Z" fill="url(#ink)" opacity=".75"><animate attributeName="d" values="M0 -52 C60 -60 65 30 0 55 C-65 40 -60 -45 0 -52Z;M0 -65 C35 -35 70 60 0 40 C-40 65 -70 -65 0 -65Z;M0 -52 C60 -60 65 30 0 55 C-65 40 -60 -45 0 -52Z" dur="24s" repeatCount="indefinite"/></path></g>'
    return b

def hero(mobile=False):
    w,h=(600,760) if mobile else (1000,500)
    b='<rect width="100%" height="100%" fill="url(#grid)"/>'
    b+='<g opacity=".65" filter="url(#soft)"><path d="M-100 330 C200 -140 500 600 1100 20 L1100 210 C450 740 240 80 -100 480Z" fill="url(#veil)"><animate attributeName="d" values="M-100 330 C200 -140 500 600 1100 20 L1100 210 C450 740 240 80 -100 480Z;M-100 170 C200 550 500 -160 1100 220 L1100 420 C450 20 240 720 -100 370Z;M-100 330 C200 -140 500 600 1100 20 L1100 210 C450 740 240 80 -100 480Z" dur="26s" repeatCount="indefinite"/></path></g>'
    b+=orb(310 if mobile else 790,510 if mobile else 240,165)
    b+=text(40,54,'VISION  /  LANGUAGE  /  RETRIEVAL',16,CYAN,600, 'letter-spacing="2"')
    b+=text(40,145,'DANH DUC',64 if mobile else 76,WHITE,750,'letter-spacing="-3"')
    b+=text(40,220,'NGUYEN',74 if mobile else 88,WHITE,750,'letter-spacing="-3"')
    b+='<path d="M42 240 H220" stroke="url(#ink)" stroke-width="3" stroke-dasharray="55 12"><animate attributeName="stroke-dashoffset" from="0" to="-134" dur="8s" repeatCount="indefinite"/></path>'
    b+=text(40,285,'AI ENGINEERING  ·  COMPUTER VISION',19,WHITE,600)
    b+=text(40,315,'INFORMATION RETRIEVAL  ·  MULTIMODAL AI',18,MUTED)
    yy=690 if mobile else 420
    b+=text(40,yy,'Building intelligent systems across',23)
    b+=text(40,yy+32,'vision, language, and retrieval.',23,MUTED)
    save('hero-mobile.svg' if mobile else 'hero.svg',w,h,b,'Danh Duc Nguyen — Building intelligent systems across vision, language, and retrieval.')

def moodboards():
    out=ROOT.parents[2]/'outputs'
    out.mkdir(exist_ok=True)
    for i,(name,caption) in enumerate([('Aurora Neural Studio','Atmospheric light / neural sculpture / Swiss typography'),('Violet Type Observatory','Typographic contrast / liquid symbol / holographic edge'),('Electric Flow Atlas','Parallel streamlines / geometric territories / print layers')]):
        b=text(40,52,f'0{i+1} — {name}',30,WHITE,700)+text(40,88,caption,18,MUTED)
        if i==0:
            b+=orb(735,250,125)+text(45,220,'DANH DUC',60,WHITE,700)+text(45,290,'NGUYEN',70,WHITE,700)
        elif i==1:
            b+=text(40,240,'DANH.',120,VIOLET,700)+text(45,305,'Intelligence, in motion.',28)
            b+='<circle cx="770" cy="230" r="95" fill="url(#ink)"/>'
        else:
            for j in range(20): b+=f'<path d="M40 {130+j*9} C300 {30+j*9} 500 {440-j*8} 950 {120+j*8}" stroke="{BLUE if j%2 else VIOLET}" fill="none" opacity=".55"/>'
        for j,c in enumerate(['#080B1A','#2563EB','#6D28D9','#A78BFA','#22D3EE']): b+=f'<rect x="{40+j*180}" y="360" width="164" height="20" fill="{c}"/>'
        (out/f'concept-{i+1}.svg').write_text(svg(1000,420,b,name),encoding='utf-8')

if __name__=='__main__':
    hero(); hero(True); moodboards()

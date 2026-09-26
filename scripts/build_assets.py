"""Build the profile's self-contained SVG artwork. Python standard library only."""

from html import escape
from math import cos, sin, pi
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
NAVY, PANEL, LINE, BLUE = "#0A1628", "#0F2039", "#1B3A63", "#2E5A94"
MUTED, LIGHT, WHITE = "#8A94A6", "#C9CFD9", "#FFFFFF"

STYLE = """
text { font-family: 'Segoe UI', Arial, sans-serif; }
.mono { font-family: Consolas, 'Courier New', monospace; }
.orbit { transform-box: fill-box; transform-origin: center; animation: orbit 38s linear infinite; }
.reverse { animation-direction: reverse; animation-duration: 52s; }
.flow { stroke-dasharray: 5 19; animation: flow 5s linear infinite; }
.pulse { animation: pulse 5s ease-in-out infinite; }
.float { animation: float 7s ease-in-out infinite; }
@keyframes orbit { to { transform: rotate(360deg); } }
@keyframes flow { to { stroke-dashoffset: -96; } }
@keyframes pulse { 0%, 100% { opacity: .35; } 50% { opacity: .9; } }
@keyframes float { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
@media (prefers-reduced-motion: reduce) {
  .orbit, .flow, .pulse, .float { animation: none !important; }
}
"""


def text(x, y, value, size=18, fill=LIGHT, weight=400, extra=""):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" {extra}>{escape(value)}</text>')


def rect(x, y, w, h, fill=PANEL, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'


def path(d, stroke=LINE, width=1, extra=""):
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{width}" {extra}/>'


def svg(name, w, h, title, content):
    document = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">Custom navy and white artwork for James Vincent Calunsag. Decorative motion stops when reduced motion is requested.</desc>
<defs>
  <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M 32 0 L 0 0 0 32" fill="none" stroke="{LINE}" stroke-opacity=".3"/></pattern>
  <radialGradient id="halo"><stop stop-color="{BLUE}" stop-opacity=".4"/><stop offset="1" stop-color="{NAVY}" stop-opacity="0"/></radialGradient>
  <linearGradient id="metal" x2="1" y2="1"><stop stop-color="{BLUE}"/><stop offset=".5" stop-color="{PANEL}"/><stop offset="1" stop-color="{LINE}"/></linearGradient>
</defs>
<style>{STYLE}</style>
{rect(0, 0, w, h, NAVY, 16)}
{content}
</svg>
'''
    (ASSETS / name).write_text(document, encoding="utf-8")


def processor(cx, cy, scale=1):
    parts = [f'<g transform="translate({cx} {cy}) scale({scale})">']
    parts += ['<circle r="250" fill="url(#halo)"/>',
              f'<circle r="195" fill="none" stroke="{LINE}"/>',
              f'<circle r="160" fill="none" stroke="{LINE}" stroke-dasharray="2 10"/>']
    for a in range(0, 360, 15):
        angle = a * pi / 180
        x1, y1, x2, y2 = [round(v, 2) for v in
                         (200*cos(angle), 200*sin(angle), 206*cos(angle), 206*sin(angle))]
        parts.append(path(f'M{x1} {y1} L{x2} {y2}', BLUE))
    parts += [f'<g class="orbit"><circle r="195" fill="none" stroke="{LIGHT}" stroke-width="2" stroke-dasharray="80 1146"/>',
              f'<circle cx="195" r="5" fill="{WHITE}"/></g>',
              f'<g class="orbit reverse"><circle r="160" fill="none" stroke="{BLUE}" stroke-width="3" stroke-dasharray="90 915"/></g>']
    routes = ['M-205 0 H-125 L-93 -32 H-66', 'M205 0 H125 L93 32 H66',
              'M0 -205 V-126 L32 -94 V-66', 'M0 205 V126 L-32 94 V66']
    for d in routes:
        parts += [path(d, BLUE, 1.5), path(d, LIGHT, 2, 'class="flow"')]
    parts.append('<g class="float">')
    parts += [path('M-92 -49 L0 -100 L92 -49 V58 L0 110 L-92 58 Z', LINE),
              '<path d="M-84 -44 L0 -92 L84 -44 V48 L0 96 L-84 48Z" fill="url(#metal)" stroke="#2E5A94"/>',
              path('M-84 -44 L0 4 L84 -44 M0 4 V96', BLUE, 1.5)]
    for i in range(7):
        offset = -56 + i * 18
        parts += [path(f'M{offset} {-61 + (offset+56)*.57} l-15 9', LIGHT, 2),
                  path(f'M{offset} {59 + (offset+56)*.57} l-15 9', BLUE, 2)]
    parts += [rect(-64, -65, 128, 128, NAVY, 18, f'stroke="{BLUE}" stroke-width="2"'),
              rect(-53, -54, 106, 106, PANEL, 12, f'stroke="{LINE}"'),
              text(0, 13, 'JC', 48, WHITE, 600, 'text-anchor="middle" letter-spacing="-3"'),
              text(0, 37, 'ENGINEER', 10, MUTED, extra='class="mono" text-anchor="middle" letter-spacing="2"'),
              '</g>', '</g>']
    return ''.join(parts)


def hero(mobile=False):
    w, h = (640, 930) if mobile else (1200, 650)
    p = 36 if mobile else 56
    content = rect(w*.49, 0, w*.51, h, 'url(#grid)')
    content += text(p, 48, 'tengkyuuu', 20, WHITE, 600, 'letter-spacing="-1"')
    content += text(w-p, 48, 'ENGINEERING / DESIGN', 12, MUTED, extra='class="mono" text-anchor="end" letter-spacing="1.5"')
    content += path(f'M{p} 72 H{w-p}', LINE)
    content += text(p, 123 if mobile else 155, 'FROM SILICON TO SCREEN', 13, LIGHT, extra='class="mono" letter-spacing="3"')
    content += text(p-4, 208 if mobile else 252, 'James Vincent', 73 if mobile else 78, WHITE, 650, 'letter-spacing="-4"')
    content += text(p-5, 295 if mobile else 351, 'Calunsag.', 96 if mobile else 106, WHITE, 650, 'letter-spacing="-5"')
    content += rect(p, 324 if mobile else 393, 44, 3, BLUE)
    content += text(p, 366 if mobile else 441, 'I build the circuit.', 23, LIGHT)
    content += text(p, 399 if mobile else 475, 'And the experience around it.', 23, LIGHT)
    content += processor(320, 643, .93) if mobile else processor(938, 309, 1)
    if not mobile:
        content += text(938, 548, 'HARDWARE  /  SOFTWARE  /  HUMAN', 11, MUTED, extra='class="mono" text-anchor="middle" letter-spacing="1.4"')
    y = h-68
    content += path(f'M{p} {y} H{w-p}', LINE)
    content += f'<circle cx="{p+4}" cy="{y+31}" r="4" fill="{LIGHT}" class="pulse"/>'
    content += text(p+18, y+36, 'OPEN TO OPPORTUNITIES', 11, LIGHT, extra='class="mono" letter-spacing="1"')
    content += text(w-p, y+36, 'DAPITAN, PH  /  UTC+8', 11, MUTED, extra='class="mono" text-anchor="end" letter-spacing="1"')
    svg('hero-mobile.svg' if mobile else 'hero.svg', w, h,
        'James Vincent Calunsag — from silicon to screen', content)


def portfolio():
    c = rect(650, 0, 550, 280, 'url(#grid)')
    c += text(44, 47, 'FEATURED EXPERIENCE / 01', 12, MUTED, extra='class="mono" letter-spacing="2"')
    c += text(41, 119, 'Portfolio.docx', 54, WHITE, 600, 'letter-spacing="-2"')
    c += text(44, 162, 'A portfolio that behaves like a Word document.', 21, LIGHT)
    c += text(44, 226, 'OPEN THE DOCUMENT', 13, WHITE, 600, 'class="mono" letter-spacing="1.5"')
    c += path('M247 221 H281 M274 214 L281 221 L274 228', LIGHT, 1.5)
    c += '<g class="float">'
    c += rect(859, 35, 196, 224, PANEL, 8, f'stroke="{LINE}"')
    c += rect(840, 20, 196, 224, NAVY, 8, f'stroke="{BLUE}"')
    c += rect(840, 20, 196, 36, LINE, 8)
    c += text(855, 43, 'portfolio.docx', 12, LIGHT, extra='class="mono"')
    c += text(860, 96, 'Hello, I’m James.', 18, WHITE, 600)
    c += text(860, 119, 'Engineer. Builder. Designer.', 10, MUTED)
    for y, length in [(145, 145), (157, 145), (169, 110)]:
        c += rect(860, y, length, 3, LINE, 1)
    c += rect(860, 197, 57, 21, LINE, 3)
    c += text(870, 212, 'WORK ↗', 10, LIGHT, extra='class="mono"')
    c += '</g>'
    svg('portfolio.svg', 1200, 280, 'Portfolio.docx — open my interactive portfolio', c)


def signal_path():
    c = text(40, 44, 'SHM / A READING’S JOURNEY', 13, MUTED, extra='class="mono" letter-spacing="2"')
    nodes = [('01', 'SENSOR', 'accel / strain'), ('02', 'ESP32', 'filter / pack'),
             ('03', 'TRANSPORT', 'Wi-Fi / MQTT'), ('04', 'STORAGE', 'time series'),
             ('05', 'DASHBOARD', 'charts / alerts')]
    c += path('M110 100 H1080', BLUE, 2)
    c += path('M110 100 H1080', LIGHT, 3, 'class="flow"')
    for i, (number, label, detail) in enumerate(nodes):
        x = 40+i*230
        c += rect(x, 73, 200, 109, PANEL, 8, f'stroke="{LINE}"')
        c += text(x+16, 98, number, 12, MUTED, extra='class="mono"')
        c += text(x+16, 131, label, 17, WHITE, 600, 'class="mono"')
        c += text(x+16, 158, detail, 15, LIGHT)
    svg('signal-path.svg', 1200, 214, 'SHM — sensor to dashboard', c)


def buttons():
    for name, label, width in [('portfolio', 'Explore portfolio', 206),
                               ('email', 'Email me', 144), ('linkedin', 'LinkedIn', 144)]:
        c = rect(1, 1, width-2, 42, LINE if name == 'portfolio' else PANEL, 7, f'stroke="{BLUE}"')
        c += text(17, 28, label, 14, WHITE, 600)
        c += path(f'M{width-30} 27 l10 -10 m-10 0 h10 v10', LIGHT, 1.5)
        svg(f'button-{name}.svg', width, 44, label, c)


def footer():
    c = path('M0 1 H1200', BLUE)
    c += path('M0 1 H1200', LIGHT, 2, 'class="flow"')
    c += text(35, 44, 'THANKS FOR STOPPING BY', 12, MUTED, extra='class="mono" letter-spacing="2"')
    c += text(35, 78, 'Adaptability is the engineering skill.', 23, WHITE, 500)
    c += text(1165, 76, '— tengkyuuu', 18, LIGHT, extra='class="mono" text-anchor="end"')
    svg('footer.svg', 1200, 112, 'Adaptability is the engineering skill. — tengkyuuu', c)


if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    hero()
    hero(mobile=True)
    portfolio()
    signal_path()
    buttons()
    footer()
    print('Built 8 self-contained SVG assets.')

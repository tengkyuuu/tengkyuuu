"""Build static, self-contained SVG artwork with the Python standard library.

Run from any directory: python scripts/build_assets.py
The README supplies interaction through native links and disclosure sections.
"""

from html import escape
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / "assets"
PAPER, INK, GREEN = "#F0EFE7", "#233E31", "#42634B"
SAGE, GOLD, LINE, MUTED = "#89947A", "#B39B59", "#B5BAA7", "#626D5D"
MONO = 'class="mono"'


def text(x, y, value, size=18, fill=INK, weight=400, extra=""):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" {extra}>{escape(value)}</text>')


def rect(x, y, w, h, fill=PAPER, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'


def path(d, stroke=LINE, width=1, extra=""):
    return f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{width}" {extra}/>'


def solid(d, fill, extra=""):
    return f'<path d="{d}" fill="{fill}" {extra}/>'


def svg(name, w, h, title, content, desc=""):
    description = desc or "Teng / James Vincent Calunsag. Forest green, muted gold, and textured drafting paper. Static artwork."
    document = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title>
<desc id="desc">{escape(description)}</desc>
<defs>
  <pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="{LINE}" stroke-opacity=".24" stroke-width=".6"/></pattern>
  <filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".76" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
  <filter id="shadow" x="-40%" y="-40%" width="200%" height="210%"><feDropShadow dx="3" dy="12" stdDeviation="9" flood-color="{INK}" flood-opacity=".22"/></filter>
  <linearGradient id="green-top" x2=".3" y2="1"><stop stop-color="#638067"/><stop offset="1" stop-color="#3E6049"/></linearGradient>
  <linearGradient id="cream-top" x2=".3" y2="1"><stop stop-color="#FAF8EF"/><stop offset="1" stop-color="#D8D9C9"/></linearGradient>
  <linearGradient id="gold-top" x2=".3" y2="1"><stop stop-color="#D8C486"/><stop offset="1" stop-color="#AD9554"/></linearGradient>
</defs>
<style>text {{ font-family: 'Segoe UI', Arial, sans-serif; }} .mono {{ font-family: Consolas, 'Courier New', monospace; }}</style>
{rect(0, 0, w, h)}
{content}
{rect(0, 0, w, h, '#808080', extra='filter="url(#grain)" opacity=".065" pointer-events="none"')}
</svg>
'''
    (ASSETS / name).write_text(document, encoding="utf-8")


# Drawn letterforms keep the identity consistent without hosted fonts.
GLYPHS = {
    "T": "M0 0H100V26H64V124H36V26H0Z",
    "E": "M100 0H0V124H100V98H28V75H87V49H28V26H100Z",
    "N": "M0 124V0H28L72 75V0H100V124H73L28 49V124Z",
    "G": "M100 0H32Q0 0 0 32V92Q0 124 32 124H100V55H53V80H73V98H36Q28 98 28 89V35Q28 26 36 26H100Z",
}


def wordmark(x, y, scale=1, colors=None):
    colors = colors or [GOLD, GREEN, GREEN, GREEN]
    c = f'<g transform="translate({x} {y}) scale({scale})">'
    for i, letter in enumerate("TENG"):
        c += solid(GLYPHS[letter], colors[i], f'transform="translate({i * 116} 0)"')
    return c + '</g>'


def cross(x, y, size=7, color=SAGE):
    return path(f'M{x-size} {y}H{x+size} M{x} {y-size}V{y+size}', color, .8)


def ruler(x, y, width, divisions=12):
    c = path(f'M{x} {y}H{x+width}', SAGE, .8)
    for i in range(divisions * 5 + 1):
        xx = round(x + width * i / (divisions * 5), 2)
        c += path(f'M{xx} {y}v{15 if i % 5 == 0 else 6}', MUTED, .8)
        if i % 5 == 0:
            c += text(xx, y+30, str(i//5).zfill(2), 9, MUTED, extra=f'{MONO} text-anchor="middle"')
    return c


def keycap(x, y, letter, kind="green", sub=""):
    side, rim, legend = {
        "green": ("#243C2E", "#799079", PAPER),
        "cream": ("#AAAFA0", "#FFFFF5", INK),
        "gold": ("#7E693A", "#E6D49B", INK),
    }[kind]
    c = f'<g transform="translate({x} {y})">'
    c += rect(0, 20, 116, 120, side, 15)
    c += solid('M3 36L15 9H101L113 36V116Q113 127 102 127H14Q3 127 3 116Z', side)
    c += rect(8, 0, 100, 108, f'url(#{kind}-top)', 14, f'stroke="{rim}" stroke-width="1.2"')
    c += path('M22 6H94 Q102 6 102 16', rim, 1, 'opacity=".7"')
    c += solid(GLYPHS[letter], legend, 'transform="translate(33 21) scale(.45)"')
    c += text(23, 94, sub, 7, legend, extra=MONO)
    c += path('M12 119H103', rim, .6, 'opacity=".3"')
    return c + '</g>'


def keyset(x, y, scale=1):
    c = f'<g transform="translate({x} {y}) scale({scale})">'
    c += '<g transform="matrix(.94 .25 -.34 .83 45 0)" filter="url(#shadow)">'
    c += rect(-15, 2, 278, 300, '#A4AD99', 23, f'stroke="{SAGE}"')
    c += rect(-15, -6, 278, 294, '#CED2BF', 23, f'stroke="{PAPER}"')
    c += rect(-7, 2, 262, 278, INK, 17)
    for xx, yy, letter, kind, sub in [
        (0, 0, 'T', 'gold', '01 / TENG'),
        (132, 0, 'E', 'cream', '02 / BUILD'),
        (0, 139, 'N', 'cream', '03 / MAKE'),
        (132, 139, 'G', 'green', '04 / PLAY'),
    ]:
        c += keycap(xx, yy, letter, kind, sub)
    return c + '</g></g>'


def hero(mobile=False):
    w, h = (640, 1010) if mobile else (1200, 720)
    p = 36 if mobile else 56
    c = rect(0, 86, w, h-165, 'url(#grid)')
    c += wordmark(p, 29, .20, [INK]*4)
    c += text(p+108, 47, '/ tengkyuuu', 13, MUTED, extra=MONO)
    c += text(w-p, 47, 'ENGINEERING & DESIGN', 11, INK, extra=f'{MONO} text-anchor="end" letter-spacing="1.5"')
    c += path(f'M{p} 75H{w-p}', INK)
    c += text(p, 116, 'PERSONAL FIELD NOTES', 11, MUTED, extra=f'{MONO} letter-spacing="2"')
    c += text(w-p, 116, 'VOL. 01 / PH', 11, MUTED, extra=f'{MONO} text-anchor="end"')
    scale, mark_y = (1.26, 196) if mobile else (1.43, 218)
    mark_w, mark_h = 448*scale, 124*scale
    c += ruler(p+8, 147, mark_w-16)
    for yy in [mark_y, mark_y+mark_h]:
        c += path(f'M{p-15} {yy}H{p+mark_w+15}', SAGE)
    for xx in [p, p+100*scale, p+116*scale, p+216*scale, p+232*scale, p+332*scale, p+348*scale, p+448*scale]:
        c += path(f'M{xx:.2f} {mark_y-16}V{mark_y+mark_h+16}', SAGE, .8)
    c += wordmark(p, mark_y, scale)
    for xx in [p, p+mark_w]:
        c += cross(xx, mark_y, 10, GOLD)
        c += cross(xx, mark_y+mark_h, 10, GOLD)
    label_y = 379 if mobile else 424
    c += rect(p, label_y, 258, 29, GREEN)
    c += text(p+13, label_y+19, 'CIRCUITS. CODE. CHARACTER.', 11, PAPER, extra=f'{MONO} letter-spacing="1"')
    name_y = 455 if mobile else 501
    c += text(p, name_y, 'James Vincent Calunsag', 31 if mobile else 34, INK, 600, 'letter-spacing="-1"')
    c += text(p, name_y+32, 'Computer engineer. Builder by nature.', 18, MUTED)
    c += text(p, name_y+61, 'From the circuit board to the browser.', 18, MUTED)
    if mobile:
        c += keyset(190, 571, 1.03)
        c += text(p, 573, 'FIG. 01', 10, MUTED, extra=MONO)
        c += text(w-p, 905, 'THE TENG KEYSET / 2 × 2', 11, MUTED, extra=f'{MONO} text-anchor="end"')
    else:
        c += path('M747 146V603', LINE, .8)
        c += text(792, 169, 'OBJECT STUDY / 001', 11, MUTED, extra=f'{MONO} letter-spacing="1.5"')
        c += keyset(825, 221, 1.06)
        c += path('M804 230V208H830 M1118 544H1138V519', SAGE)
        c += path('M807 567H1125 M807 560V574 M1125 560V574', SAGE, .8)
        c += text(966, 590, 'THE TENG KEYSET / 2 × 2', 11, MUTED, extra=f'{MONO} text-anchor="middle" letter-spacing="1"')
    fy = h-78
    c += path(f'M{p} {fy}H{w-p}', INK)
    c += rect(p, fy+24, 7, 7, GREEN)
    c += text(p+18, fy+32, 'OPEN TO OPPORTUNITIES', 11, INK, extra=f'{MONO} letter-spacing=".6"')
    c += text(w-p, fy+32, 'DAPITAN, PH / UTC+8', 11, MUTED, extra=f'{MONO} text-anchor="end"')
    c += text(p, h-15, 'EMBEDDED SYSTEMS / FRONTEND / VISUAL DESIGN', 9, MUTED, extra=f'{MONO} letter-spacing="1.1"')
    svg('hero-mobile.svg' if mobile else 'hero.svg', w, h,
        'TENG — James Vincent Calunsag / Computer engineer', c,
        'A custom TENG wordmark on architectural construction lines, with a dimensional four-key mechanical keycap mockup in forest green, ivory, and muted gold. James Vincent Calunsag. Embedded systems, frontend, and visual design. Open to opportunities. Dapitan, Philippines.')


def portfolio():
    c = rect(724, 0, 476, 300, 'url(#grid)')
    c += rect(0, 0, 7, 300, GREEN)
    c += text(44, 43, 'SELECTED WORK / 01', 11, MUTED, extra=f'{MONO} letter-spacing="2"')
    c += text(41, 117, 'Portfolio.docx', 57, INK, 600, 'letter-spacing="-2"')
    c += text(44, 159, 'A portfolio that behaves like a Word document.', 20, MUTED)
    c += rect(44, 204, 243, 43, GREEN, 2)
    c += text(60, 231, 'OPEN THE DOCUMENT', 12, PAPER, 600, f'{MONO} letter-spacing="1"')
    c += path('M258 232l11 -11m-11 0h11v11', PAPER, 1.4)
    c += '<g transform="translate(853 26) rotate(7 100 120)" filter="url(#shadow)">'
    c += rect(7, 8, 212, 246, '#D8DDCE', 2, f'stroke="{SAGE}"')
    c += rect(0, 0, 212, 246, '#FAF9F1', 2, f'stroke="{SAGE}"')
    c += rect(0, 0, 212, 30, GREEN)
    c += text(13, 20, 'portfolio.docx', 11, PAPER, extra=MONO)
    c += wordmark(18, 49, .17)
    c += text(18, 107, 'Hello, I’m James.', 20, INK, 600)
    c += text(18, 128, 'Engineer. Builder. Designer.', 10, MUTED)
    for yy, length in [(151, 168), (162, 168), (173, 121)]:
        c += path(f'M18 {yy}h{length}', LINE, 2)
    c += rect(18, 199, 58, 25, GOLD, 2)
    c += text(27, 216, 'WORK ↗', 10, INK, extra=MONO)
    c += text(185, 229, '01', 9, MUTED, extra=MONO)
    c += '</g>'
    svg('portfolio.svg', 1200, 300, 'Portfolio.docx — open my interactive portfolio', c)


def signal_path():
    c = rect(0, 0, 1200, 238, 'url(#grid)')
    c += text(32, 38, 'SHM / FROM SENSOR TO SCREEN', 12, MUTED, extra=f'{MONO} letter-spacing="2"')
    nodes = [('01', 'SENSOR', 'accel / strain'), ('02', 'ESP32', 'filter / pack'),
             ('03', 'TRANSPORT', 'Wi-Fi / MQTT'), ('04', 'STORAGE', 'time series'),
             ('05', 'DASHBOARD', 'charts / alerts')]
    for i, (number, label, detail) in enumerate(nodes):
        x = 32+i*233
        c += rect(x, 73, 204, 120, PAPER, extra=f'stroke="{SAGE}"')
        c += rect(x, 73, 204, 4, GOLD if i == 0 else GREEN)
        c += text(x+15, 102, number, 11, MUTED, extra=MONO)
        c += text(x+15, 137, label, 17, INK, 600, MONO)
        c += text(x+15, 165, detail, 14, MUTED)
        if i < 4:
            c += path(f'M{x+204} 134h26m-6 -5l6 5l-6 5', GREEN, 1.2)
    c += text(32, 220, 'ACQUIRE → PROCESS → TRANSMIT → STORE → UNDERSTAND', 10, MUTED, extra=MONO)
    svg('signal-path.svg', 1200, 238, 'SHM — sensor to dashboard', c)


def buttons():
    for name, label, width in [('portfolio', 'Explore portfolio', 206),
                               ('email', 'Email me', 144), ('linkedin', 'LinkedIn', 144)]:
        primary = name == 'portfolio'
        fg = PAPER if primary else INK
        c = rect(1, 1, width-2, 42, GREEN if primary else PAPER, 4, f'stroke="{GREEN}"')
        c += text(15, 28, label, 14, fg, 600)
        c += path(f'M{width-29} 27l10 -10m-10 0h10v10', fg, 1.3)
        svg(f'button-{name}.svg', width, 44, label, c)


def footer():
    c = rect(0, 0, 1200, 140, GREEN)
    c += wordmark(35, 32, .5, [GOLD, PAPER, PAPER, PAPER])
    c += path('M300 30V110', SAGE)
    c += text(335, 49, 'THANKS FOR STOPPING BY', 11, '#D5DBC9', extra=f'{MONO} letter-spacing="2"')
    c += text(334, 89, 'Adaptability is the engineering skill.', 27, PAPER, 500)
    c += text(1160, 118, 'tengkyuuu / PH', 10, '#D5DBC9', extra=f'{MONO} text-anchor="end"')
    svg('footer.svg', 1200, 140, 'TENG / Adaptability is the engineering skill.', c)


def identity():
    svg('teng-logo.svg', 560, 230, 'TENG / custom wordmark', wordmark(56, 53),
        'TENG in custom geometric lettering, with a muted gold T and forest green E, N, and G.')
    c = rect(0, 0, 1000, 560, 'url(#grid)')
    c += text(36, 43, 'ON MY DESK / A KEYCAP STUDY', 12, MUTED, extra=f'{MONO} letter-spacing="2"')
    c += path('M36 64H964', INK)
    c += keyset(210, 118, 1.14)
    c += text(641, 157, 'THE TENG', 34, INK, 600, 'letter-spacing="-1"')
    c += text(641, 199, 'KEYSET.', 44, INK, 600, 'letter-spacing="-2"')
    c += text(643, 237, 'Four keys. One nickname.', 16, MUTED)
    for i, (label, color) in enumerate([('FOREST', GREEN), ('PAPER', PAPER), ('BRASS', GOLD)]):
        xx = 644+i*101
        c += rect(xx, 278, 76, 48, color, 2, f'stroke="{LINE}"')
        c += text(xx, 346, label, 10, MUTED, extra=MONO)
        c += text(xx, 365, color, 10, MUTED, extra=MONO)
    c += text(643, 414, '01 / Mechanical keycap concept', 12, MUTED, extra=MONO)
    c += text(643, 437, '02 / Custom geometric legends', 12, MUTED, extra=MONO)
    c += path('M36 495H964', INK)
    c += wordmark(36, 513, .17)
    c += text(964, 534, 'OBJECT STUDY / 001', 11, MUTED, extra=f'{MONO} text-anchor="end"')
    svg('keycaps.svg', 1000, 560, 'TENG mechanical keycap concept — forest, paper, and brass', c)


if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    hero()
    hero(mobile=True)
    portfolio()
    signal_path()
    buttons()
    footer()
    identity()
    print('Built 10 self-contained SVG assets. No animation or external dependencies.')

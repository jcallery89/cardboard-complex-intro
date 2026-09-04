"""Build outlined SVG wordmarks for Cardboard Complex from local font files.
Usage: python3 scripts/make-wordmark.py <fontsource dir> <out dir>
Each system: CardBoard (display), Complex (secondary), TRADING CARD COLLECTIBLES (label caps).
The B in CardBoard is filled with a corrugated stripe pattern, a flat nod to the 3D logo."""
import sys, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

FS, OUT = sys.argv[1], sys.argv[2]
os.makedirs(OUT, exist_ok=True)

def font(path):
    return TTFont(path)

def text_paths(f, text, size, x, y, tracking=0):
    """Return (list of (glyphname, path d, advance), total width) at given size, baseline y."""
    upem = f['head'].unitsPerEm; k = size/upem
    cmap = f.getBestCmap(); gs = f.getGlyphSet(); hmtx = f['hmtx']
    kern = {}
    out = []; cx = x
    for ch in text:
        gn = cmap.get(ord(ch)); 
        if gn is None: cx += size*0.3; continue
        pen = SVGPathPen(gs); gs[gn].draw(pen)
        d = pen.getCommands()
        out.append((ch, d, cx, y, k))
        cx += hmtx[gn][0]*k + tracking
    return out, cx - x

def glyph_el(d, cx, y, k, fill, extra=''):
    return f'<path transform="translate({cx:.2f} {y:.2f}) scale({k:.5f} {-k:.5f})" d="{d}" fill="{fill}" {extra}/>'

SYSTEMS = {
 'A-signage':  dict(display=f'{FS}/alfa-slab-one/files/alfa-slab-one-latin-400-normal.woff', second=f'{FS}/lora/files/lora-latin-500-normal.woff', label=f'{FS}/oswald/files/oswald-latin-500-normal.woff', dsize=150, ssize=88, lsize=26, ltrack=4),
 'B-cooper':   dict(display=f'{FS}/fraunces/files/fraunces-latin-900-normal.woff', second=f'{FS}/source-serif-4/files/source-serif-4-latin-500-normal.woff', label=f'{FS}/barlow-condensed/files/barlow-condensed-latin-600-normal.woff', dsize=160, ssize=90, lsize=30, ltrack=5),
 'C-modern':   dict(display=f'{FS}/bricolage-grotesque/files/bricolage-grotesque-latin-800-normal.woff', second=f'{FS}/bricolage-grotesque/files/bricolage-grotesque-latin-300-normal.woff', label=f'{FS}/dm-sans/files/dm-sans-latin-600-normal.woff', dsize=150, ssize=88, lsize=24, ltrack=6),
}
TAN='#C89B62'; TEXT='#F3ECD8'; GOLD='#C9A227'; GROUND='#1B1512'

for name, s in SYSTEMS.items():
    fd, fs2, fl = font(s['display']), font(s['second']), font(s['label'])
    W = 1400
    line1, w1 = text_paths(fd, 'CardBoard', s['dsize'], 0, 0, tracking=-2)
    line2, w2 = text_paths(fs2, 'Complex', s['ssize'], 0, 0)
    line3, w3 = text_paths(fl, 'TRADING CARD COLLECTIBLES', s['lsize'], 0, 0, tracking=s['ltrack'])
    y1, y2, y3 = 190, 300, 350
    parts = []
    for i,(ch,d,cx,y,k) in enumerate(line1):
        x = cx + (W-w1)/2
        if ch == 'B':
            parts.append(glyph_el(d, x, y1, k, 'url(#corrugate)'))
            parts.append(glyph_el(d, x, y1, k, 'none', f'stroke="{TAN}" stroke-width="{2.2/k:.1f}"'))
        else:
            parts.append(glyph_el(d, x, y1, k, TAN))
    for ch,d,cx,y,k in line2: parts.append(glyph_el(d, cx+(W-w2)/2, y2, k, TEXT))
    for ch,d,cx,y,k in line3: parts.append(glyph_el(d, cx+(W-w3)/2, y3, k, GOLD))
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 400" width="{W}" height="400" role="img" aria-label="Cardboard Complex, trading card collectibles">
<defs>
  <pattern id="corrugate" patternUnits="userSpaceOnUse" width="1" height="13" patternTransform="rotate(0)">
    <rect width="1" height="14" fill="{TAN}"/>
    <rect y="7" width="1" height="5" fill="#86603A"/>
    <rect y="12" width="1" height="1.5" fill="#E2C08C"/>
  </pattern>
</defs>
<rect width="{W}" height="400" fill="{GROUND}"/>
{chr(10).join(parts)}
</svg>'''
    open(f'{OUT}/wordmark-{name}.svg','w').write(svg)
    # transparent variant for use on any ground
    open(f'{OUT}/wordmark-{name}-transparent.svg','w').write(svg.replace(f'<rect width="{W}" height="400" fill="{GROUND}"/>\n',''))
    print(name, 'ok', round(w1), round(w2), round(w3))

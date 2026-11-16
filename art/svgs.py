# Hình vẽ trái cà phê MeDili: mặt cắt dọc, các lớp là vùng rời nhau để chọn và làm mờ từng lớp
import math

CX, CY = 280, 318
SK_O = (176, 196)   # mép ngoài vỏ quả
SK_I = (168, 188)   # mép trong vỏ quả
MU = (116, 133)     # mép ngoài lớp nhớt
G = 10              # khoảng từ tâm tới mặt phẳng của hạt
B, A = 82, 108      # bề dày và nửa chiều dài hạt
D1 = 4              # vỏ lụa
D2 = 10             # vỏ thóc, hai vỏ thóc chạm nhau ở giữa


def f(v):
    s = ('%.1f' % v).rstrip('0').rstrip('.')
    return '0' if s == '-0' else s


def ell(cx, cy, rx, ry):
    return f'M{f(cx-rx)} {f(cy)}a{f(rx)} {f(ry)} 0 1 0 {f(2*rx)} 0a{f(rx)} {f(ry)} 0 1 0 {f(-2*rx)} 0Z'


def dsh(side, d, cx=CX, cy=CY, g=G, b=B, a=A):
    """nửa elip: mặt phẳng quay vào tâm, side=-1 hạt trái, +1 hạt phải, d là độ nở ra ngoài"""
    xf = cx + side * (g - d)
    w = b + 2 * d
    aa = a + d
    sweep = 1 if side > 0 else 0
    return f'M{f(xf)} {f(cy-aa)}A{f(w)} {f(aa)} 0 0 {sweep} {f(xf)} {f(cy+aa)}Z'


def on_ell(cx, cy, rx, ry, deg):
    t = math.radians(deg)
    return cx + rx * math.cos(t), cy + ry * math.sin(t)


def fibers(n=30):
    out = []
    for i in range(n):
        deg = i * 360 / n + 4
        x1, y1 = on_ell(CX, CY, MU[0] + 9, MU[1] + 9, deg)
        x2, y2 = on_ell(CX, CY, SK_I[0] - 9, SK_I[1] - 9, deg)
        out.append(f'M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}')
    return ''.join(out)


def arc(cx, cy, rx, ry, a0, a1):
    x0, y0 = on_ell(cx, cy, rx, ry, a0)
    x1, y1 = on_ell(cx, cy, rx, ry, a1)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f'M{f(x0)} {f(y0)}A{f(rx)} {f(ry)} 0 {large} 1 {f(x1)} {f(y1)}'


def cut_line(side):
    x = CX + side * (G + 9)
    return (f'M{f(x)} {f(CY-84)}C{f(x+side*8)} {f(CY-30)} {f(x-side*6)} {f(CY+30)} '
            f'{f(x+side*2)} {f(CY+84)}')


STEM = 'M272 130C271 106 277 84 284 67L297 70C291 87 287 108 288 130Z'
STEM_CAP = '<ellipse cx="291" cy="67" rx="9" ry="5" class="c-stem2" transform="rotate(12 291 67)"/>'


def layers(keep=(1, 2, 3, 4, 5, 6, 7), ids=True, ghost=()):
    """trả về các nhóm lớp. keep: các phần còn vẽ; ghost: phần đã bóc, vẽ nét đứt"""
    L = {}
    L[1] = f'<path class="c-stem rg" d="{STEM}"/>{STEM_CAP}'
    L[2] = (f'<path class="c-skin rg" fill-rule="evenodd" d="{ell(CX,CY,*SK_O)}{ell(CX,CY,*SK_I)}"/>'
            f'<path class="gl" d="{arc(CX,CY,SK_O[0]-4,SK_O[1]-4,196,236)}"/>')
    L[3] = (f'<path class="c-pulp rg" fill-rule="evenodd" d="{ell(CX,CY,*SK_I)}{ell(CX,CY,*MU)}"/>'
            f'<path class="fib" d="{fibers()}"/>')
    L[4] = (f'<path class="c-muc rg" fill-rule="evenodd" d="{ell(CX,CY,*MU)}{dsh(-1,D2)}{dsh(1,D2)}"/>'
            f'<path class="gl2" d="{arc(CX,CY,MU[0]-7,MU[1]-7,200,236)}"/>'
            f'<path class="gl2 t" d="{arc(CX,CY,MU[0]-7,MU[1]-7,244,256)}"/>')
    L[5] = f'<path class="c-parch rg" fill-rule="evenodd" d="{dsh(-1,D2)}{dsh(-1,D1)}{dsh(1,D2)}{dsh(1,D1)}"/>'
    L[6] = f'<path class="c-silver rg" fill-rule="evenodd" d="{dsh(-1,D1)}{dsh(-1,0)}{dsh(1,D1)}{dsh(1,0)}"/>'
    L[7] = (f'<path class="c-bean rg" d="{dsh(-1,0)}{dsh(1,0)}"/>'
            f'<ellipse class="c-bean2" cx="{CX-58}" cy="{CY-36}" rx="12" ry="34"/>'
            f'<ellipse class="c-bean2" cx="{CX+58}" cy="{CY-36}" rx="12" ry="34"/>'
            f'<path class="cut" d="{cut_line(-1)}{cut_line(1)}"/>')
    ghosts = {1: f'<path class="gh" d="{STEM}"/>', 2: f'<path class="gh" d="{ell(CX,CY,*SK_O)}"/>',
              3: '', 4: f'<path class="gh" d="{ell(CX,CY,*MU)}"/>'}
    out = []
    if 2 in keep:
        out.append(f'<g class="bk"><path class="c-skin2 rg" d="{ell(CX+14,CY+8,*SK_O)}"/>'
                   f'<path class="gl3" d="{arc(CX+14,CY+8,SK_O[0]-5,SK_O[1]-5,18,62)}"/></g>')
    for g in ghost:
        out.append(ghosts.get(g, ''))
    for k in (1, 2, 3, 4, 5, 6, 7):
        if k in keep:
            attr = f' id="ly{k}" data-k="{k}"' if ids else ''
            out.append(f'<g class="ly"{attr}>{L[k]}</g>')
    return ''.join(out)


TARGET = {1: (287, 98), 2: (415.5, 199.8), 3: (422, 318), 4: (360.8, 402),
          5: (193.1, 262), 6: (190.2, 352), 7: (238, 410)}
MARK = {1: (356, 70), 2: (512, 168), 3: (520, 318), 4: (520, 444),
        5: (40, 226), 6: (40, 332), 7: (40, 444)}


def markers():
    out = []
    for k in range(1, 8):
        (tx, ty), (mx, my) = TARGET[k], MARK[k]
        dx, dy = tx - mx, ty - my
        L = math.hypot(dx, dy)
        sx, sy = mx + dx / L * 15, my + dy / L * 15
        out.append(f'<path class="ld" data-k="{k}" d="M{f(sx)} {f(sy)}L{f(tx)} {f(ty)}"/>'
                   f'<circle class="dot" data-k="{k}" cx="{f(tx)}" cy="{f(ty)}" r="2.6"/>')
    for k in range(1, 8):
        mx, my = MARK[k]
        out.append(f'<g class="mk" data-k="{k}"><circle class="hit" cx="{mx}" cy="{my}" r="26"/><circle cx="{mx}" cy="{my}" r="15"/>'
                   f'<text x="{mx}" y="{my}">{k}</text></g>')
    return ''.join(out)


def logo(x, y, w):
    h = round(w * 319 / 1000, 1)
    return (f'<image class="lgL" href="assets/logo-mau.png" x="{x}" y="{y}" width="{w}" height="{h}"/>'
            f'<image class="lgD" href="assets/logo-kem.png" x="{x}" y="{y}" width="{w}" height="{h}"/>')


def main_figure():
    return (f'<svg id="fig1" viewBox="0 0 560 604" role="img" aria-labelledby="fig1t">'
            f'<title id="fig1t">Mặt cắt dọc trái Robusta chín: cuống quả, vỏ quả, thịt quả, lớp nhớt, '
            f'vỏ thóc, vỏ lụa và hai hạt nhân úp mặt phẳng vào nhau</title>'
            f'<g id="lys">{layers()}</g><g id="mks">{markers()}</g>{logo(398, 552, 146)}</svg>')


def mini_figure(cls='fc'):
    return (f'<svg class="{cls}" viewBox="86 44 400 494" aria-hidden="true">'
            f'{layers(ids=False)}</svg>')


def trio_figure(kind):
    keep = {'natural': (1, 2, 3, 4, 5, 6, 7), 'honey': (4, 5, 6, 7), 'washed': (5, 6, 7)}[kind]
    ghost = {'natural': (), 'honey': (1, 2), 'washed': (1, 2, 4)}[kind]
    return (f'<svg viewBox="86 44 400 494" aria-hidden="true">'
            f'{layers(keep=keep, ids=False, ghost=ghost)}</svg>')


# ---------- trái một hạt (culi) ----------
def peaberry_section():
    b = (80, 106); s = (b[0] + 4, b[1] + 4); p = (b[0] + 12, b[1] + 12)
    return (f'<path class="c-skin2 rg" d="{ell(CX+14,CY+8,*SK_O)}"/>'
            f'<path class="gl3" d="{arc(CX+14,CY+8,SK_O[0]-5,SK_O[1]-5,18,62)}"/>'
            f'<path class="c-stem rg" d="{STEM}"/>{STEM_CAP}'
            f'<path class="c-skin rg" fill-rule="evenodd" d="{ell(CX,CY,*SK_O)}{ell(CX,CY,*SK_I)}"/>'
            f'<path class="gl" d="{arc(CX,CY,SK_O[0]-4,SK_O[1]-4,196,236)}"/>'
            f'<path class="c-pulp rg" fill-rule="evenodd" d="{ell(CX,CY,*SK_I)}{ell(CX,CY,*MU)}"/>'
            f'<path class="fib" d="{fibers()}"/>'
            f'<path class="c-muc rg" fill-rule="evenodd" d="{ell(CX,CY,*MU)}{ell(CX,CY,*p)}"/>'
            f'<path class="gl2" d="{arc(CX,CY,MU[0]-7,MU[1]-7,200,236)}"/>'
            f'<path class="c-parch rg" fill-rule="evenodd" d="{ell(CX,CY,*p)}{ell(CX,CY,*s)}"/>'
            f'<path class="c-silver rg" fill-rule="evenodd" d="{ell(CX,CY,*s)}{ell(CX,CY,*b)}"/>'
            f'<path class="c-bean rg" d="{ell(CX,CY,*b)}"/>'
            f'<ellipse class="c-bean2" cx="{CX-34}" cy="{CY-40}" rx="14" ry="36"/>'
            f'<path class="cut" d="M{CX+4} {CY-80}C{CX+12} {CY-26} {CX-6} {CY+26} {CX+2} {CY+80}"/>')


def bean_face(cx, cy, rx, ry, s_curve=True, rot=0):
    if s_curve:
        cut = (f'M{f(cx)} {f(cy-ry+7)}C{f(cx+rx*.55)} {f(cy-ry*.35)} {f(cx-rx*.55)} {f(cy+ry*.35)} '
               f'{f(cx)} {f(cy+ry-7)}')
    else:
        cut = f'M{f(cx+rx*.18)} {f(cy-ry+10)}C{f(cx+rx*.32)} {f(cy-ry*.2)} {f(cx+rx*.32)} {f(cy+ry*.2)} {f(cx+rx*.18)} {f(cy+ry-10)}'
    return (f'<g transform="rotate({rot} {f(cx)} {f(cy)})">'
            f'<ellipse class="c-bean rg" cx="{f(cx)}" cy="{f(cy)}" rx="{rx}" ry="{ry}"/>'
            f'<ellipse class="c-bean2" cx="{f(cx-rx*.42)}" cy="{f(cy-ry*.25)}" rx="{f(rx*.2)}" ry="{f(ry*.45)}"/>'
            f'<path class="cut" d="{cut}"/></g>')


def duo_figure(kind):
    if kind == 'two':
        sec = layers(ids=False)
        faces = bean_face(478, 236, 32, 46, True, -8) + bean_face(550, 272, 32, 46, True, 10)
    else:
        sec = peaberry_section()
        faces = bean_face(516, 252, 40, 46, False, 6)
    return (f'<svg viewBox="70 80 530 420" aria-hidden="true">'
            f'<g transform="translate(26 54) scale(.78)">{sec}</g>'
            f'<path class="arr" d="M404 252h30m-9-8 9 8-9 8"/>{faces}</svg>')


FIG_CSS = '''
.c-skin{fill:var(--skin)}.c-skin2{fill:var(--skin2)}.c-pulp{fill:var(--pulp)}.c-muc{fill:var(--muc)}
.c-parch{fill:var(--parch)}.c-silver{fill:var(--silver)}.c-bean{fill:var(--bean)}.c-bean2{fill:var(--bean2);opacity:.75}
.c-stem{fill:var(--stem)}.c-stem2{fill:var(--stem2);stroke:var(--ol);stroke-width:1}
.rg{stroke:var(--ol);stroke-width:1.15;stroke-linejoin:round}
.fib{stroke:var(--pulp2);stroke-width:1;opacity:.5;fill:none;stroke-linecap:round;pointer-events:none}
.gl{stroke:#F2A48D;stroke-width:2.4;opacity:.55;fill:none;stroke-linecap:round;pointer-events:none}
.gl2{stroke:#FFFFFF;stroke-width:3.2;opacity:.75;fill:none;stroke-linecap:round;pointer-events:none}.gl2.t{stroke-width:2.4}
.gl3{stroke:#C4513A;stroke-width:4;opacity:.6;fill:none;stroke-linecap:round;pointer-events:none}
.cut{stroke:var(--cut);stroke-width:2;fill:none;stroke-linecap:round;pointer-events:none}
.gh{fill:none;stroke:var(--muted);stroke-width:1.4;stroke-dasharray:6 6;opacity:.75}
.arr{stroke:var(--muted);stroke-width:2;fill:none;stroke-linecap:round;stroke-linejoin:round}
.fcap{font:500 17px var(--body);fill:var(--muted)}
'''

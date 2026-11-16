# Dựng trang "Giải phẫu trái Cà Sẻ" và gắn vào site MeDili
import os, re, json, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import svgs as S

LIVE = os.path.join(HERE, '..', 'site-live')
OUT = os.path.join(HERE, '..', 'site-new')
os.makedirs(OUT, exist_ok=True)
rd = lambda f: open(os.path.join(LIVE, f), encoding='utf8').read()

PAGE = 'trai-ca-phe.html'
NAVLBL = 'Cấu tạo trái'

# ---------------- nội dung ----------------
PARTS = [
 dict(k=1, n='Cuống quả', en='stem', c='var(--stem)',
  role='Đoạn cuống ngắn giữ trái trên đốt cành. Trái chín đủ thì rời cuống dễ hơn trái xanh.',
  out='Khi hái, rồi tuyển trái',
  long='Trái cà phê mọc thành chùm sát đốt cành, mỗi trái bám bằng một cuống rất ngắn. Trên cùng một chùm thường có trái chín, trái ương và trái xanh, nên hái tốt là hái từng trái chín. Tuốt cả chùm thì trái xanh lẫn vào mẻ, ly cà phê sẽ chát và hăng.',
  medili='Lịch vườn MeDili chia mùa hái làm 3 đợt, từ tháng 11 đến đầu tháng 1, trái xanh tối đa 5 % mỗi mẻ.'),
 dict(k=2, n='Vỏ quả', en='exocarp', c='var(--skin)',
  role='Lớp da mỏng ngoài cùng, đổi từ xanh sang đỏ khi chín, giữ nước và che chắn phần thịt bên trong.',
  out='Xát tươi với Washed, Honey. Xay vỏ khô với Natural.',
  long='Lớp ngoài cùng mỏng và dai, chuyển từ xanh sang vàng rồi đỏ khi chín. Vỏ giữ nước cho thịt quả và chắn côn trùng, nấm mốc. Khi phơi nguyên trái, vỏ khô lại thành lớp sẫm màu, giòn, bao kín hạt bên trong.',
  medili='Màu vỏ là thước chọn trái đầu tiên. Ở trạm tuyển nổi, trái lép nổi lên mặt nước và được vớt bỏ.'),
 dict(k=3, n='Thịt quả', en='mesocarp, pulp', c='var(--pulp)',
  role='Phần thịt ngọt, mọng nước ngay dưới vỏ, chứa nhiều đường và nước.',
  out='Xát tươi với Washed, Honey. Xay vỏ khô với Natural.',
  long='Ngay dưới vỏ là phần thịt ngọt, mọng nước. Vỏ và thịt quả nặng khoảng 4 phần 10 trái tươi. Theo mô hình của MeDili, 95 kg trái sau tuyển còn 57 kg sau khi xát. Máy xát ép trái qua khe hẹp, vỏ và thịt bung ra, hạt còn lớp nhớt trượt qua.',
  medili='Vỏ và thịt quả sau xát về nhà ủ, thành phân hữu cơ bón lại cho vườn.'),
 dict(k=4, n='Lớp nhớt', en='mucilage', c='var(--muc)',
  role='Lớp keo trong, trơn, giàu pectin và đường, bám chặt quanh vỏ thóc.',
  out='Lên men rồi rửa với Washed. Honey và Natural để lớp nhớt khô lại trên hạt.',
  long='Bám quanh vỏ thóc là lớp keo trong, trơn tay, giàu pectin và đường. Nước không rửa trôi được lớp này. Trong bồn lên men, men và vi sinh ăn đường, phân giải pectin, sinh ra axit cùng nhiều hợp chất hương. Giữ lại nhiều hay ít lớp nhớt là chỗ khác nhau giữa Washed, Honey và Natural.',
  medili='Dòng Premium lên men Honey hoặc Washed để mở hương trái cây. Dòng Classic là Robusta sơ chế Natural.'),
 dict(k=5, n='Vỏ thóc', en='parchment', c='var(--parch)',
  role='Lớp vỏ cứng, mỏng như giấy, bọc riêng từng hạt.',
  out='Xay xát, trước khi bán nhân hoặc đem rang',
  long='Mỗi hạt nằm trong một lớp vỏ cứng, mỏng như giấy, màu vàng rơm. Lớp này giữ hạt nguyên vẹn khi phơi và khi nằm kho. Hạt còn nguyên lớp vỏ này gọi là cà phê thóc. Khi xay xát, vỏ thóc vỡ ra và được quạt thổi đi.',
  medili='Trạm sàng gió trước máy rang hút nốt mảnh vỏ thóc và bụi còn sót sang cyclone.'),
 dict(k=6, n='Vỏ lụa', en='silverskin', c='var(--silver)',
  role='Màng bạc rất mỏng ôm sát mặt hạt, lẩn cả vào rãnh giữa.',
  out='Một ít khi xay xát, phần lớn khi rang',
  long='Sát mặt hạt còn một màng bạc rất mỏng, lẩn cả vào rãnh giữa. Một ít bong ra khi xay xát hay đánh bóng, phần lớn theo hạt vào máy rang. Khi hạt nở ra trong lồng rang, vỏ lụa bong thành những vảy nhẹ.',
  medili='Quạt của máy rang kéo khói và vỏ lụa sang cyclone, giữ mẻ rang sạch.'),
 dict(k=7, n='Hạt nhân', en='green bean', c='var(--bean)',
  role='Phần lõi đem rang, xay và pha. Thường mỗi trái có hai hạt úp mặt phẳng vào nhau.',
  out='Rang, xay, pha',
  long='Phần lõi là hạt giống, cứng, màu xám vàng khi còn sống. Thường mỗi trái có hai hạt úp mặt phẳng vào nhau, mỗi mặt phẳng có một đường rãnh giữa. Nhân xanh chứa đường, axit, protein và caffeine. Nhiệt khi rang biến chúng thành hàng trăm hợp chất tạo nên hương vị trong tách.',
  medili='Rang tại xưởng Di Linh, 8 cấp độ từ Cinnamon đến Italian.'),
]

# mô hình khối lượng lấy từ trang Lên men men bia (RATIO, lọc 95 %, rang 84 %)
MS = {'washed': [1, .95, .57, .53, .45, .225, .18], 'honey': [1, .95, .57, .55, .55, .25, .18],
      'natural': [1, .95, .95, .93, .93, .33, .18]}
DRY = {'washed': 'thóc khô', 'honey': 'thóc khô còn lớp mật', 'natural': 'trái khô'}
STEPS = ['Trái chín', 'Tuyển nổi', 'Xát tươi', 'Lên men', 'Rửa', 'Phơi sấy', 'Xay xát', 'Lọc hạt lỗi', 'Rang']


def fm(n):
    r = round(n, 1)
    return str(int(r)) if abs(r - round(r)) < 1e-9 else ('%.1f' % r).replace('.', ',')


def note(m, i, d):
    D = fm(d) + ' kg'
    if i == 0: return ('hái về xưởng trong ngày', '', [])
    if i == 1: return (f'bỏ {D} trái lép', 'var(--skin2)', [])
    if i == 2: return ('không xát, giữ nguyên trái', '', []) if m == 'natural' else (f'bỏ {D} vỏ quả, thịt quả', 'var(--skin)', [2, 3])
    if i == 3: return (f'bỏ {D} nhớt, nước, CO₂' if m == 'washed' else f'bỏ {D} nước, CO₂', 'var(--muc)', [3, 4] if m == 'natural' else [4])
    if i == 4: return (f'bỏ {D} nhớt và nước rửa', 'var(--muc)', [4]) if m == 'washed' else ('không rửa, giữ lớp nhớt' if m == 'honey' else 'không rửa', '', [])
    if i == 5: return (f'bay hơi {D} nước, còn {DRY[m]} 11 % ẩm', 'var(--water)', [])
    if i == 6:
        o = {'washed': f'bỏ {D} vỏ thóc', 'honey': f'bỏ {D} vỏ thóc và lớp mật khô', 'natural': f'bỏ {D} vỏ khô gồm vỏ quả, thịt quả, nhớt, vỏ thóc'}[m]
        return (o, 'var(--husk)' if m == 'natural' else 'var(--parch)', {'washed': [5], 'honey': [4, 5], 'natural': [2, 3, 4, 5]}[m])
    if i == 7: return (f'bỏ {D} hạt lỗi', 'var(--bean)', [7])
    return (f'hao {D} nước và vỏ lụa khi rang', 'var(--chaff)', [6])


def rows(m):
    v = [x * 100 for x in MS[m]]
    g = v[6]; v += [g * .95, g * .95 * .84]
    out = []
    for i, n in enumerate(STEPS):
        p = v[i - 1] if i else v[0]
        o, c, ly = note(m, i, p - v[i])
        out.append(dict(i=i, n=n, v=v[i], p=p, o=o, c=c, ly=ly))
    return out


def rows_html(m):
    h = []
    for r in rows(m):
        prod = ' prod' if r['i'] >= 7 else ''
        u = f'left:{r["v"]:.2f}%;width:{r["p"]-r["v"]:.2f}%;--c:{r["c"] or "transparent"}'
        em = f'<em style="--c:{r["c"]}"></em>' if r['c'] else ''
        h.append(f'<div class="mrow{prod}" data-i="{r["i"]}" role="button" tabindex="0"><span>{r["n"]}</span>'
                 f'<span class="mbar"><i style="width:{r["v"]:.2f}%"></i><u style="{u}"></u></span>'
                 f'<b>{fm(r["v"])} kg</b><small>{em}{r["o"]}</small></div>')
    roast = rows(m)[-1]['v']
    bags = round(roast / .25); cups = round(roast / .018 / 100) * 100
    h.append(f'<div class="mrow prod fin"><span>Thành phẩm</span><span></span><b>{bags} gói</b>'
             f'<small>gói 250 g, khoảng {cups} ly 18 g</small></div>')
    return ''.join(h)


def parts_buttons():
    return ''.join(f'<button type="button" data-k="{p["k"]}" aria-pressed="false"><i style="--c:{p["c"]}"></i>'
                   f'<b>{p["k"]}</b><span>{p["n"]}<small>{p["en"]}</small></span></button>' for p in PARTS)


def parts_article():
    li = []
    for p in PARTS:
        li.append(f'<li data-k="{p["k"]}"><span class="n">{p["k"]}</span><div><h3><i class="swc" style="--c:{p["c"]}"></i>{p["n"]} <small>{p["en"]}</small></h3>'
                  f'<p>{p["long"]}</p><button type="button" class="see" data-k="{p["k"]}">Xem trên Hình 1</button></div>'
                  f'<div class="x"><span class="lbl">Ở MeDili</span><p>{p["medili"]}</p></div></li>')
    return ''.join(li)


TRIO = [
 ('natural', 'Natural', 'Phơi nguyên trái', 'Vỏ quả, thịt quả và lớp nhớt khô lại quanh hạt, đến khi xay xát mới bóc. Ly thường dày thân, ngọt, có hương trái chín.'),
 ('honey', 'Honey', 'Bỏ vỏ và thịt, giữ lớp nhớt', 'Lớp nhớt khô thành màng dính như mật quanh vỏ thóc. Ly thường ngọt, tròn vị.'),
 ('washed', 'Washed', 'Lên men, rửa sạch lớp nhớt', 'Khi phơi chỉ còn vỏ thóc bọc hạt. Ly thường sạch vị, sáng, rõ axit.'),
]


def trio_html():
    return ''.join(f'<figure>{S.trio_figure(k)}<figcaption><b>{t}</b><span>{s}</span><p>{d}</p>'
                   f'<button type="button" class="see" data-m="{k}">Xem 100 kg trái theo cách này</button></figcaption></figure>'
                   for k, t, s, d in TRIO)


NAV_RE = re.compile(r'(<a href="vuon\.html"[^>]*>Vườn</a>)')


def nav(html, current=False):
    if 'href="' + PAGE + '"' in html:
        return html
    link = f'<a href="{PAGE}" class=on aria-current=page>{NAVLBL}</a>' if current else f'<a href="{PAGE}">{NAVLBL}</a>'
    html, n = NAV_RE.subn(r'\1' + link, html, count=1)
    assert n == 1
    return html


# ---------------- trang mới ----------------
suc = rd('suc-khoe.html')
SHARED = re.findall(r'<style>(.*?)</style>', suc, flags=re.S)[1]
FONTS = re.search(r'<link rel="preconnect" href="https://fonts.googleapis.com">\s*<link rel="preconnect"[^>]*>\s*<link rel="stylesheet"[^>]*>', suc).group(0)
MNAV = re.search(r'<div class="mnav">.*?</div></div>', suc, flags=re.S).group(0)
MNAV = MNAV.replace(' class=on aria-current=page', '')
MNAV = nav(MNAV, current=True)

PAGE_CSS = '''
/* Trang Giải phẫu: hình mặt cắt và chú giải ở khung trái, sổ khối lượng ở khung phải, bài bảy phần và hai mục so sánh bên dưới. */
:root{
  --moss:#8D4E22;--good:#8D4E22;
  --skin:#B33A24;--skin2:#7A2414;--pulp:#E2A55E;--pulp2:#C4873C;--muc:#F7EBD0;--parch:#E4C891;--silver:#F8F3E9;
  --bean:#B49A63;--bean2:#CDB683;--cut:#6A4E30;--stem:#7A5233;--stem2:#5E3E25;--husk:#7E3A22;--chaff:#D9AA6E;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--moss:#E2A774;--good:#E2A774}}
:root[data-theme="dark"]{--moss:#E2A774;--good:#E2A774}
a{color:var(--accent)}
.f1{display:grid;grid-template-columns:minmax(0,500px) minmax(0,1fr);gap:16px 30px;align-items:start;margin-top:10px}
#fig1{display:block;width:100%;height:auto;margin-inline:auto;-webkit-tap-highlight-color:transparent}
@media (max-width:900px){.f1{grid-template-columns:minmax(0,1fr)}#fig1{max-width:500px}}
#fig1 .ly,#fig1 .bk{transition:opacity .28s}
#fig1 .ly{cursor:pointer}
#fig1.sel .ly:not(.on),#fig1.sel .bk:not(.on){opacity:.16}
#fig1 .ly.on .rg{stroke:var(--accent);stroke-width:2.8}
#fig1 .ld{stroke:var(--ink);stroke-width:1;opacity:.5;fill:none;transition:opacity .2s}
#fig1 .dot{fill:var(--ink);opacity:.7}
#fig1 .mk{cursor:pointer}
#fig1 .mk circle{fill:var(--panel);stroke:var(--ink);stroke-width:1.3}
#fig1 .mk .hit{fill:transparent;stroke:none}
#fig1 .mk text{font:800 19px var(--display);fill:var(--ink);text-anchor:middle;dominant-baseline:central;pointer-events:none}
#fig1 .mk.on circle:not(.hit){fill:var(--accent);stroke:var(--accent)}#fig1 .mk.on text{fill:var(--on-accent)}
#fig1 .ld.on{stroke:var(--accent);stroke-width:2;opacity:1}#fig1 .dot.on{fill:var(--accent);opacity:1}
#fig1.sel .ld:not(.on),#fig1.sel .dot:not(.on){opacity:.15}
#fig1 .lgD{display:none}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) #fig1 .lgL{display:none}:root:not([data-theme="light"]) #fig1 .lgD{display:inline}}
:root[data-theme="dark"] #fig1 .lgL{display:none}:root[data-theme="dark"] #fig1 .lgD{display:inline}
.parts{display:grid;gap:2px;align-content:start}
.parts button{display:grid;grid-template-columns:14px 24px minmax(0,1fr);gap:10px;align-items:center;text-align:left;width:100%;font:600 .98rem/1.25 var(--body);color:var(--ink);background:transparent;border:1px solid transparent;border-bottom-color:var(--rule);border-radius:10px;padding:9px 10px;cursor:pointer}
.parts button i,.swc,.mrow small em{display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--c);box-shadow:inset 0 0 0 1px var(--ol)}
.parts button b{font:800 1.3rem/1 var(--display);color:var(--accent)}
.parts button small{display:block;font:500 .78rem/1.3 var(--body);color:var(--muted)}
.parts button[aria-pressed="true"]{background:var(--tint);border-color:var(--accent)}
.parts button:hover{border-color:var(--rule)}
@media (max-width:900px){.parts{grid-template-columns:repeat(auto-fill,minmax(146px,1fr));gap:6px}.parts button{border-color:var(--rule);grid-template-columns:12px 16px minmax(0,1fr);gap:8px;padding:8px;font-size:.92rem}.parts button b{font-size:1.15rem}}
.f1r{display:grid;gap:12px;min-width:0}
#detail{margin-top:0}
#detail p{margin:8px 0 0}
#detail .dn{flex-basis:44px}
#detail dl.kv{margin-top:10px}
.mtog{margin-top:6px}
.msum{margin:10px 0 4px;font-size:.92rem;line-height:1.5}
.msum b{color:var(--accent)}
#mass .mrow{grid-template-columns:100px minmax(0,1fr) 78px;cursor:pointer;padding-inline:4px;border-radius:6px}
#mass .mrow:hover,#mass .mrow.on{background:var(--tint)}
#mass .mrow.fin{cursor:default;background:none}
#mass .mrow:focus-visible{outline:3px solid var(--moss);outline-offset:1px}
.mbar{position:relative;overflow:hidden}
.mbar i{transition:width .5s cubic-bezier(.3,.7,.2,1)}
.mbar u{position:absolute;top:0;bottom:0;background:var(--c);box-shadow:inset 0 0 0 1px rgba(42,27,22,.25);transition:left .5s cubic-bezier(.3,.7,.2,1),width .5s cubic-bezier(.3,.7,.2,1)}
.mrow small em{width:10px;height:10px;margin-right:6px;vertical-align:-1px}
.see{font:600 .84rem var(--body);color:var(--accent);background:none;border:0;padding:6px 0 0;cursor:pointer;text-decoration:underline;text-underline-offset:3px;text-align:left}
#bay-phan .sop li{grid-template-columns:44px minmax(0,1.7fr) minmax(0,1fr);cursor:default}
#bay-phan .sop li.on{background:var(--tint);border-radius:10px}
#bay-phan .sop h3{display:flex;flex-wrap:wrap;align-items:center;gap:4px 8px;font-size:1.06rem}
#bay-phan .sop h3 small{font-weight:500;color:var(--muted);font-size:.8rem}
#bay-phan .sop p{max-width:68ch}
@media (max-width:820px){#bay-phan .sop li{grid-template-columns:36px minmax(0,1fr)}}
.trio{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px 26px;margin-top:8px}
.trio figure{margin:0;display:grid;gap:10px;align-content:start;min-width:0}
.trio svg{display:block;width:100%;max-width:240px;height:auto;margin-inline:auto}
.trio figcaption{min-width:0}
.trio figcaption b{font:800 1.5rem/1.1 var(--display);display:block}
.trio figcaption span{display:block;font-weight:600;color:var(--accent);font-size:.92rem;margin-top:2px}
.trio figcaption p{margin:6px 0 0;font-size:.92rem}
@media (max-width:680px){.trio{grid-template-columns:minmax(0,1fr)}.trio figure{grid-template-columns:112px minmax(0,1fr);align-items:center;gap:14px}}
.mnote{background:var(--tint);border-radius:12px;padding:12px 16px;margin:16px 0 0;max-width:none}
.culi{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:18px 30px;align-items:center}
.culi h2{font:800 2.05rem/1.15 var(--display);margin:0 0 6px}
.culi p{margin:0 0 10px;max-width:62ch}
.duo{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px}
.duo figure{margin:0;min-width:0}
.duo svg{display:block;width:100%;height:auto}
.duo figcaption{font-weight:600;font-size:.9rem;text-align:center;color:var(--muted)}
.duo figcaption b{display:block;color:var(--ink);font-size:.98rem}
@media (max-width:820px){.culi{grid-template-columns:minmax(0,1fr)}}
.journey{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:12px}
.journey a{background:var(--panel);border:1px solid var(--rule);border-radius:14px;overflow:hidden;color:var(--ink);text-decoration:none;display:flex;flex-direction:column}
.journey img{display:block;width:100%;height:auto;aspect-ratio:3/2;object-fit:cover}
.journey b{font:800 1.3rem var(--display);padding:10px 14px 0}
.journey span{padding:2px 14px 14px;color:var(--muted);font-size:.9rem}
@media (max-width:820px){.journey{grid-template-columns:minmax(0,1fr)}.journey a{display:grid;grid-template-columns:120px minmax(0,1fr);grid-template-rows:auto 1fr}.journey img{grid-row:1/3;height:100%;min-height:104px;aspect-ratio:auto}.journey b,.journey span{grid-column:2}.journey b{padding:12px 12px 0}.journey span{padding:2px 12px 12px}}
@media (prefers-reduced-motion:reduce){#fig1 .ly,#fig1 .bk,#fig1 .ld,.mbar i,.mbar u{transition:none}}
''' + S.FIG_CSS

PARTS_JS = json.dumps([{k: p[k] for k in ('k', 'n', 'en', 'c', 'role', 'out')} for p in PARTS], ensure_ascii=False)

JS = r'''
const $=id=>document.getElementById(id);
const still=matchMedia('(prefers-reduced-motion: reduce)').matches;
const P=__PARTS__;
const MS={washed:[1,.95,.57,.53,.45,.225,.18],honey:[1,.95,.57,.55,.55,.25,.18],natural:[1,.95,.95,.93,.93,.33,.18]};
const DRY={washed:'thóc khô',honey:'thóc khô còn lớp mật',natural:'trái khô'};
const MN={washed:'Washed',honey:'Honey',natural:'Natural'};
const STEPS=['Trái chín','Tuyển nổi','Xát tươi','Lên men','Rửa','Phơi sấy','Xay xát','Lọc hạt lỗi','Rang'];
const fm=n=>{const r=Math.round(n*10)/10;return Number.isInteger(r)?String(r):r.toFixed(1).replace('.',',')};
function note(m,i,d){const D=fm(d)+' kg';
 switch(i){
  case 0:return ['hái về xưởng trong ngày','',[]];
  case 1:return [`bỏ ${D} trái lép`,'var(--skin2)',[]];
  case 2:return m==='natural'?['không xát, giữ nguyên trái','',[]]:[`bỏ ${D} vỏ quả, thịt quả`,'var(--skin)',[2,3]];
  case 3:return [m==='washed'?`bỏ ${D} nhớt, nước, CO₂`:`bỏ ${D} nước, CO₂`,'var(--muc)',m==='natural'?[3,4]:[4]];
  case 4:return m==='washed'?[`bỏ ${D} nhớt và nước rửa`,'var(--muc)',[4]]:[m==='honey'?'không rửa, giữ lớp nhớt':'không rửa','',[]];
  case 5:return [`bay hơi ${D} nước, còn ${DRY[m]} 11 % ẩm`,'var(--water)',[]];
  case 6:return [{washed:`bỏ ${D} vỏ thóc`,honey:`bỏ ${D} vỏ thóc và lớp mật khô`,natural:`bỏ ${D} vỏ khô gồm vỏ quả, thịt quả, nhớt, vỏ thóc`}[m],m==='natural'?'var(--husk)':'var(--parch)',{washed:[5],honey:[4,5],natural:[2,3,4,5]}[m]];
  case 7:return [`bỏ ${D} hạt lỗi`,'var(--bean)',[7]];
  default:return [`hao ${D} nước và vỏ lụa khi rang`,'var(--chaff)',[6]];
 }}
function rows(m){const v=MS[m].map(x=>x*100),g=v[6];v.push(g*.95,g*.95*.84);
 return STEPS.map((n,i)=>{const p=i?v[i-1]:v[0],[o,c,ly]=note(m,i,p-v[i]);return {i,n,v:v[i],p,o,c,ly}})}
let method='washed',sel=new Set(),src=null,step=null,timer=null;
const fig=$('fig1'),lys=$('lys');
function paint(){
 fig.classList.toggle('sel',sel.size>0);
 if(!sel.size)[1,2,3,4,5,6,7].forEach(k=>lys.appendChild($('ly'+k)));
 fig.querySelectorAll('.ly').forEach(g=>{const k=+g.dataset.k,on=sel.has(k);g.classList.toggle('on',on);if(on&&k>1)lys.appendChild(g)});
 fig.querySelector('.bk').classList.toggle('on',sel.has(2));
 fig.querySelectorAll('.mk,.ld,.dot').forEach(e=>e.classList.toggle('on',sel.has(+e.dataset.k)));
 document.querySelectorAll('#parts button').forEach(b=>b.setAttribute('aria-pressed',String(sel.has(+b.dataset.k))));
 document.querySelectorAll('#bay-phan li').forEach(l=>l.classList.toggle('on',src==='part'&&sel.has(+l.dataset.k)));
 document.querySelectorAll('#mass .mrow').forEach(r=>r.classList.toggle('on',src==='step'&&+r.dataset.i===step));
 detail();
}
function detail(){
 const d=$('detail');
 if(src==='part'&&sel.size===1){const p=P[[...sel][0]-1];
  d.innerHTML=`<div class="dh"><span class="dn">${p.k}</span><div><h2>${p.n}</h2><small>${p.en}</small></div></div><p>${p.role}</p><dl class="kv"><dt>Tách ra ở bước</dt><dd>${p.out}</dd></dl>`;return}
 if(src==='step'){const r=rows(method)[step],names=r.ly.map(k=>P[k-1].n.toLowerCase()).join(', ');
  d.innerHTML=`<div class="dh"><span class="dn">${step}</span><div><h2>${r.n}</h2><small>Sơ chế ${MN[method]}, Hình 2</small></div></div><p>Từ ${fm(r.p)} kg còn ${fm(r.v)} kg: ${r.o}.</p>${names?`<dl class="kv"><dt>Lớp bị tách</dt><dd>${names}</dd></dl>`:''}`;return}
 d.innerHTML=`<div class="dh"><span class="dn">7</span><div><h2>Bảy phần của một trái</h2><small>Từ ngoài vào trong</small></div></div><p>Bấm số trên hình hoặc tên từng phần để xem nó là gì và được tách ra ở bước nào. Năm lớp từ vỏ quả đến vỏ lụa đều bong khỏi hạt trước hoặc trong lúc rang.</p>`;
}
function pick(k){stop();if(src==='part'&&sel.size===1&&sel.has(k)){sel=new Set();src=null}else{sel=new Set([k]);src='part'}paint()}
function stop(){if(timer){clearInterval(timer);timer=null;$('run').textContent='Xem lần lượt';$('run').setAttribute('aria-pressed','false')}}
$('run').onclick=()=>{if(timer){stop();return}let k=1;sel=new Set([1]);src='part';paint();$('run').textContent='Dừng';$('run').setAttribute('aria-pressed','true');
 timer=setInterval(()=>{k++;if(k>7){stop();sel=new Set();src=null;paint();return}sel=new Set([k]);src='part';paint()},still?2600:1800)};
fig.addEventListener('click',e=>{const g=e.target.closest('.ly,.mk');if(g)pick(+g.dataset.k)});
$('parts').addEventListener('click',e=>{const b=e.target.closest('button');if(b)pick(+b.dataset.k)});
document.querySelectorAll('#bay-phan .see').forEach(b=>b.onclick=()=>{stop();sel=new Set([+b.dataset.k]);src='part';paint();const r=fig.getBoundingClientRect();if(r.bottom<80||r.top>innerHeight-120)fig.scrollIntoView({behavior:still?'auto':'smooth',block:'center'})});
function renderMass(){
 const R=rows(method),box=$('mass');
 R.forEach(r=>{const row=box.querySelector(`.mrow[data-i="${r.i}"]`);row.querySelector('i').style.width=r.v.toFixed(2)+'%';const u=row.querySelector('u');u.style.left=r.v.toFixed(2)+'%';u.style.width=(r.p-r.v).toFixed(2)+'%';u.style.setProperty('--c',r.c||'transparent');
  row.querySelector('b').textContent=fm(r.v)+' kg';row.querySelector('small').innerHTML=(r.c?`<em style="--c:${r.c}"></em>`:'')+r.o});
 document.querySelectorAll('#mtog .pill').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.m===method)));
 if(src==='step'){sel=new Set(R[step].ly);paint()}
}
$('mtog').addEventListener('click',e=>{const b=e.target.closest('.pill');if(!b)return;method=b.dataset.m;renderMass()});
function pickStep(i){stop();if(src==='step'&&step===i){src=null;step=null;sel=new Set()}else{src='step';step=i;sel=new Set(rows(method)[i].ly)}paint()}
$('mass').addEventListener('click',e=>{const r=e.target.closest('.mrow[data-i]');if(r)pickStep(+r.dataset.i)});
$('mass').addEventListener('keydown',e=>{const r=e.target.closest('.mrow[data-i]');if(r&&(e.key==='Enter'||e.key===' ')){e.preventDefault();pickStep(+r.dataset.i)}});
document.querySelectorAll('.trio .see').forEach(b=>b.onclick=()=>{method=b.dataset.m;renderMass();$('c2').scrollIntoView({behavior:still?'auto':'smooth',block:'start'})});
const copyTo=async(t,msg,srcEl,done)=>{try{await navigator.clipboard.writeText(t);$(msg).textContent=done}catch(e){const r=document.createRange();r.selectNodeContents($(srcEl));const s=getSelection();s.removeAllRanges();s.addRange(r);$(msg).textContent='Đã bôi đen, hãy sao chép bằng tay.'}};
$('copyZalo').onclick=()=>copyTo('0966770788','zaloMsg','zaloNo','Đã sao chép số Zalo.');
paint();
'''.replace('__PARTS__', PARTS_JS)

BODY = f'''{MNAV}

<div class="wrap">
<header>
  <span class="lgw"><img class="lgL" src="assets/logo-mau.png" alt="MeDili Café Di Linh" width="240" height="77"><img class="lgD" src="assets/logo-kem.png" alt="MeDili Café Di Linh" width="240" height="77"></span><div class="brandbar"><span>Mê vị Di Linh</span></div>
  <h1>Giải Phẫu <em>Trái Cà Sẻ</em></h1>
  <p>Một trái cà phê chín có năm lớp bọc quanh hạt nhân, thêm phần cuống nối trái với cành. Bấm từng phần trên hình để xem nó là gì và được tách ra ở bước nào. Đổi cách sơ chế ở Hình 2 để xem 100 kg trái chín còn lại bao nhiêu.</p>
</header>
<div class="bench">
  <div class="card" id="c1">
    <div class="fighead"><div><b>Hình 1</b> <span>Mặt cắt dọc trái Robusta chín</span></div><button class="btn small" type="button" id="run" aria-pressed="false">Xem lần lượt</button></div>
    <div class="f1">
      {S.main_figure()}
      <div class="f1r">
        <div class="parts" id="parts" role="group" aria-label="Chọn một phần của trái">{parts_buttons()}</div>
        <div id="detail" aria-live="polite"></div>
      </div>
    </div>
  </div>
  <aside class="card ctl" id="c2">
    <div class="fighead"><div><b>Hình 2</b> <span>100 kg trái chín còn lại gì</span></div></div>
    <div class="row mtog" id="mtog" role="group" aria-label="Cách sơ chế"><button class="pill" type="button" data-m="washed" aria-pressed="true">Washed</button><button class="pill" type="button" data-m="honey" aria-pressed="false">Honey</button><button class="pill" type="button" data-m="natural" aria-pressed="false">Natural</button></div>
    <p class="msum">100 kg trái chín còn khoảng <b>18 kg nhân xanh</b> và <b>14,4 kg cà phê rang</b>, đủ khoảng 57 gói 250 g. Ba cách cho cùng lượng nhân, khác nhau ở lớp bị bỏ trước khi phơi.</p>
    <div id="mass">{rows_html('washed')}</div>
    <p class="src">Ước tính theo mô hình ở trang <a href="len-men-men-bia.html">Lên men men bia</a> của MeDili. Số thật tuỳ độ chín, độ ẩm và từng lô. Bấm một dòng để xem lớp bị tách trên Hình 1.</p>
  </aside>
</div>

<section class="card" id="bay-phan">
  <h2>Bảy phần, từ ngoài vào trong</h2>
  <p class="lead">Vỏ quả, thịt quả, lớp nhớt, vỏ thóc và vỏ lụa là năm lớp bọc quanh hạt nhân. Cùng với cuống quả, đó là bảy phần đánh số trên Hình 1.</p>
  <ol class="sop">{parts_article()}</ol>
</section>

<section class="card" id="so-che">
  <h2>Natural, Honey, Washed khác nhau ở lớp nào</h2>
  <p class="lead">Cả ba cách bắt đầu từ cùng một trái chín. Khác nhau ở chỗ lớp nào còn bám quanh hạt khi đem phơi. Nét đứt là phần đã bóc đi.</p>
  <div class="trio">{trio_html()}</div>
  <p class="mnote">Ở MeDili, dòng Classic là Robusta sơ chế Natural. Dòng Premium lên men Honey hoặc Washed để mở hương trái cây. Xem từng trạm ở <a href="len-men-men-bia.html">Lên men men bia</a> và <a href="len-men-trai-cay.html">Lên men trái cây</a>.</p>
</section>

<section class="card culi" id="culi">
  <div class="duo">
    <figure>{S.duo_figure('two')}<figcaption><b>Trái hai hạt</b>hai hạt dẹt, mặt phẳng có rãnh giữa</figcaption></figure>
    <figure>{S.duo_figure('one')}<figcaption><b>Trái một hạt</b>một hạt tròn, gọi là culi</figcaption></figure>
  </div>
  <div>
    <h2>Hai hạt hay một hạt</h2>
    <p>Thường mỗi trái nuôi hai hạt úp mặt phẳng vào nhau, nên hạt cà phê có một mặt phẳng với đường rãnh giữa. Khoảng 5–10 % trái chỉ nuôi một hạt. Hạt ấy lớn lên chiếm cả khoang, tròn đều, gọi là cà phê culi.</p>
    <p>Hạt tròn lăn trong lồng rang khác hạt dẹt, nên culi thường được sàng riêng để rang một mẻ. MeDili chọn culi riêng theo từng lô.</p>
    <a class="btn main" href="mua-hang.html">Xem Cà phê Culi</a>
  </div>
</section>

<section id="doc-tiep">
  <h2>Đọc tiếp hành trình một hạt</h2>
  <div class="journey">
    <a href="vuon.html"><img src="assets/vuon.jpg" alt="" loading="lazy" width="900" height="606"><b>Vườn 12 tháng</b><span>Chăm Robusta Cà Sẻ hướng tự nhiên, từ bón phân đến thu hái.</span></a>
    <a href="len-men-men-bia.html"><img src="assets/men-bia.jpg" alt="" loading="lazy" width="900" height="606"><b>Lên men men bia</b><span>Cỗ máy 7 trạm với Washed, Honey và Natural.</span></a>
    <a href="rang.html"><img src="assets/rang.jpg" alt="" loading="lazy" width="900" height="606"><b>Sàng tuyển và rang</b><span>8 cấp độ rang, đường nhiệt và phiếu rang.</span></a>
  </div>
</section>

<section class="card src">
  <h2 style="color:var(--ink)">Nguồn tham khảo</h2>
  <ul>
    <li><a href="https://perfectdailygrind.com/?p=67723" target="_blank" rel="noopener">Perfect Daily Grind, 2019</a>: các lớp của trái cà phê, lớp nhớt giàu đường, vỏ lụa bong ra khi rang.</li>
    <li><a href="https://www.peets.com/blogs/peets/what-is-a-peaberry" target="_blank" rel="noopener">Peet's Coffee</a>: khoảng 5–10 % trái chỉ nuôi một hạt.</li>
    <li><a href="len-men-men-bia.html">MeDili, Lên men men bia</a>: khối lượng từ trái tươi đến cà phê rang theo từng cách sơ chế.</li>
    <li><a href="rang.html">MeDili, Cỗ máy Rang</a>: sàng gió, cyclone và 8 cấp độ rang.</li>
    <li><a href="vuon.html">MeDili, Vườn 12 tháng</a>: lịch 3 đợt hái, trái xanh tối đa 5 %.</li>
  </ul>
</section>

<section class="contact" id="lien-he">
  <div>
    <img class="lgK" src="assets/logo-kem.png" alt="MeDili Café Di Linh" width="260" height="83">
    <div class="tagline">Mê vị Di Linh</div>
    <p>Cà phê nguồn gốc Di Linh từ Medili Coffee Farm. Liên hệ qua Zalo để tìm hiểu vườn và cà phê.</p>
  </div>
  <div class="zalo">
    <span>Zalo MeDili</span>
    <strong id="zaloNo">0966770788</strong>
    <div><a href="https://zalo.me/3942166996018015136" target="_blank" rel="noopener">Nhắn Zalo</a><button type="button" id="copyZalo">Sao chép số</button></div>
    <small id="zaloMsg" role="status"></small>
  </div>
</section>
<footer>Medili - Farm Robusta Cà Sẻ Di Linh</footer>
</div>
'''

DESC = 'Năm lớp bọc quanh hạt cà phê, mỗi lớp được tách ra ở bước nào và vì sao Natural, Honey, Washed cho vị khác nhau.'
HEAD = (f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        f'<meta name="description" content="{DESC}"><meta property="og:title" content="Giải Phẫu Trái Cà Sẻ"><meta property="og:description" content="{DESC}">'
        f'<style>*{{box-sizing:border-box}}:root{{padding-top:env(safe-area-inset-top,0);padding-bottom:env(safe-area-inset-bottom,0)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>'
        f'<title>Giải Phẫu Trái Cà Sẻ</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n')
html = HEAD + '<style>' + SHARED + '</style>\n<style>' + PAGE_CSS + '</style></head><body>' + BODY + '\n<script>' + JS + '</script>\n</body></html>\n'
assert '</script' not in JS.lower()
open(os.path.join(OUT, PAGE), 'w', encoding='utf8').write(html)
open(os.path.join(HERE, '_page.check.js'), 'w', encoding='utf8').write(JS)

# ---------------- trang chủ ----------------
idx = rd('index.html')
SKEL = re.match(r'<!doctype html><html><head>.*?</head><body>\n?', idx, flags=re.S)
assert SKEL
idx = idx[SKEL.end():]
idx = re.sub(r'\s*</body></html>\s*$', '\n', idx)
idx = nav(idx)
FEAT_CSS = ('\n.feat a{display:grid;grid-template-columns:190px minmax(0,1fr);gap:16px 30px;align-items:center;background:var(--panel);border:1px solid var(--rule);border-radius:16px;padding:18px 24px;color:var(--ink);text-decoration:none}'
            '.feat svg{display:block;width:100%;height:auto}.feat h2{font:800 2.05rem/1.15 var(--display);margin:4px 0 6px;text-wrap:balance}'
            '.feat p{margin:0;max-width:62ch;color:var(--muted)}.feat .btn{margin-top:14px}.feat a:hover .btn{filter:brightness(1.08)}'
            '@media (max-width:620px){.feat a{grid-template-columns:96px minmax(0,1fr);padding:16px;gap:14px}.feat h2{font-size:1.65rem}}\n' + S.FIG_CSS +
            ':root{--skin:#B33A24;--skin2:#7A2414;--pulp:#E2A55E;--pulp2:#C4873C;--muc:#F7EBD0;--parch:#E4C891;--silver:#F8F3E9;--bean:#B49A63;--bean2:#CDB683;--cut:#6A4E30;--stem:#7A5233;--stem2:#5E3E25}\n')
i = idx.rfind('</style>')
idx = idx[:i] + FEAT_CSS + idx[i:]
FEAT = (f'\n<section class="feat"><a href="{PAGE}">{S.mini_figure()}<div><p class="eye">Giải phẫu trái cà phê</p>'
        f'<h2>Bên trong trái Cà Sẻ</h2><p>Năm lớp bọc một hạt nhân, lớp nào được tách ra ở bước nào, và vì sao Natural, Honey, Washed cho vị khác nhau.</p>'
        f'<span class="btn main">Đọc bài</span></div></a></section>')
anchor = '</div></section>\n<section><h2>Sản phẩm tiêu biểu</h2>'
assert idx.count(anchor) == 1
idx = idx.replace(anchor, '</div></section>' + FEAT + '\n<section><h2>Sản phẩm tiêu biểu</h2>')
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf8').write(idx)

# ---------------- menu các trang còn lại ----------------
for f in ['vuon.html', 'len-men-men-bia.html', 'len-men-trai-cay.html', 'rang.html', 'quay-pha.html', 'suc-khoe.html', 'mua-hang.html']:
    open(os.path.join(OUT, f), 'w', encoding='utf8').write(nav(rd(f)))

print('trang mới', len(html.encode()) // 1024, 'KB; trang chủ', len(idx.encode()) // 1024, 'KB')

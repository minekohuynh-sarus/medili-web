# Bộ 4 ảnh đăng Facebook 1080 x 1350, cùng hình vẽ với trang Giải phẫu trái Cà Sẻ
import os, sys, base64
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import svgs as S
import build_site as BS

OUT = os.path.join(HERE, 'fb'); os.makedirs(OUT, exist_ok=True)
LOGO = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(HERE, '..', 'site-live', 'assets', 'logo-mau.png'), 'rb').read()).decode()
GF = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=Big+Shoulders+Display:wght@700;800&family=JetBrains+Mono:wght@500;700&family=Playfair+Display:ital,wght@1,600&display=swap">'

CSS = '''
:root{--bg:#EFE4D2;--panel:#FDFAF2;--tint:#F5E7CF;--ink:#4A2C1A;--muted:#6B5C50;--rule:#CFC4AE;--accent:#9E3B26;--on-accent:#FFF6EC;
--copper:#B8894A;--ol:#2A1B16;--water:#9CCBD3;
--skin:#B33A24;--skin2:#7A2414;--pulp:#E2A55E;--pulp2:#C4873C;--muc:#F7EBD0;--parch:#E4C891;--silver:#F8F3E9;
--bean:#B49A63;--bean2:#CDB683;--cut:#6A4E30;--stem:#7A5233;--stem2:#5E3E25;--husk:#7E3A22;--chaff:#D9AA6E;
--display:"Big Shoulders Display","Be Vietnam Pro",sans-serif;--body:"Be Vietnam Pro",sans-serif;--mono:"JetBrains Mono",monospace;--sign:"Playfair Display",Georgia,serif}
*{box-sizing:border-box}html,body{margin:0}
body{width:1080px;height:1350px;background:var(--bg);color:var(--ink);font:400 24px/1.45 var(--body);overflow:hidden}
.pg{position:relative;width:1080px;height:1350px;padding:56px 64px 0;display:flex;flex-direction:column}
.top{display:flex;align-items:center;justify-content:space-between}
.top img{width:236px;height:auto;display:block}
.top span{font:600 19px var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--muted)}
h1{font:800 104px/1 var(--display);margin:34px 0 0;letter-spacing:.005em}
h1 em{font-style:normal;color:var(--accent)}
.sub{font:500 30px/1.35 var(--body);color:var(--muted);margin:14px 0 0;max-width:900px;text-wrap:balance}
.foot{position:absolute;left:64px;right:64px;bottom:42px;border-top:1px solid var(--rule);padding-top:20px;display:flex;justify-content:space-between;align-items:baseline}
.foot i{font:italic 600 27px var(--sign);color:var(--accent)}
.foot span{font:600 19px var(--body);color:var(--muted);letter-spacing:.04em}
.card{background:var(--panel);border:1px solid var(--rule);border-radius:22px}
.bd{flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:112px}
/* hình */
.ld{stroke:var(--ink);stroke-width:1.1;opacity:.6;fill:none}.dot{fill:var(--ink)}
.mk circle{fill:var(--accent);stroke:var(--accent)}.mk .hit{fill:none;stroke:none}
.mk text{font:800 19px var(--display);fill:var(--on-accent);text-anchor:middle;dominant-baseline:central}
.lgL,.lgD{display:none}
''' + S.FIG_CSS


def page(n, body, extra=''):
    return (f'<!doctype html><html lang="vi"><head><meta charset="utf-8">{GF}<style>{CSS}{extra}</style></head><body><div class="pg">'
            f'<div class="top"><img src="{LOGO}" alt="MeDili"><span>Giải phẫu trái cà phê · {n}/4</span></div>{body}'
            f'<div class="foot"><i>Medili - Farm Robusta Cà Sẻ Di Linh</i><span>Mê vị Di Linh</span></div></div></body></html>')


# 1. mặt cắt bảy phần
SHORT = {1: 'Giữ trái trên đốt cành', 2: 'Lớp da ngoài, đỏ khi chín', 3: 'Ngọt, mọng nước, nhiều đường',
         4: 'Keo trong, giàu pectin và đường', 5: 'Vỏ cứng mỏng như giấy, bọc từng hạt',
         6: 'Màng bạc ôm sát hạt, bong khi rang', 7: 'Phần đem rang, xay và pha'}
fig = S.main_figure().replace('id="fig1"', 'class="f"').replace('<g id="lys">', '<g>').replace('<g id="mks">', '<g>')
leg = ''.join(f'<li><b>{p["k"]}</b><div><strong><i style="background:{p["c"]}"></i>{p["n"]}</strong><span>{SHORT[p["k"]]}</span></div></li>' for p in BS.PARTS)
p1 = page(1, f'''<h1>Giải Phẫu <em>Trái Cà Sẻ</em></h1><p class="sub">Năm lớp bọc một hạt nhân, cộng phần cuống nối trái với cành.</p>
<div class="bd"><div class="g1">{fig}<ol>{leg}</ol></div></div>''', '''
.g1{display:grid;grid-template-columns:600px minmax(0,1fr);gap:16px;align-items:center;margin-left:-22px}
.g1 .f{width:600px;height:auto;display:block}
.g1 ol{list-style:none;margin:0;padding:0;display:grid;gap:18px}
.g1 li{display:grid;grid-template-columns:44px minmax(0,1fr);gap:12px;align-items:start}
.g1 li>b{width:44px;height:44px;border-radius:50%;background:var(--accent);color:var(--on-accent);display:grid;place-items:center;font:800 26px var(--display)}
.g1 strong{display:flex;align-items:center;gap:10px;font:700 28px/1.2 var(--body)}
.g1 strong i{width:18px;height:18px;border-radius:50%;box-shadow:inset 0 0 0 1.5px var(--ol);flex:none}
.g1 span{display:block;font:400 22px/1.35 var(--body);color:var(--muted);margin-top:3px;text-wrap:balance}
''')

# 2. ba cách sơ chế
tri = ''.join(f'<figure>{S.trio_figure(k)}<figcaption><b>{t}</b><em>{s}</em><p>{d}</p></figcaption></figure>' for k, t, s, d in BS.TRIO)
p2 = page(2, f'''<h1>Natural, Honey, <em>Washed</em></h1><p class="sub">Cùng một trái chín. Khác nhau ở lớp nào còn bám quanh hạt khi đem phơi. Nét đứt là phần đã bóc đi.</p>
<div class="bd"><div class="g2">{tri}</div><p class="note"><b>Ở MeDili:</b> dòng Classic là Robusta sơ chế Natural. Dòng Premium lên men Honey hoặc Washed để mở hương trái cây.</p></div>''', '''
.g2{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:30px}
.g2 figure{margin:0}.g2 svg{display:block;width:100%;height:auto}
.g2 b{display:block;font:800 54px/1 var(--display);margin-top:14px}
.g2 em{display:block;font:700 22px/1.3 var(--body);font-style:normal;color:var(--accent);margin-top:8px}
.g2 p{font:400 21px/1.45 var(--body);margin:10px 0 0}
.note{margin:34px 0 0;background:var(--tint);border-radius:18px;padding:22px 26px;font:400 24px/1.45 var(--body)}
.note b{color:var(--accent)}
''')

# 3. hai hạt hay một hạt
p3 = page(3, f'''<h1>Hai Hạt Hay <em>Một Hạt</em></h1><p class="sub">Thường mỗi trái nuôi hai hạt úp mặt phẳng vào nhau. Có trái chỉ nuôi một hạt tròn.</p>
<div class="bd"><div class="g3"><figure>{S.duo_figure('two')}<figcaption><b>Trái hai hạt</b>hai hạt dẹt, mặt phẳng có rãnh giữa</figcaption></figure>
<figure>{S.duo_figure('one')}<figcaption><b>Trái một hạt</b>một hạt tròn, gọi là cà phê culi</figcaption></figure></div>
<div class="stat"><b>5–10 %</b><p>số trái chỉ nuôi một hạt. Hạt culi tròn đều, lăn trong lồng rang khác hạt dẹt, nên thường được sàng riêng để rang một mẻ. MeDili chọn culi riêng theo từng lô.</p></div></div>''', '''
.g3{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px}
.g3 figure{margin:0;background:var(--panel);border:1px solid var(--rule);border-radius:22px;padding:22px 18px 22px}
.g3 svg{display:block;width:100%;height:auto}
.g3 figcaption{text-align:center;font:500 21px/1.35 var(--body);color:var(--muted);margin-top:8px}
.g3 figcaption b{display:block;font:800 40px/1.1 var(--display);color:var(--ink);margin-bottom:4px}
.stat{display:grid;grid-template-columns:auto minmax(0,1fr);gap:28px;align-items:center;margin-top:44px}
.stat b{font:800 120px/1 var(--display);color:var(--accent)}
.stat p{margin:0;font:400 26px/1.45 var(--body)}
''')

# 4. 100 kg trái chín
R = BS.rows('washed')
rws = ''
for r in R:
    prod = ' prod' if r['i'] >= 7 else ''
    em = f'<em style="background:{r["c"]}"></em>' if r['c'] else ''
    rws += (f'<div class="r{prod}"><span>{r["n"]}</span><span class="bar"><i style="width:{r["v"]:.2f}%"></i>'
            f'<u style="left:{r["v"]:.2f}%;width:{r["p"]-r["v"]:.2f}%;background:{r["c"] or "transparent"}"></u></span>'
            f'<b>{BS.fm(r["v"])} kg</b><small>{em}{r["o"]}</small></div>')
p4 = page(4, f'''<h1 class="h4">100 kg Trái Chín <em>Còn Lại Gì</em></h1><p class="sub">Sơ chế Washed, ước tính theo mô hình của MeDili. Mỗi bước bóc đi một lớp.</p>
<div class="bd"><div class="g4">{rws}</div><p class="end"><b>≈ 57 gói 250 g</b><span>khoảng 800 ly 18 g</span></p></div>''', '''
.h4{font-size:90px}.g4{display:grid}
.r{display:grid;grid-template-columns:200px minmax(0,1fr) 150px;gap:3px 20px;align-items:center;padding:8px 0;border-bottom:1px solid var(--rule)}
.r>span:first-child{font:600 26px var(--body)}
.bar{position:relative;height:22px;background:var(--tint);border-radius:0 6px 6px 0;overflow:hidden}
.bar i{display:block;height:100%;background:var(--copper);border-radius:0 6px 6px 0}
.bar u{position:absolute;top:0;bottom:0;box-shadow:inset 0 0 0 1px rgba(42,27,22,.25)}
.r b{font:700 28px var(--mono);text-align:right}
.r small{grid-column:2/4;font:400 19px var(--body);color:var(--muted);display:flex;align-items:center;gap:8px}
.r small em{width:13px;height:13px;border-radius:50%;box-shadow:inset 0 0 0 1px var(--ol);flex:none}
.r.prod>span:first-child{color:var(--accent)}.r.prod .bar i{background:var(--accent)}
.end{margin:26px 0 0;display:flex;align-items:baseline;gap:22px}
.end b{font:800 64px/1 var(--display);color:var(--accent)}.end span{font:500 26px var(--body);color:var(--muted)}
''')

for i, h in enumerate([p1, p2, p3, p4], 1):
    open(os.path.join(OUT, f'medili-trai-ca-phe-{i}.html'), 'w', encoding='utf8').write(h)
print('ok')

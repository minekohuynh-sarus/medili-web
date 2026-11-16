# Bộ 4 ảnh Facebook cho bài "Từ vườn đến ly", cùng khung với bộ Giải phẫu
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import fb_build as FB
import build_f2c as F

OUT = os.path.join(HERE, 'fb'); os.makedirs(OUT, exist_ok=True)
M = F.M
fm = F.fm
f1 = lambda n: (('%.1f' % n).rstrip('0').rstrip('.')).replace('.', ',')
pct = lambda v: f1(v / F.GL * 100)
nb = lambda s: s.replace(' đ', '&nbsp;đ').replace(' %', '&nbsp;%').replace(' kg', '&nbsp;kg').replace(' g', '&nbsp;g')

CSS = FB.CSS + '''
h1{text-wrap:balance}
.ic{width:66px;height:66px;padding:14px;border-radius:50%;border:2px solid var(--ink);background:var(--panel);fill:none;stroke:var(--ink);stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;flex:none}
.ic .fi{fill:var(--accent);stroke:none}
'''


def page(n, body, extra=''):
    return (f'<!doctype html><html lang="vi"><head><meta charset="utf-8">{FB.GF}<style>{CSS}{extra}</style></head><body><div class="pg">'
            f'<div class="top"><img src="{FB.LOGO}" alt="MeDili"><span>Từ vườn đến ly · {n}/4</span></div>{body}'
            f'<div class="foot"><i>Medili - Farm Robusta Cà Sẻ Di Linh</i><span>Mê vị Di Linh</span></div></div></body></html>')


# 1. chuỗi MeDili
rows = ''
for i, (ic, t, d, seg, dl) in enumerate(F.LANE_B):
    rows += f'<li class="{"dl" if dl else ""}">{F.icon(ic)}<div><b>{t}</b><span>{d}</span></div></li>'
p1 = page(1, f'''<h1>Từ Vườn <em>Đến Ly</em></h1><p class="sub">Farm to cup là cách làm cà phê để người uống biết ly của mình đến từ vườn nào và đi qua những tay ai.</p>
<div class="bd"><div class="lane"><span class="tag">Ở Di Linh</span><ol>{rows}</ol></div>
<p class="note">Chuỗi thường gặp chỉ có khâu trồng ở vùng trồng. Ở MeDili, trồng, sơ chế và rang đều ở Di Linh.</p></div>''', '''
.lane{position:relative}
.lane ol{list-style:none;margin:0;padding:0;display:grid}
.lane li{position:relative;display:grid;grid-template-columns:66px minmax(0,1fr);gap:24px;align-items:center;padding:18px 26px}
.lane li+li::before{content:"";position:absolute;left:52px;top:-10px;width:14px;height:14px;border-right:2.5px solid var(--muted);border-bottom:2.5px solid var(--muted);transform:rotate(45deg);opacity:.7}
.lane li.dl{background:#E9D2A6}
.lane li.dl:first-child{border-radius:22px 22px 0 0}.lane li.dl:nth-child(3){border-radius:0 0 22px 22px}
.lane b{display:block;font:700 31px/1.2 var(--body)}
.lane span{display:block;font:400 22px/1.4 var(--body);color:var(--muted);margin-top:2px}
.tag{position:absolute;right:26px;top:16px;font:700 18px var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--accent);z-index:1}
.note{margin:26px 0 0;background:var(--panel);border:1px solid var(--rule);border-radius:18px;padding:20px 24px;font:400 24px/1.45 var(--body)}
''')

# 2. một ly, tiền đi về đâu
p2 = page(2, f'''<h1>Người Trồng <em>Nhận Bao Nhiêu</em></h1><p class="sub">{nb(f"Một ly phin 25 g bán {fm(F.GL)} đ. Giá nhân xô Lâm Đồng ngày 7/11/2026: 83.600 đ/kg.")}</p>
<div class="bd"><div class="hero"><b>{fm(M["farm"])}&nbsp;đ</b><span>{pct(M["farm"])}&nbsp;% giá một ly</span></div>
<div class="bar"><i class="f" style="width:{M["farm"]/F.GL*100:.2f}%"></i><i class="m" style="width:{M["mid"]/F.GL*100:.2f}%"></i><i class="q" style="width:{M["cafe"]/F.GL*100:.2f}%"></i></div>
<div class="segs">
<div><i class="f"></i><p><b>Người trồng</b><span>tiền nhân xô trong ly</span></p><strong>{fm(M["farm"])}&nbsp;đ<small>{pct(M["farm"])}&nbsp;%</small></strong></div>
<div><i class="m"></i><p><b>Sơ chế, rang, phân phối</b><span>từ nhân xô đến túi cà phê rang</span></p><strong>{fm(M["mid"])}&nbsp;đ<small>{pct(M["mid"])}&nbsp;%</small></strong></div>
<div><i class="q"></i><p><b>Quán</b><span>pha, mặt bằng, nhân công, sữa, đá, ly</span></p><strong>{fm(M["cafe"])}&nbsp;đ<small>{pct(M["cafe"])}&nbsp;%</small></strong></div>
</div><p class="fine">Phần của người trồng là doanh thu, chưa trừ phân bón, công hái, nước tưới. Quán mua cà phê rang theo giá sỉ MeDili 252.000&nbsp;đ/kg.</p></div>''', '''
.hero{display:flex;align-items:baseline;gap:24px}
.hero b{font:800 170px/1 var(--display);color:var(--accent)}
.hero span{font:600 32px var(--body);color:var(--muted)}
.bar{display:flex;height:60px;border-radius:12px;overflow:hidden;margin-top:26px;box-shadow:inset 0 0 0 1.5px var(--rule)}
.bar i{display:block;height:100%}
.f{background:#B49A63}.m{background:#B8894A}.q{background:#E8D6B8}
.segs{display:grid;margin-top:18px}
.segs>div{display:grid;grid-template-columns:24px minmax(0,1fr) auto;gap:18px;align-items:center;padding:16px 0;border-bottom:1px solid var(--rule)}
.segs i{width:24px;height:24px;border-radius:6px;box-shadow:inset 0 0 0 1.5px var(--ol)}
.segs p{margin:0}.segs b{display:block;font:700 28px/1.2 var(--body)}.segs span{display:block;font:400 21px var(--body);color:var(--muted)}
.segs strong{font:700 34px var(--mono);text-align:right}.segs strong small{display:block;font:500 21px var(--body);color:var(--muted)}
.fine{margin:22px 0 0;font:400 21px/1.45 var(--body);color:var(--muted)}
''')

# 3. 1 kg nhân xô đi bao xa
steps = [('1 kg', 'nhân xô Robusta', '83.600&nbsp;đ, giá Lâm Đồng ngày 7/11/2026'),
         (f'{f1(F.YIELD)} kg', 'cà phê rang', 'sau khi lọc 5&nbsp;% hạt lỗi và hao 16&nbsp;% khi rang'),
         (f'{round(M["cups"])} ly', 'phin 25 g', 'theo công thức pha phin của MeDili'),
         (f'{f1(M["sales"]/1e6)} triệu', 'đồng ở quán', f'nếu bán {fm(F.GL)}&nbsp;đ một ly')]
st = ''.join(f'<li><b>{a}</b><div><strong>{b}</strong><span>{c}</span></div></li>' for a, b, c in steps)
p3 = page(3, f'''<h1>1 kg Nhân Xô <em>Đi Bao Xa</em></h1><p class="sub">Từ bao nhân của người trồng đến những ly cà phê trên bàn quán.</p>
<div class="bd"><ol class="flow">{st}</ol></div>''', '''
.flow{list-style:none;margin:0;padding:0;display:grid;gap:30px}
.flow li{position:relative;display:grid;grid-template-columns:340px minmax(0,1fr);gap:26px;align-items:center;background:var(--panel);border:1px solid var(--rule);border-radius:22px;padding:22px 30px}
.flow li+li::before{content:"";position:absolute;left:160px;top:-26px;width:16px;height:16px;border-right:3px solid var(--muted);border-bottom:3px solid var(--muted);transform:rotate(45deg);opacity:.7}
.flow li:last-child{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.flow b{font:800 104px/1 var(--display);color:var(--accent)}
.flow li:last-child b{color:var(--on-accent)}
.flow strong{display:block;font:700 32px/1.2 var(--body)}
.flow span{display:block;font:400 22px/1.4 var(--body);color:var(--muted);margin-top:4px}
.flow li:last-child span{color:var(--on-accent);opacity:.85}
''')

# 4. farm to cup là gì
signs = [('Biết vườn, biết lô', 'Mỗi túi ghi được vườn, mã lô và ngày rang.'),
         ('Ít khâu trung gian', 'Mỗi lần qua tay là một lần cộng giá. Bớt khâu thì giá trị ở gần nơi trồng hơn.'),
         ('Giá theo chất lượng', 'Trái chín, sơ chế kỹ được bán theo chất lượng của lô.'),
         ('Rang gần ngày uống', 'Chuỗi ngắn đưa cà phê đến tay người uống sớm hơn.')]
gs = ''.join(f'<div><b>{i}</b><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(signs, 1))
p4 = page(4, f'''<h1>Farm To Cup <em>Là Gì</em></h1><p class="sub">Một cách làm cà phê, chưa phải một chứng nhận. Có bốn dấu hiệu để nhận ra.</p>
<div class="bd"><div class="g4s">{gs}</div><p class="ctx"><b>80&nbsp;%</b>sản lượng cà phê Việt Nam vẫn ở dạng nhân xanh, chủ yếu là Robusta.<small>Vietstock, 5/2026</small></p></div>''', '''
.g4s{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px}
.g4s>div{background:var(--panel);border:1px solid var(--rule);border-radius:22px;padding:24px 26px}
.g4s b{display:grid;place-items:center;width:52px;height:52px;border-radius:50%;background:var(--accent);color:var(--on-accent);font:800 30px var(--display)}
.g4s h3{font:800 42px/1.08 var(--display);margin:16px 0 0}
.g4s p{font:400 23px/1.45 var(--body);margin:10px 0 0;color:var(--ink)}
.ctx{margin:26px 0 0;display:grid;grid-template-columns:auto minmax(0,1fr);gap:4px 24px;align-items:center;font:500 27px/1.4 var(--body)}
.ctx b{grid-row:1/3;font:800 104px/1 var(--display);color:var(--accent)}
.ctx small{font:400 19px var(--body);color:var(--muted)}
''')

for i, h in enumerate([p1, p2, p3, p4], 1):
    open(os.path.join(OUT, f'medili-tu-vuon-den-ly-{i}.html'), 'w', encoding='utf8').write(h)
print('ok')

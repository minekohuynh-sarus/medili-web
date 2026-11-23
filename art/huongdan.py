# Trang Hướng dẫn pha (23/11/2026): bốn cách pha tại nhà, mô hình 3D dựng bằng code (three.js, file assets/hd3d.js).
# Bố cục tham khảo trang hướng dẫn pha dạng kể chuyện theo thanh cuộn: khung 3D cố định, chữ khổng lồ làm nền mỗi phần.
# Câu chữ, công thức và mô hình là của MeDili; công thức khớp Quầy pha, Cỗ máy Công thức pha và Cỗ máy Cold Brew.
from kit import *

FILE = 'huong-dan-pha.html'

# Thang cỡ xay khớp Cỗ máy Chiết xuất và Quầy pha.
GRIND = [('Mịn', 'Espresso'), ('Vừa mịn', 'Pour-over, moka'), ('Vừa', 'Lọc máy, AeroPress'), ('Vừa thô', 'Phin'), ('Thô', 'Ép Pháp, cold brew')]

METHODS = [
    dict(id='phin', word='Phin', no='01', eye='Phin', h2='Giọt chậm rơi, <em>đậm vị cả buổi sáng.</em>',
         lead='Cách pha quen thuộc nhất của người Việt. Nước đi qua lớp bột rất chậm nên ly đậm, thân dày, hợp uống đen đá hay sữa đá.',
         grind=3, stats=[('Cà phê', '25 g'), ('Nước', '80 ml'), ('Tỷ lệ', '1:3,2'), ('Nhiệt độ', '90–96 °C'), ('Thời gian', '6–8 phút'), ('Ủ', '2–3 phút')],
         steps=['Tráng phin và ly bằng nước sôi cho nóng đều.',
                'Cho 25 g cà phê xay vừa thô vào phin, lắc nhẹ cho mặt bột phẳng, đặt nắp gài lên, không nén chặt.',
                'Rót khoảng 20 ml nước 90–96 °C, ủ 2–3 phút cho bột nở.',
                'Rót thêm khoảng 60 ml, đậy nắp, chờ cà phê nhỏ giọt hết trong 3–5 phút.'],
         tip='<b>Cà phê sữa đá:</b> cho khoảng 30 ml sữa đặc vào ly trước khi đặt phin. Pha xong, khuấy đều rồi rót vào ly có khoảng 120 g đá.',
         use=[('sp-phin-robusta-classic.html', 'Phin Robusta Classic'), ('sp-phin-robusta-premium.html', 'Phin Robusta Premium'), ('sp-ngu-hanh-nui.html', 'Núi')],
         alt='Mô hình 3D: phin nhôm đặt trên ly thủy tinh có lớp sữa đặc, cà phê nhỏ giọt xuống ly'),
    dict(id='pour-over', word='Pour-over', no='02', eye='Pour-over', h2='Rót thành vòng, <em>hương nở từng lớp.</em>',
         lead='Nước nóng rót qua phễu giấy, chảy qua lớp bột rồi xuống bình. Giấy giữ lại dầu và cặn nên ly sạch vị, rõ hương, hợp Arabica và các lô rang sáng đến vừa.',
         grind=1, stats=[('Cà phê', '15 g'), ('Nước', '240 ml'), ('Tỷ lệ', '1:16'), ('Nhiệt độ', '90–96 °C'), ('Thời gian', '2:30–4:00'), ('Ủ', '30–45 giây')],
         steps=['Đặt giấy lọc vào phễu, tráng bằng nước nóng rồi đổ bỏ nước tráng.',
                'Cho 15 g cà phê xay vừa mịn vào giấy lọc, lắc nhẹ cho mặt bột phẳng.',
                'Rót khoảng 30 ml nước từ tâm ra ngoài cho ướt đều, ủ 30–45 giây.',
                'Rót chậm theo vòng xoắn ốc, chia 2–3 lần cho đủ 240 ml.',
                'Để nước chảy hết. Tổng thời gian khoảng 2 phút 30 giây đến 4 phút.'],
         tip='<b>Chỉnh vị:</b> ly chua gắt, nhạt thì xay mịn hơn một nấc. Ly đắng, khô miệng thì xay thô hơn hoặc giảm nhiệt độ nước 1–2 °C.',
         use=[('sp-catimor.html', 'Catimor'), ('sp-arabica-cau-dat.html', 'Arabica Cầu Đất'), ('sp-phin-arabica-premium.html', 'Arabica Premium')],
         alt='Mô hình 3D: ấm cổ ngỗng bằng đồng rót nước theo vòng vào phễu gốm đỏ đất đặt trên bình thủy tinh'),
    dict(id='espresso', word='Espresso', no='03', eye='Espresso', h2='Chín bar áp suất, <em>nửa phút đậm đặc.</em>',
         lead='Máy ép nước nóng qua lớp bột mịn nén chặt. Ly nhỏ nhưng rất đậm, có lớp crema, làm nền cho Americano, latte, cappuccino và cà phê sữa máy.',
         grind=0, stats=[('Cà phê', '18 g'), ('Ra ly', '36 g'), ('Tỷ lệ', '1:2'), ('Nhiệt độ', '90–94 °C'), ('Thời gian', '25–30 giây'), ('Áp suất', '9 bar')],
         steps=['Xay 18 g cà phê mịn ngay trước khi pha.',
                'Dàn đều bột trong tay cầm, nén phẳng, lắp vào máy.',
                'Chiết khoảng 36 g espresso trong 25–30 giây.',
                'Cân ly ra bằng gram thay vì nhìn vạch, vì lớp crema làm sai thể tích.'],
         tip='<b>Chỉnh độ xay:</b> shot chảy dưới 22 giây thì xay mịn hơn, quá 35 giây thì xay thô hơn. Giữ nguyên liều, mỗi lần chỉ chỉnh một yếu tố.',
         use=[('sp-may-robusta-premium.html', 'Máy Robusta Premium'), ('sp-may-blend-premium-7-3.html', 'Máy Blend 7:3'), ('sp-may-arabica-premium.html', 'Máy Arabica Premium')],
         alt='Mô hình 3D: tách espresso màu đỏ đất có lớp crema, đặt trên đĩa kem, hơi nóng bốc lên'),
    dict(id='cold-brew', word='Cold brew', no='04', eye='Cold brew', h2='Nước lạnh, thời gian dài, <em>vị êm và ngọt.</em>',
         lead='Bột xay thô ngâm trong nước lạnh nhiều giờ. Nước lạnh kéo ít chất chua và đắng hơn, nên ly mát, tròn vị, dễ uống. Pha một bình, uống trong vài ngày.',
         grind=4, stats=[('Cà phê', '100 g'), ('Nước', '800 ml'), ('Tỷ lệ', '1:8'), ('Nhiệt độ', 'Ngăn mát'), ('Thời gian', '18–24 giờ'), ('Khi uống', 'Pha 1:1')],
         steps=['Cho 100 g cà phê xay thô vào bình hoặc túi lọc.',
                'Đổ 800 ml nước lọc nguội, khuấy nhẹ cho bột ngấm đều.',
                'Đậy kín, ngâm trong ngăn mát tủ lạnh 18–24 giờ.',
                'Lọc bỏ bã, giữ lạnh. Khi uống, pha 1 phần cốt với 1 phần nước, sữa tươi hoặc đá.'],
         tip='<b>Bảo quản:</b> cốt đã lọc đậy kín trong ngăn mát và dùng trong 3 ngày. Không để cốt ngoài tủ lạnh lâu.',
         use=[('sp-phin-robusta-premium.html', 'Phin Robusta Premium'), ('sp-ngu-hanh-nang.html', 'Nắng'), ('cold-brew.html', 'Cỗ máy Cold Brew')],
         alt='Mô hình 3D: chai thủy tinh nâu cold brew MeDili và ly cà phê có đá'),
]


def stage(m, alt, cls=''):
    return (f'<div class="hd-stage{cls}" data-m="{m}" role="img" aria-label="{esc(alt)}">'
            f'<img src="assets/hd-{m}.webp" alt="" width="720" height="720" loading="{"eager" if m == "bean" else "lazy"}" decoding="async">'
            f'<span class="hd-drag" aria-hidden="true">Kéo để xoay</span></div>')


def gbar(i):
    cells = ''.join(f'<i class="{"on" if k == i else ""}"></i>' for k in range(5))
    return (f'<div class="hd-grind"><span class="k">Cỡ xay</span><b>{GRIND[i][0]}</b>'
            f'<span class="hd-gb" aria-hidden="true">{cells}</span><span class="hd-gl" aria-hidden="true"><small>Mịn</small><small>Thô</small></span></div>')


def method(m, flip):
    stats = ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in m['stats'])
    steps = ''.join(f'<li>{s}</li>' for s in m['steps'])
    use = ''.join(f'<a href="{h}">{t}</a>' for h, t in m['use'])
    return f'''
<section class="hd-ch{' flip' if flip else ''}" id="{m['id']}" aria-labelledby="h-{m['id']}">
 <p class="hd-word" aria-hidden="true" style="--n:{len(m['word'])}">{m['word']}</p>
 <div class="hd-row">
  {stage(m['id'], m['alt'])}
  <div class="hd-txt">
   <p class="eye">{m['no']} · {m['eye']}</p>
   <h2 class="p-h2" id="h-{m['id']}">{m['h2']}</h2>
   <p class="hd-lead">{m['lead']}</p>
   {gbar(m['grind'])}
   <dl class="hd-stats">{stats}</dl>
   <ol class="hd-steps">{steps}</ol>
   <p class="hd-tip">{m['tip']}</p>
   <div class="hd-use"><span class="k">Dùng với</span>{use}</div>
  </div>
 </div>
</section>'''


CSS = '''
/* Hướng dẫn pha: lớp 3D phủ cả nội dung, khung vẽ cao bằng màn hình trượt theo chỗ đang xem; không nhận thao tác chuột.
   Chữ khổng lồ nằm dưới mô hình (z 1), phần chữ nội dung nằm trên mô hình (z 3). */
.wrap.hd{gap:0;padding-top:0;overflow-x:clip;position:relative;grid-template-columns:minmax(0,1fr)}
.hd-3d{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:2}
#hd3d{position:absolute;left:0;top:0;width:100%;height:100vh;display:block;will-change:transform}
.hd-hero,.hd-row{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:24px 56px;align-items:center}
.hd-hero{min-height:min(calc(100vh - 70px),860px);padding-block:28px 40px}
.hd-hero h1{font:800 clamp(3rem,7.4vw,6.4rem)/.98 var(--display);margin:10px 0 14px;letter-spacing:.005em;text-wrap:balance}
.hd-hero h1 em,.hd-txt h2 em{font-style:normal;color:var(--accent)}
.hd-hero .sub{font-size:1.08rem;line-height:1.65;color:var(--muted);max-width:52ch;margin:0}
.hd-jump{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
.hd-jump a{display:inline-flex;align-items:baseline;gap:8px;border:1px solid var(--rule);background:var(--panel);border-radius:999px;padding:8px 15px;color:var(--ink);text-decoration:none;font:600 .92rem var(--body)}
.hd-jump a small{font:700 .72rem var(--mono);color:var(--accent)}
.hd-jump a:hover{border-color:var(--accent);color:var(--accent)}
.hd-stage{position:relative;width:100%;max-width:600px;aspect-ratio:1/1;justify-self:center;touch-action:pan-y;cursor:grab;user-select:none;-webkit-user-select:none}
.hd-stage:active{cursor:grabbing}
.hd-stage::before{content:"";position:absolute;inset:9%;border-radius:50%;background:radial-gradient(circle at 50% 42%,var(--hd-disc1) 0,var(--hd-disc2) 70%,transparent 71%)}
.hd-stage img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;transition:opacity .5s}
html.r3d .hd-stage img{opacity:0}
.hd-drag{position:absolute;left:50%;bottom:0;transform:translateX(-50%);font:600 .72rem var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);opacity:0;transition:opacity .4s;white-space:nowrap}
html.r3d .hd-drag{opacity:.75}
.hd-ch{position:relative;padding-block:clamp(40px,7vw,96px) clamp(24px,4vw,56px)}
/* chữ khổng lồ: cỡ chữ tính theo số ký tự (--n) để luôn vừa một dòng */
.hd-word{position:relative;z-index:1;margin:0 0 6px;font:800 min(17rem,calc((min(100vw,1560px) - 40px) / (var(--n) * .5)))/.8 var(--display);letter-spacing:-.01em;text-transform:uppercase;color:var(--accent);text-align:center;white-space:nowrap;overflow:hidden;user-select:none;-webkit-user-select:none}
.hd-row{align-items:start}
.hd-ch.grind .hd-row{align-items:center}
/* mô hình nhô lên đè một phần chữ khổng lồ, phần chữ nội dung bắt đầu ngay dưới chữ khổng lồ */
.hd-ch:not(.grind) .hd-row .hd-stage{margin-top:calc(-1 * clamp(40px,8vw,140px))}
.hd-stage[data-m=grinder] .hd-drag{display:none}
.hd-row .hd-stage{grid-column:1;grid-row:1}.hd-row .hd-txt{grid-column:2;grid-row:1}
.hd-ch.flip .hd-row .hd-stage{grid-column:2}.hd-ch.flip .hd-row .hd-txt{grid-column:1}
.hd-txt{position:relative;z-index:3;max-width:560px;min-width:0;justify-self:center;width:100%}
.hd-txt h2{margin:6px 0 10px}
.hd-lead{margin:0 0 16px;color:var(--muted);line-height:1.65}
.hd-grind{display:grid;grid-template-columns:auto minmax(0,1fr);gap:4px 12px;align-items:baseline;margin:0 0 16px}
.hd-grind b{font:600 .95rem var(--body)}
.hd-gb{grid-column:1/-1;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:4px;margin-top:4px}
.hd-gb i{display:block;height:7px;border-radius:4px;background:var(--rule)}
.hd-gb i.on{background:var(--accent)}
.hd-gl{grid-column:1/-1;display:flex;justify-content:space-between;color:var(--muted);font-size:.74rem}
.hd-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px 18px;margin:0 0 18px;padding:14px 0 0;border-top:1px solid var(--rule)}
.hd-stats div{min-width:0}
.hd-stats dt{font:600 .7rem var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.hd-stats dd{margin:2px 0 0;font:700 1.18rem/1.25 var(--mono);color:var(--ink);font-variant-numeric:tabular-nums}
.hd-steps{list-style:none;counter-reset:hd;margin:0 0 16px;padding:0;display:grid;gap:10px}
.hd-steps li{counter-increment:hd;display:grid;grid-template-columns:30px minmax(0,1fr);gap:12px;align-items:start;line-height:1.55}
.hd-steps li::before{content:counter(hd);display:grid;place-items:center;width:28px;height:28px;border-radius:50%;background:var(--tint);color:var(--accent);font:700 .85rem var(--mono)}
.hd-tip{margin:0 0 16px;padding:12px 14px;border-radius:12px;background:var(--panel);border:1px solid var(--rule);font-size:.93rem;line-height:1.55}
.hd-use{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.hd-use .k{margin-right:2px}
.hd-use a{border:1px solid var(--rule);border-radius:999px;padding:6px 12px;color:var(--ink);text-decoration:none;font:600 .86rem var(--body);background:var(--panel)}
.hd-use a:hover{border-color:var(--accent);color:var(--accent)}
.hd-gscale{list-style:none;margin:14px 0 0;padding:0;display:grid;gap:8px}
.hd-gscale li{display:grid;grid-template-columns:22px 92px minmax(0,1fr);gap:10px;align-items:center;font-size:.93rem}
.hd-gscale i{display:block;justify-self:center;border-radius:50%;background:var(--accent)}
.hd-gscale b{font-weight:600}.hd-gscale span{color:var(--muted)}
.hd-end{position:relative;z-index:3;margin:clamp(30px,5vw,64px) 0 10px;background:var(--accent);color:var(--on-accent);border-radius:20px;padding:clamp(24px,4vw,44px);display:grid;grid-template-columns:minmax(0,1.3fr) auto;gap:18px 30px;align-items:center}
.hd-end h2{font:800 clamp(2rem,4.4vw,3.3rem)/1.05 var(--display);margin:0 0 8px;color:inherit;text-wrap:balance}
.hd-end p{margin:0;max-width:60ch;opacity:.92}
.hd-end .cta{margin:0;justify-content:flex-end}
.hd-end .btn{border-color:var(--on-accent);color:var(--on-accent);background:transparent}
.hd-end .btn.main{background:var(--on-accent);color:var(--accent)}
.hd-note{position:relative;z-index:3;text-align:center;color:var(--muted);font-size:.88rem;margin:6px 0 0}
:root{--hd-disc1:#F6EBDA;--hd-disc2:#EFDFC7}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--hd-disc1:#3A2A1F;--hd-disc2:#30231A}}
:root[data-theme="dark"]{--hd-disc1:#3A2A1F;--hd-disc2:#30231A}
@media (max-width:900px){
  .hd-hero,.hd-row{grid-template-columns:minmax(0,1fr);gap:8px}
  .hd-hero{min-height:0;padding-top:18px}
  .hd-hero .hd-stage{grid-row:2;max-width:440px}
  .hd-row .hd-stage,.hd-ch.flip .hd-row .hd-stage{grid-column:1;grid-row:1;max-width:460px}
  .hd-row .hd-txt,.hd-ch.flip .hd-row .hd-txt{grid-column:1;grid-row:2}
  .hd-ch.grind .hd-row .hd-stage{grid-row:2}.hd-ch.grind .hd-row .hd-txt{grid-row:1}
  .hd-ch:not(.grind) .hd-row .hd-stage{margin-top:calc(-1 * clamp(24px,9vw,72px))}
  .hd-end{grid-template-columns:minmax(0,1fr)}.hd-end .cta{justify-content:flex-start}
}
@media (max-width:520px){.hd-stats{grid-template-columns:repeat(2,minmax(0,1fr))}.hd-stats dd{font-size:1.06rem}}
'''


def page():
    grind_scale = ''.join(f'<li><i style="width:{6 + k * 3}px;height:{6 + k * 3}px"></i><b>{a}</b><span>{b}</span></li>'
                          for k, (a, b) in enumerate(GRIND))
    jump = ''.join(f'<a href="#{m["id"]}"><small>{m["no"]}</small>{m["eye"]}</a>' for m in METHODS)
    hero = f'''
<section class="hd-hero" aria-labelledby="h-hd">
 <div class="hd-txt" style="justify-self:start">
  <p class="eye">Hướng dẫn pha · MeDili</p>
  <h1 id="h-hd">Bốn cách pha, <em>một vị Di Linh.</em></h1>
  <p class="sub">Phin, pour-over, espresso hay cold brew: mỗi cách cần cỡ xay, lượng cà phê, nước và thời gian riêng. Chọn dụng cụ bạn có ở nhà rồi làm theo từng bước bên dưới.</p>
  <nav class="hd-jump" aria-label="Chọn cách pha">{jump}</nav>
 </div>
 {stage('bean', 'Mô hình 3D: hạt cà phê rang mộc xoay chậm')}
</section>'''
    grind = f'''
<section class="hd-ch grind flip" id="xay" aria-labelledby="h-xay">
 <div class="hd-row">
  {stage('grinder', 'Mô hình 3D: cối xay tay bằng đồng, bột cà phê rơi thành dòng xuống phin bên dưới')}
  <div class="hd-txt">
   <p class="eye">Trước khi pha · Xay</p>
   <h2 class="p-h2" id="h-xay">Mỗi cách pha, <em>một cỡ xay riêng.</em></h2>
   <p class="hd-lead">Bột càng mịn, nước lấy chất ra càng nhanh. Espresso cần bột mịn để giữ áp suất, phin cần bột vừa thô để nước nhỏ giọt đều, cold brew ngâm lâu nên xay thô. Xay ngay trước khi pha, vì bột xay sẵn mất mùi thơm nhanh hơn hạt nguyên.</p>
   <ul class="hd-gscale">{grind_scale}</ul>
  </div>
 </div>
</section>'''
    body = (hero + grind + ''.join(method(m, i % 2 == 0) for i, m in enumerate(METHODS)) + f'''
<section class="hd-end" aria-labelledby="h-end">
 <div><h2 id="h-end">Chưa có cối xay? MeDili xay sẵn đúng cỡ.</h2>
 <p>Khi đặt hàng, bạn chọn nguyên hạt hoặc xay sẵn cho phin, cho máy espresso hay cho pha thủ công. Muốn công thức riêng theo gu, thử Cỗ máy Công thức pha.</p></div>
 <div class="cta"><a class="btn main" href="cua-hang.html">Chọn cà phê</a><a class="btn" href="cong-thuc-pha.html">Tạo công thức riêng</a><a class="btn" href="quay-pha.html">Món sữa ở Quầy pha</a></div>
</section>
<p class="hd-note">Công thức là mốc khởi đầu. Pha, nếm, rồi chỉnh theo gu của bạn.</p>
<div class="hd-3d" aria-hidden="true"><canvas id="hd3d"></canvas></div>
<script type="module" src="assets/hd3d.js"></script>''')
    desc = ('Hướng dẫn pha cà phê MeDili tại nhà theo bốn cách: phin, pour-over, espresso và cold brew. '
            'Cỡ xay, lượng cà phê, nước, nhiệt độ, thời gian và từng bước, kèm mô hình 3D xoay được.')
    return doc(FILE, 'Hướng dẫn pha cà phê · MeDili', desc, body, css=CSS, wrap_cls='wrap hd')

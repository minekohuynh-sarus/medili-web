# Trang Đồng hành cùng quán (23/11/2026): trang cho khách quán theo kiểu "chọn theo ưu tiên của quán".
# Bố cục tham khảo trang đồng hành của một nhà cung cấp cà phê: ưu tiên của quán -> ba dòng cà phê -> các bước đồng hành -> phiếu liên hệ.
# Câu chữ là của MeDili; giá, chính sách lấy đúng như Phòng chọn mua và trang HORECA.
# Chị Ngân xác nhận 23/11/2026: mẫu thử 50 g miễn phí, phản hồi qua Zalo trong 60 phút (giờ làm việc 6:30–22:30),
# có hướng dẫn công thức, chỉnh cối xay, bảo trì máy tại quán. Khu vực bảo trì: "thống nhất với từng đối tác".
from kit import *
from pages_a import loc_cards

FILE = 'dong-hanh-cung-quan.html'

SP = {'pc': 'sp-phin-robusta-classic.html', 'mc': 'sp-may-robusta-classic.html', 'b91': 'sp-may-blend-premium-9-1.html',
      'pp': 'sp-phin-robusta-premium.html', 'mp': 'sp-may-robusta-premium.html', 'b82': 'sp-may-blend-premium-8-2.html',
      'b73': 'sp-may-blend-premium-7-3.html', 'pa': 'sp-phin-arabica-premium.html', 'ma': 'sp-may-arabica-premium.html',
      'b55': 'sp-may-blend-premium-5-5.html', 'ms': 'sp-may-robusta-specialty.html'}

# ba hướng ưu tiên -> ba dòng cà phê; quy mô và ly mỗi ngày khớp bảng "Quán nên chọn gì" ở Phòng chọn mua
LINES = [
    dict(id='classic', no='01', pri='Tối ưu giá vốn', name='Classic',
         need='Bán nhiều ly mỗi ngày, cần giá vốn mỗi ly thấp mà ly vẫn đậm vị.',
         taste='pc', fit='Xe đẩy, kiosk, quán vỉa hè', cups='30–80 ly mỗi ngày',
         drinks='Phin, đen đá, sữa đá, espresso, cà phê sữa máy', items=['pc', 'mc', 'b91']),
    dict(id='premium', no='02', pri='Cân bằng vị và giá', name='Premium',
         need='Khách ngồi lại lâu, cần ly tròn vị, dễ uống, giá vốn vừa phải.',
         taste='pp', fit='Quán có chỗ ngồi', cups='80–200 ly mỗi ngày',
         drinks='Phin, đen đá, sữa đá, latte, cappuccino, cold brew', items=['pp', 'mp', 'b82', 'b73']),
    dict(id='arabica', no='03', pri='Chất lượng trên hết', name='Arabica & Specialty',
         need='Thực đơn có espresso, latte, cold brew, cần hương rõ và ly đều tay mỗi ngày.',
         taste='pa', fit='Chuỗi cửa hàng, khách sạn, nhà hàng', cups='trên 200 ly mỗi ngày',
         drinks='Espresso, Americano, latte, cappuccino, cold brew', items=['pa', 'ma', 'b55', 'ms']),
]

PHOTOS = [('p-robusta-canh.jpg', 'Cành Robusta trĩu trái chín đỏ', 'Vườn Cà Sẻ Di Linh.'),
          ('p-tay-hai-doc.jpg', 'Bàn tay hái từng trái cà phê chín trên cành', 'Hái trái chín.'),
          ('p-san-phoi-wide.jpg', 'Cà phê phơi trên sân giữa đồi', 'Phơi giữa đồi.'),
          ('p-may-rang.jpg', 'Hạt cà phê vừa rang trên khay làm nguội', 'Rang tại xưởng Thôn 11.'),
          ('p-may-rang-dung.jpg', 'Hạt cà phê vừa rang đảo trên khay làm nguội', 'Làm nguội sau mẻ rang.'),
          ('p-kho-wide.jpg', 'Xe xúc đổ cà phê trong kho, bụi vàng dưới ánh đèn', 'Kho nguyên liệu mùa vụ.')]

CSS = '''
/* Đồng hành cùng quán */
.dh-hero{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:22px 44px;align-items:center;padding-block:10px 6px}
.dh-hero h1{font:800 clamp(2.7rem,6vw,5rem)/1 var(--display);margin:8px 0 12px;letter-spacing:.005em;text-wrap:balance}
.dh-hero h1 em,.dhq .p-h2 em{font-style:normal;color:var(--accent)}
.dh-hero .lead{font-size:1.04rem;line-height:1.65}
.dh-hero .pf img{border-radius:18px;aspect-ratio:1/1;object-fit:cover;width:100%;height:auto}
.dh-pri{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:0;border-top:1px solid var(--rule)}
.dh-pri a{display:grid;grid-template-columns:clamp(64px,9vw,120px) minmax(0,1fr) auto;gap:4px 18px;align-items:center;padding:18px 4px;border-bottom:1px solid var(--rule);color:var(--ink);text-decoration:none}
.dh-pri .n{grid-row:1/3;grid-column:1;font:800 clamp(2.6rem,6vw,4.6rem)/.9 var(--display);color:var(--accent)}
.dh-pri b{grid-column:2;font:800 clamp(1.3rem,2.4vw,1.8rem)/1.15 var(--display);letter-spacing:.01em}
.dh-pri span{grid-column:2;color:var(--muted);font-size:.95rem;line-height:1.5}
.dh-pri .go{grid-row:1/3;grid-column:3;width:42px;height:42px;border-radius:50%;border:1px solid var(--rule);display:grid;place-items:center;color:var(--accent);transition:transform .2s,background .2s}
.dh-pri .go svg{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.dh-pri a:hover .go{background:var(--accent);color:var(--on-accent);transform:translateY(2px)}
.dh-pri a:hover b{color:var(--accent)}
.dh-cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;align-items:stretch}
.dh-card{display:flex;flex-direction:column;gap:10px;background:var(--panel);border:1px solid var(--rule);border-radius:18px;padding:20px 20px 18px;min-width:0;scroll-margin-top:90px;transition:border-color .25s,box-shadow .25s}
.dh-card.on{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent) inset}
.dh-card .k{color:var(--accent)}
.dh-card h3{font:800 clamp(1.8rem,3vw,2.3rem)/1.05 var(--display);margin:0;letter-spacing:.01em}
.dh-card .taste{margin:0;color:var(--muted);font-size:.93rem;line-height:1.55}
.dh-fit{display:flex;flex-wrap:wrap;gap:6px}
.dh-fit span{background:var(--tint);border-radius:999px;padding:5px 11px;font:600 .8rem var(--body)}
.dh-card .use{margin:0;font-size:.9rem;line-height:1.5}
.dh-card .use b{font-weight:600}
.dh-pr{margin:4px 0 0;padding:0;list-style:none;border-top:1px solid var(--rule)}
.dh-pr li{display:flex;justify-content:space-between;align-items:baseline;gap:10px;padding:9px 0;border-bottom:1px dashed var(--rule)}
.dh-pr a{color:var(--ink);text-decoration:none;font-weight:600;font-size:.93rem}
.dh-pr a:hover{color:var(--accent)}
.dh-pr b{font:700 .95rem var(--mono);white-space:nowrap;font-variant-numeric:tabular-nums}
.dh-pr .h{font:600 .7rem var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);border-bottom:0;padding-bottom:0}
.dh-card .cta{margin-top:auto;padding-top:6px}
.dh-card .cta .btn{width:100%;justify-content:center}
.dh-ask{background:var(--accent);color:var(--on-accent);border-radius:20px;padding:clamp(22px,4vw,40px);display:grid;grid-template-columns:minmax(0,1.4fr) auto;gap:16px 28px;align-items:center}
.dh-ask h2{font:800 clamp(1.9rem,4vw,3rem)/1.05 var(--display);margin:0 0 8px;color:inherit;text-wrap:balance}
.dh-ask p{margin:0;opacity:.92;max-width:62ch}
.dh-ask .cta{margin:0;justify-content:flex-end}
.dh-ask .btn{border-color:var(--on-accent);color:var(--on-accent);background:transparent}
.dh-ask .btn.main{background:var(--on-accent);color:var(--accent)}
.dh-ph{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.dh-ph .pf img{aspect-ratio:4/3;object-fit:cover;width:100%;height:auto;border-radius:14px}
.dh-ph .pf figcaption{font-size:.82rem;color:var(--muted)}
.dh-sup{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}
.dh-sup ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.dh-sup li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:10px;align-items:start;font-size:.93rem;line-height:1.5}
.dh-sup li::before{content:"";width:9px;height:9px;margin:7px 0 0 6px;border-radius:50%;background:var(--accent)}
.dh-promise{margin:0;font:600 1rem var(--body);color:var(--ink)}.dh-promise b{color:var(--accent)}
.dhq .p-form label.chk{display:flex;align-items:center;gap:10px;cursor:pointer;font:600 .95rem var(--body)}
.dhq .p-form label.chk input{width:18px;height:18px;padding:0;margin:0;flex:none;accent-color:var(--accent)}
.dhq .p-form textarea{min-height:84px;resize:vertical;font:inherit}
.btn.off{opacity:.55;cursor:not-allowed}
@media (max-width:900px){
  .dh-hero{grid-template-columns:minmax(0,1fr)}
  .dh-hero .pf img{aspect-ratio:16/10}
  .dh-cards,.dh-sup{grid-template-columns:minmax(0,1fr)}
  .dh-ask{grid-template-columns:minmax(0,1fr)}.dh-ask .cta{justify-content:flex-start}
}
@media (max-width:600px){
  .dh-ph{grid-template-columns:repeat(2,minmax(0,1fr))}
  .dh-pri a{grid-template-columns:56px minmax(0,1fr) auto;gap:2px 12px;padding:14px 2px}
  .dh-pri .go{width:34px;height:34px}
}
'''

JS = r'''
(()=>{const f=document.getElementById('dh-f');if(!f)return;const $=id=>document.getElementById(id);
const cards=[...document.querySelectorAll('.dh-card')];
function pick(p){const s=$('dh-p');if(p&&[...s.options].some(o=>o.value===p))s.value=p;
 cards.forEach(c=>c.classList.toggle('on',c.dataset.pri===s.value));sync()}
document.querySelectorAll('[data-pick]').forEach(a=>a.addEventListener('click',()=>pick(a.dataset.pick)));
const val=n=>[...f.querySelectorAll('[name="'+n+'"]:checked')].map(x=>x.value);
function build(){const L=['ĐỒNG HÀNH CÙNG QUÁN'];const g=id=>$(id).value.trim();
 const q=g('dh-q'),t=g('dh-t');if(q)L.push('Quán / doanh nghiệp: '+q);if(t)L.push('Tỉnh / thành phố: '+t);
 L.push('Loại hình: '+$('dh-m').value);L.push('Ưu tiên: '+$('dh-p').value);
 const b=val('pha');L.push('Cách pha: '+(b.length?b.join(', '):'chưa chọn'));L.push('Lượng dự kiến: '+$('dh-v').value);
 if($('dh-s').checked)L.push('Muốn nhận mẫu thử 50 g: có');const m=g('dh-n');if(m)L.push('Lời nhắn: '+m);
 const nm=g('dh-name'),ph=$('dh-ph').value.replace(/[\s.]/g,'');if(nm)L.push('Liên hệ: '+nm+(ph?' | '+ph:''));
 return {txt:L.join('\n'),nm,ph}}
function sync(){const r=build();$('dh-msg').textContent=r.txt;const ok=r.nm&&/^(0|\+84)\d{9,10}$/.test(r.ph),a=$('dh-gf');
 if(ok){const q=encodeURIComponent;a.href=FORM+'&'+FN.name+'='+q(r.nm)+'&'+FN.phone+'='+q(r.ph)+'&'+FN.txt+'='+q(r.txt);a.removeAttribute('aria-disabled');a.classList.remove('off');$('dh-st').textContent=''}
 else{a.removeAttribute('href');a.setAttribute('aria-disabled','true');a.classList.add('off')}}
f.addEventListener('input',sync);f.addEventListener('change',()=>pick());f.addEventListener('submit',e=>e.preventDefault());
$('dh-gf').addEventListener('click',e=>{if(!$('dh-gf').getAttribute('href')){e.preventDefault();
 $('dh-st').textContent='Vui lòng nhập họ tên và số điện thoại đúng để mở phiếu gửi MeDili.';($('dh-name').value.trim()?$('dh-ph'):$('dh-name')).focus()}});
$('dh-cp').addEventListener('click',async()=>{const t=$('dh-msg').textContent;
 try{await navigator.clipboard.writeText(t);$('dh-st').textContent='Đã sao chép tin nhắn. Mở Zalo MeDili rồi dán vào.'}
 catch(e){const r=document.createRange();r.selectNodeContents($('dh-msg'));const s=getSelection();s.removeAllRanges();s.addRange(r);$('dh-st').textContent='Đã chọn sẵn tin nhắn, bạn bấm sao chép trên máy.'}});
pick();
})();
'''

ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M6 13l6 6 6-6"/></svg>'


def page(P):
    t1 = lambda k: fm(P[k]['p'][1] * 1000)
    pri = ''.join(f'<li><a href="#{x["id"]}" data-pick="{x["pri"]}"><span class="n" aria-hidden="true">{x["no"]}</span>'
                  f'<b>{x["pri"]}</b><span>{x["need"]}</span><i class="go" aria-hidden="true">{ARROW}</i></a></li>' for x in LINES)
    cards = ''
    for x in LINES:
        rows = ''.join(f'<li><a href="{SP[k]}">{P[k]["n"]}</a><b>{t1(k)} đ/kg</b></li>' for k in x['items'])
        cards += f'''
 <article class="dh-card" id="{x['id']}" data-pri="{x['pri']}" aria-labelledby="h-{x['id']}">
  <p class="k">{x['no']} · {x['pri']}</p>
  <h3 id="h-{x['id']}">{x['name']}</h3>
  <p class="taste">{P[x['taste']]['taste']}.</p>
  <div class="dh-fit"><span>{x['fit']}</span><span>{x['cups']}</span></div>
  <p class="use"><b>Món phù hợp:</b> {x['drinks']}.</p>
  <ul class="dh-pr"><li class="h"><span>Sản phẩm</span><span>Sỉ cấp 1</span></li>{rows}</ul>
  <div class="cta"><a class="btn main" href="#ket-noi" data-pick="{x['pri']}">Chọn dòng {x['name']}</a></div>
 </article>'''
    photos = ''.join(photo(n, a, c) for n, a, c in PHOTOS)
    hero = f'''
<section class="dh-hero" aria-labelledby="h-dh">
 <div>
  <p class="eye">Đồng hành cùng quán · MeDili</p>
  <h1 id="h-dh">Chọn cà phê theo <em>cách quán bạn bán.</em></h1>
  <p class="lead">Quán vỉa hè cần giá vốn thấp. Quán có chỗ ngồi cần ly cân bằng giữa vị và giá. Chuỗi cửa hàng, nhà hàng, khách sạn cần ly ngon và đều tay mỗi ngày. MeDili rang Cà Sẻ Di Linh và cùng quán chọn dòng cà phê, cách pha, bậc giá phù hợp.</p>
  <div class="cta"><a class="btn main" href="#uu-tien">Tìm dòng cà phê cho quán</a><a class="btn" href="#ket-noi">Gửi nhu cầu</a></div>
 </div>
 {photo('p-hat-rang.jpg', 'Hạt cà phê rang trong phễu máy xay', 'Hạt rang MeDili trong phễu máy xay.', lazy=False)}
</section>'''
    body = hero + f'''
<section class="p-sec" id="uu-tien" aria-labelledby="h-uu">
 <p class="eye">Bắt đầu từ quán của bạn</p>
 <h2 class="p-h2" id="h-uu">Quán bạn đang <em>ưu tiên điều gì?</em></h2>
 <p class="lead">Chọn một hướng để xem dòng cà phê đi kèm. Chưa chắc thì cứ gửi nhu cầu, MeDili tư vấn thêm.</p>
 <ul class="dh-pri">{pri}</ul>
</section>

<section class="p-sec" id="giai-phap" aria-labelledby="h-gp">
 <p class="eye">Ba dòng cà phê cho quán</p>
 <h2 class="p-h2" id="h-gp">Ba hướng ưu tiên, <em>ba dòng cà phê MeDili.</em></h2>
 <div class="dh-cards">{cards}
 </div>
 <p class="note">Đơn vị đ/kg cà phê rang. Giá sỉ cấp 1 áp dụng khi quán mua từ 5 kg trong tháng. Khi đạt 20 kg trong tháng, quán được giá sỉ cấp 2 và phần chênh lệch được chiết khấu vào đơn kế tiếp. Giá chưa gồm 8% VAT và phí vận chuyển, có hiệu lực trong tháng và được xác nhận khi đặt hàng. Giá lẻ và bảng giá đầy đủ ở <a class="lnk" href="mua-hang.html">Phòng chọn mua</a>.</p>
</section>

<section class="dh-ask" aria-labelledby="h-ask">
 <div><h2 id="h-ask">Chưa chắc dòng nào hợp với quán?</h2>
 <p>Gửi MeDili thực đơn, số ly mỗi ngày và máy pha đang dùng. MeDili tư vấn dòng cà phê, độ xay, tỷ lệ pha và gửi mẫu 50 g miễn phí để quán thử. Phản hồi qua Zalo trong 60 phút, từ 6:30 đến 22:30.</p></div>
 <div class="cta"><a class="btn main" href="#ket-noi" data-pick="Chưa rõ, cần tư vấn">Nhận tư vấn</a><a class="btn" href="mua-hang.html">Tự tính giá mỗi ly</a></div>
</section>

<section class="p-sec" id="dong-hanh" aria-labelledby="h-dh2">
 <p class="eye">Đồng hành</p>
 <h2 class="p-h2" id="h-dh2">Từ vườn Di Linh <em>đến quầy pha của quán.</em></h2>
 <p class="lead">MeDili trồng, sơ chế và rang tại Di Linh, nên biết rõ từng mẻ cà phê giao cho quán đến từ đâu.</p>
 <div class="dh-ph">{photos}</div>
 <ol class="pst three">
  <li><span class="n">{icon('chat')}</span><h3><small>01</small>Hiểu mô hình quán</h3><p>MeDili hỏi thực đơn, số ly mỗi ngày, máy pha đang dùng và mức giá vốn quán mong muốn.</p></li>
  <li><span class="n">{icon('ly')}</span><h3><small>02</small>Thử mẫu miễn phí</h3><p>MeDili gửi miễn phí 50 g cà phê để quán pha thử trên máy và theo công thức của mình. Hai bên chốt lại dòng cà phê sau khi thử.</p></li>
  <li><span class="n">{icon('may')}</span><h3><small>03</small>Đưa vào vận hành</h3><p>Chốt quy cách túi 1 kg hoặc 5 kg và bậc giá theo khối lượng tháng. MeDili hướng dẫn công thức, chỉnh cối xay theo máy pha của quán và bảo trì máy.</p></li>
 </ol>
 <div class="dh-sup">
  <div class="box"><p class="k">MeDili hỗ trợ quán</p>
   <ul><li>Tư vấn chọn cà phê, độ xay, tỷ lệ pha.</li><li>Hướng dẫn công thức và thực đơn tại quán.</li><li>Chỉnh cối xay theo máy pha của quán.</li><li>Bảo trì máy pha, máy xay; tư vấn thiết bị pha chế.</li>
   <li>Hồ sơ đối tác: chứng nhận đủ điều kiện sản xuất, chứng nhận an toàn thực phẩm.</li></ul>
   <p class="note" style="margin-top:10px">Phạm vi hỗ trợ được thống nhất với từng đối tác.</p>
   <div class="lnks"><a class="lnk" href="huong-dan-pha.html">Hướng dẫn pha</a><a class="lnk" href="quay-pha.html">Quầy pha</a><a class="lnk" href="cong-thuc-pha.html">Cỗ máy Công thức pha</a></div></div>
  <div class="box"><p class="k">Cam kết và giao nhận</p>
   <ul><li>Các dòng rang mộc: cà phê nguyên chất, đúng thành phần công bố, không pha tạp, không thêm hương liệu hay chất bảo quản.</li>
   <li>Giao hàng toàn quốc, phí và thời gian được báo trước khi xác nhận đơn.</li>
   <li>Đổi trả 7 ngày khi có lỗi sản xuất, lỗi đóng gói, hư hỏng khi vận chuyển hoặc giao sai loại.</li>
   <li>Xưởng rang trung bình 20 tấn mỗi tháng, công suất tối đa 60 tấn.</li></ul>
   <div class="lnks"><a class="lnk" href="giao-hang.html">Giao hàng &amp; đổi trả</a><a class="lnk" href="horeca.html#ho-so">Hồ sơ cho đối tác</a></div></div>
 </div>
</section>

<section class="box p-sec" id="ket-noi" aria-labelledby="h-kn">
 <p class="eye">Kết nối với MeDili</p>
 <h2 class="p-h2" id="h-kn" style="margin:0">Kể MeDili nghe <em>về quán của bạn.</em></h2>
 <p class="dh-promise">MeDili phản hồi qua Zalo trong <b>60 phút</b>, từ 6:30 đến 22:30.</p>
 <p class="note">Trang không tự gửi tin. Bạn mở phiếu để gửi cho MeDili, hoặc sao chép tin nhắn rồi dán vào Zalo.</p>
 <form class="p-form" id="dh-f" novalidate>
  <div class="row2">
   <label for="dh-name">Họ tên<input id="dh-name" autocomplete="name" maxlength="80" placeholder="Ví dụ: Nguyễn Thị Lan" required></label>
   <label for="dh-ph">Số điện thoại hoặc Zalo<input id="dh-ph" type="tel" inputmode="tel" autocomplete="tel" maxlength="20" placeholder="0901234567" required></label>
  </div>
  <div class="row2">
   <label for="dh-q">Tên quán hoặc doanh nghiệp <small>không bắt buộc</small><input id="dh-q" autocomplete="organization" maxlength="80" placeholder="Ví dụ: Quán Mộc"></label>
   <label for="dh-t">Tỉnh, thành phố <small>không bắt buộc</small><input id="dh-t" maxlength="60" placeholder="Ví dụ: TP.HCM"></label>
  </div>
  <div class="row2">
   <label for="dh-m">Loại hình<select id="dh-m"><option>Quán cà phê</option><option>Chuỗi cửa hàng</option><option>Nhà hàng</option><option>Khách sạn</option><option>Văn phòng</option><option>Nhà rang</option><option>Đại lý, nhà phân phối</option><option>Khác</option></select></label>
   <label for="dh-p">Quán đang ưu tiên<select id="dh-p"><option>Tối ưu giá vốn</option><option>Cân bằng vị và giá</option><option>Chất lượng trên hết</option><option selected>Chưa rõ, cần tư vấn</option></select></label>
  </div>
  <div class="row2">
   <label for="dh-v">Lượng dự kiến mỗi tháng<select id="dh-v"><option>Dưới 5 kg</option><option selected>5–20 kg</option><option>20–100 kg</option><option>Trên 100 kg</option></select></label>
   <fieldset><legend>Cách pha ở quán</legend><div class="opts">
    <label><input type="checkbox" name="pha" value="Phin" checked>Phin</label>
    <label><input type="checkbox" name="pha" value="Pha máy">Pha máy</label>
    <label><input type="checkbox" name="pha" value="Cold brew">Cold brew</label>
    <label><input type="checkbox" name="pha" value="Pour-over">Pour-over</label>
   </div></fieldset>
  </div>
  <label for="dh-n">Lời nhắn <small>không bắt buộc</small><textarea id="dh-n" maxlength="400" placeholder="Máy pha đang dùng, món bán chạy, mức giá mong muốn…"></textarea></label>
  <label class="chk"><input type="checkbox" id="dh-s"> Quán muốn nhận mẫu thử 50 g miễn phí</label>
  <div><span class="k">Tin nhắn sẽ gửi</span><pre class="msg" id="dh-msg"></pre></div>
  <div class="cta" style="margin-top:0"><a class="btn main off" id="dh-gf" target="_blank" rel="noopener" aria-disabled="true">Mở phiếu gửi MeDili</a><button class="btn" type="button" id="dh-cp">Sao chép tin nhắn</button><a class="btn" href="{ZALO}" target="_blank" rel="noopener">Mở Zalo MeDili</a></div>
  <p class="fstat" id="dh-st" role="status"></p>
 </form>
</section>

<section class="p-sec">
 <h2 class="p-h2">Hai điểm <em>kết nối.</em></h2>
 {loc_cards()}
</section>
'''
    js = f"const FORM={FORM!r},FN={{name:{FORM_F['name']!r},phone:{FORM_F['phone']!r},txt:{FORM_F['txt']!r}}};" + JS
    desc = ('MeDili đồng hành cùng quán cà phê, nhà hàng, khách sạn: chọn dòng Classic, Premium hay Arabica & Specialty theo ưu tiên của quán, '
            'giá sỉ theo khối lượng tháng, mẫu thử 50 g miễn phí, hướng dẫn công thức, chỉnh cối xay, bảo trì máy, phản hồi qua Zalo trong 60 phút từ 6:30 đến 22:30.')
    return doc(FILE, 'Đồng hành cùng quán · MeDili', desc, body, css=CSS, js=js, wrap_cls='wrap pg dhq')

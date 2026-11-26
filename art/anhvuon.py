# Trang Ảnh vườn MeDili (21/11/2026) và khối ảnh nền toàn khung dùng chung (đầu trang, dải ảnh).
# Ảnh do chị Ngân gửi: thư mục Google Drive "11/2026" và ảnh đính kèm trong cuộc trò chuyện. Mọi ảnh đều có logo chìm MeDili.
from kit import *
from kit import _psize

A = lambda k: k           # mã ảnh đính kèm, xem make_photos.SRC
D = lambda p: p            # đường dẫn trong thư mục ảnh Drive đã tải về, xem make_photos.SRC2

GROUPS = [
    ('vuon', 'Vườn', 'Vườn <em>vào mùa.</em>',
     'Cà phê không chín cùng lúc. Trên một cành có trái xanh, trái ương và trái chín đỏ, vì thế mùa hái thường phải đi nhiều lượt.',
     [('trai-chin.html', 'Cỗ máy Trái chín'), ('vuon.html', 'Vườn 12 tháng')]),
    ('hai', 'Hái', 'Hái <em>bằng tay.</em>',
     'Trái chín được hái bằng tay rồi gom vào giỏ đeo, vào xô. Hái đúng độ chín là bước đầu của hương vị trong ly.',
     [('trai-ca-phe.html', 'Cấu tạo trái cà phê')]),
    ('thu', 'Thu hoạch', 'Mùa thu hoạch <em>rời vườn.</em>',
     'Cuối buổi hái, cà phê được đóng bao, chằng lên máy cày và chở theo đường lô ra khỏi vườn, về kho và sân phơi.',
     [('vung-trong.html', 'Vùng trồng Di Linh')]),
    ('phoi', 'Phơi & xay', 'Phơi <em>và xay xát.</em>',
     'Trái chín được phơi nguyên trái (Natural), phơi khi hạt còn lớp nhớt (Honey) hoặc xát tươi rồi mới phơi. Cà phê khô mới đem xay xát, tách vỏ để lấy nhân xanh.',
     [('len-men-men-bia.html', 'Ba cách sơ chế'), ('nhan-xanh.html', 'Chọn nhân xanh')]),
    ('doi', 'Giữa đồi', 'Từ vườn đến ly, <em>giữa đồi.</em>',
     'Trái cà phê chín, hạt rang MeDili và bàn pha nhìn ra đồi và hồ: một buổi pha cà phê ngoài trời.',
     [('cong-thuc-pha.html', 'Công thức pha'), ('cua-hang.html', 'Chọn cà phê')]),
]

# (nhóm, tên ảnh, nguồn, tỷ lệ cắt hoặc None = giữ khung gốc, tâm x, tâm y, alt, chú thích)
GAL = [
    ('vuon', 'vuon-chum-chin', A('a9bfa20b'), None, .5, .5, 'Chùm cà phê có trái xanh, trái vàng và trái đỏ trên cùng một cành', 'Một chùm, nhiều độ chín.'),
    ('vuon', 'vuon-trai-ung', A('e7526603'), None, .5, .5, 'Trái cà phê chuyển màu dưới tán lá', 'Trái chuyển màu dưới tán lá.'),
    ('vuon', 'vuon-robusta-canh', A('10517b97'), None, .5, .5, 'Cành Robusta trĩu trái chín đỏ', 'Robusta chín đỏ trĩu cành.'),
    ('vuon', 'vuon-canh-do', A('aa8c978e'), None, .5, .5, 'Cành cà phê có những trái đã chín đỏ', 'Những trái chín đầu tiên.'),
    ('vuon', 'vuon-tan-la', A('508fdebf'), None, .5, .5, 'Trái cà phê non và trái chín xen giữa tán lá', 'Trái non, trái chín dưới tán lá.'),
    ('vuon', 'vuon-robusta-chum', A('8a31c288'), None, .5, .5, 'Những chùm Robusta chín dày trên cành', 'Chùm Robusta chín dày.'),
    ('hai', 'hai-tay-hai', D('src/IMG_0603.jpg'), 4 / 5, .5, .55, 'Bàn tay hái giữa những chùm cà phê chín', 'Bàn tay hái giữa chùm chín.'),
    ('hai', 'hai-robusta', A('3759dff3'), None, .5, .5, 'Hai bàn tay hái chùm Robusta chín đỏ', 'Hái chùm Robusta chín.'),
    ('hai', 'hai-tung-trai', A('381f5a09'), None, .5, .5, 'Bàn tay hái từng trái cà phê chín trên cành', 'Hái từng trái chín.'),
    ('hai', 'hai-nam-tay', A('b922b23f'), None, .5, .5, 'Trái cà phê chín gom trong lòng bàn tay người hái', 'Trái chín gom trong lòng tay.'),
    ('hai', 'hai-vao-gio', A('7d3bb1b2'), None, .5, .5, 'Người hái tuốt trái cà phê vào giỏ đeo bên hông', 'Hái vào giỏ đeo bên hông.'),
    ('hai', 'hai-trai-chin', A('c7aa0b06'), None, .5, .5, 'Trái cà phê chín đỏ trên tay người hái', 'Trái chín vừa hái.'),
    ('thu', 'thu-xo-trai', A('67b383a6'), None, .5, .5, 'Người hái bê xô đầy trái cà phê chín', 'Một xô trái chín sau buổi hái.'),
    ('thu', 'thu-chat-bao', D('work/H0550.jpg'), None, .5, .5, 'Hai người mặc áo MeDili chằng bao cà phê trên máy cày', 'Chằng bao cà phê lên máy cày.'),
    ('thu', 'thu-noi-duoi', D('work/H0547.jpg'), None, .5, .5, 'Máy cày chở bao cà phê nối đuôi trên đường lô', 'Máy cày nối đuôi rời vườn.'),
    ('thu', 'thu-trong-kho', A('b75910ab'), None, .5, .5, 'Xe xúc làm việc trong kho cà phê dưới ánh đèn vàng', 'Trong kho, mùa thu hoạch.'),
    ('phoi', 'phoi-san-doi', A('5c6c7a3b'), None, .5, .5, 'Cà phê phơi trên sân giữa đồi', 'Phơi trên sân giữa đồi.'),
    ('phoi', 'phoi-natural', A('caff86f5'), None, .5, .5, 'Trái cà phê phơi nguyên trái trên giàn', 'Natural: phơi nguyên trái.'),
    ('phoi', 'phoi-honey', A('ce2fd9de'), None, .5, .5, 'Hạt cà phê còn lớp nhớt phơi trên giàn', 'Honey: hạt còn lớp nhớt.'),
    ('phoi', 'phoi-trai-kho', A('0a3c5421'), None, .5, .5, 'Trái cà phê khô dần trên lưới phơi', 'Trái khô dần trên lưới phơi.'),
    ('phoi', 'xay-xat-tuoi', A('47fb57b2'), None, .5, .5, 'Máy xát tươi tách vỏ cà phê', 'Xát tươi: máy tách vỏ khỏi hạt.'),
    ('phoi', 'xay-sang-nhan', A('4653ff83'), None, .5, .5, 'Nhân cà phê chảy qua máng gỗ xuống rổ', 'Nhân chảy qua máng sàng.'),
    ('phoi', 'xay-nhan-xanh', A('2c197a7a'), None, .5, .5, 'Nhân xanh trong đĩa, đặt trên tấm thảm bánh xe hương vị', 'Nhân xanh sau xay xát.'),
    # Đợt 3 (26/11/2026): thư mục Drive "LỌC 10 ẢNH CHỊ NGÂN" và "ĐIỆN THOẠI" chị Ngân gửi để bổ sung mục Vùng trồng Di Linh.
    # Không dùng ảnh có người chụp rõ mặt (IMG_0214, IMG_0220, IMG_0253) và ảnh người nữ đội mũ MeDili.
    ('vuon', 'vuon-chum-do-xen', D('dot3/IMG_0582.jpg'), None, .5, .5, 'Nhiều chùm Robusta chín đỏ xen vài trái xanh trên cành', 'Chùm chín đỏ, xen trái xanh.'),
    ('vuon', 'vuon-chum-can', D('dot3/IMG_0585.jpg'), None, .5, .5, 'Cận cảnh chùm Robusta chín đỏ dưới tán lá', 'Cận cảnh chùm Robusta chín.'),
    ('vuon', 'vuon-chin-khong-deu', D('dot3/IMG_0239.jpg'), None, .5, .5, 'Bàn tay đỡ những cành cà phê có trái xanh, trái ương và trái chín đỏ', 'Trên một cành, trái chín không đều.'),
    ('vuon', 'vuon-ba-mau', D('dot3/IMG_0243.jpg'), None, .5, .5, 'Hai bàn tay nâng cành cà phê có trái xanh, trái cam và trái đỏ', 'Xanh, cam, đỏ trên cùng một cành.'),
    ('vuon', 'vuon-doc-canh', D('dot3/IMG_0240.jpg'), None, .5, .5, 'Những chùm cà phê chín dần dọc theo cành', 'Chùm trái chín dần dọc cành.'),
    ('vuon', 'vuon-troi-xanh', D('dot3/IMG_0251.jpg'), None, .5, .5, 'Cành cà phê trĩu trái xanh và trái đỏ dưới bầu trời xanh', 'Trái trĩu cành dưới trời xanh.'),
    ('vuon', 'vuon-chin-sam', D('dot3/IMG_0256.jpg'), None, .5, .5, 'Những chùm cà phê chín đỏ sẫm buông dài trên cành', 'Chùm chín đỏ sẫm buông dài.'),
    ('hai', 'hai-nang-chum', D('dot3/IMG_0614.jpg'), None, .5, .5, 'Bàn tay nâng chùm Robusta chín đỏ trên cành', 'Nâng chùm Robusta chín đỏ.'),
    ('hai', 'hai-chum-xen', D('dot3/IMG_0612.jpg'), None, .5, .5, 'Bàn tay đỡ chùm cà phê có trái chín đỏ xen trái vàng và trái xanh', 'Chùm chín đỏ xen trái vàng trên tay.'),
    ('hai', 'hai-gio-trai', D('dot3/IMG_0280.jpg'), None, .5, .5, 'Bàn tay xách giỏ đựng trái cà phê chín đỏ dưới gốc cây', 'Giỏ trái chín vừa hái.'),
    ('hai', 'hai-ao-medili', D('dot3/20261114_110252.jpg'), None, .5, .5, 'Người mặc áo MeDili đứng bên cây cà phê trĩu trái dưới trời xanh', 'Người vườn MeDili bên cây trĩu trái.'),
    ('doi', 'doi-canh-trai', D('dot3/IMG_0479.jpg'), None, .5, .5, 'Cành cà phê chín đỏ phía trước bàn pha nhìn ra đồi', 'Cành chín đỏ trước bàn pha.'),
    ('doi', 'doi-ban-pha', D('dot3/IMG_0490.jpg'), None, .5, .5, 'Bàn pha cà phê với hũ hạt MeDili, phía xa là đồi và hồ', 'Bàn pha nhìn ra đồi và hồ.'),
    ('doi', 'doi-trai-tren-tay', D('dot3/IMG_0493.jpg'), None, .5, .5, 'Bàn tay cầm trái cà phê chín trước bàn pha và đồi xa', 'Trái chín trên tay, đồi xa phía sau.'),
    ('doi', 'doi-espresso', D('dot3/IMG_0488.jpg'), None, .5, .5, 'Ly espresso vừa chiết cạnh khay trái cà phê chín', 'Espresso bên khay trái chín.'),
    ('doi', 'doi-ly-nhieu-lop', D('dot3/IMG_0638.jpg'), 1, .5, .64, 'Ly cà phê nhiều lớp trên bàn gỗ, cạnh hũ hạt MeDili và chùm trái chín', 'Ly cà phê bên chùm trái chín.'),
]

# ảnh nền: tên -> (nguồn, máy tính (tỷ lệ, tâm x, tâm y, rộng ra), điện thoại (...))
BG = {
    'bg-trang-chu': (D('src/IMG_0603.jpg'), (16 / 9, .5, .6, 1920), (3 / 5, .5, .5, 900)),
    'bg-mua-vu': (A('e7526603'), (12 / 5, .5, .5, 1920), (3 / 4, .55, .5, 900)),
    'bg-trong-kho': (A('b75910ab'), (12 / 5, .5, .62, 1920), (3 / 4, .42, .55, 900)),
    'bg-anh-vuon': (A('b922b23f'), (12 / 5, .5, .6, 1920), (4 / 5, .64, .5, 900)),
}

# ---------- ảnh nền toàn khung ----------
PHOTO_CSS = r'''
/* Ảnh nền toàn khung: đầu trang và dải ảnh. Ảnh neo góc dưới phải để logo chìm luôn còn trong khung; lớp phủ nâu cà phê, không đen. */
.phero,.pband{position:relative;isolation:isolate;overflow:hidden;background:#2A1810;color:#FFF3E4}
.phero>picture,.pband>picture{position:absolute;inset:0;z-index:-2;display:block}
.phero>picture img,.pband>picture img{display:block;width:100%;height:100%;max-width:none;object-fit:cover;object-position:100% 100%}
.phero::before,.pband::before{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;
  background:linear-gradient(90deg,rgba(36,20,11,.9) 0%,rgba(36,20,11,.76) 30%,rgba(36,20,11,.34) 58%,rgba(36,20,11,.06) 80%),linear-gradient(0deg,rgba(36,20,11,.32),rgba(36,20,11,0) 34%)}
.ph-in{max-width:1320px;margin:auto;display:grid;align-content:center;min-height:min(86vh,860px);padding-block:56px 64px;
  padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.ph-txt{max-width:610px;min-width:0}
.phero .lgk{display:block;width:min(240px,64vw);height:auto;margin:0 0 14px}
.phero h1{font:800 clamp(2.5rem,5.8vw,4.6rem)/1.07 var(--display);margin:10px 0;color:#FFF3E4;text-wrap:balance;text-shadow:0 2px 22px rgba(24,12,6,.4)}
.pband h2{font:800 clamp(2rem,4.2vw,3.2rem)/1.1 var(--display);margin:8px 0;color:#FFF3E4;text-wrap:balance;text-shadow:0 2px 22px rgba(24,12,6,.4)}
.phero h1 em,.pband h2 em{font-style:normal;color:#F4B47C}
.phero .eye,.pband .eye{color:#F4CC97}
.phero .sub,.pband p.sub{font-size:1.06rem;line-height:1.62;color:rgba(255,243,228,.93);max-width:56ch;margin:0}
.pband .k{color:rgba(255,243,228,.8)}
.phero .btn,.pband .btn{border-color:rgba(255,243,228,.72);color:#FFF3E4;background:rgba(42,24,14,.28)}
.phero .btn:hover,.pband .btn:hover{border-color:#FFF3E4;background:rgba(255,243,228,.14)}
.phero .btn.main,.pband .btn.main{background:#B9442A;border-color:#B9442A;color:#FFF6EC}
.phero .btn.main:hover,.pband .btn.main:hover{background:#CC5536;border-color:#CC5536}
.phero .btn:focus-visible,.pband .btn:focus-visible{outline:3px solid #F4CC97;outline-offset:2px}
.phero.ph-s .ph-in{min-height:clamp(380px,40vw,560px)}
.pband .ph-in{min-height:clamp(400px,42vw,620px)}
.ph-nav{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}
.ph-nav a{display:inline-flex;align-items:baseline;gap:6px;border:1px solid rgba(255,243,228,.6);border-radius:999px;padding:7px 14px;color:#FFF3E4;text-decoration:none;font:600 .9rem var(--body);background:rgba(42,24,14,.3)}
.ph-nav a small{font:700 12px var(--mono);color:#F4CC97}
.ph-nav a:hover{background:rgba(255,243,228,.16);border-color:#FFF3E4}
@media (max-width:820px){
  .phero::before,.pband::before{background:linear-gradient(180deg,rgba(36,20,11,.08) 0%,rgba(36,20,11,.5) 20%,rgba(36,20,11,.82) 40%,rgba(36,20,11,.84) 78%,rgba(36,20,11,.4) 100%)}
  .ph-in,.phero.ph-s .ph-in,.pband .ph-in{min-height:0;align-content:end;padding-block:42vw 104px}
  .phero.ph-s .ph-in,.pband .ph-in{padding-top:34vw}
}
'''


def _bg(name, alt, first=False):
    w, h = _psize(f'{name}.jpg')
    wm, hm = _psize(f'{name}-m.jpg')
    ld = ' fetchpriority="high"' if first else ' loading="lazy"'
    return (f'<picture><source media="(max-width:820px)" srcset="assets/{name}-m.jpg" width="{wm}" height="{hm}">'
            f'<img src="assets/{name}.jpg" alt="{esc(alt)}" width="{w}" height="{h}" decoding="async"{ld}></picture>')


def band(name, alt, eye, h2, sub, cta='', label=''):
    return (f'<section class="pband" aria-label="{esc(label or re.sub("<[^>]+>", "", h2))}">{_bg(name, alt)}<div class="ph-in"><div class="ph-txt">'
            f'<p class="eye">{eye}</p><h2>{h2}</h2><p class="sub">{sub}</p>' + (f'<div class="cta">{cta}</div>' if cta else '') + '</div></div></section>')


def hero(name, alt, inner, cls='phero', first=True):
    return f'<section class="{cls}" aria-label="Đầu trang">{_bg(name, alt, first)}<div class="ph-in"><div class="ph-txt">{inner}</div></div></section>'


def logo_kem():
    return '<img class="lgk" src="assets/logo-kem.png" alt="MeDili Café Di Linh" width="240" height="77">'


# ---------- trang Ảnh vườn ----------
GAL_CSS = r'''
.wrap.av{gap:40px;padding-top:34px}
.gv-grp{display:grid;gap:14px;scroll-margin-top:80px}
.gv-hd{display:grid;gap:4px}
.gv-hd .lead{margin:4px 0 0;max-width:64ch;color:var(--muted)}
.gv-hd .lnks{margin-top:4px}
.gv{columns:4;column-gap:12px}
.gv-i{position:relative;display:block;break-inside:avoid;margin:0 0 12px;border-radius:12px;overflow:hidden;background:var(--tint);border:1px solid var(--rule);transform:translateZ(0)}
.gv-i img{display:block;width:100%;height:auto;aspect-ratio:var(--r);object-fit:cover}
.gv-i:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
@media (prefers-reduced-motion:no-preference){.gv-i img{transition:transform .5s ease}.gv-i:hover img{transform:scale(1.03)}}
@media (max-width:1100px){.gv{columns:3}}
@media (max-width:700px){.gv{columns:2;column-gap:8px}.gv-i{margin-bottom:8px;border-radius:10px}}
.av-note{display:grid;grid-template-columns:auto minmax(0,1fr);gap:12px 16px;align-items:start}
.av-note svg.pi{width:34px;height:34px;color:var(--accent)}
.av-note p{margin:0}
/* xem ảnh lớn */
dialog.lb{position:fixed;inset:0;width:100%;height:100%;max-width:none;max-height:none;margin:0;padding:0;border:0;background:transparent;color:#FFF3E4;overflow:hidden}
dialog.lb::backdrop{background:rgba(26,15,9,.94)}
.lb-f{margin:0;position:absolute;inset:0;display:grid;grid-template-rows:auto auto;align-content:center;justify-items:center;gap:12px;
  padding:max(56px,env(safe-area-inset-top,0px)) 16px max(18px,env(safe-area-inset-bottom,0px))}
.lb-f img{display:block;max-width:min(100%,1600px);max-height:calc(100vh - 190px);max-height:calc(100dvh - 190px);width:auto;height:auto;object-fit:contain;border-radius:8px}
.lb-f figcaption{display:flex;flex-wrap:wrap;gap:4px 14px;justify-content:center;font:500 .95rem/1.4 var(--body);text-align:center;max-width:70ch}
.lb-f figcaption b{font:700 .8rem var(--mono);color:#F4CC97}
.lb button{position:absolute;display:grid;place-items:center;width:46px;height:46px;border-radius:999px;border:1px solid rgba(255,243,228,.6);background:rgba(42,24,14,.55);color:#FFF3E4;cursor:pointer;padding:0}
.lb button svg{width:22px;height:22px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.lb button:hover{background:rgba(255,243,228,.16);border-color:#FFF3E4}
.lb button:focus-visible{outline:3px solid #F4CC97;outline-offset:2px}
.lb .lb-x{top:max(10px,env(safe-area-inset-top,0px));right:max(12px,env(safe-area-inset-right,0px))}
.lb .lb-p,.lb .lb-n{top:50%;transform:translateY(-50%)}
.lb .lb-p{left:max(12px,env(safe-area-inset-left,0px))}.lb .lb-n{right:max(12px,env(safe-area-inset-right,0px))}
@media (max-width:620px){.lb .lb-p,.lb .lb-n{top:auto;bottom:max(14px,env(safe-area-inset-bottom,0px));transform:none}.lb-f{padding-bottom:max(76px,env(safe-area-inset-bottom,0px))}}
'''

GAL_JS = r'''
(()=>{const L=document.getElementById('lb');if(!L||typeof L.showModal!=='function')return;
const items=[...document.querySelectorAll('.gv-i')],im=L.querySelector('img'),cap=L.querySelector('.lb-c'),num=L.querySelector('.lb-k');let i=0,x0=null;
function show(k){i=(k+items.length)%items.length;const a=items[i],t=a.querySelector('img');im.src=a.getAttribute('href');im.alt=t.alt;cap.textContent=a.dataset.cap||t.alt;num.textContent=(i+1)+' / '+items.length;
 [i+1,i-1].forEach(j=>{const b=items[(j+items.length)%items.length];if(b){const p=new Image();p.src=b.getAttribute('href')}})}
items.forEach((a,k)=>a.addEventListener('click',e=>{if(e.metaKey||e.ctrlKey||e.shiftKey||e.button)return;e.preventDefault();show(k);L.showModal()}));
L.querySelector('.lb-x').addEventListener('click',()=>L.close());
L.querySelector('.lb-p').addEventListener('click',()=>show(i-1));
L.querySelector('.lb-n').addEventListener('click',()=>show(i+1));
L.addEventListener('keydown',e=>{if(e.key==='ArrowLeft'){e.preventDefault();show(i-1)}else if(e.key==='ArrowRight'){e.preventDefault();show(i+1)}});
L.addEventListener('click',e=>{if(e.target===L||e.target.classList.contains('lb-f'))L.close()});
L.addEventListener('pointerdown',e=>{x0=e.clientX});
L.addEventListener('pointerup',e=>{if(x0===null)return;const d=e.clientX-x0;x0=null;if(Math.abs(d)>48)show(i+(d<0?1:-1))});
L.addEventListener('close',()=>{im.removeAttribute('src');const a=items[i];if(a)a.focus({preventScroll:true})});
})();
'''

SVG_X = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
SVG_P = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
SVG_N = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'
FILE = 'anh-vuon.html'


def _tile(name, alt, cap):
    w, h = _psize(f'g-{name}-s.jpg')
    r = f'{w / h:.4f}'.rstrip('0').rstrip('.')
    return (f'<a class="gv-i" href="assets/g-{name}.jpg" data-cap="{esc(cap)}" style="--r:{r}">'
            f'<img src="assets/g-{name}-s.jpg" alt="{esc(alt)}" width="{w}" height="{h}" loading="lazy" decoding="async"></a>')


def tiles(names):
    """Ô ảnh lấy theo tên trong GAL, đúng thứ tự truyền vào (dùng lại ở trang Vùng trồng Di Linh)."""
    by = {x[1]: x for x in GAL}
    return ''.join(_tile(n, by[n][6], by[n][7]) for n in names)


def lb_dialog():
    """Khung xem ảnh lớn dùng chung cho mọi trang có lưới ảnh .gv-i (GAL_JS)."""
    return (f'<dialog class="lb" id="lb" aria-label="Xem ảnh lớn"><figure class="lb-f"><img alt=""><figcaption><span class="lb-c"></span><b class="lb-k"></b></figcaption></figure>'
            f'<button class="lb-x" type="button" aria-label="Đóng">{SVG_X}</button><button class="lb-p" type="button" aria-label="Ảnh trước">{SVG_P}</button>'
            f'<button class="lb-n" type="button" aria-label="Ảnh sau">{SVG_N}</button></dialog>')


def counts():
    return {g: sum(1 for x in GAL if x[0] == g) for g, *_ in GROUPS}


def page():
    n = counts()
    nav = ''.join(f'<a href="#{g}">{t} <small>{n[g]}</small></a>' for g, t, *_ in GROUPS)
    top = hero('bg-anh-vuon', 'Trái cà phê chín gom trong lòng bàn tay người hái',
               f'<p class="eye">Ảnh vườn MeDili · {len(GAL)} ảnh</p><h1>Từ cành chín <em>đến sân phơi.</em></h1>'
               '<p class="sub">Mùa vụ cà phê qua từng tấm ảnh: trái chín trên cành, bàn tay hái, máy cày chở bao rời vườn, phơi và xay xát, rồi pha cà phê giữa đồi. Bấm vào ảnh để xem lớn.</p>'
               f'<nav class="ph-nav" aria-label="Nhóm ảnh">{nav}</nav>', cls='phero ph-s')
    body = ''
    for k, (g, t, h2, lead, links) in enumerate(GROUPS, 1):
        tiles = ''.join(_tile(name, alt, cap) for gg, name, src, ratio, fx, fy, alt, cap in GAL if gg == g)
        lk = ''.join(f'<a class="lnk" href="{h}">{x}</a>' for h, x in links)
        body += (f'<section class="gv-grp" id="{g}" aria-labelledby="h-{g}"><div class="gv-hd"><p class="eye">{k:02d} · {t}</p>'
                 f'<h2 class="p-h2" id="h-{g}" style="margin:0">{h2}</h2><p class="lead">{lead}</p><div class="lnks">{lk}</div></div>'
                 f'<div class="gv">{tiles}</div></section>\n')
    body += (f'<section class="box av-note">{icon("ghim")}<div class="p-sec" style="gap:6px"><h2 class="p-h2" style="margin:0;font-size:1.6rem">Muốn ghé vườn <em>hoặc xưởng rang?</em></h2>'
             f'<p>Vườn và xưởng rang ở {ADDR_FARM}. Gọi trước để MeDili hẹn lịch: <span class="sel">{PHONE}</span>.</p>'
             '<p class="note">Ảnh trên trang có logo MeDili. Nếu cần dùng ảnh cho bài viết hay sự kiện, bạn vui lòng liên hệ MeDili.</p>'
             f'<div class="cta"><a class="btn main" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo MeDili</a><a class="btn" href="vung-trong.html">Vùng trồng Di Linh</a><a class="btn" href="cua-hang.html">Chọn cà phê</a></div></div></section>')
    dlg = lb_dialog()
    return doc(FILE, 'Ảnh vườn MeDili',
               'Ảnh mùa vụ cà phê của MeDili: vườn vào mùa, hái bằng tay, máy cày chở bao rời vườn, phơi và xay xát, pha cà phê giữa đồi.',
               body + dlg, css=PHOTO_CSS + GAL_CSS, js=GAL_JS, wrap_cls='wrap av', hero=top)

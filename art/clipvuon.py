# Khối "Clip quay tại vườn MeDili" ở trang Vùng trồng Di Linh (chị Ngân 26/11/2026: bổ sung ảnh và video, rồi "ghép clip lại cho hay").
# Một clip ghép khoảng 40 giây (art/make_montage.py): hoa nở → nắng qua tán → chùm chín → một chùm nhiều độ chín →
# người vườn nhặt cành lá → đồi cà phê trong sương → logo MeDili. Bên cạnh (điện thoại: bên dưới) là danh sách 6 cảnh,
# bấm vào cảnh nào thì clip nhảy tới cảnh đó; cảnh đang chiếu được tô đậm.
# Cách chạy: clip tự chạy (tắt tiếng, lặp lại) khi cuộn tới hơn nửa khung, dừng khi cuộn qua; không tự chạy khi máy bật giảm
# chuyển động hoặc tiết kiệm dữ liệu. Có nút Phát/Dừng và Toàn màn hình (WCAG 2.2.2). Màn hình rộng tải bản 1280×720,
# điện thoại tải bản 854×480 để nhẹ dữ liệu.
from kit import *
from make_montage import chapters, NAME

CAPS = {1: 'Hoa cà phê nở trắng trên cành.', 2: 'Nắng xuyên qua tán cà phê.', 3: 'Những chùm Robusta chín đỏ.',
        4: 'Một chùm, nhiều độ chín.', 5: 'Nhặt cành lá lẫn trong trái trên bạt.', 6: 'Đồi cà phê, sương trên núi xa.'}

CSS = r'''
/* Clip ghép từ vườn: khung 16:9 + danh sách cảnh. Nút tròn góc dưới trái (logo chìm nằm góc dưới phải). */
.vcg-sec{display:grid;gap:14px;scroll-margin-top:80px}
.vm{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:16px;align-items:start}
.vm-f{position:relative;aspect-ratio:16/9;border-radius:16px;overflow:hidden;background:#231812;border:1px solid var(--rule)}
.vm-f video{display:block;width:100%;height:100%;object-fit:cover;cursor:pointer}
.vm-bar{position:absolute;left:0;right:0;bottom:0;height:4px;background:rgba(255,243,228,.22);pointer-events:none}
.vm-bar i{display:block;height:100%;background:#F4B47C;transform-origin:0 50%;transform:scaleX(0);transition:transform .25s linear}
.vc-b{position:absolute;bottom:14px;display:grid;place-items:center;width:44px;height:44px;padding:0;border-radius:999px;
  border:1px solid rgba(255,243,228,.62);background:rgba(42,24,14,.58);color:#FFF3E4;cursor:pointer;transition:background .2s}
.vc-p{left:14px}.vc-x{left:66px}
.vc-b svg{width:19px;height:19px}
.vc-p .i-pa,.vc-p.on .i-pl{display:none}.vc-p.on .i-pa{display:block}
.vc-b .fi{fill:currentColor;stroke:none}.vc-b .st{fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.vc-b:hover{background:#B9442A;border-color:#B9442A}
.vc-b:focus-visible{outline:3px solid #F4CC97;outline-offset:2px}
.vm-ch{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.vm-c{position:relative;display:grid;grid-template-columns:112px minmax(0,1fr);gap:12px;align-items:center;padding:6px;border:1px solid var(--rule);
  border-radius:12px;background:var(--panel);transition:border-color .2s,background .2s}
.vm-c img{display:block;width:112px;height:63px;object-fit:cover;border-radius:8px;background:var(--tint)}
.vm-c button{display:flex;gap:8px;align-items:baseline;min-height:44px;margin:0;padding:4px 2px;border:0;background:none;color:var(--ink);text-align:left;
  font:500 .93rem/1.35 var(--body);cursor:pointer}
.vm-c button::after{content:"";position:absolute;inset:0;border-radius:12px}
.vm-c button b{font:700 .78rem var(--mono);color:var(--accent);flex:none}
.vm-c:hover,.vm-c.on{border-color:var(--accent)}
.vm-c.on{background:var(--tint)}
.vm-c.on button{font-weight:700}
.vm-c button:focus-visible{outline:none}.vm-c button:focus-visible::after{outline:3px solid var(--accent);outline-offset:2px}
@media (max-width:1100px){.vm{grid-template-columns:minmax(0,1fr)}.vm-ch{grid-template-columns:repeat(3,minmax(0,1fr))}
  .vm-c{grid-template-columns:minmax(0,1fr);align-items:start;gap:6px}.vm-c img{width:100%;height:auto;aspect-ratio:16/9}}
@media (max-width:700px){.vc-b{bottom:12px}.vc-p{left:12px}.vc-x{left:62px}
  .vm-ch{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:46%;overflow-x:auto;scroll-snap-type:x mandatory;
  overscroll-behavior-x:contain;padding-bottom:6px}.vm-c{scroll-snap-align:start}}
'''

JS = r'''
(()=>{const v=document.querySelector('.vm video');if(!v)return;v.muted=true;
const f=v.closest('.vm-f'),b=f.querySelector('.vc-p'),x=f.querySelector('.vc-x'),bar=f.querySelector('.vm-bar i');
const C=[...document.querySelectorAll('.vm-c')].map(li=>({li,btn:li.querySelector('button'),t:+li.dataset.t,s:+li.dataset.s}));
const rm=matchMedia('(prefers-reduced-motion: reduce)'),sd=!!(navigator.connection&&navigator.connection.saveData);
const auto=()=>!rm.matches&&!sd;let src=false;
const pick=()=>{if(src)return;src=true;const hd=matchMedia('(min-width: 900px)').matches&&!sd;v.src=hd?v.dataset.hd:v.dataset.sd};
const go=()=>{pick();return v.play().catch(()=>{})};
const sync=()=>{const on=!v.paused;b.classList.toggle('on',on);b.setAttribute('aria-label',on?b.dataset.pa:b.dataset.pl)};
v.addEventListener('play',sync);v.addEventListener('pause',sync);
const mark=()=>{const t=v.currentTime;let k=0;C.forEach((c,i)=>{if(t>=c.s)k=i});C.forEach((c,i)=>{const on=i===k;c.li.classList.toggle('on',on);
 if(on)c.btn.setAttribute('aria-current','true');else c.btn.removeAttribute('aria-current')});
 if(v.duration)bar.style.transform='scaleX('+(t/v.duration).toFixed(4)+')'};
v.addEventListener('timeupdate',mark);v.addEventListener('seeked',mark);
b.addEventListener('click',()=>{if(v.paused){v.dataset.u='';go()}else{v.dataset.u='1';v.pause()}});
v.addEventListener('click',()=>b.click());
x.addEventListener('click',()=>{pick();if(v.requestFullscreen)v.requestFullscreen().then(go).catch(()=>{});else if(v.webkitEnterFullscreen){go();v.webkitEnterFullscreen()}});
v.addEventListener('fullscreenchange',()=>{v.controls=document.fullscreenElement===v});
C.forEach(c=>c.btn.addEventListener('click',()=>{v.dataset.u='';pick();
 const seek=()=>{v.currentTime=c.t;mark()};if(v.readyState>=1)seek();else v.addEventListener('loadedmetadata',seek,{once:true});go()}));
mark();
if('IntersectionObserver' in window){new IntersectionObserver(es=>es.forEach(e=>{
 if(e.isIntersecting&&e.intersectionRatio>=.5){if(auto()&&!v.dataset.u&&v.paused)go()}
 else if(!v.paused&&document.fullscreenElement!==v)v.pause()}),{threshold:[0,.5]}).observe(v)}
})();
'''

SVG_PL = '<svg class="i-pl" viewBox="0 0 24 24" aria-hidden="true"><path class="fi" d="M8 5.5v13l10.5-6.5z"/></svg>'
SVG_PA = '<svg class="i-pa" viewBox="0 0 24 24" aria-hidden="true"><path class="fi" d="M7 5h3.6v14H7zM13.4 5H17v14h-3.6z"/></svg>'
SVG_FS = '<svg viewBox="0 0 24 24" aria-hidden="true"><path class="st" d="M4 9V4h5M15 4h5v5M20 15v5h-5M9 20H4v-5"/></svg>'


def section():
    items = ''.join(f'<li class="vm-c" data-t="{seek}" data-s="{start}"><img src="assets/{NAME}-c{ch}.jpg" alt="" width="384" height="216" loading="lazy" decoding="async">'
                    f'<button type="button"><b>{ch:02d}</b><span>{CAPS[ch]}</span></button></li>' for ch, seek, start in chapters())
    label = ('Clip ghép một mùa ở vườn MeDili: hoa cà phê nở, nắng qua tán, những chùm Robusta chín, người vườn nhặt cành lá trên bạt '
             'và đồi cà phê trong sương')
    return (f'<section class="vcg-sec" id="clip-vuon" aria-labelledby="h-clip-vuon"><div class="gv-hd"><p class="eye">Clip quay tại vườn MeDili</p>'
            f'<h2 class="p-h2" id="h-clip-vuon" style="margin:0">Một mùa <em>ở vườn Di Linh.</em></h2>'
            f'<p class="lead">Hoa nở trắng cành, chùm trái chín không đều, người vườn nhặt cành lá trên bạt và đồi cà phê trong sương. '
            f'Một clip 40 giây ghép từ sáu cảnh quay tại vườn, không có tiếng. Bấm vào một cảnh để xem lại cảnh đó.</p></div>'
            f'<div class="vm"><div class="vm-f">'
            f'<video muted loop playsinline preload="none" poster="assets/{NAME}.jpg" width="1280" height="720" aria-label="{esc(label)}" '
            f'data-hd="assets/{NAME}-720.mp4" data-sd="assets/{NAME}-480.mp4"><source src="assets/{NAME}-480.mp4" type="video/mp4"></video>'
            f'<span class="vm-bar" aria-hidden="true"><i></i></span>'
            f'<button class="vc-b vc-p" type="button" aria-label="Phát clip" data-pl="Phát clip" data-pa="Dừng clip">{SVG_PL}{SVG_PA}</button>'
            f'<button class="vc-b vc-x" type="button" aria-label="Xem toàn màn hình">{SVG_FS}</button></div>'
            f'<ol class="vm-ch" aria-label="Các cảnh trong clip">{items}</ol></div></section>')

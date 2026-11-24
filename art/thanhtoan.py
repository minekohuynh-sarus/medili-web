# Trang Thanh toán MeDili (24/11/2026, chị Ngân yêu cầu "làm trang liên kết thanh toán"):
# - Khách đặt hàng trong Giỏ hàng hoặc Phòng chọn mua rồi trả ngay: chuyển khoản bằng mã VietQR (chuẩn Napas 247).
#   App ngân hàng, MoMo, ZaloPay đều quét được; số tiền và nội dung (mã đơn) tự điền.
# - Tiền mặt khi nhận hàng (COD), hoặc chờ MeDili báo giá. Apple Pay cần hợp đồng cổng thanh toán (vd. OnePay), chưa làm.
# - Link thanh toán: thanh-toan.html?ma=MD24113520&tien=475200 (cuối trang có ô để MeDili tự tạo link, gửi khách qua Zalo).
#   pt=cod (trả tiền mặt khi nhận), pt=sau (Phòng chọn mua: MeDili xác nhận rồi thu), pt=bg (giỏ có dòng hỏi giá).
# - Mã QR dựng ngay trên trình duyệt bằng thư viện qrcode-generator (MIT, assets/qrcode.js), không gửi dữ liệu ra ngoài.
# - Tài khoản nhận tiền: kit.BANK.
from kit import *
from pages_a import head

FILE = 'thanh-toan.html'


def page():
    hero = head('Thanh toán', 'Thanh toán <em>cho MeDili.</em>',
                'Quét mã QR bằng app ngân hàng, MoMo hoặc ZaloPay. Số tiền và nội dung chuyển khoản được điền sẵn. '
                'Tiền chuyển vào tài khoản Công ty TNHH Thực phẩm DSunfood, đơn vị phân phối MeDili.')
    hero = hero.replace('<h1>', '<h1 id="tt-h">', 1).replace('<p class="lead">', '<p class="lead" id="tt-lead">', 1)
    body = hero + f'''
<section class="tt" aria-label="Thanh toán">
 <div class="tt-col">
  <div class="box tt-ok" id="tt-done" hidden>
   <p class="eye" id="tt-d-eye">Đã gửi đơn</p>
   <h2 class="p-h2" id="tt-d-h"></h2>
   <p id="tt-d-p"></p>
   <p class="tt-sum" id="tt-d-amt" hidden></p>
   <div class="cta" style="margin:0"><a class="btn main" id="tt-zl2" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo cho MeDili</a><button type="button" class="btn" id="tt-sw" hidden>Chuyển khoản ngay</button></div>
  </div>
  <div class="box tt-card" id="tt-ck">
   <div class="tt-top"><p class="eye" id="tt-eye">Chuyển khoản · quét mã QR</p><p class="tt-big" id="tt-big" hidden><span>Số tiền</span><b id="tt-amt"></b></p></div>
   <div class="tt-apps" id="tt-apps" hidden>
    <p class="tt-apt"><b>Chọn app ngân hàng để trả</b><small>App ghi “Điền sẵn” mở ra với số tiền và nội dung đã điền. App khác: mở app, chọn quét mã rồi chọn ảnh mã QR đã lưu.</small></p>
    <div class="tt-apl" id="tt-apl"></div>
    <details class="tt-more"><summary>Ngân hàng khác</summary><div class="tt-apl" id="tt-apl2"></div></details>
   </div>
   <div class="tt-grid">
    <figure class="tt-qr"><div class="tt-qrbox" id="tt-qr" role="img" aria-label="Mã QR chuyển khoản cho MeDili"></div>
     <figcaption>App ngân hàng · MoMo · ZaloPay</figcaption></figure>
    <div class="tt-r"><dl class="tt-kv">
     <div><dt>Ngân hàng</dt><dd id="tt-bank"></dd></div>
     <div><dt>Số tài khoản</dt><dd><b id="tt-acc"></b><button type="button" class="tt-cp" data-cp="acc">Chép</button></dd></div>
     <div><dt>Tên tài khoản</dt><dd id="tt-name"></dd></div>
     <div id="tt-r-amt" hidden><dt>Số tiền</dt><dd><b id="tt-amt2"></b><button type="button" class="tt-cp" data-cp="amt">Chép</button></dd></div>
     <div id="tt-r-nd" hidden><dt>Nội dung</dt><dd><b id="tt-nd"></b><button type="button" class="tt-cp" data-cp="nd">Chép</button></dd></div>
    </dl>
    <div class="cta tt-act"><button type="button" class="btn main" id="tt-save">Lưu ảnh mã QR</button><a class="btn" id="tt-zl" href="{ZALO}" target="_blank" rel="noopener">Báo đã chuyển khoản</a></div>
    <p class="tt-st" id="tt-st" role="status" aria-live="polite"></p>
   </div>
   </div>
   <ol class="tt-steps">
    <li>Mở app ngân hàng, MoMo hoặc ZaloPay, chọn quét mã QR.</li>
    <li>Quét mã trên màn hình. Nếu đang xem trên chính điện thoại đó, bấm Lưu ảnh mã QR rồi chọn ảnh vừa lưu trong mục quét mã của app.</li>
    <li>Kiểm tra tên tài khoản, số tiền và nội dung, rồi xác nhận chuyển.</li>
    <li>Bấm Báo đã chuyển khoản để MeDili đối chiếu và giao hàng sớm.</li>
   </ol>
  </div>
  <div class="box" id="tt-off" hidden><p class="eye">Chuyển khoản</p><p style="margin:0">Số tài khoản nhận tiền đang được cập nhật. Bạn nhắn Zalo {PHONE} để nhận thông tin chuyển khoản, hoặc chọn trả tiền mặt khi nhận hàng.</p></div>
 </div>
 <aside class="tt-col">
  <div class="box" id="tt-don" hidden><p class="eye">Đơn của bạn</p><pre class="msg" id="tt-msg" style="margin-top:8px"></pre></div>
  <div class="box tt-note"><p class="eye">Lưu ý khi thanh toán</p>
   <ul>
    <li>MeDili chỉ nhận chuyển khoản vào tài khoản Công ty TNHH Thực phẩm DSunfood ghi trên trang này.</li>
    <li>Phí giao: miễn phí cho đơn từ 10 kg. Đơn dưới 10 kg, MeDili báo phí giao và thu sau.</li>
    <li>Cần hóa đơn VAT: ghi tên công ty, mã số thuế, địa chỉ và email nhận hóa đơn trong ghi chú đơn, hoặc nhắn Zalo.</li>
    <li>Hoàn tiền trong 5 ngày theo <a class="lnk" href="chinh-sach.html#hoan-tien">Chính sách hoàn tiền</a>.</li>
    <li>Mã QR dùng với app ngân hàng và ví điện tử tại Việt Nam. Khách ở nước ngoài có thể trả khi nhận hàng hoặc nhắn MeDili.</li>
   </ul>
   <p class="note">Hỗ trợ: Zalo, điện thoại {PHONE}, email {EMAIL}.</p></div>
 </aside>
</section>
<details class="box tt-mk" id="tt-mk"><summary>Dành cho MeDili: tạo link thanh toán gửi khách</summary>
 <p class="note" style="margin-top:8px">Nhập mã đơn và số tiền đã chốt với khách. Link mở đúng trang này, mã QR có sẵn số tiền và nội dung.</p>
 <div class="tt-mkf"><label>Mã đơn<input id="mk-ma" maxlength="20" autocomplete="off" spellcheck="false"></label><label>Số tiền (đ)<input id="mk-tien" inputmode="numeric" autocomplete="off"></label></div>
 <p class="tt-st" id="mk-st" role="status" aria-live="polite"></p>
 <div class="cta" style="margin:0"><button type="button" class="btn main" id="mk-go">Tạo link</button></div>
 <div id="mk-out" hidden><pre class="msg" id="mk-link" data-sel style="margin-top:10px"></pre>
  <div class="cta" style="margin:10px 0 0"><button type="button" class="btn" id="mk-c1">Chép link</button><button type="button" class="btn" id="mk-c2">Chép tin nhắn gửi khách</button><a class="btn" id="mk-open" target="_blank" rel="noopener">Mở thử</a></div></div>
</details>
<script src="assets/qrcode.js"></script>
'''
    js = 'const B=' + json.dumps(BANK, ensure_ascii=False) + ';\n' + JS
    desc = ('Thanh toán đơn cà phê MeDili: chuyển khoản bằng mã QR (app ngân hàng, MoMo, ZaloPay) với số tiền và mã đơn điền sẵn, '
            'hoặc trả tiền mặt khi nhận hàng.')
    out = doc(FILE, 'Thanh toán · MeDili', desc, body, css=CSS, js=js, wrap_cls='wrap pg', contact=False)
    return out.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex">', 1)


JS = r'''
(()=>{const $=id=>document.getElementById(id),P=new URLSearchParams(location.search);
 const MA=(P.get('ma')||'').toUpperCase().replace(/[^A-Z0-9]/g,'').slice(0,20),TIEN=Math.min(999999999,+String(P.get('tien')||'').replace(/\D/g,'')||0),PT=P.get('pt')||'';
 const fmt=n=>Math.round(n).toLocaleString('vi-VN').replace(/,/g,'.'),money=n=>fmt(n)+' đ';
 const st=(id,t)=>{const e=$(id);e.textContent=t;clearTimeout(e._t);e._t=setTimeout(()=>{e.textContent=''},6000)};
 const copy=async(t,id,ok)=>{try{await navigator.clipboard.writeText(t);if(ok)st(id,ok);return true}catch(e){st(id,'Không chép được tự động. Hãy chọn và chép thủ công.');return false}};
 // VietQR theo chuẩn EMVCo của Napas: 38 = tài khoản nhận (A000000727, mã ngân hàng, số tài khoản, QRIBFTTA), 54 = số tiền, 62/08 = nội dung
 const TLV=(i,v)=>i+String(v.length).padStart(2,'0')+v;
 const crc=s=>{let c=0xFFFF;for(let i=0;i<s.length;i++){c^=s.charCodeAt(i)<<8;for(let j=0;j<8;j++)c=(c&0x8000)?((c<<1)^0x1021)&0xFFFF:(c<<1)&0xFFFF}return c.toString(16).toUpperCase().padStart(4,'0')};
 const payload=(amt,nd)=>{const m=TLV('00','A000000727')+TLV('01',TLV('00',B.bin)+TLV('01',B.acc))+TLV('02','QRIBFTTA');
  const s=TLV('00','01')+TLV('01',amt?'12':'11')+TLV('38',m)+TLV('53','704')+(amt?TLV('54',String(amt)):'')+TLV('58','VN')+(nd?TLV('62',TLV('08',nd)):'')+'6304';return s+crc(s)};
 // Mở app ngân hàng qua dịch vụ deeplink của VietQR (dl.vietqr.io, Casso). Năm app đầu tự điền số tiền, nội dung (danh sách vietqr.io/deeplink/bank-apps, 11/2026).
 const APPS=[['mb','MB Bank',1],['icb','VietinBank',1],['bidv','BIDV',1],['acb','ACB',1],['ocb','OCB',1],['vcb','Vietcombank'],['tcb','Techcombank'],['vpb','VPBank'],['vba','Agribank']];
 const APPS2=[['tpb','TPBank'],['hdb','HDBank'],['vib-2','VIB'],['shb','SHB'],['lpb','LPBank'],['seab','SeABank'],['cake','Cake'],['timo','Timo'],['scb','SCB'],['eib','Eximbank'],['nab','Nam A Bank'],['abb','ABBank'],['shbvn','Shinhan Bank'],['wvn','Woori Bank'],['klb','KienlongBank'],['bvb','BAOVIET Bank'],['vab','Vietbank'],['ncb','NCB'],['pvcb','PVcomBank'],['coopbank','Co-opBank'],['mbv','MBV'],['pbvn','Public Bank'],['sgicb','Saigonbank'],['cimb','CIMB'],['acb-biz','ACB ONE Biz']];
 const MOB=/Android|iPhone|iPad|iPod/i.test(navigator.userAgent)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);
 function apps(amt,nd){if(!MOB||!amt||!nd||!B.code)return;const q=new URLSearchParams({ba:B.acc+'@'+B.code,am:String(amt),tn:nd,bn:B.name,url:location.href}).toString().replace('%40','@');
  // Trang nằm trong khung (bản xem trước): mở tab mới để app ngân hàng bật được. Trên medili.vn mở ngay tab này để quay lại đúng trang.
  const TG=(()=>{try{return window.top!==window.self}catch(e){return true}})()?' target="_blank"':'';
  const btn=([id,n,f])=>'<a class="tt-ap'+(f?' fill':'')+'" href="https://dl.vietqr.io/pay?app='+id+'&'+q+'" rel="noopener"'+TG+'><b>'+n+'</b><small>'+(f?'Điền sẵn':'Mở app')+'</small></a>';
  $('tt-apl').innerHTML=APPS.map(btn).join('');$('tt-apl2').innerHTML=APPS2.map(btn).join('');$('tt-apps').hidden=false}
 let Q=null;
 function draw(amt,nd){if(typeof qrcode!=='function'){$('tt-qr').textContent='';return}
  const q=qrcode(0,'M');q.addData(payload(amt,nd),'Byte');q.make();const n=q.getModuleCount(),z=4;let d='';
  for(let r=0;r<n;r++)for(let c=0;c<n;c++)if(q.isDark(r,c))d+='M'+(c+z)+' '+(r+z)+'h1v1h-1z';
  $('tt-qr').innerHTML='<svg viewBox="0 0 '+(n+2*z)+' '+(n+2*z)+'" shape-rendering="crispEdges" aria-hidden="true"><rect width="100%" height="100%" fill="#fff"/><path d="'+d+'" fill="#4A2C1A"/></svg>';
  Q={q,n,amt,nd};$('tt-qr').dataset.payload=payload(amt,nd)}
 function showCK(amt,nd){$('tt-ck').hidden=false;$('tt-bank').textContent=B.bank;$('tt-acc').textContent=B.acc;$('tt-name').textContent=B.name;
  $('tt-big').hidden=!amt;$('tt-r-amt').hidden=!amt;$('tt-r-nd').hidden=!nd;
  if(amt){$('tt-amt').textContent=money(amt);$('tt-amt2').textContent=money(amt)}if(nd)$('tt-nd').textContent=nd;
  $('tt-eye').textContent=amt?'Chuyển khoản · quét mã QR':'Tài khoản nhận tiền của MeDili';$('tt-zl').hidden=!nd;draw(amt,nd);apps(amt,nd)}
 const BANK=!!(B.bin&&B.acc),O=MA?MDO.get(MA):null;
 if(O&&O.t){$('tt-don').hidden=false;$('tt-msg').textContent=O.t}
 $('tt-ck').hidden=true;
 if(MA&&(PT==='cod'||PT==='sau'||PT==='bg')){
  $('tt-h').innerHTML=`Đã gửi <em>đơn ${MA}.</em>`;$('tt-lead').hidden=true;$('tt-done').hidden=false;$('tt-d-eye').textContent='Đơn '+MA;
  if(PT==='cod'){$('tt-d-h').innerHTML='Trả tiền mặt <em>khi nhận hàng.</em>';$('tt-d-p').textContent='MeDili gọi hoặc nhắn Zalo trong 60 phút (6:30–22:30) để xác nhận đơn, phí giao và thời gian giao. Bạn trả tiền mặt cho người giao khi nhận hàng.'}
  else if(PT==='sau'){$('tt-d-h').innerHTML='MeDili sẽ <em>xác nhận đơn.</em>';$('tt-d-p').textContent='MeDili gọi hoặc nhắn Zalo trong 60 phút (6:30–22:30) để xác nhận giá, phí giao và thời hạn thanh toán. Bạn trả khi nhận hàng, hoặc theo thời hạn ghi trong xác nhận đơn.'}
  else{$('tt-d-h').innerHTML='Chờ MeDili <em>báo giá.</em>';$('tt-d-p').textContent='Đơn có dòng cà phê chưa niêm yết giá. MeDili báo giá qua Zalo trong 60 phút (6:30–22:30), rồi gửi link thanh toán cho bạn.'}
  if(TIEN&&PT!=='bg'){$('tt-d-amt').hidden=false;$('tt-d-amt').innerHTML='Số tiền dự kiến: <b>'+money(TIEN)+'</b>, chưa gồm phí giao.';
   if(BANK){$('tt-sw').hidden=false;$('tt-sw').addEventListener('click',()=>{$('tt-sw').hidden=true;showCK(TIEN,MA);$('tt-ck').scrollIntoView({behavior:'smooth',block:'start'})})}}}
 else if(MA&&TIEN){$('tt-h').innerHTML=`Thanh toán <em>đơn ${MA}.</em>`;
  if(O)$('tt-lead').textContent='Đã gửi đơn cho MeDili. Bạn chuyển khoản để hoàn tất, MeDili đối chiếu rồi giao hàng.';
  if(BANK)showCK(TIEN,MA);else $('tt-off').hidden=false}
 else{if(BANK)showCK(0,'');else $('tt-off').hidden=false}
 document.querySelectorAll('[data-cp]').forEach(b=>b.addEventListener('click',async()=>{const k=b.dataset.cp,t=k==='acc'?B.acc:k==='amt'?String(TIEN):MA;
  if(await copy(t,'tt-st')){const o=b.textContent;b.textContent='Đã chép';setTimeout(()=>{b.textContent=o},2000)}}));
 const zmsg=()=>`Chào MeDili, mình đã chuyển khoản ${money(TIEN)} cho đơn ${MA}.`+(O&&O.t?'\n\n'+O.t:'');
 $('tt-zl').addEventListener('click',()=>copy(zmsg(),'tt-st','Đã chép tin nhắn. Dán vào Zalo MeDili rồi gửi kèm ảnh chụp giao dịch.'));
 $('tt-zl2').addEventListener('click',()=>copy(`Chào MeDili, mình vừa gửi đơn ${MA}.`+(O&&O.t?'\n\n'+O.t:''),'tt-st','Đã chép nội dung đơn. Dán vào Zalo MeDili rồi gửi.'));
 // lưu ảnh mã QR để quét từ thư viện ảnh khi xem trên chính điện thoại trả tiền
 function png(){const {q,n,amt,nd}=Q,s=12,z=4,W=(n+2*z)*s,H=W+(amt?168:128),cv=document.createElement('canvas');cv.width=W;cv.height=H;const g=cv.getContext('2d');
  g.fillStyle='#fff';g.fillRect(0,0,W,H);g.fillStyle='#4A2C1A';for(let r=0;r<n;r++)for(let c=0;c<n;c++)if(q.isDark(r,c))g.fillRect((c+z)*s,(r+z)*s,s,s);
  g.textAlign='center';let y=W+8;const line=(t,f)=>{g.font=f;y+=parseInt(f.split(' ')[1],10)+12;g.fillText(t,W/2,y,W-40)};
  if(amt)line(money(amt)+(nd?' · '+nd:''),'700 34px system-ui,sans-serif');line(B.name,'600 26px system-ui,sans-serif');line(B.bank+' · '+B.acc,'500 26px system-ui,sans-serif');
  return new Promise(r=>cv.toBlob(r,'image/png'))}
 $('tt-save').addEventListener('click',async()=>{if(!Q)return;const b=await png();if(!b)return;const fn='MeDili-'+(Q.nd||'QR')+'.png';
  try{const f=new File([b],fn,{type:'image/png'});if(navigator.canShare&&navigator.canShare({files:[f]})&&/Android|iPhone|iPad/i.test(navigator.userAgent)){await navigator.share({files:[f]});return}}catch(e){if(e&&e.name==='AbortError')return}
  const a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=fn;document.body.append(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},4000);
  st('tt-st','Đã lưu ảnh mã QR. Mở app ngân hàng, chọn quét mã rồi chọn ảnh này.')});
 // MeDili tạo link thanh toán gửi khách (chỉ hiện khi mở trang Thanh toán không kèm mã đơn)
 if(MA)$('tt-mk').hidden=true;let MK=null;$('mk-ma').value=MDO.code();
 $('mk-go').addEventListener('click',()=>{const ma=$('mk-ma').value.toUpperCase().replace(/[^A-Z0-9]/g,'').slice(0,20),tien=Math.min(999999999,+$('mk-tien').value.replace(/\D/g,'')||0);
  if(!ma||!tien){st('mk-st','Nhập mã đơn và số tiền.');return}
  const u=location.origin+location.pathname+'?ma='+ma+'&tien='+tien;MK={u,ma,tien};$('mk-link').textContent=u;$('mk-open').href=u;$('mk-out').hidden=false});
 $('mk-c1').addEventListener('click',()=>MK&&copy(MK.u,'mk-st','Đã chép link.'));
 $('mk-c2').addEventListener('click',()=>MK&&copy(`MeDili gửi bạn link thanh toán đơn ${MK.ma}, số tiền ${money(MK.tien)}: ${MK.u}`,'mk-st','Đã chép tin nhắn.'));
})();
'''

CSS = r'''
.tt{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:22px;align-items:start;margin-top:8px}
.tt-col{display:grid;gap:16px;min-width:0}
.tt-card{display:grid;gap:14px}
.tt-top{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:6px 16px}
.tt-big{margin:0;display:grid;justify-items:end}
.tt-big span{font-size:.8rem;color:var(--muted)}
.tt-big b{font:800 clamp(1.6rem,4vw,2.1rem)/1.1 var(--mono);color:var(--accent)}
.tt-grid{display:grid;grid-template-columns:minmax(0,250px) minmax(0,1fr);gap:18px;align-items:start}
.tt-apps{display:grid;gap:10px;padding-bottom:14px;border-bottom:1px dashed var(--rule)}
.tt-apt{margin:0;display:grid;gap:3px}
.tt-apt small{color:var(--muted);font-size:.82rem}
.tt-apl{display:grid;grid-template-columns:repeat(auto-fill,minmax(96px,1fr));gap:7px}
.tt-ap{display:grid;gap:1px;padding:8px 7px 8px 9px;border:1px solid var(--rule);border-radius:12px;background:var(--bg);color:var(--ink);text-decoration:none;min-width:0}
.tt-ap b{font-size:.78rem;letter-spacing:-.01em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tt-ap small{font-size:.74rem;color:var(--muted)}
.tt-ap.fill small{color:var(--accent);font-weight:700}
.tt-ap:hover,.tt-ap:focus-visible{border-color:var(--accent)}
.tt-more summary{cursor:pointer;font-weight:600;font-size:.9rem;margin:2px 0 8px}
.tt-qr{margin:0;display:grid;gap:6px;justify-items:center}
.tt-qrbox{width:100%;max-width:250px;aspect-ratio:1;background:#fff;border-radius:14px;border:1px solid var(--rule);padding:6px}
.tt-qrbox svg{display:block;width:100%;height:100%}
.tt-qr figcaption{font-size:.78rem;color:var(--muted);text-align:center}
.tt-kv{margin:0;display:grid;gap:8px}
.tt-kv>div{display:grid;gap:2px;border-bottom:1px dashed var(--rule);padding-bottom:7px}
.tt-kv>div:last-child{border-bottom:0;padding-bottom:0}
.tt-kv dt{font-size:.76rem;color:var(--muted);letter-spacing:.02em}
.tt-kv dd{margin:0;display:flex;align-items:center;justify-content:space-between;gap:10px;font-weight:600;overflow-wrap:anywhere}
.tt-kv dd b{font:700 1rem var(--mono)}
.tt-cp{flex:none;font:700 .74rem var(--body);border:1px solid var(--rule);background:var(--tint);color:var(--accent);border-radius:999px;padding:5px 11px;cursor:pointer}
.tt-cp:hover{border-color:var(--accent)}
.tt-r{display:grid;gap:12px;min-width:0}
.tt-act{margin:0}
.tt-st{margin:0;min-height:1.2em;font-size:.86rem;font-weight:600;color:var(--accent)}
.tt-steps{margin:0;padding-left:1.2em;display:grid;gap:6px;font-size:.9rem}
.tt-note ul{margin:8px 0 10px;padding-left:1.1em;display:grid;gap:7px;font-size:.9rem}
.tt-ok{display:grid;gap:10px;border-color:var(--accent)}
.tt-ok .p-h2{margin:0}
.tt-ok p{margin:0}
.tt-sum b{font:700 1.05rem var(--mono);color:var(--accent)}
.tt-mk{margin-top:22px}
.tt-mk summary{cursor:pointer;font-weight:700}
.tt-mkf{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:12px 0 8px}
.tt-mkf label{display:grid;gap:4px;font-size:.86rem;font-weight:600}
.tt-mkf input{font:600 1rem var(--mono);padding:9px 11px;border:1px solid var(--rule);border-radius:10px;background:var(--bg);color:var(--ink);min-width:0}
@media (max-width:900px){.tt{grid-template-columns:minmax(0,1fr)}}
@media (max-width:560px){.tt-card{padding:16px 14px}.tt-grid{grid-template-columns:minmax(0,1fr)}.tt-qrbox{max-width:280px}.tt-big{justify-items:start}.tt-mkf{grid-template-columns:minmax(0,1fr)}}
'''

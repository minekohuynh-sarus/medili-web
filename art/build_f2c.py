# Dựng trang "Từ vườn đến ly" (farm to cup) và gắn vào site MeDili
import os, re, json, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import svgs as S

BASE = os.path.join(HERE, '..', 'site-new')      # bản đang chạy, đã có trang Giải phẫu
LIVE = os.path.join(HERE, '..', 'site-live')
OUT = os.path.join(HERE, '..', 'site-new2')
os.makedirs(OUT, exist_ok=True)
rd = lambda f: open(os.path.join(BASE, f), encoding='utf8').read()

PAGE = 'tu-vuon-den-ly.html'
NAVLBL = 'Từ vườn đến ly'

# giá và mô hình
GX = 83600        # nhân xô Lâm Đồng 7/11/2026, Báo Lào Cai
GR = 252000       # sỉ cấp 1 Phin Robusta Classic
GL = 35000        # giá ly ví dụ
YIELD = .95 * .84  # lọc hạt lỗi, hao khi rang
FRESH = .18       # trái tươi ra nhân xanh

ICON = {
 'vuon': '<path d="M12 21v-6"/><circle cx="12" cy="9" r="6"/><circle cx="10" cy="8" r="1.1" class="fi"/><circle cx="14" cy="10.5" r="1.1" class="fi"/><circle cx="11" cy="12" r="1.1" class="fi"/>',
 'can': '<path d="M12 4v15M6 20h12M5 7h14"/><path d="M5 7l-3 6h6zM19 7l-3 6h6z"/>',
 'nha': '<path d="M3 20V10l5 3v-3l5 3V5h4l2 15z"/><path d="M2 20h20"/>',
 'soche': '<path d="M12 3s5 6 5 10a5 5 0 0 1-10 0c0-4 5-10 5-10z"/><path d="M10 14a2 2 0 0 0 2 2"/>',
 'rang': '<circle cx="11" cy="12" r="6"/><path d="M11 6V3M17 12h4M5 21h12M9 9.5c1.5 1 2 3.5 4 5"/>',
 'xe': '<path d="M2 7h12v9H2zM14 10h4l3 3v3h-7"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
 'ly': '<path d="M5 9h11v5a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5z"/><path d="M16 11h2a2 2 0 0 1 0 4h-2M8 3v3M11 3v3"/>',
 'nguoi': '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>',
}
icon = lambda k, cls='ic': f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICON[k]}</svg>'

LANE_A = [('vuon', 'Nông hộ', 'Trồng, hái, phơi, bán nhân xô theo giá ngày', 'f', 1),
          ('can', 'Thương lái, đại lý', 'Gom hàng từ nhiều hộ, cân và trả tiền', 'm', 0),
          ('nha', 'Nhà máy, xuất khẩu', 'Sàng, phân loại, đánh bóng, đóng bao', 'm', 0),
          ('rang', 'Nhà rang', 'Rang, đóng gói, gắn thương hiệu', 'm', 0),
          ('ly', 'Quán', 'Pha và phục vụ', 'q', 0),
          ('nguoi', 'Người uống', 'Trả tiền một ly', '', 0)]
LANE_B = [('vuon', 'Vườn MeDili', 'Trồng Robusta Cà Sẻ, hái chọn, ghi mã lô', 'f', 1),
          ('soche', 'Sơ chế', 'Natural, Honey, Washed, lên men men bia và trái cây', 'm', 1),
          ('rang', 'Xưởng rang', 'Sàng tuyển, 8 cấp độ rang', 'm', 1),
          ('xe', 'Phân phối', 'DSunfood, 143 Phạm Văn Hai, TP.HCM', 'm', 0),
          ('ly', 'Quán, gia đình', 'Pha theo công thức MeDili', 'q', 0),
          ('nguoi', 'Người uống', 'Đọc số lô, ngày rang trên thẻ túi', '', 0)]


def lane(nodes):
    out = []
    n = len(nodes)
    for i, (ic, t, d, seg, dl) in enumerate(nodes):
        cls = ['nd']
        if dl:
            cls.append('dl')
            if i == 0 or not nodes[i - 1][4]: cls.append('dl0')
            if i == n - 1 or not nodes[i + 1][4]: cls.append('dl1')
        tag = '<em>Di Linh</em>' if dl else '<em class="ph" aria-hidden="true">Di Linh</em>'
        segattr = f' data-seg="{seg}" tabindex="0" role="button"' if seg else ''
        out.append(f'<li class="{" ".join(cls)}"{segattr}>{icon(ic)}<div>{tag}<b>{t}</b><span>{d}</span></div></li>')
    return ''.join(out)


def fm(n):
    return f'{round(n):,}'.replace(',', '.')


def model(gx=GX, g=25, gr=GR, gl=GL):
    green = g / YIELD
    farm = green * gx / 1000
    coffee = g * gr / 1000
    return dict(green=green, fresh=green / FRESH, farm=farm, mid=coffee - farm, cafe=gl - coffee, coffee=coffee,
                cups=YIELD * 1000 / g, sales=YIELD * 1000 / g * gl)


M = model()
pct = lambda v: ('%.1f' % (v / GL * 100)).replace('.', ',')

suc = open(os.path.join(LIVE, 'suc-khoe.html'), encoding='utf8').read()
SHARED = re.findall(r'<style>(.*?)</style>', suc, flags=re.S)[1]
FONTS = re.search(r'<link rel="preconnect" href="https://fonts.googleapis.com">\s*<link rel="preconnect"[^>]*>\s*<link rel="stylesheet"[^>]*>', suc).group(0)

NAV_RE = re.compile(r'(<a href="suc-khoe\.html"[^>]*>Sức khỏe</a>)')


def nav(html, current=False):
    if 'href="' + PAGE + '"' in html:
        return html
    link = f'<a href="{PAGE}" class=on aria-current=page>{NAVLBL}</a>' if current else f'<a href="{PAGE}">{NAVLBL}</a>'
    html, n = NAV_RE.subn(r'\1' + link, html, count=1)
    assert n == 1
    return html


MNAV = re.search(r'<div class="mnav">.*?</div></div>', rd('trai-ca-phe.html'), flags=re.S).group(0)
MNAV = MNAV.replace(' class=on aria-current=page', '')
MNAV = nav(MNAV, current=True)

PAGE_CSS = '''
/* Trang Từ vườn đến ly: hai chuỗi so sánh ở khung trái, máy tính tiền một ly ở khung phải, bốn dấu hiệu và phép tính bên dưới. */
:root{--moss:#8D4E22;--good:#8D4E22;--seg-f:#B49A63;--seg-m:#B8894A;--seg-q:#E8D6B8;--band:#E9D2A6}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--moss:#E2A774;--good:#E2A774;--seg-q:#5A4636;--band:#4A3624}}
:root[data-theme="dark"]{--moss:#E2A774;--good:#E2A774;--seg-q:#5A4636;--band:#4A3624}
a{color:var(--accent)}
.lanes{display:grid;gap:22px;margin-top:12px}
.lh{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;margin-bottom:8px}
.lh b{font:800 1.35rem/1.1 var(--display)}
.lh span{color:var(--muted);font-size:.88rem}
.chain{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,minmax(0,1fr))}
.nd{position:relative;display:grid;gap:6px;align-content:start;padding:12px 12px 12px 14px;min-width:0;border-radius:0}
.nd+.nd::before{content:"";position:absolute;left:-6px;top:30px;width:10px;height:10px;border-top:2px solid var(--muted);border-right:2px solid var(--muted);transform:rotate(45deg);opacity:.7}
.nd.dl{background:var(--band)}
.nd.dl0{border-radius:12px 0 0 12px}.nd.dl1{border-radius:0 12px 12px 0}.nd.dl0.dl1{border-radius:12px}
.nd[data-seg]{cursor:pointer}
.nd[data-seg]:hover .ic,.nd.on .ic{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.nd:focus-visible{outline:3px solid var(--moss);outline-offset:2px}
.ic{width:44px;height:44px;padding:9px;border-radius:50%;border:1.5px solid var(--ink);background:var(--panel);color:var(--ink);fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round;transition:background-color .2s,color .2s}
.ic .fi{fill:var(--accent);stroke:none}.nd.on .ic .fi,.nd[data-seg]:hover .ic .fi{fill:var(--on-accent)}
.nd em.ph{visibility:hidden}
.nd em{display:inline-block;font:600 .68rem/1 var(--body);letter-spacing:.08em;text-transform:uppercase;font-style:normal;color:var(--accent);margin-bottom:3px}
.nd b{display:block;font-size:.98rem;line-height:1.25}
.nd span{display:block;font-size:.84rem;line-height:1.4;color:var(--muted)}
.lnote{margin:14px 0 0;font-size:.86rem;color:var(--muted)}
.lnote i{display:inline-block;width:12px;height:12px;border-radius:3px;background:var(--band);vertical-align:-1px;margin-right:6px}
@media (max-width:760px){
 .chain{grid-template-columns:minmax(0,1fr)}
 .nd{grid-template-columns:44px minmax(0,1fr);gap:12px;align-items:center;padding:10px 12px}
 .nd+.nd::before{left:31px;top:-6px;transform:rotate(135deg)}
 .nd em.ph{display:none}
 .nd.dl0{border-radius:12px 12px 0 0}.nd.dl1{border-radius:0 0 12px 12px}.nd.dl0.dl1{border-radius:12px}
}
.calc{margin-top:10px}
.calc small{font-weight:400;color:var(--muted);font-size:.78rem;line-height:1.35}
.calc .full{grid-column:1/-1}
.big{margin:14px 0 8px;font-size:1rem;line-height:1.5}
.big b{color:var(--accent);font:700 1.05rem var(--mono)}
.mbarw{display:flex;height:22px;border-radius:6px;overflow:hidden;box-shadow:inset 0 0 0 1px var(--rule)}
.mbarw i{display:block;height:100%;transition:width .45s cubic-bezier(.3,.7,.2,1)}
.mbarw .f{background:var(--seg-f)}.mbarw .m{background:var(--seg-m)}.mbarw .q{background:var(--seg-q)}
.segs{display:grid;gap:2px;margin-top:8px}
.seg{display:grid;grid-template-columns:14px minmax(0,1fr) auto;gap:10px;align-items:baseline;padding:7px 6px;border-bottom:1px solid var(--rule);border-radius:6px;cursor:pointer}
.seg i{width:12px;height:12px;border-radius:3px;box-shadow:inset 0 0 0 1px var(--ol)}
.seg.f i{background:var(--seg-f)}.seg.m i{background:var(--seg-m)}.seg.q i{background:var(--seg-q)}
.seg span small{display:block;color:var(--muted);font-size:.78rem}
.seg b{font:700 .95rem var(--mono);text-align:right;white-space:nowrap}
.seg b small{display:block;font:500 .78rem var(--body);color:var(--muted)}
.seg.on{background:var(--tint)}
.warn{color:var(--accent);font-size:.86rem;margin:8px 0 0}
.gumap{margin-top:8px}
.gm p{margin:6px 0 0;font-size:.92rem}
.ctx{background:var(--tint);border-radius:12px;padding:12px 16px;margin:16px 0 0}
.sop.tight li{grid-template-columns:36px minmax(0,1fr)}
#tinh .sop p{max-width:70ch}
.journey{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:12px}
.journey a{background:var(--panel);border:1px solid var(--rule);border-radius:14px;overflow:hidden;color:var(--ink);text-decoration:none;display:flex;flex-direction:column}
.journey img{display:block;width:100%;height:auto;aspect-ratio:3/2;object-fit:cover}
.journey b{font:800 1.3rem var(--display);padding:10px 14px 0}
.journey span{padding:2px 14px 14px;color:var(--muted);font-size:.9rem}
@media (max-width:820px){.journey{grid-template-columns:minmax(0,1fr)}.journey a{display:grid;grid-template-columns:120px minmax(0,1fr);grid-template-rows:auto 1fr}.journey img{grid-row:1/3;height:100%;min-height:104px;aspect-ratio:auto}.journey b,.journey span{grid-column:2}.journey b{padding:12px 12px 0}.journey span{padding:2px 12px 12px}}
@media (prefers-reduced-motion:reduce){.mbarw i,.ic{transition:none}}
'''

JS = r'''
const $=id=>document.getElementById(id);
const Y=.95*.84,F=.18;let g=25,hl=null;
const fm=n=>String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g,'.');
const f1=n=>{const r=Math.round(n*10)/10;return Number.isInteger(r)?String(r):r.toFixed(1).replace('.',',')};
const num=id=>{const v=+String($(id).value).replace(/[^0-9]/g,'');return v>0?v:0};
function calc(){
 const gx=num('gx'),gr=num('gr'),gl=num('gl'),green=g/Y,farm=green*gx/1000,coffee=g*gr/1000,mid=coffee-farm,cafe=gl-coffee;
 const ok=gx&&gr&&gl&&mid>=0&&cafe>=0;
 $('warn').hidden=ok;
 if(!ok){$('warn').textContent=!gx||!gr||!gl?'Nhập đủ ba giá để tính.':mid<0?'Giá cà phê rang đang thấp hơn tiền nhân xô trong ly, kiểm tra lại hai giá này.':'Giá ly đang thấp hơn tiền cà phê rang trong ly, kiểm tra lại giá bán.'}
 const P=v=>ok?f1(v/gl*100)+'\u00a0%':'–';
 $('bf').style.width=ok?(farm/gl*100)+'%':'0';$('bm').style.width=ok?(mid/gl*100)+'%':'0';$('bq').style.width=ok?(cafe/gl*100)+'%':'0';
 $('vf').innerHTML=`${ok?fm(farm):'–'}\u00a0đ<small>${P(farm)}</small>`;$('vm').innerHTML=`${ok?fm(mid):'–'}\u00a0đ<small>${P(mid)}</small>`;$('vq').innerHTML=`${ok?fm(cafe):'–'}\u00a0đ<small>${P(cafe)}</small>`;
 $('big').innerHTML=ok?`Người trồng nhận khoảng <b>${fm(farm)}\u00a0đ</b>, tức <b>${P(farm)}</b> một ly <b>${fm(gl)}\u00a0đ</b>.`:'';
 $('sg').textContent=f1(green)+'\u00a0g';$('sf').textContent=fm(green/F)+'\u00a0g';$('sc').textContent=f1(Y*1000/g)+'\u00a0ly';$('ss').textContent=gl?fm(Y*1000/g*gl)+'\u00a0đ':'–';
}
['gx','gr','gl'].forEach(id=>{$(id).addEventListener('input',calc);$(id).addEventListener('blur',()=>{const v=num(id);if(v)$(id).value=fm(v)})});
$('cup').addEventListener('click',e=>{const b=e.target.closest('.pill');if(!b)return;g=+b.dataset.g;document.querySelectorAll('#cup .pill').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));calc()});
function mark(seg){hl=hl===seg?null:seg;document.querySelectorAll('.nd[data-seg]').forEach(n=>n.classList.toggle('on',n.dataset.seg===hl));document.querySelectorAll('.seg').forEach(s=>s.classList.toggle('on',s.dataset.seg===hl))}
document.querySelectorAll('.nd[data-seg]').forEach(n=>{n.addEventListener('click',()=>mark(n.dataset.seg));n.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();mark(n.dataset.seg)}})});
document.querySelectorAll('.seg').forEach(s=>s.addEventListener('click',()=>mark(s.dataset.seg)));
const copyTo=async(t,msg,srcEl,done)=>{try{await navigator.clipboard.writeText(t);$(msg).textContent=done}catch(e){const r=document.createRange();r.selectNodeContents($(srcEl));const s=getSelection();s.removeAllRanges();s.addRange(r);$(msg).textContent='Đã bôi đen, hãy sao chép bằng tay.'}};
$('copyZalo').onclick=()=>copyTo('0966770788','zaloMsg','zaloNo','Đã sao chép số Zalo.');
calc();
'''

f1 = lambda n: (('%.1f' % n).rstrip('0').rstrip('.')).replace('.', ',')

BODY = f'''{MNAV}

<div class="wrap">
<header>
  <span class="lgw"><img class="lgL" src="assets/logo-mau.png" alt="MeDili Café Di Linh" width="240" height="77"><img class="lgD" src="assets/logo-kem.png" alt="MeDili Café Di Linh" width="240" height="77"></span><div class="brandbar"><span>Mê vị Di Linh</span></div>
  <h1>Từ Vườn <em>Đến Ly</em></h1>
  <p>Farm to cup là cách làm cà phê để người uống biết ly của mình đến từ vườn nào và đi qua những tay ai. Trang này cho thấy một ly cà phê đi qua những khâu nào, và với giá cà phê hôm nay, người trồng nhận được bao nhiêu trong một ly.</p>
</header>
<div class="bench">
  <div class="card" id="c1">
    <div class="fighead"><div><b>Hình 1</b> <span>Một ly cà phê đi qua những khâu nào</span></div></div>
    <div class="lanes">
      <div><div class="lh"><b>Chuỗi thường gặp</b><span>Chỉ khâu đầu ở vùng trồng</span></div><ol class="chain">{lane(LANE_A)}</ol></div>
      <div><div class="lh"><b>Từ vườn đến ly ở MeDili</b><span>Ba khâu đầu ở Di Linh</span></div><ol class="chain">{lane(LANE_B)}</ol></div>
    </div>
    <p class="lnote"><i></i>Khâu diễn ra ở Di Linh. Bấm một khâu để xem phần tiền của khâu đó ở Hình 2.</p>
  </div>
  <aside class="card ctl" id="c2">
    <div class="fighead"><div><b>Hình 2</b> <span>Một ly, tiền đi về đâu</span></div></div>
    <div class="calc">
      <label class="full" for="gx">Giá nhân xô Robusta, đ/kg<input id="gx" inputmode="numeric" value="{fm(GX)}"><small>Lâm Đồng ngày 7/11/2026: 83.600 đ/kg.</small></label>
      <div class="full"><span class="lbl">Cà phê rang mỗi ly</span><div class="row" id="cup" role="group" aria-label="Cà phê rang mỗi ly" style="margin-top:4px"><button class="pill" type="button" data-g="25" aria-pressed="true">Phin 25 g</button><button class="pill" type="button" data-g="18" aria-pressed="false">Espresso 18 g</button></div></div>
      <label for="gr">Giá cà phê rang quán mua, đ/kg<input id="gr" inputmode="numeric" value="{fm(GR)}"><small>Giá sỉ 5–20 kg/tháng của Phin Robusta Classic.</small></label>
      <label for="gl">Giá bán một ly, đ<input id="gl" inputmode="numeric" value="{fm(GL)}"><small>Ví dụ, đổi theo quán của bạn.</small></label>
    </div>
    <p class="big" id="big">Người trồng nhận khoảng <b>{fm(M["farm"])} đ</b>, tức <b>{pct(M["farm"])} %</b> một ly <b>{fm(GL)} đ</b>.</p>
    <div class="mbarw" aria-hidden="true"><i class="f" id="bf" style="width:{M["farm"]/GL*100:.2f}%"></i><i class="m" id="bm" style="width:{M["mid"]/GL*100:.2f}%"></i><i class="q" id="bq" style="width:{M["cafe"]/GL*100:.2f}%"></i></div>
    <div class="segs">
      <div class="seg f" data-seg="f"><i></i><span>Người trồng<small>tiền nhân xô trong ly</small></span><b id="vf">{fm(M["farm"])} đ<small>{pct(M["farm"])} %</small></b></div>
      <div class="seg m" data-seg="m"><i></i><span>Sơ chế, rang, phân phối<small>từ nhân xô đến túi cà phê rang</small></span><b id="vm">{fm(M["mid"])} đ<small>{pct(M["mid"])} %</small></b></div>
      <div class="seg q" data-seg="q"><i></i><span>Quán<small>pha, mặt bằng, nhân công, sữa, đá, ly</small></span><b id="vq">{fm(M["cafe"])} đ<small>{pct(M["cafe"])} %</small></b></div>
    </div>
    <p class="warn" id="warn" hidden></p>
    <div class="stats">
      <div class="stat"><span>Nhân xanh mỗi ly</span><b id="sg">{f1(M["green"])} g</b></div>
      <div class="stat"><span>Trái chín mỗi ly</span><b id="sf">{fm(M["fresh"])} g</b></div>
      <div class="stat"><span id="scl">1 kg nhân xô ra</span><b id="sc">{f1(M["cups"])} ly</b></div>
      <div class="stat"><span id="ssl">Bán ra ở quán</span><b id="ss">{fm(M["sales"])} đ</b></div>
    </div>
    <p class="src">Phần của người trồng là doanh thu, chưa trừ phân bón, công hái, nước tưới. Hao hụt theo mô hình của MeDili: lọc 5 % hạt lỗi, hao 16 % khi rang, 100 kg trái chín ra 18 kg nhân.</p>
  </aside>
</div>

<section class="card" id="la-gi">
  <h2>Farm to cup là gì</h2>
  <p class="lead">Farm to cup, hay từ vườn đến ly, là một cách làm. Đây không phải một chứng nhận. Có bốn dấu hiệu để nhận ra.</p>
  <div class="gumap">
    <div class="gm"><h3>Biết vườn, biết lô</h3><p>Mỗi túi cà phê ghi được vườn, mã lô và ngày rang. Người uống hỏi được ly này đến từ đâu.</p></div>
    <div class="gm"><h3>Ít khâu trung gian</h3><p>Mỗi lần qua tay là một lần cộng giá. Bớt khâu thì phần giá trị ở gần nơi trồng hơn.</p></div>
    <div class="gm"><h3>Giá theo chất lượng</h3><p>Trái chín, sơ chế kỹ được bán theo chất lượng của lô, thay vì chỉ theo giá nhân xô hằng ngày.</p></div>
    <div class="gm"><h3>Rang gần ngày uống</h3><p>Cà phê rang cần nghỉ vài ngày, rồi ngon nhất trong vài tuần sau đó. Chuỗi ngắn đưa cà phê đến tay người uống sớm hơn.</p></div>
  </div>
  <p class="ctx">Khoảng 80 % sản lượng cà phê Việt Nam vẫn ở dạng nhân xanh, chủ yếu là Robusta. Phần giá trị của rang, đóng gói và pha phần lớn vì vậy nằm ngoài vùng trồng.</p>
</section>

<section class="card" id="tinh">
  <h2>Một ly {fm(GL)} đ, người trồng nhận bao nhiêu</h2>
  <p class="lead">Phép tính dưới đây dùng giá nhân xô Lâm Đồng ngày 7/11/2026 và mô hình hao hụt trên trang Lên men men bia của MeDili.</p>
  <ol class="sop tight">
    <li><span class="n">1</span><p>Một ly phin dùng <b>25 g</b> cà phê rang.</p></li>
    <li><span class="n">2</span><p>25 g rang cần khoảng <b>{f1(M["green"])} g</b> nhân xanh, vì nhân còn lọc hạt lỗi và mất nước khi rang. Số nhân này đến từ khoảng <b>{fm(M["fresh"])} g</b> trái chín.</p></li>
    <li><span class="n">3</span><p>Với giá <b>83.600 đ/kg</b>, {f1(M["green"])} g nhân xô đáng khoảng <b>{fm(M["farm"])} đ</b>. Quán mua 25 g cà phê rang theo giá sỉ MeDili hết khoảng <b>{fm(M["coffee"])} đ</b>.</p></li>
    <li><span class="n">4</span><p>Ly bán {fm(GL)} đ thì phần của người trồng khoảng <b>{pct(M["farm"])} %</b>. Một kg nhân xô làm ra khoảng <b>{round(M["cups"])} ly</b>, bán ở quán được khoảng <b>{f1(M["sales"]/1e6)} triệu đồng</b>.</p></li>
  </ol>
  <p>Phần còn lại trả cho nhiều việc. Quán trả mặt bằng, nhân công, sữa, đường, đá và ly. Nhà rang trả công sơ chế, rang, bao bì và vận chuyển. Farm to cup thay đổi chỗ ai làm những khâu đó. Ở MeDili, vườn, xưởng sơ chế và xưởng rang cùng một nhà, cùng ở Di Linh, nên phần giá trị của sơ chế và rang ở lại vùng trồng.</p>
  <p>Phần của người trồng ở đây là doanh thu, chưa trừ chi phí. Chi phí phân bón, công hái và nước tưới cho từng tháng có ở trang <a href="vuon.html">Vườn 12 tháng</a>.</p>
</section>

<section id="doc-tiep">
  <h2>Đọc tiếp</h2>
  <div class="journey">
    <a href="vuon.html"><img src="assets/vuon.jpg" alt="" loading="lazy" width="900" height="606"><b>Vườn 12 tháng</b><span>Chăm Robusta Cà Sẻ hướng tự nhiên, từ bón phân đến thu hái.</span></a>
    <a href="trai-ca-phe.html"><img src="assets/trai-ca-phe.jpg" alt="" loading="lazy" width="900" height="600"><b>Giải phẫu trái Cà Sẻ</b><span>Năm lớp bọc một hạt nhân và cách mỗi lớp được tách ra.</span></a>
    <a href="mua-hang.html"><img src="assets/mua.jpg" alt="" loading="lazy" width="900" height="606"><b>Chọn mua</b><span>Giá theo gói, giá sỉ theo sản lượng tháng, gửi đơn.</span></a>
  </div>
</section>

<section class="card src">
  <h2 style="color:var(--ink)">Nguồn số liệu</h2>
  <ul>
    <li><a href="https://baolaocai.vn/gia-ca-phe-hom-nay-7112026-trong-nuoc-nhich-len-phien-thu-hai-post913779.html" target="_blank" rel="noopener">Báo Lào Cai, 7/11/2026</a>: giá nhân xô Lâm Đồng 83.600 đ/kg.</li>
    <li><a href="https://en.vietstock.vn/2026/05/coffee-sector-shifts-to-deep-processing-as-export-markets-demand-more-970-633733.htm" target="_blank" rel="noopener">Vietstock, 20/5/2026</a>: khoảng 80 % sản lượng cà phê Việt Nam vẫn ở dạng nhân xanh.</li>
    <li><a href="https://dailycoffeenews.com/2021/01/28/ico-releases-flagship-annual-report-the-value-of-coffee" target="_blank" rel="noopener">ICO, The Value of Coffee, 2021</a>: phần lớn giá trị thị trường cà phê thuộc về các khâu ở nước tiêu thụ.</li>
    <li><a href="len-men-men-bia.html">MeDili, Lên men men bia</a>: tỷ lệ trái tươi ra nhân, lọc hạt lỗi, hao hụt khi rang.</li>
    <li><a href="mua-hang.html">MeDili, Chọn mua</a>: giá sỉ Phin Robusta Classic.</li>
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

BODY = re.sub(r'(\d) (đ|kg|g|ly|%|triệu)(?=[\s<.,)/])', r'\1&nbsp;\2', BODY)
DESC = 'Farm to cup là gì, một ly cà phê đi qua những khâu nào, và với giá cà phê hôm nay người trồng nhận bao nhiêu trong một ly.'
HEAD = (f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        f'<meta name="description" content="{DESC}"><meta property="og:title" content="Từ Vườn Đến Ly MeDili"><meta property="og:description" content="{DESC}">'
        f'<style>*{{box-sizing:border-box}}:root{{padding-top:env(safe-area-inset-top,0);padding-bottom:env(safe-area-inset-bottom,0)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>'
        f'<title>Từ Vườn Đến Ly MeDili</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n')
assert '</script' not in JS.lower()
html = HEAD + '<style>' + SHARED + '</style>\n<style>' + PAGE_CSS + '</style></head><body>' + BODY + '\n<script>' + JS + '</script>\n</body></html>\n'
open(os.path.join(OUT, PAGE), 'w', encoding='utf8').write(html)
open(os.path.join(HERE, '_f2c.check.js'), 'w', encoding='utf8').write(JS)

# ---------- trang chủ: hai bài đọc thêm ----------
idx = nav(rd('index.html'))
m = re.search(r'\n<section class="feat"><a href="trai-ca-phe\.html">(.*?)</a></section>', idx, flags=re.S)
assert m
CUP = ('<svg class="fc" viewBox="0 0 200 220" aria-hidden="true">'
       '<path d="M78 112C92 150 140 128 136 150" fill="none" stroke="var(--muted)" stroke-width="2.5" stroke-dasharray="2 8" stroke-linecap="round"/>'
       '<path d="M62 96v42" stroke="var(--stem2)" stroke-width="8" stroke-linecap="round"/>'
       '<g fill="var(--stem)" stroke="var(--ol)" stroke-width="1.5"><circle cx="44" cy="70" r="24"/><circle cx="78" cy="62" r="28"/><circle cx="62" cy="92" r="22"/><circle cx="58" cy="52" r="20"/></g>'
       '<g fill="var(--skin)" stroke="var(--ol)" stroke-width="1"><circle cx="48" cy="66" r="5.5"/><circle cx="76" cy="52" r="5.5"/><circle cx="88" cy="74" r="5.5"/><circle cx="62" cy="88" r="5.5"/><circle cx="38" cy="82" r="5"/><circle cx="66" cy="40" r="5"/></g>'
       '<ellipse cx="136" cy="200" rx="48" ry="7" fill="none" stroke="var(--ink)" stroke-width="3"/>'
       '<path d="M104 152h64v22a26 26 0 0 1-26 26h-12a26 26 0 0 1-26-26z" fill="var(--panel)" stroke="var(--ink)" stroke-width="3" stroke-linejoin="round"/>'
       '<path d="M168 160h7a10 10 0 0 1 0 20h-7" fill="none" stroke="var(--ink)" stroke-width="3"/>'
       '<ellipse cx="136" cy="153" rx="30" ry="5" fill="var(--stem2)"/>'
       '<path d="M124 132c-5 6 5 8 0 14M140 128c-5 6 5 8 0 14" fill="none" stroke="var(--muted)" stroke-width="2.5" stroke-linecap="round"/></svg>')
F2 = (f'<a href="{PAGE}">{CUP}<div><p class="eye">Farm to cup</p><h2>Từ vườn đến ly</h2>'
      f'<p>Một ly cà phê đi qua những khâu nào, và với giá cà phê hôm nay, người trồng nhận bao nhiêu trong một ly {fm(GL)}&nbsp;đ.</p>'
      f'<span class="btn main">Đọc bài</span></div></a>')
idx = idx.replace(m.group(0), m.group(0)[:-len('</section>')] + F2 + '</section>')
EXTRA = ('\n.feat{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.feat a{grid-template-columns:150px minmax(0,1fr)}'
         '@media (max-width:980px){.feat{grid-template-columns:minmax(0,1fr)}}@media (max-width:620px){.feat a{grid-template-columns:96px minmax(0,1fr)}}\n')
i = idx.rfind('</style>')
idx = idx[:i] + EXTRA + idx[i:]
open(os.path.join(OUT, 'index.html'), 'w', encoding='utf8').write(idx)

for f in ['vuon.html', 'trai-ca-phe.html', 'len-men-men-bia.html', 'len-men-trai-cay.html', 'rang.html', 'quay-pha.html', 'suc-khoe.html', 'mua-hang.html']:
    open(os.path.join(OUT, f), 'w', encoding='utf8').write(nav(rd(f)))

print('trang mới', len(html.encode()) // 1024, 'KB', {k: round(v, 1) for k, v in M.items()})

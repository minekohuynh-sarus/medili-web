# Gộp toàn bộ nội dung web Manus vào site MeDili trên Claude.
# Đọc site-new3 (bản đang chạy), ghi site-new4: trang mới, trang chủ theo 8 chương, menu và chân trang mới trên mọi trang.
import os, re, json, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
import ill, pages_a, pages_b, chiet, coldbrew, traichin, visinh, huong, banhxe, phanbiet, nhanxanh, cuahang, congthuc, anhvuon, huongdan, donghanh, chinhsach, thanhtoan, tintuc, lenmentuthan

os.makedirs(OUT, exist_ok=True)
rd = lambda f: open(os.path.join(BASE, f), encoding='utf8').read()

# Giá theo bảng báo giá MeDili tháng 11/2026 (chị Ngân chốt 12/11/2026): Catimor 400k/kg, Culi 350k/kg, chưa có giá sỉ.
PRICE_FIX = [("{id:'cat',n:'Catimor',full:'Cà phê Catimor',line:'Đặc sản',kind:'phin',p:[350,null,null],",
              "{id:'cat',n:'Catimor',full:'Cà phê Catimor',line:'Đặc sản',kind:'phin',p:[400,null,null],"),
             ("{id:'cul',n:'Culi',full:'Cà phê Culi',line:'Đặc sản',kind:'phin',p:null,",
              "{id:'cul',n:'Culi',full:'Cà phê Culi',line:'Đặc sản',kind:'phin',p:[350,null,null],")]
# Câu "Catimor, Culi và Blend MeDili chưa có giá sỉ" đã sửa thẳng trong site-new3/mua-hang.html (23/11/2026).


def price_fix(s):
    for a, b in PRICE_FIX:
        assert s.count(a) == 1, a[:60]
        s = s.replace(a, b)
    return s

# ---------- danh mục 14 dòng từ Phòng chọn mua ----------
shop = price_fix(rd('mua-hang.html'))
a, b = shop.index('const CL='), shop.index('const byId=')
node = subprocess.run(['node', '-e', shop[a:b] + ';process.stdout.write(JSON.stringify(S))'], capture_output=True, text=True, check=True)
P = {x['id']: x for x in json.loads(node.stdout)}
assert len(P) == 14, len(P)

# ---------- hình trái cà phê và cây trên trang chủ cũ ----------
home_old = rd('index.html')
FEAT = re.findall(r'<svg class="fc".*?</svg>', home_old, flags=re.S)
assert len(FEAT) == 2
HOME_CSS_OLD = re.findall(r'<style>(.*?)</style>', home_old, flags=re.S)[0]
i0 = HOME_CSS_OLD.index('.c-skin{fill:var(--skin)}')
i1 = HOME_CSS_OLD.index(':root{--skin:#B33A24')
i2 = HOME_CSS_OLD.index('}', i1) + 1
FIGCSS = HOME_CSS_OLD[i0:i2] + '\n.jcards .th svg.fc{width:auto;height:84%;max-width:84%}'
pages_b.FIGCSS = FIGCSS

# ---------- dữ liệu bài Tìm gu (artifact Tìm Gu MeDili của chị Ngân) ----------
tg = open(os.path.join(HERE, '..', 'artifact-files', 'bcca7630-2c1d-4149-a4f4-ed7eca69eee8', 'index.html'), encoding='utf8').read()
seg = lambda start, end: tg[tg.index(start):tg.index(end)]
TG_DATA = (seg('const PRODUCTS = [', '/* a = tỷ lệ Arabica phù hợp') + seg('const QUESTIONS = [', 'function scoreAnswers') +
           seg('function scoreAnswers', 'const state = {'))
assert 'RECIPES' in TG_DATA and 'function profile' in TG_DATA
# đối chiếu giá với Phòng chọn mua
tgp = json.loads(subprocess.run(['node', '-e', TG_DATA.split('const QUESTIONS')[0] + ';process.stdout.write(JSON.stringify(PRODUCTS))'],
                                capture_output=True, text=True, check=True).stdout)
idmap = {'p-rc': 'pc', 'p-rp': 'pp', 'm-rc': 'mc', 'm-rp': 'mp', 'm-rs': 'ms', 'p-ap': 'pa', 'm-ap': 'ma', 'b-91': 'b91', 'b-82': 'b82', 'b-73': 'b73', 'b-55': 'b55'}
for x in tgp:
    assert [v // 1000 for v in x['prices']] == P[idmap[x['id']]]['p'], x['id']

# ---------- thời gian đọc của hai bài đã có ----------
def page_words(f):
    s = rd(f)
    s = re.sub(r'<(script|style|svg)[^>]*>.*?</\1>', ' ', s, flags=re.S)
    s = s[s.find('<div class="wrap">'):]
    s = s[:s.find('class="contact"')]
    return len(re.findall(r'\w+', re.sub(r'<[^>]+>', ' ', s)))

M_TRAI = max(2, -(-page_words('trai-ca-phe.html') // 200))
M_F2C = max(2, -(-page_words('tu-vuon-den-ly.html') // 200))

CARDS = []
for f, a_ in pages_b.ART.items():
    CARDS.append((f, pages_b.jcard(f, a_['cat'], f'{pages_b.mins(a_["body"])} phút đọc', re.sub(r'</?em>', '', a_['h1']).rstrip('.'), a_['dek'], a_['svg']())))
CARDS += [
    ('trai-ca-phe.html', pages_b.jcard('trai-ca-phe.html', 'Giải phẫu trái', f'{M_TRAI} phút đọc', 'Bên trong trái Cà Sẻ',
                                       'Năm lớp bọc quanh hạt nhân, mỗi lớp được tách ra ở bước nào, và vì sao Natural, Honey, Washed cho vị khác nhau.', FEAT[0])),
    ('tu-vuon-den-ly.html', pages_b.jcard('tu-vuon-den-ly.html', 'Farm to cup', f'{M_F2C} phút đọc', 'Từ vườn đến ly',
                                          'Một ly cà phê đi qua những khâu nào, và với giá cà phê hôm nay, người trồng nhận bao nhiêu trong một ly 35.000 đ.', FEAT[1])),
    ('suc-khoe.html', pages_b.jcard('suc-khoe.html', 'Sức khỏe', 'Có công cụ tính', 'Cà phê và cơ thể',
                                    'Điều gì xảy ra sau một ngụm, một tuần và một năm uống cà phê. Tính lượng caffeine theo thói quen của bạn.', ill.suckhoe())),
]

# ---------- trang mới ----------
NEW = {
    'cau-chuyen.html': pages_a.cau_chuyen(),
    'doi-ngu.html': pages_a.doi_ngu(),
    'vung-trong.html': pages_a.vung_trong(),
    'horeca.html': pages_a.horeca(P),
    'xuong-rang.html': pages_a.xuong_rang(),
    'quan-medili.html': pages_a.quan_medili(),
    'journal.html': pages_b.journal(CARDS),
    'tim-gu.html': pages_b.tim_gu(TG_DATA),
    'lien-he.html': pages_b.lien_he(),
    'giao-hang.html': pages_b.giao_hang(),
    'bao-mat.html': pages_b.bao_mat(),
    'chiet-xuat.html': chiet.page(),
    'cold-brew.html': coldbrew.page(),
    'trai-chin.html': traichin.page(),
    'vi-sinh.html': visinh.page(),
    'tien-chat-huong.html': huong.page(),
    'banh-xe-huong.html': banhxe.page(),
    'phan-biet-ca-phe.html': phanbiet.page(),
    'nhan-xanh.html': nhanxanh.page(),
    anhvuon.FILE: anhvuon.page(),   # Ảnh vườn MeDili (21/11/2026)
    huongdan.FILE: huongdan.page(),   # Hướng dẫn pha, mô hình 3D (23/11/2026)
}
for f, a_ in pages_b.ART.items():
    NEW[f] = pages_b.article(f, a_, CARDS)
# Cửa hàng theo cấu trúc web medilinh.com: danh mục, 20 trang sản phẩm, giỏ hàng, tìm kiếm
SHOP, CATALOG = cuahang.pages(P)
NEW.update(SHOP)
NEW[congthuc.FILE] = congthuc.page(CATALOG)   # Cỗ máy Công thức pha (17/11/2026)
NEW[donghanh.FILE] = donghanh.page(P)   # Đồng hành cùng quán (23/11/2026)
NEW[chinhsach.FILE] = chinhsach.page()   # Chính sách MeDili: khách sỉ, đổi trả, kiểm hàng, hoàn tiền (23/11/2026)
NEW.update(tintuc.pages())   # Tin tức hằng ngày, bài đã duyệt trong art/data/tin-tuc.json (24/11/2026)
NEW[thanhtoan.FILE] = thanhtoan.page()   # Thanh toán: mã VietQR chuyển khoản, link thanh toán, COD (24/11/2026)
NEW[lenmentuthan.FILE] = lenmentuthan.page()   # Lên men tự thân trái cà phê: clip 3D trong mục Vùng trồng & sản xuất (25/11/2026)
N_SHELF = sum(x['st'] != 'sap' for x in CATALOG)   # dòng đang bán (kể cả Ngũ Hành)

# ---------- trang cũ: menu, chân trang, màu ----------
OLD = ['gia-ca-phe.html', 'vuon.html', 'trai-ca-phe.html', 'len-men-men-bia.html', 'len-men-trai-cay.html', 'rang.html',
       'quay-pha.html', 'suc-khoe.html', 'tu-vuon-den-ly.html', 'mua-hang.html']
UPD = {}
for f in OLD:
    s = rd(f)
    s, n = re.subn(r'<div class="mnav">.*?</div></div>', lambda m: header(f), s, count=1, flags=re.S); assert n == 1, f
    s, n = re.subn(r'\s*<footer>.*?</footer>', '', s, count=1, flags=re.S); assert n == 1, f
    assert s.count('</head>') == 1 and s.count('</body>') == 1, f
    s = s.replace('</head>', '<style>' + CORE_CSS + '</style></head>')
    s = s.replace('</body>', footer() + '\n<script>' + COMMON_JS + '</script>\n</body>')
    GAL = {'len-men-trai-cay.html': ('Ảnh thực tế', 'Cà phê trái chín đồng lên men với nhãn, dâu tằm và chanh dây.', STRIP_LM),
           'len-men-men-bia.html': ('Ba cách sơ chế', 'Natural phơi nguyên trái, Honey giữ lớp nhớt, Washed xát tươi tách vỏ rồi lên men và rửa.', STRIP_SOCHE),
           'vuon.html': ('Vườn vào mùa', 'Robusta chín đỏ, thu hái rồi phơi.', STRIP_VUON)}
    if f in GAL:
        t, d, items = GAL[f]
        assert s.count('</header>') == 1, f
        more = '<div class="lnks" style="margin-top:0"><a class="lnk" href="anh-vuon.html">Xem toàn bộ ảnh vườn</a></div>' if f == 'vuon.html' else ''
        s = s.replace('</header>', f'</header>\n<section class="pgal" aria-label="{t}"><h2>{t}</h2><p>{nb(d)}</p>{strip(items)}{more}</section>', 1)
    if f == 'mua-hang.html':
        s = price_fix(s)
        assert s.count("col:'#2F6B4A'") == 2 and s.count("col:'#3F7F5A'") == 1
        s = s.replace("col:'#2F6B4A'", "col:'#B5832F'").replace("col:'#3F7F5A'", "col:'#C9A15B'")
        assert s.count('</header>') == 1
        s = s.replace('</header>', '</header>\n<p class="note" style="margin:0 0 14px">Mua lẻ từng gói? Vào <a href="cua-hang.html" '
                      'style="color:var(--accent);font-weight:600">Cửa hàng MeDili</a>, thêm vào giỏ rồi gửi đơn. Phòng chọn mua giúp quán tính lượng dùng và giá sỉ.</p>', 1)
    UPD[f] = s

# ---------- giá cà phê: không hiện tên nguồn cụ thể ----------
_g = UPD['gia-ca-phe.html']
for _a, _b in [
    ("`Báo giá ngày ${dd(F.date)}${F.place?', '+F.place:''}, theo ${F.src.name}.`", "`Báo giá ngày ${dd(F.date)}${F.place?', '+F.place:''}.`"),
    ("const s=el('span','',`${dd(q.date)} · ${q.place||'bài không nêu nơi thu mua'} · `);const a=el('a','',q.src.name);a.href=q.src.url;a.target='_blank';a.rel='noopener';s.append(a);e.append(s);",
     "const s=el('span','',`${dd(q.date)} · ${q.place||'chưa rõ nơi thu mua'}`);e.append(s);"),
    ("function srcs(){", "function srcs(){return;"),
]:
    assert _g.count(_a) == 1, _a[:60]
    _g = _g.replace(_a, _b)
UPD['gia-ca-phe.html'] = _g

# ---------- nguồn: chỉ ghi "Nguồn tổng hợp", giữ ghi chú cách đọc mô hình và link nội bộ ----------
LEADFIX = [('được canh theo các mốc dưới đây', 'được canh theo các mốc trong tài liệu tổng hợp'),
           ('Tôi không tìm thấy định mức chuẩn', 'MeDili chưa tìm thấy định mức chuẩn'),
           ('Công thức là mốc khởi đầu từ các nguồn dưới đây. Các con số không có nguồn riêng, như', 'Công thức là mốc khởi đầu, tổng hợp từ tài liệu pha chế. Các con số như'),
           ('Mỗi nguồn chia cấp độ hơi khác nhau', 'Mỗi tài liệu chia cấp độ hơi khác nhau')]


def nguon_tong_hop(s):
    def rep(m):
        sec = m.group(0)
        note = ' '.join(re.sub(r'\s+', ' ', x).strip() for x in re.findall(r'<p class="lead"[^>]*>(.*?)</p>', sec, flags=re.S))
        for x, y in LEADFIX:
            note = note.replace(x, y)
        lnks = ''.join(re.findall(r'<div class="lnks">.*?</div>', sec, flags=re.S))
        return ('<section class="card src"><p style="margin:0;font-size:.88rem;color:var(--muted);max-width:110ch">'
                '<b style="color:var(--ink)">Nguồn tổng hợp.</b>' + (' ' + note if note else '') + '</p>' + lnks + '</section>')
    return re.sub(r'<section class="card src">.*?</section>', rep, s, flags=re.S)


# ---------- trang chủ theo 8 chương ----------
J = json.load(open(os.path.join(HERE, '..', 'run-check', 'gia-ca-phe.json'), encoding='utf8'))
dl = sorted([d for d in J['days'] if d.get('vn', {}).get('lamdong')], key=lambda d: d['date'])[-1]
dw = sorted([d for d in J['days'] if d.get('world', {}).get('robusta')], key=lambda d: d['date'])[-1]
ddmm = lambda d: '/'.join(d.split('-')[::-1][:2])

def pr(k):
    return P[k]['p'][0] * 1000

COLL = [
    ('#6B4226', 'Classic · Natural', 'Robusta Classic', P['pc']['taste'], P['pc']['use'], f'Phin và máy · từ <b>{fm(min(pr("pc"), pr("mc")))} đ/kg</b>'),
    ('#A23B24', 'Premium · Honey, Washed', 'Robusta Premium', P['pp']['taste'], P['pp']['use'], f'Phin và máy · từ <b>{fm(min(pr("pp"), pr("mp")))} đ/kg</b>'),
    ('#B5832F', 'Premium · Cầu Đất', 'Arabica Premium', P['pa']['taste'], P['ma']['use'], f'Phin và máy · <b>{fm(pr("pa"))} đ/kg</b>'),
    ('#8A5A32', 'Premium · Robusta, Arabica', 'Blend 9:1 đến 5:5', 'Từ đậm ca cao đến cân bằng, thơm, chua thanh', P['b73']['use'],
     f'Pha máy · <b>{fm(pr("b91"))}–{fm(pr("b55"))} đ/kg</b>'),
]
COLL_HREF = ['cua-hang.html?q=classic', 'cua-hang.html?q=robusta%20premium', 'cua-hang.html?loai=arabica', 'cua-hang.html?loai=blend']
coll = ''.join(f'<a class="box coll" href="{h}"><i class="bag" style="--c:{c}" aria-hidden="true"></i><span class="k">{k}</span><h3>{t}</h3>'
               f'<p>{taste}.</p><p class="use">{use}</p><div class="ft">{ft}</div></a>' for h, (c, k, t, taste, use, ft) in zip(COLL_HREF, COLL))

BAND_MUA = anhvuon.band('bg-mua-vu', 'Trái cà phê chuyển màu dưới tán lá', 'Ảnh vườn MeDili', 'Mỗi mùa chín <em>là một câu chuyện.</em>',
                        f'Trái chín trên cành, bàn tay hái, máy cày chở bao rời vườn, rồi phơi và xay xát. Trọn mùa vụ trong {len(anhvuon.GAL)} tấm ảnh.',
                        '<a class="btn main" href="anh-vuon.html">Xem ảnh vườn</a><a class="btn" href="vung-trong.html">Vùng trồng Di Linh</a>')
BAND_KHO = anhvuon.band('bg-trong-kho', 'Xe xúc làm việc trong kho cà phê dưới ánh đèn vàng', 'Chương 08 · Hẹn nhau ở MeDili',
                        'Một niềm mê để sẻ chia. <em>Một hành trình còn tiếp.</em>',
                        'Di Linh origin · Saigon soul. Cà phê đi từ vườn, kho và sân phơi ở Di Linh đến những tách cà phê ở Sài Gòn.',
                        '<a class="btn main" href="quan-medili.html">Ghé MeDili Café</a><a class="btn" href="lien-he.html">Liên hệ &amp; bản đồ</a>')

HOME_BODY = f'''{header('index.html')}
{anhvuon.hero('bg-trang-chu', 'Bàn tay hái giữa những chùm cà phê chín', f"""{anhvuon.logo_kem()}<p class="eye">Chương 01 · Nhà rang cà phê chuyên nghiệp</p>
  <h1>Từ gốc Cà Sẻ.<br><em>Đến nghệ thuật rang.</em></h1>
  <p class="sub">MeDili là nhà rang cà phê trên cao nguyên Di Linh, chọn Cà Sẻ Di Linh làm nguyên liệu gốc. Vùng trồng canh tác từ năm 2010, xưởng rang đặt tại Thôn 11, xã Di Linh. MeDili rang cà phê cho gia đình, quán cà phê, nhà hàng và khách sạn.</p>
  <div class="cta"><a class="btn main" href="cua-hang.html">Chọn cà phê</a><a class="btn" href="tim-gu.html">Tìm gu của bạn</a><a class="btn" href="horeca.html">Giải pháp HORECA</a></div>
  <a class="tick" href="gia-ca-phe.html"><span class="k">Giá cà phê <span id="tk-d" translate="no">{ddmm(dl['date'])}</span></span><span>Nhân xô Lâm Đồng <b><span id="tk-v" translate="no">{fm(dl['vn']['lamdong'])}</span> đ/kg</b></span><span>Robusta London <b><span id="tk-r" translate="no">{fm(dw['world']['robusta'])}</span> USD/tấn</b></span><i>Xem bảng giá</i></a>""")}
<div class="wrap hm">
<section class="p-sec" id="bo-suu-tap">
 <p class="eye">Chương 02 · Bộ sưu tập MeDili</p>
 <h2 class="p-h2">Bốn hương vị. <em>Một niềm mê.</em></h2>
 <p class="lead">Bốn nhóm cà phê rang mộc của MeDili. Mỗi nhóm có loại pha phin, loại pha máy và giá sỉ theo lượng dùng mỗi tháng.</p>
 <div class="g4">{coll}</div>
 <div class="box gu"><div>{icon('gu')}</div><div><p class="eye">Tìm gu cà phê của bạn</p><p>Sáu câu hỏi ngắn. Không có đáp án đúng, chỉ có ly cà phê đúng gu.</p></div><div class="cta" style="margin:0"><a class="btn main" href="tim-gu.html">Bắt đầu khám phá</a><a class="btn" href="cua-hang.html">Xem cả {N_SHELF} dòng</a></div></div>
 <p class="note">Giá đề xuất, chưa gồm 8% VAT và phí vận chuyển. MeDili xác nhận giá khi bạn đặt hàng.</p>
</section>
</div>
{BAND_MUA}
<div class="wrap hm">
<section class="split">
 <div class="p-sec">
  <p class="eye">Chương 03 · Câu chuyện MeDili</p>
  <h2 class="p-h2" style="margin:0">Cà Sẻ Di Linh. <em>Nguồn gốc của niềm mê.</em></h2>
  <p>MeDili chọn Cà Sẻ Di Linh làm nền tảng. Vùng trồng canh tác từ năm 2010, cây đã 15 năm tuổi, được chăm sóc theo hướng tự nhiên. Xưởng rang ở Thôn 11 đưa nguyên liệu từ vườn đến người uống và các quán.</p>
  <blockquote class="quote">Nguồn gốc là nền tảng của mỗi mẻ rang.</blockquote>
  <div class="cta"><a class="btn main" href="cau-chuyen.html">Đọc câu chuyện MeDili</a></div>
 </div>
 <div class="p-sec">
  <p class="k">Những người giữ lửa cho hương vị</p>
  <a class="box role" href="doi-ngu.html">{icon('rang')}<div><span class="k">01 · Hiểu nguyên liệu</span><h3>Đội ngũ rang xay</h3><p>Nguyên liệu, hồ sơ rang và hương vị.</p></div></a>
  <a class="box role" href="doi-ngu.html">{icon('ly')}<div><span class="k">02 · Pha trọn vị trong tách</span><h3>Nghệ nhân barista</h3><p>Phin, espresso và gu của từng khách.</p></div></a>
  <div class="lnks"><a class="lnk" href="doi-ngu.html">Khám phá đội ngũ MeDili</a></div>
 </div>
</section>

<section class="box p-sec">
 <p class="eye">Chương 04 · Vùng đất Di Linh</p>
 <h2 class="p-h2" style="margin:0">Di Linh. <em>Nơi câu chuyện bắt đầu.</em></h2>
 <p class="lead" style="margin:0">Bốn vùng trồng với tổng diện tích {ha(TOTAL)} ha. Ngoài ra có {LINKED} ha liên kết tại Di Linh, tính riêng, không gộp vào {ha(TOTAL)} ha.</p>
 {photo('p-san-phoi-wide.jpg', 'Cà phê phơi trên sân giữa đồi', 'Phơi cà phê giữa đồi.', cls='pfw')}
 <div class="pgal"><p class="k">Vào mùa ở vườn MeDili</p>{strip(STRIP_MUAVU)}<div class="lnks" style="margin-top:0"><a class="lnk" href="anh-vuon.html">Xem toàn bộ ảnh vườn</a></div></div>
 {pages_a.seg_block()}
 <div class="lnks"><a class="lnk" href="vung-trong.html">Khám phá vùng nguyên liệu</a><a class="lnk" href="{MAP_FARM}" target="_blank" rel="noopener">Chỉ đường đến xưởng rang ↗</a></div>
</section>

<section class="p-sec" id="hanh-trinh">
 <p class="eye">Chương 05 · Từ nông trại đến tách</p>
 <h2 class="p-h2">Một hành trình <em>trong từng tách cà phê.</em></h2>
 <p class="lead">Năm công đoạn làm nên hương vị. Mỗi công đoạn có một mô hình để bạn tự bấm, chỉnh thông số và xem cách làm.</p>
 {pages_a.trip()}
 <div class="pgal"><p class="k">Những lô lên men đặc biệt</p>{strip(STRIP_LM)}<div class="lnks" style="margin-top:0"><a class="lnk" href="len-men-trai-cay.html">Xem cỗ máy lên men cùng trái cây</a><a class="lnk" href="xuong-rang.html">Xưởng rang &amp; năng lực</a></div></div>
</section>

<section class="band">
 <div><p class="eye">Giải pháp cà phê cho HORECA</p><h2>Cho quán cà phê, nhà hàng, khách sạn</h2>
 <p>Nhân xanh, cà phê pha phin, pha máy và cold brew. Xưởng rang trung bình 20 tấn mỗi tháng, tối đa 60 tấn, đóng gói bằng máy bán tự động.</p></div>
 <div class="cta" style="margin:0"><a class="btn light" href="horeca.html">Khám phá giải pháp</a><a class="btn light2" href="mua-hang.html">Tính giá mỗi ly</a></div>
</section>

<section class="box split">
 <div class="p-sec">
  <p class="eye">Chương 06 · MeDili Café</p>
  <h2 class="p-h2" style="margin:0">Một tách cà phê. <em>Một cuộc hẹn.</em></h2>
  <p>Công ty TNHH Thực phẩm DSunfood tại 143 Phạm Văn Hai là điểm phân phối của MeDili ở TP.HCM, đồng thời là MeDili Café. Bạn có thể ghé uống một ly, hỏi thực đơn trong ngày hoặc trao đổi về việc cung cấp cà phê cho quán.</p>
  <p class="k">Hôm nay, bạn mê vị gì?</p>
  <div class="chips" style="margin-top:0"><span>Cà phê sữa đá Việt Nam</span><span>Cà phê phin</span><span>Cappuccino</span><span>Espresso</span></div>
  <p class="note">Thực đơn gợi ý. Vui lòng gọi trước để xác nhận món trong ngày.</p>
  <div class="cta"><a class="btn main" href="quan-medili.html">Ghé MeDili Café</a><a class="btn" href="{MAP_HCM}" target="_blank" rel="noopener">Chỉ đường ↗</a></div>
 </div>
 <div class="illw">{ill.suada()}</div>
</section>

<section class="p-sec">
 <p class="eye">Chương 07 · Kiến thức cà phê</p>
 <h2 class="p-h2">Những ghi chép <em>bên tách cà phê.</em></h2>
 {pages_b.feat_chiet()}
 <div class="jcards">{''.join(c for f, c in CARDS)}</div>
 <div class="lnks"><a class="lnk" href="journal.html">Mở mục Kiến thức cà phê</a></div>
</section>

</div>
{BAND_KHO}
<div class="wrap hm end">
<section class="p-sec">
 <div class="facts"><div><b>{ha(TOTAL)} ha</b><span>bốn vùng trồng ở Lâm Đồng</span></div><div><b>{LINKED} ha</b><span>liên kết tại Di Linh, tính riêng</span></div><div><b>2010</b><span>năm vùng trồng bắt đầu canh tác</span></div><div><b>{N_SHELF}</b><span>dòng cà phê trên kệ</span></div></div>
 {pages_a.loc_cards()}
</section>
{contact_band()}
</div>
{footer('MeDili Coffee Farm · Di Linh')}
'''

HOME_CSS = '''
/* Trang chủ theo 8 chương của web Manus. */
.wrap.hm{gap:34px}
.wrap .contact{margin-inline:0}
.tick{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline;margin-top:18px;padding:10px 14px;border:1px solid var(--rule);border-radius:12px;background:var(--panel);color:var(--ink);text-decoration:none;font-size:.9rem;max-width:560px}
.tick .k{font:600 .72rem var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
.tick b{font:700 .95rem var(--mono)}.tick i{font-style:normal;color:var(--accent);font-weight:600;margin-left:auto}
.tick:hover{border-color:var(--accent)}
.coll{display:flex;flex-direction:column;gap:4px;text-decoration:none;color:var(--ink)}.coll p{margin:0}.coll .ft{margin-top:auto}
.coll .bag{display:block;width:30px;height:40px;background:var(--c);clip-path:polygon(14% 0,86% 0,100% 16%,100% 100%,0 100%,0 16%);border-radius:0 0 6px 6px;margin-bottom:6px}
.coll .use{font-size:.88rem;color:var(--muted)}
.coll:hover h3{color:var(--accent)}
.gu{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:10px 18px;align-items:center}
.gu svg.pi{width:40px;height:40px;color:var(--accent)}.gu p{margin:0}
@media (max-width:760px){.gu{grid-template-columns:auto minmax(0,1fr)}.gu .cta{grid-column:1/-1}}
.role{display:grid;grid-template-columns:auto minmax(0,1fr);gap:14px;align-items:center;text-decoration:none;color:var(--ink)}
.role svg.pi{width:36px;height:36px;color:var(--accent)}.role h3{margin:2px 0}.role p{margin:0;color:var(--muted)}
.role:hover h3{color:var(--accent)}
.band .eye{color:var(--on-accent);opacity:.85}.band h2{margin:4px 0 6px}
.wrap.hm{padding-block:40px}.wrap.hm.end{padding-bottom:56px}
.phero .tick{background:rgba(42,24,14,.46);border-color:rgba(255,243,228,.32);color:#FFF3E4;-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.phero .tick .k,.phero .tick i{color:#F4CC97}.phero .tick:hover{border-color:#F4CC97}
.btn.light2{background:transparent;color:var(--on-accent);border-color:var(--on-accent)}
'''

HOME_JS = r'''
fetch('gia-ca-phe.json',{cache:'no-store'}).then(r=>r.ok?r.json():null).then(j=>{if(!j||!j.days)return;
const f=n=>n.toLocaleString('vi-VN').replace(/,/g,'.'),by=k=>j.days.filter(x=>x[k[0]]&&x[k[0]][k[1]]).sort((a,b)=>a.date<b.date?-1:1).pop();
const v=by(['vn','lamdong']),w=by(['world','robusta']);if(v){const [y,m,d]=v.date.split('-');document.getElementById('tk-d').textContent=d+'/'+m;document.getElementById('tk-v').textContent=f(v.vn.lamdong)}
if(w)document.getElementById('tk-r').textContent=f(w.world.robusta)}).catch(()=>{});
'''

head_old = home_old[:home_old.index('<style>')]
STD_STYLE = '<style id="md-std">' + STD_CSS + '</style>'   # chuẩn hiển thị điện thoại/laptop (kit.STD_CSS)
# Ngôn ngữ mặc định (chị Ngân 25/11/2026): khách vào web lần đầu (gõ medili.vn, bấm link từ nơi khác) thấy trang chủ tiếng Anh.
# Ở lại tiếng Việt khi khách đã xem/chọn tiếng Việt (kit.COMMON_JS ghi 'medili-lang'), hoặc đi từ trang khác trong web
# (bấm nút ngôn ngữ, bấm về trang chủ). Đã xem tiếng Nhật/Trung thì mở trang chủ tiếng đó. Bản en/ja/zh bỏ đoạn này (i18n.localize).
LANG_GO = ('<script id="md-lang-go">(()=>{let s=null,i=false;try{s=localStorage.getItem("medili-lang")}catch(e){}'
           'try{i=!!document.referrer&&new URL(document.referrer).origin===location.origin}catch(e){}'
           'if(s==="vi"||i)return;const t=s==="ja"||s==="zh"?s:"en";window.MD_GO=1;'
           'location.replace(t+"/"+(/(^|[.])medili[.]vn$/.test(location.hostname)?"":"index.html")+location.search+location.hash)})();</script>')
HOME_HEAD = LANG_GO + head_old + '<style>' + HOME_CSS_OLD + '</style>\n<style>' + CORE_CSS + NEW_CSS + anhvuon.PHOTO_CSS + HOME_CSS + '</style>' + STD_STYLE
HOME_TAIL = nb(HOME_BODY) + '<script>' + COMMON_JS + HOME_JS + '</script>\n'
HOME = HOME_HEAD + HOME_TAIL
assert '<div class="mnav">' not in HOME

# Trang chủ có hai bản:
# - artifact-main/index.html: bản mảnh để đăng artifact; khung artifact tự thêm doctype, charset, viewport.
# - site-new4/index.html: bản đầy đủ cho medili.vn. Phần đầu trang chép đúng khung artifact (như t5.js)
#   để trang hiển thị y như trên artifact. Thiếu charset utf-8 thì tiếng Việt trên hosting bị lỗi phông.
SKELETON_HEAD = ('<!doctype html><html lang="vi"><head><meta charset="utf-8">'
                 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
                 '<style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
                 'html{scroll-padding-top:env(safe-area-inset-top,0px)}'
                 'body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}'
                 'img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style>')
HOME_DESC = ('MeDili là nhà rang cà phê trên cao nguyên Di Linh, chọn Cà Sẻ Di Linh làm nguyên liệu gốc. '
             'MeDili rang cà phê cho gia đình, quán cà phê, nhà hàng và khách sạn.')
HOME_FULL = (SKELETON_HEAD + f'<meta name="description" content="{esc(HOME_DESC)}">'
             f'<meta property="og:title" content="MeDili · Cà phê Di Linh"><meta property="og:description" content="{esc(HOME_DESC)}">\n'
             + HOME_HEAD + '</head><body>' + HOME_TAIL + '</body></html>\n')

# ---------- ghi ra ----------
for f, s in {**NEW, **UPD, 'index.html': HOME_FULL}.items():
    s = nguon_tong_hop(s)
    if f != 'index.html' and 'id="md-std"' not in s:
        s = s.replace('</head>', STD_STYLE + '</head>', 1)
    open(os.path.join(OUT, f), 'w', encoding='utf8').write(s)
AM = os.path.join(HERE, '..', 'artifact-main')
os.makedirs(AM, exist_ok=True)
# khung xem trước trên Claude không tự mở thư mục: nút ngôn ngữ trỏ thẳng tới en/index.html
open(os.path.join(AM, 'index.html'), 'w', encoding='utf8').write(re.sub(r'href="(en|ja|zh)/"', r'href="\1/index.html"', nguon_tong_hop(HOME)))
shutil.copy(os.path.join(HERE, '..', 'run-check', 'gia-ca-phe.json'), os.path.join(OUT, 'gia-ca-phe.json'))
# Mô hình 3D trang Hướng dẫn pha: gộp art/hd3d.js với three.js (giấy phép MIT, giữ ở cuối file) thành một file assets/hd3d.js.
# Ảnh dự phòng assets/hd-*.webp (khi máy không chạy được 3D) chụp lại bằng: node hdshot.js
subprocess.run([os.path.join(HERE, 'node_modules', '.bin', 'esbuild'), os.path.join(HERE, 'hd3d.js'), '--bundle', '--format=esm', '--minify',
                '--target=es2020', '--legal-comments=eof', '--log-level=warning', '--outfile=' + os.path.join(OUT, 'assets', 'hd3d.js')], check=True)
# Thư viện dựng mã QR cho trang Thanh toán: qrcode-generator (Kazuhiko Arase, giấy phép MIT), nén lại, giữ dòng giấy phép ở đầu file.
subprocess.run([os.path.join(HERE, 'node_modules', '.bin', 'esbuild'), os.path.join(HERE, 'node_modules', 'qrcode-generator', 'dist', 'qrcode.js'), '--minify',
                '--target=es2017', '--log-level=warning', '--outfile=' + os.path.join(OUT, 'assets', 'qrcode.js')], check=True)
_qr = os.path.join(OUT, 'assets', 'qrcode.js')
_qrs = open(_qr, encoding='utf8').read()
open(_qr, 'w', encoding='utf8').write('/*! QR Code Generator for JavaScript (qrcode-generator 2.0.4) · Copyright (c) 2009 Kazuhiko Arase · MIT license · '
                                    'http://www.opensource.org/licenses/mit-license.php · QR Code is a registered trademark of DENSO WAVE INCORPORATED */\n' + _qrs)
# bản tiếng Anh, Nhật, Trung trong /en /ja /zh, dịch theo từ điển art/i18n (24/11/2026)
import i18n
for _l, _miss in i18n.build().items():
    if _miss:
        print('!!', _l, 'thiếu', len(_miss), 'đoạn dịch:', list(_miss)[:3])
shutil.rmtree(os.path.join(OUT, 'xx'), ignore_errors=True)
# chỉ mục cho trang Tìm kiếm, sơ đồ trang và robots cho medili.vn
open(os.path.join(OUT, 'tim-kiem.json'), 'w', encoding='utf8').write(cuahang.search_index(OUT))
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf8').write(cuahang.sitemap(OUT))
open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf8').write(cuahang.ROBOTS)
open(os.path.join(HERE, '_new_pages.txt'), 'w').write('\n'.join(sorted(NEW)))
tot = 0
for f in sorted(os.listdir(OUT)):
    n = os.path.getsize(os.path.join(OUT, f)); tot += n
    print(f'{f:28s} {n // 1024:4d} KB' + ('  (mới)' if f in NEW else ''))
print('tổng', tot // 1024, 'KB, trang mới', len(NEW), 'trang cũ cập nhật', len(UPD) + 1)

# Gộp toàn bộ nội dung web Manus vào site MeDili trên Claude.
# Đọc site-new3 (bản đang chạy), ghi site-new4: trang mới, trang chủ theo 8 chương, menu và chân trang mới trên mọi trang.
import os, re, json, shutil, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
import ill, pages_a, pages_b, chiet, coldbrew, traichin, visinh, huong, banhxe, phanbiet, nhanxanh, cuahang

os.makedirs(OUT, exist_ok=True)
rd = lambda f: open(os.path.join(BASE, f), encoding='utf8').read()

# ---------- danh mục 14 dòng từ Phòng Chọn Mua ----------
shop = rd('mua-hang.html')
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
# đối chiếu giá với Phòng Chọn Mua
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
                                       'Năm lớp bọc một hạt nhân, lớp nào được tách ra ở bước nào, và vì sao Natural, Honey, Washed cho vị khác nhau.', FEAT[0])),
    ('tu-vuon-den-ly.html', pages_b.jcard('tu-vuon-den-ly.html', 'Farm to cup', f'{M_F2C} phút đọc', 'Từ vườn đến ly',
                                          'Một ly cà phê đi qua những khâu nào, và với giá cà phê hôm nay, người trồng nhận bao nhiêu trong một ly 35.000 đ.', FEAT[1])),
    ('suc-khoe.html', pages_b.jcard('suc-khoe.html', 'Sức khoẻ', 'Có công cụ tính', 'Cà phê và cơ thể',
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
}
for f, a_ in pages_b.ART.items():
    NEW[f] = pages_b.article(f, a_, CARDS)
# Cửa hàng theo cấu trúc web medilinh.com: danh mục, 20 trang sản phẩm, giỏ hàng, tìm kiếm
SHOP, CATALOG = cuahang.pages(P)
NEW.update(SHOP)

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
           'len-men-men-bia.html': ('Ba cách sơ chế', 'Natural phơi nguyên trái, Honey giữ lớp nhớt, xát tươi tách vỏ trước khi lên men và rửa.', STRIP_SOCHE),
           'vuon.html': ('Vườn vào mùa', 'Robusta chín đỏ, thu hái rồi phơi.', STRIP_VUON)}
    if f in GAL:
        t, d, items = GAL[f]
        assert s.count('</header>') == 1, f
        s = s.replace('</header>', f'</header>\n<section class="pgal" aria-label="{t}"><h2>{t}</h2><p>{nb(d)}</p>{strip(items)}</section>', 1)
    if f == 'mua-hang.html':
        assert s.count("col:'#2F6B4A'") == 2 and s.count("col:'#3F7F5A'") == 1
        s = s.replace("col:'#2F6B4A'", "col:'#B5832F'").replace("col:'#3F7F5A'", "col:'#C9A15B'")
        assert s.count('</header>') == 1
        s = s.replace('</header>', '</header>\n<p class="note" style="margin:0 0 14px">Mua lẻ từng gói? Vào <a href="cua-hang.html" '
                      'style="color:var(--accent);font-weight:600">Cửa hàng MeDili</a>, thêm vào giỏ rồi gửi đơn. Phòng Chọn Mua giúp quán tính lượng dùng và giá sỉ.</p>', 1)
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
    ('#A23B24', 'Premium · Honey, washed', 'Robusta Premium', P['pp']['taste'], P['pp']['use'], f'Phin và máy · từ <b>{fm(min(pr("pp"), pr("mp")))} đ/kg</b>'),
    ('#B5832F', 'Premium · Cầu Đất', 'Arabica Premium', P['pa']['taste'], P['ma']['use'], f'Phin và máy · <b>{fm(pr("pa"))} đ/kg</b>'),
    ('#8A5A32', 'Premium · Robusta, Arabica', 'Blend 9:1 đến 5:5', 'Từ đậm cacao đến cân bằng, thơm, chua thanh', P['b73']['use'],
     f'Pha máy · <b>{fm(pr("b91"))}–{fm(pr("b55"))} đ/kg</b>'),
]
COLL_HREF = ['cua-hang.html?q=classic', 'cua-hang.html?q=robusta%20premium', 'cua-hang.html?loai=arabica', 'cua-hang.html?loai=blend']
coll = ''.join(f'<a class="box coll" href="{h}"><i class="bag" style="--c:{c}" aria-hidden="true"></i><span class="k">{k}</span><h3>{t}</h3>'
               f'<p>{taste}.</p><p class="use">{use}</p><div class="ft">{ft}</div></a>' for h, (c, k, t, taste, use, ft) in zip(COLL_HREF, COLL))

HOME_BODY = f'''{header('index.html')}
<div class="hero"><div class="hwrap">
  <div>{logo()}<p class="eye">Chương 01 · Nhà rang cà phê chuyên nghiệp</p>
  <h1>Từ gốc Cà Sẻ.<br><em>Đến nghệ thuật rang.</em></h1>
  <p class="sub">MeDili là nhà rang cà phê ở cao nguyên Di Linh, lấy Cà Sẻ Di Linh làm gốc. Vùng trồng canh tác từ năm 2010, xưởng rang tại Thôn 11, Xã Di Linh. Cà phê rang cho gia đình, quán, nhà hàng và khách sạn.</p>
  <div class="cta"><a class="btn main" href="cua-hang.html">Chọn cà phê</a><a class="btn" href="tim-gu.html">Tìm gu của bạn</a><a class="btn" href="horeca.html">Giải pháp HORECA</a></div>
  <a class="tick" href="gia-ca-phe.html"><span class="k">Giá cà phê <span id="tk-d">{ddmm(dl['date'])}</span></span><span>Nhân xô Lâm Đồng <b id="tk-v">{fm(dl['vn']['lamdong'])} đ/kg</b></span><span>Robusta London <b id="tk-r">{fm(dw['world']['robusta'])} USD/tấn</b></span><i>Xem bảng giá</i></a>
  </div>
  <a class="heroimg" href="vung-trong.html"><img src="assets/p-robusta-tay.jpg" alt="Chùm Robusta chín đỏ trên tay người hái" width="1500" height="1000"></a>
</div></div>
<div class="wrap hm">
<section class="p-sec" id="bo-suu-tap">
 <p class="eye">Chương 02 · Bộ sưu tập MeDili</p>
 <h2 class="p-h2">Bốn hương vị. <em>Một niềm mê.</em></h2>
 <p class="lead">Bốn nhóm cà phê rang mộc trên kệ MeDili. Mỗi nhóm có bản cho phin, cho máy, và giá sỉ theo lượng dùng mỗi tháng.</p>
 <div class="g4">{coll}</div>
 <div class="box gu"><div>{icon('gu')}</div><div><p class="eye">Tìm gu cà phê của bạn</p><p>Sáu câu hỏi ngắn. Không có đáp án đúng, chỉ có ly cà phê đúng gu.</p></div><div class="cta" style="margin:0"><a class="btn main" href="tim-gu.html">Bắt đầu khám phá</a><a class="btn" href="cua-hang.html">Xem đủ 20 dòng</a></div></div>
 <p class="note">Bảng giá đề xuất, chưa gồm 8 % VAT và phí vận chuyển. MeDili xác nhận khi đặt hàng.</p>
</section>

<section class="split">
 <div class="p-sec">
  <p class="eye">Chương 03 · Câu chuyện MeDili</p>
  <h2 class="p-h2" style="margin:0">Cà Sẻ Di Linh. <em>Nguồn gốc của niềm mê.</em></h2>
  <p>MeDili lấy Cà Sẻ Di Linh làm nền. Vùng trồng canh tác từ năm 2010, cây 15 năm tuổi, chăm theo hướng tự nhiên. Xưởng rang ở Thôn 11 nối nguyên liệu với người uống và các quán.</p>
  <blockquote class="quote">Nguồn gốc là nền tảng của mỗi mẻ rang.</blockquote>
  <div class="cta"><a class="btn main" href="cau-chuyen.html">Đọc câu chuyện MeDili</a></div>
 </div>
 <div class="p-sec">
  <p class="k">Những người giữ lửa cho hương vị</p>
  <a class="box role" href="doi-ngu.html">{icon('rang')}<div><span class="k">01 · Đọc nguyên liệu</span><h3>Đội ngũ rang xay</h3><p>Nguyên liệu, hồ sơ rang và hương vị.</p></div></a>
  <a class="box role" href="doi-ngu.html">{icon('ly')}<div><span class="k">02 · Mở vị trong tách</span><h3>Nghệ nhân barista</h3><p>Phin, espresso và gu của từng khách.</p></div></a>
  <div class="lnks"><a class="lnk" href="doi-ngu.html">Khám phá đội ngũ MeDili</a></div>
 </div>
</section>

<section class="box p-sec">
 <p class="eye">Chương 04 · Vùng đất Di Linh</p>
 <h2 class="p-h2" style="margin:0">Di Linh. <em>Nơi câu chuyện bắt đầu.</em></h2>
 <p class="lead" style="margin:0">Bốn vùng trồng, tổng {ha(TOTAL)} ha. Thêm {LINKED} ha liên kết tại Di Linh, tính riêng, không gộp vào {ha(TOTAL)} ha.</p>
 {photo('p-san-phoi-wide.jpg', 'Cà phê phơi trên sân giữa đồi', 'Phơi cà phê giữa đồi.', cls='pfw')}
 {pages_a.seg_block()}
 <div class="lnks"><a class="lnk" href="vung-trong.html">Khám phá vùng nguyên liệu</a><a class="lnk" href="{MAP_FARM}" target="_blank" rel="noopener">Chỉ đường đến xưởng rang ↗</a></div>
</section>

<section class="p-sec" id="hanh-trinh">
 <p class="eye">Chương 05 · Từ nông trại đến tách</p>
 <h2 class="p-h2">Một hành trình <em>trong từng tách cà phê.</em></h2>
 <p class="lead">Năm công đoạn mở ra hương vị. Mỗi chặng là một mô hình bạn có thể tự bấm, chỉnh thông số và xem cách làm.</p>
 {pages_a.trip()}
 <div class="pgal"><p class="k">Những lô lên men đặc biệt</p>{strip(STRIP_LM)}<div class="lnks" style="margin-top:0"><a class="lnk" href="len-men-trai-cay.html">Xem cỗ máy lên men trái cây</a><a class="lnk" href="xuong-rang.html">Xưởng rang &amp; năng lực</a></div></div>
</section>

<section class="band">
 <div><p class="eye">Coffee Solutions for HORECA</p><h2>Cho quán, nhà hàng, khách sạn</h2>
 <p>Nhân xanh, cà phê phin, pha máy và cold brew. Xưởng rang trung bình 20 tấn mỗi tháng, tối đa 60 tấn, đóng gói bán tự động.</p></div>
 <div class="cta" style="margin:0"><a class="btn light" href="horeca.html">Khám phá giải pháp</a><a class="btn light2" href="mua-hang.html">Tính giá mỗi ly</a></div>
</section>

<section class="box split">
 <div class="p-sec">
  <p class="eye">Chương 06 · MeDili Café</p>
  <h2 class="p-h2" style="margin:0">Một tách cà phê. <em>Một cuộc hẹn.</em></h2>
  <p>Công ty TNHH DSunfood ở 143 Phạm Văn Hai là điểm phân phối của MeDili tại TP.HCM và cũng là MeDili Café. Ghé để uống một ly, hỏi menu trong ngày, hoặc bàn chuyện cung cấp cà phê cho quán.</p>
  <p class="k">Hôm nay, bạn mê vị gì?</p>
  <div class="chips" style="margin-top:0"><span>Cà phê sữa đá Việt Nam</span><span>Cà phê phin</span><span>Cappuccino</span><span>Espresso</span></div>
  <p class="note">Menu gợi ý, gọi trước để xác nhận món trong ngày.</p>
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

<section class="p-sec">
 <p class="eye">Chương 08 · Hẹn nhau ở MeDili</p>
 <h2 class="p-h2">Một niềm mê để sẻ chia. <em>Một hành trình còn tiếp.</em></h2>
 <p class="k">Di Linh origin · Saigon soul</p>
 <div class="facts"><div><b>{ha(TOTAL)} ha</b><span>bốn vùng trồng ở Lâm Đồng</span></div><div><b>{LINKED} ha</b><span>liên kết tại Di Linh, tính riêng</span></div><div><b>2010</b><span>năm vùng trồng bắt đầu canh tác</span></div><div><b>14</b><span>dòng cà phê trên kệ</span></div></div>
 {pages_a.loc_cards()}
</section>
{contact_band()}
</div>
{footer('Medili Coffee Farm - Di Linh')}
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
.btn.light2{background:transparent;color:var(--on-accent);border-color:var(--on-accent)}
'''

HOME_JS = r'''
fetch('gia-ca-phe.json',{cache:'no-store'}).then(r=>r.ok?r.json():null).then(j=>{if(!j||!j.days)return;
const f=n=>n.toLocaleString('vi-VN').replace(/,/g,'.'),by=k=>j.days.filter(x=>x[k[0]]&&x[k[0]][k[1]]).sort((a,b)=>a.date<b.date?-1:1).pop();
const v=by(['vn','lamdong']),w=by(['world','robusta']);if(v){const [y,m,d]=v.date.split('-');document.getElementById('tk-d').textContent=d+'/'+m;document.getElementById('tk-v').textContent=f(v.vn.lamdong)+' đ/kg'}
if(w)document.getElementById('tk-r').textContent=f(w.world.robusta)+' USD/tấn'}).catch(()=>{});
'''

head_old = home_old[:home_old.index('<style>')]
HOME_HEAD = head_old + '<style>' + HOME_CSS_OLD + '</style>\n<style>' + CORE_CSS + NEW_CSS + HOME_CSS + '</style>'
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
HOME_DESC = ('MeDili là nhà rang cà phê ở cao nguyên Di Linh, lấy Cà Sẻ Di Linh làm gốc. '
             'Cà phê rang cho gia đình, quán, nhà hàng và khách sạn.')
HOME_FULL = (SKELETON_HEAD + f'<meta name="description" content="{esc(HOME_DESC)}">'
             f'<meta property="og:title" content="MeDili Coffee Di Linh"><meta property="og:description" content="{esc(HOME_DESC)}">\n'
             + HOME_HEAD + '</head><body>' + HOME_TAIL + '</body></html>\n')

# ---------- ghi ra ----------
for f, s in {**NEW, **UPD, 'index.html': HOME_FULL}.items():
    s = nguon_tong_hop(s)
    open(os.path.join(OUT, f), 'w', encoding='utf8').write(s)
AM = os.path.join(HERE, '..', 'artifact-main')
os.makedirs(AM, exist_ok=True)
open(os.path.join(AM, 'index.html'), 'w', encoding='utf8').write(nguon_tong_hop(HOME))
shutil.copy(os.path.join(HERE, '..', 'run-check', 'gia-ca-phe.json'), os.path.join(OUT, 'gia-ca-phe.json'))
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

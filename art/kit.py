# Bộ khung chung cho site MeDili sau khi gộp nội dung web Manus:
# menu 5 nhóm, chân trang, màu theo phong thủy (không xanh lá, không đen), icon, hàm dựng trang.
import os, re, html as H
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '..', 'site-new3')   # bản đang chạy
LIVE = os.path.join(HERE, '..', 'site-live')
OUT = os.path.join(HERE, '..', 'site-new4')

esc = lambda s: H.escape(s, quote=True)

# ---------- liên hệ (theo site Claude, chị Ngân chọn) ----------
PHONE, PHONE_RAW = '0966 770 788', '0966770788'
ZALO = 'https://zalo.me/3942166996018015136'
EMAIL = 'cafe@medili.vn'
ADDR_HCM = '143 Phạm Văn Hai, Phường Tân Sơn Nhất, Quận Tân Bình, TP.HCM'
ADDR_FARM = 'Thôn 11, Xã Di Linh, Lâm Đồng'
MAP_HCM = 'https://www.google.com/maps/search/?api=1&query=' + quote('143 Phạm Văn Hai, Tân Sơn Nhất, Tân Bình, Thành phố Hồ Chí Minh')
MAP_FARM = 'https://www.google.com/maps/search/?api=1&query=' + quote('Thôn 11, Xã Di Linh, Lâm Đồng, Việt Nam')
FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSfFnK1eOB8u1UJg-5mIVS_k9h7ElULoxnmVDvCEYVjeSLWS_w/viewform?usp=pp_url'
FORM_F = {'name': 'entry.1445823936', 'phone': 'entry.907299194', 'txt': 'entry.730970220'}

# ---------- vùng trồng (web Manus) ----------
AREAS = [('Tà Hine', 'Đức Trọng', 8.0), ('Tân Nghĩa', 'Di Linh', 4.0), ('Lộc Châu 3', 'Bảo Thuận, Di Linh', 3.0), ('Gia Bắc 2', 'Di Linh', 2.7)]
TOTAL, LINKED = 17.7, 50

def ha(v):
    return (('%.1f' % v).rstrip('0').rstrip('.')).replace('.', ',')

def fm(n):
    return f'{round(n):,}'.replace(',', '.')

def nb(s):
    """Khoảng trắng không ngắt giữa số và đơn vị."""
    return re.sub(r'(\d) (đ|kg|ha|tấn|g|ml|%|phút|giây|°C|ly|triệu|năm)(?=[\s<.,;:)/·]|$)', '\\1\u00a0\\2', s)

# ---------- phông và CSS gốc của site ----------
suc = open(os.path.join(LIVE, 'suc-khoe.html'), encoding='utf8').read()
SHARED = re.findall(r'<style>(.*?)</style>', suc, flags=re.S)[1]
FONTS = re.search(r'<link rel="preconnect" href="https://fonts.googleapis.com">\s*<link rel="preconnect"[^>]*>\s*<link rel="stylesheet"[^>]*>', suc).group(0)

# ---------- menu ----------
GROUPS = [
    ('MeDili', [('./', 'Trang chủ'), ('cau-chuyen.html', 'Câu chuyện MeDili'), ('doi-ngu.html', 'Đội ngũ'),
                ('quan-medili.html', 'Quán MeDili Café'), ('lien-he.html', 'Liên hệ')]),
    ('Vùng trồng & sản xuất', [('vung-trong.html', 'Vùng trồng Di Linh'), ('vuon.html', 'Vườn 12 tháng'), ('trai-ca-phe.html', 'Cấu tạo trái'),
                               ('len-men-men-bia.html', 'Lên men men bia'), ('len-men-trai-cay.html', 'Lên men trái cây')]),
    ('Rang & pha', [('xuong-rang.html', 'Xưởng rang & năng lực'), ('rang.html', 'Phòng rang'), ('quay-pha.html', 'Quầy pha'),
                    ('cold-brew.html', 'Cỗ máy Cold Brew'), ('tim-gu.html', 'Tìm gu cà phê')]),
    ('Mua & hợp tác', [('mua-hang.html', 'Phòng Chọn Mua'), ('horeca.html', 'Giải pháp HORECA'), ('nhan-xanh.html', 'Chọn nhân xanh · khách sỉ'),
                       ('gia-ca-phe.html', 'Giá cà phê hôm nay'), ('giao-hang.html', 'Giao hàng & đổi trả')]),
    ('Kiến thức cà phê', [('journal.html', 'Tất cả bài viết'), ('chiet-xuat.html', 'Cỗ máy Chiết xuất'), ('phan-biet-ca-phe.html', 'Cỗ máy Phân biệt cà phê'), ('trai-chin.html', 'Cỗ máy Trái chín'),
                        ('vi-sinh.html', 'Cỗ máy Vi sinh'), ('tien-chat-huong.html', 'Cỗ máy Tiền chất hương'), ('banh-xe-huong.html', 'Bánh xe hương MeDili'),
                        ('journal-phin.html', 'Phin và nhịp rơi của thời gian'),
                        ('journal-tu-qua.html', 'Từ quả cà phê đến hương vị'), ('journal-di-linh.html', 'Di Linh trong một tách cà phê'),
                        ('tu-vuon-den-ly.html', 'Từ vườn đến ly'), ('suc-khoe.html', 'Cà phê và cơ thể')]),
]
PRIMARY = [('cau-chuyen.html', 'Câu chuyện'), ('vung-trong.html', 'Vùng trồng'), ('xuong-rang.html', 'Xưởng rang'),
           ('horeca.html', 'HORECA'), ('quan-medili.html', 'Quán MeDili'), ('journal.html', 'Kiến thức'), ('gia-ca-phe.html', 'Giá cà phê')]


def _cur(href, current):
    return ' aria-current="page"' if (href == current or (href == './' and current == 'index.html')) else ''


def header(current):
    prim = ''.join(f'<a href="{h}"{_cur(h, current)}>{t}</a>' for h, t in PRIMARY)
    cols = ''.join('<div class="mh-c"><p class="mh-g">' + g + '</p><ul>' +
                   ''.join(f'<li><a href="{h}"{_cur(h, current)}>{t}</a></li>' for h, t in items) + '</ul></div>' for g, items in GROUPS)
    return (f'<div class="mh"><div class="mh-in"><a class="mh-b" href="./">MeDili Café</a>'
            f'<nav class="mh-p" aria-label="Mục chính">{prim}</nav>'
            f'<details class="mh-m" id="mhm"><summary><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg><span>Menu</span></summary>'
            f'<nav class="mh-pan" aria-label="Tất cả trang"><div class="mh-grid">{cols}</div></nav></details>'
            f'<a class="mh-go" href="mua-hang.html"{_cur("mua-hang.html", current)}>Chọn mua</a></div></div>')


FOOT_EXPLORE = [('cau-chuyen.html', 'Câu chuyện MeDili'), ('doi-ngu.html', 'Đội ngũ MeDili'), ('vung-trong.html', 'Vùng trồng Di Linh'),
                ('xuong-rang.html', 'Xưởng rang & năng lực'), ('rang.html', 'Phòng rang'), ('quay-pha.html', 'Quầy pha'),
                ('tim-gu.html', 'Tìm gu cà phê'), ('chiet-xuat.html', 'Cỗ máy Chiết xuất'), ('cold-brew.html', 'Cỗ máy Cold Brew'),
                ('journal.html', 'Kiến thức cà phê')]
FOOT_YOU = [('mua-hang.html', 'Phòng Chọn Mua'), ('horeca.html', 'Giải pháp HORECA'), ('nhan-xanh.html', 'Nhân xanh cho khách sỉ'), ('gia-ca-phe.html', 'Giá cà phê hôm nay'),
            ('quan-medili.html', 'Quán MeDili Café'), ('lien-he.html', 'Liên hệ & bản đồ'), ('giao-hang.html', 'Giao hàng & đổi trả'),
            ('bao-mat.html', 'Chính sách bảo mật')]


def footer(sig='Medili - Farm Robusta Cà Sẻ Di Linh'):
    a = lambda L: ''.join(f'<a href="{h}">{t}</a>' for h, t in L)
    return (f'<footer class="mf"><div class="mf-in">'
            f'<div class="mf-cta"><span class="mf-k">A little coffee, a lot of connection</span>'
            f'<p class="mf-h">Luôn có thời gian cho <em>một tách cà phê ngon.</em></p>'
            f'<a class="btn main" href="quan-medili.html">Hẹn nhau ở MeDili</a></div>'
            f'<div class="mf-grid">'
            f'<div class="mf-brand"><b>Mê Cà Phê, Mê Di Linh.</b><span>Gìn giữ di sản. Chắt chiu từng hương vị.</span><small>Di Linh · Lâm Đồng · Việt Nam</small></div>'
            f'<nav class="mf-col" aria-label="Khám phá"><p class="mf-t">Khám phá</p>{a(FOOT_EXPLORE)}</nav>'
            f'<nav class="mf-col" aria-label="MeDili và bạn"><p class="mf-t">MeDili &amp; bạn</p>{a(FOOT_YOU)}</nav>'
            f'<div class="mf-col"><p class="mf-t">Phân phối · DSunfood</p>'
            f'<p>Công ty TNHH DSunfood<br>{ADDR_HCM}</p><p>Farm &amp; xưởng rang<br>{ADDR_FARM}</p>'
            f'<p><span class="mf-n">{PHONE}</span> · <span class="mf-n">{EMAIL}</span></p>'
            f'<a href="{MAP_HCM}" target="_blank" rel="noopener">Chỉ đường đến MeDili ↗</a><a href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo MeDili ↗</a></div>'
            f'</div><div class="mf-base"><span>© 2026 MeDili Café</span><i>{sig}</i></div></div></footer>')


def contact_band():
    return (f'<section class="contact" id="lien-he"><div><img class="lgK" src="assets/logo-kem.png" alt="MeDili Café Di Linh" width="260" height="83">'
            f'<div class="tagline">Mê vị Di Linh</div>'
            f'<p>Phân phối: Công ty TNHH DSunfood, {ADDR_HCM}.<br>Farm và xưởng rang: {ADDR_FARM}.</p></div>'
            f'<div class="zalo"><span>Zalo MeDili</span><strong data-sel>{PHONE}</strong>'
            f'<div><a href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo</a><button type="button" data-copy="{PHONE_RAW}" data-done="Đã sao chép số">Sao chép số</button></div>'
            f'<small>Email: {EMAIL}</small></div></section>')


def logo():
    return ('<span class="lgw"><img class="lgL" src="assets/logo-mau.png" alt="MeDili Café Di Linh" width="240" height="77">'
            '<img class="lgD" src="assets/logo-kem.png" alt="MeDili Café Di Linh" width="240" height="77"></span>')


# ---------- icon nét 24 px ----------
ICON = {
    'vuon': '<path d="M12 21v-6"/><circle cx="12" cy="9" r="6"/><circle cx="10" cy="8" r="1.1" class="fi"/><circle cx="14" cy="10.5" r="1.1" class="fi"/><circle cx="11" cy="12" r="1.1" class="fi"/>',
    'trai': '<path d="M10 11c0-4 3-6.5 7-8M15.5 9.5c.3-2.2-.2-4.2-1-6"/><circle cx="9" cy="15.5" r="4.2" class="fi"/><circle cx="16.5" cy="13.5" r="4"/>',
    'soche': '<path d="M12 3s5 6 5 10a5 5 0 0 1-10 0c0-4 5-10 5-10z"/><path d="M10 14a2 2 0 0 0 2 2"/>',
    'rang': '<circle cx="11" cy="12" r="6"/><path d="M11 6V3M17 12h4M5 21h12M9 9.5c1.5 1 2 3.5 4 5"/>',
    'ly': '<path d="M5 9h11v5a5 5 0 0 1-5 5h-1a5 5 0 0 1-5-5z"/><path d="M16 11h2a2 2 0 0 1 0 4h-2M8 3v3M11 3v3"/>',
    'xe': '<path d="M2 7h12v9H2zM14 10h4l3 3v3h-7"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/>',
    'nguoi': '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/>',
    'nhan': '<path d="M7.5 4h9l-1.2 3c3 2.2 4 6 3.2 10.2A3 3 0 0 1 15.6 20H8.4a3 3 0 0 1-2.9-2.8C4.7 13 5.7 9.2 8.7 7z"/><path d="M8.6 7h6.8"/><ellipse class="fi" cx="12" cy="13.6" rx="2" ry="3"/>',
    'phin': '<path d="M6 4h12M7.5 4l1.2 6.5h6.6L16.5 4"/><path d="M4.5 10.5h15"/><path d="M8 13h8v4.5a3.5 3.5 0 0 1-3.5 3.5h-1A3.5 3.5 0 0 1 8 17.5z"/><path class="fi" d="M11.2 12.2h1.6v1.6h-1.6z"/>',
    'may': '<rect x="4" y="3" width="16" height="5" rx="1.2"/><path d="M6 8v13h12V8"/><path d="M8.5 11h7v2.2a3.5 3.5 0 0 1-7 0z"/><path d="M10 18.5h4"/>',
    'lanh': '<path d="M8.5 3h7M9.5 3v3L7 8.8V19a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V8.8L14.5 6V3"/><path d="M7 12h10"/><rect class="fi" x="9.4" y="14.3" width="2.8" height="2.8" rx=".6"/><rect class="fi" x="12.6" y="16.4" width="2.4" height="2.4" rx=".6"/>',
    'kinh': '<circle cx="10.5" cy="10.5" r="6.2"/><path d="M15 15l5.5 5.5"/><ellipse class="fi" cx="10.5" cy="10.5" rx="2" ry="3"/>',
    'so': '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V2.8h6V4M8.5 9.5h7M8.5 13h7M8.5 16.5h4"/>',
    'lua': '<path d="M12 3c1 4 6 6 6 11a6 6 0 0 1-12 0c0-3 2-4.5 3-6.5 1 2 2 2.4 3 2.5.3-3-1-5 0-7z"/>',
    'no': '<ellipse cx="12" cy="12" rx="4" ry="6.3"/><path d="M12 5.8c-1.2 3 1.2 9.2 0 12.4M4.5 9v6M19.5 9v6M2 11v2M22 11v2"/>',
    'quat': '<circle cx="12" cy="12" r="8.5"/><path d="M12 12c0-4 1.8-6 4.2-6M12 12c4 0 6 1.8 6 4.2M12 12c0 4-1.8 6-4.2 6M12 12c-4 0-6-1.8-6-4.2"/>',
    'tui': '<path d="M6 7.5h12L19.2 21H4.8z"/><path d="M8.5 7.5V4.5h7v3"/><circle class="fi" cx="12" cy="13" r="1.7"/>',
    'ghim': '<path d="M12 21.5s-6.5-6.2-6.5-11.5a6.5 6.5 0 0 1 13 0c0 5.3-6.5 11.5-6.5 11.5z"/><circle cx="12" cy="10" r="2.3"/>',
    'dt': '<rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M11 18.2h2"/>',
    'thu': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 7l8.5 6 8.5-6"/>',
    'chat': '<path d="M4 4.5h16v11.5H9.5L5 20.2V16H4z"/><path d="M8 8.7h8M8 12h5"/>',
    'nui': '<path d="M2 19.5l6.2-9.2 4.1 5 3-4L22 19.5z"/><circle class="fi" cx="17.5" cy="5.8" r="2.2"/>',
    'tim': '<path d="M12 20.3s-7.5-4.7-7.5-10.4A4.2 4.2 0 0 1 12 7.3a4.2 4.2 0 0 1 7.5 2.6c0 5.7-7.5 10.4-7.5 10.4z"/>',
    'khien': '<path d="M12 2.8l7.5 3V12c0 4.6-3.1 7.7-7.5 9.2C7.6 19.7 4.5 16.6 4.5 12V5.8z"/><path d="M8.8 12.2l2.3 2.3 4.3-4.6"/>',
    'phoi': '<circle cx="12" cy="7" r="3"/><path d="M12 1.5v1M5.2 4.2l.8.8M18.8 4.2l-.8.8M3 17h18M6 17l1.2 4M18 17l-1.2 4M5.5 21h13"/>',
    'gu': '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle class="fi" cx="12" cy="12" r="1.6"/>',
    'hen': '<rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 9.5h17M8 3v4M16 3v4"/><circle class="fi" cx="12" cy="14.8" r="1.8"/>',
    'mua': '<path d="M5 8h14l-1.2 12.5H6.2z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/>',
    'cung': '<path d="M3 12h4l2.5-6 5 12 2.5-6h4"/>',
    'can': '<path d="M12 4v15M6 20h12M5 7h14"/><path d="M5 7l-3 6h6zM19 7l-3 6h6z"/>',
    'doi': '<path d="M4 9h13l-3.5-3.5M20 15H7l3.5 3.5"/>',
    'visinh': '<ellipse cx="12" cy="12" rx="7.6" ry="4.8" transform="rotate(-30 12 12)"/><circle class="fi" cx="10.2" cy="11.6" r="1.3"/><circle class="fi" cx="14" cy="12.8" r="1"/><path d="M4.6 17.6l-2.4 2M19.4 6.4l2.4-2"/>',
    'phantu': '<circle cx="6" cy="16.5" r="2.6"/><circle cx="12" cy="6.5" r="2.6"/><circle class="fi" cx="18" cy="16.5" r="2.6"/><path d="M7.4 14.2l3.2-5.4M13.4 8.8l3.2 5.4M8.6 16.5h6.8"/>',
    'banhxe': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.2"/><path d="M12 3v5.8M12 15.2V21M3 12h5.8M15.2 12H21M5.6 5.6l4.1 4.1M14.3 14.3l4.1 4.1M18.4 5.6l-4.1 4.1M9.7 14.3l-4.1 4.1"/>',
    'la': '<path d="M5 19c0-8.5 5.2-13.6 14.5-14.5C18.6 13.8 13.5 19 5 19z"/><path d="M5 19l8.5-8.5"/>',
    'soi': '<ellipse cx="7" cy="12" rx="4.2" ry="6.6"/><path d="M7 6.8v10.4"/><ellipse cx="17" cy="12" rx="4.2" ry="6.6"/><path d="M17 6.6c2.6 3-2.6 7.2 0 10.8"/>',
}


# ---------- ảnh thật ----------
def _psize(name):
    from PIL import Image
    return Image.open(os.path.join(OUT, 'assets', name)).size


def photo(name, alt, cap='', cls='', lazy=True):
    w, h = _psize(name)
    lz = ' loading="lazy"' if lazy else ''
    fc = f'<figcaption>{cap}</figcaption>' if cap else ''
    return f'<figure class="pf {cls}"><img src="assets/{name}" alt="{esc(alt)}" width="{w}" height="{h}"{lz}>{fc}</figure>'


def strip(items):
    return '<div class="pfs">' + ''.join(photo(*it) for it in items) + '</div>'


STRIP_LM = [('p-lm-nhan.jpg', 'Cà phê trái chín đổ chung với cùi nhãn', 'Đồng lên men với nhãn.'),
            ('p-lm-dau-tam.jpg', 'Dâu tằm nghiền đổ lên cà phê trái chín', 'Đồng lên men với dâu tằm.'),
            ('p-lm-chanh-day.jpg', 'Ruột chanh dây đổ lên cà phê trái chín', 'Đồng lên men với chanh dây.')]
STRIP_SOCHE = [('p-natural.jpg', 'Trái cà phê phơi nguyên trái trên giàn', 'Natural: phơi nguyên trái trên giàn.'),
               ('p-honey.jpg', 'Hạt cà phê còn lớp nhớt phơi trên giàn', 'Honey: hạt còn lớp nhớt, phơi trên giàn.'),
               ('p-xat-tuoi.jpg', 'Máy xát tươi tách vỏ cà phê', 'Xát tươi: máy tách vỏ khỏi hạt.')]
STRIP_VUON = [('p-sq-canh.jpg', 'Robusta chín đỏ trên cành', 'Robusta chín đỏ trên cành.'),
              ('p-sq-tay.jpg', 'Chùm Robusta chín trên tay người hái', 'Chùm Robusta vào mùa thu hái.'),
              ('p-sq-san-phoi.jpg', 'Cà phê phơi trên sân giữa đồi', 'Phơi cà phê giữa đồi.')]


def icon(k, cls='pi'):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICON[k]}</svg>'


# ---------- CSS chung ----------
CORE_CSS = r'''
/* Khung chung sau khi gộp Manus: menu nhóm, chân trang, màu phong thủy Thổ (nâu, vàng đất, đỏ; không xanh lá, không đen). */
:root{--moss:#8D4E22;--good:#8D4E22;
  --i-red:#B33A24;--i-red2:#7A2414;--i-gold:#D9B77E;--i-gold2:#B8894A;--i-coffee:#6B4226;--i-brown:#8D5A32;--i-milk:#E9D3AE;
  --seg1:#9E3B26;--seg2:#B8894A;--seg3:#6B4226;--seg4:#D9B77E;--seg-t1:#FFF6EC;--seg-t2:#2E1C12;--cmp2:#C9A46A;
  --cx1:#BB8526;--cx2:#7A348E;--cx3:#83470D;--cx4:#CB4D54}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--moss:#E2A774;--good:#E2A774;--accent:#E27A5E;--on-accent:#2B120C;
  --bg:#231812;--panel:#2D2018;--tint:#3B2A1F;--rule:#574434;
  --i-red:#C8553D;--i-red2:#8E3020;--i-gold:#CDA769;--i-gold2:#C0904F;--i-coffee:#A06C45;--i-brown:#A36B3E;--i-milk:#D9C19A;
  --seg1:#C0553A;--seg2:#CF9A55;--seg3:#8E5D38;--seg4:#E2C48E;--cmp2:#B08A55;
  --cx1:#B88B23;--cx2:#A06BCD;--cx3:#904E0A;--cx4:#D54E5B}}
:root[data-theme="dark"]{--moss:#E2A774;--good:#E2A774;--accent:#E27A5E;--on-accent:#2B120C;
  --bg:#231812;--panel:#2D2018;--tint:#3B2A1F;--rule:#574434;
  --i-red:#C8553D;--i-red2:#8E3020;--i-gold:#CDA769;--i-gold2:#C0904F;--i-coffee:#A06C45;--i-brown:#A36B3E;--i-milk:#D9C19A;
  --seg1:#C0553A;--seg2:#CF9A55;--seg3:#8E5D38;--seg4:#E2C48E;--cmp2:#B08A55;
  --cx1:#B88B23;--cx2:#A06BCD;--cx3:#904E0A;--cx4:#D54E5B}
html{scroll-padding-top:calc(70px + env(safe-area-inset-top,0px))}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:60;background:var(--panel)}
.mnav{display:none!important}

/* menu */
.mh{position:sticky;top:env(safe-area-inset-top,0px);z-index:50;background:var(--panel);border-bottom:1px solid var(--rule)}
.mh-in{max-width:1560px;margin:auto;display:flex;align-items:center;gap:8px 14px;padding-block:8px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.mh-b{font:700 1rem var(--body);color:var(--accent);text-decoration:none;white-space:nowrap;margin-right:auto}
.mh-p{display:flex;gap:4px 18px;font:600 .88rem var(--body)}
.mh-p a{color:var(--ink);text-decoration:none;white-space:nowrap;padding:5px 1px;border-bottom:2px solid transparent}
.mh-p a:hover{color:var(--accent)}
.mh-p a[aria-current="page"]{color:var(--accent);border-color:var(--accent)}
.mh-m{margin:0;font-size:inherit}
.mh-m>summary{list-style:none;display:flex;align-items:center;gap:6px;cursor:pointer;font:600 .86rem var(--body);color:var(--ink);border:1px solid var(--rule);border-radius:999px;padding:6px 12px;white-space:nowrap;user-select:none}
.mh-m>summary::-webkit-details-marker{display:none}
.mh-m>summary svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round}
.mh-m[open]>summary{background:var(--ink);border-color:var(--ink);color:var(--panel)}
.mh-m>summary:focus-visible{outline:3px solid var(--moss);outline-offset:2px}
.mh-pan{position:absolute;left:0;right:0;top:100%;background:var(--panel);border-bottom:1px solid var(--rule);box-shadow:0 18px 30px rgba(46,28,18,.16);max-height:calc(100vh - 60px - env(safe-area-inset-top,0px));overflow:auto;overscroll-behavior:contain}
.mh-grid{max-width:1560px;margin:auto;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:18px 26px;padding-block:18px 24px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.mh-g{margin:0 0 6px;font:600 .72rem/1.3 var(--body);letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
.mh-c ul{list-style:none;margin:0;padding:0;display:grid;gap:1px}
.mh-c a{display:block;color:var(--ink);text-decoration:none;font:500 .95rem/1.35 var(--body);padding:6px 0;border-bottom:1px solid transparent}
.mh-c a:hover{color:var(--accent)}
.mh-c a[aria-current="page"]{color:var(--accent);font-weight:700}
.mh-go{background:var(--accent);color:var(--on-accent);padding:7px 14px;border-radius:999px;text-decoration:none;font:600 .86rem var(--body);white-space:nowrap}
.mh-go[aria-current="page"]{box-shadow:0 0 0 2px var(--panel),0 0 0 4px var(--accent)}
@media (max-width:1260px){.mh-p{display:none}}
@media (max-width:980px){.mh-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.mh-grid{grid-template-columns:minmax(0,1fr);gap:14px}.mh-c a{padding:8px 0;font-size:1rem}.mh-b{font-size:.95rem}}

/* chân trang */
.mf{font:400 .9rem/1.6 var(--body);text-align:left;color:var(--ink);background:var(--tint);margin-top:28px;padding:0}
.mf-in{max-width:1560px;margin:auto;padding-block:30px 22px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:grid;gap:26px}
.mf-cta{display:flex;flex-wrap:wrap;align-items:center;gap:10px 24px;border-bottom:1px solid var(--rule);padding-bottom:24px}
.mf-k{flex-basis:100%;font:600 .72rem var(--body);letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
.mf-h{margin:0;font:italic 600 clamp(1.5rem,3.4vw,2.2rem)/1.2 var(--sign);color:var(--ink);text-wrap:balance}
.mf-h em{color:var(--accent)}
.mf-grid{display:grid;grid-template-columns:minmax(0,1.3fr) repeat(3,minmax(0,1fr));gap:22px 30px}
.mf-brand b{display:block;font:italic 600 1.35rem/1.25 var(--sign);color:var(--accent)}
.mf-brand span{display:block;margin-top:6px}.mf-brand small{display:block;margin-top:6px;color:var(--muted);letter-spacing:.06em}
.mf-t{margin:0 0 6px;font:600 .72rem var(--body);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
.mf-col{display:flex;flex-direction:column;gap:3px;min-width:0}
.mf-col a{color:var(--ink);text-decoration:none;padding:2px 0}.mf-col a:hover{color:var(--accent);text-decoration:underline}
.mf-col p{margin:0 0 6px}.mf-n{white-space:nowrap;user-select:all}
.mf-base{display:flex;flex-wrap:wrap;justify-content:space-between;gap:6px 18px;border-top:1px solid var(--rule);padding-top:14px;color:var(--muted);font-size:.84rem}
.mf-base i{font:italic 600 1rem var(--sign);color:var(--accent)}
@media (max-width:980px){.mf-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.mf-brand{grid-column:1/-1}}
@media (max-width:520px){.mf-grid{grid-template-columns:minmax(0,1fr)}}

/* ảnh thật */
.pf{margin:0;display:grid;gap:6px;min-width:0;align-content:start}
.pf img{display:block;width:100%;height:auto;max-width:100%;border-radius:14px;border:1px solid var(--rule);background:var(--tint)}
.pf figcaption{font:400 .84rem/1.4 var(--body);color:var(--muted)}
.pfw img{aspect-ratio:3/1;object-fit:cover}
.split .pf img{max-height:560px;object-fit:cover}
@media (max-width:700px){.pfw img{aspect-ratio:2/1}}
.pfs{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
@media (max-width:700px){.pfs{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:78%;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:6px}.pfs>.pf{scroll-snap-align:start}}
.pgal{display:grid;gap:10px}
.pgal>h2{margin:0}
.pgal>p{margin:0;color:var(--muted);max-width:72ch}

'''

NEW_CSS = r'''
/* thành phần dùng chung cho trang mới */
.wrap.art{max-width:980px}
.k{font:600 .72rem/1.3 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0}
.eye{font:600 .8rem/1.3 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin:0}
section>h2 em,.p-h2 em{font-style:normal;color:var(--accent)}
.p-h2{font:800 2.05rem/1.15 var(--display);margin:4px 0 6px;letter-spacing:.01em;text-wrap:balance}
.p-head{display:grid;gap:4px}
.p-head h1{margin:6px 0 0}
.p-head .lead{font-size:1.06rem;color:var(--muted);max-width:68ch;margin:10px 0 0}
.p-sig{font:italic 600 1.25rem var(--sign);color:var(--accent);margin:10px 0 0}
.cta{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
a.btn{text-decoration:none;display:inline-block}
.btn.ghost{border-color:var(--rule)}
.p-sec{display:grid;gap:10px}
.p-sec>.lead{margin:0;max-width:72ch;color:var(--muted)}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}
.facts>div{border-top:2px solid var(--accent);padding-top:8px;min-width:0}
.facts b{display:block;font:800 2.4rem/1.05 var(--display);color:var(--accent)}
.facts span{display:block;color:var(--muted);font-size:.88rem;margin-top:2px}
.g2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.g3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.g4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
@media (max-width:1100px){.g4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:900px){.g3{grid-template-columns:minmax(0,1fr)}}
@media (max-width:760px){.g2{grid-template-columns:minmax(0,1fr)}}
@media (max-width:560px){.g4{grid-template-columns:minmax(0,1fr)}}
.box{background:var(--panel);border:1px solid var(--rule);border-radius:16px;padding:18px 20px;min-width:0}
.box h3{font:800 1.45rem/1.15 var(--display);margin:4px 0 6px;letter-spacing:.01em}
.box p{margin:0 0 8px}.box p:last-child{margin-bottom:0}
.box .k{font:600 .72rem/1.3 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.box .ft{margin-top:10px;padding-top:10px;border-top:1px solid var(--rule);font-size:.88rem;color:var(--muted)}
.box .ft b{color:var(--ink)}
.box>svg.pi{width:34px;height:34px;color:var(--accent)}
svg.pi{width:26px;height:26px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;flex:none}
svg.pi .fi{fill:var(--accent);stroke:none}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.chips span{font:600 .76rem var(--body);border:1px solid var(--rule);border-radius:999px;padding:4px 10px;color:var(--ink)}
.lnk{color:var(--accent);font-weight:600;text-decoration:none}.lnk:hover{text-decoration:underline}
.lnks{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:10px}
.quote{margin:0;font:italic 600 clamp(1.4rem,3vw,2.1rem)/1.3 var(--sign);color:var(--accent);max-width:34ch;text-wrap:balance}
.split{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:20px 30px;align-items:center}
.split img{display:block;width:100%;height:auto;border-radius:14px;border:1px solid var(--rule)}
.illw{max-width:320px;width:100%;justify-self:center}
@media (max-width:820px){.split{grid-template-columns:minmax(0,1fr)}.illw{max-width:210px}}
.pst{list-style:none;margin:0;padding:0;display:grid;gap:12px;counter-reset:st}
.pst>li{display:grid;grid-template-columns:52px minmax(0,1fr);gap:4px 16px;align-items:start;background:var(--panel);border:1px solid var(--rule);border-radius:14px;padding:14px 16px;min-width:0}
.pst>li .n{grid-row:1/3;display:grid;place-items:center;width:44px;height:44px;border-radius:50%;background:var(--tint);color:var(--accent)}
.pst>li .n svg{width:24px;height:24px}
.pst h3{margin:0;font:700 1.05rem/1.3 var(--body)}
.pst h3 small{font:600 .74rem var(--body);letter-spacing:.06em;color:var(--muted);margin-right:6px}
.pst p{margin:0;font-size:.93rem}
.pst.two{grid-template-columns:repeat(2,minmax(0,1fr))}
.pst.three{grid-template-columns:repeat(3,minmax(0,1fr))}
@media (max-width:900px){.pst.three{grid-template-columns:minmax(0,1fr)}}
@media (max-width:760px){.pst.two{grid-template-columns:minmax(0,1fr)}}
.trip{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}
.trip a{display:flex;flex-direction:column;height:100%;background:var(--panel);border:1px solid var(--rule);border-radius:14px;overflow:hidden;color:var(--ink);text-decoration:none}
.trip img{display:block;width:100%;height:auto;aspect-ratio:3/2;object-fit:cover;max-width:100%}
.trip b{font:800 1.25rem/1.15 var(--display);padding:10px 14px 0}
.trip b small{display:block;font:600 .72rem var(--body);letter-spacing:.08em;color:var(--accent);margin-bottom:2px}
.trip span{padding:4px 14px 14px;color:var(--muted);font-size:.88rem}
.trip a:hover b{color:var(--accent)}
@media (max-width:1180px){.trip{grid-template-columns:none;grid-auto-flow:column;grid-auto-columns:minmax(240px,32%);overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:6px}.trip li{scroll-snap-align:start}}
@media (max-width:640px){.trip{grid-auto-flow:row;grid-auto-columns:auto;grid-template-columns:minmax(0,1fr);overflow:visible}}
.seg{display:flex;gap:2px;height:28px;margin:6px 0 4px}
.seg i{display:flex;align-items:center;padding:0 8px;border-radius:4px;font:700 .78rem var(--mono);font-style:normal;white-space:nowrap;overflow:hidden;min-width:0}
.seg i.s1{background:var(--seg1);color:var(--seg-t1)}.seg i.s2{background:var(--seg2);color:var(--seg-t2)}
.seg i.s3{background:var(--seg3);color:var(--seg-t1)}.seg i.s4{background:var(--seg4);color:var(--seg-t2)}
.areas{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin-top:8px}
.areas>div{border-top:1px solid var(--rule);padding-top:10px;min-width:0}
.areas .sw{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.areas b{font:700 1rem var(--body)}.areas span{display:block;color:var(--muted);font-size:.86rem}
.areas strong{display:block;font:800 1.9rem/1.1 var(--display);margin-top:4px}
.areas strong small{font:600 .8rem var(--body);color:var(--muted);margin-left:6px}
@media (max-width:900px){.areas{grid-template-columns:repeat(2,minmax(0,1fr))}}
.cmp{display:grid;gap:10px;margin-top:8px}
.cmp>div{display:grid;grid-template-columns:150px minmax(0,1fr);gap:12px;align-items:center}
.cmp span{font-size:.88rem}.cmp span b{display:block;font-size:.95rem}
.cmp .tr{position:relative;height:24px;margin-right:64px}
.cmp .tr i{position:absolute;left:0;top:0;bottom:0;border-radius:0 4px 4px 0;background:var(--accent)}
.cmp .tr i.b{background:var(--cmp2)}
.cmp .tr em{position:absolute;top:50%;transform:translateY(-50%);font:700 .9rem var(--mono);font-style:normal;color:var(--ink);white-space:nowrap}
@media (max-width:520px){.cmp>div{grid-template-columns:minmax(0,1fr)}}
.loc{display:grid;gap:4px}
.loc .ttl{display:flex;gap:10px;align-items:center}
.loc .ttl svg{color:var(--accent)}
.sel{user-select:all}
.cp{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:8px}
.cp strong{font:700 1.25rem var(--mono);user-select:all;overflow-wrap:anywhere}
.note{font-size:.86rem;color:var(--muted);margin:0}
.p-form{display:grid;gap:12px}
.p-form .row2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
@media (max-width:620px){.p-form .row2{grid-template-columns:minmax(0,1fr)}}
.p-form label{display:grid;gap:4px;font:600 .9rem var(--body)}
.p-form label small{font-weight:400;color:var(--muted)}
.p-form input,.p-form select,.p-form textarea{font:500 1rem var(--body);padding:9px 11px;border:1px solid var(--rule);border-radius:10px;background:var(--bg);color:var(--ink);width:100%;min-width:0}
.p-form textarea{resize:vertical}
.p-form fieldset{border:0;margin:0;padding:0;min-width:0}
.p-form legend{font:600 .9rem var(--body);padding:0;margin-bottom:6px}
.opts{display:flex;flex-wrap:wrap;gap:6px}
.opts label{display:inline-flex;flex-direction:row;align-items:center;gap:6px;border:1px solid var(--rule);border-radius:999px;padding:6px 12px;font:600 .86rem var(--body);cursor:pointer;background:var(--panel)}
.opts input{width:auto;margin:0;accent-color:var(--accent)}
.opts label:has(input:checked){border-color:var(--accent);background:var(--tint)}
.msg{white-space:pre-wrap;font:500 .84rem/1.6 var(--mono);background:var(--tint);border-radius:10px;padding:12px;margin:0;overflow-wrap:anywhere;user-select:all}
.fstat{font:500 .86rem var(--body);color:var(--muted);min-height:1.3em;margin:0}
.p-art{max-width:70ch;font-size:1.04rem;line-height:1.78}
.p-art h2{font:800 1.75rem/1.2 var(--display);margin:30px 0 8px;letter-spacing:.01em}
.p-art p{margin:0 0 14px}
.p-art ul,.p-art ol{margin:0 0 14px;padding-left:22px}.p-art li{margin-bottom:6px}
.p-art .rbox{background:var(--panel);border:1px solid var(--rule);border-radius:14px;padding:14px 18px;margin:18px 0}
.p-art .rbox h3{margin:0 0 6px;font:700 1rem var(--body)}
.p-art .rbox ol{margin:0}
.p-art .pf,.p-art .pfs{margin:20px 0}
.p-art blockquote{margin:22px 0;padding:0 0 0 18px;border-left:3px solid var(--accent);font:italic 600 1.3rem/1.45 var(--sign);color:var(--accent)}
.meta{display:flex;flex-wrap:wrap;gap:6px 14px;font:600 .8rem var(--body);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.meta b{color:var(--accent)}
.art-fig{max-width:880px}
.art-fig svg{display:block;width:100%;height:auto;max-height:340px;background:var(--tint);border-radius:16px}
.jcards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
.jcards a{display:flex;flex-direction:column;background:var(--panel);border:1px solid var(--rule);border-radius:16px;overflow:hidden;color:var(--ink);text-decoration:none;min-width:0}
.jcards .th{background:var(--tint);display:grid;place-items:center;aspect-ratio:3/2;max-width:100%}
.jcards .th svg{display:block;width:100%;height:100%}
.jcards .bd{padding:12px 16px 16px;display:grid;gap:4px}
.jcards .meta{font-size:.72rem}
.jcards h3{margin:2px 0 0;font:800 1.35rem/1.15 var(--display);text-wrap:balance}
.jcards p{margin:0;color:var(--muted);font-size:.9rem}
.jcards a:hover h3{color:var(--accent)}
@media (max-width:1000px){.jcards{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:620px){.jcards{grid-template-columns:minmax(0,1fr)}}
.jfeat{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);padding:0;overflow:hidden;text-decoration:none;color:var(--ink)}
.jfeat .th{background:var(--tint);display:grid;place-items:center;padding:14px;min-width:0}
.jfeat .th svg{display:block;width:100%;max-width:340px;height:auto}
.jfeat .bd{padding:20px 24px;display:grid;gap:6px;align-content:center;min-width:0}
.jfeat h3{font:800 2.1rem/1.1 var(--display);margin:0;letter-spacing:.01em}
.jfeat p{margin:0}.jfeat .bd>p:not(.meta){color:var(--muted);max-width:60ch}
.jfeat:hover h3{color:var(--accent)}
@media (max-width:760px){.jfeat{grid-template-columns:minmax(0,1fr)}.jfeat .th svg{max-width:280px}}
.mdl{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px 16px;margin-top:4px}
.mdl a{display:grid;grid-template-columns:auto minmax(0,1fr);gap:12px;align-items:center;border-top:1px solid var(--rule);padding-top:10px;color:var(--ink);text-decoration:none;min-width:0}
.mdl a svg.pi{width:30px;height:30px;color:var(--accent)}
.mdl b{display:block;font:700 1rem var(--body)}.mdl small{display:block;color:var(--muted);font-size:.86rem}
.mdl a:hover b{color:var(--accent)}
.kser{display:flex;flex-direction:column;gap:4px;text-decoration:none;color:var(--ink)}
.kser svg.pi{width:34px;height:34px;color:var(--accent);margin-bottom:4px}
.kser p{color:var(--muted);font-size:.92rem}
.kser .lnk{margin-top:auto;padding-top:6px}
.kser:hover h3{color:var(--accent)}
.g5k{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px}
@media (max-width:1280px){.g5k{grid-template-columns:repeat(2,minmax(0,1fr))}.g5k>:first-child{grid-column:1/-1}}
@media (max-width:560px){.g5k{grid-template-columns:minmax(0,1fr)}}
@media (max-width:1100px){.mdl{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.mdl{grid-template-columns:minmax(0,1fr)}}
.ill .o{stroke:var(--ink);stroke-width:2.5;stroke-linejoin:round;stroke-linecap:round}
.ill text{font:600 12px var(--body);fill:var(--muted)}
@media (max-width:620px){.p-h2{font-size:1.75rem}.facts b{font-size:2rem}}
'''

COMMON_JS = r'''
(()=>{const m=document.getElementById('mhm');
if(m){document.addEventListener('keydown',e=>{if(e.key==='Escape'&&m.open){m.open=false;m.querySelector('summary').focus()}});
document.addEventListener('click',e=>{if(m.open&&!m.contains(e.target))m.open=false})}
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',async()=>{const t=b.dataset.copy,o=b.dataset.label||(b.dataset.label=b.textContent);
try{await navigator.clipboard.writeText(t);b.textContent=b.dataset.done||'Đã sao chép'}catch(e){const s=b.closest('div,p,section').querySelector('[data-sel]');if(s){const r=document.createRange();r.selectNodeContents(s);const g=getSelection();g.removeAllRanges();g.addRange(r)}b.textContent='Đã bôi đen, hãy sao chép'}
setTimeout(()=>{b.textContent=o},2400)}))})();
'''


def doc(fname, title, desc, body, css='', js='', wrap_cls='wrap', contact=True):
    head = (f'<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            f'<meta name="description" content="{esc(desc)}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">'
            '<style>*{box-sizing:border-box}:root{padding-top:env(safe-area-inset-top,0);padding-bottom:env(safe-area-inset-bottom,0)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>'
            f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n')
    assert '</script' not in (COMMON_JS + js).lower()
    out = (head + '<style>' + SHARED + '</style>\n<style>' + CORE_CSS + NEW_CSS + css + '</style></head><body>' + header(fname) +
           f'\n<div class="{wrap_cls}">\n' + nb(body) + ('\n' + contact_band() if contact else '') + '\n</div>\n' + footer() +
           '\n<script>' + COMMON_JS + js + '</script>\n</body></html>\n')
    return out


def form_url(name, phone, txt):
    q = lambda s: quote(s, safe='')
    return f"{FORM}&{FORM_F['name']}={q(name)}&{FORM_F['phone']}={q(phone)}&{FORM_F['txt']}={q(txt)}"

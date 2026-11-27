# Thông tin liên hệ và thanh thông báo, sửa ở trang quản trị medili.vn/quan-tri (27/11/2026). Dữ liệu: art/data/cai-dat.json.
# Liên hệ: mã dựng web vẫn viết số điện thoại, Zalo, Facebook, email, giờ trả lời Zalo như cũ (kit.py) để bản dịch EN/JA/ZH
# khớp từ điển; khi chị đổi ở trang quản trị, bước cuối của build_manus.py thay chuỗi cũ bằng chuỗi mới trên mọi trang đã dựng
# (tiếng Việt và bản dịch). Địa chỉ chưa sửa được ở trang quản trị vì xuất hiện ở nhiều dạng câu trong bài viết.
# Thông báo: một dải chữ trên đầu mọi trang (bật/tắt, ngày bắt đầu, ngày kết thúc, kiểu thường/quan trọng, link tùy chọn).
import json, os, re, datetime, hashlib
from kit import HERE, PHONE, PHONE_RAW, ZALO, FACEBOOK, EMAIL, esc

DATA = os.path.join(HERE, 'data', 'cai-dat.json')
GIO = ('6:30', '22:30')   # giờ MeDili trả lời Zalo trong 60 phút, đang viết trong các trang
VN_TZ = datetime.timezone(datetime.timedelta(hours=7))


def _load():
    try:
        d = json.load(open(DATA, encoding='utf8'))
        return d if isinstance(d, dict) else {}
    except (FileNotFoundError, ValueError):
        return {}


def _txt(v, n):
    """Chữ thuần một dòng, không thẻ HTML."""
    if not isinstance(v, str):
        return ''
    return re.sub(r'\s+', ' ', re.sub(r'<[^<>]*>|[<>]', '', v)).strip()[:n]


def _url(v):
    v = _txt(v, 300)
    return v if re.fullmatch(r'https://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(/[^\s"\'<>]*)?', v) else ''


def _phone(v):
    """'0912 345 678' -> ('0912 345 678', '0912345678', '+84912345678'); số không hợp lệ -> None."""
    d = re.sub(r'\D', '', v or '')
    if d.startswith('84') and len(d) == 11:
        d = '0' + d[2:]
    if not re.fullmatch(r'0[1-9]\d{8}', d):
        return None
    return f'{d[:4]} {d[4:7]} {d[7:]}', d, '+84' + d[1:]


def _gio(v):
    return v if isinstance(v, str) and re.fullmatch(r'([01]?\d|2[0-3]):[0-5]\d', v) else None


def lien_he():
    """Liên hệ hiện hành sau khi đọc cai-dat.json (giá trị sai thì giữ giá trị gốc)."""
    d = _load().get('lien_he') or {}
    ph = _phone(d.get('dien_thoai')) or (PHONE, PHONE_RAW, '+84' + PHONE_RAW[1:])
    em = _txt(d.get('email'), 120)
    gio = d.get('gio_zalo') if isinstance(d.get('gio_zalo'), list) and len(d.get('gio_zalo')) == 2 else []
    g0, g1 = (_gio(gio[0]), _gio(gio[1])) if gio else (None, None)
    return dict(phone=ph[0], phone_raw=ph[1], phone_intl=ph[2],
                zalo=_url(d.get('zalo')) or ZALO, facebook=_url(d.get('facebook')) or FACEBOOK,
                email=em if re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', em) else EMAIL,
                gio=(g0, g1) if g0 and g1 else GIO)


GIO_RE = re.compile(r'(?<![\d:])6:30(\s*(?:–|-|—|〜|～|~|至|から|đến|to)\s*)22:30(?![\d])')


def substitutions():
    """[(chuỗi cũ, chuỗi mới)] cho các mục chị đã đổi. Rỗng khi không đổi gì."""
    c = lien_he()
    pairs = [(PHONE, c['phone']), (PHONE_RAW, c['phone_raw']), ('+84' + PHONE_RAW[1:], c['phone_intl']),
             (ZALO, c['zalo']), (FACEBOOK, c['facebook']), (EMAIL, c['email'])]
    return [(a, b) for a, b in pairs if a != b], (c['gio'] if c['gio'] != GIO else None)


def canon(s):
    """Ngược với apply_out: đưa thông tin liên hệ mới về như trong mã, để tách câu cần dịch (i18n.py) khớp từ điển."""
    pairs, gio = substitutions()
    for a, b in sorted(pairs, key=lambda x: -len(x[1])):   # chuỗi dài trước: link Zalo mới có thể chứa số điện thoại mới
        s = s.replace(b, a)
    if gio:
        rx = re.compile(r'(?<![\d:])' + re.escape(gio[0]) + r'(\s*(?:–|-|—|〜|～|~|至|から|đến|to)\s*)' + re.escape(gio[1]) + r'(?![\d])')
        s = rx.sub(lambda m: GIO[0] + m.group(1) + GIO[1], s)
    return s


def apply_out(roots):
    """Thay thông tin liên hệ cũ bằng mới trong mọi trang đã dựng (bỏ qua ảnh, video, trang quản trị)."""
    pairs, gio = substitutions()
    if not pairs and not gio:
        return 0
    n = 0
    for root in roots:
        files = []
        if os.path.isfile(root):
            files = [root]
        else:
            for d, ds, fs in os.walk(root):
                ds[:] = [x for x in ds if x not in ('assets', 'quan-tri')]
                files += [os.path.join(d, f) for f in fs if f.endswith(('.html', '.json', '.xml', '.txt'))]
        for p in files:
            s = open(p, encoding='utf8').read()
            t = s
            for a, b in pairs:
                t = t.replace(a, b)
            if gio:
                t = GIO_RE.sub(lambda m: gio[0] + m.group(1) + gio[1], t)
            if t != s:
                open(p, 'w', encoding='utf8').write(t)
                n += 1
    return n


# ---------- thanh thông báo ----------
NOTE_CSS = ('.mdtb{position:relative;z-index:51;font:500 15px/1.45 var(--body,system-ui,sans-serif);background:#F4CC97;color:#4A2C1A;border-bottom:1px solid #D9A866}'
            '.mdtb.qt{background:#9E3B26;color:#FFF3E4;border-color:#7E2C1B}'
            '.mdtb-in{max-width:1320px;margin:auto;display:flex;gap:6px 14px;align-items:center;justify-content:center;flex-wrap:wrap;'
            'padding:9px max(52px,env(safe-area-inset-right,0px)) 9px max(16px,env(safe-area-inset-left,0px));text-align:center}'
            '.mdtb p{margin:0;max-width:90ch}.mdtb a{color:inherit;font-weight:700;text-decoration:underline;text-underline-offset:3px}'
            '.mdtb button{position:absolute;top:50%;right:max(6px,env(safe-area-inset-right,0px));transform:translateY(-50%);width:44px;height:44px;'
            'display:grid;place-items:center;border:0;border-radius:999px;background:transparent;color:inherit;font:400 26px/1 system-ui,sans-serif;cursor:pointer}'
            '.mdtb button:hover{background:rgba(74,44,26,.12)}.mdtb.qt button:hover{background:rgba(255,243,228,.16)}'
            '.mdtb a:focus-visible,.mdtb button:focus-visible{outline:3px solid currentColor;outline-offset:2px}')
# ẩn khi ngoài khoảng ngày (theo lịch máy người xem) hoặc khi khách đã đóng thông báo này
NOTE_JS = ('(()=>{const b=document.currentScript.closest(".mdtb");if(!b)return;const d=new Date(),t=d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0");'
           'let k=null;try{k=localStorage.getItem("medili-tb")}catch(e){}'
           'if((b.dataset.tu&&t<b.dataset.tu)||(b.dataset.den&&t>b.dataset.den)||k===b.dataset.k){b.remove();return}'
           'b.querySelector("button").addEventListener("click",()=>{try{localStorage.setItem("medili-tb",b.dataset.k)}catch(e){}b.remove()})})();')


def _day(v):
    return v if isinstance(v, str) and re.fullmatch(r'20\d\d-[01]\d-[0-3]\d', v) else ''


def notice(today=None):
    """Thanh thông báo đầu trang, hoặc '' khi đang tắt, chưa có chữ hay đã qua ngày kết thúc."""
    d = _load().get('thong_bao') or {}
    chu = _txt(d.get('chu'), 220)
    if not d.get('bat') or not chu:
        return ''
    tu, den = _day(d.get('tu')), _day(d.get('den'))
    today = today or datetime.datetime.now(VN_TZ).strftime('%Y-%m-%d')
    if den and today > den:
        return ''
    link = _txt(d.get('link'), 300)
    if not (re.fullmatch(r'[a-z0-9-]+\.html(#[a-z0-9-]+)?', link) or _url(link)):
        link = ''
    nhan = _txt(d.get('chu_link'), 40) or 'Xem chi tiết'
    ext = ' target="_blank" rel="noopener"' if link.startswith('https://') else ''
    a = f' <a href="{esc(link)}"{ext}>{esc(nhan)}</a>' if link else ''

    k = hashlib.sha1((chu + '|' + link + '|' + tu + '|' + den).encode()).hexdigest()[:10]
    cls = 'mdtb qt' if d.get('kieu') == 'quan-trong' else 'mdtb'
    return (f'<aside class="{cls}" aria-label="Thông báo" data-k="{k}" data-tu="{tu}" data-den="{den}"><style>{NOTE_CSS}</style>'
            f'<div class="mdtb-in"><p>{esc(chu)}{a}</p></div><button type="button" aria-label="Đóng thông báo">×</button>'
            f'<script>{NOTE_JS}</script></aside>')

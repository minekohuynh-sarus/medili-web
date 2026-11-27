# Mục Tin tức MeDili (24/11/2026): mỗi ngày một bài tin về cà phê, ca cao, nông sản Di Linh.
# Bài do tác vụ "Bài tin tức MeDili hằng ngày" soạn, chị Ngân duyệt trên trang "Duyệt bài MeDili",
# tác vụ "Đăng bài tin tức đã duyệt" ghi bài vào art/data/tin-tuc.json rồi dựng lại web.
# Mỗi bài: {"slug","date":"YYYY-MM-DD","title","desc","keywords":[..],"body":[{"h":".."}|{"p":".."}],
#           "cta":"..","sources":[{"name","url"}]}. Chữ trong bài là chữ thuần (không HTML), được thoát ký tự khi dựng.
# Trang quản trị medili.vn/quan-tri (27/11/2026): chị và nhân viên viết, sửa, ẩn bài ("an": true), lưu bài nháp chưa đăng
# ("nhap": true, chưa từng lên web nên không cần trang báo gỡ); chị xóa bài thì tên bài vào
# art/data/tin-tuc-go.json. Hosting không xóa tệp cũ, nên bài đã ẩn hoặc đã xóa được thay bằng một trang ngắn báo bài không còn,
# không đưa vào tìm kiếm và sơ đồ trang.
import json, os, re
from kit import *
from pages_a import head

DATA = os.path.join(HERE, 'data', 'tin-tuc.json')
GONE = os.path.join(HERE, 'data', 'tin-tuc-go.json')
LIST = 'tin-tuc.html'

CSS = r'''
.tt-list{display:grid;gap:14px;margin:8px 0 28px}
.tt-card{display:block;text-decoration:none;color:inherit;padding:18px 20px}
.tt-card h2{margin:4px 0 6px;font-size:1.15rem;line-height:1.35}
.tt-card p{margin:0}
.tt-d{font-size:.82rem;opacity:.75;letter-spacing:.02em}
.tt-art{max-width:720px;margin:0 auto 28px}
.tt-art h2{margin:26px 0 8px;font-size:1.2rem;line-height:1.35}
.tt-art p{line-height:1.7;margin:0 0 12px}
.tt-cta{margin:22px 0;padding:18px 20px}
.tt-cta p{margin:0 0 12px}
.tt-src{font-size:.88rem;margin-top:22px}
.tt-src ul{padding-left:18px;margin:6px 0}
.tt-src a{word-break:break-word}
.tt-kw{font-size:.82rem;opacity:.75}
.tt-empty{padding:18px 20px}
'''


def load():
    try:
        posts = json.load(open(DATA, encoding='utf8'))
    except FileNotFoundError:
        posts = []
    ok = []
    for p in posts:
        if not isinstance(p, dict) or p.get('an') or p.get('nhap') or not re.fullmatch(r'[a-z0-9-]{3,80}', str(p.get('slug', ''))) or not p.get('title') or not p.get('body'):
            continue
        ok.append(p)
    return sorted(ok, key=lambda p: (p['date'], p['slug']), reverse=True)


def fname(p):
    return f"tin-tuc-{p['slug']}.html"


def vdate(d):
    y, m, dd = d.split('-')
    return f'{int(dd)}/{int(m)}/{y}'


def safe_url(u):
    return u if isinstance(u, str) and u.startswith('https://') else ''


def article(p, posts):
    blocks = ''
    for b in p['body']:
        if 'h' in b:
            blocks += f'<h2>{esc(b["h"])}</h2>'
        elif 'p' in b:
            blocks += f'<p>{esc(b["p"])}</p>'
    src = ''.join((f'<li><a href="{esc(safe_url(s.get("url")))}" target="_blank" rel="noopener nofollow">{esc(s.get("name", ""))}</a></li>'
                   if safe_url(s.get('url')) else f'<li>{esc(s.get("name", ""))}</li>') for s in p.get('sources', []))
    cta = (f'<div class="box tt-cta"><p>{esc(p["cta"])}</p>'
           f'<a class="btn main" href="{ZALO}" target="_blank" rel="noopener">Đặt cà phê qua Zalo</a> '
           '<a class="btn" href="cua-hang.html">Xem cửa hàng</a></div>') if p.get('cta') else ''
    more = [q for q in posts if q is not p][:3]
    more_h = ('<h2>Tin khác</h2><div class="tt-list">' + ''.join(card(q) for q in more) + '</div>') if more else ''
    kw = ', '.join(esc(k) for k in p.get('keywords', []))
    body = (head(f'Tin tức MeDili · {vdate(p["date"])}', esc(p['title']), esc(p.get('desc', '')),
                 f'<a class="btn" href="{LIST}">Tất cả tin tức</a>')
            + f'<article class="tt-art">{blocks}{cta}'
            + (f'<div class="tt-src"><b>Nguồn:</b><ul>{src}</ul></div>' if src else '')
            + (f'<p class="tt-kw">Từ khóa: {kw}</p>' if kw else '')
            + more_h + '</article>')
    return doc(fname(p), esc(p['title']) + ' · MeDili Café', p.get('desc', ''), body, css=CSS)


def card(p):
    return (f'<a class="box tt-card" href="{fname(p)}"><span class="tt-d">{vdate(p["date"])}</span>'
            f'<h2>{esc(p["title"])}</h2><p>{esc(p.get("desc", ""))}</p></a>')


def listing(posts):
    cards = ''.join(card(p) for p in posts) or '<div class="box tt-empty">Tin tức sẽ được cập nhật mỗi ngày.</div>'
    body = (head('Tin tức MeDili', 'Tin cà phê, ca cao <em>và nông sản Di Linh.</em>',
                 'Mỗi ngày một tin chọn lọc về thị trường cà phê, ca cao và nông sản Lâm Đồng, kèm góc nhìn từ vườn MeDili. Mỗi bài đều ghi nguồn báo gốc.',
                 f'<a class="btn main" href="{ZALO}" target="_blank" rel="noopener">Hỏi MeDili qua Zalo</a><a class="btn" href="gia-ca-phe.html">Giá cà phê hôm nay</a>')
            + f'<div class="tt-list">{cards}</div>')
    return doc(LIST, 'Tin tức cà phê, ca cao, nông sản Di Linh · MeDili Café',
               'Tin mới mỗi ngày về thị trường cà phê, ca cao và nông sản Di Linh, Lâm Đồng, kèm góc nhìn từ vườn MeDili.', body, css=CSS)


def gone(posts):
    """Tên bài đã ẩn hoặc đã xóa (không còn trong danh sách đang hiện)."""
    names = set()
    try:
        names |= {p.get('slug') for p in json.load(open(DATA, encoding='utf8')) if isinstance(p, dict) and p.get('an')}
    except (FileNotFoundError, ValueError):
        pass
    try:
        names |= {x for x in json.load(open(GONE, encoding='utf8')) if isinstance(x, str)}
    except (FileNotFoundError, ValueError):
        pass
    live = {p['slug'] for p in posts}
    return sorted(n for n in names if isinstance(n, str) and re.fullmatch(r'[a-z0-9-]{3,80}', n) and n not in live)


def stub(slug, posts):
    more = posts[:3]
    body = (head('Tin tức MeDili', 'Bài viết này <em>không còn trên web.</em>',
                 'MeDili đã gỡ hoặc tạm ẩn bài viết này. Mời bạn xem các tin mới hơn.',
                 f'<a class="btn main" href="{LIST}">Tất cả tin tức</a>')
            + ('<div class="tt-list">' + ''.join(card(q) for q in more) + '</div>' if more else ''))
    s = doc(f'tin-tuc-{slug}.html', 'Bài viết không còn · MeDili Café', 'Bài viết này không còn trên web MeDili.', body, css=CSS)
    return s.replace('<meta charset="utf-8">', '<meta charset="utf-8">' + NOINDEX_META, 1)


def pages():
    posts = load()
    out = {LIST: listing(posts)}
    for p in posts:
        out[fname(p)] = article(p, posts)
    for n in gone(posts):
        out[f'tin-tuc-{n}.html'] = stub(n, posts)
    return out

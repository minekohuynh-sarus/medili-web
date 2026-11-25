# Bản tiếng Anh, Nhật, Trung (giản thể) cho web MeDili (chị Ngân yêu cầu 24/11/2026: dịch toàn bộ, đúng 100% theo bản tiếng Việt).
#
# Cách làm: dựng web tiếng Việt như cũ (site-new4/*.html). Công cụ này tách từng đoạn chữ ra khỏi trang:
#   - đoạn chữ trong HTML (giữ thẻ in đậm, nghiêng, link... thành chỗ trống <1>…</1>, <2/>),
#   - thuộc tính có chữ Việt (alt, aria-label, placeholder, content của thẻ meta, data-…),
#   - chuỗi chữ trong JavaScript (cả chuỗi mẫu `…${x}…`, phần ${x} thành chỗ trống {1}),
# rồi tra từ điển art/i18n/<lang>.json để ghi ra site-new4/<lang>/*.html. Từ điển lấy chính câu tiếng Việt làm khóa,
# nên sửa câu tiếng Việt thì câu đó thành "chưa dịch" và lệnh build báo ra để dịch bổ sung.
#
# Lệnh (chạy trong thư mục art):
#   python3 i18n.py extract        tách đoạn chữ -> i18n/segments.json
#   python3 i18n.py status         đếm đoạn đã dịch, còn thiếu
#   python3 i18n.py next [ký tự]   in các đoạn chưa dịch tiếp theo (mã<TAB>câu), mặc định khoảng 5000 ký tự
#   python3 i18n.py add tệp.json   nạp bản dịch dạng {mã: {"en": …, "ja": …, "zh": …}}
#   python3 i18n.py build          ráp trang /en /ja /zh (đoạn thiếu bản dịch giữ tiếng Việt và được liệt kê)
#   python3 i18n.py pseudo         ráp thử bằng bản dịch giả vào site-new4/xx để kiểm tra không sót chữ, không lỗi JS
import os, re, sys, json, hashlib, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'site-new4')
DD = os.path.join(HERE, 'i18n')
LANGS = ['en', 'ja', 'zh']
SITE = 'https://www.medili.vn/'
LNAME = {'vi': 'Tiếng Việt', 'en': 'English', 'ja': '日本語', 'zh': '中文'}
LSHORT = {'vi': 'VI', 'en': 'EN', 'ja': 'JA', 'zh': 'ZH'}
HTML_LANG = {'vi': 'vi', 'en': 'en', 'ja': 'ja', 'zh': 'zh-Hans'}
NUM_LOCALE = {'en': 'en-US', 'ja': 'ja-JP', 'zh': 'zh-CN'}
_DEC_SWAP = str.maketrans({',': '.', '.': ','})
_VNNUM = r'\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?'
# ô chỉ có số (bảng tĩnh): 15,3 · 0,1% · ≈ 2,2–2,7 · 1:3,2
_NUMCELL = re.compile(r'>(\s*(?:[≈~±]\s?)?)((?:' + _VNNUM + r')(?:\s?[–:\-]\s?(?:' + _VNNUM + r'))*)(\s?(?:%|g|mm|kg|ml|°C|ha|cm)?\s*)<')


def _numcell(m):
    if not re.search(r'\d,\d', m.group(2)):
        return m.group(0)
    return '>' + m.group(1) + m.group(2).translate(_DEC_SWAP) + m.group(3) + '<'

_MON = "['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']"
_TODAY_VI = "const today=()=>{const d=new Date();return String(d.getDate()).padStart(2,'0')+'/'+String(d.getMonth()+1).padStart(2,'0')+'/'+d.getFullYear()};"
_TODAY = {'en': "const today=()=>{const d=new Date();return " + _MON + "[d.getMonth()]+' '+d.getDate()+', '+d.getFullYear()};",
          '*': "const today=()=>{const d=new Date();return d.getFullYear()+'年'+(d.getMonth()+1)+'月'+d.getDate()+'日'};"}
DATE_FIX = [   # (trang, mã ngày kiểu Việt, {ngôn ngữ: mã mới}); '*' dùng cho ja, zh
    ('cold-brew.html', "const dmy=d=>String(d.getDate()).padStart(2,'0')+'/'+String(d.getMonth()+1).padStart(2,'0')+'/'+d.getFullYear();",
     {'en': "const dmy=d=>" + _MON + "[d.getMonth()]+' '+d.getDate()+', '+d.getFullYear();",
      '*': "const dmy=d=>d.getFullYear()+'年'+(d.getMonth()+1)+'月'+d.getDate()+'日';"}),
    ('trai-chin.html', "return String(x.getDate()).padStart(2,'0')+'/'+String(x.getMonth()+1).padStart(2,'0')};",
     {'en': "return " + _MON + "[x.getMonth()]+' '+x.getDate()};", '*': "return (x.getMonth()+1)+'月'+x.getDate()+'日'};"}),
    ('nhan-xanh.html', _TODAY_VI, _TODAY),
    ('gio-hang.html', _TODAY_VI, _TODAY),
    ('gia-ca-phe.html', "const dd=s=>{const [y,m,d]=s.split('-');return `${d}/${m}/${y}`};",
     {'en': "const dd=s=>{const [y,m,d]=s.split('-');return `${" + _MON + "[+m-1]} ${+d}, ${y}`};",
      '*': "const dd=s=>{const [y,m,d]=s.split('-');return `${y}年${+m}月${+d}日`};"}),
    ('gia-ca-phe.html', "const dshort=s=>{const [y,m,d]=s.split('-');return `${d}/${m}`};",
     {'*': "const dshort=s=>{const [y,m,d]=s.split('-');return `${+m}/${+d}`};"}),
    ('index.html', "document.getElementById('tk-d').textContent=d+'/'+m;",
     {'*': "document.getElementById('tk-d').textContent=(+m)+'/'+(+d);"}),
    ('banh-xe-huong.html', "pd=`${String(d.getDate()).padStart(2,'0')}/${String(d.getMonth()+1).padStart(2,'0')}/${d.getFullYear()}`;",
     {'en': "pd=`${" + _MON + "[d.getMonth()]} ${d.getDate()}, ${d.getFullYear()}`;",
      '*': "pd=`${d.getFullYear()}年${d.getMonth()+1}月${d.getDate()}日`;"}),
]
SEARCH_KIND = {'en': {'Công cụ': 'Tool', 'Bài viết': 'Article', 'Trang': 'Page'},
               'ja': {'Công cụ': 'ツール', 'Bài viết': '記事', 'Trang': 'ページ'},
               'zh': {'Công cụ': '工具', 'Bài viết': '文章', 'Trang': '页面'}}
CJK_FONT = {'ja': 'Noto Sans JP', 'zh': 'Noto Sans SC'}

VN = re.compile(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]', re.I)
LETTER = re.compile(r'[A-Za-zÀ-ỹ]')
INLINE = {'a', 'b', 'i', 'em', 'strong', 'small', 'span', 'br', 'sup', 'sub', 'abbr', 'code', 'mark', 's', 'u', 'time', 'wbr',
          'q', 'cite', 'kbd', 'bdi', 'data', 'var', 'dfn', 'ins', 'del', 'img'}
VOID = {'br', 'wbr', 'img', 'input', 'hr', 'meta', 'link', 'source', 'area', 'col', 'embed', 'param', 'track'}
ATTR_SKIP = {'href', 'src', 'id', 'class', 'style', 'd', 'viewbox', 'xmlns', 'rel', 'type', 'target', 'name', 'for', 'role',
             'data-copy', 'srcset', 'sizes', 'width', 'height', 'loading', 'decoding', 'inputmode', 'autocomplete', 'lang',
             'charset', 'http-equiv', 'property', 'tabindex', 'aria-controls', 'aria-labelledby', 'aria-describedby'}
SHOW_ATTR = {'title', 'alt', 'aria-label', 'placeholder', 'content', 'label'}   # thuộc tính chỉ để hiển thị
TOKEN = re.compile(r'<!--.*?-->|<script\b[^>]*>.*?</script\s*>|<style\b[^>]*>.*?</style\s*>|<![^>]*>|</?[a-zA-Z][^>]*>|[^<]+|<', re.S | re.I)
SENT = '\x00'          # đánh dấu biểu thức ${…} trong chuỗi mẫu JS
def _force():
    """Chuỗi tiếng Việt không dấu trong JS (vd. 'Chua thanh') vẫn cần dịch: liệt kê trong i18n/force.json.
    Mục dạng 'tệp.html::chuỗi' chỉ ép dịch trong tệp đó (vd. 'cao' ở vi-sinh, vì trang khác dùng 'cao' làm mã)."""
    try:
        items = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'i18n', 'force.json'), encoding='utf8'))
    except FileNotFoundError:
        items = []
    glob, per = set(), {}
    for x in items:
        f, sep, k = x.partition('::')
        if sep and f.endswith('.html'):
            per.setdefault(f, set()).add(k)
        else:
            glob.add(x)
    return glob, per


FORCE, FILE_FORCE = _force()
NOTR = re.compile(r'\stranslate=["\']?no\b', re.I)   # phần tử không dịch (số, ngày do JS cập nhật)


def sid(key):
    return hashlib.sha1(key.encode('utf8')).hexdigest()[:9]


def tagname(tok):
    m = re.match(r'<(/?)([a-zA-Z][a-zA-Z0-9-]*)', tok)
    return (m.group(1) == '/', m.group(2).lower()) if m else (False, '')


def norm(s, js=False):
    s = s.replace('&nbsp;', ' ').replace('\u00a0', ' ').replace('\u202f', ' ')
    if js:
        s = re.sub(r'[ \t]+', ' ', s)
        s = re.sub(r' *\n *', '\n', s)
        return s.strip(' \t')
    return re.sub(r'\s+', ' ', s).strip()


# ---------------------------------------------------------------- đoạn chữ trong HTML
class Seg:
    __slots__ = ('key', 'tags', 'lead', 'trail', 'raw', 'keep')

    def __init__(self, key, tags, lead, trail, raw, keep=()):
        self.key, self.tags, self.lead, self.trail, self.raw = key, tags, lead, trail, raw
        self.keep = set(keep)      # chỗ trống giữ nguyên văn (phần tử translate="no")


def _make_seg(toks, js):
    """toks: list of (kind, text) kind in t (text), g (tag), x (biểu thức), o (phần tử translate="no", giữ nguyên) — đã cân thẻ. Trả về Seg hoặc None."""
    raw = ''.join(t for _, t in toks)
    # bỏ khoảng trắng đầu, cuối
    lead = trail = ''
    while toks and toks[0][0] == 't' and not toks[0][1].strip():
        lead += toks[0][1]; toks = toks[1:]
    while toks and toks[-1][0] == 't' and not toks[-1][1].strip():
        trail = toks[-1][1] + trail; toks = toks[:-1]
    if not toks:
        return None
    if toks[0][0] == 't':
        s = toks[0][1]; k = len(s) - len(s.lstrip())
        lead += s[:k]; toks = [('t', s[k:])] + toks[1:]
    if toks[-1][0] == 't':
        s = toks[-1][1]; k = len(s.rstrip())
        trail = s[k:] + trail; toks = toks[:-1] + [('t', s[:k])]
    text = ''.join(t for k, t in toks if k == 't')
    if not LETTER.search(H.unescape(text)):
        return None
    tags, out, stack, num, xn, keep = {}, [], [], 0, 0, set()
    # ghép cặp thẻ
    pair = {}
    st = []
    for i, (k, t) in enumerate(toks):
        if k != 'g':
            continue
        close, name = tagname(t)
        if name in VOID or t.endswith('/>'):
            continue
        if not close:
            st.append((name, i))
        elif st and st[-1][0] == name:
            pair[st.pop()[1]] = i
    closing = {v: k for k, v in pair.items()}
    for i, (k, t) in enumerate(toks):
        if k == 't':
            out.append(t)
        elif k == 'x':
            xn += 1; out.append('{%d}' % xn); tags['{%d}' % xn] = t
        elif k == 'o':
            num += 1; tags['<%d/>' % num] = t; keep.add('<%d/>' % num); out.append('<%d/>' % num)
        else:
            if i in pair:
                num += 1; tags['<%d>' % num] = t; tags['</%d>' % num] = toks[pair[i]][1]; tags[i] = num; out.append('<%d>' % num)
            elif i in closing:
                out.append('</%d>' % tags[closing[i]])
            else:
                num += 1; tags['<%d/>' % num] = t; out.append('<%d/>' % num)
    tags = {k: v for k, v in tags.items() if isinstance(k, str)}
    key = norm(''.join(out), js)
    return Seg(key, tags, lead, trail, raw, keep)


def _split_run(run, js):
    """run: list of (kind, text). Tách tại thẻ không có cặp, bóc thẻ bọc ngoài cùng. Trả về list mảnh: str hoặc Seg."""
    # tìm thẻ không cặp
    st, unmatched = [], set()
    for i, (k, t) in enumerate(run):
        if k != 'g':
            continue
        close, name = tagname(t)
        if name in VOID or t.endswith('/>'):
            continue
        if not close:
            st.append((name, i))
        elif st and st[-1][0] == name:
            st.pop()
        else:
            unmatched.add(i)
    unmatched |= {i for _, i in st}
    pieces, cur = [], []

    def flush():
        nonlocal cur
        if cur:
            pieces.extend(_peel(cur, js))
        cur = []
    for i, tok in enumerate(run):
        if i in unmatched:
            flush(); pieces.append(('tag', tok[1]))
        else:
            cur.append(tok)
    flush()
    return pieces


def _peel(toks, js):
    """Bóc thẻ mở đầu và thẻ đóng cuối nếu chúng bọc trọn đoạn (để khóa gọn hơn)."""
    pre, post = [], []
    while True:
        # bỏ khoảng trắng ra ngoài khi cần
        i0 = 0
        while i0 < len(toks) and toks[i0][0] == 't' and not toks[i0][1].strip():
            i0 += 1
        i1 = len(toks) - 1
        while i1 >= 0 and toks[i1][0] == 't' and not toks[i1][1].strip():
            i1 -= 1
        if i0 >= i1 or toks[i0][0] != 'g' or toks[i1][0] != 'g':
            break
        c0, n0 = tagname(toks[i0][1]); c1, n1 = tagname(toks[i1][1])
        if c0 or not c1 or n0 != n1 or n0 in VOID:
            break
        # kiểm tra thẻ đầu đóng đúng ở cuối
        depth, ok = 0, True
        for j in range(i0, i1 + 1):
            k, t = toks[j]
            if k != 'g':
                continue
            c, n = tagname(t)
            if n != n0:
                continue
            depth += -1 if c else 1
            if depth == 0 and j != i1:
                ok = False; break
        if not ok:
            break
        pre += toks[:i0 + 1]
        post = toks[i1:] + post
        toks = toks[i0 + 1:i1]
    seg = _make_seg(toks, js) if toks else None
    raw = lambda L: [('tag', t) if k == 'g' else t for k, t in L]
    return raw(pre) + ([seg] if seg else raw(toks)) + raw(post)


def segment_html(doc, js=False, scripts=True):
    """Chia tài liệu HTML (hoặc nội dung chuỗi JS) thành mảnh: str (giữ nguyên), Seg (đoạn dịch), ('tag', str), ('script', open, body, close)."""
    pieces, run = [], []
    hold = None          # [tên thẻ, độ sâu, các mảnh] khi đang ở trong phần tử translate="no"

    def flush():
        nonlocal run
        if run:
            pieces.extend(_split_run(run, js))
        run = []
    for m in TOKEN.finditer(doc):
        t = m.group(0)
        if hold is not None:
            hold[2].append(t)
            if t.startswith('<') and len(t) > 1 and not t.startswith('<!'):
                c, n = tagname(t)
                if n == hold[0] and n not in VOID and not t.endswith('/>'):
                    hold[1] += -1 if c else 1
            if hold[1] == 0:
                whole = ''.join(hold[2])
                if hold[0] in INLINE:
                    run.append(('o', whole))
                else:
                    flush(); pieces.append(whole)
                hold = None
            continue
        if t.startswith('<') and len(t) > 1 and not t.startswith('</') and NOTR.search(t.split('>', 1)[0]):
            c, n = tagname(t)
            if n and n not in VOID and not t.endswith('/>') and n not in ('script', 'style'):
                hold = [n, 1, [t]]
                continue
        if t.startswith('<!--') or t.startswith('<!'):
            flush(); pieces.append(t); continue
        low = t[:7].lower()
        if low.startswith('<script') or low.startswith('<style'):
            flush()
            if low.startswith('<script') and scripts and not re.search(r'type=["\']?application/json', t[:t.index('>')], re.I):
                a = t.index('>') + 1; b = t.lower().rindex('</script')
                pieces.append(('script', t[:a], t[a:b], t[b:]))
            else:
                pieces.append(t)
            continue
        if t.startswith('<') and len(t) > 1:
            close, name = tagname(t)
            if name in INLINE:
                run.append(('g', t)); continue
            flush(); pieces.append(('tag', t)); continue
        # chữ thường (có thể chứa dấu SENT của biểu thức JS)
        if js and SENT in t:
            parts = re.split('(' + SENT + r'\d+' + SENT + ')', t)
            for p in parts:
                if p.startswith(SENT):
                    run.append(('x', p))
                elif p:
                    run.append(('t', p))
        else:
            run.append(('t', t))
    flush()
    return pieces


# ---------------------------------------------------------------- JavaScript
KW = {'return', 'typeof', 'case', 'do', 'else', 'in', 'of', 'new', 'delete', 'void', 'throw', 'instanceof', 'yield', 'await'}


def lex(code, i=0, until_brace=False):
    """Trả về (danh sách chuỗi, vị trí kết thúc). Mỗi chuỗi: ('s', đầu, cuối, dấu nháy) hoặc ('t', đầu, cuối, phần)."""
    n, out, prev, depth = len(code), [], '', 0
    while i < n:
        ch = code[i]
        if ch in ' \t\r\n':
            i += 1; continue
        if code.startswith('//', i):
            j = code.find('\n', i); i = n if j < 0 else j; continue
        if code.startswith('/*', i):
            j = code.find('*/', i + 2); i = n if j < 0 else j + 2; continue
        if ch in '"\'':
            j = i + 1
            while j < n and code[j] != ch:
                if code[j] == '\\':
                    j += 1
                elif code[j] == '\n':
                    break
                j += 1
            out.append(('s', i, j + 1, ch)); i = j + 1; prev = 'lit'; continue
        if ch == '`':
            j, parts = i + 1, []
            start = j
            while j < n:
                c = code[j]
                if c == '\\':
                    j += 2; continue
                if c == '`':
                    break
                if c == '$' and j + 1 < n and code[j + 1] == '{':
                    parts.append(('txt', start, j))
                    sub, k = lex(code, j + 2, until_brace=True)
                    parts.append(('expr', j + 2, k, sub))
                    j = k + 1; start = j; continue
                j += 1
            parts.append(('txt', start, j))
            out.append(('t', i, j + 1, parts)); i = j + 1; prev = 'lit'; continue
        if ch == '/':
            if prev in ('', 'kw') or (len(prev) == 1 and prev in '(,=:[!&|?{};+-*%<>~^'):
                j = i + 1; cls = False
                while j < n:
                    c = code[j]
                    if c == '\\':
                        j += 2; continue
                    if c == '[':
                        cls = True
                    elif c == ']':
                        cls = False
                    elif c == '/' and not cls:
                        break
                    elif c == '\n':
                        break
                    j += 1
                j += 1
                while j < n and (code[j].isalpha()):
                    j += 1
                i = j; prev = 'lit'; continue
            i += 1; prev = '/'; continue
        if ch.isalnum() or ch in '_$':
            j = i
            while j < n and (code[j].isalnum() or code[j] in '_$'):
                j += 1
            w = code[i:j]; prev = 'kw' if w in KW else 'id'; i = j; continue
        if until_brace:
            if ch == '{':
                depth += 1
            elif ch == '}':
                if depth == 0:
                    return out, i
                depth -= 1
        prev = ch; i += 1
    return out, i


ESC = {'n': '\n', 't': '\t', 'r': '\r', 'b': '\b', 'f': '\f', 'v': '\v', '0': '\0'}


def js_decode(s):
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == '\\' and i + 1 < len(s):
            d = s[i + 1]
            if d in ESC:
                out.append(ESC[d]); i += 2
            elif d == 'u' and s[i + 2:i + 3] == '{':
                j = s.index('}', i); out.append(chr(int(s[i + 3:j], 16))); i = j + 1
            elif d == 'u':
                out.append(chr(int(s[i + 2:i + 6], 16))); i += 6
            elif d == 'x':
                out.append(chr(int(s[i + 2:i + 4], 16))); i += 4
            elif d == '\n':
                i += 2
            else:
                out.append(d); i += 2
        else:
            out.append(c); i += 1
    return ''.join(out)


def js_encode(s, q):
    s = s.replace('\\', '\\\\').replace('\n', '\\n').replace('\r', '\\r')
    if q == '`':
        return s.replace('`', '\\`').replace('${', '\\${')
    return s.replace(q, '\\' + q)


# ---------------------------------------------------------------- tra từ điển
class Tr:
    """Bộ dịch: mode 'collect' (gom khóa), 'apply' (dịch theo từ điển), 'pseudo' (dịch giả)."""

    def __init__(self, mode, lang=None, dic=None):
        self.mode, self.lang, self.dic = mode, lang, dic or {}
        self.keys = {}       # khóa -> {'k': loại, 'f': set tệp, 'c': ngữ cảnh}
        self.missing = {}
        self.file = ''

    def forced(self, key):
        return key in FORCE or key in FILE_FORCE.get(self.file, ())

    def need(self, key, kind):
        """Đoạn có cần dịch không."""
        if not LETTER.search(key):
            return False
        if kind in ('j', 'a'):
            return bool(VN.search(key)) or self.forced(key) or (kind == 'a' and key in self.dic)
        return True

    def get(self, key, kind, ctx=''):
        if not self.need(key, kind):
            return None
        if self.mode == 'collect':
            e = self.keys.setdefault(key, {'k': kind, 'f': set(), 'c': ctx})
            e['f'].add(self.file)
            return None
        if self.mode == 'pseudo':
            return pseudo(key)
        t = self.dic.get(self.file + '::' + key, self.dic.get(key))
        if t is None:
            self.missing.setdefault(key, set()).add(self.file)
        return t

    # ---- thuộc tính trong một thẻ
    def tag(self, t):
        def rep(m):
            name, q, val = m.group(1), m.group(2), m.group(3)
            if name.lower() in ATTR_SKIP or name.lower().startswith('on'):
                return m.group(0)
            if not VN.search(val) and name.lower() not in SHOW_ATTR and not self.forced(norm(val)):
                return m.group(0)     # giá trị không dấu ở data-*, value…: thường là mã cho JS, giữ nguyên
            if name.lower() == 'content' and not re.search(r'name="(description|twitter:[a-z]+)"|property="og:(title|description|site_name)"', t):
                return m.group(0)
            marks = re.findall(SENT + r'\d+' + SENT, val)
            if marks:   # thuộc tính có biểu thức ${…} bên trong (trong chuỗi mẫu JS)
                k = iter(range(1, 99))
                val = re.sub(SENT + r'\d+' + SENT, lambda _: '{%d}' % next(k), val)
            key = norm(val)
            tr = self.get(key, 'a')
            if tr is None:
                return m.group(0)
            if marks:
                tr = re.sub(r'\{(\d+)\}', lambda x: marks[int(x.group(1)) - 1], tr)
            if q == '"':
                tr = tr.replace('"', '&quot;')
            return f' {name}={q}{tr}{q}'
        return re.sub(r'\s([a-zA-Z_:][-a-zA-Z0-9_:.]*)=(["\'])(.*?)\2', rep, t, flags=re.S)

    # ---- một đoạn HTML
    def seg(self, s, js=False):
        tr = self.get(s.key, 'j' if js else 'h', s.raw[:80])
        if tr is None:
            return s.raw if self.mode != 'collect' else s.raw
        out = tr
        # thay chỗ trống bằng thẻ gốc (thẻ cũng được dịch thuộc tính)
        def rep(m):
            k = m.group(0)
            v = s.tags.get(k)
            if v is None:
                raise ValueError(f'chỗ trống lạ {k} trong bản dịch của: {s.key[:60]}')
            return v if k.startswith('{') or k in s.keep else self.tag(v)
        out = re.sub(r'</?\d+/?>|\{\d+\}', rep, out)
        return s.lead + out + s.trail

    def html(self, doc, js=False):
        res = []
        for p in segment_html(doc, js):
            if isinstance(p, Seg):
                res.append(self.seg(p, js))
            elif isinstance(p, tuple) and p[0] == 'tag':
                res.append(self.tag(p[1]))
            elif isinstance(p, tuple) and p[0] == 'script':
                res.append(self.tag(p[1]) + self.js(p[2]) + p[3])
            else:
                res.append(p)
        return ''.join(res)

    # ---- JavaScript
    def js(self, code):
        toks, _ = lex(code)
        return self._js_apply(code, toks, 0, len(code))

    def _js_apply(self, code, toks, a, b):
        out, pos = [], a
        for tk in toks:
            if tk[1] < pos or tk[2] > b:
                continue
            out.append(code[pos:tk[1]])
            out.append(self._js_str(code, tk))
            pos = tk[2]
        out.append(code[pos:b])
        return ''.join(out)

    def _js_str(self, code, tk):
        if tk[0] == 's':
            q = tk[3]; raw = code[tk[1] + 1:tk[2] - 1]
            if '\\' not in raw and not LETTER.search(raw):
                return code[tk[1]:tk[2]]
            try:
                val = js_decode(raw)
            except Exception:
                return code[tk[1]:tk[2]]
            if not (VN.search(val) or self.forced(norm(val, True))):
                return code[tk[1]:tk[2]]
            new = self.html(val, js=True)
            if self.mode == 'collect' or new == val:
                return code[tk[1]:tk[2]]
            return q + js_encode(new, q) + q
        # chuỗi mẫu
        parts = tk[3]
        exprs, text = [], []
        for p in parts:
            if p[0] == 'txt':
                text.append(code[p[1]:p[2]])
            else:
                exprs.append(self._js_apply(code, p[3], p[1], p[2]))
                text.append(SENT + str(len(exprs)) + SENT)
        raw = ''.join(text)
        try:
            val = js_decode(raw.replace('\\${', '\x01'))
        except Exception:
            val = raw
        val = val.replace('\x01', '${')
        if VN.search(re.sub(SENT + r'\d+' + SENT, '', val)) or self.mode != 'collect' or FORCE:
            new = self.html(val, js=True)
        else:
            new = val
        enc = js_encode(new, '`')
        # trả biểu thức về chỗ
        enc = re.sub(SENT + r'(\d+)' + SENT, lambda m: '${' + exprs[int(m.group(1)) - 1] + '}', enc)
        return '`' + enc + '`'


def pseudo(key):
    """Bản dịch giả: giữ chỗ trống, đổi chữ thành ‹…› để thấy chỗ nào còn sót tiếng Việt."""
    parts = re.split(r'(</?\d+/?>|\{\d+\})', key)
    return ''.join(p if re.fullmatch(r'</?\d+/?>|\{\d+\}', p or 'x') else ('‹' + re.sub(r'[A-Za-zÀ-ỹ]', 'x', p) + '›' if p.strip() else p) for p in parts)


# ---------------------------------------------------------------- tệp
def pages():
    return sorted(f for f in os.listdir(OUT) if f.endswith('.html'))


def load(lang):
    p = os.path.join(DD, lang + '.json')
    return json.load(open(p, encoding='utf8')) if os.path.exists(p) else {}


def save(lang, d):
    os.makedirs(DD, exist_ok=True)
    json.dump(dict(sorted(d.items())), open(os.path.join(DD, lang + '.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)


def extract():
    tr = Tr('collect')
    for f in pages():
        tr.file = f
        tr.html(open(os.path.join(OUT, f), encoding='utf8').read())
    segs = {}
    for k, e in tr.keys.items():
        segs[sid(k)] = {'s': k, 'k': e['k'], 'f': sorted(e['f']), 'c': e['c']}
    os.makedirs(DD, exist_ok=True)
    json.dump(segs, open(os.path.join(DD, 'segments.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=0)
    return segs


def status():
    segs = json.load(open(os.path.join(DD, 'segments.json'), encoding='utf8'))
    tot = sum(len(v['s']) for v in segs.values())
    print('đoạn', len(segs), 'ký tự', tot)
    for l in LANGS:
        d = load(l)
        done = [v for v in segs.values() if v['s'] in d]
        print(l, 'đã dịch', len(done), '/', len(segs), '| ký tự còn', tot - sum(len(v['s']) for v in done))


PLACE = re.compile(r'</?\d+/?>|\{\d+\}')


def check(src, tr):
    a = sorted(PLACE.findall(src)); b = sorted(PLACE.findall(tr))
    if a != b:
        return f'chỗ trống khác nhau: {a} / {b}'
    if re.search(r'<(?!/?\d+/?>)', tr) and not re.search(r'<(?!/?\d+/?>)', src):
        return 'có dấu < lạ'
    return ''


def add(path):
    segs = json.load(open(os.path.join(DD, 'segments.json'), encoding='utf8'))
    data = json.load(open(path, encoding='utf8'))
    dicts = {l: load(l) for l in LANGS}
    bad = 0
    for i, v in data.items():
        pre = ''
        if '::' in i:       # bản dịch riêng cho một trang: tệp.html::mã
            pre, i = i.split('::', 1); pre += '::'
        if i not in segs:
            print('không có mã', i); bad += 1; continue
        src = segs[i]['s']
        for l in LANGS:
            if l not in v:
                continue
            e = check(src, v[l])
            if e:
                print(i, l, e, '|', src[:70]); bad += 1; continue
            dicts[l][pre + src] = v[l]
    for l in LANGS:
        save(l, dicts[l])
    print('đã nạp', len(data), 'đoạn, lỗi', bad)


def addtsv(path):
    """Nạp bản dịch dạng TSV: mã<TAB>en<TAB>ja<TAB>zh (⏎ là xuống dòng). Dòng bắt đầu bằng # bị bỏ qua."""
    data = {}
    for n, line in enumerate(open(path, encoding='utf8'), 1):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        f = [x.strip() for x in (line.split('|||') if '|||' in line else line.split('\t'))]
        if len(f) != 4:
            print('dòng', n, 'cần 4 cột, có', len(f), '|', line[:60]); continue
        data[f[0].strip()] = {l: f[k + 1].replace('⏎', '\n') for k, l in enumerate(LANGS)}
    tmp = path + '.json'
    json.dump(data, open(tmp, 'w', encoding='utf8'), ensure_ascii=False)
    add(tmp)
    os.remove(tmp)


def nxt(limit=5000):
    segs = json.load(open(os.path.join(DD, 'segments.json'), encoding='utf8'))
    dicts = {l: load(l) for l in LANGS}
    order = {f: i for i, f in enumerate(pages())}
    todo = [(order.get(v['f'][0], 0), i, v) for i, v in segs.items() if any(v['s'] not in dicts[l] for l in LANGS)]
    todo.sort(key=lambda x: (x[0], x[1]))
    n = 0
    for _, i, v in todo:
        if n and n + len(v['s']) > limit:
            break
        s = v['s'].replace('\n', '⏎')
        print(f"{i}\t{v['k']}\t{v['f'][0]}\t{s}")
        n += len(v['s'])
    print(f'# còn {len(todo)} đoạn', file=sys.stderr)


# ---------------------------------------------------------------- ráp trang
def lang_menu(page, lang):
    """Nút chọn ngôn ngữ trong thanh menu. page: tên tệp ('index.html' là trang chủ)."""
    tgt = '' if page == 'index.html' else page
    up = '../' if lang != 'vi' else ''
    links = []
    for l in ['vi'] + LANGS:
        href = (up + tgt if l == 'vi' else up + l + '/' + tgt) or './'
        if l == lang:
            href = tgt or './'
        cur = ' aria-current="true"' if l == lang else ''
        links.append(f'<a href="{href}" hreflang="{HTML_LANG[l]}" lang="{HTML_LANG[l]}"{cur}>{LNAME[l]}</a>')
    lab = {'vi': 'Ngôn ngữ · Language', 'en': 'Language', 'ja': '言語 · Language', 'zh': '语言 · Language'}[lang]
    return (f'<details class="mh-l"><summary aria-label="{lab}">'
            f'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.6 2.4 3.8 5.3 3.8 8.5s-1.2 6.1-3.8 8.5c-2.6-2.4-3.8-5.3-3.8-8.5s1.2-6.1 3.8-8.5z"/></svg>'
            f'<span>{LSHORT[lang]}</span></summary><div class="mh-lp">{"".join(links)}</div></details>')


def alternates(page):
    tgt = '' if page == 'index.html' else page
    out = [f'<link rel="alternate" hreflang="vi" href="{SITE}{tgt}">']
    out += [f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="{SITE}{l}/{tgt}">' for l in LANGS]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{SITE}en/{tgt}">')   # mặc định tiếng Anh (25/11/2026)
    return ''.join(out)


LANG_BLOCK = re.compile(r'<details class="mh-l">.*?</details>', re.S)


def finish_vi(page, s):
    """Trang tiếng Việt: thêm hreflang (nút chọn ngôn ngữ đã có sẵn trong kit.header). Ghi lại mỗi lần dựng."""
    s = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]*">', '', s)
    return s.replace('</head>', alternates(page) + '</head>', 1)


def localize(page, s, lang, tr):
    tr.file = page
    s = re.sub(r'<script id="md-lang-go">.*?</script>', '', s, count=1, flags=re.S)   # chỉ trang chủ tiếng Việt chuyển hướng
    s = tr.html(s)
    # đường dẫn: trang con nằm trong /<lang>/
    s = re.sub(r'(\s(?:src|href|poster)=")assets/', r'\1../assets/', s)
    s = re.sub(r'url\((["\']?)assets/', r'url(\1../assets/', s)
    s = re.sub(r"(['\"`])assets/", r'\1../assets/', s)
    s = s.replace("'gia-ca-phe.json'", "'../gia-ca-phe.json'").replace('"gia-ca-phe.json"', '"../gia-ca-phe.json"')
    s = re.sub(r'(\s(?:href)=")\./(")', r'\1./\2', s)
    # số theo kiểu quốc tế: 1,234.5
    loc = NUM_LOCALE[lang]
    s = s.replace("toLocaleString('vi-VN').replace(/,/g,'.')", f"toLocaleString('{loc}')")
    s = s.replace("toLocaleString('vi-VN')", f"toLocaleString('{loc}')").replace("toLocaleString('de-DE')", f"toLocaleString('{loc}')")
    s = s.replace(".replace('.',',')", '')
    s = s.replace(".replace(/\\B(?=(\\d{3})+(?!\\d))/g,'.')", ".replace(/\\B(?=(\\d{3})+(?!\\d))/g,',')")
    # ngày tháng theo thói quen từng ngôn ngữ: Nov 24, 2026 · 2026年11月24日 · ngắn 11/24
    for f0, old, new in DATE_FIX:
        if f0 != page:
            continue
        if old not in s:
            print('  ! không thấy mã ngày ở', page, old[:50])
            continue
        s = s.replace(old, new.get(lang, new.get('*')))
    s = re.sub(r'(id="tk-d" translate="no">)(\d{1,2})/(\d{1,2})<', lambda m: f'{m.group(1)}{int(m.group(3))}/{int(m.group(2))}<', s)
    s = re.sub(r'(translate="no">)(\d{1,3}(?:\.\d{3})+)<', lambda m: m.group(1) + m.group(2).replace('.', ',') + '<', s)
    # chuỗi số thuần trong mã (không qua từ điển): 1:3,2 → 1:3.2 · 7,10 mm → 7.10 mm · value="83.600" → 83,600
    s = re.sub(r"""(['"`])((?:pH ?|≈ ?)?)(\d[\d.,:–\-]*,\d[\d.,:–\-]*)((?: ?(?:mm|%|°C|g|kg|ml|L|ha|cm))?)\1""",
               lambda m: m.group(1) + m.group(2) + m.group(3).translate(_DEC_SWAP) + m.group(4) + m.group(1), s)
    s = s.replace("+'.000'", "+',000'")
    s = re.sub(r'(\svalue=")(\d{1,3}(?:\.\d{3})+)(")', lambda m: m.group(1) + m.group(2).replace('.', ',') + m.group(3), s)
    s = _NUMCELL.sub(_numcell, s)
    # danh sách ghép bằng dấu phẩy: tiếng Nhật, tiếng Trung dùng dấu 、 và 。
    if lang in ('ja', 'zh'):
        s = s.replace(".join(', ')", ".join('、')").replace(".join('. ')", ".join('。')")
        # trang Giá cà phê: “ngày, giờ” → 2026年11月21日 19:38 · “ngày, nơi” → 日付、場所
        s = s.replace("${x.time?', '+x.time:''}", "${x.time?' '+x.time:''}")
        # dấu hai chấm toàn khổ, không cách sau: 業態：レストラン · 用途：烘焙厂
        s = s.replace('： ', '：')
        s = s.replace("createTextNode(': '+", "createTextNode('：'+").replace("QT[k]+': '+", "QT[k]+'：'+")
        s = re.sub(r"(\$\{[\w.\[\]]+\}): (\$\{)", r"\1：\2", s)
        s = s.replace("${F.place?', '+F.place:''}", "${F.place?'" + ('、' if lang == 'ja' else '，') + "'+F.place:''}")
    # nhãn SVG tính bề rộng theo số ký tự: chữ Nhật, Trung rộng gần gấp đôi chữ Latin
    if lang in ('ja', 'zh'):
        s, n = re.subn(r"(?<![\w.$])(l|t|sign|t2)\.length\*(\d+(?:\.\d+)?)",
                       lambda m: f"__tl({m.group(1)})*{m.group(2)}" if 5 <= float(m.group(2)) <= 10 else m.group(0), s)
        if n:
            s = s.replace('</head>', '<script>const __tl=s=>{let n=0;for(const c of String(s))n+=/[\u2e80-\u9fff\uac00-\ud7af\uff00-\uffef]/.test(c)?1.85:1;return n};</script></head>', 1)
    # tiếng Anh: 1 cup, 2 cups
    if lang == 'en':
        s = re.sub(r"([A-Za-z_$][\w$.]*)\+' cups'", r"\1+(\1==1?' cup':' cups')", s)
        s = re.sub(r"\$\{([A-Za-z_$][\w$.]*)\} cups\b", r"${\1} cup${\1==1?'':'s'}", s)
    # ngôn ngữ trang, nút chọn ngôn ngữ, hreflang
    s = re.sub(r'<html lang="vi"', f'<html lang="{HTML_LANG[lang]}"', s, count=1)
    s = LANG_BLOCK.sub(lambda m: lang_menu(page, lang), s, count=1)
    if 'hreflang="x-default"' not in s:
        s = s.replace('</head>', alternates(page) + '</head>', 1)
    # phông chữ cho tiếng Nhật, tiếng Trung
    if lang in CJK_FONT:
        fam = CJK_FONT[lang].replace(' ', '+')
        s = s.replace('family=Be+Vietnam+Pro', f'family={fam}:wght@400;500;700;800&family=Be+Vietnam+Pro', 1)
        f = CJK_FONT[lang]
        s = s.replace('</head>', f'<style>:root{{--body:"Be Vietnam Pro","{f}",system-ui,sans-serif;'
                                 f'--display:"Big Shoulders Display","{f}","Be Vietnam Pro",system-ui,sans-serif}}'
                                 f'body{{line-break:strict;word-break:normal;overflow-wrap:anywhere}}'
                                 # tiếng Nhật: tiêu đề xuống dòng theo cụm từ (Chrome, Edge), không cắt giữa 原|点, 届|く
                                 + ('h1,h2,h3,h4,.btn,.lede{word-break:auto-phrase}' if lang == 'ja' else '')
                                 + '</style></head>', 1)
    return s


def build(mode='apply', langs=None):
    """Ráp trang dịch. Trả về {lang: {khóa thiếu: tệp}}."""
    import cuahang
    langs = langs or LANGS
    report = {}
    for f in pages():
        p = os.path.join(OUT, f)
        s = open(p, encoding='utf8').read()
        s2 = finish_vi(f, s)
        if s2 != s:
            open(p, 'w', encoding='utf8').write(s2)
    for lang in langs:
        tr = Tr(mode, lang, load(lang) if mode == 'apply' else {})
        d = os.path.join(OUT, lang if mode == 'apply' else 'xx')
        os.makedirs(d, exist_ok=True)
        for f in pages():
            s = open(os.path.join(OUT, f), encoding='utf8').read()
            open(os.path.join(d, f), 'w', encoding='utf8').write(localize(f, s, lang, tr))
        idx = json.loads(cuahang.search_index(d))
        if mode == 'apply':   # nhãn loại kết quả tìm kiếm theo ngôn ngữ; 'Sản phẩm' phải khớp chuỗi so sánh trong tim-kiem.html
            kind = dict(SEARCH_KIND[lang], **{'Sản phẩm': tr.dic.get('Sản phẩm', 'Sản phẩm')})
            for it in idx:
                it['k'] = kind.get(it['k'], it['k'])
        open(os.path.join(d, 'tim-kiem.json'), 'w', encoding='utf8').write(json.dumps(idx, ensure_ascii=False, separators=(',', ':')))
        report[lang] = tr.missing
        if mode != 'apply':
            break
    return report


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'status'
    sys.path.insert(0, HERE)
    if cmd == 'extract':
        s = extract(); print('đoạn', len(s), 'ký tự', sum(len(v['s']) for v in s.values()))
    elif cmd == 'status':
        status()
    elif cmd == 'next':
        nxt(int(sys.argv[2]) if len(sys.argv) > 2 else 5000)
    elif cmd == 'add':
        add(sys.argv[2])
    elif cmd == 'addtsv':
        addtsv(sys.argv[2])
    elif cmd == 'build':
        r = build()
        for l, m in r.items():
            print(l, 'thiếu', len(m), 'đoạn')
    elif cmd == 'pseudo':
        build('pseudo', ['en'])
        print('đã ráp thử vào site-new4/xx')

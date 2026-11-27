# Giá, trạng thái và lời mô tả sản phẩm, sửa ở trang quản trị medili.vn/quan-tri (27/11/2026). Dữ liệu: art/data/san-pham.json.
# Mỗi dòng: p (nghìn đồng mỗi kg: [giá lẻ dưới 5 kg, sỉ 5–20 kg/tháng, sỉ trên 20 kg/tháng]; bộ Ngũ Hành chỉ có [giá kg],
# trên web hiện giá túi 250 g = 1/4), st (ban: đang bán, het: tạm hết hàng, sap: sắp mở bán; không có giá thì là liên hệ),
# taste (hương vị), use (cách dùng), fit (phù hợp với), head (một câu giới thiệu).
# ten, nhom, loai, dv chỉ để trang quản trị hiển thị và kiểm tra.
# loai: core = 11 dòng có đủ 3 mức giá (Tìm gu, HORECA, Đồng hành cùng quán, trang chủ cần đủ giá); le = Blend MeDili, Catimor,
# Culi (giá sỉ có thể để trống, giá lẻ để trống là liên hệ); ngu = Ngũ Hành (túi 250 g); sap = 6 dòng sắp mở bán.
# Giá trị sai (chữ, số âm, thiếu giá ở dòng bắt buộc) thì bỏ qua, giữ giá trị trong mã, để web luôn dựng được.
import json, os, re
from kit import HERE

DATA = os.path.join(HERE, 'data', 'san-pham.json')
TEXT = ('taste', 'use', 'fit', 'head')
TG_ID = {'pc': 'p-rc', 'pp': 'p-rp', 'mc': 'm-rc', 'mp': 'm-rp', 'ms': 'm-rs', 'pa': 'p-ap', 'ma': 'm-ap',
         'b91': 'b-91', 'b82': 'b-82', 'b73': 'b-73', 'b55': 'b-55'}


_C = {}


def load():
    if 'd' not in _C:
        try:
            d = json.load(open(DATA, encoding='utf8'))
        except (FileNotFoundError, ValueError):
            d = {}
        _C['d'] = d if isinstance(d, dict) else {}
    return _C['d']


def _txt(v):
    return re.sub(r'\s+', ' ', re.sub(r'<[^<>]*>|[<>]', '', v)).strip()[:300] if isinstance(v, str) else None


def _n(v):
    return v if isinstance(v, int) and not isinstance(v, bool) and 1 <= v <= 100000 else None


def price(loai, v, old):
    """Giá hợp lệ theo loại dòng, sai thì trả lại giá cũ."""
    if loai == 'core':
        ok = isinstance(v, list) and len(v) == 3 and all(_n(x) for x in v)
        return list(v) if ok else old
    if loai == 'le':
        if v is None:
            return None
        if isinstance(v, list) and len(v) == 3 and _n(v[0]) and ((v[1] is None and v[2] is None) or (_n(v[1]) and _n(v[2]))):
            return list(v)
        return old
    if loai in ('ngu', 'sap'):
        if v is None and loai == 'sap':
            return None
        return [v[0]] if isinstance(v, list) and len(v) == 1 and _n(v[0]) else old
    return old


def status(loai, v, has_price):
    if not has_price:
        return 'sap' if loai == 'sap' else 'lh'
    ok = ('ban', 'het', 'sap') if loai == 'sap' else ('ban', 'het')
    return v if v in ok else ('sap' if loai == 'sap' else 'ban')


def line_overrides(P):
    """Phần khác với mã cho 14 dòng trong Phòng chọn mua: {mã: {p?, taste?, use?, fit?, head?}}."""
    out = {}
    for i, d in load().items():
        if i not in P or not isinstance(d, dict):
            continue
        s, o = P[i], {}
        loai = 'core' if i in TG_ID else 'le'
        p = price(loai, d.get('p', s['p']), s['p'])
        if p != s['p']:
            o['p'] = p
        desc = s.get('desc') or {}
        for f in TEXT:
            t = _txt(d.get(f))
            cur = desc.get(f, '') if f == 'head' else s.get(f, '')
            if t is not None and t != cur:
                o[f] = t
        if o:
            out[i] = o
    return out


def inject(src, ov):
    """Ghi phần sửa vào dữ liệu Phòng chọn mua (đoạn mã ngay trước 'const byId=' trong mua-hang.html)."""
    if not ov:
        return src
    assert src.count('const byId=') == 1
    js = (';' + json.dumps([[k, v] for k, v in ov.items()], ensure_ascii=False, separators=(',', ':')) +
          ".forEach(([k,v])=>{const x=byIdRaw(k);if(!x)return;if('p' in v)x.p=v.p;['taste','use','fit'].forEach(f=>{if(f in v)x[f]=v[f]});"
          "if(['taste','use','head'].some(f=>f in v)){x.desc=x.desc||{};['taste','use','head'].forEach(f=>{if(f in v)x.desc[f]=v[f]})}});\n")
    return src.replace('const byId=', js + 'const byId=', 1)


def patch_tg(tg, P):
    """Giá trong bài Tìm gu theo giá đang bán (đồng)."""
    for i, t in TG_ID.items():
        m = re.search(r'(\{ id: "' + re.escape(t) + r'",[^\n]*?prices: )\[[^\]]*\]', tg)
        assert m, t
        new = '[' + ', '.join(str(v * 1000) for v in P[i]['p']) + ']'
        tg = tg[:m.start()] + m.group(1) + new + tg[m.end():]
    return tg


def catalog(x, loai):
    """Áp trạng thái và phần sửa cho một dòng trong danh mục Cửa hàng (cuahang.products)."""
    d = load().get(x['id'])
    if not isinstance(d, dict):
        return x
    if loai in ('ngu', 'sap'):
        old = [x['p'][0]] if x['p'] else None
        p = price(loai, d.get('p', old), old)
        x['p'] = [p[0], None, None] if p else None
        for f in TEXT:
            t = _txt(d.get(f))
            if t is not None and not (loai == 'sap' and f == 'use'):
                x[f] = t
    elif 'head' in d and _txt(d['head']) is not None:
        x['head'] = _txt(d['head'])
    st = status(loai, d.get('st'), bool(x['p']))
    if loai == 'sap' and st != 'sap' and x['st'] == 'sap':
        x['note'] = 'Chưa có giá sỉ, MeDili sẽ báo giá khi đặt hàng.'
    x['st'] = st
    return x

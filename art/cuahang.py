# Cửa hàng MeDili trên medili.vn: danh mục, trang từng dòng cà phê, giỏ hàng, tìm kiếm toàn site.
# Dựng theo cấu trúc web medilinh.com (source Manus chị Ngân gửi ngày 16/11/2026): danh mục có lọc, trang sản phẩm,
# giỏ hàng, tìm kiếm. Không dùng Shopify: giỏ lưu trên trình duyệt, khách gửi đơn qua Google Form, Zalo hoặc email,
# MeDili xác nhận giá cuối, phí giao rồi chốt đơn. Không thanh toán online.
# Danh mục = 14 dòng theo kg (bảng báo giá MeDili tháng 11/2026, trang 1; Catimor 400k, Culi 350k)
#          + bộ Ngũ Hành 6 dòng túi 250 g (bảng báo giá trang 2, giá túi = 1/4 giá kg)
#          + 6 dòng chỉ có trong source Manus, chưa có giá (ghi "Liên hệ", trạng thái "Sắp mở bán").
# Cách pha và chỉ số khẩu vị của 6 dòng mới lấy từ art/data/manus-catalog.json (trích từ source Manus).
# Không ghi nguồn cụ thể, không ghi bên cung cấp. Màu bao bì theo mệnh Thổ: không xanh lá, không đen, tránh xanh dương.
import json, os, re, html as H, unicodedata
from kit import *
from pages_a import head
import sanpham

SITE = 'https://www.medili.vn/'
GREENFIX = {'#2F6B4A': '#B5832F', '#3F7F5A': '#C9A15B'}   # giống bản Phòng chọn mua trên web
MAN = json.load(open(os.path.join(HERE, 'data', 'manus-catalog.json'), encoding='utf8'))

# mã dòng → tên trang (bỏ tiền tố "medili-" của handle Manus)
SLUG = {'pc': 'phin-robusta-classic', 'pp': 'phin-robusta-premium', 'mc': 'may-robusta-classic', 'mp': 'may-robusta-premium',
        'ms': 'may-robusta-specialty', 'pa': 'phin-arabica-premium', 'ma': 'may-arabica-premium',
        'b91': 'may-blend-premium-9-1', 'b82': 'may-blend-premium-8-2', 'b73': 'may-blend-premium-7-3', 'b55': 'may-blend-premium-5-5',
        'bm': 'blend-medili', 'cat': 'catimor', 'cul': 'culi',
        'ng-suong': 'ngu-hanh-suong', 'ng-rung': 'ngu-hanh-rung', 'ng-suoi': 'ngu-hanh-suoi',
        'ng-nang': 'ngu-hanh-nang', 'ng-nui': 'ngu-hanh-nui', 'ng-may': 'ngu-hanh-may',
        'frd': 'fine-robusta-di-linh', 'rh': 'fine-robusta-honey-di-linh', 'acd': 'arabica-cau-dat', 'sig': 'signature-coffee',
        'an': 'arabica-natural-cau-dat', 'aw': 'arabica-washed-cau-dat'}
ORDER = list(SLUG)

BREW = {'phin': 'Phin', 'espresso': 'Máy espresso', 'v60': 'Pha thủ công', 'coldbrew': 'Cold brew'}
GRIND = ['Nguyên hạt', 'Xay cho phin', 'Xay cho máy espresso', 'Xay pha thủ công']
PACKS = [250, 500, 1000, 5000]
BARS = ['Đậm', 'Ngọt hậu', 'Chua thanh', 'Thơm']
SAP_NOTE = ('Dòng đang hoàn thiện. Mức rang, hương vị và giá được MeDili xác nhận theo từng lô. '
            'Thêm vào giỏ để hỏi giá, hoặc nhắn Zalo để nhận mẫu thử khi mở bán.')

# 6 dòng chỉ có trong source Manus. Lời viết lại ngắn gọn từ hồ sơ định hướng của Manus, giữ chữ "Định hướng" vì chưa chốt theo lô.
NEW6 = {
    'frd': dict(n='Fine Robusta Di Linh', line='Robusta', tier='Premium', col='#8B4A2B', oshort='Di Linh',
                proc='Xác nhận theo lô', head='Robusta Di Linh thân rõ, ngọt rang',
                origin='Robusta Di Linh, Lâm Đồng', roast='Rang vừa, có thể rang đậm hơn cho phin và espresso',
                taste='Định hướng: ca cao đen, caramel rang, hạt rang, hậu sạch',
                fit='Quán và người pha cần một dòng Robusta cao cấp dễ lên công thức',
                tips=['Phù hợp với phin và espresso; có thể thử thêm pha thủ công và cold brew.',
                      'Mức rang được chốt sau khi rang thử và nếm từng lô.']),
    'rh': dict(n='Robusta Honey Di Linh', line='Robusta', tier='Premium', col='#C27B2C', oshort='Di Linh',
               proc='Honey', head='Robusta sơ chế Honey, thân dày, hậu ngọt',
               origin='Robusta Di Linh, Lâm Đồng', roast='Rang vừa đến vừa đậm',
               taste='Định hướng: ca cao, đường nâu, hạt rang, trái cây khô nhẹ',
               fit='Người uống hằng ngày thích Robusta đậm, hậu ngọt',
               tips=['Honey là cách sơ chế giữ lớp nhớt quanh nhân khi phơi, không phải tẩm mật ong.',
                     'Phù hợp với phin và espresso hằng ngày.']),
    'acd': dict(n='Arabica Cầu Đất', line='Arabica', tier='Premium', col='#A86B3C', oshort='Cầu Đất',
                proc='Xác nhận theo lô', head='Arabica Cầu Đất chua thanh vừa, ngọt sạch',
                origin='Arabica Cầu Đất, Lâm Đồng', roast='Rang vừa sáng đến rang vừa',
                taste='Định hướng: trái cây sáng nhẹ, cam quýt, caramel, hậu sạch',
                fit='Khách muốn Arabica Cầu Đất cân bằng, dễ đổi cách pha',
                tips=['Pha thủ công để rõ hương, phin hoặc espresso để đậm thân hơn.']),
    'sig': dict(n='MeDili Signature', line='Blend', tier='Signature', col='#5C2A3A', oshort='Di Linh',
                proc='Blend đặc trưng, công thức được xác nhận theo lô', head='Blend đặc trưng của MeDili, đậm vừa, thân dày',
                origin='Robusta Honey và Robusta Sẻ Di Linh, tỷ lệ do MeDili xác nhận', roast='Rang vừa đến vừa đậm',
                taste='Định hướng: ca cao, caramel, hạt rang, chua thấp, hậu gọn',
                fit='Gia đình và quầy pha cần một blend linh hoạt từ phin đến espresso',
                tips=['Dòng đặc trưng của MeDili, khác với Classic dễ uống và Premium thơm hương.']),
    'an': dict(n='Arabica Natural Cầu Đất', line='Arabica', tier='Premium', col='#9E4B6E', oshort='Cầu Đất',
               proc='Natural', head='Arabica Natural, vị trái chín, ngọt',
               origin='Arabica Cầu Đất, Lâm Đồng', roast='Rang vừa sáng đến rang vừa',
               taste='Định hướng: trái chín nhẹ, caramel, đường nâu, hậu sạch',
               fit='Khách muốn khám phá Arabica sơ chế Natural',
               tips=['Natural là phơi nguyên trái, hương trái cây thể hiện khác nhau theo từng lô.']),
    'aw': dict(n='Arabica Washed Cầu Đất', line='Arabica', tier='Premium', col='#C08A3E', oshort='Cầu Đất',
               proc='Washed', head='Arabica Washed, thanh rõ, cân bằng',
               origin='Arabica Cầu Đất, Lâm Đồng', roast='Rang vừa sáng đến rang vừa',
               taste='Định hướng: thanh rõ, cam chanh nhẹ, đường mía, hậu sạch',
               fit='Khách thích ly thanh, chua cân bằng',
               tips=['Washed là xát vỏ, lên men rồi rửa sạch lớp nhớt trước khi phơi, vị thường thanh và sạch.']),
}
OSHORT = {'Robusta': 'Di Linh', 'Arabica': 'Cầu Đất', 'Blend': 'Di Linh · Cầu Đất', 'Đặc sản': 'Lâm Đồng'}

# Bộ sưu tập Ngũ Hành, túi 250 g: theo bảng báo giá MeDili tháng 11/2026 (trang 2) và thông số trên bao bì Ngũ Hành.
# kg = giá 1 kg (nghìn đồng), túi 250 g = 1/4. bars lấy theo dòng gốc gần nhất trên kệ (base).
NGU = {
    'ng-suong': dict(n='Sương', sub='Mist', badge='Kim', kg=450, base='pa', col='#9C8466', oshort='Cầu Đất',
                     proc='Honey, Washed', origin='100% Arabica, Cầu Đất, Lâm Đồng',
                     roast='Rang mộc. Bản phin rang đậm (Dark), bản máy rang cho espresso',
                     taste='Socola, cam chanh, chua nhẹ, đắng vừa, ngọt hậu',
                     use='Bản phin: phin, đen đá, sữa đá. Bản máy: espresso, Americano, latte', brews=['phin', 'espresso'],
                     head='Một khoảng lặng giữa ngày', fit='Người thích Arabica thơm, chua nhẹ, ngọt hậu',
                     story='Arabica từ vùng đồi Cầu Đất, nơi sương sớm phủ những hàng cà phê. Thơm socola, cam chanh, chua nhẹ, ngọt hậu, cho một khoảng lặng giữa ngày.',
                     grinds=['Bản phin · nguyên hạt', 'Bản phin · xay cho phin', 'Bản máy · nguyên hạt', 'Bản máy · xay cho máy espresso']),
    'ng-rung': dict(n='Rừng', sub='Forest', badge='Mộc', kg=350, base='bm', col='#C8962E', oshort='Di Linh · Cầu Đất',
                    proc='Robusta : Arabica : Culi = 6 : 2 : 2', origin='60% Robusta Di Linh, 20% Arabica Cầu Đất, 20% Culi',
                    roast='Rang vừa (Medium), rang mộc', taste='Đậm, thơm, hậu ngọt',
                    use='Espresso, Americano, latte, phin', brews=['espresso', 'phin'],
                    head='Ba hạt, một nhịp', fit='Người thích ly đậm, thơm, pha máy hoặc phin',
                    story='Robusta Di Linh, Arabica Cầu Đất và Culi: ba hạt, một nhịp. Đậm từ Robusta và Culi, thơm từ Arabica, hậu ngọt, trọn vị trong một ly.'),
    'ng-suoi': dict(n='Suối', sub='Stream', badge='Thủy', kg=400, base='b82', col='#8A6F5A', oshort='Di Linh · Cầu Đất',
                    proc='Robusta Honey : Arabica : Culi = 7 : 2 : 1', origin='70% Robusta Honey Di Linh, 20% Arabica Cầu Đất, 10% Culi',
                    roast='Rang vừa (Medium), rang mộc', taste='Đậm vừa, ngọt mật, thơm, hậu dài',
                    use='Phin, đen đá, sữa đá, cold brew', brews=['phin', 'coldbrew'],
                    head='Ba hạt chảy chung một dòng', fit='Người thích ly đậm vừa, ngọt mật, hậu dài',
                    story='Robusta Honey làm nền, Arabica Cầu Đất cho hương, chút Culi cho đậm: ba hạt chảy chung một dòng.'),
    'ng-nang': dict(n='Nắng', sub='Sunshine', badge='Hỏa', kg=350, base='pp', col='#B33A24', oshort='Di Linh',
                    proc='Honey, giữ lớp thịt trái khi phơi', origin='100% Robusta Premium, Di Linh, Lâm Đồng',
                    roast='Rang vừa (Medium), rang mộc', taste='Cân bằng, đường nâu, caramel, hậu ngọt',
                    use='Phin, đen đá, sữa đá, cold brew', brews=['phin', 'coldbrew'],
                    head='Đắng đầu lưỡi, ngọt ở hậu vị', fit='Người thích Robusta êm, hậu ngọt, pha phin hoặc cold brew',
                    story='Trái chín hái chọn, giữ lớp thịt trái khi phơi dưới nắng cao nguyên Di Linh. Đắng đầu lưỡi, ngọt ở hậu vị, cho những giờ làm việc cần hứng khởi.'),
    'ng-nui': dict(n='Núi', sub='Mountain', badge='Thổ', kg=400, base='pc', col='#5A3A28', oshort='Tân Nghĩa · Di Linh',
                   proc='Natural, phơi nguyên trái', origin='100% Robusta Sẻ tuyển chọn, Tân Nghĩa, Di Linh',
                   roast='Rang đậm (Dark), rang mộc', taste='Đậm đà, đắng rõ, hậu tròn, socola đen',
                   use='Phin truyền thống, đen đá, sữa đá', brews=['phin'],
                   head='Đậm, đắng rõ, cho buổi sáng tỉnh táo', fit='Người thích phin đậm, đen đá, sữa đá buổi sáng',
                   story='Từ gốc Cà Sẻ trên đồi Tân Nghĩa, cây 15 năm tuổi, chăm sóc theo hướng tự nhiên. Rang mộc, không tẩm ướp. Đậm, đắng rõ, hậu tròn, cho những buổi sáng cần tỉnh táo.'),
    'ng-may': dict(n='Mây', sub='Cloud', badge='Soleil', kg=420, base='b73', col='#C98F7A', oshort='Di Linh · Cầu Đất',
                   proc='Robusta Sẻ : Arabica = 7 : 3', origin='70% Robusta Sẻ Tân Nghĩa, 30% Arabica Cầu Đất',
                   roast='Rang vừa (Medium), rang mộc', taste='Đậm, thơm, hậu ngọt thanh',
                   use='Phin, espresso, Americano, latte', brews=['phin', 'espresso'],
                   head='Vững như núi, thoáng như mây', fit='Người thích ly đậm mà thoáng, pha phin hoặc máy',
                   story='Trước bình minh, mây phủ kín thung lũng, chỉ còn đỉnh núi nhô lên. Bảy phần Robusta Sẻ, ba phần Arabica Cầu Đất: vững như núi, thoáng như mây.'),
}
NGU_NOTE = 'Bộ sưu tập Ngũ Hành: sáu dòng cà phê, sáu cảnh trời đất Di Linh. Bán theo túi 250 g, chưa có giá sỉ.'


def _brews(text, kind):
    t = text.lower()
    b = set()
    if 'phin' in t or kind == 'phin': b.add('phin')
    if kind == 'may' or any(k in t for k in ('espresso', 'latte', 'americano', 'cappuccino', 'máy')): b.add('espresso')
    if any(k in t for k in ('pour', 'v60', 'thủ công', 'drip')): b.add('v60')
    if 'cold' in t: b.add('coldbrew')
    return b


def _pk(proc):
    t = proc.lower()
    return [k for k in ('natural', 'honey', 'washed') if k in t] or ['lot']


def products(P):
    """Danh mục theo thứ tự gợi ý: 14 dòng theo kg, bộ Ngũ Hành túi 250 g, rồi các dòng sắp mở bán."""
    out = []
    for i in ORDER:
        slug = SLUG[i]
        m = MAN.get('medili-' + slug)
        if i in NGU:
            g = NGU[i]
            x = {k: v for k, v in g.items() if k not in ('kg', 'base', 'story')}
            x.update(id=i, line='Ngũ Hành', tier='Ngũ Hành', kind='all', full=f'{g["n"]} · {g["sub"]}', p=[g['kg'], None, None], st='ban',
                     bars=list(P[g['base']]['bars']), tips=[g['story']], note=NGU_NOTE, kline=f'Ngũ Hành · {g["badge"]}')
        elif i in NEW6:
            x = dict(NEW6[i])
            x.update(id=i, kind='all', p=None, st='sap', brews=list(m['brews']), use=', '.join(BREW[b] for b in m['brews']).capitalize(),
                     bars=[round(m['profile'][k] * 20 / 5) * 5 for k in ('intensity', 'sweetness', 'acidity', 'complexity')],
                     full=x['n'], note=SAP_NOTE)
        else:
            s = P[i]
            d = s.get('desc') or {}
            use = d.get('use') or s['use']
            b = _brews(use + ' ' + s['use'], s['kind']) | set(m['brews'] if m else [])
            if i in ('cat', 'cul'): b |= {'phin', 'espresso'}   # bảng báo giá T11/2026: Phin · Máy
            p = s['p'] if s['p'] and s['p'][0] else None
            x = dict(id=i, n=s['n'], full=s.get('full') or s['n'], line=s['line'], tier=s['tier'], kind=s['kind'],
                     col=GREENFIX.get(s['col'], s['col']), oshort=OSHORT.get(s['line'], 'Lâm Đồng'), proc=s['proc'],
                     head=d.get('head', ''), origin=d.get('origin') or ('Robusta Di Linh, Lâm Đồng' if s['line'] == 'Robusta' else 'Lâm Đồng'),
                     roast=d.get('roast') or 'Xác nhận theo lô', taste=d.get('taste') or s['taste'], use=use, fit=s['fit'],
                     tips=list(d.get('tips') or []), p=p, st='ban' if p else 'lh', brews=[k for k in BREW if k in b], bars=list(s['bars']))
            notes = []
            if i in ('ms', 'cul'): notes.append('Gói lẻ 250 g, 500 g: liên hệ MeDili.')
            if p and p[1] is None: notes.append('Chưa có giá sỉ, MeDili sẽ báo giá khi đặt hàng.')
            if not p: notes.append('Giá theo từng lô, MeDili sẽ báo giá khi đặt hàng.')
            x['note'] = ' '.join(notes)
        x['brews'] = [k for k in BREW if k in x['brews']]
        x['pk'] = _pk(x['proc'])
        x['packs'] = [250] if i in NGU else [1000, 5000] if i in ('ms', 'cul') else PACKS
        x.setdefault('badge', x['tier'])
        x.setdefault('sub', x['oshort'])
        x.setdefault('kline', f'{x["tier"]} · {x["oshort"]}')
        x.setdefault('grinds', None)
        x['slug'] = slug
        x['file'] = f'sp-{slug}.html'
        sanpham.catalog(x, 'ngu' if i in NGU else 'sap' if i in NEW6 else 'core' if i in sanpham.TG_ID else 'le')   # trang quản trị (27/11/2026)
        out.append(x)
    assert len(out) == len(ORDER) and len({x['file'] for x in out}) == len(ORDER)
    return out


def tui(x):
    """Dòng bán theo túi 250 g (bộ Ngũ Hành)."""
    return x['packs'] == [250]


def price_txt(x):
    if not x['p']:
        return 'Liên hệ'
    return f'{fm(x["p"][0] * 250)} đ/túi 250 g' if tui(x) else f'{fm(x["p"][0] * 1000)} đ/kg'


def price_html(x):
    """Giá trên thẻ: số tiền đậm, đơn vị nhỏ."""
    if not x['p']:
        return 'Liên hệ'
    v, u = (x['p'][0] * 250, 'túi 250 g') if tui(x) else (x['p'][0] * 1000, 'kg')
    return f'{fm(v)} đ<small>/{u}</small>'


def bag(x, cls=''):
    return (f'<div class="sb {cls}" style="--c:{x["col"]}" aria-hidden="true"><span class="sb-t">{esc(x["badge"])}</span>'
            f'<span class="sb-l"><b>MeDili</b><i>{esc(x["n"])}</i><small>{esc(x["sub"])}</small></span></div>')


def badge_html(x):
    return {'sap': '<span class="sh-bd">Sắp mở bán</span>', 'het': '<span class="sh-bd">Tạm hết hàng</span>'}.get(x['st'], '')


def card(x):
    badge = badge_html(x)
    add = 'Thêm vào giỏ' if x['st'] == 'ban' else 'Hỏi giá'
    return (f'<article class="sh-card" data-id="{x["id"]}"><a class="sh-img" href="{x["file"]}" tabindex="-1" aria-hidden="true">{bag(x)}</a>'
            f'<div class="sh-b">{badge}<p class="sh-k">{esc(x["kline"])}</p>'
            f'<h3 class="sh-h"><a href="{x["file"]}">{esc(x["n"])}</a></h3>'
            f'<p class="sh-t">{esc(x["taste"])}</p><p class="sh-u">{" · ".join(BREW[b] for b in x["brews"])}</p>'
            f'<div class="sh-f"><b class="sh-p">{price_html(x)}</b><div class="sh-a">'
            + (f'<a class="btn small main" href="{ZALO}" target="_blank" rel="noopener">Hỏi qua Zalo</a>' if x['st'] == 'het' else
               f'<button type="button" class="btn small main" data-add="{x["id"]}">{add}</button>') +
            f'<button type="button" class="btn small ghost" data-quick="{x["id"]}">Xem nhanh</button></div></div></div></article>')


def jsdata(L):
    keep = ('id', 'n', 'file', 'tier', 'line', 'kind', 'brews', 'pk', 'p', 'st', 'packs', 'col', 'taste', 'use', 'fit', 'head', 'oshort', 'bars', 'note',
            'kline', 'grinds')
    return json.dumps([{k: x[k] for k in keep} for x in L], ensure_ascii=False, separators=(',', ':'))


def js_head(L):
    return (f"const D={jsdata(L)};\nconst ZALO={ZALO!r},EMAIL={EMAIL!r},PHONE={PHONE!r};\n"
            f"const FORM={FORM!r},FN={{name:{FORM_F['name']!r},phone:{FORM_F['phone']!r},txt:{FORM_F['txt']!r}}};\n"
            f"const BREW={json.dumps(BREW, ensure_ascii=False)},GRIND={json.dumps(GRIND, ensure_ascii=False)},BARS={json.dumps(BARS, ensure_ascii=False)};\n")


# ---------------- CSS ----------------
CSS = r'''
.sh-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* bao bì minh họa */
.sb{position:relative;width:100%;max-width:230px;margin:auto;aspect-ratio:4/5;background:var(--c);
 background:linear-gradient(160deg,color-mix(in srgb,var(--c) 78%,#FFF3D6) 0%,var(--c) 52%,color-mix(in srgb,var(--c) 78%,#1E120C) 100%);
 clip-path:polygon(7% 0,93% 0,100% 6%,100% 100%,0 100%,0 6%);border-radius:0 0 14px 14px;display:grid;place-items:center;color:#FFF3D6}
.sb::before{content:"";position:absolute;left:0;right:0;top:10%;border-top:2px dashed rgba(255,243,214,.45)}
.sb-t{position:absolute;top:15%;left:0;right:0;text-align:center;font:600 .62rem/1 var(--body);letter-spacing:.16em;text-transform:uppercase;opacity:.92}
.sb-l{width:76%;background:#FFF3D6;color:#3A2418;border-radius:8px;padding:12px 8px 10px;display:grid;gap:4px;text-align:center;margin-top:12%}
.sb-l b{font:800 1.25rem/1 var(--display);letter-spacing:.02em;color:#4A2C1A}
.sb-l i{font:600 .78rem/1.25 var(--body);font-style:normal;overflow-wrap:anywhere}
.sb-l small{font:600 .6rem/1.2 var(--body);letter-spacing:.12em;text-transform:uppercase;color:#8D4E22}
.sb.big{max-width:320px}.sb.big .sb-l{padding:16px 10px 14px}.sb.big .sb-l b{font-size:1.7rem}.sb.big .sb-l i{font-size:1rem}.sb.big .sb-t{font-size:.72rem}
/* thanh lọc */
.sh-tool{display:grid;gap:12px;background:var(--panel);border:1px solid var(--rule);border-radius:16px;padding:14px 16px;position:sticky;top:calc(53px + env(safe-area-inset-top,0px));z-index:5}
.sh-s{display:flex;align-items:center;gap:8px;border:1px solid var(--rule);border-radius:999px;padding:0 14px;background:var(--bg)}
.sh-s svg{width:18px;height:18px;flex:none;fill:none;stroke:var(--muted);stroke-width:2;stroke-linecap:round}
.sh-s input{border:0;background:transparent;color:var(--ink);font:500 1rem var(--body);padding:10px 0;width:100%;min-width:0;outline:none}
.sh-s:focus-within{border-color:var(--accent);box-shadow:0 0 0 2px var(--tint)}
.sh-tabs{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;margin:0 -4px;padding:2px 4px}
.sh-tabs::-webkit-scrollbar{display:none}
.sh-tabs button{flex:none;font:600 .86rem/1.2 var(--body);border:1px solid var(--rule);background:transparent;color:var(--ink);border-radius:999px;padding:7px 12px;cursor:pointer;white-space:nowrap}
.sh-tabs button i{font-style:normal;color:var(--muted);font-weight:500;margin-left:2px}
.sh-tabs button[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:var(--panel)}
.sh-tabs button[aria-pressed="true"] i{color:inherit;opacity:.75}
.sh-row{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px}
.sh-row label{display:flex;align-items:center;gap:6px;font:600 .84rem var(--body);color:var(--muted)}
.sh-row select{font:500 .9rem var(--body);color:var(--ink);background:var(--bg);border:1px solid var(--rule);border-radius:10px;padding:6px 8px}
.sh-n{margin:0 0 0 auto;font:500 .84rem var(--body);color:var(--muted)}
/* thẻ sản phẩm */
.sh-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,230px),1fr));gap:16px}
.sh-card{display:grid;grid-template-rows:auto 1fr;background:var(--panel);border:1px solid var(--rule);border-radius:16px;overflow:hidden;min-width:0}
.sh-card[hidden]{display:none}
.sh-img{display:block;background:var(--tint);padding:18px 18px 14px;text-decoration:none;color:inherit}
.sh-img .sb{max-width:150px}
.sh-b{display:flex;flex-direction:column;gap:5px;padding:12px 14px 14px;min-width:0}
.sh-bd{align-self:flex-start;font:700 .66rem/1 var(--body);letter-spacing:.08em;text-transform:uppercase;background:var(--tint);color:var(--accent);border:1px solid var(--accent);border-radius:999px;padding:4px 8px}
.sh-k{margin:0;font:600 .7rem/1.3 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
.sh-h{margin:0;font:800 1.3rem/1.15 var(--display);letter-spacing:.01em}
.sh-h a{color:var(--ink);text-decoration:none}.sh-h a:hover{color:var(--accent)}
.sh-t{margin:0;font-size:.9rem;line-height:1.45}
.sh-u{margin:0;font-size:.8rem;color:var(--muted)}
.sh-f{margin-top:auto;padding-top:8px;display:grid;gap:8px}
.sh-p{font:700 1rem var(--mono);color:var(--ink)}
.sh-p small{font:500 .76rem var(--body);color:var(--muted);margin-left:2px;white-space:nowrap}
.sh-a{display:flex;flex-wrap:wrap;gap:6px}
.sh-a .btn{flex:1 1 auto}
.sh-empty{text-align:center;color:var(--muted);margin:10px 0}
.sh-empty button{background:none;border:0;font:inherit;cursor:pointer;padding:0}
.sh-info{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:14px}
.sh-info p{margin:4px 0 0}
@media (max-width:560px){.sh-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.sh-img{padding:12px 10px 8px}.sh-b{padding:10px 10px 12px}
 .sh-h{font-size:1.08rem}.sh-t{font-size:.82rem;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}.sh-u{font-size:.74rem}
 .sh-a .btn{padding:7px 8px;font-size:.78rem}.sh-tool{position:static}.sb-l b{font-size:1.05rem}.sb-l i{font-size:.7rem}}
/* hộp xem nhanh, thông báo */
.sh-dlg{border:0;border-radius:18px;padding:0;max-width:min(760px,calc(100vw - 24px));width:100%;background:var(--panel);color:var(--ink);box-shadow:0 24px 60px rgba(30,18,12,.35)}
.sh-dlg::backdrop{background:rgba(30,18,12,.55)}
.sh-dw{display:grid;grid-template-columns:minmax(0,2fr) minmax(0,3fr);gap:20px;padding:22px;position:relative}
.sh-x{position:absolute;top:10px;right:10px;width:36px;height:36px;border-radius:50%;border:1px solid var(--rule);background:var(--panel);color:var(--ink);font:500 1.3rem/1 var(--body);cursor:pointer}
@media (max-width:620px){.sh-dw{grid-template-columns:minmax(0,1fr);padding:18px}.sh-dw .sb{max-width:150px}}
.sh-toast{position:fixed;left:50%;bottom:calc(18px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);z-index:80;background:var(--ink);color:var(--panel);border-radius:999px;padding:10px 18px;font:500 .9rem var(--body);box-shadow:0 10px 26px rgba(30,18,12,.3);max-width:calc(100vw - 24px)}
.sh-toast a{color:inherit;font-weight:700}
/* trang sản phẩm */
.pd-bc{font-size:.86rem;color:var(--muted);display:flex;flex-wrap:wrap;gap:4px 8px}
.pd-bc a{color:var(--muted)}.pd-bc span{color:var(--ink)}
.pd-top{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:30px;align-items:start}
.pd-fig{background:var(--tint);border-radius:22px;padding:34px 24px;position:sticky;top:calc(72px + env(safe-area-inset-top,0px))}
.pd-info{display:grid;gap:12px;min-width:0}
.pd-h{font:800 clamp(2.2rem,5vw,3.4rem)/1.05 var(--display);margin:0;text-wrap:balance}
.pd-tag{font:italic 600 1.2rem/1.35 var(--sign);margin:0;color:var(--accent)}
.pd-en{font:italic 600 .45em var(--sign);color:var(--muted);letter-spacing:0;vertical-align:.25em}
.pd-story{margin:10px 0 0;font:italic 600 1.02rem/1.5 var(--sign);color:var(--accent)}
.pd-dl{display:grid;grid-template-columns:auto minmax(0,1fr);gap:6px 16px;margin:0;font-size:.95rem}
.pd-dl dt{font-weight:600;color:var(--muted)}.pd-dl dd{margin:0}
.pd-pr{display:grid;gap:4px;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:12px 0}
.pd-pr b{font:700 1.5rem var(--mono)}
.pd-pr small{color:var(--muted);font-size:.86rem}
.pd-form{display:grid;gap:12px}
.pd-form fieldset{border:0;margin:0;padding:0;min-width:0}
.pd-form legend{font:600 .88rem var(--body);margin-bottom:6px;padding:0}
.pd-l{display:grid;gap:4px;font:600 .88rem var(--body)}
.pd-l select{font:500 1rem var(--body);padding:9px 11px;border:1px solid var(--rule);border-radius:10px;background:var(--bg);color:var(--ink);max-width:320px}
.pd-q{display:flex;align-items:center;gap:12px;font:600 .88rem var(--body)}
.pd-st{display:inline-flex;align-items:center;border:1px solid var(--rule);border-radius:999px;overflow:hidden}
.pd-st button{width:38px;height:38px;border:0;background:transparent;color:var(--ink);font:600 1.2rem/1 var(--body);cursor:pointer}
.pd-st button:hover{background:var(--tint)}
.pd-st output{min-width:30px;text-align:center;font:700 1rem var(--mono)}
.pd-sum{margin:0;font-size:.95rem}.pd-sum b{font:700 1.05rem var(--mono)}.pd-sum small{display:block;color:var(--muted);font-size:.8rem}
.pd-note{margin:0;padding:10px 12px;border-radius:10px;background:var(--tint);font-size:.88rem}
.pd-bars{display:grid;gap:8px;max-width:520px}
.pd-bar{display:grid;grid-template-columns:90px minmax(0,1fr) 34px;gap:10px;align-items:center;font-size:.88rem}
.pd-tr{display:block;height:9px;border-radius:999px;background:var(--rule);overflow:hidden}
.pd-tr i{display:block;height:100%;border-radius:999px;background:var(--accent)}
.pd-bar b{font:600 .8rem var(--mono);color:var(--muted);text-align:right}
.pd-two{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.pd-tips{margin:6px 0 0;padding-left:1.1em;display:grid;gap:4px}
.pd-brew{display:flex;flex-wrap:wrap;gap:8px}
.pd-rel{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
@media (max-width:980px){.pd-rel{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:760px){.pd-top{grid-template-columns:minmax(0,1fr);gap:18px}.pd-fig{position:static;padding:22px}.pd-fig .sb{max-width:210px}.pd-two{grid-template-columns:minmax(0,1fr)}}
/* giỏ hàng */
.ct-wrap{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:22px;align-items:start}
.ct-list{display:grid;gap:10px}
.ct-row{display:grid;grid-template-columns:44px minmax(0,1fr) auto;gap:6px 12px;align-items:center;background:var(--panel);border:1px solid var(--rule);border-radius:14px;padding:12px}
.ct-sw{width:44px;height:54px;border-radius:4px 4px 8px 8px;background:var(--c);clip-path:polygon(10% 0,90% 0,100% 8%,100% 100%,0 100%,0 8%)}
.ct-n{min-width:0}.ct-n a{color:var(--ink);font-weight:700;text-decoration:none}.ct-n a:hover{color:var(--accent)}
.ct-n small{display:block;color:var(--muted);font-size:.82rem}
.ct-n select{font:500 .82rem var(--body);color:var(--ink);background:var(--bg);border:1px solid var(--rule);border-radius:8px;padding:3px 4px;margin:4px 4px 0 0;max-width:100%}
.ct-r{display:grid;justify-items:end;gap:6px}
.ct-r b{font:700 .95rem var(--mono);white-space:nowrap}
.ct-rm{background:none;border:0;color:var(--muted);font:500 .8rem var(--body);text-decoration:underline;cursor:pointer;padding:0}
.ct-side{display:grid;gap:14px;position:sticky;top:calc(72px + env(safe-area-inset-top,0px))}
.ct-tot{display:grid;gap:6px}
.ct-tot p{margin:0;display:flex;justify-content:space-between;gap:12px;font-size:.92rem}
.ct-tot p b{font-family:var(--mono)}
#ct-tier{font-family:var(--body)}
.ct-tot .big{font-size:1.05rem;border-top:1px solid var(--rule);padding-top:8px}
.ct-tot .big b{font-size:1.25rem}
.ct-empty{text-align:center;display:grid;gap:10px;justify-items:center;padding:40px 16px}
.ct-send{display:grid;gap:8px}
.ct-send .btn{text-align:center}
.ct-err{color:var(--bad);font-weight:600;margin:0}
.ct-pt{border:0;margin:2px 0 0;padding:0;display:grid;gap:8px;min-width:0}
.ct-pt legend{padding:0;margin-bottom:6px}
.ct-op{display:grid;grid-template-columns:auto minmax(0,1fr);gap:10px;align-items:start;border:1px solid var(--rule);border-radius:12px;padding:10px 12px;cursor:pointer;background:var(--bg)}
.ct-op input{margin:3px 0 0;accent-color:var(--accent)}
.ct-op span{display:grid;gap:2px}
.ct-op small{color:var(--muted);font-size:.82rem}
.ct-op:has(input:checked){border-color:var(--accent);background:var(--tint)}
.ct-op:has(input:disabled){opacity:.55;cursor:not-allowed}
#ct-go{width:100%;font-size:1rem;padding:13px 16px}
#ct-go:disabled{opacity:.6;cursor:progress}
@media (max-width:900px){.ct-wrap{grid-template-columns:minmax(0,1fr)}.ct-side{position:static}}
@media (max-width:420px){.ct-row{grid-template-columns:36px minmax(0,1fr)}.ct-sw{width:36px;height:44px}.ct-r{grid-column:2;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:6px 12px}}
/* tìm kiếm */
.sr-box{display:grid;gap:10px}
.sr-chips{display:flex;flex-wrap:wrap;gap:6px}
.sr-chips button{font:600 .84rem var(--body);border:1px solid var(--rule);background:var(--panel);color:var(--ink);border-radius:999px;padding:6px 12px;cursor:pointer}
.sr-chips button:hover{border-color:var(--accent);color:var(--accent)}
.sr-n{margin:0;color:var(--muted);font-size:.88rem}
.sr-list{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.sr-list a{display:grid;gap:3px;background:var(--panel);border:1px solid var(--rule);border-radius:14px;padding:12px 14px;color:var(--ink);text-decoration:none}
.sr-list a:hover{border-color:var(--accent)}
.sr-list b{font:700 1.02rem var(--body)}
.sr-k{font:600 .68rem/1.2 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
.sr-x{font-size:.88rem;color:var(--muted);overflow-wrap:anywhere}
.sr-x mark,.sr-list b mark{background:var(--tint);color:var(--ink);border-radius:3px;padding:0 1px}
'''

# ---------------- JS dùng chung cho trang cửa hàng, sản phẩm, giỏ ----------------
SHOP_JS = r'''
const byId=Object.fromEntries(D.map(x=>[x.id,x]));
const fmt=n=>Math.round(n).toLocaleString('vi-VN').replace(/,/g,'.');
const wlab=w=>w>=1000?(w/1000)+' kg':w+' g';
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const unitP=(x,tier)=>x.p?(tier&&x.p[1]?x.p[1]:x.p[0]):null;   // nghìn đồng mỗi kg
const tuiJ=x=>x.packs.length===1&&x.packs[0]===250;   // bộ Ngũ Hành: bán theo túi 250 g
const ptxt=x=>x.p?(tuiJ(x)?fmt(x.p[0]*250)+' đ/túi 250 g':fmt(x.p[0]*1000)+' đ/kg'):'Liên hệ';
const GR=x=>x.grinds||GRIND;
function toast(h){let t=document.getElementById('sh-toast');if(!t){t=document.createElement('div');t.id='sh-toast';t.className='sh-toast';t.setAttribute('role','status');document.body.append(t)}
 t.innerHTML=h;t.hidden=false;clearTimeout(t._h);t._h=setTimeout(()=>{t.hidden=true},3600)}
function addCart(id,w,g,q){MDC.add({id,w,g,q});toast(`Đã thêm <b>${esc(byId[id].n)}</b> vào giỏ · <a href="gio-hang.html">Xem giỏ</a>`)}
function buyHTML(x,k){
 const ban=x.st==='ban',w0=x.packs.includes(500)?500:x.packs[0];
 return `<div class="pd-form" data-buy="${x.id}">
 <fieldset><legend>Quy cách</legend><div class="opts">${x.packs.map(w=>`<label><input type="radio" name="w-${k}" value="${w}"${w===w0?' checked':''}>${wlab(w)}</label>`).join('')}</div></fieldset>
 <label class="pd-l">${x.grinds?'Bản và độ xay':'Độ xay'}<select name="g">${GR(x).map(g=>`<option>${g}</option>`).join('')}</select></label>
 <div class="pd-q"><span>Số lượng</span><div class="pd-st"><button type="button" data-d="-1" aria-label="Bớt một">−</button><output aria-live="polite">1</output><button type="button" data-d="1" aria-label="Thêm một">+</button></div></div>
 <p class="pd-sum" aria-live="polite"></p>
 <div class="cta" style="margin:0">${x.st==='het'?'<button type="button" class="btn main" data-act="add" disabled>Tạm hết hàng</button>':`<button type="button" class="btn main" data-act="add">${ban?'Thêm vào giỏ':'Thêm vào giỏ để hỏi giá'}</button>`}<a class="btn" href="${ZALO}" target="_blank" rel="noopener" data-act="zalo">Hỏi qua Zalo</a></div></div>`}
function wireBuy(root){
 const f=root.querySelector('[data-buy]');if(!f)return;const x=byId[f.dataset.buy],out=f.querySelector('output');
 const st=()=>({w:+f.querySelector('input[type=radio]:checked').value,g:f.querySelector('select').value,q:+out.textContent});
 const sum=()=>{const s=st(),u=unitP(x,0);f.querySelector('.pd-sum').innerHTML=x.st==='het'?`<b>Tạm hết hàng</b><small>Nhắn Zalo để MeDili báo khi có hàng lại.</small>`:u?`Tạm tính: <b>${fmt(u*s.w*s.q)} đ</b><small>${tuiJ(x)?`Túi 250 g giá ${fmt(u*250)} đ`:`Giá lẻ ${fmt(u*1000)} đ/kg`}, chưa gồm 8% VAT và phí giao.${x.p[1]?' Đơn từ 5 kg được giá sỉ.':''}</small>`:`Giá: <b>Liên hệ</b><small>MeDili báo giá khi nhận đơn.</small>`};
 f.addEventListener('change',sum);
 f.querySelectorAll('[data-d]').forEach(b=>b.addEventListener('click',()=>{out.textContent=Math.max(1,Math.min(99,+out.textContent+ +b.dataset.d));sum()}));
 f.querySelector('[data-act=add]').addEventListener('click',()=>{const s=st();addCart(x.id,s.w,s.g,s.q)});
 f.querySelector('[data-act=zalo]').addEventListener('click',async()=>{const s=st();const t=`Chào MeDili, mình muốn hỏi về ${x.n}, gói ${wlab(s.w)}, ${s.g.toLowerCase()}, số lượng ${s.q}.`;
  try{await navigator.clipboard.writeText(t);toast('Đã sao chép câu hỏi. Dán vào Zalo MeDili để gửi.')}catch(e){}});
 sum()}
'''

SHOP_PAGE_JS = r'''
(()=>{const grid=document.getElementById('sh-grid'),cards=[...grid.children],q=document.getElementById('sh-q'),pk=document.getElementById('sh-pk'),so=document.getElementById('sh-sort'),
 tabs=[...document.querySelectorAll('.sh-tabs button')],n=document.getElementById('sh-n'),empty=document.getElementById('sh-empty');
 const N=s=>s.normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[đĐ]/g,'d').toLowerCase();
 const TXT=Object.fromEntries(D.map(x=>[x.id,N([x.n,x.tier,x.line,x.taste,x.use,x.fit,x.head,x.oshort,x.pk.join(' '),x.brews.map(b=>BREW[b]).join(' ')].join(' '))]));
 const F={all:()=>1,ngu:x=>x.line==='Ngũ Hành',phin:x=>x.brews.includes('phin'),may:x=>x.brews.includes('espresso'),robusta:x=>x.line==='Robusta',arabica:x=>x.line==='Arabica',
  blend:x=>x.line==='Blend',dac:x=>x.tier==='Specialty'||x.line==='Đặc sản',sap:x=>x.st==='sap'};
 let tab='all';
 const P0=new URLSearchParams(location.search);if(F[P0.get('loai')])tab=P0.get('loai');if(P0.get('q'))q.value=P0.get('q');if(P0.get('so-che'))pk.value=P0.get('so-che');
 function apply(){const terms=N(q.value.trim()).split(/\s+/).filter(Boolean);let shown=0;
  const order=[...cards];const pr=c=>{const x=byId[c.dataset.id];return x.p?x.p[0]:1e9};
  if(so.value==='pa')order.sort((a,b)=>pr(a)-pr(b));else if(so.value==='pd')order.sort((a,b)=>(byId[b.dataset.id].p?byId[b.dataset.id].p[0]:-1)-(byId[a.dataset.id].p?byId[a.dataset.id].p[0]:-1));
  else if(so.value==='n')order.sort((a,b)=>byId[a.dataset.id].n.localeCompare(byId[b.dataset.id].n,'vi'));
  order.forEach(c=>{const x=byId[c.dataset.id],ok=F[tab](x)&&(!pk.value||x.pk.includes(pk.value))&&terms.every(t=>TXT[x.id].includes(t));c.hidden=!ok;if(ok)shown++;grid.append(c)});
  n.textContent=shown+' dòng cà phê';empty.hidden=!!shown;tabs.forEach(b=>b.setAttribute('aria-pressed',b.dataset.f===tab));
  const u=new URLSearchParams();if(tab!=='all')u.set('loai',tab);if(q.value.trim())u.set('q',q.value.trim());if(pk.value)u.set('so-che',pk.value);
  try{history.replaceState(null,'',u.toString()?'?'+u:location.pathname)}catch(e){}}
 tabs.forEach(b=>b.addEventListener('click',()=>{tab=b.dataset.f;apply()}));
 q.addEventListener('input',apply);pk.addEventListener('change',apply);so.addEventListener('change',apply);
 document.getElementById('sh-reset').addEventListener('click',()=>{tab='all';q.value='';pk.value='';apply()});
 grid.addEventListener('click',e=>{const a=e.target.closest('[data-add]'),v=e.target.closest('[data-quick]');
  if(a){const x=byId[a.dataset.add];addCart(x.id,x.packs.includes(500)?500:x.packs[0],GR(x)[0],1)}
  if(v)quick(byId[v.dataset.quick])});
 const dlg=document.getElementById('sh-dlg'),dw=document.getElementById('sh-dw');
 function quick(x){
  dw.innerHTML=`<button type="button" class="sh-x" aria-label="Đóng">×</button>
  <div>${document.querySelector(`.sh-card[data-id="${x.id}"] .sb`).outerHTML}</div>
  <div class="pd-info"><p class="eye">${esc(x.kline)}</p><h2 class="pd-h" id="sh-dt" style="font-size:2rem">${esc(x.n)}</h2>
  ${x.head?`<p class="pd-tag">${esc(x.head)}</p>`:''}<p style="margin:0">${esc(x.taste)}</p><p class="note">Pha: ${x.brews.map(b=>BREW[b]).join(' · ')}. Phù hợp với: ${esc(x.fit)}.</p>
  <div class="pd-pr"><b>${ptxt(x)}</b>${x.p&&x.p[1]?`<small>Sỉ 5–20 kg/tháng ${fmt(x.p[1]*1000)} đ/kg · trên 20 kg ${fmt(x.p[2]*1000)} đ/kg</small>`:x.p&&tuiJ(x)?`<small>Tương đương ${fmt(x.p[0]*1000)} đ/kg</small>`:''}</div>
  ${x.note?`<p class="pd-note">${esc(x.note)}</p>`:''}${buyHTML(x,'q')}<a class="lnk" href="${x.file}">Xem trang ${esc(x.n)} →</a></div>`;
  dw.querySelector('.sh-x').addEventListener('click',()=>dlg.close());wireBuy(dw);
  if(dlg.showModal)dlg.showModal();else location.href=x.file}
 dlg.addEventListener('click',e=>{if(e.target===dlg)dlg.close()});
 apply()})();
'''

PD_JS = r'''
wireBuy(document);
'''

CART_JS = r'''
(()=>{const box=document.getElementById('ct'),K2='medili-cart-khach',$=id=>document.getElementById(id);
 const f=$('ct-f'),msg=$('ct-msg'),err=$('ct-err'),go=$('ct-go');
 try{const v=JSON.parse(localStorage.getItem(K2)||'{}');for(const k in v)if(f.elements[k])f.elements[k].value=v[k]}catch(e){}
 if(f.elements.ai.selectedIndex<0)f.elements.ai.selectedIndex=0;if(!f.elements.pt.value)f.elements.pt[0].checked=true;
 // mã đơn giữ nguyên trong phiên để nội dung xem trước khớp với đơn gửi đi
 let CODE='';try{CODE=sessionStorage.getItem('medili-ma')||''}catch(e){}if(!CODE){CODE=MDO.code();try{sessionStorage.setItem('medili-ma',CODE)}catch(e){}}
 const today=()=>{const d=new Date();return String(d.getDate()).padStart(2,'0')+'/'+String(d.getMonth()+1).padStart(2,'0')+'/'+d.getFullYear()};
 function calc(){const c=MDC.get().filter(it=>byId[it.id]);let kg=0;c.forEach(it=>{const x=byId[it.id];if(x.p&&!tuiJ(x))kg+=it.w*it.q/1000});const tier=kg>=5?1:0;
  let tot=0,ask=0;const rows=c.map(it=>{const x=byId[it.id],u=unitP(x,tier),v=u?u*it.w*it.q:null;if(v)tot+=v;else ask++;return {it,x,v}});
  const all=c.reduce((a,it)=>a+it.w*it.q,0)/1000,vat=Math.round(tot*.08);
  return {c,rows,kg,all,tier,tot,vat,pay:tot+vat,ask,used:!!tier&&rows.some(o=>o.x.p&&o.x.p[1]&&!tuiJ(o.x))}}
 const PT=r=>r.ask?'bg':f.elements.pt.value;
 function text(){const r=calc(),v=f.elements,pt=PT(r);const L=['ĐƠN CÀ PHÊ · MEDILI '+CODE,'Ngày: '+today(),''];
  r.rows.forEach(({it,x,v:val},i)=>L.push(`${i+1}. ${x.n} · ${wlab(it.w)} · ${it.g} · x${it.q} · ${val?fmt(val)+' đ':'hỏi giá'}`));
  L.push('',`Tổng khối lượng: ${(Math.round(r.all*10)/10).toLocaleString('vi-VN')} kg`);
  L.push(`Tạm tính: ${fmt(r.tot)} đ (${r.used?'giá sỉ cấp 1':'giá lẻ'})${r.ask?' + '+r.ask+' dòng hỏi giá':''}`);
  L.push(`VAT 8%: ${fmt(r.vat)} đ`,`Cần thanh toán: ${fmt(r.pay)} đ, chưa gồm phí giao`);
  L.push(r.all>=10?'Phí giao: miễn phí (đơn từ 10 kg)':'Phí giao: MeDili báo và thu sau');
  L.push('Thanh toán: '+(pt==='bg'?'chờ MeDili báo giá rồi gửi link thanh toán':pt==='cod'?'tiền mặt khi nhận hàng':'chuyển khoản ngay bằng mã QR'),'');
  L.push('Khách: '+(v.ten.value.trim()||'...')+' · '+(v.sdt.value.trim()||'...'));
  if(v.dc.value.trim())L.push('Giao đến: '+v.dc.value.trim());L.push('Mua cho: '+v.ai.value);if(v.gc.value.trim())L.push('Ghi chú: '+v.gc.value.trim());
  return L.join('\n')}
 function render(){const r=calc();$('ct-has').hidden=!r.c.length;$('ct-none').hidden=!!r.c.length;
  box.innerHTML=r.rows.map(({it,x,v},i)=>`<div class="ct-row" data-i="${i}"><i class="ct-sw" style="--c:${x.col}" aria-hidden="true"></i>
  <div class="ct-n"><a href="${x.file}">${esc(x.n)}</a><small>${esc(x.kline)} · ${x.p?(tuiJ(x)?fmt(x.p[0]*250)+' đ/túi 250 g':fmt(unitP(x,r.tier)*1000)+' đ/kg'+(r.tier&&x.p[1]?' (sỉ)':'')):'Liên hệ'}${x.st==='het'?' · Tạm hết hàng':''}</small>
  <select aria-label="Quy cách" data-k="w">${x.packs.map(w=>`<option value="${w}"${w===it.w?' selected':''}>${wlab(w)}</option>`).join('')}</select><select aria-label="Độ xay" data-k="g">${GR(x).map(g=>`<option${g===it.g?' selected':''}>${g}</option>`).join('')}</select></div>
  <div class="ct-r"><div class="pd-st"><button type="button" data-d="-1" aria-label="Bớt một">−</button><output>${it.q}</output><button type="button" data-d="1" aria-label="Thêm một">+</button></div>
  <b>${v?fmt(v)+' đ':'Hỏi giá'}</b><button type="button" class="ct-rm" data-rm>Bỏ khỏi giỏ</button></div></div>`).join('');
  $('ct-kg').textContent=(Math.round(r.all*10)/10).toLocaleString('vi-VN')+' kg';
  $('ct-tier').textContent=r.used?'Sỉ cấp 1 (từ 5 kg)':'Giá lẻ';
  $('ct-sum').textContent=fmt(r.tot)+' đ'+(r.ask?' + hỏi giá':'');$('ct-vat').textContent=fmt(r.vat)+' đ';$('ct-pay').textContent=fmt(r.pay)+' đ'+(r.ask?' + hỏi giá':'');
  $('ct-hint').textContent=r.used?'Đơn đã từ 5 kg nên áp giá sỉ cấp 1 cho các dòng có giá sỉ. Khi đạt 20 kg trong tháng, phần chênh lệch được chiết khấu vào đơn kế tiếp.':r.tier?'Các dòng trong giỏ chưa có giá sỉ, MeDili sẽ báo giá khi đặt hàng.':
   (r.kg>0?`Thêm ${(Math.round((5-r.kg)*10)/10).toLocaleString('vi-VN')} kg nữa để được giá sỉ cấp 1.`:'');
  $('ct-ship').textContent=(r.all>=10?'Đơn từ 10 kg được miễn phí giao hàng.':'Phí giao: miễn phí cho đơn từ 10 kg. Đơn dưới 10 kg, MeDili báo phí giao và thu sau.')+(r.ask?' Dòng ghi “Hỏi giá” được MeDili báo giá khi nhận đơn.':'');
  const ck=f.querySelector('input[name=pt][value=ck]');ck.disabled=!!r.ask;if(r.ask&&ck.checked)f.querySelector('input[name=pt][value=cod]').checked=true;
  const pt=PT(r);go.textContent=pt==='bg'?'Gửi đơn để MeDili báo giá':pt==='cod'?'Đặt hàng':'Đặt hàng và thanh toán';
  msg.textContent=text()}
 box.addEventListener('click',e=>{const row=e.target.closest('.ct-row');if(!row)return;const c=MDC.get(),it=c[+row.dataset.i];if(!it)return;
  const d=e.target.closest('[data-d]');if(d){it.q=Math.max(1,Math.min(99,it.q+ +d.dataset.d));MDC.set(c);render()}
  if(e.target.closest('[data-rm]')){c.splice(+row.dataset.i,1);MDC.set(c);render()}});
 box.addEventListener('change',e=>{const s=e.target.closest('select');if(!s)return;const row=s.closest('.ct-row'),c=MDC.get(),it=c[+row.dataset.i];
  it[s.dataset.k]=s.dataset.k==='w'?+s.value:s.value;const j=c.findIndex((o,k)=>k!==+row.dataset.i&&o.id===it.id&&o.w===it.w&&o.g===it.g);
  if(j>=0){c[j].q=Math.min(99,c[j].q+it.q);c.splice(+row.dataset.i,1)}MDC.set(c);render()});
 const save=()=>{const o={};['ten','sdt','dc','ai','gc','pt'].forEach(k=>o[k]=f.elements[k].value);try{localStorage.setItem(K2,JSON.stringify(o))}catch(e){}};
 f.addEventListener('input',()=>{save();render();err.hidden=true});f.addEventListener('change',()=>{save();render()});
 const ok=()=>{const v=f.elements,t=v.ten.value.trim(),p=v.sdt.value.replace(/[\s.()-]/g,''),a=v.dc.value.trim();
  const m=!t?['Vui lòng nhập tên người nhận.',v.ten]:!/^(0\d{9,10}|\+\d{8,15})$/.test(p)?['Vui lòng nhập số điện thoại đúng (ví dụ 0901234567 hoặc +84 901 234 567).',v.sdt]:a.length<6?['Vui lòng nhập địa chỉ giao. Nhận tại quán thì ghi “Nhận tại quán”.',v.dc]:null;
  if(m){err.hidden=false;err.textContent=m[0];m[1].focus();return false}return true};
 // Đặt hàng: gửi đơn thẳng cho MeDili (Google Form), lưu đơn trên máy, sang trang Thanh toán
 let busy=false;
 f.addEventListener('submit',async e=>{e.preventDefault();if(busy||!ok())return;const r=calc();if(!r.c.length)return;
  busy=true;const lab=go.textContent;go.disabled=true;go.textContent='Đang gửi đơn…';const v=f.elements,pt=PT(r),txt=text();
  try{await MDO.send({name:v.ten.value.trim(),phone:v.sdt.value.trim(),txt})}
  catch(x){busy=false;go.disabled=false;go.textContent=lab;err.hidden=false;err.textContent='Chưa gửi được đơn. Kiểm tra kết nối mạng rồi bấm lại, hoặc gửi đơn qua Zalo MeDili.';return}
  MDO.keep(CODE,{t:txt,tien:r.pay,pt});MDC.set([]);try{sessionStorage.removeItem('medili-ma')}catch(x){}
  location.href='thanh-toan.html?ma='+CODE+(pt==='ck'?'&tien='+r.pay:'&pt='+pt+(r.pay?'&tien='+r.pay:''))});
 $('ct-zl').addEventListener('click',async e=>{if(!ok()){e.preventDefault();return}try{await navigator.clipboard.writeText(text());toast('Đã sao chép đơn. Dán vào Zalo MeDili rồi gửi.')}catch(x){toast('Hãy sao chép nội dung đơn bên dưới rồi dán vào Zalo.')}});
 $('ct-em').addEventListener('click',e=>{if(!ok()){e.preventDefault();return}
  e.currentTarget.href='mailto:'+EMAIL+'?subject='+encodeURIComponent('Đơn cà phê MeDili · '+CODE)+'&body='+encodeURIComponent(text())});
 $('ct-clr').addEventListener('click',()=>{MDC.set([]);render()});
 addEventListener('storage',render);render()})();
'''

SEARCH_JS = r'''
(()=>{const q=document.getElementById('sr-q'),list=document.getElementById('sr-list'),n=document.getElementById('sr-n');
 const N=s=>s.normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/[đĐ]/g,'d').toLowerCase();
 const E=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
 let IX=null;
 // từ ngắn (tối đa 3 chữ) phải khớp nguyên từ, từ dài khớp đầu từ: "gia" không khớp "giao", "robu" khớp "robusta"
 const RX=(t,g)=>new RegExp('(^|[^a-z0-9])'+t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+(t.length<=3?'(?![a-z0-9])':''),g?'g':'');
 function hits(ns,t){const r=RX(t,1),out=[];let m;while((m=r.exec(ns))){const i=m.index+m[1].length;out.push(i);r.lastIndex=i+t.length}return out}
 function mark(s,terms){const ns=N(s);if(ns.length!==s.length)return E(s);const on=new Array(s.length).fill(0);
  terms.forEach(t=>hits(ns,t).forEach(i=>{for(let k=i;k<i+t.length;k++)on[k]=1}));
  let o='',m=0;for(let i=0;i<s.length;i++){if(on[i]&&!m){o+='<mark>';m=1}if(!on[i]&&m){o+='</mark>';m=0}o+=E(s[i])}return o+(m?'</mark>':'')}
 function snip(e,terms){for(const [src,ns] of [[e.d,e.nd],[e.x,e.nx]]){if(!src)continue;let i=-1;for(const t of terms){const j=hits(ns,t)[0];if(j!=null&&(i<0||j<i))i=j}
  if(i>=0){const a=Math.max(0,i-70),b=Math.min(src.length,i+150);return (a?'… ':'')+mark(src.slice(a,b),terms)+(b<src.length?' …':'')}}return E((e.d||e.x||'').slice(0,160))}
 function run(){const raw=q.value.trim(),terms=N(raw).split(/\s+/).filter(Boolean),ph=terms.join(' ');
  try{history.replaceState(null,'',raw?'?q='+encodeURIComponent(raw):location.pathname)}catch(e){}
  if(!IX){n.textContent='Đang tải chỉ mục…';return}
  if(!terms.length){list.innerHTML='';n.textContent='Gõ tên dòng cà phê, cách pha, sơ chế hoặc câu hỏi, ví dụ: honey, cold brew, giá sỉ.';return}
  const R=terms.map(t=>RX(t));
  const res=[];IX.forEach(e=>{let s=0;for(const r of R){const w=(r.test(e.nt)?12:0)+(r.test(e.nh)?5:0)+(r.test(e.nd)?4:0)+(r.test(e.nx)?1:0);if(!w)return;s+=w}
   if(terms.length>1){if(e.nt.includes(ph))s+=20;if(e.nh.includes(ph)||e.nd.includes(ph))s+=10;if(e.nx.includes(ph))s+=6}
   if(e.k==='Sản phẩm')s+=2;res.push([s,e])});
  res.sort((a,b)=>b[0]-a[0]);n.textContent=res.length?`${res.length} kết quả cho “${raw}”`:`Không thấy kết quả cho “${raw}”. Thử từ ngắn hơn, hoặc xem Cửa hàng.`;
  list.innerHTML=res.slice(0,40).map(([s,e])=>`<li><a href="${e.u}"><span class="sr-k">${E(e.k)}</span><b>${mark(e.t,terms)}</b><span class="sr-x">${snip(e,terms)}</span></a></li>`).join('')}
 const P0=new URLSearchParams(location.search).get('q');if(P0)q.value=P0;
 q.addEventListener('input',run);
 document.querySelectorAll('.sr-chips button').forEach(b=>b.addEventListener('click',()=>{q.value=b.textContent;run();q.focus()}));
 fetch('tim-kiem.json',{cache:'no-store'}).then(r=>r.json()).then(j=>{IX=j.map(e=>Object.assign(e,{nt:N(e.t),nh:N(e.h||''),nd:N(e.d||''),nx:N(e.x||'')}));run()})
  .catch(()=>{n.textContent='Chưa tải được chỉ mục tìm kiếm. Hãy tải lại trang.'});
 run()})();
'''

SEARCH_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/></svg>'


# ---------------- trang ----------------
def shop_page(L):
    ban = [x for x in L if x['st'] != 'sap']
    sap = [x for x in L if x['st'] == 'sap']
    ngu = [x for x in L if x['line'] == 'Ngũ Hành']
    tabs = [('all', 'Tất cả', len(L)), ('ngu', 'Ngũ Hành', len(ngu)), ('phin', 'Pha phin', sum('phin' in x['brews'] for x in L)),
            ('may', 'Pha máy', sum('espresso' in x['brews'] for x in L)), ('robusta', 'Robusta', sum(x['line'] == 'Robusta' for x in L)),
            ('arabica', 'Arabica', sum(x['line'] == 'Arabica' for x in L)), ('blend', 'Blend', sum(x['line'] == 'Blend' for x in L)),
            ('dac', 'Đặc sản', sum(x['tier'] == 'Specialty' or x['line'] == 'Đặc sản' for x in L)), ('sap', 'Sắp mở bán', len(sap))]
    body = head('Cửa hàng MeDili', 'Cà phê rang mộc <em>từ Di Linh.</em>',
                f'{len(ban)} dòng đang bán (gồm bộ Ngũ Hành túi 250 g) và {len(sap)} dòng sắp mở bán, dành cho pha phin, pha máy và pha thủ công. Chọn gói, thêm vào giỏ rồi gửi đơn. '
                'MeDili xác nhận giá cuối và phí giao trước khi chốt đơn.',
                '<a class="btn main" href="#ke">Xem kệ cà phê</a><a class="btn" href="tim-gu.html">Chưa biết chọn? Tìm gu</a>'
                '<a class="btn" href="mua-hang.html">Mua cho quán: Phòng chọn mua</a>')
    body += f'''
<section class="sh-tool" id="ke" aria-label="Lọc và tìm cà phê">
 <label class="sh-s"><span class="sh-sr">Tìm cà phê</span>{SEARCH_ICON}<input id="sh-q" type="search" placeholder="Tìm: Robusta, honey, phin, blend…" autocomplete="off" enterkeyhint="search"></label>
 <div class="sh-tabs" role="group" aria-label="Nhóm cà phê">{"".join(f'<button type="button" data-f="{k}" aria-pressed="{str(k == "all").lower()}">{t} <i>{c}</i></button>' for k, t, c in tabs)}</div>
 <div class="sh-row">
  <label>Sơ chế <select id="sh-pk"><option value="">Tất cả</option><option value="natural">Natural</option><option value="honey">Honey</option><option value="washed">Washed</option><option value="lot">Theo lô</option></select></label>
  <label>Sắp xếp <select id="sh-sort"><option value="">Gợi ý MeDili</option><option value="pa">Giá thấp đến cao</option><option value="pd">Giá cao đến thấp</option><option value="n">Tên A đến Z</option></select></label>
  <p class="sh-n" id="sh-n" aria-live="polite">{len(L)} dòng cà phê</p>
 </div>
</section>
<div class="sh-grid" id="sh-grid">{"".join(card(x) for x in L)}</div>
<p class="sh-empty" id="sh-empty" hidden>Không có dòng nào khớp. <button type="button" class="lnk" id="sh-reset">Xem tất cả</button></p>
<section class="sh-info" aria-label="Mua hàng tại MeDili">
 <div class="box"><p class="eye">Giá và quy cách</p><p>Giá bán lẻ tính theo kg cà phê rang, chưa gồm 8% VAT và phí giao. Có các gói 250 g, 500 g, 1 kg và 5 kg. Từ 5 kg mỗi tháng có giá sỉ cấp 1, trên 20 kg có giá sỉ cấp 2. Bộ Ngũ Hành bán theo túi 250 g.</p></div>
 <div class="box"><p class="eye">Đặt hàng</p><p>Thêm vào giỏ, điền tên, số điện thoại, địa chỉ rồi gửi đơn qua Google Form, Zalo hoặc email. MeDili liên hệ lại để xác nhận giá cuối, phí giao và thời gian giao.</p></div>
 <div class="box"><p class="eye">Đổi trả</p><p>Đổi trả trong 7 ngày đối với lỗi sản xuất, lỗi đóng gói, hư hỏng khi vận chuyển hoặc giao sai loại. <a class="lnk" href="giao-hang.html">Giao hàng và đổi trả</a></p></div>
</section>
<dialog class="sh-dlg" id="sh-dlg" aria-labelledby="sh-dt"><div class="sh-dw" id="sh-dw"></div></dialog>
'''
    return doc('cua-hang.html', 'Cửa hàng MeDili · Cà phê rang mộc Di Linh',
               'Cửa hàng cà phê rang mộc MeDili: Robusta Di Linh, Arabica Cầu Đất, blend pha máy, Culi, Catimor. '
               'Giá theo kg, giá sỉ từ 5 kg, gửi đơn qua Zalo, Google Form hoặc email.',
               body, css=CSS, js=js_head(L) + SHOP_JS + SHOP_PAGE_JS, wrap_cls='wrap pg')


def _ld(x):
    d = dict(**{'@context': 'https://schema.org', '@type': 'Product'}, name=x['n'], brand={'@type': 'Brand', 'name': 'MeDili'},
             description=f'{x["head"] + ". " if x["head"] else ""}{x["taste"]}. Pha: {", ".join(BREW[b] for b in x["brews"]).lower()}.',
             category='Cà phê rang', url=SITE + x['file'])
    if x['p']:
        v, q, u = (x['p'][0] * 250, 250, 'GRM') if tui(x) else (x['p'][0] * 1000, 1, 'KGM')
        d['offers'] = {'@type': 'Offer', 'priceCurrency': 'VND', 'price': v, 'availability': 'https://schema.org/' + ('OutOfStock' if x['st'] == 'het' else 'InStock'),
                       'url': SITE + x['file'], 'priceSpecification': {'@type': 'UnitPriceSpecification', 'price': v,
                       'priceCurrency': 'VND', 'unitCode': u, 'referenceQuantity': {'@type': 'QuantitativeValue', 'value': q, 'unitCode': u}}}
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False).replace('</', '<\\/') + '</script>'


def product_page(x, L):
    pr = (f'<b>{fm(x["p"][0] * 250)} đ/túi 250 g</b><small>Tương đương {fm(x["p"][0] * 1000)} đ/kg, chưa gồm 8% VAT và phí giao.</small>'
          if x['p'] and tui(x) else
          f'<b>{fm(x["p"][0] * 1000)} đ/kg</b><small>Giá lẻ, chưa gồm 8% VAT và phí giao.'
          + (f' Sỉ 5–20 kg/tháng: {fm(x["p"][1] * 1000)} đ/kg · trên 20 kg/tháng: {fm(x["p"][2] * 1000)} đ/kg.' if x['p'][1] else '') + '</small>'
          if x['p'] else '<b>Liên hệ</b><small>MeDili báo giá khi nhận đơn.</small>')
    badge = badge_html(x)
    bars = ''.join(f'<div class="pd-bar"><span>{BARS[i]}</span><span class="pd-tr"><i style="width:{v}%"></i></span><b>{v}</b></div>' for i, v in enumerate(x['bars']))
    ngu = x['line'] == 'Ngũ Hành'
    tips = '' if ngu else ''.join(f'<li>{esc(t)}</li>' for t in x['tips'])
    story = f'<p class="pd-story">{esc(x["tips"][0])}</p>' if ngu else ''
    brew_links = [f'<a class="btn main" href="cong-thuc-pha.html?sp={x["id"]}">Công thức pha cho dòng này</a>']
    if 'phin' in x['brews']: brew_links.append('<a class="btn" href="quay-pha.html">Công thức phin ở Quầy pha</a>')
    if 'espresso' in x['brews'] or 'v60' in x['brews']: brew_links.append('<a class="btn" href="chiet-xuat.html">Cỗ máy Chiết xuất</a>')
    if 'coldbrew' in x['brews']: brew_links.append('<a class="btn" href="cold-brew.html">Cỗ máy Cold Brew</a>')
    brew_links.append('<a class="btn" href="tim-gu.html">Tìm gu cà phê</a>')
    rel = sorted((y for y in L if y['id'] != x['id']),
                 key=lambda y: (y['line'] != x['line'], y['st'] != 'ban', not (set(y['brews']) & set(x['brews'])), ORDER.index(y['id'])))[:4]
    body = f'''{_ld(x)}
<nav class="pd-bc" aria-label="Vị trí trang"><a href="./">Trang chủ</a>/<a href="cua-hang.html">Cửa hàng</a>/<span aria-current="page">{esc(x['n'])}</span></nav>
<section class="pd-top">
 <div class="pd-fig">{bag(x, 'big')}</div>
 <div class="pd-info">
  {badge}<p class="eye">{esc(x['kline'])}{' · Túi 250 g' if tui(x) else ' · ' + esc(x['line']) if x['line'] not in x['kline'] else ''}</p>
  <h1 class="pd-h">{esc(x['n'])}{f' <span class="pd-en">{esc(x["sub"])}</span>' if ngu else ''}</h1>
  {f'<p class="pd-tag">{esc(x["head"])}</p>' if x['head'] else ''}
  <dl class="pd-dl"><dt>Nguồn gốc</dt><dd>{esc(x['origin'])}</dd><dt>{'Phối trộn' if x['line'] == 'Blend' or ':' in x['proc'] else 'Sơ chế'}</dt><dd>{esc(x['proc'])}</dd><dt>Mức rang</dt><dd>{esc(x['roast'])}</dd>
   <dt>Hương vị</dt><dd>{esc(x['taste'])}</dd><dt>Cách pha</dt><dd>{esc(x['use'])}</dd></dl>
  <div class="pd-pr">{pr}</div>
  {f'<p class="pd-note">{esc(x["note"])}</p>' if x['note'] else ''}
  <div id="pd-buy"><noscript><p>Đặt hàng qua Zalo {PHONE} hoặc email {EMAIL}.</p></noscript></div>
 </div>
</section>
<section class="p-sec">
 <p class="eye">Hồ sơ vị</p>
 <h2 class="p-h2">Uống thế nào, <em>phù hợp với ai.</em></h2>
 <div class="pd-two">
  <div class="box"><div class="pd-bars" aria-label="Hồ sơ vị, thang 100">{bars}</div>
   <p class="note" style="margin-top:10px">{'Chỉ số định hướng, MeDili xác nhận theo từng lô.' if x['st'] == 'sap' else 'Thang điểm 100, so sánh giữa các dòng của MeDili.'}</p></div>
  <div class="box"><p class="eye">Phù hợp với</p><p style="margin:4px 0 0">{esc(x['fit'])}.</p>{f'<ul class="pd-tips">{tips}</ul>' if tips else ''}{story}</div>
 </div>
</section>
<section class="p-sec">
 <p class="eye">Pha cho ngon</p>
 <div class="pd-brew">{"".join(brew_links)}</div>
</section>
<section class="p-sec">
 <p class="eye">Cùng kệ MeDili</p>
 <h2 class="p-h2">Có thể bạn cũng thích.</h2>
 <div class="pd-rel">{"".join(card(y) for y in rel)}</div>
</section>
'''
    js = (js_head(L) + SHOP_JS +
          "document.getElementById('pd-buy').innerHTML=buyHTML(byId[%s],'p');wireBuy(document.getElementById('pd-buy'));\n" % json.dumps(x['id']) +
          REL_JS)
    desc = f'{x["n"]}{"" if "MeDili" in x["n"] else " MeDili"}: {x["head"] + ". " if x["head"] else ""}{x["taste"]}. Pha {", ".join(BREW[b].lower() for b in x["brews"])}. {price_txt(x) if x["p"] else "Giá liên hệ"}.'
    return doc(x['file'], f'{x["n"]} · Cà phê MeDili', desc, body, css=CSS, js=js, wrap_cls='wrap pg')


# nút trên thẻ "Cùng kệ" ở trang sản phẩm: thêm vào giỏ, xem nhanh thì mở trang dòng đó
REL_JS = r'''
document.querySelector('.pd-rel').addEventListener('click',e=>{const a=e.target.closest('[data-add]'),v=e.target.closest('[data-quick]');
 if(a){const x=byId[a.dataset.add];addCart(x.id,x.packs.includes(500)?500:x.packs[0],GR(x)[0],1)}if(v)location.href=byId[v.dataset.quick].file});
'''


def cart_page(L):
    body = head('Giỏ hàng', 'Giỏ cà phê <em>của bạn.</em>',
                'Kiểm tra gói, độ xay, số lượng, chọn cách thanh toán rồi đặt hàng. Chuyển khoản ngay bằng mã QR, hoặc trả tiền mặt khi nhận hàng.')
    body += f'''
<div id="ct-none" class="box ct-empty" hidden><p class="eye">Giỏ đang trống</p><p style="margin:0">Chọn cà phê trong Cửa hàng rồi bấm Thêm vào giỏ.</p>
 <div class="cta" style="margin:0;justify-content:center"><a class="btn main" href="cua-hang.html">Vào Cửa hàng</a><a class="btn" href="tim-gu.html">Tìm gu cà phê</a></div></div>
<div id="ct-has" class="ct-wrap">
 <section aria-label="Các món trong giỏ"><div class="ct-list" id="ct"></div>
  <p class="note" style="margin-top:10px"><a class="lnk" href="cua-hang.html">← Chọn thêm cà phê</a> · <button type="button" class="ct-rm" id="ct-clr">Xóa cả giỏ</button></p></section>
 <aside class="ct-side" aria-label="Gửi đơn">
  <div class="box ct-tot"><p><span>Tổng khối lượng</span><b id="ct-kg">0 kg</b></p><p><span>Mức giá</span><b id="ct-tier">Giá lẻ</b></p>
   <p><span>Tạm tính</span><b id="ct-sum">0 đ</b></p><p><span>VAT 8%</span><b id="ct-vat">0 đ</b></p>
   <p class="big"><span>Cần thanh toán</span><b id="ct-pay">0 đ</b></p><p class="note" id="ct-hint" style="display:block"></p>
   <p class="note" id="ct-ship" style="display:block"></p></div>
  <form class="box p-form" id="ct-f" autocomplete="on">
   <p class="eye">Người nhận</p>
   <label>Họ và tên<input name="ten" autocomplete="name" required></label>
   <label>Số điện thoại hoặc Zalo<input name="sdt" type="tel" inputmode="tel" autocomplete="tel" required></label>
   <label>Địa chỉ giao <small>số nhà, đường, phường, tỉnh</small><input name="dc" autocomplete="street-address" required></label>
   <label>Mua cho<select name="ai"><option>Gia đình</option><option>Quán cà phê</option><option>Nhà hàng, khách sạn</option><option>Văn phòng</option><option>Quà tặng</option></select></label>
   <label>Ghi chú <small>giờ nhận, xuất hóa đơn, đóng gói</small><textarea name="gc" rows="2"></textarea></label>
   <fieldset class="ct-pt"><legend class="eye">Cách thanh toán</legend>
    <label class="ct-op"><input type="radio" name="pt" value="ck" checked><span><b>Chuyển khoản ngay</b><small>Quét mã QR bằng app ngân hàng, MoMo hoặc ZaloPay</small></span></label>
    <label class="ct-op"><input type="radio" name="pt" value="cod"><span><b>Tiền mặt khi nhận hàng</b><small>Trả cho người giao hàng (COD)</small></span></label>
   </fieldset>
   <p class="ct-err" id="ct-err" role="alert" hidden></p>
   <div class="ct-send"><button type="submit" class="btn main" id="ct-go">Đặt hàng và thanh toán</button></div>
   <p class="note">Hoặc gửi đơn qua <a class="lnk" id="ct-zl" href="{ZALO}" target="_blank" rel="noopener">Zalo MeDili</a> hay <a class="lnk" id="ct-em" href="mailto:{EMAIL}">email</a>.</p>
   <p class="note">Thông tin chỉ dùng để giao đơn này, xem <a class="lnk" href="bao-mat.html">Chính sách bảo mật</a>. Hỗ trợ: Zalo {PHONE}.</p>
  </form>
  <details class="box"><summary>Xem nội dung đơn sẽ gửi</summary><pre class="msg" id="ct-msg" data-sel style="margin-top:10px"></pre></details>
 </aside>
</div>
'''
    return doc('gio-hang.html', 'Giỏ hàng · MeDili', 'Giỏ cà phê MeDili: kiểm tra gói, độ xay, số lượng rồi đặt hàng, chuyển khoản bằng mã QR hoặc trả tiền mặt khi nhận hàng.',
               body, css=CSS, js=js_head(L) + SHOP_JS + CART_JS, wrap_cls='wrap pg', contact=False)


def search_page():
    chips = ['Robusta honey', 'Arabica Cầu Đất', 'cold brew', 'giá sỉ', 'phin', 'nhân xanh', 'lên men', 'HORECA']
    body = head('Tìm kiếm', 'Tìm trên <em>MeDili.</em>', 'Tìm dòng cà phê, cách pha, kiến thức và công cụ trên web MeDili. Gõ không dấu cũng được.')
    body += f'''
<section class="sr-box" aria-label="Tìm kiếm">
 <label class="sh-s"><span class="sh-sr">Từ cần tìm</span>{SEARCH_ICON}<input id="sr-q" type="search" placeholder="Ví dụ: robusta honey, cold brew, giá sỉ" autocomplete="off" enterkeyhint="search" autofocus></label>
 <div class="sr-chips" aria-label="Gợi ý">{"".join(f'<button type="button">{c}</button>' for c in chips)}</div>
 <p class="sr-n" id="sr-n" aria-live="polite"></p>
 <ol class="sr-list" id="sr-list"></ol>
</section>
'''
    return doc('tim-kiem.html', 'Tìm kiếm · MeDili', 'Tìm dòng cà phê, cách pha, kiến thức và công cụ trên web MeDili.',
               body, css=CSS, js=SEARCH_JS, wrap_cls='wrap pg', contact=False)


def pages(P):
    L = products(P)
    out = {'cua-hang.html': shop_page(L), 'gio-hang.html': cart_page(L), 'tim-kiem.html': search_page()}
    for x in L:
        out[x['file']] = product_page(x, L)
    return out, L


# ---------------- chỉ mục tìm kiếm, sitemap, robots ----------------
TOOLS = {'chiet-xuat.html', 'cold-brew.html', 'cong-thuc-pha.html', 'trai-chin.html', 'vi-sinh.html', 'tien-chat-huong.html', 'banh-xe-huong.html',
         'phan-biet-ca-phe.html', 'tim-gu.html', 'nhan-xanh.html', 'mua-hang.html', 'gia-ca-phe.html', 'len-men-men-bia.html', 'len-men-trai-cay.html'}
ARTS = {'journal-phin.html', 'journal-tu-qua.html', 'journal-di-linh.html', 'tu-vuon-den-ly.html', 'suc-khoe.html'}
NOINDEX = {'gio-hang.html', 'tim-kiem.html', 'thanh-toan.html'}


def _plain(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = H.unescape(s).replace('\xa0', ' ')
    return unicodedata.normalize('NFC', re.sub(r'\s+', ' ', s)).strip()


def search_index(out_dir):
    items = []
    for f in sorted(os.listdir(out_dir)):
        if not f.endswith('.html') or f in NOINDEX:
            continue
        s = open(os.path.join(out_dir, f), encoding='utf8').read()
        if NOINDEX_META in s:   # trang bài tin đã ẩn hoặc đã gỡ (tintuc.py)
            continue
        t = _plain(re.search(r'<title>(.*?)</title>', s, re.S).group(1))
        m = re.search(r'<meta name="description" content="([^"]*)"', s)
        d = _plain(m.group(1)) if m else ''
        b = s[s.find('<body'):] if '<body' in s else s
        b = re.sub(r'<(script|style|svg|noscript|dialog|select|button)\b.*?</\1>', ' ', b, flags=re.S)
        b = re.sub(r'<div class="mh">.*?class="mh-go"[^>]*>[^<]*</a></div></div>', ' ', b, count=1, flags=re.S)
        b = re.sub(r'<footer class="mf">.*?</footer>', ' ', b, flags=re.S)
        b = re.sub(r'<aside class="mdtb.*?</aside>', ' ', b, flags=re.S)   # thanh thông báo đầu trang (caidat.py)
        b = re.sub(r'<section class="contact".*?</section>', ' ', b, flags=re.S)
        hs = ' · '.join(dict.fromkeys(_plain(h) for h in re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', b, flags=re.S) if _plain(h)))
        x = _plain(b)
        k = 'Sản phẩm' if f.startswith('sp-') else 'Công cụ' if f in TOOLS else 'Bài viết' if f in ARTS else 'Trang'
        items.append(dict(u='./' if f == 'index.html' else f, t=t, k=k, d=d, h=hs[:600], x=x[:3000]))
    return json.dumps(items, ensure_ascii=False, separators=(',', ':'))


def _in_map(d, f):
    return (f.endswith('.html') and f not in ('gio-hang.html', 'thanh-toan.html')
            and NOINDEX_META not in open(os.path.join(d, f), encoding='utf8').read())


def sitemap(out_dir):
    urls = [SITE if f == 'index.html' else SITE + f for f in sorted(os.listdir(out_dir)) if _in_map(out_dir, f)]
    for lang in ('en', 'ja', 'zh'):   # bản tiếng Anh, Nhật, Trung (24/11/2026)
        d = os.path.join(out_dir, lang)
        if os.path.isdir(d):
            urls += [SITE + lang + '/' + ('' if f == 'index.html' else f) for f in sorted(os.listdir(d)) if _in_map(d, f)]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + ''.join(f'<url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n')


ROBOTS = ('User-agent: *\nAllow: /\nDisallow: /quan-tri/\n' + ''.join(f'Disallow: /{l}{f}\n' for f in ('gio-hang.html', 'thanh-toan.html') for l in ('', 'en/', 'ja/', 'zh/'))
          + f'\nSitemap: {SITE}sitemap.xml\n')

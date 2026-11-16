# Trang "Chọn nhân xanh" cho khách sỉ: bảng 13 câu hỏi, máy gợi ý dòng nhân, phiếu gửi MeDili (Google Form, Zalo, in),
# danh mục nhân xanh MeDili và phần giải thích.
# Danh mục dựng theo cấu trúc một bảng báo giá nhân xanh chị Ngân gửi ngày 16/11/2026, nhưng KHÔNG ghi tên, địa chỉ,
# liên hệ, mã hàng hay giá của bên báo giá. Tên dòng và mã hàng là của MeDili.
# Giá nhân xanh: chỉ ghi "Liên hệ để nhận báo giá mỗi ngày." (chị Ngân chọn 16/11/2026); không có con số hay bậc giá nào.
import json
from kit import *
from pages_a import head

FILE = 'nhan-xanh.html'
TITLE = 'Chọn Nhân Xanh MeDili'
DESC = ('Bảng câu hỏi cho khách sỉ mua cà phê nhân xanh: gu, Robusta hay Arabica, Ro Sẻ, Fine Robusta hay cao sản, '
        'độ chín, sơ chế natural, honey, washed, sàng 14 đến 18. MeDili gợi ý dòng nhân và gửi mẫu thử. Liên hệ để nhận báo giá mỗi ngày.')

# ---------- danh mục nhân xanh MeDili ----------
# g: nhóm; sp: R/A; ro: kiểu Robusta; sc: sơ chế; s: sàng; ch: % chín (0 = không cam kết, None = theo lô);
# vu: 25 = vụ 2025–2026, 26 = vụ 2026–2027 (None = theo vụ); gu: độ hợp từng gu 0–1. Không có trường giá nào.
LINES = [
    dict(id='r18bm', g='tm', code='MD-R18-BM', n='Robusta S18 bắn màu', sub='Hàng thương mại sạch, nhân to đều',
         sp='R', ro='cs', sc='tm', s=18, ch=0, vu=25, c='var(--nx1)', use='phin, cà phê sữa, nền blend',
         gu=dict(dam=1, ngot=.3, can=.5, chua=0, trai=0)),
    dict(id='r16bm', g='tm', code='MD-R16-BM', n='Robusta S16 bắn màu', sub='Hàng thương mại, nhân vừa',
         sp='R', ro='cs', sc='tm', s=16, ch=0, vu=25, c='var(--nx1)', use='phin, nền blend, chế biến',
         gu=dict(dam=1, ngot=.3, can=.4, chua=0, trai=0)),
    dict(id='rc18bm', g='tm', code='MD-RC18-BM', n='Culi Robusta S18 bắn màu', sub='Nhân tròn một hạt, tách riêng',
         sp='R', ro='culi', sc='tm', s=18, ch=0, vu=25, c='var(--nx2)', use='phin đậm, bán hạt nguyên',
         gu=dict(dam=1, ngot=.4, can=.4, chua=0, trai=0)),
    dict(id='r18h97', g='fine', code='MD-R18-H97', n='Robusta Honey S18 · chín 97–98 %', sub='Ngọt, tròn vị',
         sp='R', ro='fine', sc='honey', s=18, ch=97, vu=25, c='var(--nx3)', use='phin ngọt hậu, espresso, cold brew',
         gu=dict(dam=.6, ngot=1, can=.8, chua=.1, trai=.5)),
    dict(id='r18h98', g='fine', code='MD-R18-H98', n='Robusta Honey S18 · chín 98 % tuyển', sub='Tuyển kỹ hơn, sạch vị hơn',
         sp='R', ro='fine', sc='honey', s=18, ch=98, vu=25, c='var(--nx3)', use='espresso, Robusta chất lượng cao',
         gu=dict(dam=.5, ngot=1, can=.9, chua=.2, trai=.6)),
    dict(id='r18n99', g='fine', code='MD-R18-N99', n='Robusta Natural S18 · chín 99 %', sub='Ngọt trái chín, thân dày',
         sp='R', ro='fine', sc='natural', s=18, ch=99, vu=25, c='var(--nx4)', use='pha máy, pha phễu, cold brew',
         gu=dict(dam=.5, ngot=.9, can=.6, chua=.2, trai=1)),
    dict(id='rse', g='se', code='MD-RSE-DL', n='Ro Sẻ Di Linh', sub='Giống Robusta cũ, trồng từ hạt',
         sp='R', ro='se', sc=None, s=None, ch=None, vu=None, c='var(--nx5)', use='phin đậm, rang mộc, dòng đặc biệt',
         gu=dict(dam=.9, ngot=.9, can=.5, chua=0, trai=.3)),
    dict(id='a18w99', g='ara', code='MD-A18-W99', n='Arabica Cầu Đất S18 · washed · chín 99 %', sub='Sạch vị, chua sáng, thơm hoa',
         sp='A', ro=None, sc='washed', s=18, ch=99, vu=25, c='var(--nx6)', use='pha phễu, espresso một nguồn',
         gu=dict(dam=0, ngot=.3, can=.6, chua=1, trai=.4)),
    dict(id='a18w98m', g='ara', code='MD-A18-W98-VM', n='Arabica Cầu Đất S18 · washed · chín 98 % · vụ mới', sub='Hương tươi của vụ 2026–2027',
         sp='A', ro=None, sc='washed', s=18, ch=98, vu=26, c='var(--nx6)', use='pha phễu, espresso',
         gu=dict(dam=0, ngot=.3, can=.7, chua=1, trai=.4)),
    dict(id='a18w95', g='ara', code='MD-A18-W95', n='Arabica Cầu Đất S18 · washed · chín 95 %', sub='Cân bằng, dễ phối blend',
         sp='A', ro=None, sc='washed', s=18, ch=95, vu=25, c='var(--nx6)', use='espresso, blend cao cấp',
         gu=dict(dam=.1, ngot=.3, can=.8, chua=.9, trai=.3)),
    dict(id='a14w97', g='ara', code='MD-A14-W97', n='Arabica Cầu Đất S14 · washed · chín 97 %', sub='Nhân nhỏ hơn, độ chín cao',
         sp='A', ro=None, sc='washed', s=14, ch=97, vu=25, c='var(--nx6)', use='blend, pha máy',
         gu=dict(dam=.1, ngot=.3, can=.8, chua=.8, trai=.3)),
    dict(id='a18n89', g='ara', code='MD-A18-N89', n='Arabica S18 · natural · chín 89 %', sub='Phơi khô cả trái, ngọt, thân dày',
         sp='A', ro=None, sc='natural', s=18, ch=89, vu=25, c='var(--nx7)', use='blend, pha máy, cold brew',
         gu=dict(dam=.2, ngot=.6, can=.8, chua=.5, trai=.9)),
]
GRP = {'tm': ('Robusta thương mại', 'bắn màu, hàng phổ biến'),
       'fine': ('Robusta hái chín', 'honey và natural, nền cho Fine Robusta; điểm nếm xác nhận theo lô'),
       'se': ('Ro Sẻ Di Linh', 'tuyển theo vụ, quy cách báo theo lô'),
       'ara': ('Arabica', 'washed và natural')}
SCN = {'tm': 'Thương mại', 'natural': 'Natural', 'honey': 'Honey', 'washed': 'Washed'}

# ---------- 13 câu hỏi ----------
# mỗi phương án: (giá trị, tiêu đề, mô tả, phụ) — phụ: màu ly cho câu gu, cỡ lỗ (mm) cho câu sàng
Q = {
    'muc': ('Bạn mua nhân xanh để làm gì?', 'Mục đích', 'Mỗi kiểu kinh doanh cần một mức chất lượng và giá khác nhau.', [
        ('xr', 'Xưởng rang, thương hiệu rang xay', 'Rang bán lẻ, bán sỉ cà phê hạt.', None),
        ('quan', 'Quán, chuỗi tự rang', 'Rang cho quầy pha của mình.', None),
        ('tm', 'Mua bán lại nhân xanh', 'Phân phối, đóng gói, xuất hàng.', None),
        ('sx', 'Chế biến, sản xuất', 'Hòa tan, cà phê lon, nguyên liệu công nghiệp.', None),
        ('khac', 'Mục đích khác', 'Ghi rõ ở phần ghi chú.', None)]),
    'gu': ('Gu ly cà phê bạn hướng tới', 'Gu', 'Chọn gu gần nhất. Đây là điểm xuất phát, MeDili chỉnh tiếp sau khi bạn thử mẫu.', [
        ('dam', 'Đậm đắng truyền thống', 'Phin, cà phê sữa đá. Thân dày, đắng rõ, ít chua.', '#5A3420'),
        ('ngot', 'Đậm mà ngọt hậu', 'Đắng dịu, hậu ngọt dài, không gắt.', '#8D5A32'),
        ('can', 'Cân bằng cho pha máy', 'Espresso, blend Robusta và Arabica.', '#B8894A'),
        ('chua', 'Chua thanh, thơm hoa', 'Pha phễu, Arabica sáng vị.', '#D9B77E'),
        ('trai', 'Ngọt trái chín, hương lên men', 'Natural, honey: mận chín, nho khô, rượu vang nhẹ.', '#A23B24'),
        ('mau', 'Chưa rõ, muốn thử mẫu', 'MeDili chuẩn bị mẫu vài dòng gần nhu cầu.', 'none')]),
    'loai': ('Robusta hay Arabica?', 'Loại', 'Có thể lấy cả hai để phối blend.', [
        ('R', 'Robusta', 'Đậm, đắng, nhiều caffeine. Giá mềm hơn.', None),
        ('A', 'Arabica', 'Chua thanh, thơm. Giá cao hơn.', None),
        ('RA', 'Cả hai, để phối', 'Robusta làm nền, Arabica làm hương.', None),
        ('x', 'Chưa rõ', 'MeDili gợi ý theo gu.', None)]),
    'ro': ('Robusta loại nào?', 'Robusta', 'Cao sản và Ro Sẻ là giống. Fine Robusta là mức chất lượng. Culi là hình dạng hạt.', [
        ('cs', 'Robusta cao sản', 'Dòng chọn lọc năng suất cao như TR4, TR9, TRS1. Nhân to, đều; đắng rõ, thân vừa.', None),
        ('fine', 'Fine Robusta', 'Hái chín, sơ chế kỹ, nếm đạt từ 80 điểm. Ngọt và sạch vị.', None),
        ('se', 'Ro Sẻ Di Linh', 'Giống Robusta cũ trồng từ hạt. Nhân nhỏ, chắc; đậm, hậu dài. Ít hàng, tuyển theo vụ.', None),
        ('culi', 'Culi Robusta', 'Mỗi trái một nhân tròn. Hạt tròn rang đều hơn.', None),
        ('x', 'Chưa rõ', 'MeDili gợi ý theo gu.', None)]),
    'chin': ('Độ chín khi hái', 'Độ chín', 'Tỉ lệ trái chín trong mẻ hái. Càng cao, ly càng ngọt và sạch vị, giá càng cao.', [
        ('99', 'Chín 99 %', 'Tuyển gần như toàn trái chín.', None),
        ('97', 'Chín 97–98 %', 'Mức của hàng chất lượng cao.', None),
        ('95', 'Chín 95 %', 'Cân bằng chất lượng và giá.', None),
        ('90', 'Khoảng 90 %', 'Hàng khá, giá mềm.', None),
        ('0', 'Không yêu cầu', 'Hàng thương mại, không cam kết tỉ lệ chín.', None)]),
    'sc': ('Phương pháp sơ chế', 'Sơ chế', 'Cách bỏ vỏ và phơi quyết định phần lớn vị ngọt, độ chua và hương.', [
        ('tm', 'Thương mại', 'Phơi khô thông thường, bắn màu. Đậm, đắng, giá tốt.', None),
        ('natural', 'Natural', 'Phơi nguyên trái chín. Ngọt trái chín, thân dày.', None),
        ('honey', 'Honey', 'Xát vỏ, giữ lớp nhớt khi phơi. Ngọt, tròn vị.', None),
        ('washed', 'Washed (ướt)', 'Xát vỏ, lên men, rửa sạch nhớt. Sạch vị, chua sáng.', None),
        ('x', 'Chưa rõ', 'MeDili gợi ý theo gu.', None)]),
    'sang': ('Cỡ sàng', 'Sàng', 'Sàng càng lớn, nhân càng to và đều, rang dễ đều màu.', [
        ('18', 'S18', 'Nhân to, lỗ sàng 7,14 mm.', 7.14),
        ('16', 'S16', 'Nhân vừa, lỗ sàng 6,35 mm.', 6.35),
        ('14', 'S14', 'Nhân nhỏ, lỗ sàng 5,56 mm. Hay gặp ở Arabica.', 5.56),
        ('x', 'Không yêu cầu', 'Theo lô hợp gu nhất.', None)]),
    'vu': ('Vụ mùa', 'Vụ', 'Vụ thu hoạch của lô nhân.', [
        ('26', 'Vụ mới 2026–2027', 'Nhân tươi, hương rõ. Đang vào vụ, có hàng theo đợt.', None),
        ('25', 'Vụ 2025–2026', 'Nhân đã ổn định, rang dễ đoán.', None),
        ('x', 'Không yêu cầu', 'Lô nào hợp gu hơn thì chọn.', None)]),
    'sl': ('Mỗi lần mua bao nhiêu?', 'Mỗi lần mua', '1 bao = 60 kg.', [
        ('mau', 'Mẫu thử', 'Dưới 5 kg.', None),
        ('le', 'Dưới 1 bao', 'Từ 5 đến 59 kg.', None),
        ('bao', '1–16 bao', 'Từ 60 đến 960 kg.', None),
        ('tan', 'Từ 17 bao', 'Khoảng 1 tấn trở lên.', None)]),
    'tan': ('Bao lâu mua một lần?', 'Tần suất', 'Giúp MeDili lên kế hoạch hàng theo vụ.', [
        ('1', 'Một lần', 'Mua thử hoặc theo dự án.', None),
        ('thang', 'Hằng tháng', 'Nhập đều mỗi tháng.', None),
        ('tuan', 'Hằng tuần', 'Rang nhiều, xoay vòng nhanh.', None),
        ('vu', 'Theo hợp đồng cả vụ', 'Chốt lượng và lịch giao cho cả vụ.', None)]),
    'mau': ('Bạn cần mẫu thử?', 'Mẫu thử', 'Nên thử mẫu trước khi chốt đơn lớn.', [
        ('nhan', 'Mẫu nhân xanh', 'Để tự rang thử theo hồ sơ quen.', None),
        ('rang', 'Mẫu đã rang', 'Để nếm ngay, so với lô đang dùng.', None),
        ('ca2', 'Cả hai', 'Nhân để rang, hạt rang để nếm.', None),
        ('khong', 'Không cần', 'Đã quen hàng, cần báo giá.', None)]),
    'giao': ('Nhận hàng thế nào?', 'Nhận hàng', 'Phí giao ghi rõ trong báo giá.', [
        ('hcm', 'Giao tại TP.HCM', 'Giao tận nơi trong thành phố.', None),
        ('tinh', 'Giao đi tỉnh', 'Qua chành xe hoặc đơn vị vận chuyển.', None),
        ('lay', 'Tự đến lấy', 'Hẹn giờ lấy hàng với MeDili.', None)]),
    'ben': ('Bên mua là', 'Bên mua', 'Để MeDili báo đúng thuế và hóa đơn.', [
        ('dn', 'Doanh nghiệp', 'Có mã số thuế công ty.', None),
        ('hkd', 'Hộ kinh doanh', 'Đã đăng ký hộ kinh doanh.', None),
        ('cn', 'Cá nhân', 'Mua không qua đăng ký kinh doanh.', None)]),
}
GROUPS_Q = [
    ('A', 'Bạn và ly cà phê', 'Hai câu để MeDili hiểu bạn rang cho ai và ly cà phê bạn muốn.', ['muc', 'gu']),
    ('B', 'Thông số nhân', 'Sáu câu về loại, giống, độ chín, sơ chế, cỡ hạt và vụ mùa. Giải thích ở cuối trang.',
     ['loai', 'ro', 'chin', 'sc', 'sang', 'vu']),
    ('C', 'Số lượng và giao nhận', 'Số lượng, mẫu thử và cách nhận hàng. 1 bao = 60 kg.', ['sl', 'tan', 'mau', 'giao', 'ben']),
]
QS = [k for _, _, _, ks in GROUPS_Q for k in ks]
assert sorted(QS) == sorted(Q) and len(QS) == 13


ALT = {'muc': 'khac', 'ro': 'x', 'chin': '0', 'sc': 'x'}


def _opt(k, v, t, d, x):
    extra, cls = '', 'op'
    if ALT.get(k) == v:
        cls += ' alt'
    if k == 'gu':
        cls += ' hasx'
        extra = f'<i class="swc{" none" if x == "none" else ""}" style="--c:{x if x != "none" else "transparent"}" aria-hidden="true"></i>'
    elif k == 'sang' and x:
        cls += ' hasx'
        rx, ry = x * .82, x * 1.18   # hạt vẽ theo tỉ lệ cỡ lỗ sàng
        extra = (f'<svg class="sv" viewBox="0 0 24 24" aria-hidden="true"><ellipse cx="12" cy="12" rx="{rx:.2f}" ry="{ry:.2f}"/>'
                 f'<path d="M12 {12 - ry * .7:.2f}V{12 + ry * .7:.2f}"/></svg>')
    return (f'<label class="{cls}"><input type="radio" name="{k}" value="{v}">'
            f'<b>{t}</b><span>{d}</span>{extra}</label>')


def question(no, k):
    t, short, h, opts = Q[k]
    skip = ''
    if k == 'ro':
        skip = ('<p class="skip">Bạn chọn Arabica, câu này bỏ qua.</p>'
                '<p class="qlnk"><a class="lnk" href="phan-biet-ca-phe.html#ca-se">Cách phân biệt Ro Sẻ và cao sản</a></p>')
    return (f'<fieldset class="nxq" id="q-{k}"><legend><span class="qn">{no:02d}</span>{t}</legend>'
            f'<p class="hint">{h}</p><div class="nxo" style="--n:{3 if k == "gu" else len(opts) - (1 if k in ALT else 0)}">' + ''.join(_opt(k, *o) for o in opts) + '</div>' + skip + '</fieldset>')


def form_html():
    out, no = [], 0
    for letter, title, desc, ks in GROUPS_Q:
        qs = []
        for k in ks:
            no += 1
            qs.append(question(no, k))
        out.append(f'<section class="box nxg" data-q="{" ".join(ks)}" aria-labelledby="g-{letter}">'
                   f'<div class="nxgh"><span class="lt" aria-hidden="true">{letter}</span><h3 id="g-{letter}">{title}</h3>'
                   f'<p>{desc}</p><span class="cnt" aria-label="Số câu đã trả lời">0/{len(ks)}</span></div>' + ''.join(qs) + '</section>')
    out.append('''<section class="box nxg" aria-labelledby="g-D">
 <div class="nxgh"><span class="lt" aria-hidden="true">D</span><h3 id="g-D">Liên hệ</h3><p>Để MeDili gửi gợi ý, mẫu và báo giá. Tên và số điện thoại cần cho phiếu gửi online.</p></div>
 <div class="p-form">
  <div class="row2">
   <label for="nx-name">Người liên hệ<input id="nx-name" autocomplete="name" maxlength="80" placeholder="Ví dụ: anh Minh"></label>
   <label for="nx-ph">Số điện thoại hoặc Zalo<input id="nx-ph" type="tel" inputmode="tel" autocomplete="tel" maxlength="20" placeholder="0901234567"></label>
  </div>
  <div class="row2">
   <label for="nx-org">Xưởng, quán hoặc công ty <small>không bắt buộc</small><input id="nx-org" autocomplete="organization" maxlength="100" placeholder="Ví dụ: Xưởng rang Mộc"></label>
   <label for="nx-area">Khu vực nhận hàng <small>không bắt buộc</small><input id="nx-area" maxlength="80" placeholder="Ví dụ: Thủ Đức, TP.HCM"></label>
  </div>
  <label for="nx-note">Ghi chú <small>không bắt buộc</small><textarea id="nx-note" rows="3" maxlength="400" placeholder="Lô đang dùng, máy rang, yêu cầu riêng về độ ẩm, đóng gói..."></textarea></label>
 </div>
</section>''')
    return '<form class="nxf" id="nxf" novalidate>' + ''.join(out) + '</form>'


def _ch(c):
    return 'Theo lô' if c is None else 'Không cam kết' if c == 0 else '97–98 %' if c == 97 else f'{c} %'


def catalog_html():
    rows, g = [], None
    for L in LINES:
        if L['g'] != g:
            g = L['g']
            t, d = GRP[g]
            rows.append(f'<tr class="gr" data-sp="{L["sp"]}"><td colspan="7"><b>{t}</b> · {d}</td></tr>')
        rows.append(
            f'<tr class="ln" id="l-{L["id"]}" data-id="{L["id"]}" data-sp="{L["sp"]}" style="--c:{L["c"]}">'
            f'<td><div class="nxdn"><i aria-hidden="true"></i><b>{L["n"]}</b><small>{L["sub"]}. Hợp {L["use"]}.</small></div></td>'
            f'<td data-l="Sơ chế">{SCN.get(L["sc"], "Theo lô")}</td>'
            f'<td data-l="Sàng">{"S" + str(L["s"]) if L["s"] else "Theo lô"}</td>'
            f'<td data-l="Độ chín">{_ch(L["ch"])}</td>'
            f'<td data-l="Vụ">{"Theo vụ" if L["vu"] is None else "2026–2027" if L["vu"] == 26 else "2025–2026"}</td>'
            f'<td data-l="Mã MeDili" class="code">{L["code"]}</td>'
            f'<td data-l="Quan tâm"><label class="pk"><input type="checkbox" name="pick" value="{L["id"]}"><span>Quan tâm</span></label></td></tr>')
    return ('<div class="tw nxt"><table id="nx-tab"><thead><tr><th scope="col">Dòng nhân</th><th scope="col">Sơ chế</th><th scope="col">Sàng</th>'
            '<th scope="col">Độ chín</th><th scope="col">Vụ</th><th scope="col">Mã MeDili</th><th scope="col"><span class="vh">Đánh dấu</span></th></tr></thead>'
            '<tbody>' + ''.join(rows) + '</tbody></table></div>')


# ---------- hình minh hoạ ----------
def svg_soche():
    def beans(cx, cy):
        return ''.join(f'<ellipse class="Lb" cx="{cx + d}" cy="{cy}" rx="7" ry="17.5"/><path class="Lc" d="M{cx + d} {cy - 12}v24"/>'
                       for d in (-7.6, 7.6))
    cells = [('Thương mại', 'phơi cả trái, hái lẫn', 'all2'), ('Natural', 'phơi cả trái chín', 'all'),
             ('Honey', 'phơi hạt còn nhớt', 'honey'), ('Washed', 'phơi hạt đã rửa', 'washed')]
    out = []
    for i, (t, d, kind) in enumerate(cells):
        cx, cy = 75 + 150 * (i % 2), 54 + 122 * (i // 2)
        s = ''
        if kind in ('all', 'all2'):
            s += f'<ellipse class="Ls" cx="{cx}" cy="{cy}" rx="35" ry="41"/>'
            if kind == 'all2':
                s += f'<path class="Lu" d="M{cx} {cy - 41}A35 41 0 0 0 {cx - 31} {cy + 19}L{cx} {cy}z"/>'
            s += f'<ellipse class="Lp" cx="{cx}" cy="{cy}" rx="30.5" ry="36.5"/>'
        if kind in ('all', 'all2', 'honey'):
            s += f'<ellipse class="Lm" cx="{cx}" cy="{cy}" rx="25.5" ry="31.5"/>'
        s += f'<ellipse class="Lt" cx="{cx}" cy="{cy}" rx="20.5" ry="26.5"/>' + beans(cx, cy)
        s += (f'<text class="t1" x="{cx}" y="{cy + 58}" text-anchor="middle">{t}</text>'
              f'<text class="t2" x="{cx}" y="{cy + 72}" text-anchor="middle">{d}</text>')
        out.append(s)
    leg = [('Ls', 'Vỏ quả', 8), ('Lp', 'Thịt quả', 66), ('Lm', 'Lớp nhớt', 130), ('Lt', 'Vỏ trấu', 197), ('Lb', 'Nhân', 256)]
    lg = ''.join(f'<circle class="{c}" cx="{x + 5}" cy="290" r="5"/><text class="t2" x="{x + 14}" y="294">{t}</text>' for c, t, x in leg)
    return (f'<svg class="fig sc" viewBox="0 0 300 302" role="img" aria-label="Mặt cắt trái cà phê khi đem phơi theo bốn cách sơ chế: '
            f'thương mại và natural còn đủ vỏ quả, thịt quả, lớp nhớt; honey còn lớp nhớt; washed chỉ còn vỏ trấu bọc nhân.">'
            + ''.join(out) + lg + '</svg>')


def svg_sang():
    hs = ''
    for i, (n, mm) in enumerate([(18, 7.14), (16, 6.35), (14, 5.56)]):
        cx = 58 + 92 * i
        hs += (f'<circle class="ho" cx="{cx}" cy="50" r="{mm * 3:.2f}"/>'
               f'<text class="t1" x="{cx}" y="112" text-anchor="middle">Sàng {n}</text>'
               f'<text class="t2" x="{cx}" y="127" text-anchor="middle">{str(mm).replace(".", ",")} mm</text>')
    return ('<svg class="fig sg2" viewBox="0 0 300 134" role="img" aria-label="Ba lỗ sàng vẽ đúng tỉ lệ: sàng 18 lỗ 7,14 mm, sàng 16 lỗ 6,35 mm, sàng 14 lỗ 5,56 mm.">'
            '<rect class="pl" x="6" y="8" width="288" height="84" rx="12"/>' + hs + '</svg>')


def svg_banmau():
    b = ''.join(f'<ellipse class="{"bd" if i == 2 else "Lb"}" cx="{22 + 24 * i}" cy="62" rx="9" ry="6.2"/>' for i in range(5))
    return ('<svg class="fig bm" viewBox="0 0 300 150" role="img" aria-label="Nhân chạy qua camera soi màu; hạt lỗi bị khí nén thổi sang đường loại, hạt đạt đi tiếp.">'
            '<path class="belt" d="M8 70H176"/>' + b +
            '<rect class="cam" x="108" y="10" width="34" height="20" rx="4"/><circle class="lens" cx="125" cy="20" r="5"/>'
            '<path class="beam" d="M117 30L104 56M133 30L146 56"/>'
            '<text class="t2" x="148" y="22">camera soi màu</text>'
            '<path class="jet" d="M170 108v-14M164 96c2 6 10 6 12 0M161 88c3 9 15 9 18 0"/>'
            '<text class="t2" x="160" y="104" text-anchor="end">khí nén</text>'
            '<path class="flow" d="M178 66H226"/><path class="flowd" d="M176 74C190 88 196 112 214 128"/>'
            '<rect class="bin" x="230" y="48" width="62" height="36" rx="8"/><text class="t1" x="261" y="71" text-anchor="middle">Đạt</text>'
            '<rect class="bin bad" x="216" y="116" width="76" height="30" rx="8"/><text class="t1" x="254" y="136" text-anchor="middle">Loại</text>'
            '<ellipse class="bd" cx="200" cy="104" rx="7" ry="5"/>'
            '</svg>')


def svg_robusta():
    def bean(cx, rx, ry, cut, lab, sub):
        c = (f'<path class="Lc2" d="M{cx} {50 - ry * .72}V{50 + ry * .72}"/>' if cut == 'thang' else
             f'<path class="Lc2" d="M{cx - rx * .2} {50 - ry * .7}C{cx + rx * .5} {50 - ry * .2} {cx + rx * .5} {50 + ry * .2} {cx - rx * .2} {50 + ry * .7}"/>')
        return (f'<ellipse class="Lb" cx="{cx}" cy="50" rx="{rx}" ry="{ry}"/>' + c +
                f'<text class="t1" x="{cx}" y="98" text-anchor="middle">{lab}</text><text class="t2" x="{cx}" y="113" text-anchor="middle">{sub}</text>')
    return ('<svg class="fig rb" viewBox="0 0 300 120" role="img" aria-label="Ba dạng nhân Robusta: cao sản to và đều, Ro Sẻ nhỏ và chắc, Culi tròn một nhân.">'
            + bean(55, 17, 25, 'thang', 'Cao sản', 'to, đều') + bean(150, 15, 21.5, 'thang', 'Ro Sẻ', 'nhỏ, chắc')
            + bean(245, 15.5, 20, 'culi', 'Culi', 'tròn, một nhân') + '</svg>')


CSS = r'''
/* Chọn nhân xanh: màu dòng nhân theo bảng màu Thổ (nâu, cam, vàng mật, hồng, đỏ, tím); không xanh lá, không xanh dương, không đen. */
:root{--nx1:#6B4226;--nx2:#C8692A;--nx3:#B8862A;--nx4:#C74B7A;--nx5:var(--accent);--nx6:#7A348E;--nx7:#A0699A;
  --L-skin:#B33A24;--L-unripe:#D7B45E;--L-pulp:#EDBB8C;--L-muc:#C99A3E;--L-par:#F1E2C2;--L-bean:#B39A62;--L-cut:#7A6438;--L-bad:#5E3A24;--L-hole:var(--bg)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--nx1:#B07A50;--nx2:#EE9A5A;--nx3:#D9AE55;--nx4:#E07AA0;--nx6:#A06BCD;--nx7:#CFA0C8;
  --L-skin:#C8553D;--L-unripe:#C9A24E;--L-pulp:#C99A6A;--L-muc:#B8893A;--L-par:#D9C19A;--L-bean:#9E8656;--L-cut:#5E4B2A;--L-bad:#8A4A2A;--L-hole:#5A4232}}
:root[data-theme="dark"]{--nx1:#B07A50;--nx2:#EE9A5A;--nx3:#D9AE55;--nx4:#E07AA0;--nx6:#A06BCD;--nx7:#CFA0C8;
  --L-skin:#C8553D;--L-unripe:#C9A24E;--L-pulp:#C99A6A;--L-muc:#B8893A;--L-par:#D9C19A;--L-bean:#9E8656;--L-cut:#5E4B2A;--L-bad:#8A4A2A;--L-hole:#5A4232}
.vh{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.nxfacts b{font-size:1.45rem;line-height:1.15}
@media (max-width:620px){.nxfacts b{font-size:1.3rem}}
.nxw{display:grid;grid-template-columns:minmax(0,1.7fr) minmax(300px,1fr);gap:18px;align-items:start}
@media (max-width:1020px){.nxw{grid-template-columns:minmax(0,1fr)}}
.nxf{display:grid;gap:16px;min-width:0}
.nxg{display:grid;gap:18px}
.nxgh{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:2px 12px;align-items:center;border-bottom:1px solid var(--rule);padding-bottom:12px}
.nxgh .lt{grid-row:1/3;display:grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--accent);color:var(--on-accent);font:800 1.3rem var(--display)}
.nxgh h3{margin:0;font:800 1.4rem/1.15 var(--display);letter-spacing:.01em}
.nxgh p{margin:0;font-size:.88rem;color:var(--muted);grid-column:2}
.nxgh .cnt{grid-row:1/3;grid-column:3;font:600 .82rem var(--mono);color:var(--muted);border:1px solid var(--rule);border-radius:999px;padding:3px 10px}
.nxgh .cnt.full{background:var(--accent);border-color:var(--accent);color:var(--on-accent)}
.nxq{border:0;margin:0;padding:0;min-width:0;display:grid;gap:6px}
.nxq legend{padding:0;font:700 1.04rem/1.35 var(--body);display:flex;gap:10px;align-items:baseline;margin-bottom:2px}
.nxq legend .qn{font:700 .8rem var(--mono);color:var(--accent)}
.nxq .hint{margin:0 0 4px;font-size:.86rem;color:var(--muted);max-width:76ch}
.nxo{display:grid;grid-template-columns:repeat(var(--n,4),minmax(0,1fr));gap:8px}
@media (max-width:760px){.nxo{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.nxo{grid-template-columns:minmax(0,1fr);gap:6px}.nxg{gap:16px}.nxg.box{padding:14px}.nxs-h,.nxs-b,.nxs-f{padding-left:14px;padding-right:14px}}
label.op{position:relative;display:grid;align-content:start;gap:3px;border:1px solid var(--rule);border-radius:12px;padding:10px 12px 11px 38px;background:var(--bg);cursor:pointer;min-width:0;transition:border-color .15s,background-color .15s}
label.op input{position:absolute;left:13px;top:13px;width:16px;height:16px;margin:0;accent-color:var(--accent)}
label.op b{font:700 .96rem/1.3 var(--body)}
label.op span{font-size:.82rem;line-height:1.42;color:var(--muted)}
label.op:hover{border-color:var(--accent)}
label.op:has(input:checked){border-color:var(--accent);background:var(--tint);box-shadow:inset 0 0 0 1px var(--accent)}
label.op:has(input:focus-visible){outline:3px solid var(--moss);outline-offset:2px}
label.op.hasx{padding-right:40px}
label.op.alt{grid-column:1/-1;display:flex;flex-wrap:wrap;align-items:baseline;gap:0 10px;padding-top:8px;padding-bottom:8px}
label.op.alt input{top:10px}
@media (max-width:560px){label.op{padding:9px 12px 9px 36px}label.op input{top:11px;left:12px}}
.swc{position:absolute;right:11px;top:11px;width:20px;height:20px;border-radius:50%;background:var(--c);box-shadow:0 0 0 2px var(--panel),0 0 0 3px var(--rule)}
.swc.none{border:2px dashed var(--muted);box-shadow:none}
svg.sv{position:absolute;right:9px;top:9px;width:24px;height:24px}
svg.sv ellipse{fill:var(--L-bean);stroke:var(--L-cut);stroke-width:.8}svg.sv path{stroke:var(--L-cut);stroke-width:1.2;stroke-linecap:round}
.nxq[disabled]{opacity:.5}
.nxq .skip{display:none;font-size:.86rem;color:var(--muted);margin:0}
.nxq[disabled] .skip{display:block}
.nxq[disabled] .qlnk{display:none}
.qlnk{margin:2px 0 0;font-size:.88rem}
/* phiếu bên phải */
.nxs{position:sticky;top:70px;display:flex;flex-direction:column;padding:0;max-height:calc(100vh - 86px);overflow:hidden}
.nxs-h{padding:18px 20px 12px;display:grid;gap:10px;border-bottom:1px solid var(--rule)}
.nxs-b{flex:1 1 auto;min-height:0;overflow:auto;overscroll-behavior:contain;scrollbar-width:thin;padding:14px 20px;display:grid;gap:14px;align-content:start}
.nxs-f{padding:12px 20px 14px;border-top:1px solid var(--rule);display:grid;gap:6px}
@media (max-width:1020px){.nxs{position:static;max-height:none;overflow:visible}.nxs-b{overflow:visible}}
.nxs h3{margin:0;font:800 1.4rem/1.15 var(--display)}
.nxs .top{display:flex;justify-content:space-between;align-items:baseline;gap:10px}
.nxs .top b{font:700 .9rem var(--mono);color:var(--accent)}
.nx-meter{display:flex;gap:3px}.nx-meter i{flex:1;height:6px;border-radius:3px;background:var(--tint)}.nx-meter i.on{background:var(--accent)}
.sgl{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.sgl .em{font-size:.88rem;color:var(--muted);border:1px dashed var(--rule);border-radius:12px;padding:12px}
.sg{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 10px;border:1px solid var(--rule);border-left:6px solid var(--c);border-radius:12px;padding:10px 12px;background:var(--bg)}
.sg-k{grid-column:1/-1;font:600 .7rem var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.sg-n{font:700 .95rem/1.3 var(--body);color:var(--ink);text-decoration:none}
.sg-n:hover{color:var(--accent);text-decoration:underline}
.sg-p{font:800 1.35rem/1 var(--display);color:var(--accent);align-self:start;white-space:nowrap}
.sg-c{grid-column:1/-1;display:flex;flex-wrap:wrap;gap:4px 10px;align-items:center;font:500 .78rem var(--mono);color:var(--muted)}
.sg-f{grid-column:1/-1;height:6px;border-radius:3px;background:var(--tint);overflow:hidden}.sg-f i{display:block;height:100%;background:var(--c)}
.nxcs{grid-column:1/-1;display:flex;flex-wrap:wrap;gap:4px}
.nxc{font:600 .74rem/1.3 var(--body);padding:2px 8px;border-radius:999px;border:1px solid var(--rule);color:var(--ink);white-space:nowrap}
.nxc.y{border-color:var(--accent)}.nxc.m{border-style:dashed;color:var(--muted)}.nxc.n{color:var(--muted);background:var(--tint);border-color:transparent}
.tips{list-style:none;margin:0;padding:0;display:grid;gap:6px}
.tips li{position:relative;padding:8px 10px 8px 32px;border-radius:10px;background:var(--tint);font-size:.86rem;line-height:1.45}
.tips li::before{content:'!';position:absolute;left:10px;top:9px;width:15px;height:15px;border-radius:50%;background:var(--accent);color:var(--on-accent);font:800 .68rem/15px var(--body);text-align:center}
.pkl{display:flex;flex-wrap:wrap;gap:4px}
.pkl .nxc{border-left:5px solid var(--c)}
.nxs .cta{margin-top:0;gap:6px}
.nxs .cta .btn{flex:1 1 auto;text-align:center}
.btn.off{opacity:.55;cursor:not-allowed}
.nxs details summary{cursor:pointer;font:600 .86rem var(--body);color:var(--accent)}
.nxs details .msg{margin-top:8px;max-height:260px;overflow:auto}
.nxs .sec{display:grid;gap:6px}
/* danh mục */
.nxfl{display:flex;flex-wrap:wrap;gap:6px}
.nxt table{font-size:.88rem}
.nxt th{font:600 .72rem var(--body);letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.nxt{min-width:0}
.nxt td,.nxt th{padding:10px 12px 10px 0;vertical-align:top}
.nxt td{white-space:normal}.nxt td[data-l="Sàng"],.nxt td[data-l="Vụ"]{white-space:nowrap}
.nxt tr.gr td{font-size:.84rem;color:var(--muted);padding-top:20px;border-bottom:2px solid var(--rule)}
.nxt tr.gr b{font:700 .78rem var(--body);letter-spacing:.07em;text-transform:uppercase;color:var(--accent)}
.nxt .nxdn{display:grid;grid-template-columns:10px minmax(0,1fr);gap:3px 12px;min-width:250px}
.nxt .nxdn i{grid-row:1/3;width:10px;border-radius:5px;background:var(--c)}
.nxt .nxdn b{font:700 .95rem/1.3 var(--body)}
.nxt .nxdn small{color:var(--muted);font-size:.8rem;line-height:1.4}
.nxt td.code{font:600 .8rem var(--mono);white-space:nowrap}
.nxt tr.ln{transition:background-color .3s}
.nxt tr.ln.hl{background:var(--tint)}
.nxt tr.ln.sugd .nxdn b::after{content:'  ★ gợi ý';font:600 .72rem var(--body);color:var(--accent);white-space:nowrap}
.pk{display:inline-flex;align-items:center;gap:6px;font:600 .8rem var(--body);cursor:pointer;white-space:nowrap;border:1px solid var(--rule);border-radius:999px;padding:4px 10px}
.pk:has(input:checked){border-color:var(--accent);background:var(--tint)}
.pk input{width:15px;height:15px;accent-color:var(--accent);margin:0}
@media (max-width:820px){
 .nxt{overflow:visible}
 .nxt thead{display:none}
 .nxt table,.nxt tbody,.nxt tr,.nxt td{display:block;width:100%}
 .nxt tr.ln{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 14px;border:1px solid var(--rule);border-left:6px solid var(--c);border-radius:12px;padding:12px 14px;margin-bottom:8px;background:var(--panel)}
 .nxt tr.ln[hidden],.nxt tr.gr[hidden]{display:none}
 .nxt tr.ln td{border:0;padding:0}
 .nxt tr.ln td:first-child{grid-column:1/-1}
 .nxt .nxdn{min-width:0;grid-template-columns:minmax(0,1fr)}.nxt .nxdn i{display:none}
 .nxt tr.ln td[data-l]::before{content:attr(data-l);display:block;font:600 .66rem var(--body);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin-bottom:1px}
 .nxt tr.ln td[data-l="Quan tâm"]::before{display:none}
 .nxt tr.ln td[data-l="Quan tâm"]{align-self:end}
 .nxt tr.gr td{border:0;padding:14px 0 6px}
}
/* giải thích */
.nxx{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
@media (max-width:1100px){.nxx{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:680px){.nxx{grid-template-columns:minmax(0,1fr)}}
.nxx .box{display:flex;flex-direction:column;gap:6px}
.nxx .box p{margin:0}
.nxx .box .pf img{aspect-ratio:3/2;object-fit:cover}
.nxx .lnks{margin-top:auto;padding-top:4px}
.nxph .pfs{margin:4px 0 0}.nxph .pf img{aspect-ratio:3/2;object-fit:cover}
svg.fig{display:block;width:100%;max-width:340px;height:auto;margin:4px auto 8px}
svg.fig .t1{font:700 12.5px var(--body);fill:var(--ink)}svg.fig .t2{font:500 10.5px var(--body);fill:var(--muted)}
svg.fig .Ls{fill:var(--L-skin)}svg.fig .Lu{fill:var(--L-unripe)}svg.fig .Lp{fill:var(--L-pulp)}svg.fig .Lm{fill:var(--L-muc)}
svg.fig .Lt{fill:var(--L-par)}svg.fig .Lb{fill:var(--L-bean);stroke:var(--L-cut);stroke-width:.8}svg.fig .Lc,svg.fig .Lc2{fill:none;stroke:var(--L-cut);stroke-width:1.4;stroke-linecap:round}
svg.fig .pl{fill:var(--tint);stroke:var(--rule)}svg.fig .ho{fill:var(--L-hole);stroke:var(--muted);stroke-width:1.2}
svg.fig .belt{stroke:var(--muted);stroke-width:3;stroke-linecap:round}svg.fig .bd{fill:var(--L-bad)}
svg.fig .cam{fill:var(--muted)}svg.fig .lens{fill:var(--panel)}svg.fig .beam{stroke:var(--accent);stroke-width:1.2;stroke-dasharray:3 3}
svg.fig .jet{fill:none;stroke:var(--muted);stroke-width:1.6;stroke-linecap:round}
svg.fig .flow,svg.fig .flowd{fill:none;stroke:var(--rule);stroke-width:2.2;stroke-dasharray:5 4}
svg.fig .bin{fill:var(--panel);stroke:var(--muted);stroke-width:1.2}svg.fig .bin.bad{stroke:var(--accent)}
.nxprice{display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px;padding:12px 16px;border-radius:12px;background:var(--tint);border:1px solid var(--rule)}
.nxprice .k{color:var(--accent)}.nxprice b{font:700 1.05rem/1.35 var(--body);color:var(--ink);margin-right:auto}
.gia{margin:0;font:700 1rem/1.4 var(--body);color:var(--accent)}
/* báo giá */
.nxquote{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px 28px;align-items:center;background:var(--tint)}
.nxquote h3{margin:4px 0 6px}.nxquote .cta{margin:0}
@media (max-width:760px){.nxquote{grid-template-columns:minmax(0,1fr)}}
.pr-head{display:none}
#bang-cau-hoi,#danh-muc,#hieu-nhanh,#bao-gia,#nx-sum,.nxt tr.ln{scroll-margin-top:72px}
.nx-bar{display:none}
@media (max-width:1020px){.nx-bar{position:fixed;left:max(10px,env(safe-area-inset-left,0px));right:max(10px,env(safe-area-inset-right,0px));bottom:calc(10px + env(safe-area-inset-bottom,0px));z-index:40;display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:14px;background:var(--ink);color:var(--bg);text-decoration:none;box-shadow:0 8px 24px rgba(46,28,18,.28);font:600 .86rem var(--body)}
 .nx-bar[hidden]{display:none}.nx-bar .c{font:700 .78rem var(--mono);background:var(--accent);color:var(--on-accent);border-radius:999px;padding:3px 8px;white-space:nowrap}
 .nx-bar .t{flex:1;min-width:0;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.nx-bar b{white-space:nowrap}}
@media (prefers-reduced-motion:reduce){label.op,.nxt tr.ln{transition:none}}
/* bản in: phiếu câu hỏi trên giấy A4 */
@media print{
 @page{size:A4;margin:11mm 12mm}
 :root{color-scheme:light}
 body{background:#fff!important;color:#3A2416!important;font-size:11px}
 .mh,.mf,.contact,.p-head,.nxfacts,#danh-muc,#hieu-nhanh,#bao-gia,.nx-bar,.nxs-f,.nxs details,.qlnk,.nx-intro .note,.nx-intro .eye{display:none!important}
 .wrap{padding:0!important;gap:8px!important;max-width:none!important}
 .pr-head{display:flex!important;justify-content:space-between;align-items:center;gap:12px;border-bottom:2px solid #9E3B26;padding-bottom:6px;margin-bottom:6px}
 .pr-head img{width:120px;height:auto}
 .pr-head div{text-align:right;font-size:10px;line-height:1.5}
 .pr-head b{font:800 16px var(--display);letter-spacing:.04em;color:#9E3B26;display:block}
 .nx-intro h2{font-size:18px;margin:0}
 .nxw{display:block}
 .box{border:0!important;padding:0!important;background:none!important}
 .nxg{gap:7px;margin-bottom:8px;break-inside:auto}
 .nxgh{padding-bottom:4px}
 .nxgh .lt{width:22px;height:22px;font-size:12px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
 .nxgh h3{font-size:14px}.nxgh p,.nxgh .cnt{display:none}
 .nxq{break-inside:avoid;gap:2px}
 .nxq legend{font-size:11.5px}
 .nxq .hint{font-size:9.5px;margin:0}
 .nxq[disabled]{opacity:1}.nxq .skip{display:none!important}
 .nxo{display:flex;flex-wrap:wrap;gap:3px 16px}
 label.op{display:inline-flex;align-items:center;gap:5px;border:0;padding:0;background:none!important;box-shadow:none!important}
 label.op input,label.op span,.swc,svg.sv{display:none}
 label.op b{font-weight:500;font-size:11px}
 label.op::before{content:'';display:inline-block;width:10px;height:10px;border:1.3px solid #6B4226;border-radius:2px;font:800 10px/10px var(--body);text-align:center;color:#9E3B26}
 label.op:has(input:checked)::before{content:'✓'}
 label.op:has(input:checked) b{font-weight:800}
 .p-form .row2{grid-template-columns:1fr 1fr}
 .p-form label{font-size:10.5px}
 .p-form input,.p-form textarea{border:0;border-bottom:1px solid #8D7A66;border-radius:0;padding:4px 2px;font-size:11px;background:none}
 .p-form textarea{min-height:44px}
 .p-form input::placeholder,.p-form textarea::placeholder{color:transparent}
 .nxs{display:block;position:static;max-height:none;overflow:visible;border:1px solid #CFC4AE!important;padding:8px 10px!important;margin-top:8px;break-inside:avoid}
 .nxs-h,.nxs-b{padding:0;border:0;overflow:visible;gap:6px}.nxs-b{margin-top:6px}
 .sg,.tips li,.nxc{-webkit-print-color-adjust:exact;print-color-adjust:exact}
 label.op.alt{display:inline-flex;padding:0}
 .nxs.empty,.nxs .nx-meter,.nxs .sec-pk:not(.has){display:none!important}
 .gia{font-size:11px}
 .nxs h3{font-size:14px}.nxs .top b{font-size:11px}
 .sg{padding:5px 8px;gap:2px 8px;border-left-width:4px}.sg-n{font-size:11px}.sg-p{font-size:14px}.sg-k{font-size:8px}.sg-c{font-size:9px}.sg-f{height:4px}
 .nxc{font-size:8.5px;padding:1px 6px}.tips li{font-size:9.5px;padding:4px 8px 4px 24px}.tips li::before{top:4px;left:6px}
 .nxt{display:none}
}
'''

JS = r'''
(()=>{const NB=' ',$=id=>document.getElementById(id),F=$('nxf');if(!F)return;
const escH=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const QS=D.qs,LAB=D.lab,QT=D.qt,LINES=D.lines,byId=Object.fromEntries(LINES.map(l=>[l.id,l]));
const val=n=>{const x=F.querySelector('input[name="'+n+'"]:checked');return x?x.value:null};
function ans(){const a={};QS.forEach(k=>a[k]=val(k));if(a.loai==='A')a.ro=null;return a}
const W={loai:3,ro:3,gu:2,sc:2,chin:2,sang:1.5,vu:1,muc:.8};
const ROM={cs:{r18bm:1,r16bm:1,rc18bm:.6,r18h97:.5,r18h98:.5,r18n99:.5,rse:.2},fine:{r18h97:1,r18h98:1,r18n99:1,rse:.5},se:{rse:1},culi:{rc18bm:1}};
const SCM={tm:{tm:1,natural:.5,honey:.2,washed:0},natural:{natural:1,tm:.4,honey:.5,washed:.1},honey:{honey:1,natural:.5,washed:.5,tm:.1},washed:{washed:1,honey:.5,natural:.1,tm:0}};
const SGM={18:{18:1,16:.4,14:.1},16:{16:1,18:.8,14:.3},14:{14:1,16:.7,18:.6}};
const SCL={tm:'Thương mại',natural:'Natural',honey:'Honey',washed:'Washed'},ROL={cs:'Dòng cao sản',fine:'Dòng hái chín',se:'Ro Sẻ',culi:'Culi'};
const chL=c=>c==null?'Chín theo lô':c===0?'Không cam kết chín':c===97?'Chín 97–98'+NB+'%':'Chín '+c+NB+'%';
function parts(L,a){const P=[];
 if(a.loai&&a.loai!=='x')P.push(['loai',a.loai==='RA'||L.sp===a.loai?1:0,L.sp==='R'?'Robusta':'Arabica']);
 if(a.ro&&a.ro!=='x'){if(L.sp==='R'){const m=(ROM[a.ro]||{})[L.id];P.push(['ro',m===undefined?.1:m,ROL[L.ro]])}else if(a.loai!=='RA')P.push(['ro',0,'Arabica'])}
 if(a.gu&&a.gu!=='mau')P.push(['gu',L.gu[a.gu],'']);
 if(a.sc&&a.sc!=='x')P.push(['sc',L.sc?SCM[a.sc][L.sc]:.6,L.sc?SCL[L.sc]:'Sơ chế theo lô']);
 if(a.chin&&a.chin!=='0'){const r=+a.chin,c=L.ch;P.push(['chin',c==null?.6:c===0?.2:c>=r?1:Math.max(0,1-(r-c)/8),chL(c)])}
 if(a.sang&&a.sang!=='x')P.push(['sang',L.s==null?(a.sang==='18'?.2:.8):SGM[a.sang][L.s],L.s?'S'+L.s:'Sàng theo lô']);
 if(a.vu&&a.vu!=='x')P.push(['vu',L.vu==null?.8:(+a.vu===L.vu?1:(a.vu==='26'?.4:.7)),L.vu==null?'Theo vụ':L.vu===26?'Vụ mới':'Vụ 2025–2026']);
 if(a.muc==='sx')P.push(['muc',L.g==='tm'?1:L.sp==='A'?.5:.4,'']);
 return P}
function rank(a){return LINES.map((L,i)=>{const P=parts(L,a);let s=0,w=0;P.forEach(([k,m])=>{s+=W[k]*m;w+=W[k]});return {L,P,f:w?s/w:0,w,i}}).sort((x,y)=>y.f-x.f||x.i-y.i)}
function sugs(a){const sp=a.loai==='R'||a.loai==='A'?a.loai:((!a.loai||a.loai==='x')&&a.ro&&a.ro!=='x'?'R':null),R=rank(a).filter(x=>!sp||x.L.sp===sp);if(!R.length||!R[0].w)return [];
 if(a.loai==='RA'){const r=R.find(x=>x.L.sp==='R'),A=R.find(x=>x.L.sp==='A'),o=R.find(x=>x!==r&&x!==A);return [[r,'Nền Robusta'],[A,'Hương Arabica'],[o,'Lựa chọn khác']]}
 return R.slice(0,3).map((x,i)=>[x,['Hợp nhất','Lựa chọn hai','Lựa chọn ba'][i]])}
const pct=f=>Math.round(f*100);
const sym=m=>m>=.95?['y','✓','khớp']:m>=.45?['m','≈','gần']:['n','✗','lệch'];
function chipsH(P){return P.map(([k,m,t])=>{const [c,s,w]=sym(m);const lab=k==='gu'?(c==='y'?'Đúng gu':c==='m'?'Gần gu':'Khác gu'):k==='muc'?(c==='y'?'Hợp chế biến':'Cao hơn mức cần'):t;
 return `<span class="nxc ${c}" title="${w}">${s} ${escH(lab)}</span>`}).join('')}
function sgH([x,lab]){const L=x.L;return `<li class="sg" style="--c:${L.c}"><span class="sg-k">${lab}</span><a class="sg-n" href="#l-${L.id}" data-id="${L.id}">${escH(L.n)}</a><b class="sg-p">${pct(x.f)}${NB}%</b>
<span class="sg-c"><span>${L.code}</span></span><span class="sg-f" aria-hidden="true"><i style="width:${pct(x.f)}%"></i></span><span class="nxcs">${chipsH(x.P)}</span></li>`}
function tips(a){const T=[],wantR=a.loai==='R'||((!a.loai||a.loai==='x')&&a.ro&&a.ro!=='x');
 if(a.loai==='A'&&a.gu==='dam')T.push('Gu đậm đắng truyền thống thường cần Robusta. Arabica cho vị chua thanh, thân nhẹ hơn.');
 if(a.loai==='R'&&a.gu==='chua')T.push('Gu chua thanh hợp Arabica hơn. Nếu vẫn chọn Robusta, Honey hoặc Natural chín cao cho vị sạch và ngọt hơn.');
 if(a.ro==='se'&&a.sang==='18')T.push('Ro Sẻ nhân nhỏ, hiếm khi đạt S18. Nên chọn S16 hoặc không yêu cầu sàng.');
 if(a.ro==='fine'&&(a.chin==='0'||a.chin==='90'||a.sc==='tm'))T.push('Fine Robusta cần hái chín từ 95'+NB+'% và sơ chế kỹ: honey, natural hoặc washed.');
 if(a.sc==='tm'&&['99','97','95'].includes(a.chin))T.push('Hàng thương mại không cam kết tỉ lệ chín. Muốn chín từ 95'+NB+'%, chọn Natural hoặc Honey.');
 if(wantR&&a.sc==='washed')T.push('Robusta washed chưa có sẵn trong danh mục. MeDili báo riêng nếu có lô; gần nhất là Robusta Honey.');
 if(a.loai==='A'&&a.sc==='honey')T.push('Arabica honey chưa có sẵn trong danh mục. MeDili báo riêng nếu có lô; gần nhất là Arabica washed chín cao.');
 if(a.loai==='A'&&a.sang==='16')T.push('Arabica trong danh mục có S18 và S14. S16 báo riêng theo lô.');
 if((wantR||a.loai==='RA')&&a.vu==='26')T.push('Robusta vụ 2026–2027 đang thu hoạch. MeDili báo khi có lô mới theo từng đợt.');
 if(a.ro==='culi'&&(a.sang==='16'||a.sang==='14'))T.push('Culi Robusta trong danh mục là cỡ S18.');
 if(a.muc==='sx'&&(['honey','natural','washed'].includes(a.sc)||a.ro==='fine'))T.push('Cho chế biến công nghiệp, hàng thương mại bắn màu thường đủ dùng và tiết kiệm hơn.');
 if(a.loai==='RA')T.push('Phối blend thường bắt đầu từ Robusta'+NB+':'+NB+'Arabica = 9'+NB+':'+NB+'1 đến 5'+NB+':'+NB+'5, rồi chỉnh theo thử nếm.');
 if(a.sl==='tan'&&a.mau==='khong')T.push('Đơn từ 17 bao nên thử mẫu trước khi chốt.');
 if(a.gu==='mau')T.push('MeDili sẽ chuẩn bị mẫu vài dòng gần nhu cầu để bạn nếm và chọn.');
 return T}
const picks=()=>[...document.querySelectorAll('#nx-tab input[name="pick"]:checked')].map(x=>byId[x.value]).filter(Boolean);
const today=()=>{const d=new Date();return String(d.getDate()).padStart(2,'0')+'/'+String(d.getMonth()+1).padStart(2,'0')+'/'+d.getFullYear()};
function msg(a,S,nm,ph){const L=['PHIẾU CHỌN NHÂN XANH · MEDILI','Ngày: '+today()];
 const org=$('nx-org').value.trim();if(org)L.push('Đơn vị: '+org);
 QS.forEach(k=>{if(a[k])L.push(QT[k]+': '+LAB[k][a[k]])});
 const pk=picks();if(pk.length)L.push('Dòng quan tâm: '+pk.map(l=>l.code+' '+l.n).join('; '));
 if(S.length)L.push('MeDili gợi ý: '+S.map(([x])=>x.L.code+' ('+pct(x.f)+'%)').join(', '));
 const ar=$('nx-area').value.trim();if(ar)L.push('Khu vực: '+ar);
 const no=$('nx-note').value.trim();if(no)L.push('Ghi chú: '+no);
 if(nm)L.push('Liên hệ: '+nm+(ph?' | '+ph:''));
 return L.join('\n')}
const KEY='medili-nhanxanh-1',FIELDS=['nx-name','nx-ph','nx-org','nx-area','nx-note'];
function save(){try{const o={pick:picks().map(l=>l.id)};QS.forEach(k=>o[k]=val(k));FIELDS.forEach(id=>o[id]=$(id).value);localStorage.setItem(KEY,JSON.stringify(o))}catch(e){}}
function load(){try{const o=JSON.parse(localStorage.getItem(KEY)||'null');if(!o)return;
 QS.forEach(k=>{if(o[k]){const x=F.querySelector('input[name="'+k+'"][value="'+o[k]+'"]');if(x)x.checked=true}});
 FIELDS.forEach(id=>{if(typeof o[id]==='string')$(id).value=o[id]});
 (o.pick||[]).forEach(id=>{const x=document.querySelector('#nx-tab input[name="pick"][value="'+id+'"]');if(x)x.checked=true})}catch(e){}}
let lastBest='';
function render(){const a=ans();$('q-ro').disabled=a.loai==='A';
 const app=QS.filter(k=>!(k==='ro'&&a.loai==='A')),done=app.filter(k=>a[k]).length;
 $('nx-cnt').textContent=done+' / '+app.length;$('nx-meter').innerHTML=app.map((k,i)=>`<i class="${i<done?'on':''}"></i>`).join('');
 document.querySelectorAll('.nxg[data-q]').forEach(g=>{const ks=g.dataset.q.split(' ').filter(k=>!(k==='ro'&&a.loai==='A')),n=ks.filter(k=>a[k]).length,c=g.querySelector('.cnt');c.textContent=n+'/'+ks.length;c.classList.toggle('full',n===ks.length)});
 const S=sugs(a);
 $('nx-sug').innerHTML=S.length?S.map(sgH).join(''):'<li class="em">Trả lời vài câu ở phần A và B, gợi ý hiện ở đây.</li>';
 const best=S.length?`Hợp nhất lúc này: ${S[0][0].L.n}, khớp ${pct(S[0][0].f)}${NB}%.`:'';if(best!==lastBest){$('nx-best').textContent=best;lastBest=best}
 const ids=S.map(([x])=>x.L.id);document.querySelectorAll('#nx-tab tr.ln').forEach(tr=>tr.classList.toggle('sugd',ids.includes(tr.dataset.id)));
 $('nx-bar-c').textContent=done+'/'+app.length;$('nx-bar-t').textContent=S.length?S[0][0].L.n+' · '+pct(S[0][0].f)+NB+'%':'Trả lời vài câu để xem gợi ý';
 const T=tips(a);$('nx-tips').innerHTML=T.map(t=>`<li>${escH(t)}</li>`).join('');$('nx-tipw').hidden=!T.length;
 const pk=picks();$('nx-sum').classList.toggle('empty',!done&&!pk.length);$('nx-pk').closest('.sec').classList.toggle('has',pk.length>0);$('nx-pk').innerHTML=pk.length?pk.map(l=>`<span class="nxc" style="--c:${l.c}">${escH(l.code)}</span>`).join(''):'<span class="note">Chưa đánh dấu. Bấm ô Quan tâm trong danh mục bên dưới.</span>';
 const nm=$('nx-name').value.trim(),ph=$('nx-ph').value.replace(/[\s.]/g,''),t=msg(a,S,nm,ph);$('nx-msg').textContent=t;
 const g=$('nx-gf');if(nm&&/^(0|\+84)\d{9,10}$/.test(ph)){const q=encodeURIComponent;g.href=FORM+'&'+FN.name+'='+q(nm)+'&'+FN.phone+'='+q(ph)+'&'+FN.txt+'='+q(t);g.classList.remove('off');g.removeAttribute('aria-disabled')}
 else{g.removeAttribute('href');g.classList.add('off');g.setAttribute('aria-disabled','true')}
 save()}
F.addEventListener('input',render);F.addEventListener('change',render);F.addEventListener('submit',e=>e.preventDefault());
$('nx-tab').addEventListener('change',render);
document.querySelectorAll('#nx-fl .pill').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('#nx-fl .pill').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
 const f=b.dataset.f;document.querySelectorAll('#nx-tab tbody tr').forEach(tr=>{tr.hidden=f!=='all'&&tr.dataset.sp!==f})}));
$('nx-sug').addEventListener('click',e=>{const a=e.target.closest('a.sg-n');if(!a)return;const tr=$('l-'+a.dataset.id);if(!tr)return;
 if(tr.hidden)document.querySelector('#nx-fl .pill[data-f="all"]').click();setTimeout(()=>{tr.classList.add('hl');setTimeout(()=>tr.classList.remove('hl'),1800)},60)});
const st=t=>{$('nx-st').textContent=t};
$('nx-gf').addEventListener('click',e=>{if(!$('nx-gf').getAttribute('href')){e.preventDefault();st('Nhập tên và số điện thoại ở mục D để mở phiếu gửi MeDili.');($('nx-name').value.trim()?$('nx-ph'):$('nx-name')).focus()}else st('Phiếu đã mở ở thẻ mới. Bấm Gửi ở cuối phiếu để hoàn tất.')});
$('nx-cp').addEventListener('click',async()=>{try{await navigator.clipboard.writeText($('nx-msg').textContent);st('Đã chép tin nhắn. Mở Zalo MeDili rồi dán vào.')}catch(e){const d=$('nx-msg').closest('details');if(d)d.open=true;const r=document.createRange();r.selectNodeContents($('nx-msg'));const s=getSelection();s.removeAllRanges();s.addRange(r);st('Đã bôi đen tin nhắn, hãy sao chép rồi dán vào Zalo.')}});
$('nx-pr').addEventListener('click',()=>window.print());
$('nx-rs').addEventListener('click',()=>{F.reset();document.querySelectorAll('#nx-tab input[name="pick"]').forEach(x=>x.checked=false);try{localStorage.removeItem(KEY)}catch(e){}render();st('Đã xoá câu trả lời. Muốn in phiếu trống, bấm In phiếu.');$('bang-cau-hoi').scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'})});
load();render();
if('IntersectionObserver' in window){const bar=$('nx-bar'),vis={f:false,s:false};const io=new IntersectionObserver(es=>{es.forEach(e=>{vis[e.target===F?'f':'s']=e.isIntersecting});bar.hidden=!(vis.f&&!vis.s)},{threshold:0});io.observe(F);io.observe($('nx-sum'))}
})();
'''


def page():
    lab = {k: {v: t for v, t, d, x in Q[k][3]} for k in QS}
    qt = {k: Q[k][1] for k in QS}
    lines = [{k: L[k] for k in ('id', 'g', 'code', 'n', 'sp', 'ro', 'sc', 's', 'ch', 'vu', 'c', 'gu')} for L in LINES]
    data = 'const D=' + json.dumps(dict(qs=QS, lab=lab, qt=qt, lines=lines), ensure_ascii=False, separators=(',', ':')) + ';\n'
    data = data.replace(' %', ' %')
    js = f"const FORM={FORM!r},FN={{name:{FORM_F['name']!r},phone:{FORM_F['phone']!r},txt:{FORM_F['txt']!r}}};\n" + data + JS

    body = head('Khách sỉ · Cà phê nhân xanh', 'Chọn nhân xanh <em>đúng gu, đúng lô.</em>',
                'Bảng câu hỏi cho xưởng rang, quán tự rang và đơn vị thương mại. Trả lời 13 câu, khoảng 3 phút: gu, loại cà phê, '
                'độ chín, sơ chế, sàng, vụ và số lượng. MeDili gợi ý dòng nhân hợp nhất và gửi mẫu thử. Liên hệ để nhận báo giá mỗi ngày.',
                '<a class="btn main" href="#bang-cau-hoi">Bắt đầu trả lời</a><a class="btn" href="#danh-muc">Xem danh mục nhân</a>')
    body += '''
<div class="facts nxfacts">
 <div><b>Robusta · Arabica</b><span>Ro Sẻ, Fine Robusta, cao sản, Culi và Arabica Cầu Đất.</span></div>
 <div><b>Natural · Honey · Washed</b><span>cùng hàng thương mại bắn màu.</span></div>
 <div><b>Sàng 14 · 16 · 18</b><span>độ chín từ 89 đến 99 %.</span></div>
 <div><b>Bao 60 kg</b><span>từ mẫu thử dưới 5 kg đến hơn 1 tấn mỗi đơn.</span></div>
</div>
'''
    body += f'''
<div class="pr-head" aria-hidden="true">{logo()}<div><b>PHIẾU CHỌN NHÂN XANH</b>MeDili Café · Zalo {PHONE} · {EMAIL}<br>Liên hệ để nhận báo giá mỗi ngày.<br>Ngày: ........................</div></div>
<section class="p-sec nx-intro" id="bang-cau-hoi">
 <p class="eye">Bảng câu hỏi</p>
 <h2 class="p-h2">Trả lời theo nhu cầu <em>của xưởng bạn.</em></h2>
 <p class="note">Câu nào chưa chắc, cứ bỏ qua hoặc chọn Chưa rõ. Câu trả lời được lưu trên trình duyệt này cho lần ghé sau.</p>
</section>
<div class="nxw">
 {form_html()}
 <aside class="box nxs" id="nx-sum" aria-labelledby="nx-h">
  <div class="nxs-h"><div class="top"><h3 id="nx-h">Phiếu của bạn</h3><b id="nx-cnt">0 / 13</b></div>
   <div class="nx-meter" id="nx-meter" aria-hidden="true"></div><p class="vh" id="nx-best" role="status"></p></div>
  <div class="nxs-b">
   <div class="sec"><p class="k">MeDili gợi ý</p><ol class="sgl" id="nx-sug"></ol></div>
   <div class="sec" id="nx-tipw" hidden><p class="k">Lưu ý</p><ul class="tips" id="nx-tips"></ul></div>
   <div class="sec sec-gia"><p class="k">Giá nhân xanh</p><p class="gia">Liên hệ để nhận báo giá mỗi ngày.</p></div>
   <div class="sec sec-pk"><p class="k">Dòng bạn đánh dấu</p><div class="pkl" id="nx-pk"></div></div>
   <details><summary>Xem tin nhắn sẽ gửi</summary><pre class="msg" id="nx-msg"></pre></details>
  </div>
  <div class="nxs-f">
   <div class="cta acts"><a class="btn main off" id="nx-gf" target="_blank" rel="noopener" aria-disabled="true">Mở phiếu gửi MeDili</a><button class="btn" type="button" id="nx-cp">Chép tin nhắn</button>
    <a class="btn" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo MeDili</a><button class="btn" type="button" id="nx-pr">In phiếu</button><button class="btn ghost" type="button" id="nx-rs">Làm lại</button></div>
   <p class="fstat" id="nx-st" role="status"></p>
  </div>
 </aside>
</div>
<a class="nx-bar" id="nx-bar" href="#nx-sum" hidden><span class="c" id="nx-bar-c">0/13</span><span class="t" id="nx-bar-t">Trả lời vài câu để xem gợi ý</span><b>Xem phiếu ↓</b></a>

<section class="box p-sec" id="danh-muc">
 <p class="eye">Danh mục nhân xanh</p>
 <h2 class="p-h2" style="margin:0">Mười một dòng có sẵn, <em>thêm Ro Sẻ theo vụ.</em></h2>
 <p class="note">Mã MeDili dùng khi đặt hàng. Mỗi báo giá ghi rõ vùng trồng, vụ và quy cách của lô. Bấm Quan tâm để đưa dòng đó vào phiếu.</p>
 <div class="nxprice"><span class="k">Giá nhân xanh</span><b>Liên hệ để nhận báo giá mỗi ngày.</b><a class="btn main small" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo MeDili</a><button class="btn small" type="button" data-copy="{PHONE_RAW}" data-done="Đã sao chép số">Sao chép số {PHONE}</button></div>
 <div class="nxfl" id="nx-fl" role="group" aria-label="Lọc danh mục"><button type="button" class="pill" data-f="all" aria-pressed="true">Tất cả</button><button type="button" class="pill" data-f="R" aria-pressed="false">Robusta</button><button type="button" class="pill" data-f="A" aria-pressed="false">Arabica</button></div>
 {catalog_html()}
</section>

<section class="p-sec" id="hieu-nhanh">
 <p class="eye">Hiểu nhanh trước khi chọn</p>
 <h2 class="p-h2">Sáu điều <em>quyết định lô nhân.</em></h2>
 <div class="nxx">
  <div class="box">{photo('p-hai-chon.jpg', 'Bàn tay nhặt trái cà phê chín', '')}<span class="k">Độ chín</span><h3>Trái chín cho vị ngọt</h3>
   <p>Độ chín là tỉ lệ trái chín trong mẻ hái. Trái chín đủ tích nhiều đường hơn, nên ly ngọt và sạch vị hơn; trái chưa chín làm vị chát, gắt. Hái càng chọn lọc, công càng nhiều, giá càng cao.</p></div>
  <div class="box">{svg_soche()}<span class="k">Sơ chế</span><h3>Phần nào của trái ở lại khi phơi</h3>
   <p>Natural phơi cả trái chín nên ngọt trái chín, thân dày. Honey xát vỏ nhưng giữ lớp nhớt, vị ngọt tròn. Washed rửa sạch nhớt trước khi phơi, vị sạch, chua sáng. Hàng thương mại phơi cả trái, hái lẫn trái chín và chưa chín.</p></div>
  <div class="box">{svg_sang()}<span class="k">Cỡ sàng</span><h3>Số sàng là cỡ lỗ</h3>
   <p>Số sàng tính theo phần 64 của inch: sàng 18 có lỗ 7,14 mm, sàng 16 lỗ 6,35 mm, sàng 14 lỗ 5,56 mm. Nhân S18 là lô mà phần lớn nhân nằm lại trên sàng 18. Nhân to và đều cỡ thì rang chín đều hơn. Hình vẽ đúng tỉ lệ giữa ba lỗ.</p></div>
  <div class="box">{svg_banmau()}<span class="k">Bắn màu</span><h3>Máy loại hạt lỗi từng hạt một</h3>
   <p>Máy tách màu soi từng hạt bằng camera. Gặp hạt đen, nâu, sâu, mốc hay lệch màu, máy thổi khí nén cho hạt rơi sang đường loại. Nhân đều màu thì rang đều hơn, ly ít vị lạ.</p></div>
  <div class="box">{svg_robusta()}<span class="k">Robusta</span><h3>Giống, mức chất lượng, hình dạng</h3>
   <p>Cao sản là các dòng chọn lọc năng suất cao, phần lớn trồng bằng cây ghép, nhân to và đều. Ro Sẻ là giống Robusta cũ của Di Linh, trồng từ hạt, nhân nhỏ và chắc, vị đậm, hậu dài. Fine Robusta là mức chất lượng: hái chín, sơ chế kỹ, nếm đạt từ 80 điểm. Culi là trái chỉ nuôi một nhân tròn.</p>
   <div class="lnks"><a class="lnk" href="phan-biet-ca-phe.html">Cỗ máy Phân biệt cà phê</a></div></div>
  <div class="box">{icon('hen')}<span class="k">Vụ mùa</span><h3>Vụ mới hay vụ trước</h3>
   <p>Nhân vụ mới tươi, hương rõ, nhưng độ ẩm thường còn cao hơn nên cần chỉnh hồ sơ rang. Nhân vụ trước đã ổn định, rang dễ đoán; để lâu, hương dịu dần. Lô nào cũng nên rang thử trước khi chốt số lượng lớn.</p>
   <div class="lnks"><a class="lnk" href="rang.html">Phòng rang</a></div></div>
 </div>
 <div class="nxph">{strip(STRIP_SOCHE)}</div>
</section>

<section class="p-sec" id="bao-gia">
 <p class="eye">Cách MeDili báo giá</p>
 <h2 class="p-h2">Từ phiếu câu hỏi <em>đến bao nhân.</em></h2>
 <ol class="pst two">
  <li><span class="n">{icon('so')}</span><h3><small>Bước 1</small>Gửi phiếu</h3><p>Mở phiếu gửi MeDili, hoặc chép tin nhắn rồi dán vào Zalo. MeDili đọc gu, số lượng và cách nhận hàng của bạn.</p></li>
  <li><span class="n">{icon('nhan')}</span><h3><small>Bước 2</small>Thử mẫu</h3><p>MeDili gửi mẫu nhân hoặc mẫu rang của vài dòng gần gu nhất để bạn rang thử, nếm thử.</p></li>
  <li><span class="n">{icon('can')}</span><h3><small>Bước 3</small>Nhận báo giá mỗi ngày</h3><p>Báo giá ghi rõ lô, vùng trồng, vụ, quy cách, thuế và phí giao.</p></li>
  <li><span class="n">{icon('xe')}</span><h3><small>Bước 4</small>Chốt đơn và giao</h3><p>Đóng bao 60 kg; đơn dưới 1 bao đóng túi theo số kg. Giao tại TP.HCM, đi tỉnh, hoặc hẹn đến lấy.</p></li>
 </ol>
 <div class="box nxquote"><div><p class="eye">Giá nhân xanh</p><h3>Liên hệ để nhận báo giá mỗi ngày.</h3><p class="note">Nhắn Zalo hoặc gửi phiếu câu hỏi ở trên, MeDili gửi báo giá theo lô và số lượng bạn cần.</p></div><div class="cta"><a class="btn main" href="{ZALO}" target="_blank" rel="noopener">Nhắn Zalo MeDili</a><a class="btn" href="#bang-cau-hoi">Gửi phiếu câu hỏi</a></div></div>
</section>
'''
    assert '</script' not in js.lower()
    return doc(FILE, TITLE, DESC, body, css=CSS, js=js, wrap_cls='wrap pg')

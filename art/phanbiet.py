# Cỗ máy Phân biệt cà phê: Robusta Cà Sẻ Di Linh, Robusta cao sản, Arabica, Catimor, Moka, Culi, Liberica, Excelsa.
# Định tính (vườn, trái, hình nhân, nếm), định lượng (sàng, cân 100 nhân, phòng thí nghiệm) và một bộ phân loại Bayes đơn giản để minh họa.
# Màu theo phong thủy: không xanh lá, không xanh dương, không đen.
import json
from iso import *

FILE = 'phan-biet-ca-phe.html'
TITLE = 'Cỗ máy Phân biệt cà phê MeDili'
DESC = ('Phân biệt Robusta Cà Sẻ Di Linh với Robusta cao sản, Arabica, Catimor, Moka, Culi, Liberica và Excelsa: xem vườn, soi nhân, '
        'sàng, cân 100 nhân, phòng thí nghiệm và nếm. Định tính, định lượng, cảm quan. Mô hình tương tác của MeDili, có nguồn.')

# ---------- tám mẫu ----------
# q: [trung bình, độ lệch] cho bộ phân loại; Lmm: chiều dài nhân ước theo khối lượng 100 nhân và dáng hạt (Liberica theo đo đạc).
SAMPLES = [
    dict(k='se', n='Cà Sẻ Di Linh', s='Cà Sẻ', sp='Robusta, giống cũ', grp='R', c='var(--k1)',
         prop='Thực sinh: trồng từ hạt qua nhiều thế hệ, quần thể không đồng đều',
         tree='Mỗi cây một dáng, lá và trái khác nhau; tán thường gọn; gốc không có vết ghép.', tc='cây thực sinh',
         cher='Trái nhỏ, chùm dày; màu và độ chín khác nhau giữa các cây.', cc='nhỏ, chùm dày',
         bean='Nhỏ, chắc, lưng dày, dáng tròn ngắn.', cutT='Thẳng',
         alt='Khoảng 900–1.000 m, cao nguyên Di Linh', har='Tháng 11 tới đầu tháng 1, hái nhiều lượt',
         notes='Đậm, đắng rõ, hậu dài, thân dày; socola đen, ca cao', cupS='đắng đậm, hậu dài',
         scale='Fine Robusta', prof=[6, 3, 5, 8, 8, 8], dist=[8, 54, 33, 5],
         q=dict(caf=[2.4, .25], lip=[10, 1], suc=[4, .8], w=[15, 1.6], s16=[62, 9], cu=[4, 2]),
         sh=dict(a=1.2, asym=.04, hook=0, pt=0, cut='t'), Lmm=8.6, omc='Cao, như mọi Robusta', omcS='cao',
         yld='Ước 2–3 tấn nhân/ha', conf='Robusta cao sản trồng ở vùng khó (nhân cũng nhỏ), hoặc lô đã sàng lấy nhân nhỏ.',
         lo=[-20, -20], tv=dict(t=3, h=5.6, cr=4.6, n=14, lr=14, ir=1, seed=3),
         cv=dict(n=14, r=4.2, cols=['#B33A24', '#C8553D', '#D9782E', '#8E2418'], cl=3)),
    dict(k='cs', n='Robusta cao sản', s='Cao sản', sp='Robusta, dòng chọn lọc', grp='R', c='var(--k2)',
         prop='Ghép chồi, giâm cành: TR4, TR9, TR11, TR14, TR15; riêng TRS1 trồng bằng hạt lai',
         tree='Vườn đồng đều như đúc, gốc có vết ghép; phải trồng xen nhiều dòng vì Robusta cần thụ phấn chéo. TR9 thấp, gọn, lá non màu đồng sẫm.', tc='cây ghép đồng đều',
         cher='Trái to, đều trong cùng một dòng.', cc='to, đều',
         bean='To, đều, dáng tròn hơi dài.', cutT='Thẳng',
         alt='Tùy vùng: Đắk Lắk, Gia Lai, Lâm Đồng; TR9 phù hợp ở khoảng 500–800 m', har='Tùy dòng; TR9, TR14, TR15 chín muộn',
         notes='Đắng rõ, gỗ, ngũ cốc rang; vị nhẹ hơn Cà Sẻ', cupS='đắng rõ, thân vừa',
         scale='Fine Robusta', prof=[5, 2.5, 4, 7.5, 6, 5], dist=[45, 43, 11, 1],
         q=dict(caf=[2.1, .25], lip=[10, 1], suc=[4, .8], w=[21, 3], s16=[88, 6], cu=[4, 2]),
         sh=dict(a=1.28, asym=.04, hook=0, pt=0, cut='t'), Lmm=10.1, omc='Cao, như mọi Robusta', omcS='cao',
         yld='3,7–7,3 tấn nhân/ha trong thí nghiệm', conf='Cà Sẻ, khi cao sản trồng ở vùng khó làm nhân nhỏ đi: TR4 ở Gia Lai chỉ 15,3 g mỗi 100 nhân.',
         lo=[0, -20], tv=dict(t=1, h=5, cr=4, n=10, lr=15, ir=0, gr=1, seed=7),
         cv=dict(n=11, r=5.6, cols=['#8E2418', '#9E2A1C'], cl=3)),
    dict(k='ara', n='Arabica (Typica, Bourbon)', s='Arabica', sp='Arabica, giống cổ', grp='A', c='var(--k3)',
         prop='Trồng từ hạt; Arabica tự thụ phấn nên giống khá ổn định',
         tree='Typica cao, cành ngang, lá non màu đồng; lá nhỏ, bóng hơn Robusta.', tc='cây cao, lá nhỏ',
         cher='Trái đỏ, cỡ vừa; mỗi đốt ít trái hơn Robusta.', cc='vừa, thưa',
         bean='Dẹt, thuôn dài, mặt phẳng rộng.', cutT='Cong chữ S',
         alt='Vùng cao; Cầu Đất khoảng 1.500 m trở lên', har='Tùy vùng',
         notes='Hoa, cam chanh, trái cây; chua thanh, ngọt', cupS='chua thanh, thơm',
         scale='SCA', prof=[8, 7, 7, 3, 5, 6], dist=[30, 50, 18, 2],
         q=dict(caf=[1.2, .15], lip=[16, 1], suc=[8, 1], w=[18, 1.6], s16=[80, 7], cu=[4, 2]),
         sh=dict(a=1.45, asym=.06, hook=0, pt=0, cut='s'), Lmm=10.4, omc='Chỉ ở mức vết', omcS='vết',
         yld='Thấp; Typica Cầu Đất chỉ khoảng 2,5–3 tấn mỗi năm cả vùng', conf='Catimor: cùng loài, hình nhân gần như giống nhau.',
         lo=[14, -15], tv=dict(t=1, h=7.4, cr=3.8, n=10, lr=14, tier=1, br=1, seed=11),
         cv=dict(n=7, r=5.8, cols=['#B33A24', '#C0432A'], cl=2)),
    dict(k='cat', n='Catimor', s='Catimor', sp='Arabica, giống lai', grp='A', c='var(--k4)',
         prop='Lai Timor Hybrid với Caturra, tạo ở Bồ Đào Nha năm 1959',
         tree='Cây thấp, lóng đốt ngắn, tán gọn; kháng gỉ sắt nhờ gen Robusta trong Timor Hybrid.', tc='cây thấp, lóng ngắn',
         cher='Trái đỏ, cỡ vừa, sai trái.', cc='vừa, sai',
         bean='Dẹt, thuôn, cỡ vừa đến to.', cutT='Cong chữ S',
         alt='Sơn La, Lâm Đồng, Quảng Trị…', har='Tùy vùng',
         notes='Hạt, thảo mộc, anh đào, quả mọng; chua vừa', cupS='chua vừa, thảo mộc',
         scale='SCA', prof=[6, 6, 5, 4, 5, 5], dist=[25, 53, 20, 2],
         q=dict(caf=[1.3, .15], lip=[15, 1.2], suc=[7, 1], w=[17, 1.6], s16=[78, 8], cu=[4, 2]),
         sh=dict(a=1.42, asym=.06, hook=0, pt=0, cut='s'), Lmm=10.0, omc='Chỉ ở mức vết', omcS='vết',
         yld='1,67 tấn nhân/ha, đối chứng trong thí nghiệm giống', conf='Arabica giống cổ: hình nhân gần như giống nhau.',
         lo=[-34, -12], tv=dict(t=1, h=3.6, cr=3.5, n=14, lr=11, seed=13),
         cv=dict(n=9, r=5.4, cols=['#B33A24', '#C0432A'], cl=3)),
    dict(k='mok', n='Moka Cầu Đất', s='Moka', sp='Arabica, nhóm Bourbon', grp='A', c='var(--k5)',
         prop='Trồng từ hạt; thường được mô tả là dạng lùn của Bourbon',
         tree='Cây nhỏ, ít lá, nhìn gầy; dạng Mokka gốc mọc rậm như hàng rào.', tc='cây lùn, nhỏ',
         cher='Trái nhỏ, tròn.', cc='nhỏ, tròn',
         bean='Rất nhỏ, tròn như hạt đậu.', cutT='Cong, ngắn',
         alt='Khoảng 1.500–1.600 m, Cầu Đất', har='Tùy vụ',
         notes='Vỏ quýt, hạnh nhân, dâu, vani; có tài liệu mô tả socola, trái khô, gia vị', cupS='thơm nồng, chua thanh',
         scale='SCA', prof=[9, 7, 8, 3, 6, 7], dist=[3, 27, 55, 15],
         q=dict(caf=[.9, .25], lip=[16, 1], suc=[8, 1], w=[11.5, 1.5], s16=[30, 10], cu=[6, 3]),
         sh=dict(a=1.12, asym=.03, hook=0, pt=0, cut='s'), Lmm=7.5, omc='Chỉ ở mức vết', omcS='vết',
         yld='Khoảng 1–2 kg mỗi cây mỗi năm', conf='Arabica thường được gọi chung là “Moka” cho dễ bán.',
         lo=[0, -20], tv=dict(t=1, h=3.2, cr=2.8, n=7, lr=9, ir=.5, seed=17),
         cv=dict(n=7, r=4.4, cols=['#B33A24', '#9E2A1C'], cl=2)),
    dict(k='culi', n='Culi (hạt tròn)', s='Culi', sp='Hình dạng hạt, có ở mọi giống', grp='R', c='var(--k6)',
         prop='Không phải giống: trái chỉ nuôi một nhân thay vì hai',
         tree='Theo cây mẹ; vườn nào cũng có.', tc='theo cây mẹ',
         cher='Nhìn ngoài như trái thường.', cc='như thường',
         bean='Tròn đều, không có mặt phẳng.', cutT='Một đường dọc thân tròn',
         alt='Theo vườn', har='Theo vườn',
         notes='Theo cây mẹ; hạt tròn rang đều hơn, vị có thể tròn hơn nhưng không bảo đảm', cupS='theo cây mẹ',
         scale='Theo loài của cây mẹ', prof=[6, 3, 5, 7.5, 7.5, 7], dist=[10, 35, 45, 10],
         q=dict(caf=[2.3, .3], lip=[10, 1], suc=[4, .8], w=[15.5, 2], s16=[45, 15], cu=[92, 5]),
         sh=dict(a=1.32, asym=0, hook=0, pt=0, cut='p'), Lmm=8.0, omc='Theo loài của cây mẹ', omcS='theo cây mẹ',
         yld='Khoảng 4–5% sản lượng một vụ', conf='Cà Sẻ: Sẻ là giống, Culi là hình hạt. Có Culi Sẻ, Culi cao sản, Culi Arabica.',
         lo=[26, 24], tv=dict(t=2, h=5.2, cr=4.2, n=12, lr=13, ir=.6, seed=19),
         cv=dict(n=11, r=4.6, cols=['#B33A24', '#C8553D'], cl=3)),
    dict(k='lib', n='Liberica (cà phê mít)', s='Liberica', sp='Coffea liberica', grp='L', c='var(--k7)',
         prop='Loài riêng; cây gỗ thật, rễ cọc sâu',
         tree='Cây gỗ lớn, lá to, dày, rễ cọc sâu.', tc='cây gỗ cao, lá to',
         cher='Trái to, vỏ dày, nhiều thịt quả: thịt và nhân khoảng 60 : 40.', cc='to, vỏ dày',
         bean='To nhất trong các loài: dài khoảng 11,5 mm, dáng lệch, đầu nhọn có móc.', cutT='Nhăn, lệch',
         alt='Kon Tum, Quảng Trị, Lâm Đồng; khoảng 800 m', har='Theo vùng',
         notes='Mít chín, xoài, vải, chanh dây khi chế biến tốt; gỗ, da thuộc khi chế biến kém', cupS='mít chín, nhiệt đới',
         scale='Chưa có thang riêng phổ biến', prof=[7.5, 3, 6.5, 5, 7, 6], dist=[60, 33, 6, 1],
         q=dict(caf=[1.2, .2], lip=[12, 2.5], suc=[5.5, 1.5], w=[22, 2], s16=[93, 4], cu=[3, 2]),
         sh=dict(a=1.52, asym=.32, hook=1, pt=.5, cut='r'), Lmm=11.5, omc='Chưa rõ', omcS='?',
         yld='Chưa có số tin cậy ở Việt Nam', conf='Excelsa: cùng bị gọi chung là cà phê mít.',
         lo=[0, -16], tv=dict(t=1, h=9.5, cr=5.2, n=10, lr=20, tw=.6, seed=23),
         cv=dict(n=4, r=8.5, cols=['#C8553D', '#D9782E', '#B33A24'], cl=2)),
    dict(k='exc', n='Excelsa (Chari)', s='Excelsa', sp='Coffea dewevrei', grp='L', c='var(--k8)',
         prop='Từng được xếp là một thứ của Liberica; nghiên cứu gen năm 2025 tách thành loài riêng',
         tree='Cây cao tới khoảng 15 m, lá dày dai, rễ sâu; chịu hạn, ít sâu bệnh.', tc='cây gỗ cao',
         cher='Trái và nhân nhỏ hơn Liberica, vỏ trấu mỏng hơn.', cc='vừa, đỏ sẫm',
         bean='Cỡ vừa, dáng giọt nước hơi lệch.', cutT='Hơi nhăn, lệch',
         alt='Có trồng ở Việt Nam, Ấn Độ, Indonesia', har='Theo vùng',
         notes='Chua kiểu trái cây, trái sẫm, socola, gia vị, hạt phỉ; ít đắng', cupS='chua trái cây, ít đắng',
         scale='Chưa có thang riêng phổ biến', prof=[7, 7, 6, 3, 5, 6], dist=[25, 50, 22, 3],
         q=dict(caf=[1.2, .25], lip=[12, 2.5], suc=[5.5, 1.5], w=[17.5, 2], s16=[75, 10], cu=[3, 2]),
         sh=dict(a=1.36, asym=.22, hook=0, pt=.45, cut='r'), Lmm=9.9, omc='Chưa rõ', omcS='?',
         yld='Cao hơn Liberica khi điều kiện tốt', conf='Liberica: cùng bị gọi chung là cà phê mít.',
         lo=[22, 26], tv=dict(t=1, h=8.6, cr=4.8, n=10, lr=18, tw=.5, seed=29),
         cv=dict(n=6, r=6.6, cols=['#A8321F', '#B33A24'], cl=2)),
]
SM = {s['k']: s for s in SAMPLES}

# ---------- máy nhận diện bằng giác quan: trọng số do MeDili đặt từ mô tả trong tài liệu ----------
def _o(i, t, se, cs, ara, cat, mok, culi, lib, exc):
    return dict(id=i, t=t, w=dict(se=se, cs=cs, ara=ara, cat=cat, mok=mok, culi=culi, lib=lib, exc=exc))


QZ = [
    dict(id='hinh', n='Hình nhân xanh', h='Lật mặt phẳng lên, nhìn dáng nhân.', o=[
        _o('tron', 'Tròn đều, không có mặt phẳng', .05, .05, .03, .03, .25, .95, .02, .05),
        _o('gu', 'Dẹt một mặt, tròn ngắn, lưng dày', .9, .85, .1, .15, .2, .1, .05, .2),
        _o('thuon', 'Dẹt, thuôn dài, mặt phẳng rộng', .05, .15, .9, .85, .1, .05, .15, .3),
        _o('dau', 'Rất nhỏ, tròn như hạt đậu', .15, .03, .03, .05, .9, .2, .01, .05),
        _o('moc', 'Rất to, lệch, đầu nhọn có móc', .01, .03, .02, .02, .01, .02, .9, .25),
        _o('giot', 'Cỡ vừa, dáng giọt nước hơi lệch', .05, .05, .1, .1, .05, .05, .3, .8)]),
    dict(id='ranh', n='Rãnh giữa', h='Đường rãnh trên mặt phẳng của nhân.', o=[
        _o('t', 'Thẳng, gọn', .9, .9, .1, .15, .25, .1, .1, .2),
        _o('s', 'Cong chữ S', .1, .1, .9, .85, .7, .1, .15, .3),
        _o('r', 'Nhăn, lệch, không đều', .05, .05, .05, .05, .05, .05, .85, .7),
        _o('p', 'Không có mặt phẳng', .02, .02, .02, .02, .1, .95, .02, .02)]),
    dict(id='co', n='Cỡ nhân', h='Lỗ sàng 16 là 6,30 mm, sàng 13 là 5,00 mm.', o=[
        _o('nho', 'Nhỏ: lọt sàng 16, nằm trên sàng 13', .55, .12, .15, .2, .85, .5, .02, .15),
        _o('vua', 'Vừa: nằm trên sàng 16', .4, .45, .5, .55, .15, .4, .1, .45),
        _o('to', 'To: nằm trên sàng 18', .08, .45, .35, .25, .02, .15, .4, .35),
        _o('rto', 'Rất to: dài từ 11 mm', .01, .03, .03, .02, .01, .02, .85, .15)]),
    dict(id='mui', n='Mùi bột vừa xay', h='Ngửi khô ngay sau khi xay.', o=[
        _o('soco', 'Socola đen, ca cao, hạt rang', .85, .55, .3, .35, .45, .7, .2, .3),
        _o('hoa', 'Hoa, cam chanh, trái cây tươi', .15, .08, .85, .55, .8, .15, .2, .3),
        _o('mit', 'Mít chín, trái nhiệt đới, gỗ', .05, .05, .05, .05, .05, .05, .9, .3),
        _o('sam', 'Trái sẫm, chua lên men, gia vị', .1, .08, .25, .25, .35, .1, .3, .85),
        _o('coc', 'Ngũ cốc, đất, gỗ khô', .3, .7, .05, .2, .03, .45, .15, .1),
        _o('tm', 'Thảo mộc, lá, hăng nhẹ', .1, .25, .1, .6, .05, .15, .1, .15)]),
    dict(id='chua', n='Độ chua', h='Nếm khi ly nguội còn khoảng 60 °C.', o=[
        _o('khong', 'Gần như không', .3, .7, .03, .05, .05, .5, .5, .05),
        _o('thap', 'Thấp, chua thanh nhẹ', .7, .3, .2, .35, .3, .5, .45, .25),
        _o('ro', 'Rõ, sáng', .1, .05, .9, .7, .85, .1, .1, .45),
        _o('chat', 'Chua chát kiểu trái cây sẫm', .05, .05, .2, .35, .2, .05, .15, .85)]),
    dict(id='dang', n='Vị đắng', h='', o=[
        _o('rr', 'Rất rõ, kéo dài', .75, .7, .03, .1, .03, .65, .2, .05),
        _o('ro', 'Rõ, vừa phải', .3, .35, .3, .55, .3, .4, .65, .4),
        _o('nhe', 'Nhẹ', .03, .03, .85, .5, .85, .05, .3, .75)]),
    dict(id='than', n='Thể chất', h='Cảm giác dày, sánh trong miệng.', o=[
        _o('day', 'Dày, sánh', .8, .4, .2, .2, .5, .65, .7, .2),
        _o('vua', 'Vừa', .3, .6, .65, .65, .55, .45, .4, .55),
        _o('mong', 'Nhẹ, mỏng', .05, .15, .45, .4, .2, .1, .1, .5)]),
    dict(id='hau', n='Hậu vị', h='Vị còn lại sau khi nuốt.', o=[
        _o('dai', 'Dài, đậm', .8, .3, .55, .3, .7, .6, .55, .45),
        _o('vua', 'Vừa', .3, .5, .55, .55, .4, .45, .5, .55),
        _o('ngan', 'Ngắn, khô, chát', .1, .45, .1, .35, .05, .2, .2, .2)]),
    dict(id='cay', n='Cây ngoài vườn', h='Nếu xem được vườn hay ảnh vườn.', o=[
        _o('thuc', 'Thực sinh lâu năm, mỗi cây một dáng', .9, .1, .15, .05, .1, .5, .1, .1),
        _o('ghep', 'Cây ghép đồng đều, trồng xen nhiều dòng', .08, .9, .03, .05, .02, .5, .02, .02),
        _o('thap', 'Cây bụi thấp, lóng ngắn, lá nhỏ bóng', .03, .05, .3, .9, .3, .15, .02, .02),
        _o('dong', 'Cây cao, cành ngang, lá non màu đồng', .03, .03, .8, .05, .1, .05, .05, .05),
        _o('lun', 'Cây nhỏ, lùn, nhân rất nhỏ', .02, .02, .05, .1, .9, .05, .02, .02),
        _o('go', 'Cây gỗ cao trên 5 m, lá to dày', .03, .02, .02, .01, .01, .05, .9, .9)]),
]
PRE = dict(
    se=dict(hinh='gu', ranh='t', co='nho', mui='soco', chua='thap', dang='rr', than='day', hau='dai', cay='thuc'),
    cs=dict(hinh='gu', ranh='t', co='to', mui='coc', chua='khong', dang='rr', than='vua', hau='ngan', cay='ghep'),
    ara=dict(hinh='thuon', ranh='s', co='vua', mui='hoa', chua='ro', dang='nhe', than='vua', hau='dai', cay='dong'),
    cat=dict(hinh='thuon', ranh='s', co='vua', mui='tm', chua='ro', dang='ro', than='vua', hau='vua', cay='thap'),
    mok=dict(hinh='dau', ranh='s', co='nho', mui='hoa', chua='ro', dang='nhe', than='vua', hau='dai', cay='lun'),
    culi=dict(hinh='tron', ranh='p', co='nho', mui='soco', chua='thap', dang='rr', than='day', hau='dai'),
    lib=dict(hinh='moc', ranh='r', co='rto', mui='mit', chua='thap', dang='ro', than='day', hau='vua', cay='go'),
    exc=dict(hinh='giot', ranh='r', co='vua', mui='sam', chua='chat', dang='nhe', than='vua', hau='vua', cay='go'),
)

# ---------- Hình 2: Phan Việt Hà (2017), khối lượng 100 nhân (g) và % nhân trên sàng 16 ----------
RG = dict(dl=('Đắk Lắk', 'var(--k2)'), gl=('Gia Lai', 'var(--k4)'), ld=('Lâm Đồng', 'var(--k3)'), all=('TRS1, trung bình 4 vùng', 'var(--k5)'))
ROB = [('TR4', 'dl', 18.4, 80.0), ('TR9', 'dl', 22.5, 94.3), ('TR11', 'dl', 18.3, 88.2), ('TR14', 'dl', 20.9, 97.8), ('TR15', 'dl', 24.9, 98.1),
       ('TR16', 'dl', 20.0, 94.3), ('TR6', 'dl', 19.4, 92.7),
       ('TR4', 'gl', 15.3, 63.2), ('TR9', 'gl', 17.0, 75.0), ('TR11', 'gl', 15.7, 65.0), ('TR14', 'gl', 20.5, 95.4), ('TR15', 'gl', 22.0, 97.9),
       ('TR16', 'gl', 19.1, 93.2), ('TR6', 'gl', 18.4, 91.5),
       ('TR4', 'ld', 21.6, 86.9), ('TR9', 'ld', 29.6, 99.2), ('TR11', 'ld', 22.8, 95.8), ('TR14', 'ld', 22.4, 95.7), ('TR15', 'ld', 23.5, 96.3),
       ('TR16', 'ld', 20.2, 91.2), ('TR6', 'ld', 19.2, 90.0),
       ('TRS1', 'all', 19.1, 85.3)]

# ---------- bảng định lượng: giá trị và cờ nguồn ----------
FL = dict(N='NC', L='Loài', T='TL', U='Ước')
QT = [
    ('se', [('2,2–2,7', 'T'), ('≈ 10', 'L'), ('≈ 4', 'L'), ('13–17', 'U'), ('55–70%', 'U'), ('4–5%', 'T'), ('2–3 tấn/ha', 'U'), ('Cao', 'L')]),
    ('cs', [('≈ 2,2', 'L'), ('≈ 10', 'L'), ('≈ 4', 'L'), ('15,3–29,6; Lâm Đồng 19,2–29,6', 'N'), ('63–99%; Lâm Đồng 87–99%', 'N'), ('4–5%', 'T'),
            ('3,7–7,3 tấn/ha', 'N'), ('Cao', 'L')]),
    ('ara', [('≈ 1,2', 'L'), ('≈ 16', 'L'), ('≈ 8', 'L'), ('≈ 18', 'U'), ('≈ 80%', 'U'), ('4–5%', 'T'), ('Thấp', 'T'), ('Vết', 'N')]),
    ('cat', [('≈ 1,2', 'L'), ('≈ 16', 'L'), ('≈ 8', 'L'), ('16–18', 'U'), ('70–85%', 'U'), ('4–5%', 'T'), ('1,67 tấn/ha', 'N'), ('Vết', 'N')]),
    ('mok', [('Nếu là Mokka: khoảng ½ Arabica', 'T'), ('≈ 16', 'L'), ('≈ 8', 'L'), ('10–13', 'U'), ('20–40%', 'U'), ('—', ''), ('1–2 kg/cây/năm', 'T'), ('Vết', 'N')]),
    ('culi', [('Theo cây mẹ', ''), ('Theo cây mẹ', ''), ('Theo cây mẹ', ''), ('Theo cây mẹ', ''), ('Sàng riêng', ''), ('4–5% một vụ; lô culi từ 90%', 'T'), ('—', ''),
              ('Theo loài', '')]),
    ('lib', [('Gần Arabica', 'T'), ('—', ''), ('—', ''), ('≈ 21 (0,212 g một nhân)', 'N'), ('Hàng xuất khẩu từ 90%', 'T'), ('—', ''), ('—', ''), ('Chưa rõ', '')]),
    ('exc', [('Gần Arabica', 'T'), ('—', ''), ('—', ''), ('Nhỏ hơn Liberica', 'T'), ('—', ''), ('—', ''), ('Cao hơn Liberica', 'T'), ('Chưa rõ', '')]),
]
QROWS = [('Loài, nhóm', 'sp'), ('Nhân giống', 'prop'), ('Cây', 'tree'), ('Trái', 'cher'), ('Nhân xanh', 'bean'), ('Rãnh giữa', 'cutT'), ('Vùng, độ cao', 'alt'),
         ('Mùa hái', 'har'), ('Mùi vị', 'notes'), ('Thang chấm', 'scale'), ('Năng suất', 'yld'), ('Dễ nhầm với', 'conf')]

NAMES = [
    ('Cà Sẻ, Robusta Sẻ, Ro Sẻ, Robusta hạt nhỏ', 'Giống Robusta cũ, trồng từ hạt, nhân nhỏ. Tên dân gian, không phải tên phân loại.', 'Hồ sơ vườn, cây không vết ghép; cân 100 nhân; sàng.'),
    ('Robusta cao sản, Ro ghép, TR4, TR9, TR11, TR14, TRS1', 'Các dòng chọn lọc năng suất cao của Viện WASI, phần lớn nhân bằng ghép.', 'Nhân to, đều; ở Lâm Đồng thường trên 20 g mỗi 100 nhân.'),
    ('Culi', 'Hình hạt: trái chỉ có một nhân tròn. Robusta hay Arabica đều có, khoảng 4–5% một vụ.', 'Đếm hạt tròn trong 100 hạt; lô culi đã tách từ 90% trở lên.'),
    ('Moka', 'Giống Arabica thường được mô tả là dạng lùn của Bourbon; nhân rất nhỏ, tròn. Có nguồn cho rằng Cầu Đất chỉ còn khoảng 500 cây thuần.', 'Hỏi vườn, độ cao; cân 100 nhân; giá cao vì hiếm.'),
    ('Arabica Cầu Đất', 'Tên vùng, không phải tên giống. Ở đó có Typica, Bourbon, Moka, Catimor.', 'Hỏi giống cụ thể của lô.'),
    ('Catimor', 'Arabica lai Timor Hybrid với Caturra, giống trồng nhiều ở Việt Nam.', 'Cây thấp, lóng ngắn; hỏi vườn.'),
    ('Cà phê mít, Cherry, Chari', 'Tên chợ gọi chung nhóm Liberica và Excelsa; nay là hai loài khác nhau.', 'Nhân to, lệch, có móc là Liberica; dáng giọt nước là Excelsa.'),
    ('Fine Robusta', 'Hạng chất lượng: từ 80 điểm theo thang chấm Fine Robusta. Không phải giống.', 'Hỏi phiếu chấm điểm của lô.'),
    ('Honey, Natural, Washed', 'Cách sơ chế, không phải giống.', 'Hỏi quy trình, xem nhân và nếm.'),
    ('Rang bơ, tẩm hương', 'Cách tẩm, ướp khi rang. Không nói gì về giống.', 'Đọc thành phần trên bao bì.'),
]

SOP = [
    ('Lấy mẫu', 'Khoảng 300 g, trộn từ nhiều bao. Ghi mã lô và tên gọi khi chào hàng.'),
    ('Đo ẩm', 'Tối đa 12,5% theo TCVN 4193. Độ ẩm cao thì mọi số cân đều sai.'),
    ('Soi 100 nhân', 'Lật mặt phẳng lên, đếm rãnh thẳng, chữ S, nhăn lệch, hạt tròn.'),
    ('Sàng', 'Sàng 18 (7,10 mm), 16 (6,30 mm), 13 (5,00 mm). Cân từng tầng.'),
    ('Cân 100 nhân', 'Nhân nguyên, không vỡ. Cân 3 lần, lấy trung bình.'),
    ('Đếm lỗi', 'Hạt đen, nâu, non, vỡ, tạp chất, tính phần trăm khối lượng.'),
    ('Rang mẫu', 'Rang sáng đến vừa, cùng một hồ sơ rang cho mọi mẫu.'),
    ('Nếm', 'Nghỉ 8–24 giờ, 5 ly mỗi mẫu, nếm mù. Thang Fine Robusta hoặc SCA.'),
    ('Lab khi cần', 'Caffeine, 16-OMC bằng HPLC hoặc NMR; DNA để định danh dòng.'),
    ('Lưu mẫu', 'Giữ một phần mẫu đối chứng tới khi hết lô, ghi phiếu.'),
]

TCVN = [('R1 18a', '10', '0,1'), ('R1 18b', '15', '0,5'), ('R1 16a', '14', '0,5'), ('R1 16b', '16', '0,5'), ('R1 16c', '18', '0,5'),
        ('R2 13a', '17', '0,5'), ('R2 13b', '20', '0,5'), ('R2 13c', '24', '1,0'), ('R3', '70', '5,0')]

READ = [
    ('nhan', 'Cà Sẻ không phải Culi',
     'Sẻ là giống cây. Culi là hình hạt: trái chỉ nuôi một nhân tròn, giống nào cũng có, khoảng 4–5% một vụ. Có Culi Sẻ, Culi cao sản, Culi Arabica.', 'CoffeeHow; MeDili'),
    ('can', 'Nhân nhỏ chưa chắc là Sẻ',
     'Dòng TR4 trồng ở Gia Lai chỉ 15,3 g mỗi 100 nhân, ngang Cà Sẻ. Hạn, thiếu dinh dưỡng, hái non hay sàng lấy phần nhân nhỏ đều làm nhân nhỏ đi.', 'Phan Việt Hà 2017'),
    ('phantu', 'Caffeine không chứng minh được giống',
     'Robusta có caffeine gần gấp đôi Arabica, nhưng trong cùng loài, caffeine đổi theo vùng, độ chín, năm. Không có ngưỡng caffeine nào tách Sẻ khỏi cao sản.', 'Clarke 1987; MeDili'),
    ('trai', '“Moka” không phải tên chung của Arabica ngon',
     'Moka Cầu Đất là một giống Arabica cụ thể, thường được mô tả là dạng lùn của Bourbon: nhân rất nhỏ, tròn, mỗi cây chỉ khoảng 1–2 kg mỗi năm.', 'Helena; Coffee Review'),
    ('kinh', 'Màu nhân xanh không nói lên giống',
     'Màu đổi theo cách sơ chế, độ ẩm, thời gian kho. Đọc dáng nhân và rãnh giữa thay vì màu.', 'MeDili'),
    ('khien', 'Culi không “mạnh gấp đôi”',
     'Culi mang thành phần của cây mẹ. Hạt tròn lăn đều nên rang đều hơn, ly có thể tròn vị hơn, nhưng không bảo đảm.', 'CoffeeHow'),
]

SRC = [
    ('Prime Coffee (25/07/2026, cập nhật 06/10/2026). Nguồn gốc giống cà phê Robusta Sẻ Việt Nam: tên dân gian, nhân bằng hạt, nhóm di truyền ER, chương trình chọn giống từ 1976',
     'Prime Coffee', 'https://primecoffea.com/nguon-goc-giong-ca-phe-robusta-se-viet-nam/'),
    ('Phan Việt Hà (2017). Research results on robusta coffee breeding in Vietnam. Vietnam Journal of Science, Technology and Engineering 59(4): năng suất, khối lượng 100 nhân, tỷ lệ sàng 16 của các dòng TR theo vùng',
     'VJSTE', 'https://vietnamscience.vjst.vn/index.php/vjste/article/download/269/255/1044'),
    ('World Coffee Research. Varieties Catalog, TR9: dòng vô tính ghép, nhân lớn trên sàng 17, chín muộn, 5–6 tấn/ha, cần trồng xen dòng khác', 'WCR',
     'https://varieties.worldcoffeeresearch.org/varieties/tr9'),
    ('Đinh Thị Tiếu Oanh và cộng sự (2016). Kết quả chọn lọc dòng tự thụ cà phê chè thế hệ F5 tại các tỉnh Tây Nguyên. Tạp chí KH&amp;CN Nông nghiệp Việt Nam 2(63): Catimor 1,67 tấn/ha',
     'VAAS', 'https://tapchi.vaas.vn/vi/tap-chi/ket-qua-chon-loc-dong-tu-thu-ca-phe-che-he-f5-tai-cac-tinh-tay-nguyen'),
    ('IARC (2018). Monographs Vol. 116, Coffee: thành phần nhân xanh Arabica và Robusta theo Clarke (1987)', 'IARC',
     'https://publications.iarc.who.int/_publications/media/download/1796/e3b9d8b93f56977f63fd3c4b9aff66e768296f17.pdf'),
    ('Gunning Y. và cộng sự (2018). 16-O-methylcafestol is present in ground roast Arabica coffees. Food Chemistry: Robusta 600–1.800 mg/kg, Arabica chỉ có vết, phát hiện từ khoảng 1–3% Robusta trộn',
     'UEA', 'https://ueaeprints.uea.ac.uk/67696/1/Gunning_etal_2018_FoodChemistry.pdf'),
    ('SCA News số 25 (2025). Beyond Arabica and Robusta: Liberica và Excelsa là hai loài, hương vị, caffeine gần Arabica', 'SCA',
     'https://sca.coffee/sca-news/25/issue-25-insight-liberica-excelsa'),
    ('Ismail I., Anuar M. S., Shamsudin R. (2010). Physical properties of Malaysian coffee bean (Coffea liberica): nhân dài 11,46 mm, rộng 7,54 mm, dày 4,53 mm, nặng 0,212 g', 'UPM',
     'https://libmast.utm.my/Record/upm.eprints-41656/Description'),
    ('Helena Coffee (20/01/2026). Coffea Liberica in the Trend of Processing Innovation: tỷ lệ thịt quả, hương vị, lỗi khi chế biến kém', 'Helena',
     'https://www.helenacoffee.vn/coffea-liberica-processing-innovation/'),
    ('Helena Coffee. Vietnam Liberica Coffee Beans S18, S16: Kon Tum, Quảng Trị, Lâm Đồng, khoảng 800 m', 'Helena',
     'https://www.helenacoffee.vn/product/vietnam-liberica-coffee-beans-s18-s16/'),
    ('AP, đăng lại trên Vietnam Agriculture (2025). Excelsa: cây cao tới 15 m, chịu hạn, ngọt, trái sẫm, socola, hạt phỉ', 'Vietnam Agriculture',
     'https://vietnamagriculture.nongnghiep.vn/this-rare-coffee-bean-may-someday-be-your-new-brew-d741722.html'),
    ('Helena Coffee (16/05/2025). The Origin of Moka Cau Dat Coffee: dạng lùn của Bourbon, nhân nhỏ tròn, 1–2 kg mỗi cây, 1.500–1.600 m', 'Helena',
     'https://www.helenacoffee.vn/the-origin-of-moka-cau-dat-coffee/'),
    ('Coffee Review. Demystifying Mokka: đột biến lùn của Bourbon, nhân tròn như hạt đậu, năng suất thấp, caffeine khoảng một nửa Arabica thường', 'Coffee Review',
     'https://www.coffeereview.com/demystifying-mokka/'),
    ('Nguyen Coffee Supply. Types of Vietnamese coffee varietals: Catimor (Bồ Đào Nha, 1959), Typica Cầu Đất 2,5–3 tấn mỗi năm, Moka', 'Nguyen Coffee Supply',
     'https://nguyencoffeesupply.com/blogs/news/types-of-vietnamese-coffee-varietals'),
    ('Dallmayr. How to tell the difference between Arabica and Robusta: dáng nhân, rãnh giữa, vị', 'Dallmayr',
     'https://www.dallmayr.com/hr/academy/magazine/how-to-tell-the-difference-between-arabica-and-robusta/'),
    ('Kaffeemacher. Fine Robusta und Q Robusta Grading: thang điểm, từ 80 điểm là Fine Robusta', 'Kaffeemacher',
     'https://kaffeemacher.ch/en/blogs/kaffeewissen/fine-robusta-und-q-robusta-grading'),
    ('CoffeeHow. Peaberry coffee: hạt culi khoảng 4–5% một vụ, rang đều hơn, vị không bảo đảm khác', 'CoffeeHow', 'https://coffeehow.co/peaberry-coffee/'),
    ('Helena Coffee. Vietnam National Coffee Export Standards: tóm tắt TCVN 4193:2014 về hạng, % hạt lỗi, lẫn loại, lỗ sàng, độ ẩm', 'Helena', 'https://www.helenacoffee.vn/?p=1372'),
    ('Nhật Trường Kon Tum. Robusta hạt sẻ là gì: giống cũ, nhân nhỏ chắc, vị đậm; đổi sang cao sản tăng sản lượng khoảng 60–80%', 'Nhật Trường',
     'https://nhattruongkontum.com/news/tan-man/robusta-hat-se-la-gi-co-may-loai-robusta-90.html'),
    ('Doanh Đăng. Robusta Sẻ là gì: caffeine 2,2–2,7% theo tài liệu thương mại', 'Doanh Đăng',
     'https://doanhdang.com/robusta-se-la-gi-nhung-dac-diem-noi-bat-cua-ca-phe-thuan-chung.html'),
    ('Mia.vn. Cao nguyên Di Linh: độ cao khoảng 1.000 m, Robusta trồng ở 900–1.000 m', 'Mia.vn',
     'https://mia.vn/cam-nang-du-lich/cao-nguyen-di-linh-mot-thoang-thien-nhien-khoac-len-minh-ve-dep-hoang-so-quyen-ru-1493'),
]


def _tag(v, f):
    # Không gắn nhãn nguồn trên web; riêng số MeDili ước thì ghi rõ chữ “Ước”.
    if f == 'U' and not v.startswith('Ước'):
        return 'Ước ' + (v[2:] if v.startswith('≈ ') else v)
    return v


def _sw(k):
    return f'<i class="sw" style="background:{SM[k]["c"]}"></i>'


def qtable():
    hd = ['Mẫu', 'Caffeine, % chất khô', 'Chất béo, %', 'Sucrose, %', '100 nhân, g', 'Trên sàng 16', 'Hạt tròn (culi)', 'Năng suất nhân', '16-OMC']
    rows = ''
    for k, cells in QT:
        cls = ' class="hl"' if k == 'se' else ''
        rows += f'<tr{cls}><td>{_sw(k)}{SM[k]["n"]}</td>' + ''.join(f'<td>{_tag(v, f)}</td>' for v, f in cells) + '</tr>'
    return '<thead><tr>' + ''.join(f'<th>{h}</th>' for h in hd) + '</tr></thead><tbody>' + rows + '</tbody>'


def qualtable():
    head_ = '<thead><tr><th></th>' + ''.join(f'<th>{_sw(s["k"])}{s["s"]}</th>' for s in SAMPLES) + '</tr></thead>'
    body = ''.join(f'<tr><th>{n}</th>' + ''.join(f'<td>{s[f]}</td>' for s in SAMPLES) + '</tr>' for n, f in QROWS)
    return head_ + '<tbody>' + body + '</tbody>'


def robtable():
    rows = ''.join(f'<tr><td>{c}</td><td>{RG[r][0]}</td><td>{str(w).replace(".", ",")}</td><td>{str(s).replace(".", ",")}%</td></tr>' for c, r, w, s in ROB)
    return '<thead><tr><th>Dòng</th><th>Vùng</th><th>100 nhân, g</th><th>Trên sàng 16</th></tr></thead><tbody>' + rows + '</tbody>'


def page():
    body = head('Phân biệt cà phê', 'Cỗ máy',
                'Tám mẫu cà phê đi qua tám trạm: vườn, trái chín, bàn soi nhân, sàng, cân, phòng thí nghiệm, bàn nếm và bộ quyết định. '
                'Nhìn và nếm là định tính; sàng, cân, phân tích là định lượng. Trọng tâm là Robusta Cà Sẻ Di Linh: nhận ra thế nào, và khác Robusta cao sản ở đâu.')
    vs2 = [
        ('Nguồn gốc', 'Robusta đưa vào Việt Nam từ đầu thế kỷ XX, trồng phổ biến ở Tây Nguyên trước khi có giống WASI', 'Các dòng WASI chọn lọc từ năm 1976: TR4, TR9, TR11, TR14, TR15; TRS1 lai từ TR4, TR9, TR11, TR12'),
        ('Nhân giống', 'Từ hạt, nên mỗi cây một khác', 'Ghép chồi, giâm cành, vườn đồng đều; phải trồng xen nhiều dòng'),
        ('100 nhân', _tag('Ước 13–17 g', 'U'), _tag('15,3–29,6 g tùy dòng và vùng; ở Lâm Đồng 19,2–29,6 g', 'N')),
        ('Trên sàng 16', _tag('Ước 55–70%', 'U'), _tag('63–99%; ở Lâm Đồng 86,9–99,2%', 'N')),
        ('Năng suất', _tag('Ước 2–3 tấn nhân/ha', 'U'), _tag('3,7–7,3 tấn nhân/ha trong thí nghiệm', 'N')),
        ('Caffeine', _tag('2,2–2,7% theo tài liệu thương mại', 'T'), _tag('Robusta nói chung khoảng 2,2%', 'L')),
        ('Ly cà phê', 'Đậm, đắng rõ, hậu dài, thân dày; socola đen, ca cao', 'Đắng rõ, gỗ, ngũ cốc rang; vị nhẹ hơn'),
        ('Điểm mạnh', 'Nguồn gen thích nghi với hạn và sâu bệnh; câu chuyện của vùng', 'Năng suất cao, nhân to đều, kháng gỉ sắt'),
        ('Điểm yếu', 'Năng suất thấp, nhân nhỏ, ít hàng sàng to', 'Cần thâm canh; TRS1 chịu hạn kém'),
    ]
    vs2h = ('<thead><tr><th></th><th>' + _sw('se') + 'Cà Sẻ Di Linh</th><th>' + _sw('cs') + 'Robusta cao sản</th></tr></thead><tbody>'
            + ''.join(f'<tr><th>{a}</th><td class="a">{b}</td><td>{c}</td></tr>' for a, b, c in vs2) + '</tbody>')
    flg = ''
    sop = ''.join(f'<div><span class="k">Bước {i}</span><b>{t}</b><p>{p}</p></div>' for i, (t, p) in enumerate(SOP, 1))
    names = ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a, b, c in NAMES)
    tcvn = ''.join(f'<tr><td>{a}</td><td>{b}%</td><td>{c}%</td></tr>' for a, b, c in TCVN)
    body += f'''
<div class="bench">
  <div class="card">
    <div class="fighead">
      <div><b>Hình 1</b> <span id="figsub"></span></div>
      <button class="btn small" id="run2" type="button">Chạy máy</button>
    </div>
    <div class="scroller"><svg id="scene" viewBox="0 0 1040 720" aria-label="Bàn mô hình tám trạm: vườn, trái chín, bàn soi nhân, sàng, cân 100 nhân, phòng thí nghiệm, bàn nếm, bộ quyết định. Bấm từng trạm để xem chi tiết."></svg></div>
    <div class="strip" id="strip" role="group" aria-label="Chọn trạm"></div>
    <div id="detail" aria-live="polite"></div>
  </div>

  <aside class="card ctl">
    <div class="head2"><h3>Mẫu đưa vào máy</h3><small>8 mẫu</small></div>
    <div class="row" id="samps"></div>
    <p class="mnote" id="sNote"></p>
    <div class="row" style="margin-top:12px"><button class="btn main" id="run" type="button">Chạy máy</button><button class="btn" id="myst" type="button">Mẫu bí ẩn</button><button class="btn" id="reveal" type="button" hidden>Lộ đáp án</button><button class="btn" id="back" type="button" hidden>Về hồ sơ chuẩn</button></div>
    <hr>
    <div class="head2"><h3>Số đo</h3><small id="modeL"></small></div>
    <div class="sl" style="margin-top:6px"><label for="iW">Khối lượng 100 nhân <output id="oW"></output></label><input id="iW" type="range" min="9" max="31" step="0.1"><p>Nhân nguyên, độ ẩm từ 12,5% trở xuống.</p></div>
    <div class="sl"><label for="iS">Nhân trên sàng 16 <output id="oS"></output></label><input id="iS" type="range" min="10" max="100" step="1"><p>Lỗ sàng 6,30 mm, mẫu 300 g.</p></div>
    <div class="sl"><label for="iC">Hạt tròn trong 100 hạt <output id="oC"></output></label><input id="iC" type="range" min="0" max="100" step="1"></div>
    <span class="lbl" style="margin-top:12px">Rãnh giữa của nhân</span>
    <div class="row" id="cuts"></div>
    <label class="tg"><input type="checkbox" id="lab"> Có kết quả phòng thí nghiệm</label>
    <div id="labBox">
      <div class="sl"><label for="iCa">Caffeine <output id="oCa"></output></label><input id="iCa" type="range" min="0.4" max="3" step="0.05"></div>
      <div class="sl"><label for="iL">Chất béo <output id="oL"></output></label><input id="iL" type="range" min="6" max="19" step="0.5"></div>
      <div class="sl"><label for="iSu">Sucrose <output id="oSu"></output></label><input id="iSu" type="range" min="1.5" max="10" step="0.1"><p>Tính trên chất khô của nhân xanh.</p></div>
    </div>
    <div class="stats" id="stats"></div>
    <div id="verdict" aria-live="polite"></div>
    <hr>
    <span class="lbl">Bản đồ hai chỉ số</span>
    <div class="charts"><svg class="ch" id="cM" viewBox="0 0 340 200" role="img" aria-label="Caffeine theo khối lượng 100 nhân của tám mẫu"></svg></div>
    <p class="mnote" id="mTip"></p>
  </aside>
</div>

<section class="card sehero" id="ca-se">
  <div class="seh">
    <div>
      <p class="eye">Trọng tâm · Robusta Cà Sẻ Di Linh</p>
      <h2 class="p-h2" style="margin:0">Cà Sẻ là một giống, <em>không phải hình hạt hay hạng hàng.</em></h2>
      <p>“Sẻ” là tên dân gian, không phải tên phân loại chính thức; tên chung vẫn là Robusta. Cà Sẻ, Robusta Sẻ, Ro Sẻ hay Robusta hạt nhỏ đều chỉ giống Robusta cổ do người Pháp đưa vào Việt Nam từ đầu thế kỷ XX, mang lên Di Linh và khắp Tây Nguyên trồng trước khi có các giống chọn lọc của Viện WASI. Cây được nhân bằng hạt nên quần thể không đồng đều: mỗi cây một dáng, trái và năng suất khác nhau. Tên gọi phản ánh nhân nhỏ, trái nhỏ và tán gọn.</p>
      <p>Phân tích 126 mẫu trong ngân hàng gen của WASI cho thấy phần lớn vật liệu Robusta Việt Nam thuộc nhóm di truyền ER, từ lưu vực sông Congo. Từ năm 1976, WASI bắt đầu chọn giống quy mô lớn; các dòng TR4, TR9, TR11, rồi TR14, TR15 dần thay Cà Sẻ vì năng suất cao và nhân to. Cà Sẻ ít được trồng mới, nhưng là vật liệu nền của Robusta Việt Nam và giữ nhiều gen thích nghi với hạn, sâu bệnh.</p>
    </div>
    <div class="medili">
      <h3>Vườn Cà Sẻ của MeDili</h3>
      <ul>
        <li>Cao nguyên Di Linh khoảng 1.000 m; Robusta trồng ở khoảng 900–1.000 m.</li>
        <li>Canh tác từ năm 2010, cây 15 năm tuổi, chăm sóc theo hướng tự nhiên.</li>
        <li>Trời mát nên trái chín chậm: hái nhiều lượt từ tháng 11 tới đầu tháng 1, trái xanh tối đa 5%.</li>
        <li>MeDili ghi nhận: những cây Cà Sẻ lâu năm cho ly cà phê ngon, giàu caffeine.</li>
      </ul>
    </div>
  </div>
  <h3 class="h3s">Bảy dấu hiệu nhận ra Cà Sẻ</h3>
  <ol class="signs">
    <li><b>Gốc không vết ghép</b><span>Cây mọc từ hạt. Đi một hàng 20 cây sẽ thấy dáng, lá, trái khác nhau.</span><em>Vườn · định tính</em></li>
    <li><b>Trái nhỏ, chùm dày</b><span>Trái nhỏ hơn dòng ghép; màu và độ chín khác nhau giữa các cây.</span><em>Trái · định tính</em></li>
    <li><b>Nhân nhỏ, chắc, lưng dày</b><span>Dáng tròn ngắn, rãnh giữa thẳng như mọi Robusta.</span><em>Nhân · định tính</em></li>
    <li><b>Nhẹ khi cân</b><span>Ước 13–17 g mỗi 100 nhân; các dòng TR4, TR9, TR11 trồng ở Lâm Đồng nặng 21,6–29,6 g.</span><em>Cân · định lượng</em></li>
    <li><b>Ít nhân sàng to</b><span>Phần lớn nằm ở sàng 13–16; dòng ghép ở Lâm Đồng có 87–99% nằm trên sàng 16.</span><em>Sàng · định lượng</em></li>
    <li><b>Đậm, đắng rõ, hậu dài</b><span>Socola đen, ca cao; thân dày, ít chua. Cao sản đắng nhưng vị nhẹ hơn.</span><em>Nếm · cảm quan</em></li>
    <li><b>Có hồ sơ vườn</b><span>Mã vườn, năm trồng, nguồn hạt giống. Đây là bằng chứng mạnh nhất; cần chắc chắn thì xét nghiệm DNA.</span><em>Truy xuất</em></li>
  </ol>
  <h3 class="h3s">Cà Sẻ và Robusta cao sản, đặt cạnh nhau</h3>
  {flg}
  <div class="tw"><table class="rich vs2">{vs2h}</table></div>
  <p class="mnote">Cùng loài Robusta nên caffeine, chất béo, đường của hai nhóm chồng lên nhau; phân tích hóa học không tách được. Khác biệt nằm ở cây, cỡ nhân, năng suất và ly cà phê. Số “ước” của Cà Sẻ suy từ đối chứng Robusta trồng hạt đại trà trong thí nghiệm giống TRS1 (TRS1 hơn đối chứng 50,2% năng suất và 25,4% khối lượng 100 nhân), chưa phải số đo riêng của vườn Di Linh.</p>
</section>

<section class="card" id="robusta">
  <h2>Hình 2: cỡ nhân của các dòng Robusta theo vùng</h2>
  <p class="lead">Mỗi chấm là một dòng Robusta ở một vùng, theo số liệu thí nghiệm giống. Cùng dòng TR4: 15,3 g mỗi 100 nhân ở Gia Lai nhưng 21,6 g ở Lâm Đồng. Vì vậy chỉ so cỡ nhân khi cùng vùng, cùng vụ. Vùng tô viền đứt là khoảng ước của Cà Sẻ.</p>
  <div class="lg" id="lgR"></div>
  <div class="chw" id="wR"><svg id="cR" class="c2" role="img" aria-label="Khối lượng 100 nhân và phần trăm nhân trên sàng 16 của các dòng Robusta ở Đắk Lắk, Gia Lai, Lâm Đồng"></svg></div>
  <details class="more"><summary>Xem số liệu của Hình 2</summary><div class="tw"><table class="rich">{robtable()}</table></div></details>
</section>

<section class="card" id="nhan-dien">
  <h2>Máy nhận diện bằng giác quan</h2>
  <p class="lead">Chọn điều bạn nhìn, ngửi, nếm được. Máy cộng dồn bằng chứng và xếp hạng tám mẫu. Trọng số do MeDili đặt từ mô tả trong tài liệu, không phải mô hình đo đạc; dùng để luyện mắt, mũi, lưỡi. Bấm lại một lựa chọn để bỏ.</p>
  <div class="prow"><span>Điền thử như mẫu</span><div class="row" id="qPre" style="margin-top:0"></div></div>
  <div class="qzw">
    <div class="qgrid" id="qz"></div>
    <div class="qres" id="qzr" aria-live="polite"></div>
  </div>
</section>

<section class="card" id="dinh-luong">
  <h2>Định lượng: tám mẫu, tám chỉ số</h2>
  <p class="lead">Số liệu tổng hợp từ tài liệu nghiên cứu và tài liệu ngành. Ô có chữ “Ước” là số MeDili ước cho mô hình; ô gạch ngang là chưa có số đáng tin, MeDili không tự điền.</p>
  {flg}
  <div class="tw"><table class="rich qtab">{qtable()}</table></div>
  <p class="mnote">Caffeine, chất béo, sucrose tính trên chất khô của nhân xanh. 16-OMC (16-O-methylcafestol) là dấu vết hóa học của Robusta, dùng để phát hiện Robusta trộn vào Arabica.</p>
  <details class="more"><summary>Tham số mà cỗ máy dùng (trung bình ± độ lệch)</summary><div class="tw"><table class="rich" id="pTab"></table></div>
  <p class="mnote">Giá trị trung tâm chọn từ bảng trên. Ở chỗ chưa có số, như chất béo của Liberica, MeDili đặt khoảng rộng để máy không dựa nhiều vào đó.</p></details>
</section>

<section class="card" id="dinh-tinh">
  <h2>Định tính: dáng nhân và từng cặp dễ nhầm</h2>
  <p class="lead">Hình 3 vẽ nhân xanh của tám mẫu cùng một tỷ lệ, mặt phẳng hướng lên. Chiều dài ước theo khối lượng 100 nhân và dáng nhân; riêng Liberica theo số đo 11,46 mm. Đây là hình vẽ khái niệm.</p>
  <div class="bgal" id="bgal"></div>
  <h3 class="h3s">Đối chiếu từng cặp</h3>
  <div class="prow"><span>Mẫu A</span><div class="row" id="pA" style="margin-top:0"></div><span>Mẫu B</span><div class="row" id="pB" style="margin-top:0"></div></div>
  <div class="pX" id="pX"></div>
  <div class="tw"><table class="rich pt" id="pT"></table></div>
  <details class="more"><summary>Xem bảng định tính đầy đủ cả tám mẫu</summary><div class="tw"><table class="rich qual">{qualtable()}</table></div></details>
</section>

<section class="card" id="cam-quan">
  <h2>Hình 4: hồ sơ cảm quan, Cà Sẻ đặt cạnh mẫu khác</h2>
  <p class="lead">Cường độ tương đối trên thang 10, MeDili chuyển từ mô tả cảm quan trong tài liệu; không phải điểm thử nếm (cupping).</p>
  <div class="prow"><span>So với</span><div class="row" id="rB" style="margin-top:0"></div></div>
  <div class="radg">
    <div><div class="radw"><svg id="cRad" viewBox="0 0 340 300" role="img" aria-label="Biểu đồ sáu trục: thơm, chua, ngọt, đắng, thể chất, hậu vị"></svg></div><div class="lg" id="lgRad" style="justify-content:center"></div><p class="mnote" id="radT" style="text-align:center"></p></div>
    <div>
      <h3 class="h3s" style="margin-top:0">Chấm điểm theo thang nào</h3>
      <ul class="dots">
        <li><b>Robusta:</b> thang Fine Robusta, gồm hương, vị, hậu vị, tỷ lệ mặn và chua, tỷ lệ đắng và ngọt, cảm giác miệng, cân bằng, độ đồng đều, độ sạch và tổng thể. Từ 80 điểm là Fine Robusta.</li>
        <li><b>Arabica:</b> thang của SCA. Catimor, Typica, Moka đều chấm theo thang này.</li>
        <li><b>Liberica, Excelsa:</b> chưa có thang riêng phổ biến; thường mượn phiếu của Arabica.</li>
        <li><b>Muốn so giống:</b> rang sáng đến vừa, cùng một hồ sơ rang, nghỉ 8–24 giờ, 5 ly mỗi mẫu, nếm mù. Rang đậm che mất khác biệt.</li>
      </ul>
      <p class="mnote">Ghi phiếu theo <a class="lnk" href="banh-xe-huong.html">Bánh xe hương MeDili</a>.</p>
    </div>
  </div>
</section>

<section class="p-sec">
  <p class="eye">Hiểu nhầm hay gặp</p>
  <h2 class="p-h2" style="margin:0">Sáu điều <em>dễ nói sai khi bán cà phê.</em></h2>
  <div class="g3">{boxes(READ)}</div>
</section>

<section class="card" id="ten-goi">
  <h2>Tên gọi trên thị trường</h2>
  <p class="lead">Nhiều tên bán hàng là tên giống, nhiều tên lại là hình hạt, tên vùng, hạng hay cách sơ chế. Hỏi đúng câu thì bớt mua nhầm.</p>
  <div class="tw"><table class="rich ten"><thead><tr><th>Tên gọi</th><th>Thật ra là gì</th><th>Kiểm thế nào</th></tr></thead><tbody>{names}</tbody></table></div>
</section>

<section class="card" id="quy-trinh">
  <h2>Quy trình kiểm tra mẫu khi mua nhân</h2>
  <p class="lead">Mười bước MeDili dùng khi nhận mẫu. Bước 1–6 làm ở xưởng trong một buổi; bước 7–8 cần lò rang mẫu và bàn nếm; bước 9 chỉ khi cần chứng nhận.</p>
  <div class="flowx">{sop}</div>
  <div class="cols" style="margin-top:16px">
    <div>
      <h3 class="h3s" style="margin-top:0">TCVN 4193:2014 cho Robusta</h3>
      <div class="tw"><table class="rich"><thead><tr><th>Hạng</th><th>Hạt lỗi tối đa</th><th>Tạp chất tối đa</th></tr></thead><tbody>{tcvn}</tbody></table></div>
      <p class="mnote">Tính theo phần trăm khối lượng, mẫu khoảng 300 g. Độ ẩm tối đa 12,5%. Robusta hạng 1 được lẫn tối đa 0,5% cà phê mít và 3% Arabica; hạng 2, 3 tối đa 1% và 5%. Arabica hạng 1 không được lẫn Robusta và cà phê mít. Lỗ sàng: số 18 là 7,10 mm, 16 là 6,30 mm, 14 là 5,60 mm, 13 là 5,00 mm.</p>
    </div>
    <div>
      <h3 class="h3s" style="margin-top:0">Phiếu kiểm mẫu</h3>
      <pre class="msg" id="sheet"></pre>
      <button class="btn small" id="cpSh" type="button">Sao chép phiếu</button> <span class="cpst" id="cpShS" role="status"></span>
    </div>
  </div>
</section>

<section class="card src">
  <h2>Nguồn và cách đọc mô hình</h2>
  <p class="lead">Cỗ máy là mô hình minh họa. Mỗi mẫu có một khoảng giá trị điển hình cho sáu chỉ số và kiểu rãnh giữa; máy tính xem số đo khớp mẫu nào nhất, theo cách cộng dồn bằng chứng của bộ phân loại Bayes đơn giản. Số có chữ “Ước” là MeDili ước cho mô hình. Với hai giống cùng loài như Cà Sẻ và cao sản, chỉ hồ sơ vườn và xét nghiệm DNA mới cho câu trả lời chắc chắn.</p>
  <ul>{srclist(SRC)}<li>Đinh Thị Tiếu Oanh và cộng sự (2016). Giống cà phê vối lai đa dòng TRS1. Tạp chí KH&amp;CN Nông nghiệp Việt Nam 2(63): 3–8. TRS1 hơn đối chứng đại trà 50,2% năng suất và 25,4% khối lượng 100 nhân; MeDili dùng để ước Cà Sẻ.</li><li>MeDili: vườn Cà Sẻ Di Linh canh tác từ năm 2010, cây 15 năm tuổi, lịch hái và mô tả vị từ phiếu nếm của xưởng.</li></ul>
  <div class="lnks"><a class="lnk" href="trai-chin.html">Cỗ máy Trái chín</a><a class="lnk" href="vi-sinh.html">Cỗ máy Vi sinh</a><a class="lnk" href="tien-chat-huong.html">Cỗ máy Tiền chất hương</a><a class="lnk" href="banh-xe-huong.html">Bánh xe hương MeDili</a><a class="lnk" href="trai-ca-phe.html">Giải phẫu trái Cà Sẻ</a><a class="lnk" href="journal.html">Tất cả kiến thức cà phê</a></div>
</section>
'''
    data = 'const SM=' + json.dumps(SM, ensure_ascii=False) + ';const QZ=' + json.dumps(QZ, ensure_ascii=False) + ';const PRE=' + json.dumps(PRE) + \
           ';const ROB=' + json.dumps(ROB) + ';const RG=' + json.dumps(RG, ensure_ascii=False) + ';\n'
    return doc(FILE, TITLE, DESC, body, css=ISO_CSS + CSS, js=ISO_JS + data + JS)


CSS = r'''
/* Cỗ máy Phân biệt cà phê */
:root{--k1:var(--accent);--k2:#B8862A;--k3:#7A348E;--k4:#C74B7A;--k5:#5E3A24;--k6:#D9782E;--k7:#8D5A32;--k8:#A0699A}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--k2:#D9AE55;--k3:#A06BCD;--k4:#E07AA0;--k5:#C9A27A;--k6:#EE9A5A;--k7:#B5865A;--k8:#CFA0C8}}
:root[data-theme="dark"]{--k2:#D9AE55;--k3:#A06BCD;--k4:#E07AA0;--k5:#C9A27A;--k6:#EE9A5A;--k7:#B5865A;--k8:#CFA0C8}
#scene .soil{fill:#7A5233}#scene .soilT{fill:#8D6A45}#scene .soil2{fill:#5E3E24}
#scene .can1{fill:#A9743F}#scene .can2{fill:#8D5A32}#scene .can3{fill:#C08A4E}
#scene .trk{fill:#6B4226}#scene .grf{fill:#D9B77E}
#scene .pnl{fill:#E6DCC8}#scene .pnl2{fill:#CFC2A8}#scene .pnl3{fill:#B7A98C}
#scene .pnlF{fill:#F6EEDC;stroke:#B7A98C;stroke-width:1}
#scene .lbx{fill:#F6EBCF}#scene .lbx2{fill:#D8C9A6}#scene .lbx3{fill:#BFAE88}
#scene .sv1{fill:#B7A98C}#scene .sv1t{fill:#CFC2A8}#scene .sv2{fill:#A99878}#scene .sv2t{fill:#C2B089}
#scene .plt{fill:#D8CBAE}
#scene .bnf{fill:#B8894A}#scene .bnft{fill:#CFA05E}
#scene .ins{fill:#E6DCC8}#scene .ins2{fill:#CFC2A8}#scene .ins3{fill:#B7A98C}
#scene .vial{fill:#F6F0E4;fill-opacity:.55}#scene .vialT{fill:#F6F0E4;fill-opacity:.4}
#scene .lampOn{fill:#E3B341}#scene .lampOff{fill:#8D7A63}
#scene .cup{fill:#FFF6EC}#scene .cupT{fill:#6B4226}
#scene .cab{fill:#E6DCC8}#scene .cab2{fill:#CFC2A8}#scene .cab3{fill:#B7A98C}
#scene .belt{fill:#8D7A63}#scene .belt2{fill:#6F5E4A}#scene .beltT{fill:#A8957A}
#scene .qm{font:800 26px var(--display);fill:#6B4226}
#scene .bt{font:700 6.4px var(--body);fill:#3A2416}
#scene .bbg{fill:#D8CBAE}
#scene .m .cbn{stroke:#8D6A45;stroke-width:1.1}
#scene .m .cbc{stroke:#6B4226;stroke-width:1.5}
#scene .m .cbh{stroke:none}
#scene .stm{opacity:.55}
#scene.running .stm{animation:stmA 1.8s ease-in-out infinite}
@keyframes stmA{0%{transform:translateY(3px);opacity:0}40%{opacity:.8}100%{transform:translateY(-8px);opacity:0}}
.cbn{fill:#D8C79C;stroke:#8D6A45;stroke-width:1.2}
.cbc{fill:none;stroke:#6B4226;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}
.cbh{fill:#F3EAD0;opacity:.55;stroke:none}
.fl{display:inline-block;font:700 .62rem/1.5 var(--body);letter-spacing:.04em;padding:0 5px;border-radius:5px;margin-left:4px;vertical-align:1px;white-space:nowrap}
.fN{background:var(--accent);color:var(--on-accent)}
.fL{background:var(--panel);color:var(--ink);box-shadow:inset 0 0 0 1px var(--ink)}
.fT{background:var(--panel);color:var(--muted);box-shadow:inset 0 0 0 1px var(--rule)}
.fU{background:var(--panel);color:var(--muted);border:1px dashed var(--muted);padding:0 4px;line-height:1.35}
.flg{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:.84rem;color:var(--muted);margin:4px 0 10px}
.flg .fl{margin:0 4px 0 0}
.sw{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:7px;vertical-align:0;flex:none}
.qtab td:first-child{font-weight:700;white-space:nowrap}
.qtab td{min-width:120px}
tr.hl td{background:var(--tint)}
.vs2 th:first-child{width:120px}
.vs2 td{min-width:200px}
@media (max-width:560px){.vs2 td,.pt td,.ten td,.ten td:first-child{min-width:160px}}
.vs2 td.a{background:var(--tint)}
.qual td{min-width:170px}.qual tbody th{white-space:nowrap}
.ten td{min-width:180px}.ten td:first-child{min-width:200px}
.seh{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:18px 28px;align-items:start}
.seh p{max-width:72ch}
@media (max-width:900px){.seh{grid-template-columns:minmax(0,1fr)}}
.h3s{font:800 1.4rem/1.2 var(--display);margin:22px 0 8px;letter-spacing:.01em}
.signs{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
.signs li:last-child{grid-column:span 2}
@media (max-width:1100px){.signs{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.signs{grid-template-columns:minmax(0,1fr)}.signs li:last-child{grid-column:auto}}
.signs li{background:var(--tint);border-radius:14px;padding:12px 14px 12px 52px;position:relative;counter-increment:sg;min-width:0}
.signs{counter-reset:sg}
.signs li::before{content:counter(sg);position:absolute;left:12px;top:12px;width:28px;height:28px;border-radius:50%;background:var(--accent);color:var(--on-accent);font:800 1rem/28px var(--display);text-align:center}
.signs b{display:block;font:700 .98rem/1.3 var(--body)}
.signs span{display:block;font-size:.88rem;margin-top:3px}
.signs em{display:block;font:600 .68rem/1.3 var(--body);font-style:normal;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin-top:7px}
.prow{display:grid;grid-template-columns:auto minmax(0,1fr);gap:8px 12px;align-items:center;margin:8px 0 4px}
.prow>span{font-weight:600;font-size:.88rem;white-space:nowrap}
.prow .pill{font-size:.82rem;padding:7px 11px}
@media (max-width:620px){.prow{grid-template-columns:minmax(0,1fr)}}
.qzw{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:18px;align-items:start;margin-top:10px}
@media (max-width:1100px){.qzw{grid-template-columns:minmax(0,1fr)}}
.qgrid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
@media (max-width:1250px){.qgrid{grid-template-columns:repeat(2,minmax(0,1fr))}.qgrid>.qb:last-child{grid-column:1/-1}}
@media (max-width:620px){.qgrid{grid-template-columns:minmax(0,1fr)}}
.qb{border:1px solid var(--rule);border-radius:12px;padding:10px 12px;min-width:0}
.qb b{display:block;font:700 .95rem var(--body)}
.qb small{display:block;color:var(--muted);font-size:.8rem;line-height:1.35}
.qb .row{margin-top:6px}
.qb .pill{font-size:.8rem;padding:6px 10px;text-align:left;line-height:1.25}
.qres{background:var(--tint);border-radius:14px;padding:14px 16px;position:sticky;top:76px;min-width:0}
@media (max-width:1100px){.qres{position:static}}
.qh{display:block;font:800 1.3rem/1.2 var(--display);margin:2px 0 4px}
.pbar{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:3px 8px;align-items:center;margin-top:8px;font-size:.88rem}
.pbar span{font-weight:600;min-width:0}
.pbar b{font:700 .88rem var(--mono);text-align:right}
.pbar i{grid-column:1/-1;display:block;height:8px;border-radius:4px;background:var(--rule);overflow:hidden}
.pbar i em{display:block;height:100%;border-radius:4px}
#verdict .pbar b{color:var(--ink);display:inline}
.why{display:flex;flex-wrap:wrap;gap:6px;margin-top:6px}
.why span{font-size:.78rem;background:var(--panel);border:1px solid var(--rule);border-radius:999px;padding:3px 9px}
.bgal{display:grid;grid-template-columns:repeat(8,minmax(0,1fr));gap:10px;margin-top:6px}
@media (max-width:1250px){.bgal{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media (max-width:560px){.bgal{grid-template-columns:repeat(2,minmax(0,1fr))}}
.bgal figure{margin:0;background:var(--tint);border-radius:12px;padding:8px 8px 10px;text-align:center;min-width:0}
.bgal svg{display:block;width:100%;height:auto;max-width:150px;margin:0 auto}
.bgal figcaption b{display:block;font:700 .92rem var(--body)}
.bgal figcaption span{display:block;font-size:.78rem;color:var(--muted);line-height:1.35}
.pX{background:var(--tint);border-radius:12px;padding:10px 14px;margin:10px 0;font-size:.92rem;max-width:110ch}
.pX b{display:block;font:700 .72rem/1.3 var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--accent);margin-bottom:3px}
.pt td{min-width:200px}.pt tbody th{white-space:nowrap;color:var(--muted);font-weight:600}
.radg{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:18px 32px;align-items:center;margin-top:6px}
@media (max-width:900px){.radg{grid-template-columns:minmax(0,1fr)}}
.radw{max-width:420px;margin:0 auto}
#cRad{display:block;width:100%;height:auto}
#cRad text{font:600 12px var(--body);fill:var(--ink)}
#cRad .grid{fill:none;stroke:var(--rule);stroke-width:1}
.dots{margin:0;padding-left:18px}.dots li{margin-bottom:6px}
.tg{display:flex;gap:8px;align-items:center;font-weight:600;margin-top:12px;cursor:pointer}
.tg input{width:18px;height:18px;accent-color:var(--accent);margin:0}
.ctl .row .pill{font-size:.82rem;padding:7px 11px}
details.more{margin-top:10px}
details.more summary{cursor:pointer;font-weight:600;color:var(--accent)}
details.more[open] summary{margin-bottom:6px}
#sheet{min-height:300px}
@media (prefers-reduced-motion:reduce){#scene .stm{animation:none!important}}
'''

JS = r'''
const U=7,OX=196,OY=118,VBW=1040;
const ORD=['se','cs','ara','cat','mok','culi','lib','exc'];
const FE=['w','s16','cu','caf','lip','suc'];
const FN={w:['100 nhân','g',1],s16:['Trên sàng 16','%',0],cu:['Hạt tròn','%',0],caf:['Caffeine','%',2],lip:['Chất béo','%',1],suc:['Sucrose','%',1]};
const CUTN={t:'rãnh thẳng',s:'rãnh chữ S',r:'rãnh nhăn, lệch',p:'tròn, không mặt phẳng'},CUTS={t:'rãnh thẳng',s:'rãnh chữ S',r:'rãnh nhăn',p:'tròn, culi'};
const CUTL={};QZ.find(q=>q.id==='ranh').o.forEach(o=>CUTL[o.id]=o.w);
const pc=v=>clamp(Math.round(v*100),0,99);
const st={k:'se',mode:'ref',hid:null,mm:null,am:11.8,rev:false,myN:0,own:null,cut:null,lab:true,step:8,sel:1,qa:{...PRE.se},pa:'se',pb:'cs',rb:'cs'};
let R={};
function means(k){const m={};FE.forEach(f=>m[f]=SM[k].q[f][0]);return m}
function post(m,lab,cut){const lp={};
 ORD.forEach(k=>{const q=SM[k].q;let l=0;
  ['w','s16','cu'].concat(lab?['caf','lip','suc']:[]).forEach(f=>{const mu=q[f][0],sd=q[f][1],z=(m[f]-mu)/sd;l+=-.5*z*z-Math.log(sd)});
  if(cut&&CUTL[cut])l+=Math.log(CUTL[cut][k]);lp[k]=l});
 const mx=Math.max(...ORD.map(k=>lp[k]));let t=0;const e={};ORD.forEach(k=>{e[k]=Math.exp(lp[k]-mx);t+=e[k]});
 return ORD.map(k=>({k,p:e[k]/t})).sort((a,b)=>b.p-a.p)}
function calc(){let V;
 if(st.mode==='ref')V={vis:st.k,m:means(st.k),cut:SM[st.k].sh.cut,lab:true,am:11.8,name:SM[st.k].n};
 else if(st.mode==='myst')V={vis:st.hid,m:st.mm,cut:SM[st.hid].sh.cut,lab:true,am:st.am,name:st.rev?SM[st.hid].n:'Mẫu bí ẩn số '+st.myN};
 else V={vis:null,m:st.own,cut:st.cut,lab:st.lab,am:12,name:'Lô của bạn'};
 const P=post(V.m,V.lab,V.cut);R={V,P,t:P[0]};return R}
const S_=()=>R.V.vis?SM[R.V.vis]:null;
isOff=i=>st.mode==='own'&&(i===1||i===2||i===7||(i===6&&!st.lab)||(i===3&&!st.cut));
function bins(){const V=R.V,m=V.m,b=V.vis?SM[V.vis].dist:null;
 if(st.mode==='ref')return b.slice();
 const r18=b?b[0]/(b[0]+b[1]):clamp((m.w-12)/16,.04,.75),r13=b?b[2]/((b[2]+b[3])||1):.85,s=clamp(m.s16,0,100);
 return [s*r18,s*(1-r18),(100-s)*r13,(100-s)*(1-r13)]}

/* ====== HÌNH NHÂN ====== */
function beanG(sh,cx,cy,L){const a=sh.a,Wd=L/a,n=64,pt=sh.pt||0,p=[];
 for(let i=0;i<n;i++){const t=i/n*Math.PI*2,c=Math.cos(t),s=Math.sin(t),pw=1+pt*Math.max(0,-s);
  let x=Wd/2*Math.sign(c)*Math.pow(Math.abs(c),pw)*(1+.07*s)*(1+(sh.asym||0)*(c>0?1:-.6)*Math.max(0,-s));const y=L/2*s;
  if(sh.hook)x+=Wd*.3*Math.pow(Math.max(0,-s),5)
  p.push([cx+x,cy+y])}
 let g=`<polygon class="cbn" points="${p.map(q=>q.map(f1).join(',')).join(' ')}"/>`;
 const T=L*.37;
 if(sh.cut==='p')g+=`<ellipse class="cbh" cx="${f1(cx-Wd*.12)}" cy="${f1(cy-L*.1)}" rx="${f1(Wd*.26)}" ry="${f1(L*.3)}"/><path class="cbc" d="M${f1(cx-Wd*.06)} ${f1(cy-L*.42)}C${f1(cx+Wd*.34)} ${f1(cy-L*.15)} ${f1(cx+Wd*.34)} ${f1(cy+L*.15)} ${f1(cx-Wd*.06)} ${f1(cy+L*.42)}"/>`;
 else{g+=`<ellipse class="cbh" cx="${f1(cx-Wd*.22)}" cy="${f1(cy-L*.1)}" rx="${f1(Wd*.11)}" ry="${f1(L*.22)}"/>`;
  if(sh.cut==='t')g+=`<path class="cbc" d="M${f1(cx+.4)} ${f1(cy-T)}Q${f1(cx+1.4)} ${f1(cy)} ${f1(cx+.4)} ${f1(cy+T)}"/>`;
  else if(sh.cut==='s')g+=`<path class="cbc" d="M${f1(cx)} ${f1(cy-T)}C${f1(cx+Wd*.3)} ${f1(cy-T*.35)} ${f1(cx-Wd*.3)} ${f1(cy+T*.35)} ${f1(cx)} ${f1(cy+T)}"/>`;
  else{const J=[.05,-.03,.045,-.05,.02,-.04,.05,-.02,.035,-.03,0];let d=`M${f1(cx+(sh.hook?Wd*.08:0))} ${f1(cy-T)}`;for(let k=1;k<=10;k++){const yy=cy-T+2*T*k/10,xx=cx+(sh.hook?Wd*.08*(1-k/10):0)+J[k]*Wd+(sh.asym||0)*Wd*.18*Math.sin(k/10*Math.PI);d+=`L${f1(xx)} ${f1(yy)}`}g+=`<path class="cbc" d="${d}"/>`}}
 return g}

/* ====== 8 TRẠM ====== */
const ST=[
 {n:'Vườn và cây',sub:()=>S_()?S_().tc:'chưa xem vườn',offNote:'chưa có quan sát',
  mech:'Bằng chứng đầu tiên nằm ngoài vườn. Cây mọc từ hạt (thực sinh) mỗi cây một dáng, lá và trái khác nhau; cây ghép giống nhau như đúc vì cùng một dòng. Arabica là cây bụi lá nhỏ, bóng; Liberica và Excelsa là cây gỗ cao, lá to, dày.',
  check:'Nhìn gốc: vết ghép là một gờ hay chỗ lệch thân gần mặt đất. Đi một hàng 20 cây: dáng, lá, trái khác nhau nhiều là dấu hiệu cây thực sinh.',
  kv:()=>{const S=S_();return S?[['Nhân giống',S.prop],['Cây',S.tree],['Vùng',S.alt]]:[['Quan sát','Chưa có. Điền ở Máy nhận diện bằng giác quan.']]},
  fail:'Tin lời “cây Sẻ” mà không xem vườn. Nhân đã rời vườn thì phân tích hóa học cũng khó tách Cà Sẻ với cao sản.',
  tip:'Vườn MeDili canh tác từ năm 2010, cây 15 năm tuổi, chăm sóc theo hướng tự nhiên; mỗi lô ghi mã vườn.'},
 {n:'Trái chín',sub:()=>S_()?'Trái · '+S_().cc:'chưa xem trái',offNote:'chưa có quan sát',
  mech:'Trái cho thêm manh mối. Robusta trái nhỏ, mọc thành chùm dày dọc cành; Arabica mỗi đốt ít trái hơn; Liberica trái to, vỏ dày, nhiều thịt quả. Dòng ghép cao sản trái to và đều; cây thực sinh trái khác nhau giữa các cây.',
  check:'Lấy 100 trái chín ngẫu nhiên, ghi màu, cỡ, số trái mỗi chùm. Trái xanh lẫn nhiều làm nhân nhỏ, nhẹ, dễ đoán sai giống.',
  kv:()=>{const S=S_();return S?[['Trái',S.cher],['Mùa hái',S.har]]:[['Quan sát','Chưa có.']]},
  fail:'Đoán giống theo màu trái: cùng một giống, màu khi chín đổi theo độ chín và nắng.',
  tip:'MeDili hái nhiều lượt từ tháng 11 tới đầu tháng 1, trái xanh tối đa 5%. Xem Cỗ máy Trái chín.'},
 {n:'Bàn soi nhân',sub:()=>R.V.cut?CUTN[R.V.cut]:'chưa soi',offNote:'chọn kiểu rãnh ở khung bên phải',
  mech:'Mặt phẳng của nhân là chỗ dễ đọc nhất. Robusta: nhân tròn ngắn, rãnh giữa thẳng. Arabica: nhân dẹt, thuôn, rãnh cong chữ S. Liberica: to, lệch, đầu nhọn có móc, rãnh nhăn. Culi: tròn đều, không có mặt phẳng.',
  check:'Rải 100 nhân trên nền sáng, lật mặt phẳng lên, đếm theo bốn nhóm: rãnh thẳng, chữ S, nhăn lệch, hạt tròn.',
  kv:()=>{const S=S_();return [['Dáng nhân',S?S.bean:'—'],['Rãnh giữa',R.V.cut?CUTN[R.V.cut]:'chưa soi'],['Dài, ước',S?vn(S.Lmm,1)+NB+'mm':'—']]},
  fail:'Dựa vào màu nhân xanh: màu đổi theo sơ chế, độ ẩm và thời gian kho, không theo giống.',
  tip:'Đếm luôn hạt lạ. Theo TCVN 4193, Robusta hạng 1 chỉ được lẫn tối đa 3% Arabica và 0,5% cà phê mít.'},
 {n:'Sàng phân cỡ',sub:()=>`Trên sàng 16: ${vn(R.V.m.s16,0)}%`,
  mech:'Sàng lỗ tròn chia nhân theo bề ngang: sàng 18 lỗ 7,10 mm, sàng 16 lỗ 6,30 mm, sàng 13 lỗ 5,00 mm. Các dòng TR trồng ở Lâm Đồng có 87–99% nhân nằm trên sàng 16; Cà Sẻ nhân nhỏ nên phần lớn nằm ở sàng 13–16.',
  check:'Mẫu 300 g, lắc chồng sàng 2–3 phút, cân từng tầng rồi chia cho tổng.',
  kv:()=>{const d=bins();return [['Trên sàng 18',vn(d[0],0)+'%'],['Sàng 16–18',vn(d[1],0)+'%'],['Sàng 13–16',vn(d[2],0)+'%'],['Lọt sàng 13',vn(d[3],0)+'%']]},
  fail:'Đem lô đã sàng lấy nhân nhỏ ra so: lô nhân nhỏ của cao sản cũng toàn nhân nhỏ.',
  tip:'Ghi phân bố cỡ nhân mỗi vụ để có số chuẩn riêng cho Cà Sẻ của vườn.'},
 {n:'Cân 100 nhân',sub:()=>`${vn(R.V.m.w,1)}${NB}g mỗi 100 nhân`,
  mech:'Khối lượng 100 nhân gộp cả cỡ và độ chắc. Trong các thí nghiệm giống, các dòng TR trồng ở Lâm Đồng nặng 19,2–29,6 g; cũng các dòng TR4, TR9, TR11 ở Gia Lai chỉ 15,3–17 g. Cà Sẻ ước 13–17 g; Moka khoảng 10–13 g; Liberica khoảng 21 g.',
  check:'Đếm 100 nhân nguyên, không vỡ, cân 3 lần lấy trung bình. Nhân phải khô tới độ ẩm 12,5% trở xuống mới so được.',
  kv:()=>{const w=R.V.m.w,ref=SM.se.q.w[0],d=(w/ref-1)*100;return [['100 nhân',vn(w,1)+NB+'g'],['So với Cà Sẻ',(d>=0?'+':'−')+vn(Math.abs(d),0)+'%'],['Độ ẩm',vn(R.V.am,1)+'% (tối đa 12,5)']]},
  fail:'So nhân ẩm với nhân khô: nhân ẩm nặng hơn.',
  tip:'Chỉ so với cao sản trồng cùng vùng, cùng vụ; khác vùng thì cỡ nhân đổi rất nhiều.'},
 {n:'Phòng thí nghiệm',sub:()=>R.V.lab?`Caffeine ${vn(R.V.m.caf,1)}%`:'chưa gửi mẫu',offNote:'chưa có kết quả',
  mech:'Phòng thí nghiệm tách loài rất tốt: Robusta có caffeine gần gấp đôi Arabica, ít dầu và ít đường hơn. Chất 16-O-methylcafestol (16-OMC) có nhiều trong Robusta, khoảng 600–1.800 mg/kg, còn Arabica chỉ có vết, nên dùng để phát hiện Robusta trộn vào Arabica. Trong cùng loài, như Cà Sẻ với cao sản, các chỉ số này chồng lên nhau.',
  check:'HPLC đo caffeine và 16-OMC; NMR phát hiện được từ khoảng 1–3% Robusta trộn trong Arabica. Muốn định danh dòng thì xét nghiệm DNA.',
  kv:()=>{const m=R.V.m,S=S_();return R.V.lab?[['Caffeine',vn(m.caf,2)+'%'],['Chất béo',vn(m.lip,1)+'%'],['Sucrose',vn(m.suc,1)+'%'],['16-OMC',S?S.omc:(m.caf>1.7?'nhiều khả năng cao':'nhiều khả năng chỉ có vết')]]:[['Kết quả','Chưa có. Bật “Có kết quả phòng thí nghiệm”.']]},
  fail:'Dùng caffeine để chứng minh “Sẻ thật”. Caffeine của Robusta đổi theo vùng, độ chín, năm; không có ngưỡng nào tách giống trong cùng loài.',
  tip:'Hằng ngày MeDili dùng cân, sàng và nếm; gửi phòng thí nghiệm khi khách cần chứng nhận.'},
 {n:'Bàn nếm',sub:()=>{const S=S_();return S?(/^(Fine|SCA)/.test(S.scale)?'Thang '+S.scale:S.scale):'chưa nếm'},offNote:'chưa có quan sát',
  mech:'Nếm cho biết chất lượng, gu và gợi ý loài: Robusta đắng, thân dày, ít chua; Arabica chua thanh, thơm; Liberica mùi mít chín, trái nhiệt đới. Robusta chấm theo thang Fine Robusta, từ 80 điểm là Fine; Arabica chấm theo thang SCA.',
  check:'Rang sáng đến vừa, cùng một hồ sơ rang cho mọi mẫu, nghỉ 8–24 giờ, 5 ly mỗi mẫu, nếm mù.',
  kv:()=>{const S=S_();if(!S)return [['Quan sát','Chưa có. Điền ở Máy nhận diện bằng giác quan.']];const p=S.prof;return [['Mùi vị',S.notes],['Thang chấm',S.scale],['Cường độ',`đắng ${g1(p[3])}, chua ${g1(p[1])}, thân ${g1(p[4])} trên 10`]]},
  fail:'Nếm mẫu rang đậm: rang đậm che mất khác biệt giữa các giống.',
  tip:'Ghi phiếu theo Bánh xe hương MeDili.'},
 {n:'Bộ quyết định',sub:()=>`${SM[R.t.k].s} · ${pc(R.t.p)}%`,
  mech:'Máy ghép mọi số đo lại. Mỗi mẫu có một khoảng giá trị điển hình cho từng chỉ số; mẫu nào khớp nhiều chỉ số nhất thì xác suất cao nhất. Đây là mô hình minh họa; số đo thật có sai số và có vùng chồng lấn.',
  check:'Từ 80% trở lên: khá chắc. Từ 50 đến 80%: nghiêng về. Dưới 50%: cần thêm bằng chứng. Máy làm tròn tối đa 99%.',
  kv:()=>R.P.slice(0,3).map(o=>[SM[o.k].s,pc(o.p)+'%']),
  fail:'Coi kết quả của máy là chứng nhận. Với hai giống cùng loài, chỉ hồ sơ vườn và DNA mới chắc chắn.',
  tip:'Ghi kết quả vào Phiếu kiểm mẫu ở cuối trang.'}];
ST.forEach(s=>{s.l1='Trạm này đọc gì';s.l2='Làm tay thế nào'});

/* ====== DỰNG CẢNH ====== */
const ANCH=[null,[7.5,14,11],[21,13,5],[36,8,10.4],[52.5,12,6.5],[64.5,13,3],[77.5,11,6.3],[93,13,4.6],[110,12,7.8]];
const CHIP=[null,{x:150,y:12},{x:236,y:56},{x:330,y:100},{x:420,y:150},{x:500,y:196},{x:590,y:240},{x:676,y:290},{x:770,y:340}];
function buildScene(){
 let h=box(1,2.2,0,120,2.6,.6,['beltT','belt','belt2'])+`<polyline class="flowL" points="${pts([P(2,3.5,.62),P(120,3.5,.62)])}"/>`;
 h=bench(124,24,'Cỗ máy Phân biệt · Vườn Di Linh',44)+h;
 /* 1 vườn */
 let s=box(3,9.5,0,9,9,2,['soilT','soil','soil2'])+'<g id="tree"></g>';h+=stG(1,s);
 /* 2 trái */
 s=box(17,9,0,8,8,2.6,['ped','ped2','ped3'])+'<g id="cher"></g>'+lcd(17.4,17,2.4,54,'kTr');h+=stG(2,s);
 /* 3 bàn soi */
 s=box(30.5,7.2,0,11,1,10.6,['pnl','pnl2','pnl3'])+`<g transform="${face(31.1,8.2,10.1)}"><rect class="pnlF" x="0" y="0" width="64" height="52" rx="3"/><g id="bean"></g></g>`;
 s+=box(29.5,9.4,0,14,8.6,2.2,['lbx','lbx2','lbx3'])+'<g id="beans"></g>'+lcd(30.2,18,1.95,66,'kSo');h+=stG(3,s);
 /* 4 sàng */
 s='';[0,1.1,2.2].forEach((z,i)=>s+=cyl(52.5,9.3,z,3.2,1.1,i%2?'sv2':'sv1',i%2?'sv2t':'sv1t'));
 [47.8,51.2,54.6,58].forEach((x,i)=>{const q=P(x,14.8,6.3);s+=cyl(x,14.8,0,1,6,'gl','glt')+`<g id="bf${i}"></g>`+`<text class="wtx" x="${f1(q[0])}" y="${f1(q[1]-5)}" text-anchor="middle" style="font-size:8px">${['18','16','13','<13'][i]}</text>`});
 s+=box(46.4,16.4,0,13.2,1.8,1.7,['ped','ped2','ped3'])+lcd(47.2,18.2,1.55,70,'kSa');h+=stG(4,s);
 /* 5 cân */
 s=box(61,10,0,7.5,6,1.6,['ped','ped2','ped3'])+cyl(64.75,13,1.6,2.3,.35,'cu2','plt')+'<g id="pile"></g>'+lcd(61.4,16,1.5,48,'kW');
 s+=box(66.8,17,0,3.6,2.4,2.4,['ped','ped2','ped3'])+cyl(68.6,18.2,2.4,.2,2.4,'cu2','cu2')+lcd(66.95,19.4,2.2,24,'kAm');h+=stG(5,s);
 /* 6 lab */
 s=box(72,8,0,11,6,5.6,['ins','ins2','ins3'])+lcd(72.5,14,5.15,72,'kLab')+lcd(72.5,14,3.55,72,'kOMC')+'<g id="lampG"></g>';
 s+=box(73.5,15.4,0,8,2.4,.9,['ped','ped2','ped3']);[0,1,2,3].forEach(i=>s+=cyl(74.8+i*1.9,16.6,.9,.42,2.3,'vial','vialT')+`<g id="vl${i}"></g>`);h+=stG(6,s);
 /* 7 bàn nếm */
 s=box(86.5,9,0,13,8,3,['wo','wo2','cu2']);[0,1,2,3,4].forEach(i=>{const x=88.4+i*2.35;s+=cyl(x,12.6,3,.85,1.15,'cup','cupT');const q=P(x,12.6,4.4);s+=`<path class="stm" d="M${f1(q[0]-2)} ${f1(q[1]-2)}c-3 -4 3 -6 0 -10s3 -6 0 -9" style="fill:none;stroke:#B9A274;stroke-width:1.3;animation-delay:${i*.3}s"/>`});
 s+=lcd(87,17,2.8,62,'kCup');h+=stG(7,s);
 /* 8 quyết định */
 s=box(103.5,8,0,13,8,7.6,['cab','cab2','cab3'])+`<g transform="${face(104.2,16,7.1)}"><rect x="0" y="0" width="84" height="34" rx="3" style="fill:#2E1C12"/><g id="bars"></g></g>`+lcd(104.2,16,2.15,84,'kOut')+'<g id="lamp8"></g>';h+=stG(8,s);
 h+='<g id="flow"></g><g id="chips"></g><circle id="tok" r="7"/>';
 $('scene').innerHTML=h;['kTr','kSo','kSa','kW','kAm','kLab','kOMC','kCup','kOut'].forEach(i=>$(i).classList.add('sm'));initStations()}
function treeSVG(k){const T=SM[k].tv,cx=7.5,cy=14,z0=2,g=rng(T.seed);let s='';
 const offs=T.t===3?[[-1,.6],[.9,-.5],[.2,1.2]]:T.t===2?[[-.6,.3],[.6,-.3]]:[[0,0]];
 offs.forEach(([dx,dy],i)=>s+=cyl(cx+dx,cy+dy,z0,T.tw||.3,T.h*(T.t>1?(.82+.12*i):1),'trk','trk'));
 if(T.gr)s+=cyl(cx,cy,z0+.55,(T.tw||.3)+.18,.35,'grf','grf');
 const top=P(cx,cy,z0+T.h),Rx=T.cr*U*1.05,bl=[];
 if(T.tier){for(let j=0;j<3;j++){const yy=top[1]-6+j*13,w=Rx*(.5+j*.32);for(let i=-2;i<=2;i++)bl.push([top[0]+i*w/2.4,yy+Math.abs(i)*3.2,T.lr*(1-j*.06),T.lr*.5])}}
 else if(T.hedge){for(let j=0;j<2;j++)for(let i=-3;i<=3;i++)bl.push([top[0]+i*Rx/3.3+(j?Rx/6.6:0),top[1]-2+j*8,T.lr,T.lr*.82])}
 else{for(let i=0;i<T.n;i++){const a=i/T.n*Math.PI*2+g()*.6,rr=(T.ir?(.38+g()*.62):.6)*Rx;bl.push([top[0]+Math.cos(a)*rr,top[1]+Math.sin(a)*rr*.55-(T.ir?g()*T.lr*.6:0),T.lr*(.8+g()*.45),T.lr*(.8+g()*.45)*.8])}
  bl.push([top[0],top[1]-5,T.lr*1.15,T.lr*.95])}
 bl.sort((a,b)=>a[1]-b[1]).forEach(([x,y,rx,ry],i)=>s+=`<ellipse class="${['can1','can2','can3'][i%3]}" cx="${f1(x)}" cy="${f1(y)}" rx="${f1(rx)}" ry="${f1(ry)}"/>`);
 if(T.br)bl.slice(0,5).forEach(([x,y,rx])=>s+=`<circle cx="${f1(x+rx*.6)}" cy="${f1(y-2)}" r="2.6" style="fill:#C9783A"/>`);
 return s}
function cherSVG(k){const C=SM[k].cv,q=P(21,13,2.6),g=rng(C.n*7+3);
 let s=`<path d="M${f1(q[0]-26)} ${f1(q[1]-20)}Q${f1(q[0])} ${f1(q[1]-34)} ${f1(q[0]+26)} ${f1(q[1]-18)}" style="fill:none;stroke:#6B4226;stroke-width:3.2;stroke-linecap:round"/>`;
 const nodes=C.cl===3?[.18,.5,.82]:[.3,.72];
 nodes.forEach((t,j)=>{const nx=q[0]-26+52*t,ny=q[1]-20-11*Math.sin(t*Math.PI)+(t-.5)*4,cnt=Math.floor(C.n/nodes.length)+(j<C.n%nodes.length?1:0);
  for(let c=0;c<cnt;c++){const a=c/cnt*Math.PI*2+g()*.5,rr=cnt>1?C.r*1.05:0,x=nx+Math.cos(a)*rr,y=ny+Math.sin(a)*rr*.75+C.r*.7;
   s+=`<circle cx="${f1(x)}" cy="${f1(y)}" r="${C.r}" style="fill:${C.cols[Math.floor(g()*C.cols.length)]}"/><circle cx="${f1(x-C.r*.35)}" cy="${f1(y-C.r*.35)}" r="${f1(C.r*.28)}" style="fill:#FFF6EC;opacity:.55;stroke:none"/>`}});
 return s}
function renderScene(){const V=R.V,m=V.m,S=S_();
 const qm=(x,y,z)=>{const q=P(x,y,z);return `<text class="qm" x="${f1(q[0])}" y="${f1(q[1])}" text-anchor="middle">?</text>`};
 $('tree').innerHTML=S?treeSVG(V.vis):qm(7.5,14,5);
 $('cher').innerHTML=S?cherSVG(V.vis):qm(21,13,5.4);
 const sh=S?{...S.sh}:{a:1.3,asym:.04,hook:0,pt:0,cut:V.cut},Lmm=S?S.Lmm:clamp(11.46*Math.cbrt(m.w*1.69)/3.703,6,13);
 if(V.cut)sh.cut=V.cut;
 $('bean').innerHTML=(S||V.cut)&&st.step>=3?beanG(sh,32,26,Lmm*3.6):`<text x="32" y="36" text-anchor="middle" class="qm">?</text>`;
 let bb='';if(S||V.cut){const g=rng(5),l=Lmm*.95,rx=l*.55,ry=l*.55/sh.a;for(let i=0;i<7;i++){const q=P(31.5+g()*10,10.6+g()*6,2.2);bb+=`<g transform="translate(${f1(q[0])} ${f1(q[1])}) rotate(${f1(-30+g()*60)}) scale(1 .62)"><ellipse rx="${f1(rx)}" ry="${f1(ry)}" style="fill:#D8C79C;stroke:#8D6A45;stroke-width:.9"/>${sh.cut==='p'?'':`<line x1="${f1(-rx*.7)}" x2="${f1(rx*.7)}" y1="0" y2="0" style="stroke:#6B4226;stroke-width:1"/>`}</g>`}}
 $('beans').innerHTML=bb;
 const d=bins();d.forEach((v,i)=>{const hgt=clamp(v/100*6*1.35,.05,6);$('bf'+i).innerHTML=st.step>=4?cyl(47.8+i*3.4,14.8,0,.86,hgt,'bnf','bnft'):''});
 let pl='';const gp=rng(9);for(let i=0;i<9;i++){const q=P(64.75+(gp()-.5)*2.4,13+(gp()-.5)*2.4,1.95);pl+=`<ellipse cx="${f1(q[0])}" cy="${f1(q[1]-2)}" rx="3.2" ry="2.2" style="fill:#D8C79C"/>`}$('pile').innerHTML=pl;
 const Lc=(id,t,i)=>{$(id).textContent=st.step>=i?t:'···'};
 Lc('kTr',S?S.cc:'chưa xem',2);Lc('kSo',V.cut?CUTS[V.cut]:'chưa soi',3);Lc('kSa','trên S16: '+vn(m.s16,0)+'%',4);
 Lc('kW',vn(m.w,1)+' g',5);Lc('kAm',vn(V.am,1)+'%',5);
 Lc('kLab',V.lab?`caf ${vn(m.caf,1)} · béo ${vn(m.lip,0)}`:'chưa đo',6);
 Lc('kOMC',V.lab?'16-OMC: '+(S?S.omcS:(m.caf>1.7?'cao':'vết')):'16-OMC: ?',6);
 Lc('kCup',S?`đắng ${g1(S.prof[3])} · chua ${g1(S.prof[1])}`:'chưa nếm',7);
 Lc('kOut',`${SM[R.t.k].s} ${pc(R.t.p)}%`,8);
 const hi=V.lab&&(S?S.grp==='R':m.caf>1.7);$('lampG').innerHTML=sph(81.6,11,5.6,.72,hi&&st.step>=6?'lampOn':'lampOff');
 [0,1,2,3].forEach(i=>$('vl'+i).innerHTML=V.lab&&st.step>=6?cyl(74.8+i*1.9,16.6,.95,.34,1.1+i*.2,'#8D5A32','#A9743F'):'');
 let b='';if(st.step>=8)R.P.slice(0,3).forEach((o,i)=>{const y=4+i*10;b+=`<text class="bt" x="4" y="${y+6}" style="fill:#F3D9A4">${SM[o.k].s}</text><rect x="34" y="${y}" width="44" height="6.5" rx="2" class="bbg" style="fill:#5A3E2A"/><rect x="34" y="${y}" width="${f1(Math.max(1.5,o.p*44))}" height="6.5" rx="2" style="fill:${SM[o.k].c}"/>`});
 $('bars').innerHTML=b;$('lamp8').innerHTML=sph(114.6,10,7.6,.6,st.step>=8?'lampOn':'lampOff');
 drawFlow();drawChips()}
function chipLabel(i){const V=R.V,m=V.m,S=S_();
 if(st.step<i)return ['','Vườn','Trái','Bàn soi','Sàng','Cân','Phòng lab','Bàn nếm','Kết luận'][i]+' · ···';
 return ['','Vườn · '+(S?S.tc:'chưa xem'),'Trái · '+(S?S.cc:'chưa xem'),'Nhân · '+(V.cut?CUTN[V.cut]:'chưa soi'),'Sàng 16+ · '+vn(m.s16,0)+'%','100 nhân · '+vn(m.w,1)+NB+'g',
  V.lab?'Caffeine · '+vn(m.caf,1)+'%':'Lab · chưa đo','Nếm · '+(S?S.cupS:'chưa nếm'),'Kết luận · '+SM[R.t.k].s+' '+pc(R.t.p)+'%'][i]}
function drawFlow(){const V=R.V,m=V.m;
 const rows=[['Chế độ',st.mode==='ref'?'Hồ sơ chuẩn':st.mode==='myst'?'Mẫu bí ẩn':'Số đo của bạn'],['Mẫu',V.name],['100 nhân',vn(m.w,1)+NB+'g'],['Trên sàng 16',vn(m.s16,0)+'%'],['Hạt tròn',vn(m.cu,0)+'%'],['Caffeine',V.lab?vn(m.caf,2)+'%':'chưa đo'],['Máy kết luận',`${SM[R.t.k].s} · ${pc(R.t.p)}%`]];
 const X=16,rh=27,h=50+rows.length*rh+20,y=712-h,w=330;
 let g=`<rect x="${X}" y="${y}" width="${w}" height="${h}" rx="10" class="pa" style="stroke:var(--ink);stroke-width:1.2"/><text x="${X+16}" y="${y+26}" class="lab12" style="letter-spacing:.08em">MẪU TRONG MÁY</text>`;
 rows.forEach(([a,b],i)=>{const yy=y+48+i*rh;g+=`<text class="flowT" x="${X+16}" y="${yy+4}">${a}</text><text x="${X+w-16}" y="${yy+4}" text-anchor="end" class="mono flowT">${b}</text>`});
 g+=`<text x="${X+16}" y="${y+h-10}" class="tiny mutedt">Bản vẽ khái niệm · mô hình minh họa</text>`;$('flow').innerHTML=g}

/* ====== ĐIỀU KHIỂN ====== */
function halt(){stopRun();st.step=8}
function toOwn(){if(st.mode!=='own'){st.own={...R.V.m};st.cut=R.V.cut;st.lab=R.V.lab;st.mode='own';st.rev=false}}
function mystery(){const r=Math.random,k=ORD[Math.floor(r()*ORD.length)],q=SM[k].q,m={};
 const lim={w:[9,31],s16:[10,100],cu:[0,100],caf:[.4,3],lip:[6,19],suc:[1.5,10]};
 FE.forEach(f=>m[f]=clamp(q[f][0]+q[f][1]*gauss(r)*.9,lim[f][0],lim[f][1]));
 st.hid=k;st.mm=m;st.am=10.8+r()*1.6;st.mode='myst';st.rev=false;st.myN++}
function sliders(){const m=R.V.m;
 [['iW','oW','w',1],['iS','oS','s16',0],['iC','oC','cu',0],['iCa','oCa','caf',2],['iL','oL','lip',1],['iSu','oSu','suc',1]].forEach(([i,o,f,d])=>{$(i).value=m[f];$(o).textContent=vn(m[f],d)+'%'.replace('%',f==='w'?'g':'%')});
 $('lab').checked=R.V.lab;$('labBox').hidden=!R.V.lab;
 $('modeL').textContent=st.mode==='ref'?'hồ sơ chuẩn của '+SM[st.k].s:st.mode==='myst'?'máy đo mẫu bí ẩn':'bạn đang nhập'}
function stats(){const m=R.V.m,t=(a,b)=>`<div class="stat"><span>${a}</span><b>${b}</b></div>`;
 $('stats').innerHTML=t('100 nhân',vn(m.w,1)+NB+'g')+t('Trên sàng 16',vn(m.s16,0)+'%')+t('Caffeine',R.V.lab?vn(m.caf,1)+'%':'chưa đo')+t('Máy kết luận',SM[R.t.k].s)}
function verdict(){const P=R.P,t=P[0],t2=P[1],S1=SM[t.k];let cls=t.p>=.8?'good':t.p>=.5?'warn':'bad',hd;
 if(st.mode==='myst'&&st.rev){const ok=t.k===st.hid;cls=ok?'good':'bad';hd=(ok?'✓ Máy đoán đúng: ':'✕ Máy đoán sai: ')+'đáp án là '+SM[st.hid].n}
 else hd=`${t.p>=.8?'✓':'!'} ${st.mode==='myst'?'Máy đoán':'Gần nhất'}: ${S1.n} · ${pc(t.p)}%`;
 const bars=P.slice(0,3).map(o=>`<div class="pbar"><span>${SM[o.k].n}</span><b>${pc(o.p)}%</b><i><em style="width:${f1(Math.max(1,o.p*100))}%;background:${SM[o.k].c}"></em></i></div>`).join('');
 let msg='';if(t.p<.5)msg='Chưa đủ bằng chứng. ';
 if(!R.V.lab&&S1.grp!==SM[t2.k].grp&&t2.p>.15)msg+='Thêm kết quả phòng thí nghiệm hoặc soi rãnh giữa để tách loài. ';
 if(S1.grp===SM[t2.k].grp&&t2.p>.15)msg+=`${S1.s} và ${SM[t2.k].s} cùng loài: cần hồ sơ vườn, nếm hoặc DNA. `;
 if(st.mode==='myst'&&st.rev&&t.k!==st.hid)msg+='Số đo của mẫu này rơi vào vùng chồng lấn; ngoài đời cũng vậy.';
 $('verdict').className=cls;$('verdict').innerHTML=`<b>${hd}</b>${bars}${msg?`<p style="margin:8px 0 0">${msg}</p>`:''}`}
function drawM(){const W=340,H=200,l=30,r=10,t=20,b=22,x0=9,x1=27,y0=.4,y1=3,X=x=>l+(x-x0)/(x1-x0)*(W-l-r),Y=y=>t+(1-(y-y0)/(y1-y0))*(H-t-b);
 let g=`<text class="ttl" x="${l}" y="12">Caffeine % · trục ngang: 100 nhân (g)</text>`;
 [1,2,3].forEach(v=>g+=`<line x1="${l}" x2="${W-r}" y1="${f1(Y(v))}" y2="${f1(Y(v))}" style="stroke:var(--rule);stroke-width:.8"/><text x="${l-5}" y="${f1(Y(v)+3.5)}" text-anchor="end">${v}</text>`);
 [10,15,20,25].forEach(v=>g+=`<text x="${f1(X(v))}" y="${H-5}" text-anchor="middle">${v}</text>`);
 ORD.forEach(k=>{const q=SM[k].q,c=SM[k].c;g+=`<ellipse cx="${f1(X(q.w[0]))}" cy="${f1(Y(q.caf[0]))}" rx="${f1(X(q.w[0]+q.w[1])-X(q.w[0]))}" ry="${f1(Y(q.caf[0])-Y(q.caf[0]+q.caf[1]))}" style="fill:${c};fill-opacity:.16;stroke:${c};stroke-width:1.2"/>`});
 ORD.forEach(k=>{const q=SM[k].q,o=SM[k].lo;g+=`<text x="${f1(X(q.w[0])+o[0])}" y="${f1(Y(q.caf[0])+o[1])}" text-anchor="middle" style="fill:var(--ink);font:600 10px var(--body);paint-order:stroke;stroke:var(--panel);stroke-width:3px;stroke-linejoin:round">${SM[k].s}</text>`});
 const m=R.V.m,x=X(clamp(m.w,x0,x1));
 if(R.V.lab)g+=`<circle cx="${f1(x)}" cy="${f1(Y(clamp(m.caf,y0,y1)))}" r="5" style="fill:var(--ink);stroke:var(--panel);stroke-width:2"/>`;
 else g+=`<line x1="${f1(x)}" x2="${f1(x)}" y1="${t}" y2="${H-b}" style="stroke:var(--ink);stroke-width:1.4;stroke-dasharray:4 3"/>`;
 $('cM').innerHTML=g;
 $('mTip').textContent=R.V.lab?'Chấm đậm là mẫu đang đo. Trục dọc tách loài: Robusta nằm trên. Trục ngang tách cỡ nhân trong cùng loài: Cà Sẻ bên trái, cao sản bên phải.':'Chưa có caffeine nên máy chỉ biết cỡ nhân (vạch đứt). Bật kết quả phòng thí nghiệm để tách loài.'}
function figsub(){$('figsub').textContent=`${R.V.name} · máy kết luận: ${SM[R.t.k].s} ${pc(R.t.p)}%`}
function sNote(){const S=SM[st.k];
 $('sNote').innerHTML=st.mode==='ref'?`<b>${S.n}</b> · ${S.sp}. ${S.prop}.`:st.mode==='myst'?(st.rev?`Đáp án: <b>${SM[st.hid].n}</b>. Bấm Mẫu bí ẩn để thử mẫu khác.`:'Máy đang đo một mẫu chưa biết tên. Xem từng trạm, đoán trước, rồi bấm Lộ đáp án.'):'Bạn đang chỉnh số đo. Bấm một mẫu hoặc Về hồ sơ chuẩn để quay lại.';
 $('reveal').hidden=!(st.mode==='myst'&&!st.rev);$('back').hidden=st.mode==='ref'}
function update(){calc();
 pills('samps',ORD.map(k=>[k,SM[k].s]),st.mode==='ref'?st.k:'',k=>{halt();st.k=k;st.mode='ref';st.rev=false;update()});
 pills('cuts',[['','Chưa soi'],['t','Thẳng'],['s','Chữ S'],['r','Nhăn, lệch'],['p','Tròn, culi']],R.V.cut||'',k=>{halt();toOwn();st.cut=k||null;update()});
 sNote();sliders();stats();verdict();renderScene();drawM();renderStation();figsub();sheet()}
function runMachine(){stopRun();st.step=0;calc();renderScene();
 tour([1,2,3,4,5,6,7,8],600,k=>{st.step=k+1;renderScene();renderStation()})}
const onS=(id,f)=>$(id).addEventListener('input',()=>{halt();toOwn();st.own[f]=+$(id).value;if(['caf','lip','suc'].includes(f))st.lab=true;update()});
onS('iW','w');onS('iS','s16');onS('iC','cu');onS('iCa','caf');onS('iL','lip');onS('iSu','suc');
$('lab').addEventListener('change',()=>{halt();toOwn();st.lab=$('lab').checked;update()});
$('run').onclick=runMachine;$('run2').onclick=runMachine;
$('myst').onclick=()=>{halt();mystery();update();runMachine()};
$('reveal').onclick=()=>{halt();st.rev=true;update()};
$('back').onclick=()=>{halt();st.mode='ref';st.rev=false;update()};

/* ====== MÁY NHẬN DIỆN BẰNG GIÁC QUAN ====== */
function qz(){$('qz').innerHTML=QZ.map(q=>`<div class="qb"><b>${q.n}</b>${q.h?`<small>${q.h}</small>`:''}<div class="row">${q.o.map(o=>`<button class="pill" type="button" data-q="${q.id}" data-o="${o.id}" aria-pressed="${st.qa[q.id]===o.id}">${o.t}</button>`).join('')}</div></div>`).join('');
 $('qz').querySelectorAll('button').forEach(b=>b.onclick=()=>{const q=b.dataset.q,o=b.dataset.o;if(st.qa[q]===o)delete st.qa[q];else st.qa[q]=o;qz()});
 qres();sheet()}
function qres(){const ans=Object.entries(st.qa),lp={};ORD.forEach(k=>lp[k]=0);
 ans.forEach(([q,o])=>{const w=QZ.find(x=>x.id===q).o.find(x=>x.id===o).w;ORD.forEach(k=>lp[k]+=Math.log(w[k]))});
 const mx=Math.max(...ORD.map(k=>lp[k]));let t=0;const e={};ORD.forEach(k=>{e[k]=Math.exp(lp[k]-mx);t+=e[k]});
 const P=ORD.map(k=>({k,p:e[k]/t})).sort((a,b)=>b.p-a.p);st.qP=P;
 if(!ans.length){$('qzr').innerHTML='<span class="lbl">0/'+QZ.length+' câu</span><b class="qh">Chưa có quan sát</b><p class="mnote">Chọn ít nhất hai câu, hoặc bấm một mẫu ở dòng “Điền thử như mẫu”.</p>';return}
 const t1=P[0],t2=P[1];
 const why=ans.map(([q,o])=>{const O=QZ.find(x=>x.id===q).o.find(x=>x.id===o),w=O.w,oth=ORD.filter(k=>k!==t1.k).reduce((s,k)=>s+w[k],0)/7;return {t:O.t,r:w[t1.k]/oth}}).filter(x=>x.r>1.4).sort((a,b)=>b.r-a.r).slice(0,4);
 let nx='';if(t1.p-t2.p<.3){let best=null,bv=0;QZ.forEach(Q=>{if(st.qa[Q.id])return;const v=Math.max(...Q.o.map(O=>Math.abs(Math.log(O.w[t1.k]/O.w[t2.k]))));if(v>bv){bv=v;best=Q}});
  nx=best?`Để tách ${SM[t1.k].s} với ${SM[t2.k].s}, xem thêm: <b>${best.n.toLowerCase()}</b>.`:`${SM[t1.k].s} và ${SM[t2.k].s} còn sát nhau: cần cân, sàng hoặc hồ sơ vườn.`}
 const robNote=(t1.k==='se'||t1.k==='cs')?'<p class="mnote">Giữa Cà Sẻ và cao sản, giác quan chỉ gợi ý. Hãy cân 100 nhân và sàng ở cỗ máy phía trên, và hỏi hồ sơ vườn.</p>':'';
 $('qzr').innerHTML=`<span class="lbl">${ans.length}/${QZ.length} câu đã chọn</span><b class="qh">${t1.p>=.8?'Khá chắc':t1.p>=.5?'Nghiêng về':'Chưa rõ, gần nhất'}: ${SM[t1.k].n}</b>${P.slice(0,4).map(o=>`<div class="pbar"><span>${SM[o.k].n}</span><b>${pc(o.p)}%</b><i><em style="width:${f1(Math.max(1,o.p*100))}%;background:${SM[o.k].c}"></em></i></div>`).join('')}${why.length?`<span class="lbl" style="margin-top:12px">Dấu hiệu khớp ${SM[t1.k].s}</span><div class="why">${why.map(x=>`<span>${x.t}</span>`).join('')}</div>`:''}${nx?`<p class="mnote">${nx}</p>`:''}${robNote}`}
pills('qPre',ORD.map(k=>[k,SM[k].s]).concat([['x','Xóa hết']]),'',k=>{st.qa=k==='x'?{}:{...PRE[k]};qz()});

/* ====== HÌNH 2 ====== */
function drawR(){const W=cw('wR'),mob=W<640,H=mob?300:360,l=mob?36:48,r=mob?12:22,t=26,b=34,x0=13,x1=31,y0=54,y1=101,X=x=>l+(x-x0)/(x1-x0)*(W-l-r),Y=y=>t+(1-(y-y0)/(y1-y0))*(H-t-b);
 $('cR').setAttribute('viewBox',`0 0 ${W} ${H}`);
 let g=`<text class="ttl" x="${l}" y="14">${mob?'% nhân trên sàng 16 · ngang: g/100 nhân':'Phần trăm nhân trên sàng 16 · trục ngang: khối lượng 100 nhân (g)'}</text>`;
 [60,70,80,90,100].forEach(v=>g+=`<line x1="${l}" x2="${W-r}" y1="${f1(Y(v))}" y2="${f1(Y(v))}" style="stroke:var(--rule);stroke-width:.8"/><text x="${l-6}" y="${f1(Y(v)+4)}" text-anchor="end">${v}</text>`);
 (mob?[14,18,22,26,30]:[14,16,18,20,22,24,26,28,30]).forEach(v=>g+=`<text x="${f1(X(v))}" y="${H-b+18}" text-anchor="middle">${v}</text>`);
 g+=`<ellipse cx="${f1(X(15))}" cy="${f1(Y(62))}" rx="${f1(X(16.6)-X(15))}" ry="${f1(Y(62)-Y(71))}" style="fill:var(--k1);fill-opacity:.13;stroke:var(--k1);stroke-width:1.8;stroke-dasharray:6 4"/>`;
 ROB.forEach(([cl,rg,w,s])=>{g+=`<circle cx="${f1(X(w))}" cy="${f1(Y(s))}" r="${rg==='all'?7:5.5}" style="fill:${RG[rg][1]};stroke:var(--panel);stroke-width:1.6"><title>${cl} · ${RG[rg][0]}: ${vn(w,1)} g, ${vn(s,1)}%</title></circle>`});
 const lab=(x,y,txt,anc,c)=>`<text class="val" x="${f1(x)}" y="${f1(y)}" text-anchor="${anc}"${c?` style="fill:${c}"`:''}>${txt}</text>`;
 g+=mob?lab(X(16.8)+2,Y(57.5),'Cà Sẻ (ước)','start','var(--k1)'):lab(X(15)+4,Y(71)-10,'Cà Sẻ (ước)','middle','var(--k1)');
 g+=lab(X(15.7)+10,Y(65)+18,'TR4, TR11 · Gia Lai','start');
 g+=mob?lab(X(29.6)+4,Y(91),'TR9 · Lâm Đồng','end'):lab(X(29.6)-9,Y(99.2)+18,'TR9 · Lâm Đồng','end');
 g+=lab(X(19.1)+10,Y(85.3)+4,'TRS1','start');
 $('cR').innerHTML=g;
 legend('lgR',[{n:'Đắk Lắk',c:'var(--k2)',box:1},{n:'Gia Lai',c:'var(--k4)',box:1},{n:'Lâm Đồng',c:'var(--k3)',box:1},{n:'TRS1, trung bình 4 vùng',c:'var(--k5)',box:1},{n:'Cà Sẻ, ước của MeDili',c:'var(--k1)',d:1}])}

/* ====== HÌNH 3, ĐỐI CHIẾU CẶP, THAM SỐ ====== */
function gallery(){$('bgal').innerHTML=ORD.map(k=>{const S=SM[k],L=S.Lmm*7;return `<figure><svg viewBox="0 0 120 112" role="img" aria-label="Nhân xanh ${S.n}">${beanG(S.sh,60,50,L)}<line x1="12" x2="47" y1="104" y2="104" style="stroke:var(--muted);stroke-width:1.6"/><text x="12" y="99" style="font:600 9px var(--body);fill:var(--muted)">5 mm</text></svg><figcaption><b>${S.s}</b><span>${CUTN[S.sh.cut]} · dài ≈${NB}${vn(S.Lmm,1)}${NB}mm</span></figcaption></figure>`}).join('')}
const PROWS=[['Loài, nhóm','sp'],['Nhân giống','prop'],['Cây','tree'],['Trái','cher'],['Nhân xanh','bean'],['Rãnh giữa','cutT'],['Vùng, độ cao','alt'],['Mùi vị','notes'],['Thang chấm','scale'],['Năng suất','yld'],['Dễ nhầm với','conf']];
const PAIRS={'se|cs':'Nhìn vườn trước: cây thực sinh hay cây ghép. Rồi cân 100 nhân và sàng, so với cao sản trồng cùng vùng. Nếm: Cà Sẻ đậm, thân dày, hậu dài hơn. Cùng loài nên caffeine không tách được; muốn chắc chắn thì xét nghiệm DNA.',
 'se|culi':'Đếm hạt tròn trong 100 hạt. Lô Cà Sẻ chỉ có vài phần trăm hạt tròn; lô culi đã tách từ 90% trở lên. Culi lấy từ vườn Sẻ thì vẫn là Culi Sẻ.',
 'cs|culi':'Đếm hạt tròn trong 100 hạt. Lô hạt dẹt chỉ có vài phần trăm hạt tròn; lô culi đã tách từ 90% trở lên.',
 'ara|cat':'Dáng nhân gần như giống nhau. Hỏi giống trong vườn: Typica cao, cành ngang, lá non màu đồng; Catimor thấp, lóng ngắn. Nếm: Catimor hay có vị thảo mộc. Chắc chắn thì DNA.',
 'ara|mok':'Cân 100 nhân: Moka rất nhẹ, khoảng 10–13 g, nhân tròn như hạt đậu. Sản lượng ít nên giá cao; cẩn thận tên “Moka” gắn cho Arabica thường.',
 'cat|mok':'Cân 100 nhân: Moka rất nhẹ, khoảng 10–13 g, nhân tròn như hạt đậu; Catimor nhân thuôn, to hơn nhiều. Cây Catimor thấp nhưng sai trái, Moka cây nhỏ, ít trái.',
 'lib|exc':'Liberica nhân to hơn, dài, đầu nhọn có móc; Excelsa nhỏ hơn, dáng giọt nước, vỏ trấu mỏng hơn. Nếm: Liberica trái nhiệt đới, mít chín; Excelsa chua kiểu trái cây sẫm.'};
function pairText(a,b){const key=[a,b].sort((x,y)=>ORD.indexOf(x)-ORD.indexOf(y)).join('|');if(PAIRS[key])return PAIRS[key];
 const A=SM[a],B=SM[b];
 if(a==='culi'||b==='culi')return 'Culi là hình hạt, không phải giống: có Culi Robusta, có Culi Arabica. Trước hết đếm hạt tròn; rồi tách loài như với hạt dẹt: rãnh, caffeine, mùi vị.';
 if(a==='lib'||b==='lib')return 'Liberica nhân to, lệch, đầu nhọn có móc, rãnh nhăn; mùi mít chín rất riêng; caffeine thấp hơn Robusta. TCVN 4193 chỉ cho Robusta hạng 1 lẫn tối đa 0,5% cà phê mít.';
 if(a==='exc'||b==='exc')return 'Excelsa dáng giọt nước hơi lệch, rãnh hơi nhăn; vị chua kiểu trái cây, ít đắng, ngược hẳn Robusta.';
 if(a==='mok'||b==='mok')return 'Moka nhân rất nhỏ, tròn, rãnh cong; 100 nhân chỉ khoảng 10–13 g; thơm nồng, chua thanh, ít đắng.';
 if(A.grp!==B.grp)return 'Khác loài nên dễ tách. Robusta tròn ngắn, rãnh thẳng; Arabica dẹt, thuôn, rãnh chữ S. Phòng lab: Robusta caffeine gần gấp đôi, ít dầu, ít đường, nhiều 16-OMC. Nếm: Robusta đắng, thân dày; Arabica chua thanh, thơm.';
 return 'Cùng nhóm: so cỡ nhân, nếm và hỏi hồ sơ vườn.'}
function pair(){pills('pA',ORD.map(k=>[k,SM[k].s]),st.pa,k=>{st.pa=k;if(st.pb===k)st.pb=ORD.find(x=>x!==k);pair()});
 pills('pB',ORD.filter(k=>k!==st.pa).map(k=>[k,SM[k].s]),st.pb,k=>{st.pb=k;pair()});
 const A=SM[st.pa],B=SM[st.pb],PD={w:1,s16:0,caf:1,lip:0},qr=['w','s16','caf','lip'].map(f=>[FN[f][0]+', mô hình',vn(A.q[f][0],PD[f])+NB+FN[f][1],vn(B.q[f][0],PD[f])+NB+FN[f][1]]);
 $('pT').innerHTML=`<thead><tr><th></th><th><i class="sw" style="background:${A.c}"></i>${A.n}</th><th><i class="sw" style="background:${B.c}"></i>${B.n}</th></tr></thead><tbody>${PROWS.map(([n,f])=>`<tr><th>${n}</th><td>${A[f]}</td><td>${B[f]}</td></tr>`).join('')}${qr.map(([n,a,b])=>`<tr><th>${n}</th><td>${a}</td><td>${b}</td></tr>`).join('')}</tbody>`;
 $('pX').innerHTML=`<b>Cách tách nhanh nhất</b>${pairText(st.pa,st.pb)}`}
const sdf=v=>String(+(+v).toFixed(2)).replace('.',',');
function ptab(){$('pTab').innerHTML=`<thead><tr><th>Mẫu</th>${FE.map(f=>`<th>${FN[f][0]}, ${FN[f][1]}</th>`).join('')}<th>Rãnh giữa</th></tr></thead><tbody>${ORD.map(k=>`<tr><td><i class="sw" style="background:${SM[k].c}"></i>${SM[k].s}</td>${FE.map(f=>`<td>${sdf(SM[k].q[f][0])} ± ${sdf(SM[k].q[f][1])}</td>`).join('')}<td>${CUTN[SM[k].sh.cut]}</td></tr>`).join('')}</tbody>`}

/* ====== HÌNH 4 ====== */
function drawRad(){pills('rB',ORD.filter(k=>k!=='se').map(k=>[k,SM[k].s]),st.rb,k=>{st.rb=k;drawRad()});
 const AX=['Thơm','Chua','Ngọt','Đắng','Thể chất','Hậu vị'],A=SM.se.prof,B=SM[st.rb].prof,cx=170,cy=150,Rr=100,n=6,pt=(i,r)=>{const a=(-90+i*360/n)*Math.PI/180;return [cx+r*Math.cos(a),cy+r*Math.sin(a)]};
 let g='';[2,4,6,8,10].forEach(v=>g+=`<polygon class="grid" points="${AX.map((_,i)=>pt(i,Rr*v/10).map(f1).join(',')).join(' ')}"/>`);
 AX.forEach((_,i)=>{const [x,y]=pt(i,Rr);g+=`<line x1="${cx}" y1="${cy}" x2="${f1(x)}" y2="${f1(y)}" style="stroke:var(--rule)"/>`});
 [[B,SM[st.rb].c,'6 4'],[A,SM.se.c,'']].forEach(([v,c,d])=>g+=`<polygon points="${v.map((x,i)=>pt(i,Rr*x/10).map(f1).join(',')).join(' ')}" style="fill:${c};fill-opacity:.18;stroke:${c};stroke-width:2.2${d?';stroke-dasharray:'+d:''}"/>`);
 AX.forEach((nm,i)=>{const [x,y]=pt(i,Rr+20);g+=`<text x="${f1(x)}" y="${f1(y+4)}" text-anchor="middle">${nm}</text>`});
 $('cRad').innerHTML=g;legend('lgRad',[{n:'Cà Sẻ Di Linh',c:SM.se.c},{n:SM[st.rb].n,c:SM[st.rb].c,d:1}]);
 const up=[],dn=[];AX.forEach((nm,i)=>{const d=A[i]-B[i];if(d>=1)up.push(nm.toLowerCase());else if(d<=-1)dn.push(nm.toLowerCase())});
 $('radT').textContent=!up.length&&!dn.length?`Cà Sẻ và ${SM[st.rb].s} gần giống nhau trên sáu trục.`:`So với ${SM[st.rb].s}, Cà Sẻ ${up.length?'mạnh hơn ở '+up.join(', '):''}${up.length&&dn.length?'; ':''}${dn.length?'nhẹ hơn ở '+dn.join(', '):''}.`}

/* ====== PHIẾU ====== */
function sheet(){if(!R.V)return;const m=R.V.m,P=R.P,qa=Object.entries(st.qa).map(([q,o])=>{const Q=QZ.find(x=>x.id===q);return `${Q.n}: ${Q.o.find(x=>x.id===o).t}`});
 const t=`PHIẾU KIỂM MẪU CÀ PHÊ NHÂN · MeDili
Lô: ________  Nhà cung cấp: ________  Ngày: __/__/____
Tên gọi khi chào hàng: ________  Vùng, độ cao: ________
Vườn: thực sinh / ghép / không rõ · Năm trồng: ____

1. Độ ẩm: ____ % (tối đa 12,5%)
2. Soi 100 nhân: rãnh thẳng ___ · chữ S ___ · nhăn lệch ___ · tròn ___
3. Sàng 300 g: trên 18 ___ % · 16–18 ___ % · 13–16 ___ % · lọt 13 ___ %
4. 100 nhân: ___ g · ___ g · ___ g → trung bình ___ g
5. Lỗi theo TCVN 4193: đen ___ · nâu ___ · non ___ · vỡ ___ · tạp chất ___
6. Nếm (Fine Robusta / SCA): điểm ___ · ghi chú ____________
7. Lab nếu có: caffeine ___ % · 16-OMC ___ mg/kg · DNA ________

Số đang nhập vào máy: 100 nhân ${vn(m.w,1)} g · trên sàng 16 ${vn(m.s16,0)}% · hạt tròn ${vn(m.cu,0)}%${R.V.lab?` · caffeine ${vn(m.caf,2)}%`:''}
Máy MeDili (mô hình minh họa): ${P.slice(0,2).map(o=>SM[o.k].s+' '+pc(o.p)+'%').join(' · ')}
${qa.length?'Cảm quan: '+qa.join('; ')+'\n':''}Kết luận: ________________  Người kiểm: ________`;
 $('sheet').textContent=t;st.sheet=t}
$('cpSh').onclick=()=>cp(st.sheet,'cpShS');

buildScene();calc();gallery();ptab();pair();drawRad();drawR();qz();update();
let rz=0;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(drawR,150)});
'''

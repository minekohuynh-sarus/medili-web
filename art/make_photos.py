# Cắt, thu nhỏ, nén ảnh thật của MeDili cho web và đóng logo chìm (logo kem, góc dưới). Bỏ EXIF (cả GPS).
# Chạy: python3 art/make_photos.py   (ảnh gốc phải có sẵn ở SRC và SRC2)
import os
from PIL import Image, ImageOps, ImageFilter, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'site-new4', 'assets')
LOGO = os.path.join(OUT, 'logo-kem.png')
os.makedirs(OUT, exist_ok=True)

# Đợt 1: ảnh chị Ngân gửi trong cuộc trò chuyện (tên file = mã ảnh đính kèm).
SRC = '/mnt/user-data/attachments/619bd0cf-b746-5328-b8be-a7ac0d4efa6d'
# Đợt 2: ảnh trong thư mục Google Drive "11/2026" chị Ngân gửi ngày 21/11/2026.
# IMG_0603 là ảnh máy ảnh (thư mục ẢNH); H0545, H0549 là ảnh điện thoại (HEIC đã đổi sang JPG).
# 23/11/2026: chị Ngân yêu cầu bỏ ảnh người nữ đội mũ MeDili (IMG_0548–IMG_0551) khỏi web, không dùng lại các ảnh này.
# Hosting chỉ thêm và cập nhật file, không xoá, nên các file ảnh cũ được ghi đè bằng ô màu kem (REMOVED) để thay luôn trên medili.vn.
REMOVED = ['p-nguoi-vuon.jpg', 'p-sq-nguoi-vuon.jpg', 'p-doi-ngu-vuon.jpg', 'g-vuon-nguoi-vuon.jpg', 'g-vuon-nguoi-vuon-s.jpg']
SRC2 = os.environ.get('MEDILI_ANH', '/tmp/claude-0/-home-claude/619bd0cf-b746-5328-b8be-a7ac0d4efa6d/scratchpad/anh')

# tên ra: (file nguồn, tỷ lệ rộng/cao, tâm x, tâm y, rộng ra)
JOBS = {
    'p-robusta-tay.jpg': ('3759dff3', 3 / 2, .5, .5, 1500),
    'p-sq-tay.jpg': ('3759dff3', 1, .45, .5, 900),
    'p-robusta-canh.jpg': ('10517b97', 4 / 5, .5, .45, 960),
    'p-sq-canh.jpg': ('10517b97', 1, .5, .4, 900),
    'p-robusta-chum.jpg': ('8a31c288', 3 / 2, .5, .35, 1200),
    'p-san-phoi-wide.jpg': ('5c6c7a3b', 3, .5, .40, 1350),
    'p-sq-san-phoi.jpg': ('5c6c7a3b', 1, .5, .55, 900),
    'p-honey.jpg': ('ce2fd9de', 1, .5, .5, 900),
    'p-natural.jpg': ('caff86f5', 1, .5, .55, 900),
    'p-xat-tuoi.jpg': ('47fb57b2', 1, .5, .55, 900),
    'p-lm-nhan.jpg': ('073b9a20', 1, .5, .5, 900),
    'p-lm-dau-tam.jpg': ('5eb3d637', 1, .5, .5, 900),
    'p-lm-chanh-day.jpg': ('5be6df2d', 1, .5, .5, 900),
    'p-kho-wide.jpg': ('b75910ab', 3, .5, .6, 1600),
    'p-may-rang.jpg': ('e9fd1566', 3 / 2, .5, .575, 1200),
    'p-may-rang-dung.jpg': ('e9fd1566', 4 / 5, .5, .5, 960),
    'p-hat-rang.jpg': ('2149f183', 3 / 2, .5, .36, 1200),
    'p-hai-chon.jpg': ('c7aa0b06', 3 / 2, .5, .45, 1200),
    'p-sq-chum-chin.jpg': ('a9bfa20b', 1, .5, .45, 900),      # thay ảnh người trong dải Vào mùa (23/11/2026)
    'p-tay-hai-doc.jpg': ('381f5a09', 4 / 5, .5, .5, 960),    # thay ảnh người ở trang Đội ngũ (23/11/2026)
}
JOBS2 = {
    'p-mua-chin.jpg': ('src/IMG_0603.jpg', 3 / 2, .5, .58, 1500),
    'p-sq-may-cay.jpg': ('work/H0549.jpg', 1, .5, .62, 900),
    'p-sq-duong-lo.jpg': ('work/H0545.jpg', 1, .5, .55, 900),
}


def crop(im, ratio, fx, fy):
    W, H = im.size
    if W / H > ratio:
        w, h = round(H * ratio), H
    else:
        w, h = W, round(W / ratio)
    x = min(max(round(fx * W - w / 2), 0), W - w)
    y = min(max(round(fy * H - h / 2), 0), H - h)
    return im.crop((x, y, x + w, y + h))


def watermark(im, ratio):
    """Logo kem mờ ở góc dưới phải; ảnh ngang 3:1 đặt giữa đáy vì trên điện thoại web cắt hai bên còn 2:1.
    Ảnh dọc 4:5 chừa lề dưới rộng hơn vì khung ảnh trên web có thể cắt bớt trên và dưới."""
    W, H = im.size
    k = .13 if ratio >= 2.5 else .19 if ratio >= 1.2 else .22 if ratio >= .95 else .24
    lg = Image.open(LOGO).convert('RGBA')
    lw = round(W * k); lh = round(lg.size[1] * lw / lg.size[0])
    lg = lg.resize((lw, lh), Image.LANCZOS)
    if ratio >= 2.5:
        x, y = (W - lw) // 2, H - lh - round(H * .07)
    elif ratio < .95:
        x, y = W - lw - round(W * .05), H - lh - round(H * .085)
    else:
        m = round(min(W, H) * .045)
        x, y = W - lw - m, H - lh - m
    a = lg.getchannel('A')
    # bóng mềm để logo đọc được cả trên nền sáng (trời, bao trắng)
    pad = max(4, round(lw * .04))
    sh = Image.new('L', (lw + 2 * pad, lh + 2 * pad), 0)
    sh.paste(a, (pad, pad))
    sh = sh.filter(ImageFilter.GaussianBlur(max(2, lw * .018))).point(lambda v: round(v * .38))
    base = im.convert('RGBA')
    shadow = Image.new('RGBA', sh.size, (20, 12, 8, 0)); shadow.putalpha(sh)
    base.alpha_composite(shadow, (x - pad, y - pad + max(1, round(lw * .006))))
    lg.putalpha(a.point(lambda v: round(v * .62)))
    base.alpha_composite(lg, (x, y))
    return base.convert('RGB')


def make(name, path, ratio, fx, fy, ow):
    im = ImageOps.exif_transpose(Image.open(path)).convert('RGB')
    c = crop(im, ratio, fx, fy)
    oh = round(ow / ratio)
    if c.size[0] > ow:
        c = c.resize((ow, oh), Image.LANCZOS)
    c = watermark(c, ratio)
    c.save(os.path.join(OUT, name), 'JPEG', quality=80, optimize=True, progressive=True)   # không truyền exif: ảnh ra không còn GPS
    print(f'{name:24s} {c.size} {os.path.getsize(os.path.join(OUT, name)) // 1024} KB')


def blank(name):
    Image.new('RGB', (8, 8), (239, 228, 210)).save(os.path.join(OUT, name), 'JPEG', quality=80)


if __name__ == '__main__':
    import sys
    only = set(sys.argv[1:])
    for name in REMOVED:
        blank(name)
    for name, (src, ratio, fx, fy, ow) in JOBS.items():
        if not only or name in only:
            make(name, os.path.join(SRC, src + '-image.jpg'), ratio, fx, fy, ow)
    for name, (src, ratio, fx, fy, ow) in JOBS2.items():
        if not only or name in only:
            make(name, os.path.join(SRC2, src), ratio, fx, fy, ow)
    names = [n for n in list(JOBS) + list(JOBS2) if not only or n in only]
    print('tổng', sum(os.path.getsize(os.path.join(OUT, n)) for n in names) // 1024, 'KB')

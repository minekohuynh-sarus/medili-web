# Cắt, thu nhỏ và nén ảnh chị Ngân gửi cho site MeDili. Bỏ EXIF.
import os
from PIL import Image, ImageOps

SRC = '/mnt/user-data/attachments/619bd0cf-b746-5328-b8be-a7ac0d4efa6d'
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'site-new4', 'assets')
os.makedirs(OUT, exist_ok=True)

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


SIZES = {}
for name, (src, ratio, fx, fy, ow) in JOBS.items():
    im = ImageOps.exif_transpose(Image.open(os.path.join(SRC, src + '-image.jpg'))).convert('RGB')
    c = crop(im, ratio, fx, fy)
    oh = round(ow / ratio)
    if c.size[0] > ow:
        c = c.resize((ow, oh), Image.LANCZOS)
    c.save(os.path.join(OUT, name), 'JPEG', quality=80, optimize=True, progressive=True)
    SIZES[name] = c.size
    print(f'{name:24s} {c.size} {os.path.getsize(os.path.join(OUT, name)) // 1024} KB')
print('tổng', sum(os.path.getsize(os.path.join(OUT, n)) for n in JOBS) // 1024, 'KB')

# Ảnh cho trang Ảnh vườn và ảnh nền toàn khung (trang chủ, dải ảnh, đầu trang Ảnh vườn).
# Mọi ảnh đều đóng logo chìm MeDili (logo kem) và không mang EXIF/GPS.
# Chạy: python3 art/make_gallery.py   (ảnh gốc phải có sẵn ở SRC và SRC2 trong make_photos.py)
import os, sys
from PIL import Image, ImageOps, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_photos import OUT, LOGO, SRC, SRC2, crop, watermark
from anhvuon import GAL_ALL, BG
# ảnh có ảnh gốc trong máy (ảnh tải lên ở trang quản trị đã được trình duyệt thu nhỏ, đóng logo sẵn: nguon = null)
GAL = [(x['nhom'], x['ten'], x['nguon'], x.get('ty_le'), x.get('x', .5), x.get('y', .5), x['alt'], x['cap']) for x in GAL_ALL if x.get('nguon')]

LONG, SMALL = 1600, 760   # cạnh dài ảnh xem lớn; khung ảnh nhỏ trong lưới


def src_path(s):
    return os.path.join(SRC, s + '-image.jpg') if '/' not in s else os.path.join(SRC2, s)


def open_rgb(s):
    return ImageOps.exif_transpose(Image.open(src_path(s))).convert('RGB')


def save(im, name, q):
    p = os.path.join(OUT, name)
    im.save(p, 'JPEG', quality=q, optimize=True, progressive=True)   # không truyền exif
    return os.path.getsize(p)


def wm_corner(im, k, mx, my, op=.55):
    """Logo chìm góc dưới phải cho ảnh nền: web neo ảnh nền ở góc dưới phải nên khung cắt cỡ nào logo vẫn còn."""
    W, H = im.size
    lg = Image.open(LOGO).convert('RGBA')
    lw = round(W * k); lh = round(lg.size[1] * lw / lg.size[0])
    lg = lg.resize((lw, lh), Image.LANCZOS)
    x, y = W - lw - round(W * mx), H - lh - round(H * my)
    a = lg.getchannel('A')
    pad = max(4, round(lw * .04))
    sh = Image.new('L', (lw + 2 * pad, lh + 2 * pad), 0)
    sh.paste(a, (pad, pad))
    sh = sh.filter(ImageFilter.GaussianBlur(max(2, lw * .02))).point(lambda v: round(v * .42))
    base = im.convert('RGBA')
    shadow = Image.new('RGBA', sh.size, (20, 12, 8, 0)); shadow.putalpha(sh)
    base.alpha_composite(shadow, (x - pad, y - pad + max(1, round(lw * .006))))
    lg.putalpha(a.point(lambda v: round(v * op)))
    base.alpha_composite(lg, (x, y))
    return base.convert('RGB')


def gallery(only=()):
    tot = 0
    for g, name, src, ratio, fx, fy, alt, cap in GAL:
        if only and name not in only:
            continue
        im = open_rgb(src)
        r = ratio or im.size[0] / im.size[1]
        if ratio:
            im = crop(im, ratio, fx, fy)
        s = min(1, LONG / max(im.size))
        if s < 1:
            im = im.resize((round(im.size[0] * s), round(im.size[1] * s)), Image.LANCZOS)
        im = watermark(im, r)
        n1 = save(im, f'g-{name}.jpg', 80)
        t = min(1, SMALL / max(im.size))
        sm = im.resize((round(im.size[0] * t), round(im.size[1] * t)), Image.LANCZOS) if t < 1 else im
        n2 = save(sm, f'g-{name}-s.jpg', 78)
        tot += n1 + n2
        print(f'g-{name:20s} {im.size} {n1 // 1024} KB · nhỏ {sm.size} {n2 // 1024} KB')
    return tot


def backgrounds(only=()):
    tot = 0
    for name, (src, desk, mob) in BG.items():
        if only and name not in only:
            continue
        im = open_rgb(src)
        for suf, (ratio, fx, fy, ow), (k, mx, my) in (('', desk, (.1, .03, .05)), ('-m', mob, (.21, .05, .035))):
            c = crop(im, ratio, fx, fy)
            if c.size[0] > ow:
                c = c.resize((ow, round(ow / ratio)), Image.LANCZOS)
            c = wm_corner(c, k, mx, my)
            n = save(c, f'{name}{suf}.jpg', 74)
            tot += n
            print(f'{name + suf + ".jpg":22s} {c.size} {n // 1024} KB')
    return tot


if __name__ == '__main__':
    only = set(sys.argv[1:])
    t = gallery(only) + backgrounds(only)
    print('tổng', t // 1024, 'KB')

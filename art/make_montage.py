# Clip ghép "Một mùa ở vườn Di Linh" cho trang Vùng trồng Di Linh (chị Ngân yêu cầu 26/11/2026: "ghép clip lại cho hay").
# Nguồn: video Sony 4K 29,97 hình/giây chị Ngân gửi trong thư mục Drive "Cảnh minh hoạ khác", "1.6 Chùm trái chín không đều",
# "3.3 Nông dân nhặt cành lá". Không dùng clip có người chụp rõ mặt và clip có người nữ đội mũ MeDili.
# Dựng: 9 cảnh nối bằng chuyển cảnh mờ dần 0,7 giây; mở đầu hiện dần từ nền nâu, kết thúc chuyển sang thẻ logo MeDili trên nền nâu,
# nên clip lặp lại liền mạch. Logo chìm góc dưới phải suốt các cảnh (ẩn ở thẻ logo). Không có tiếng, không có chữ đè lên hình
# (tên cảnh nằm trên trang web để dịch được sang các thứ tiếng). Bỏ toàn bộ siêu dữ liệu.
# Ra: assets/v-mua-vuon-720.mp4 (1280×720, máy tính), v-mua-vuon-480.mp4 (854×480, điện thoại), ảnh chờ v-mua-vuon.jpg,
#     ảnh từng cảnh v-mua-vuon-c1.jpg … c6.jpg (384×216).
# Chạy: python3 art/make_montage.py   (video gốc phải có sẵn ở SRC)
import os, sys, subprocess, tempfile
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'site-new4', 'assets')
LOGO = os.path.join(OUT, 'logo-kem.png')
SRC = os.environ.get('MEDILI_VID', '/tmp/claude-0/-home-claude/619bd0cf-b746-5328-b8be-a7ac0d4efa6d/scratchpad/vid/src')
W, H = 1280, 720
FPS = '30000/1001'
BROWN = '4A2C1A'          # nâu rang mộc của bộ nhận diện
T = 0.7                   # chuyển cảnh giữa các cảnh
T_CARD, CARD = 1.0, 3.4   # chuyển sang thẻ logo, thời lượng thẻ logo (logo hiện dần, giữ, rồi mờ đi để vòng lặp liền mạch)
NAME = 'v-mua-vuon'

# (file gốc, giây bắt đầu, số giây, cảnh số) — cảnh số khớp danh sách cảnh trên trang (clipvuon.CHAPTERS)
SEGS = [
    ('C1736.MP4', 0.5, 4.5, 1),   # hoa cà phê nở trắng, có ong
    ('C1729.MP4', 1.0, 3.5, 1),   # cận cảnh chùm hoa
    ('C1974.MP4', 1.0, 4.5, 2),   # nắng xuyên qua tán
    ('C1517.MP4', 2.0, 4.5, 3),   # lướt dọc những cành trĩu trái chín
    ('C1515.MP4', 0.5, 4.0, 3),   # lướt qua chùm Robusta chín đỏ
    ('C1519.MP4', 1.0, 5.5, 4),   # góc thấp: một chùm, nhiều độ chín
    ('C1833.MP4', 0.3, 6.0, 5),   # người vườn nhặt cành lá trên bạt (cúi, ở xa)
    ('C1734.MP4', 1.0, 5.5, 6),   # đi giữa hàng cà phê, hiện ra đồi xa
    ('C1743.MP4', 4.0, 6.0, 6),   # lia qua đồi cà phê, sương trên núi
]


def timeline():
    """Mốc bắt đầu từng cảnh trên clip ghép (giây) và tổng thời lượng."""
    starts, end = [0.0], SEGS[0][2]
    for i in range(1, len(SEGS)):
        o = end - T
        starts.append(o)
        end = o + SEGS[i][2]
    card = end - T_CARD
    return starts, card, card + CARD


def chapters():
    """[(cảnh số, giây bắt đầu để nhảy tới, giây bắt đầu tính là cảnh này)] theo thứ tự."""
    starts, _, _ = timeline()
    out = {}
    for (src, ss, d, ch), st in zip(SEGS, starts):
        if ch not in out:
            out[ch] = (round(st + (T if st else 0), 2), round(st + (T / 2 if st else 0), 2))
    return [(ch, a, b) for ch, (a, b) in sorted(out.items())]


def logo_png(path, k, op, corner=True):
    lg = Image.open(LOGO).convert('RGBA')
    lw = round(W * k); lh = round(lg.size[1] * lw / lg.size[0])
    lg = lg.resize((lw, lh), Image.LANCZOS)
    if corner:
        m = round(H * .05); x, y = W - lw - m, H - lh - m
    else:
        x, y = (W - lw) // 2, (H - lh) // 2
    a = lg.getchannel('A')
    base = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    if corner:   # bóng mềm để logo đọc được cả trên nền sáng
        pad = max(4, round(lw * .04))
        sh = Image.new('L', (lw + 2 * pad, lh + 2 * pad), 0)
        sh.paste(a, (pad, pad))
        sh = sh.filter(ImageFilter.GaussianBlur(max(2, lw * .02))).point(lambda v: round(v * .4))
        shadow = Image.new('RGBA', sh.size, (20, 12, 8, 0)); shadow.putalpha(sh)
        base.alpha_composite(shadow, (x - pad, y - pad + max(1, round(lw * .006))))
    lg.putalpha(a.point(lambda v: round(v * op)))
    base.alpha_composite(lg, (x, y))
    base.save(path)


def run(args):
    subprocess.run(['ffmpeg', '-v', 'error', '-y'] + args, check=True)


def build(td):
    starts, card_at, total = timeline()
    # 1. từng cảnh: cắt, thu về 1280×720, cảnh đầu hiện dần từ nền nâu
    segs = []
    for i, (src, ss, d, ch) in enumerate(SEGS):
        f = os.path.join(td, f's{i}.mp4')
        vf = f'scale={W}:{H}:flags=lanczos,fps={FPS},format=yuv420p,setsar=1'
        if i == 0:
            vf += f',fade=t=in:st=0:d=0.8:color=0x{BROWN}'
        run(['-ss', f'{ss}', '-i', os.path.join(SRC, src), '-t', f'{d}', '-vf', vf, '-an', '-sn', '-dn',
             '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14', f])
        segs.append(f)
    # 2. thẻ logo: nền nâu, logo kem hiện dần ở giữa
    big = os.path.join(td, 'logo_big.png'); logo_png(big, .34, 1.0, corner=False)
    card = os.path.join(td, 'card.mp4')
    run(['-f', 'lavfi', '-i', f'color=c=0x{BROWN}:s={W}x{H}:r={FPS}:d={CARD}', '-loop', '1', '-framerate', FPS, '-t', f'{CARD}', '-i', big,
         '-filter_complex', f'[1:v]format=rgba,fade=t=in:st={T_CARD * .6:.2f}:d=0.8:alpha=1,fade=t=out:st={CARD - .75:.2f}:d=0.6:alpha=1[l];[0:v][l]overlay=0:0:format=auto,format=yuv420p',
         '-t', f'{CARD}', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '14', card])
    # 3. nối bằng chuyển cảnh mờ dần, thêm logo chìm góc dưới phải (hiện dần đầu clip, mờ đi khi sang thẻ logo)
    wm = os.path.join(td, 'logo_wm.png'); logo_png(wm, .12, .55)
    ins, fc = [], []
    for i, f in enumerate(segs + [card]):
        ins += ['-i', f]
        fc.append(f'[{i}:v]fps={FPS},settb=AVTB,format=yuv420p[a{i}]')   # cùng nhịp hình và cùng đơn vị thời gian cho xfade
    prev = '[a0]'
    for i in range(1, len(segs) + 1):
        tr, off = (T_CARD, card_at) if i == len(segs) else (T, starts[i])
        lab = f'[x{i}]'
        fc.append(f'{prev}[a{i}]xfade=transition=fade:duration={tr}:offset={off:.3f}{lab}')
        prev = lab
    n = len(segs) + 1
    ins += ['-loop', '1', '-framerate', FPS, '-t', f'{total:.3f}', '-i', wm]
    fc.append(f'[{n}:v]format=rgba,fade=t=in:st=0.3:d=0.8:alpha=1,fade=t=out:st={card_at:.3f}:d=0.6:alpha=1[w]')
    fc.append(f'{prev}[w]overlay=0:0:format=auto,format=yuv420p[v]')
    master = os.path.join(td, 'master.mp4')
    run(ins + ['-filter_complex', ';'.join(fc), '-map', '[v]', '-t', f'{total:.3f}', '-c:v', 'libx264', '-preset', 'veryfast',
               '-crf', '12', master])
    return master, total


def export(master):
    common = ['-an', '-sn', '-dn', '-map_metadata', '-1', '-map_chapters', '-1', '-movflags', '+faststart',
              '-fflags', '+bitexact', '-flags:v', '+bitexact', '-c:v', 'libx264', '-preset', 'veryfast', '-profile:v', 'high']
    hd = os.path.join(OUT, f'{NAME}-720.mp4')
    run(['-i', master] + common + ['-crf', '23', '-maxrate', '4000k', '-bufsize', '8000k', '-level:v', '4.0', hd])
    sd = os.path.join(OUT, f'{NAME}-480.mp4')
    run(['-i', master, '-vf', 'scale=854:480:flags=lanczos'] + common + ['-crf', '25', '-maxrate', '1800k', '-bufsize', '3600k',
                                                                          '-level:v', '3.1', sd])
    return hd, sd


def stills(master):
    with tempfile.TemporaryDirectory() as td:
        def frame(t, w, h, out, q):
            f = os.path.join(td, 'f.png')
            run(['-ss', f'{t:.2f}', '-i', master, '-frames:v', '1', f])
            im = Image.open(f).convert('RGB')
            if (w, h) != im.size:
                im = im.resize((w, h), Image.LANCZOS)
            im.save(os.path.join(OUT, out), 'JPEG', quality=q, optimize=True, progressive=True)   # không EXIF
        starts, _, _ = timeline()
        frame(starts[4] + 1.6, W, H, f'{NAME}.jpg', 80)            # ảnh chờ: chùm Robusta chín đỏ
        for ch, seek, _ in chapters():
            frame(seek + 1.0, 384, 216, f'{NAME}-c{ch}.jpg', 76)


if __name__ == '__main__':
    with tempfile.TemporaryDirectory() as td:
        master, total = build(td)
        hd, sd = export(master)
        stills(master)
    for f in (hd, sd):
        print(os.path.basename(f), os.path.getsize(f) // 1024, 'KB')
    print('dài', round(total, 2), 'giây · cảnh', chapters())

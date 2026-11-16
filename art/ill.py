# Minh hoạ SVG cho các trang mới, tô bằng token nên đổi được nền sáng/tối. Không dùng xanh lá, không đen.

def _hill(pts, x):
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= x <= x1:
            t = (x - x0) / (x1 - x0)
            return y0 + (y1 - y0) * t
    return pts[-1][1]


def phin(label='Phin cà phê nhỏ giọt xuống ly'):
    return f'''<svg class="ill" viewBox="0 0 240 160" role="img" aria-label="{label}">
<ellipse cx="120" cy="147" rx="64" ry="6" fill="var(--rule)"/>
<path d="M89.8 108h60.4l-3 32.4a6 6 0 0 1-6 5.1H98.8a6 6 0 0 1-6-5.1z" fill="var(--i-coffee)"/>
<path class="o" d="M86 74h68l-6 66a6 6 0 0 1-6 5.5H98a6 6 0 0 1-6-5.5z" fill="none"/>
<ellipse cx="120" cy="86" rx="2.4" ry="4" fill="var(--i-coffee)"/><ellipse cx="120" cy="98" rx="2" ry="3.3" fill="var(--i-coffee)" opacity=".7"/>
<path class="o" d="M96 36h48l-3.5 30h-41z" fill="var(--i-gold)"/>
<rect class="o" x="78" y="66" width="84" height="7.5" rx="3.7" fill="var(--i-gold2)"/>
<rect class="o" x="92" y="27" width="56" height="9" rx="4" fill="var(--i-gold2)"/>
<rect class="o" x="113" y="18" width="14" height="9" rx="3" fill="var(--i-gold)"/>
<circle class="o" cx="197" cy="56" r="20" fill="var(--panel)"/><path class="o" d="M197 44v12l8 6" fill="none"/>
<text x="197" y="97" text-anchor="middle">4–5 phút</text>
</svg>'''


def qua(label='Trái chín, nhân và hạt rang'):
    arrow = lambda x: f'<path d="M{x} 80h18m-6-6 6 6-6 6" fill="none" stroke="var(--muted)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
    return f'''<svg class="ill" viewBox="0 0 240 160" role="img" aria-label="{label}">
<path d="M46 54c2-13 9-21 20-25" fill="none" stroke="var(--i-brown)" stroke-width="3" stroke-linecap="round"/>
<circle class="o" cx="44" cy="80" r="25" fill="var(--i-red)"/>
<path d="M30 70a16 16 0 0 1 11-9" fill="none" stroke="#F2A48D" stroke-width="3" stroke-linecap="round" opacity=".7"/>
{arrow(78)}
<ellipse class="o" cx="124" cy="80" rx="15" ry="22" fill="var(--i-milk)"/>
<path d="M124 60c-5 8 5 32 0 40" fill="none" stroke="var(--i-brown)" stroke-width="2" stroke-linecap="round"/>
{arrow(150)}
<ellipse class="o" cx="196" cy="80" rx="15" ry="22" fill="var(--i-coffee)"/>
<path d="M196 60c-5 8 5 32 0 40" fill="none" stroke="var(--i-milk)" stroke-width="2" stroke-linecap="round"/>
<text x="44" y="130" text-anchor="middle">Trái chín</text><text x="124" y="130" text-anchor="middle">Nhân</text><text x="196" y="130" text-anchor="middle">Hạt rang</text>
</svg>'''


def dilinh(label='Đồi cà phê Di Linh'):
    back = [(0, 100), (40, 78), (80, 72), (120, 86), (160, 96), (200, 74), (240, 80)]
    front = [(0, 126), (50, 106), (100, 108), (140, 118), (180, 128), (210, 116), (240, 116)]
    poly = lambda pts: 'M' + ' L'.join(f'{x} {y}' for x, y in pts) + ' L240 160 L0 160Z'
    dots = ''
    for x in range(10, 240, 17):
        dots += f'<circle cx="{x}" cy="{_hill(back, x) + 9:.1f}" r="4.3"/>'
    for x in range(4, 240, 15):
        dots += f'<circle cx="{x}" cy="{_hill(front, x) + 10:.1f}" r="4.8"/>'
        dots += f'<circle cx="{x + 7}" cy="{_hill(front, x + 7) + 24:.1f}" r="4.8"/>'
    return f'''<svg class="ill" viewBox="0 0 240 160" role="img" aria-label="{label}">
<circle cx="182" cy="42" r="15" fill="var(--accent)" opacity=".85"/>
<path d="{poly(back)}" fill="var(--i-gold)"/><path d="{poly(front)}" fill="var(--i-brown)"/>
<g fill="var(--i-coffee)">{dots}</g>
</svg>'''


def suckhoe(label='Tách cà phê và trái tim'):
    return f'''<svg class="ill" viewBox="0 0 240 160" role="img" aria-label="{label}">
<ellipse cx="118" cy="136" rx="66" ry="8" fill="var(--rule)"/>
<path d="M104 46c-6-7 6-10 0-18M126 46c-6-7 6-10 0-18" fill="none" stroke="var(--muted)" stroke-width="2.4" stroke-linecap="round"/>
<path class="o" d="M78 60h80v32a36 36 0 0 1-36 36h-8a36 36 0 0 1-36-36z" fill="var(--panel)"/>
<path class="o" d="M158 70h8a14 14 0 0 1 0 28h-10" fill="none"/>
<ellipse cx="118" cy="61" rx="38" ry="5.5" fill="var(--i-coffee)"/>
<path d="M118 112s-17-9.5-17-21a9 9 0 0 1 17-4.2 9 9 0 0 1 17 4.2c0 11.5-17 21-17 21z" fill="var(--accent)"/>
</svg>'''


def suada(label='Ly cà phê sữa đá với phin trên miệng ly'):
    return f'''<svg class="ill" viewBox="0 0 240 220" role="img" aria-label="{label}">
<ellipse cx="120" cy="206" rx="70" ry="7" fill="var(--rule)"/>
<path d="M76.6 150h86.8l-4.2 44a8 8 0 0 1-8 7.2H88.8a8 8 0 0 1-8-7.2z" fill="var(--i-milk)"/>
<path d="M73.2 112h93.6l-3.4 38H76.6z" fill="var(--i-coffee)"/>
<rect x="88" y="118" width="24" height="22" rx="4" fill="var(--panel)" opacity=".55"/><rect x="122" y="128" width="22" height="20" rx="4" fill="var(--panel)" opacity=".5"/>
<path class="o" d="M70 80h100l-10 114a8 8 0 0 1-8 7.2H88a8 8 0 0 1-8-7.2z" fill="none"/>
<path class="o" d="M95 38h50l-4 34h-42z" fill="var(--i-gold)"/>
<rect class="o" x="80" y="72" width="80" height="8" rx="4" fill="var(--i-gold2)"/>
<rect class="o" x="91" y="28" width="58" height="10" rx="4.5" fill="var(--i-gold2)"/>
<rect class="o" x="113" y="18" width="14" height="10" rx="3" fill="var(--i-gold)"/>
<ellipse cx="120" cy="92" rx="2.5" ry="4.2" fill="var(--i-coffee)"/><ellipse cx="120" cy="103" rx="2" ry="3.4" fill="var(--i-coffee)" opacity=".7"/>
</svg>'''


def chiet(label='Bốn ống nghiệm đầy dần theo thứ tự chiết xuất và một tách cà phê'):
    tubes = ''
    for i, (x, f) in enumerate([(46, .96), (78, .88), (110, .7), (142, .3)], 1):
        top = 120 - f * 70
        tubes += (f'<path d="M{x - 7} {top:.1f}V113a7 7 0 0 0 14 0V{top:.1f}z" fill="var(--cx{i})"/>'
                  f'<path class="o" d="M{x - 9} 34V113a9 9 0 0 0 18 0V34" fill="none"/>'
                  f'<rect class="o" x="{x - 11}" y="29" width="22" height="6" rx="3" fill="var(--panel)"/>')
    return f'''<svg class="ill" viewBox="0 0 240 160" role="img" aria-label="{label}">
<ellipse cx="120" cy="147" rx="98" ry="6.5" fill="var(--rule)"/>
<rect class="o" x="24" y="58" width="140" height="8" rx="4" fill="var(--i-gold2)"/>
{tubes}
<rect class="o" x="20" y="122" width="148" height="16" rx="5" fill="var(--i-brown)"/>
<path d="M196 64c-6-7 6-10 0-18M210 64c-6-7 6-10 0-18" fill="none" stroke="var(--muted)" stroke-width="2.4" stroke-linecap="round"/>
<path class="o" d="M180 78h46v26a20 20 0 0 1-20 20h-6a20 20 0 0 1-20-20z" fill="var(--panel)"/>
<path class="o" d="M226 86h3a9 9 0 0 1 0 18h-5" fill="none"/>
<ellipse cx="203" cy="79" rx="21.5" ry="4" fill="var(--i-coffee)"/>
</svg>'''

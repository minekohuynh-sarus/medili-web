<?php
// Trang quản trị MeDili: dựng giao diện các trang.
defined('MDQ') or exit;

const NAV = array('' => 'Tổng quan', 'thong-bao' => 'Thông báo & liên hệ', 'san-pham' => 'Sản phẩm & giá', 'tin-tuc' => 'Tin tức',
                  'anh' => 'Ảnh vườn', 'video' => 'Video', 'tai-khoan' => 'Tài khoản', 'cai-dat' => 'Cài đặt');

function icon($k) {
    $p = array(
        'nha' => '<path d="M4 11.5 12 5l8 6.5"/><path d="M6.5 10v9h11v-9"/>',
        'loa' => '<path d="M4 10v4h3l5 4V6L7 10z"/><path d="M16 9a4 4 0 0 1 0 6"/>',
        'tui' => '<path d="M6 8h12l-1 12H7z"/><path d="M9 8V6.5a3 3 0 0 1 6 0V8"/>',
        'bao' => '<path d="M5 5h11v14H6a1 1 0 0 1-1-1z"/><path d="M16 9h3v9a1 1 0 0 1-1 1h-2"/><path d="M8 9h5M8 12h5M8 15h3"/>',
        'anh' => '<rect x="4" y="5" width="16" height="14" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="m5 17 4.5-4.5 3 3 2-2L19 17"/>',
        'phim' => '<rect x="4" y="6" width="12" height="12" rx="2"/><path d="m16 10 4-2v8l-4-2"/>',
        'nguoi' => '<circle cx="12" cy="8.5" r="3.3"/><path d="M5.5 19a6.5 6.5 0 0 1 13 0"/>',
        'banh' => '<circle cx="12" cy="12" r="3"/><path d="M12 3.5v2.2M12 18.3v2.2M3.5 12h2.2M18.3 12h2.2M6 6l1.6 1.6M16.4 16.4 18 18M6 18l1.6-1.6M16.4 7.6 18 6"/>',
        'ra' => '<path d="M14 5h5v14h-5"/><path d="M10 8l-4 4 4 4M6 12h9"/>',
        'mo' => '<path d="M14 5h5v5"/><path d="M19 5l-8 8"/><path d="M18 14v5H5V6h5"/>',
        'len' => '<path d="m6 14 6-6 6 6"/>', 'xuong' => '<path d="m6 10 6 6 6-6"/>',
        'sao' => '<path d="m12 4.5 2.3 4.8 5.2.7-3.8 3.6.9 5.2-4.6-2.5-4.6 2.5.9-5.2L4.5 10l5.2-.7z"/>',
        'mat' => '<path d="M3 12s3.5-6 9-6 9 6 9 6-3.5 6-9 6-9-6-9-6z"/><circle cx="12" cy="12" r="2.5"/>',
        'mat-gach' => '<path d="M4 4l16 16"/><path d="M9.9 6.2A9.7 9.7 0 0 1 12 6c5.5 0 9 6 9 6a15.6 15.6 0 0 1-2.6 3.3M6.3 7.8A15.4 15.4 0 0 0 3 12s3.5 6 9 6a8.8 8.8 0 0 0 4-1"/>',
        'xoa' => '<path d="M5 7h14M10 7V5h4v2M7 7l1 12h8l1-12"/>',
        'cong' => '<path d="M12 5v14M5 12h14"/>', 'dung' => '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    );
    return '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true">' . $p[$k] . '</svg>';
}

function layout($title, $active, $body, $opt = array()) {
    $u = current_user();
    $nav = '';
    $ics = array('' => 'nha', 'thong-bao' => 'loa', 'san-pham' => 'tui', 'tin-tuc' => 'bao', 'anh' => 'anh', 'video' => 'phim', 'tai-khoan' => 'nguoi', 'cai-dat' => 'banh');
    if ($u) foreach (NAV as $k => $t) {
        if ($k === 'cai-dat' && $u['vai'] !== 'chu') continue;
        $nav .= '<a href="./' . ($k ? '?t=' . $k : '') . '"' . ($k === $active ? ' aria-current="page"' : '') . '>' . icon($ics[$k]) . '<span>' . h($t) . '</span></a>';
    }
    $dep = $u ? store_get('lan-dua', null) : null;
    $pending = $dep && empty($dep['xong']) && time() - $dep['t'] < 6 * 3600;
    header('Content-Type: text/html; charset=utf-8');
    echo '<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
       . '<meta name="robots" content="noindex,nofollow"><meta name="referrer" content="same-origin"><title>' . h($title) . ' · Quản trị MeDili</title>'
       . '<link rel="icon" href="../assets/logo-mau.png"><link rel="preconnect" href="https://fonts.googleapis.com">'
       . '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700&family=Big+Shoulders+Display:wght@700;800&family=JetBrains+Mono:wght@500;700&display=swap">'
       . '<link rel="stylesheet" href="qt.css?v=' . filemtime(__DIR__ . '/qt.css') . '"></head>'
       . '<body data-csrf="' . h(session_status() === PHP_SESSION_ACTIVE ? csrf_token() : '') . '"' . ($pending ? ' data-dang-dua="1"' : '') . '><!--email_off-->'
       . '<header class="qt-top"><a class="qt-brand" href="./"><img src="../assets/logo-kem.png" alt="MeDili Café" width="112" height="36"><span>Quản trị</span></a>'
       . ($u ? '<div class="qt-me"><span class="qt-who"><b>' . h($u['ten']) . '</b><small>' . ($u['vai'] === 'chu' ? 'Chủ' : 'Nhân viên') . '</small></span>'
              . '<a class="qt-site" href="../" target="_blank" rel="noopener">' . icon('mo') . '<span>Xem web</span></a>'
              . '<button type="button" class="qt-out" data-act="dang-xuat">' . icon('ra') . '<span>Đăng xuất</span></button></div>' : '')
       . '</header>' . ($nav ? '<nav class="qt-nav" aria-label="Mục quản trị"><div class="qt-nav-in">' . $nav . '</div></nav>' : '')
       . '<main class="qt-main' . (isset($opt['cls']) ? ' ' . $opt['cls'] : '') . '" id="noi-dung">' . $body . '</main>'
       . ($u ? '<div class="qt-trk" id="qt-trk" hidden role="status" aria-live="polite"></div>' : '')
       . '<div class="qt-toast" id="qt-toast" hidden role="alert"></div>'
       . '<!--/email_off--><script src="qt.js?v=' . filemtime(__DIR__ . '/qt.js') . '"></script>'
       . (isset($opt['js']) ? '<script src="' . $opt['js'] . '?v=' . filemtime(__DIR__ . '/' . $opt['js']) . '"></script>' : '')
       . '</body></html>';
}

function card($title, $inner, $cls = '', $sub = '') {
    return '<section class="qt-card ' . $cls . '">' . ($title ? '<div class="qt-card-hd"><h2>' . $title . '</h2>' . ($sub ? '<p>' . $sub . '</p>' : '') . '</div>' : '') . $inner . '</section>';
}

function page_head($eye, $h1, $lead = '', $act = '') {
    return '<div class="qt-hd"><div><p class="qt-eye">' . h($eye) . '</p><h1>' . $h1 . '</h1>' . ($lead ? '<p class="qt-lead">' . $lead . '</p>' : '') . '</div>' . ($act ? '<div class="qt-hd-act">' . $act . '</div>' : '') . '</div>';
}

function err_box($e) { return '<div class="qt-alert loi"><b>Chưa đọc được dữ liệu.</b> ' . h($e->getMessage()) . '</div>'; }

function data_attr($v) { return h(json_encode($v, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES)); }

// tệp trong assets/: có trên hosting thì lấy ở hosting, chưa đồng bộ thì lấy tạm từ GitHub
function asset_url($name) {
    return is_file(qt_dir('site') . '/assets/' . $name) ? '../assets/' . rawurlencode($name)
        : 'https://raw.githubusercontent.com/' . GH_OWNER . '/' . GH_REPO . '/' . GH_BRANCH . '/' . GH_SRC . 'assets/' . rawurlencode($name);
}

function fmt_money($n) { return number_format((int)$n, 0, ',', '.'); }

function ago($t) {
    $d = time() - (int)$t;
    if ($d < 60) return 'vừa xong';
    if ($d < 3600) return floor($d / 60) . ' phút trước';
    if ($d < 86400) return floor($d / 3600) . ' giờ trước';
    return date('d/m/Y H:i', (int)$t);
}

// ---------------------------------------------------------------- lần đầu, đăng nhập, quên mật khẩu
function page_setup() {
    $b = '<div class="qt-auth wide">' . page_head('Cài đặt lần đầu', 'Chào chị Ngân. <em>Hai bước là xong.</em>',
        'Trang quản trị ghi thay đổi vào kho GitHub của web, GitHub tự dựng lại web rồi trang này đưa lên medili.vn. Khoá GitHub chỉ lưu trên hosting, ngoài thư mục web, em (Claude) không thấy.')
       . '<form class="qt-card qt-form" data-api="cai-dat" data-next="./" autocomplete="off">'
       . '<div class="qt-step"><span>1</span><div><h2>Dán khoá GitHub</h2>'
       . '<ol class="qt-howto"><li>Mở <a href="https://github.com/settings/personal-access-tokens/new" target="_blank" rel="noopener">github.com › Settings › Fine-grained tokens › Generate new token</a> (đăng nhập tài khoản GitHub của kho web).</li>'
       . '<li>Token name: <code>medili-quan-tri</code>. Expiration: <b>1 năm</b> (đặt lịch nhắc thay khoá trước ngày hết hạn).</li>'
       . '<li>Repository access: <b>Only select repositories</b> → chọn <code>' . GH_OWNER . '/' . GH_REPO . '</code>.</li>'
       . '<li>Permissions › Repository permissions: <b>Contents: Read and write</b> và <b>Actions: Read-only</b>. Metadata tự có.</li>'
       . '<li>Bấm Generate token, sao chép chuỗi bắt đầu bằng <code>github_pat_</code> rồi dán vào ô dưới.</li></ol>'
       . '<label class="qt-f"><span>Khoá GitHub</span><input type="password" name="token" required autocomplete="off" spellcheck="false" placeholder="github_pat_…"></label>'
       . '<button type="button" class="qt-btn" data-act="khoa-kiem">Kiểm tra khoá</button><p class="qt-note" data-khoa-kq></p></div></div>'
       . '<div class="qt-step"><span>2</span><div><h2>Tạo tài khoản chủ</h2>'
       . '<div class="qt-grid2"><label class="qt-f"><span>Tên hiển thị</span><input name="ten" required maxlength="60" value="Ngân"></label>'
       . '<label class="qt-f"><span>Tên đăng nhập</span><input name="u" required maxlength="30" pattern="[a-z0-9._\-]{3,30}" autocapitalize="none" spellcheck="false" placeholder="vd. ngan"></label>'
       . '<label class="qt-f"><span>Mật khẩu (ít nhất 10 ký tự)</span><input type="password" name="pw" required minlength="10" autocomplete="new-password"></label>'
       . '<label class="qt-f"><span>Nhập lại mật khẩu</span><input type="password" name="pw2" required minlength="10" autocomplete="new-password"></label></div>'
       . '<p class="qt-note">Chị dùng mật khẩu riêng cho trang này, không dùng lại mật khẩu DirectAdmin hay email. Quên mật khẩu thì dán lại khoá GitHub để đặt mật khẩu mới.</p>'
       . '<button class="qt-btn main" type="submit">Hoàn tất cài đặt</button></div></div></form></div>';
    layout('Cài đặt lần đầu', '', $b, array('cls' => 'auth'));
}

function page_login() {
    $b = '<div class="qt-auth"><form class="qt-card qt-form" data-api="dang-nhap" data-next="./" autocomplete="on">'
       . '<p class="qt-eye">MeDili Café · Quản trị web</p><h1>Đăng nhập</h1>'
       . '<label class="qt-f"><span>Tên đăng nhập</span><input name="u" required autocomplete="username" autocapitalize="none" spellcheck="false"></label>'
       . '<label class="qt-f"><span>Mật khẩu</span><input type="password" name="pw" required autocomplete="current-password"></label>'
       . '<button class="qt-btn main wide" type="submit">Đăng nhập</button>'
       . '<p class="qt-note"><a href="?t=quen">Quên mật khẩu?</a></p></form></div>';
    layout('Đăng nhập', '', $b, array('cls' => 'auth'));
}

function page_recover() {
    $b = '<div class="qt-auth"><form class="qt-card qt-form" data-api="quen" data-next="./" autocomplete="off">'
       . '<p class="qt-eye">Quên mật khẩu</p><h1>Đặt lại mật khẩu</h1>'
       . '<p class="qt-note"><b>Tài khoản chủ:</b> tạo một khoá GitHub mới như lúc cài đặt (Contents: Read and write, Actions: Read-only), dán vào ô dưới và đặt mật khẩu mới. Khoá mới thay khoá cũ.</p>'
       . '<p class="qt-note"><b>Nhân viên:</b> nhờ chị chủ đặt lại mật khẩu ở mục Tài khoản.</p>'
       . '<label class="qt-f"><span>Khoá GitHub</span><input type="password" name="token" required autocomplete="off" spellcheck="false" placeholder="github_pat_…"></label>'
       . '<label class="qt-f"><span>Mật khẩu mới</span><input type="password" name="pw" required minlength="10" autocomplete="new-password"></label>'
       . '<label class="qt-f"><span>Nhập lại mật khẩu mới</span><input type="password" name="pw2" required minlength="10" autocomplete="new-password"></label>'
       . '<button class="qt-btn main wide" type="submit">Đặt mật khẩu mới</button><p class="qt-note"><a href="./">← Về trang đăng nhập</a></p></form></div>';
    layout('Quên mật khẩu', '', $b, array('cls' => 'auth'));
}

// ---------------------------------------------------------------- tổng quan
function page_dashboard() {
    $u = current_user();
    $b = page_head('Tổng quan', 'Chào ' . h($u['ten']) . '. <em>Hôm nay sửa gì cho web?</em>',
        'Mỗi lần bấm Lưu, web medili.vn cập nhật sau khoảng 3–5 phút, cả bản tiếng Anh, Nhật, Trung. Chữ mới viết được dịch tự động mỗi tối.');
    try {
        $cd = data_json(F_CAIDAT); $sp = data_json(F_SP); $tin = data_json(F_TIN) ?: array(); $anh = data_json(F_ANH); $clip = data_json(F_CLIP);
        $tb = $cd['thong_bao'];
        $het = 0; foreach ($sp as $x) if ($x['st'] === 'het') $het++;
        $hien = 0; $nhap = 0; foreach ($tin as $p) { if (!empty($p['nhap'])) $nhap++; elseif (empty($p['an'])) $hien++; }
        $na = 0; foreach ($anh['anh'] as $a) if (empty($a['an'])) $na++;
        $tiles = array(
            array('thong-bao', 'loa', 'Thông báo & liên hệ', $tb['bat'] ? 'Đang hiện: “' . h(mb_substr($tb['chu'], 0, 60)) . (mb_strlen($tb['chu']) > 60 ? '…' : '') . '”' : 'Đang tắt thanh thông báo', $tb['bat'] ? 'on' : ''),
            array('san-pham', 'tui', 'Sản phẩm & giá', count($sp) . ' dòng cà phê' . ($het ? " · <b>$het dòng tạm hết hàng</b>" : ''), ''),
            array('tin-tuc', 'bao', 'Tin tức', "$hien bài đang hiện" . ($nhap ? " · $nhap bài nháp" : ''), ''),
            array('anh', 'anh', 'Ảnh vườn', "$na ảnh đang hiện · " . count($anh['vung_trong']) . ' ảnh ở trang Vùng trồng', ''),
            array('video', 'phim', 'Video', !empty($clip['an']) ? 'Clip đang ẩn' : 'Clip “Một mùa ở vườn Di Linh” đang hiện', ''),
            array('tai-khoan', 'nguoi', 'Tài khoản', count(users()) . ' tài khoản', ''),
        );
        $g = '';
        foreach ($tiles as $t) $g .= '<a class="qt-tile ' . $t[4] . '" href="?t=' . $t[0] . '">' . icon($t[1]) . '<b>' . h($t[2]) . '</b><span>' . $t[3] . '</span></a>';
        $b .= '<div class="qt-tiles">' . $g . '</div>';
    } catch (QtError $e) { $b .= err_box($e); }
    $rows = '';
    foreach (array_slice(audit_rows(60), 0, 8) as $r) {
        $rows .= '<li><time>' . h(date('d/m H:i', strtotime($r['t']))) . '</time><span><b>' . h($r['ten'] ?: $r['u']) . '</b> ' . h($r['mo_ta']) . '</span></li>';
    }
    $b .= card('Việc gần đây', $rows ? '<ul class="qt-feed">' . $rows . '</ul><p class="qt-note"><a href="?t=nhat-ky">Xem cả nhật ký →</a></p>' : '<p class="qt-note">Chưa có thay đổi nào.</p>');
    layout('Tổng quan', '', $b);
}

// ---------------------------------------------------------------- thông báo và liên hệ
function page_notice() {
    $b = page_head('Thông báo & liên hệ', 'Thanh thông báo <em>và thông tin liên hệ.</em>',
        'Thanh thông báo hiện trên đầu mọi trang của web (nghỉ lễ, khuyến mãi, đổi giờ giao hàng…). Khách bấm × thì thanh ẩn với khách đó.');
    try { $cd = data_json(F_CAIDAT); } catch (QtError $e) { layout('Thông báo', 'thong-bao', $b . err_box($e)); return; }
    $tb = $cd['thong_bao']; $lh = $cd['lien_he'];
    $opt = '<option value="">Không gắn link</option>';
    $custom = $tb['link'] !== '' && !array_key_exists($tb['link'], TRANG);
    foreach (TRANG as $f => $n) $opt .= '<option value="' . h($f) . '"' . ($tb['link'] === $f ? ' selected' : '') . '>' . h($n) . '</option>';
    $opt .= '<option value="*"' . ($custom ? ' selected' : '') . '>Địa chỉ khác (https://…)</option>';
    $f = '<form class="qt-form" data-api="thong-bao" data-confirm-off="1">'
       . '<input type="hidden" name="v" value="' . h(item_ver($tb)) . '">'
       . '<label class="qt-switch"><input type="checkbox" name="bat"' . ($tb['bat'] ? ' checked' : '') . '><span></span><b>Hiện thanh thông báo trên web</b></label>'
       . '<label class="qt-f"><span>Nội dung <small data-dem="220"></small></span><textarea name="chu" rows="2" maxlength="220" placeholder="Vd. MeDili nghỉ Tết từ 14/2 đến 20/2, đơn đặt trong thời gian này giao từ 21/2.">' . h($tb['chu']) . '</textarea></label>'
       . '<fieldset class="qt-f"><legend>Kiểu</legend><div class="qt-seg">'
       . '<label><input type="radio" name="kieu" value="thuong"' . ($tb['kieu'] !== 'quan-trong' ? ' checked' : '') . '><span>Thường · nền vàng đất</span></label>'
       . '<label><input type="radio" name="kieu" value="quan-trong"' . ($tb['kieu'] === 'quan-trong' ? ' checked' : '') . '><span>Quan trọng · nền đỏ nâu</span></label></div></fieldset>'
       . '<div class="qt-grid2"><label class="qt-f"><span>Gắn link</span><select name="link_chon">' . $opt . '</select></label>'
       . '<label class="qt-f"><span>Chữ trên link</span><input name="chu_link" maxlength="40" value="' . h($tb['chu_link']) . '" placeholder="Xem chi tiết"></label></div>'
       . '<label class="qt-f" data-link-khac' . ($custom ? '' : ' hidden') . '><span>Địa chỉ link</span><input name="link_url" inputmode="url" value="' . h($custom ? $tb['link'] : '') . '" placeholder="https://…"></label>'
       . '<div class="qt-grid2"><label class="qt-f"><span>Hiện từ ngày <small>(trống = hiện ngay)</small></span><input type="date" name="tu" value="' . h($tb['tu']) . '"></label>'
       . '<label class="qt-f"><span>Đến hết ngày <small>(trống = không hết hạn)</small></span><input type="date" name="den" value="' . h($tb['den']) . '"></label></div>'
       . '<p class="qt-k">Xem trước</p><div class="qt-tb-prev" data-tb-prev><aside class="mdtb"><p></p><i aria-hidden="true">×</i></aside></div>'
       . '<div class="qt-actions"><button class="qt-btn main" type="submit">Lưu thông báo</button></div></form>';
    $b .= card('Thanh thông báo', $f);
    $own = is_owner();
    $dis = $own ? '' : ' disabled';
    $c = '<form class="qt-form" data-api="lien-he" data-confirm="Thông tin liên hệ mới sẽ thay trên mọi trang của web, cả bản tiếng Anh, Nhật, Trung. Chị chắc chắn chứ?">'
       . '<input type="hidden" name="v" value="' . h(item_ver($lh)) . '">'
       . ($own ? '' : '<p class="qt-alert">Chỉ tài khoản chủ sửa được thông tin liên hệ, để tránh đổi nhầm số nhận đơn.</p>')
       . '<div class="qt-grid2"><label class="qt-f"><span>Số điện thoại, Zalo</span><input name="dien_thoai" inputmode="tel" required value="' . h($lh['dien_thoai']) . '"' . $dis . '></label>'
       . '<label class="qt-f"><span>Email</span><input type="email" name="email" required value="' . h($lh['email']) . '"' . $dis . '></label>'
       . '<label class="qt-f"><span>Link Zalo</span><input name="zalo" inputmode="url" required value="' . h($lh['zalo']) . '"' . $dis . '></label>'
       . '<label class="qt-f"><span>Link Facebook</span><input name="facebook" inputmode="url" required value="' . h($lh['facebook']) . '"' . $dis . '></label>'
       . '<label class="qt-f"><span>Trả lời Zalo từ</span><input type="time" name="gio0" required value="' . h(str_pad($lh['gio_zalo'][0], 5, '0', STR_PAD_LEFT)) . '"' . $dis . '></label>'
       . '<label class="qt-f"><span>đến</span><input type="time" name="gio1" required value="' . h(str_pad($lh['gio_zalo'][1], 5, '0', STR_PAD_LEFT)) . '"' . $dis . '></label></div>'
       . '<p class="qt-note">Giờ trả lời Zalo đang ghi trong câu “MeDili phản hồi qua Zalo trong 60 phút, từ 6:30 đến 22:30”. Địa chỉ cửa hàng và xưởng rang có trong nhiều bài viết, chị nhắn em (Claude) khi cần đổi.</p>'
       . ($own ? '<div class="qt-actions"><button class="qt-btn main" type="submit">Lưu thông tin liên hệ</button></div>' : '') . '</form>';
    $b .= card('Thông tin liên hệ', $c);
    layout('Thông báo & liên hệ', 'thong-bao', $b);
}

// ---------------------------------------------------------------- sản phẩm
function page_products() {
    $b = page_head('Sản phẩm & giá', 'Giá, tình trạng hàng <em>và lời mô tả.</em>',
        'Giá nhập bằng đồng. Giá trên web chưa gồm 8% VAT và phí giao. Đổi xong bấm Lưu ở thanh dưới cùng; web cập nhật cửa hàng, trang sản phẩm, Phòng chọn mua, Tìm gu, HORECA.');
    try { $sp = data_json(F_SP); } catch (QtError $e) { layout('Sản phẩm & giá', 'san-pham', $b . err_box($e)); return; }
    $groups = array('core' => array('Robusta, Arabica, Blend', 'Giá theo kg: giá lẻ dưới 5 kg, sỉ 5–20 kg/tháng, sỉ trên 20 kg/tháng. Dòng này cần đủ 3 mức giá.'),
                    'le' => array('Blend MeDili và cà phê đặc sản', 'Để trống giá lẻ thì web ghi “Liên hệ”. Giá sỉ nhập đủ hai mức hoặc để trống cả hai.'),
                    'ngu' => array('Bộ sưu tập Ngũ Hành', 'Giá theo túi 250 g.'),
                    'sap' => array('Sắp mở bán', 'Đổi sang “Đang bán” và nhập giá lẻ theo kg khi mở bán.'));
    foreach ($groups as $g => $info) {
        $rows = '';
        foreach ($sp as $id => $x) {
            if ($x['loai'] !== $g) continue;
            $rows .= product_row($id, $x);
        }
        $b .= card(h($info[0]), '<div class="qt-prods">' . $rows . '</div>', 'qt-pgrp', h($info[1]));
    }
    $b .= '<div class="qt-savebar" id="qt-savebar" hidden><span data-dem-sua></span><button type="button" class="qt-btn" data-act="bo-sua">Bỏ thay đổi</button><button type="button" class="qt-btn main" data-act="luu-sp">Lưu thay đổi</button></div>';
    layout('Sản phẩm & giá', 'san-pham', $b, array('js' => 'trang-sp.js'));
}

function product_row($id, $x) {
    $loai = $x['loai'];
    $p = $x['p'] ?: array();
    $money = function ($k, $mul) use ($p) { return isset($p[$k]) && $p[$k] !== null ? fmt_money($p[$k] * $mul) : ''; };
    $in = function ($name, $label, $val, $req = false) {
        return '<label class="qt-f qt-money"><span>' . $label . '</span><span class="qt-in-u"><input name="' . $name . '" inputmode="numeric" autocomplete="off" value="' . h($val) . '"' . ($req ? ' required' : '') . '><i>đ</i></span></label>';
    };
    if ($loai === 'ngu') $prices = $in('p0', 'Giá túi 250 g', $money(0, 250), true);
    elseif ($loai === 'sap') $prices = $in('p0', 'Giá lẻ mỗi kg', $money(0, 1000));
    else $prices = $in('p0', 'Giá lẻ / kg', $money(0, 1000), $loai === 'core') . $in('p1', 'Sỉ 5–20 kg', $money(1, 1000), $loai === 'core') . $in('p2', 'Sỉ trên 20 kg', $money(2, 1000), $loai === 'core');
    $sts = $loai === 'sap' ? array('sap' => 'Sắp mở bán', 'ban' => 'Đang bán', 'het' => 'Tạm hết hàng') : array('ban' => 'Đang bán', 'het' => 'Tạm hết hàng');
    $st = $x['st'] === 'lh' ? 'ban' : $x['st'];
    $so = ''; foreach ($sts as $k => $t) $so .= '<option value="' . $k . '"' . ($k === $st ? ' selected' : '') . '>' . $t . '</option>';
    $text = '';
    foreach (array('head' => 'Câu giới thiệu', 'taste' => 'Hương vị', 'use' => 'Cách dùng', 'fit' => 'Phù hợp với') as $f => $lab) {
        if ($loai === 'sap' && $f === 'use') continue;
        $text .= '<label class="qt-f"><span>' . $lab . '</span><input name="' . $f . '" maxlength="200" value="' . h($x[$f]) . '"></label>';
    }
    return '<article class="qt-prod" data-id="' . h($id) . '" data-loai="' . $loai . '" data-v="' . h(item_ver($x)) . '">'
         . '<div class="qt-prod-hd"><h3>' . h($x['ten']) . '</h3><span class="qt-chip">' . h($x['nhom']) . '</span><a class="qt-ext" href="../sp-' . h(sp_slug($id)) . '.html" target="_blank" rel="noopener" aria-label="Xem trang ' . h($x['ten']) . '">' . icon('mo') . '</a></div>'
         . '<div class="qt-prod-bd"><label class="qt-f qt-st"><span>Tình trạng</span><select name="st">' . $so . '</select></label>' . $prices . '</div>'
         . '<details class="qt-more"><summary>Lời mô tả trên trang sản phẩm</summary><div class="qt-grid2">' . $text . '</div></details></article>';
}

function sp_slug($id) {
    $m = array('pc' => 'phin-robusta-classic', 'pp' => 'phin-robusta-premium', 'mc' => 'may-robusta-classic', 'mp' => 'may-robusta-premium',
        'ms' => 'may-robusta-specialty', 'pa' => 'phin-arabica-premium', 'ma' => 'may-arabica-premium', 'b91' => 'may-blend-premium-9-1', 'b82' => 'may-blend-premium-8-2',
        'b73' => 'may-blend-premium-7-3', 'b55' => 'may-blend-premium-5-5', 'bm' => 'blend-medili', 'cat' => 'catimor', 'cul' => 'culi',
        'ng-suong' => 'ngu-hanh-suong', 'ng-rung' => 'ngu-hanh-rung', 'ng-suoi' => 'ngu-hanh-suoi', 'ng-nang' => 'ngu-hanh-nang', 'ng-nui' => 'ngu-hanh-nui', 'ng-may' => 'ngu-hanh-may',
        'frd' => 'fine-robusta-di-linh', 'rh' => 'fine-robusta-honey-di-linh', 'acd' => 'arabica-cau-dat', 'sig' => 'signature-coffee', 'an' => 'arabica-natural-cau-dat', 'aw' => 'arabica-washed-cau-dat');
    return isset($m[$id]) ? $m[$id] : $id;
}

// ---------------------------------------------------------------- tin tức
function page_news() {
    $b = page_head('Tin tức', 'Bài tin tức <em>trên medili.vn.</em>', 'Bài tự soạn mỗi sáng vẫn duyệt ở trang Duyệt bài như cũ. Ở đây chị viết bài mới, sửa, ẩn hoặc hiện lại bài đã đăng.',
        '<a class="qt-btn main" href="?t=bai">' . icon('cong') . 'Viết bài mới</a>');
    try { $L = data_json(F_TIN) ?: array(); } catch (QtError $e) { layout('Tin tức', 'tin-tuc', $b . err_box($e)); return; }
    usort($L, function ($a, $b) { return strcmp($b['date'] . $b['slug'], $a['date'] . $a['slug']); });
    $rows = '';
    foreach ($L as $p) {
        $st = !empty($p['nhap']) ? array('nhap', 'Nháp') : (!empty($p['an']) ? array('an', 'Đã ẩn') : array('hien', 'Đang hiện'));
        $acts = '<a class="qt-btn small" href="?t=bai&amp;s=' . h(rawurlencode($p['slug'])) . '">Sửa</a>';
        if ($st[0] === 'hien') $acts .= '<button type="button" class="qt-btn small" data-bai="an">Ẩn</button><a class="qt-btn small ghost" href="../tin-tuc-' . h($p['slug']) . '.html" target="_blank" rel="noopener">' . icon('mo') . 'Xem</a>';
        if ($st[0] === 'an') $acts .= '<button type="button" class="qt-btn small" data-bai="hien">Hiện lại</button>';
        if ($st[0] === 'nhap') $acts .= '<button type="button" class="qt-btn small main" data-bai="dang">Đăng</button>';
        if (is_owner()) $acts .= '<button type="button" class="qt-btn small danger" data-bai="xoa" aria-label="Xóa bài">' . icon('xoa') . '</button>';
        $rows .= '<li class="qt-post" data-slug="' . h($p['slug']) . '" data-v="' . h(item_ver($p)) . '" data-q="' . h(mb_strtolower($p['title'] . ' ' . $p['slug'])) . '">'
               . '<div><span class="qt-badge ' . $st[0] . '">' . $st[1] . '</span><time>' . h(vn_date($p['date'])) . '</time><h3>' . h($p['title']) . '</h3><p>' . h($p['desc']) . '</p></div>'
               . '<div class="qt-post-act">' . $acts . '</div></li>';
    }
    $b .= card('', '<label class="qt-f qt-search"><span class="sr">Tìm bài</span><input type="search" data-loc placeholder="Tìm theo tiêu đề…"></label><ul class="qt-posts">' . ($rows ?: '<li class="qt-note">Chưa có bài nào.</li>') . '</ul>');
    layout('Tin tức', 'tin-tuc', $b, array('js' => 'trang-tin.js'));
}

function page_post($slug) {
    $p = null;
    if ($slug !== '') {
        try { $L = data_json(F_TIN) ?: array(); } catch (QtError $e) { layout('Sửa bài', 'tin-tuc', err_box($e)); return; }
        foreach ($L as $x) if ($x['slug'] === $slug) $p = $x;
        if (!$p) { layout('Sửa bài', 'tin-tuc', '<div class="qt-alert loi">Không thấy bài này. <a href="?t=tin-tuc">Về danh sách</a></div>'); return; }
    }
    $isNew = !$p;
    $p = $p ?: array('slug' => '', 'date' => date('Y-m-d'), 'title' => '', 'desc' => '', 'keywords' => array(), 'body' => array(), 'cta' => '', 'sources' => array());
    $draft = $isNew || !empty($p['nhap']);
    $src = '';
    $list = $p['sources'] ?: array();
    $list[] = array('name' => '', 'url' => '');
    foreach ($list as $s) $src .= '<div class="qt-src"><input name="src_name" maxlength="200" placeholder="Tên báo – tên bài" value="' . h($s['name']) . '"><input name="src_url" inputmode="url" placeholder="https://…" value="' . h(isset($s['url']) ? $s['url'] : '') . '"><button type="button" class="qt-btn small ghost" data-act="bo-nguon" aria-label="Bỏ nguồn này">' . icon('xoa') . '</button></div>';
    $b = page_head('Tin tức', $isNew ? 'Viết bài <em>mới.</em>' : 'Sửa bài <em>' . (!empty($p['nhap']) ? 'nháp' : 'đã đăng') . '.</em>', '', '<a class="qt-btn ghost" href="?t=tin-tuc">← Danh sách bài</a>');
    $f = '<form class="qt-form qt-post-f" data-api="bai-luu" data-next="?t=tin-tuc" data-slug="' . h($p['slug']) . '">'
       . '<input type="hidden" name="v" value="' . h($isNew ? '' : item_ver($p)) . '">'
       . '<label class="qt-f"><span>Tiêu đề <small data-dem="120"></small></span><input name="title" required maxlength="120" value="' . h($p['title']) . '" placeholder="Viết hoa chữ đầu câu, dưới 65 ký tự là đẹp nhất trên Google"></label>'
       . '<div class="qt-grid2"><label class="qt-f"><span>Ngày đăng</span><input type="date" name="date" required value="' . h($p['date']) . '"></label>'
       . '<label class="qt-f"><span>Đường dẫn</span><output class="qt-slug" data-slug-out>' . h($p['slug'] ? 'tin-tuc-' . $p['slug'] . '.html' : 'tự tạo theo tiêu đề') . '</output></label></div>'
       . '<label class="qt-f"><span>Mô tả ngắn <small data-dem="200"></small></span><textarea name="desc" rows="2" maxlength="200" placeholder="Hiện ở danh sách tin và trên Google">' . h($p['desc']) . '</textarea></label>'
       . '<label class="qt-f"><span>Nội dung <small>Mỗi đoạn cách nhau một dòng trống. Dòng bắt đầu bằng ## là tiêu đề nhỏ.</small></span><textarea name="body" rows="16" required>' . h(news_text($p['body'])) . '</textarea></label>'
       . '<details class="qt-more" data-xem-truoc><summary>Xem trước bài</summary><article class="qt-preview"></article></details>'
       . '<label class="qt-f"><span>Lời mời cuối bài <small>(tùy chọn, hiện kèm nút Đặt cà phê qua Zalo)</small></span><textarea name="cta" rows="2" maxlength="300">' . h($p['cta']) . '</textarea></label>'
       . '<fieldset class="qt-f"><legend>Nguồn tin <small>(ghi rõ báo gốc khi dùng tin của báo khác)</small></legend><div class="qt-srcs">' . $src . '</div>'
       . '<button type="button" class="qt-btn small" data-act="them-nguon">' . icon('cong') . 'Thêm nguồn</button></fieldset>'
       . '<label class="qt-f"><span>Từ khóa <small>(cách nhau bằng dấu phẩy)</small></span><input name="keywords" maxlength="300" value="' . h(implode(', ', $p['keywords'])) . '"></label>'
       . '<div class="qt-actions">'
       . ($draft ? '<button class="qt-btn" type="submit" name="nhap" value="1">Lưu nháp</button><button class="qt-btn main" type="submit" name="nhap" value="0">Đăng bài</button>'
                 : '<button class="qt-btn main" type="submit" name="nhap" value="0">Lưu thay đổi</button>')
       . '</div></form>';
    $b .= card('', $f);
    layout($isNew ? 'Viết bài mới' : 'Sửa bài', 'tin-tuc', $b, array('js' => 'trang-tin.js'));
}

// ---------------------------------------------------------------- ảnh vườn
function page_gallery() {
    $b = page_head('Ảnh vườn', 'Ảnh vườn <em>và trang Vùng trồng.</em>',
        'Ảnh mới được thu nhỏ và đóng logo MeDili ngay trên máy của chị trước khi tải lên, không mang theo vị trí chụp. Chọn ảnh rõ, không có người lạ chụp rõ mặt.');
    try { $d = data_json(F_ANH); } catch (QtError $e) { layout('Ảnh vườn', 'anh', $b . err_box($e)); return; }
    $gopt = ''; foreach ($d['nhom'] as $g) $gopt .= '<option value="' . h($g['ma']) . '">' . h($g['ten']) . '</option>';
    $add = '<div class="qt-up" data-up><label class="qt-drop"><input type="file" accept="image/jpeg,image/png,image/webp,image/heic" multiple data-chon-anh>'
         . icon('anh') . '<b>Chọn ảnh từ máy</b><span>JPG hoặc PNG, tối đa 20 ảnh mỗi lần. Ảnh được thu còn cạnh dài 1.600 điểm ảnh.</span></label>'
         . '<label class="qt-f qt-up-g"><span>Đưa vào nhóm</span><select data-nhom-moi>' . $gopt . '</select></label>'
         . '<div class="qt-up-list" data-up-list></div>'
         . '<div class="qt-actions" data-up-act hidden><button type="button" class="qt-btn" data-act="bo-anh-moi">Bỏ</button><button type="button" class="qt-btn main" data-act="tai-anh">Tải ảnh lên web</button></div></div>';
    $b .= card('Thêm ảnh', $add);
    $vt = array_flip($d['vung_trong']);
    foreach ($d['nhom'] as $g) {
        $cells = '';
        foreach ($d['anh'] as $a) {
            if ($a['nhom'] !== $g['ma']) continue;
            $cells .= '<figure class="qt-ph' . (!empty($a['an']) ? ' an' : '') . (isset($vt[$a['ten']]) ? ' vt' : '') . '" data-ten="' . h($a['ten']) . '" data-v="' . h(item_ver($a)) . '" data-nhom="' . h($a['nhom']) . '">'
                    . '<div class="qt-ph-img"><img src="' . h(asset_url('g-' . $a['ten'] . '-s.jpg')) . '" alt="" loading="lazy">'
                    . '<span class="qt-ph-tag an">Đang ẩn</span><span class="qt-ph-tag vt">' . icon('sao') . 'Vùng trồng</span></div>'
                    . '<figcaption><label class="qt-f"><span>Chú thích</span><input name="cap" maxlength="120" value="' . h($a['cap']) . '"></label>'
                    . '<details class="qt-more"><summary>Mô tả ảnh, nhóm</summary><label class="qt-f"><span>Mô tả cho người khiếm thị, Google</span><textarea name="alt" rows="2" maxlength="200">' . h($a['alt']) . '</textarea></label>'
                    . '<label class="qt-f"><span>Nhóm</span><select name="nhom">' . str_replace('value="' . h($a['nhom']) . '"', 'value="' . h($a['nhom']) . '" selected', $gopt) . '</select></label></details>'
                    . '<div class="qt-ph-act"><button type="button" class="qt-ic" data-act="len" aria-label="Đưa lên trước">' . icon('len') . '</button><button type="button" class="qt-ic" data-act="xuong" aria-label="Đưa xuống sau">' . icon('xuong') . '</button>'
                    . '<button type="button" class="qt-ic" data-act="vt" aria-pressed="' . (isset($vt[$a['ten']]) ? 'true' : 'false') . '" aria-label="Hiện ở trang Vùng trồng">' . icon('sao') . '</button>'
                    . '<button type="button" class="qt-ic" data-act="an" aria-pressed="' . (!empty($a['an']) ? 'true' : 'false') . '" aria-label="Ẩn ảnh khỏi web"><span class="i-on">' . icon('mat') . '</span><span class="i-off">' . icon('mat-gach') . '</span></button>'
                    . (is_owner() ? '<button type="button" class="qt-ic danger" data-act="xoa" aria-label="Xóa ảnh">' . icon('xoa') . '</button>' : '') . '</div></figcaption></figure>';
        }
        $b .= '<section class="qt-card qt-gal" data-nhom="' . h($g['ma']) . '"><div class="qt-card-hd"><h2>' . h($g['ten']) . ' <small data-dem-nhom></small></h2><p>' . h(strip_tags($g['h2'])) . '</p></div><div class="qt-phs">' . $cells . '</div></section>';
    }
    $b .= '<p class="qt-note">' . icon('sao') . ' Ảnh có sao hiện ở trang Vùng trồng Di Linh (tối đa 12 ảnh, <span data-dem-vt>' . count($d['vung_trong']) . '</span>/12), theo thứ tự chị chọn sao. Ảnh ẩn không hiện trên web nhưng vẫn giữ ở đây.</p>';
    $b .= '<div class="qt-savebar" id="qt-savebar" hidden><span data-dem-sua></span><button type="button" class="qt-btn" data-act="bo-sua">Bỏ thay đổi</button><button type="button" class="qt-btn main" data-act="luu-anh">Lưu thay đổi</button></div>';
    $b .= '<script type="application/json" id="qt-vt">' . json_encode($d['vung_trong']) . '</script>';
    layout('Ảnh vườn', 'anh', $b, array('js' => 'trang-anh.js'));
}

// ---------------------------------------------------------------- video
function page_video() {
    $b = page_head('Video', 'Clip ở trang <em>Vùng trồng Di Linh.</em>', 'Clip chạy không tiếng khi khách cuộn tới, bên cạnh là danh sách cảnh để bấm xem lại.');
    try { $d = data_json(F_CLIP); } catch (QtError $e) { layout('Video', 'video', $b . err_box($e)); return; }
    $rows = '';
    foreach ($d['canh'] as $i => $c) {
        $rows .= '<div class="qt-scene" data-i="' . $i . '"><img src="' . h(asset_url($c['anh'])) . '" alt="" width="128" height="72" loading="lazy">'
               . '<label class="qt-f qt-sec"><span>Giây</span><input name="t" inputmode="decimal" value="' . h($c['t']) . '"></label>'
               . '<label class="qt-f"><span>Tên cảnh</span><input name="cap" maxlength="90" value="' . h($c['cap']) . '"></label></div>';
    }
    $f = '<form class="qt-form" data-api="clip-luu" data-v="' . h(item_ver($d)) . '">'
       . '<div class="qt-vid"><video controls muted playsinline preload="metadata" poster="' . h(asset_url($d['poster'])) . '" src="' . h(asset_url($d['sd'])) . '"></video></div>'
       . '<label class="qt-switch"><input type="checkbox" name="hien"' . (empty($d['an']) ? ' checked' : '') . '><span></span><b>Hiện clip ở trang Vùng trồng</b></label>'
       . '<label class="qt-f"><span>Lời giới thiệu <small data-dem="400"></small></span><textarea name="lead" rows="3" maxlength="400">' . h($d['lead']) . '</textarea></label>'
       . '<label class="qt-f"><span>Mô tả clip cho người khiếm thị <small data-dem="300"></small></span><textarea name="label" rows="2" maxlength="300">' . h($d['label']) . '</textarea></label>'
       . '<p class="qt-k">Các cảnh trong clip</p><div class="qt-scenes" data-scenes>' . $rows . '</div>'
       . '<div class="qt-actions"><button class="qt-btn main" type="submit">Lưu clip</button></div></form>';
    $b .= card('Clip đang dùng', $f);
    $n = '<div class="qt-newvid" data-newvid><label class="qt-drop"><input type="file" accept="video/mp4" data-chon-video>' . icon('phim')
       . '<b>Chọn video MP4</b><span>Tối đa 40 MB, nên dài 20–60 giây, quay ngang. Video được dùng nguyên bản, không có tiếng trên web.</span></label>'
       . '<div data-nv-body hidden><div class="qt-vid"><video controls muted playsinline preload="metadata" data-nv-video></video></div>'
       . '<div class="qt-actions left"><button type="button" class="qt-btn" data-act="nv-poster">Lấy ảnh chờ tại đây</button><button type="button" class="qt-btn" data-act="nv-canh">' . icon('cong') . 'Đánh dấu cảnh tại đây</button></div>'
       . '<div class="qt-grid2"><div><p class="qt-k">Ảnh chờ</p><canvas class="qt-poster" data-nv-poster width="320" height="180"></canvas></div><div><p class="qt-k">Các cảnh <small>(tối đa 8)</small></p><div class="qt-scenes" data-nv-scenes></div></div></div>'
       . '<div class="qt-prog" data-nv-prog hidden><i></i><span></span></div>'
       . '<div class="qt-actions"><button type="button" class="qt-btn" data-act="nv-bo">Bỏ</button><button type="button" class="qt-btn main" data-act="nv-luu">Tải lên và thay clip</button></div></div></div>';
    $b .= card('Thay clip mới', $n, '', 'Clip mới thay clip đang dùng. Lời giới thiệu và mô tả ở trên giữ nguyên, chị sửa lại cho khớp clip mới.');
    layout('Video', 'video', $b, array('js' => 'trang-video.js'));
}

// ---------------------------------------------------------------- tài khoản
function page_accounts() {
    $u = current_user();
    $b = page_head('Tài khoản', 'Tài khoản <em>quản trị.</em>', 'Mỗi người một tài khoản. Nhân viên sửa được nội dung, không xóa bài, xóa ảnh, không đổi thông tin liên hệ và không quản lý tài khoản.');
    $me = '<form class="qt-form" data-api="mk-doi" data-reset="1"><p class="qt-note">Đang đăng nhập: <b>' . h($u['ten']) . '</b> (' . h($u['u']) . ', ' . ($u['vai'] === 'chu' ? 'chủ' : 'nhân viên') . ').</p>'
        . '<div class="qt-grid3"><label class="qt-f"><span>Mật khẩu hiện tại</span><input type="password" name="cu" required autocomplete="current-password"></label>'
        . '<label class="qt-f"><span>Mật khẩu mới</span><input type="password" name="moi" required minlength="10" autocomplete="new-password"></label>'
        . '<label class="qt-f"><span>Nhập lại mật khẩu mới</span><input type="password" name="moi2" required minlength="10" autocomplete="new-password"></label></div>'
        . '<div class="qt-actions"><button class="qt-btn main" type="submit">Đổi mật khẩu</button></div></form>';
    $b .= card('Mật khẩu của tôi', $me);
    if (is_owner()) {
        $rows = '';
        foreach (users() as $x) {
            $self = $x['u'] === $u['u'];
            $rows .= '<tr data-u="' . h($x['u']) . '"><td><b>' . h($x['ten']) . '</b><small>' . h($x['u']) . '</small></td><td>' . ($x['vai'] === 'chu' ? 'Chủ' : 'Nhân viên') . '</td>'
                   . '<td>' . (!empty($x['bat']) ? '<span class="qt-badge hien">Đang dùng</span>' : '<span class="qt-badge an">Đã khoá</span>') . '</td><td>' . h(date('d/m/Y', $x['tao'])) . '</td>'
                   . '<td class="qt-td-act">' . ($self ? '<small>tài khoản của chị</small>' : '<button type="button" class="qt-btn small" data-tk="mk">Đặt lại mật khẩu</button>'
                   . '<button type="button" class="qt-btn small" data-tk="' . (!empty($x['bat']) ? 'khoa' : 'mo') . '">' . (!empty($x['bat']) ? 'Khoá' : 'Mở khoá') . '</button>'
                   . '<button type="button" class="qt-btn small danger" data-tk="xoa" aria-label="Xóa tài khoản">' . icon('xoa') . '</button>') . '</td></tr>';
        }
        $b .= card('Tài khoản đang có', '<div class="qt-table"><table><thead><tr><th>Người dùng</th><th>Vai trò</th><th>Tình trạng</th><th>Tạo ngày</th><th></th></tr></thead><tbody>' . $rows . '</tbody></table></div>');
        $add = '<form class="qt-form" data-api="tk-them" data-reload="1" autocomplete="off"><div class="qt-grid3">'
             . '<label class="qt-f"><span>Tên hiển thị</span><input name="ten" required maxlength="60" placeholder="vd. Lan"></label>'
             . '<label class="qt-f"><span>Tên đăng nhập</span><input name="u" required maxlength="30" pattern="[a-z0-9._\-]{3,30}" autocapitalize="none" spellcheck="false" placeholder="vd. lan"></label>'
             . '<label class="qt-f"><span>Mật khẩu ban đầu</span><input type="text" name="pw" required minlength="10" autocomplete="off" spellcheck="false"></label></div>'
             . '<p class="qt-note">Chị gửi tên đăng nhập và mật khẩu ban đầu cho nhân viên qua Zalo riêng, nhắc đổi mật khẩu sau lần đăng nhập đầu.</p>'
             . '<div class="qt-actions"><button class="qt-btn main" type="submit">' . icon('cong') . 'Thêm nhân viên</button></div></form>';
        $b .= card('Thêm nhân viên', $add);
    }
    layout('Tài khoản', 'tai-khoan', $b, array('js' => 'trang-tk.js'));
}

// ---------------------------------------------------------------- cài đặt, nhật ký
function page_settings() {
    if (!is_owner()) { layout('Cài đặt', 'cai-dat', '<div class="qt-alert">Chỉ tài khoản chủ mở được mục này.</div>'); return; }
    $c = store_get('cau-hinh', array());
    $b = page_head('Cài đặt', 'Khoá GitHub <em>và đồng bộ web.</em>');
    $exp = isset($c['het_han']) ? $c['het_han'] : '';
    $days = $exp ? floor((strtotime($exp) - time()) / 86400) : null;
    $k = '<p>Khoá của tài khoản GitHub <b>' . h(isset($c['gh_user']) ? $c['gh_user'] : '?') . '</b>, cài ngày ' . h(isset($c['luc']) ? date('d/m/Y', $c['luc']) : '?') . '. '
       . ($exp ? 'Hết hạn ngày <b>' . h(date('d/m/Y', strtotime($exp))) . '</b>' . ($days !== null && $days < 30 ? ' <span class="qt-badge an">còn ' . max(0, $days) . ' ngày, chị thay khoá mới</span>' : '') . '.' : 'Không thấy ngày hết hạn.') . '</p>'
       . '<form class="qt-form" data-api="khoa-doi" data-reset="1" autocomplete="off"><label class="qt-f"><span>Khoá mới (Contents: Read and write, Actions: Read-only)</span><input type="password" name="token" required spellcheck="false" placeholder="github_pat_…"></label>'
       . '<div class="qt-actions"><button class="qt-btn main" type="submit">Thay khoá</button></div></form>';
    $b .= card('Khoá GitHub', $k);
    $log = '';
    $lf = qt_dir('sync') . '/sync.log';
    if (is_file($lf)) $log = implode("\n", array_slice(explode("\n", trim(file_get_contents($lf))), -12));
    $s = '<p class="qt-note">Hosting tự lấy web mới từ GitHub mỗi 30 phút. Sau khi lưu ở đây, trang quản trị tự đưa lên ngay khi GitHub dựng xong. Bấm nút dưới nếu cần đồng bộ lại toàn bộ.</p>'
       . '<pre class="qt-log">' . h($log ?: 'Chưa có nhật ký đồng bộ.') . '</pre>'
       . '<div class="qt-actions left"><button type="button" class="qt-btn" data-act="dong-bo">Đồng bộ web ngay</button>'
       . '<a class="qt-btn ghost" href="https://github.com/' . GH_OWNER . '/' . GH_REPO . '/actions" target="_blank" rel="noopener">' . icon('mo') . 'Các lần dựng web trên GitHub</a></div>';
    $b .= card('Đồng bộ medili.vn', $s);
    layout('Cài đặt', 'cai-dat', $b);
}

function page_log() {
    $own = is_owner(); $u = current_user();
    $rows = '';
    foreach (audit_rows(300) as $r) {
        if (!$own && $r['u'] !== $u['u']) continue;
        $rows .= '<tr><td>' . h(date('d/m/Y H:i', strtotime($r['t']))) . '</td><td>' . h($r['ten'] ?: $r['u']) . '</td><td>' . h($r['mo_ta']) . '</td></tr>';
    }
    $b = page_head('Nhật ký', 'Ai sửa gì, <em>lúc nào.</em>', $own ? '' : 'Nhân viên xem được việc của mình.')
       . card('', '<div class="qt-table"><table><thead><tr><th>Lúc</th><th>Người</th><th>Việc</th></tr></thead><tbody>' . ($rows ?: '<tr><td colspan="3">Chưa có.</td></tr>') . '</tbody></table></div>');
    layout('Nhật ký', '', $b);
}

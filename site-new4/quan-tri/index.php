<?php
// Trang quản trị MeDili: medili.vn/quan-tri (27/11/2026). Xem lib.php về cách lưu và đưa lên web.
define('MDQ', 1);
require __DIR__ . '/lib.php';
require __DIR__ . '/du-lieu.php';
require __DIR__ . '/trang.php';

header('X-Frame-Options: DENY');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: same-origin');
header('X-Robots-Tag: noindex, nofollow');
header('Cache-Control: no-store, private');
header('CDN-Cache-Control: no-store');
header('Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()');
header("Content-Security-Policy: default-src 'self'; img-src 'self' data: blob: https://raw.githubusercontent.com; media-src 'self' blob: https://raw.githubusercontent.com; "
     . "style-src 'self' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; script-src 'self'; connect-src 'self'; "
     . "frame-ancestors 'none'; base-uri 'none'; form-action 'self'; object-src 'none'");

if (!is_https() && !is_local() && PHP_SAPI !== 'cli') {
    header('Location: https://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'], true, 301);
    exit;
}

$api = isset($_GET['api']) ? (string)$_GET['api'] : '';
if ($api !== '') { api($api); exit; }

if (!data_ready()) {
    layout('Lỗi', '', '<div class="qt-auth"><div class="qt-alert loi"><b>Chưa tạo được thư mục riêng của trang quản trị.</b> Hosting cần cho phép ghi vào '
        . h(dirname(qt_dir('data'))) . '. Chị nhắn em (Claude) kèm ảnh chụp trang này.</div></div>');
    exit;
}
session_start_qt();
$t = isset($_GET['t']) ? (string)$_GET['t'] : '';
$cfg = store_get('cau-hinh', null);
if (!$cfg || !users()) { page_setup(); exit; }
if (!current_user()) { if ($t === 'quen') page_recover(); else page_login(); exit; }
try {
    switch ($t) {
        case '': page_dashboard(); break;
        case 'thong-bao': page_notice(); break;
        case 'san-pham': page_products(); break;
        case 'tin-tuc': page_news(); break;
        case 'bai': page_post(isset($_GET['s']) ? (string)$_GET['s'] : ''); break;
        case 'anh': page_gallery(); break;
        case 'video': page_video(); break;
        case 'tai-khoan': page_accounts(); break;
        case 'cai-dat': page_settings(); break;
        case 'nhat-ky': page_log(); break;
        default: header('Location: ./'); break;
    }
} catch (QtError $e) {
    layout('Lỗi', '', err_box($e));
}

// ---------------------------------------------------------------- các lệnh gọi từ trình duyệt
function body_json() {
    $ct = isset($_SERVER['CONTENT_TYPE']) ? $_SERVER['CONTENT_TYPE'] : '';
    if (stripos($ct, 'application/json') === 0) {
        $raw = file_get_contents('php://input');
        if (strlen($raw) > 2000000) throw new QtError('Dữ liệu gửi lên quá lớn.', 413);
        $v = json_decode($raw, true);
        if (!is_array($v)) throw new QtError('Dữ liệu gửi lên không đúng.');
        return $v;
    }
    return $_POST;
}

function verify_token($tok) {
    $tok = trim((string)$tok);
    if (!preg_match('~^(github_pat_[A-Za-z0-9_]{30,250}|ghp_[A-Za-z0-9]{30,60})$~', $tok)) throw new QtError('Khoá GitHub chưa đúng dạng. Khoá mới bắt đầu bằng github_pat_ và rất dài, chị sao chép đủ cả chuỗi.');
    $o = array('token' => $tok);
    list($c, $u, $hd) = gh('GET', '/user', null, $o);
    if ($c === 401) throw new QtError('GitHub không nhận khoá này (sai, hết hạn hoặc đã bị xóa).');
    if ($c !== 200) throw new QtError("Chưa kiểm tra được khoá (GitHub trả mã $c), chị thử lại.", 502);
    list($c, $r) = gh('GET', repo_path(''), null, $o);
    if ($c !== 200 || empty($r['permissions']['push'])) throw new QtError('Khoá thuộc tài khoản ' . h($u['login']) . ' nhưng không có quyền ghi vào kho ' . GH_OWNER . '/' . GH_REPO . '. Chị tạo khoá bằng tài khoản chủ kho web.');
    list($c) = gh('POST', repo_path('/git/blobs'), array('content' => 'medili-quan-tri kiểm tra khoá ' . date('c'), 'encoding' => 'utf-8'), $o);
    if ($c !== 201) throw new QtError('Khoá chưa có quyền Contents: Read and write cho kho ' . GH_REPO . '. Chị sửa quyền của khoá trên GitHub rồi dán lại.');
    list($c) = gh('GET', repo_path('/actions/workflows/' . GH_WORKFLOW . '/runs?per_page=1'), null, $o);
    if ($c === 403) throw new QtError('Khoá chưa có quyền Actions: Read-only. Chị thêm quyền này cho khoá trên GitHub rồi dán lại.');
    $exp = isset($hd['github-authentication-token-expiration']) ? $hd['github-authentication-token-expiration'] : '';
    return array('token' => $tok, 'gh_user' => $u['login'], 'het_han' => $exp, 'actions' => $c === 200);
}

function api($api) {
    header('Content-Type: application/json; charset=utf-8');
    try {
        if (!data_ready()) throw new QtError('Chưa tạo được thư mục riêng của trang quản trị trên hosting.', 500);
        session_start_qt();
        $get = array('tien-do');
        if ($_SERVER['REQUEST_METHOD'] !== 'POST' && !in_array($api, $get, true)) throw new QtError('Sai cách gọi.', 405);
        if ($_SERVER['REQUEST_METHOD'] === 'POST') csrf_check();
        $cfg = store_get('cau-hinh', null);
        $setup = !$cfg || !users();
        $in = $_SERVER['REQUEST_METHOD'] === 'POST' ? body_json() : $_GET;
        $public = array('khoa-kiem', 'cai-dat', 'dang-nhap', 'quen');
        if (!in_array($api, $public, true) && !current_user()) throw new QtError('Phiên đăng nhập đã hết, chị đăng nhập lại nhé.', 401);
        if ($setup && !in_array($api, array('khoa-kiem', 'cai-dat'), true)) throw new QtError('Trang quản trị chưa cài đặt xong.', 403);
        $out = api_run($api, $in, $setup);
        echo json_encode(array('ok' => true) + $out, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
    } catch (QtError $e) {
        http_response_code($e->code_http);
        echo json_encode(array('ok' => false, 'loi' => $e->getMessage()), JSON_UNESCAPED_UNICODE);
    } catch (Throwable $e) {
        http_response_code(500);
        @file_put_contents(qt_dir('data') . '/loi.php', (is_file(qt_dir('data') . '/loi.php') ? '' : GUARD) . date('c') . ' ' . $api . ' ' . $e->getMessage() . ' @' . $e->getFile() . ':' . $e->getLine() . "\n", FILE_APPEND);
        echo json_encode(array('ok' => false, 'loi' => 'Máy chủ gặp lỗi. Chị thử lại; nếu vẫn lỗi, chụp màn hình gửi em (Claude).'), JSON_UNESCAPED_UNICODE);
    }
}

function api_run($api, $in, $setup) {
    switch ($api) {
    // ---- cài đặt, đăng nhập
    case 'khoa-kiem':
        if (!$setup && !is_owner()) throw new QtError('Trang quản trị đã cài đặt.', 403);
        throttle_check(array('ip:' . client_ip()));
        try { $k = verify_token(isset($in['token']) ? $in['token'] : ''); } catch (QtError $e) { throttle_fail(array('ip:' . client_ip())); throw $e; }
        return array('gh_user' => $k['gh_user'], 'het_han' => $k['het_han'] ? date('d/m/Y', strtotime($k['het_han'])) : '', 'actions' => $k['actions']);
    case 'cai-dat':
        if (!$setup) throw new QtError('Trang quản trị đã cài đặt.', 403);
        throttle_check(array('ip:' . client_ip()));
        try { $k = verify_token(isset($in['token']) ? $in['token'] : ''); } catch (QtError $e) { throttle_fail(array('ip:' . client_ip())); throw $e; }
        $u = strtolower(trim((string)(isset($in['u']) ? $in['u'] : '')));
        if (!preg_match('~^[a-z0-9._-]{3,30}$~', $u)) throw new QtError('Tên đăng nhập dài 3–30 ký tự, chỉ chữ không dấu, số, dấu chấm, gạch.');
        $ten = txt(isset($in['ten']) ? $in['ten'] : '', 60);
        if ($ten === '') throw new QtError('Chị nhập tên hiển thị.');
        $pw = isset($in['pw']) ? (string)$in['pw'] : '';
        check_password($pw);
        if ($pw !== (isset($in['pw2']) ? (string)$in['pw2'] : '')) throw new QtError('Hai lần nhập mật khẩu chưa khớp.');
        store_edit('tai-khoan', function ($L) use ($u, $ten, $pw) {
            if ($L) throw new QtError('Trang quản trị đã có tài khoản chủ.', 403);
            return array(array('u' => $u, 'ten' => $ten, 'vai' => 'chu', 'hash' => password_hash($pw, PASSWORD_DEFAULT), 'bat' => true, 'tao' => time(), 'pv' => 1));
        });
        store_put('cau-hinh', array('token' => $k['token'], 'gh_user' => $k['gh_user'], 'het_han' => $k['het_han'], 'luc' => time()));
        login($u, $pw);
        audit('cai-dat', 'Cài đặt trang quản trị, khoá GitHub của ' . $k['gh_user']);
        return array();
    case 'dang-nhap':
        login(isset($in['u']) ? $in['u'] : '', isset($in['pw']) ? $in['pw'] : '');
        audit('dang-nhap', 'Đăng nhập');
        return array();
    case 'dang-xuat':
        audit('dang-xuat', 'Đăng xuất');
        logout();
        return array();
    case 'quen':
        throttle_check(array('ip:' . client_ip()));
        try { $k = verify_token(isset($in['token']) ? $in['token'] : ''); } catch (QtError $e) { throttle_fail(array('ip:' . client_ip())); throw $e; }
        $pw = isset($in['pw']) ? (string)$in['pw'] : '';
        check_password($pw);
        if ($pw !== (isset($in['pw2']) ? (string)$in['pw2'] : '')) throw new QtError('Hai lần nhập mật khẩu chưa khớp.');
        $owner = null;
        store_edit('tai-khoan', function ($L) use ($pw, &$owner) {
            foreach ($L as &$x) if ($x['vai'] === 'chu') { $x['hash'] = password_hash($pw, PASSWORD_DEFAULT); $x['pv']++; $x['bat'] = true; $owner = $x['u']; break; }
            return $L;
        });
        if (!$owner) throw new QtError('Không thấy tài khoản chủ.', 500);
        $c = store_get('cau-hinh', array());
        store_put('cau-hinh', array('token' => $k['token'], 'gh_user' => $k['gh_user'], 'het_han' => $k['het_han'], 'luc' => time()) + $c);
        throttle_clear('u:' . $owner);
        login($owner, $pw);
        audit('quen', 'Đặt lại mật khẩu chủ bằng khoá GitHub mới');
        return array();
    case 'khoa-doi':
        need_owner();
        $k = verify_token(isset($in['token']) ? $in['token'] : '');
        store_put('cau-hinh', array('token' => $k['token'], 'gh_user' => $k['gh_user'], 'het_han' => $k['het_han'], 'luc' => time()));
        audit('khoa-doi', 'Thay khoá GitHub (' . $k['gh_user'] . ')');
        return array('bao' => 'Đã thay khoá GitHub.');

    // ---- tài khoản
    case 'mk-doi':
        $u = current_user();
        if (!password_verify((string)(isset($in['cu']) ? $in['cu'] : ''), $u['hash'])) { throttle_fail(array('u:' . $u['u'])); throw new QtError('Mật khẩu hiện tại chưa đúng.'); }
        $pw = (string)(isset($in['moi']) ? $in['moi'] : '');
        check_password($pw);
        if ($pw !== (string)(isset($in['moi2']) ? $in['moi2'] : '')) throw new QtError('Hai lần nhập mật khẩu mới chưa khớp.');
        store_edit('tai-khoan', function ($L) use ($u, $pw) { foreach ($L as &$x) if ($x['u'] === $u['u']) { $x['hash'] = password_hash($pw, PASSWORD_DEFAULT); $x['pv']++; } return $L; });
        $_SESSION['pv'] = (int)$u['pv'] + 1;
        audit('mk-doi', 'Đổi mật khẩu của mình');
        return array('bao' => 'Đã đổi mật khẩu.');
    case 'tk-them':
        need_owner();
        $u = strtolower(trim((string)(isset($in['u']) ? $in['u'] : '')));
        if (!preg_match('~^[a-z0-9._-]{3,30}$~', $u)) throw new QtError('Tên đăng nhập dài 3–30 ký tự, chỉ chữ không dấu, số, dấu chấm, gạch.');
        $ten = txt(isset($in['ten']) ? $in['ten'] : '', 60);
        if ($ten === '') throw new QtError('Chị nhập tên hiển thị.');
        $pw = (string)(isset($in['pw']) ? $in['pw'] : '');
        check_password($pw);
        store_edit('tai-khoan', function ($L) use ($u, $ten, $pw) {
            foreach ($L as $x) if ($x['u'] === $u) throw new QtError('Tên đăng nhập này đã có.');
            if (count($L) >= 20) throw new QtError('Đã đủ 20 tài khoản.');
            $L[] = array('u' => $u, 'ten' => $ten, 'vai' => 'nv', 'hash' => password_hash($pw, PASSWORD_DEFAULT), 'bat' => true, 'tao' => time(), 'pv' => 1);
            return $L;
        });
        audit('tk-them', "Thêm tài khoản nhân viên $ten ($u)");
        return array('bao' => "Đã thêm tài khoản $u.");
    case 'tk-sua':
        need_owner();
        $who = (string)(isset($in['u']) ? $in['u'] : ''); $viec = (string)(isset($in['viec']) ? $in['viec'] : '');
        $me = current_user();
        if ($who === $me['u']) throw new QtError('Chị đổi mật khẩu của mình ở ô phía trên.');
        $pw = null;
        if ($viec === 'mk') { $pw = (string)(isset($in['pw']) ? $in['pw'] : ''); check_password($pw); }
        $name = '';
        store_edit('tai-khoan', function ($L) use ($who, $viec, $pw, &$name) {
            foreach ($L as $i => &$x) if ($x['u'] === $who) {
                if ($x['vai'] === 'chu') throw new QtError('Không sửa được tài khoản chủ ở đây.', 403);
                $name = $x['ten'];
                if ($viec === 'mk') { $x['hash'] = password_hash($pw, PASSWORD_DEFAULT); $x['pv']++; }
                elseif ($viec === 'khoa') { $x['bat'] = false; $x['pv']++; }
                elseif ($viec === 'mo') $x['bat'] = true;
                elseif ($viec === 'xoa') { unset($L[$i]); return array_values($L); }
                else throw new QtError('Việc không hợp lệ.');
                return $L;
            }
            throw new QtError('Không thấy tài khoản này.', 404);
        });
        $lab = array('mk' => 'Đặt lại mật khẩu', 'khoa' => 'Khoá tài khoản', 'mo' => 'Mở khoá tài khoản', 'xoa' => 'Xóa tài khoản');
        audit('tk-sua', $lab[$viec] . " $name ($who)");
        return array('bao' => $lab[$viec] . " $who: xong.");

    // ---- tiến độ đưa lên web
    case 'tien-do':
        return deploy_status();
    case 'dong-bo':
        return sync_step(20);

    // ---- nội dung
    case 'thong-bao':
        $in['link'] = isset($in['link_chon']) ? ($in['link_chon'] === '*' ? (isset($in['link_url']) ? $in['link_url'] : '') : $in['link_chon']) : '';
        $sha = save_notice($in);
        audit('thong-bao', !empty($in['bat']) ? 'Bật/sửa thông báo: ' . mb_substr(txt($in['chu'], 220), 0, 80) : 'Tắt thông báo', array('c' => $sha));
        return array('c' => $sha);
    case 'lien-he':
        $sha = save_contact($in);
        audit('lien-he', 'Sửa thông tin liên hệ', array('c' => $sha));
        return array('c' => $sha);
    case 'san-pham':
        list($sha, $names) = save_products($in);
        audit('san-pham', 'Sửa sản phẩm: ' . implode(', ', $names), array('c' => $sha));
        return array('c' => $sha);
    case 'bai-luu':
        list($sha, $slug) = save_post($in);
        audit('bai-luu', (!empty($in['slug']) ? 'Sửa bài ' : (!empty($in['nhap']) ? 'Lưu nháp bài ' : 'Đăng bài ')) . txt($in['title'], 120), array('c' => $sha));
        return array('c' => $sha, 'slug' => $slug);
    case 'bai-co':
        list($sha, $title) = post_flag((string)(isset($in['slug']) ? $in['slug'] : ''), (string)(isset($in['viec']) ? $in['viec'] : ''), isset($in['v']) ? $in['v'] : '');
        $lab = array('an' => 'Ẩn bài', 'hien' => 'Hiện lại bài', 'dang' => 'Đăng bài nháp', 'xoa' => 'Xóa bài');
        audit('bai-co', $lab[$in['viec']] . ' ' . $title, array('c' => $sha));
        return array('c' => $sha);
    case 'anh-tai':
        temp_clean();
        if (empty($_FILES['lon']['tmp_name']) || empty($_FILES['nho']['tmp_name'])) throw new QtError('Thiếu ảnh tải lên.' . (empty($_FILES) ? ' Ảnh có thể vượt giới hạn tải lên của hosting.' : ''));
        list($a, $w, $h1) = take_jpeg($_FILES['lon']['tmp_name'], 1600, 200, 3000000);
        list($b, $w2, $h2) = take_jpeg($_FILES['nho']['tmp_name'], 760, 100, 1000000);
        if (abs($w / $h1 - $w2 / $h2) > 0.03) throw new QtError('Hai cỡ ảnh không khớp nhau.');
        return array('lon' => $a, 'nho' => $b, 'w' => $w, 'h' => $h1);
    case 'anh-luu':
        list($sha, $parts) = save_gallery($in);
        audit('anh-luu', 'Ảnh vườn: ' . implode(', ', $parts), array('c' => $sha));
        return array('c' => $sha);
    case 'video-tai':
        return video_chunk($in);
    case 'video-anh':
        temp_clean();
        if (empty($_FILES['anh']['tmp_name'])) throw new QtError('Thiếu ảnh.');
        list($a) = take_jpeg($_FILES['anh']['tmp_name'], 1920, 100, 1500000);
        return array('anh' => $a);
    case 'clip-luu':
        $in['an'] = empty($in['hien']);
        $sha = save_clip($in);
        audit('clip-luu', !empty($in['moi']) ? 'Thay clip trang Vùng trồng' : 'Sửa clip trang Vùng trồng', array('c' => $sha));
        return array('c' => $sha);
    }
    throw new QtError('Không có lệnh này.', 404);
}

// video tải lên từng phần 1,5 MB (dưới giới hạn tải lên 2 MB thường gặp của hosting), ghép trong thư mục tạm rồi kiểm tra là MP4
function video_chunk($in) {
    temp_clean();
    $id = isset($_POST['id']) ? (string)$_POST['id'] : '';
    $i = (int)(isset($_POST['i']) ? $_POST['i'] : -1); $n = (int)(isset($_POST['n']) ? $_POST['n'] : 0);
    if ($id === '') $id = bin2hex(random_bytes(8));
    if (!preg_match('~^[a-f0-9]{16}$~', $id) || $i < 0 || $n < 1 || $n > 30 || $i >= $n) throw new QtError('Phần video không hợp lệ.');
    if (empty($_FILES['phan']['tmp_name']) || !is_uploaded_file($_FILES['phan']['tmp_name']) && !getenv('MEDILI_QT_TEST')) throw new QtError('Thiếu phần video. Có thể hosting giới hạn cỡ tải lên.');
    if (filesize($_FILES['phan']['tmp_name']) > 1600000) throw new QtError('Phần video quá lớn.');
    $part = temp_dir() . "/$id.part";
    if ($i === 0) @unlink($part);
    elseif (!is_file($part) || (int)@file_get_contents("$part.n") !== $i) throw new QtError('Tải video bị gián đoạn, chị tải lại từ đầu.');
    file_put_contents($part, file_get_contents($_FILES['phan']['tmp_name']), FILE_APPEND | LOCK_EX);
    file_put_contents("$part.n", (string)($i + 1));
    if (filesize($part) > 41943040) { @unlink($part); throw new QtError('Video quá 40 MB.'); }
    if ($i < $n - 1) return array('id' => $id);
    $fh = fopen($part, 'rb'); $head = fread($fh, 12); fclose($fh);
    if (substr($head, 4, 4) !== 'ftyp') { @unlink($part); throw new QtError('Tệp này không phải video MP4.'); }
    rename($part, temp_dir() . "/$id.mp4");
    @unlink("$part.n");
    return array('id' => $id, 'xong' => true, 'mb' => round(filesize(temp_dir() . "/$id.mp4") / 1048576, 1));
}

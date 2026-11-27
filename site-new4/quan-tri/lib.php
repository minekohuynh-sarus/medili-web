<?php
// Trang quản trị MeDili (medili.vn/quan-tri), 27/11/2026: phần lõi.
// Mã nguồn nằm trong kho GitHub công khai, nên không có bí mật nào ở đây. Khoá GitHub, tài khoản, nhật ký nằm trong thư mục
// riêng ngoài public_html (domains/medili.vn/medili-admin), mỗi tệp mở đầu bằng dòng chặn (xem GUARD) để không đọc được qua web.
// Luồng: lưu ở đây -> ghi art/data/*.json lên GitHub (nhánh main) -> GitHub Actions dựng web (.github/workflows/dung-web.yml)
// -> trang quản trị tải các trang đã dựng về public_html (giống hosting/sync.php, dùng chung state.json và sync.lock).
defined('MDQ') or exit;

const GH_OWNER = 'minekohuynh-sarus';
const GH_REPO = 'medili-web';
const GH_BRANCH = 'main';
const GH_SRC = 'site-new4/';
const GH_WORKFLOW = 'dung-web.yml';
const SITE_URL = 'https://www.medili.vn/';
const GUARD = "<?php exit; ?>\n";

ini_set('serialize_precision', '-1');
date_default_timezone_set('Asia/Ho_Chi_Minh');
if (function_exists('mb_internal_encoding')) mb_internal_encoding('UTF-8');
else {   // hosting thiếu mbstring
    function mb_strlen($s) { return preg_match_all('~.~us', $s); }
    function mb_substr($s, $a, $n = null) { $c = preg_split('~~u', $s, -1, PREG_SPLIT_NO_EMPTY); return implode('', array_slice($c, $a, $n)); }
    function mb_strtolower($s) { return strtr(strtolower($s), array('À'=>'à','Á'=>'á','Ạ'=>'ạ','Ả'=>'ả','Ã'=>'ã','Â'=>'â','Ă'=>'ă','È'=>'è','É'=>'é','Ê'=>'ê','Ì'=>'ì','Í'=>'í','Ò'=>'ò','Ó'=>'ó','Ô'=>'ô','Ơ'=>'ơ','Ù'=>'ù','Ú'=>'ú','Ư'=>'ư','Ý'=>'ý','Đ'=>'đ')); }
}

class QtError extends Exception {
    public $code_http;
    public function __construct($msg, $code = 400) { parent::__construct($msg); $this->code_http = $code; }
}

// ---------------------------------------------------------------- đường dẫn
function qt_dir($k) {
    static $d = null;
    if ($d === null) {
        $home = dirname(__DIR__, 2);   // .../domains/medili.vn
        $d = array(
            'data' => getenv('MEDILI_QT_DATA') ?: $home . '/medili-admin',
            'site' => getenv('MEDILI_QT_SITE') ?: dirname(__DIR__),          // public_html
            'sync' => getenv('MEDILI_QT_SYNC') ?: $home . '/medili-sync',
        );
    }
    return $d[$k];
}

function gh_api() { return rtrim(getenv('MEDILI_QT_API') ?: 'https://api.github.com', '/'); }

function data_ready() {
    $d = qt_dir('data');
    if (!is_dir($d) && !@mkdir($d, 0700, true)) return false;
    foreach (array('tam', 'phien') as $s) if (!is_dir("$d/$s")) @mkdir("$d/$s", 0700);
    if (!is_file("$d/index.php")) @file_put_contents("$d/index.php", GUARD);
    return is_writable($d);
}

// ---------------------------------------------------------------- kho riêng (tệp JSON có chặn đọc)
function store_get($name, $def = null) {
    $f = qt_dir('data') . "/$name.php";
    if (!is_file($f)) return $def;
    $s = file_get_contents($f);
    if (strpos($s, GUARD) === 0) $s = substr($s, strlen(GUARD));
    $v = json_decode($s, true);
    return $v === null ? $def : $v;
}

function store_put($name, $v) {
    $f = qt_dir('data') . "/$name.php";
    $t = $f . '.' . bin2hex(random_bytes(4)) . '.tmp';
    if (file_put_contents($t, GUARD . json_encode($v, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES), LOCK_EX) === false) throw new QtError('Không ghi được dữ liệu riêng của trang quản trị.', 500);
    @chmod($t, 0600);
    rename($t, $f);
}

// đọc - sửa - ghi có khoá, cho các tệp nhiều người cùng ghi (tài khoản, lượt đăng nhập)
function store_edit($name, $fn, $def = array()) {
    $lk = fopen(qt_dir('data') . "/$name.lock", 'c');
    flock($lk, LOCK_EX);
    try {
        $v = $fn(store_get($name, $def));
        if ($v !== null) store_put($name, $v);
        return $v;
    } finally { flock($lk, LOCK_UN); fclose($lk); }
}

function audit($act, $what, $extra = array()) {
    $f = qt_dir('data') . '/nhat-ky.php';
    if (is_file($f) && filesize($f) > 2000000) { @rename($f, $f . '.1.php'); }
    if (!is_file($f)) file_put_contents($f, GUARD, LOCK_EX);
    $u = current_user();
    $row = array('t' => date('c'), 'u' => $u ? $u['u'] : '', 'ten' => $u ? $u['ten'] : '', 'ip' => client_ip(), 'viec' => $act, 'mo_ta' => $what) + $extra;
    file_put_contents($f, json_encode($row, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES) . "\n", FILE_APPEND | LOCK_EX);
}

function audit_rows($n = 200) {
    $f = qt_dir('data') . '/nhat-ky.php';
    if (!is_file($f)) return array();
    $lines = array_reverse(array_slice(explode("\n", trim(substr(file_get_contents($f), strlen(GUARD)))), -$n));
    $out = array();
    foreach ($lines as $l) { $r = json_decode($l, true); if ($r) $out[] = $r; }
    return $out;
}

// ---------------------------------------------------------------- tiện ích
function h($s) { return htmlspecialchars((string)$s, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8'); }

function client_ip() { return isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : 'cli'; }

function is_https() {
    return (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off') || (isset($_SERVER['SERVER_PORT']) && $_SERVER['SERVER_PORT'] == 443)
        || (isset($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https')
        || (isset($_SERVER['HTTP_CF_VISITOR']) && strpos($_SERVER['HTTP_CF_VISITOR'], 'https') !== false);
}

function is_local() { $h = isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : ''; return (bool)preg_match('~^(localhost|127\.0\.0\.1)(:\d+)?$~', $h); }

// chữ thuần một dòng: bỏ thẻ HTML, gộp khoảng trắng, giới hạn độ dài
function txt($v, $max) {
    if (!is_string($v)) return '';
    $v = preg_replace('~<[^<>]*>|[<>]~u', '', $v);
    $v = trim(preg_replace('~\s+~u', ' ', $v));
    if (!preg_match('//u', $v)) throw new QtError('Chữ có ký tự lỗi mã hoá.');
    return mb_substr($v, 0, $max);
}

// đoạn văn nhiều dòng (bài tin): bỏ thẻ HTML, giữ xuống dòng
function para($v, $max) {
    if (!is_string($v)) return '';
    $v = str_replace(array("\r\n", "\r"), "\n", $v);
    $v = preg_replace('~<[^<>]*>|[<>]~u', '', $v);
    $v = preg_replace('~[ \t\x{00a0}]+~u', ' ', $v);
    if (!preg_match('//u', $v)) throw new QtError('Chữ có ký tự lỗi mã hoá.');
    return mb_substr(trim($v), 0, $max);
}

function https_url($v) {
    $v = trim((string)$v);
    return preg_match('~^https://[A-Za-z0-9.-]+\.[A-Za-z]{2,}(/[^\s"\'<>]*)?$~', $v) ? $v : '';
}

// tên không dấu cho đường dẫn: "Giá cà phê hôm nay" -> "gia-ca-phe-hom-nay"
function slugify($s, $max = 70) {
    $map = array('à'=>'a','á'=>'a','ạ'=>'a','ả'=>'a','ã'=>'a','â'=>'a','ầ'=>'a','ấ'=>'a','ậ'=>'a','ẩ'=>'a','ẫ'=>'a','ă'=>'a','ằ'=>'a','ắ'=>'a','ặ'=>'a','ẳ'=>'a','ẵ'=>'a',
        'è'=>'e','é'=>'e','ẹ'=>'e','ẻ'=>'e','ẽ'=>'e','ê'=>'e','ề'=>'e','ế'=>'e','ệ'=>'e','ể'=>'e','ễ'=>'e','ì'=>'i','í'=>'i','ị'=>'i','ỉ'=>'i','ĩ'=>'i',
        'ò'=>'o','ó'=>'o','ọ'=>'o','ỏ'=>'o','õ'=>'o','ô'=>'o','ồ'=>'o','ố'=>'o','ộ'=>'o','ổ'=>'o','ỗ'=>'o','ơ'=>'o','ờ'=>'o','ớ'=>'o','ợ'=>'o','ở'=>'o','ỡ'=>'o',
        'ù'=>'u','ú'=>'u','ụ'=>'u','ủ'=>'u','ũ'=>'u','ư'=>'u','ừ'=>'u','ứ'=>'u','ự'=>'u','ử'=>'u','ữ'=>'u','ỳ'=>'y','ý'=>'y','ỵ'=>'y','ỷ'=>'y','ỹ'=>'y','đ'=>'d');
    $s = strtr(mb_strtolower($s), $map);
    $s = preg_replace('~[^a-z0-9]+~', '-', $s);
    $s = trim(substr($s, 0, $max), '-');
    return preg_replace('~-+~', '-', $s);
}

// JSON giống json.dump(..., ensure_ascii=False, indent=1) của Python, để GitHub hiện thay đổi gọn
function json_py($v) {
    $s = json_encode($v, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES | JSON_PRESERVE_ZERO_FRACTION);
    if ($s === false) throw new QtError('Không ghi được dữ liệu (JSON lỗi).', 500);
    return preg_replace_callback('~^( {4})+~m', function ($m) { return str_repeat(' ', strlen($m[0]) / 4); }, $s);
}

function item_ver($v) { return substr(sha1(json_encode($v, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES)), 0, 12); }

// ---------------------------------------------------------------- phiên đăng nhập
function session_start_qt() {
    if (session_status() === PHP_SESSION_ACTIVE) return;
    $p = qt_dir('data') . '/phien';
    if (is_dir($p) && is_writable($p)) session_save_path($p);
    ini_set('session.use_strict_mode', '1');
    ini_set('session.use_only_cookies', '1');
    ini_set('session.gc_maxlifetime', '86400');
    ini_set('session.gc_probability', '1');
    ini_set('session.gc_divisor', '100');
    session_name('mdq');
    $path = rtrim(dirname($_SERVER['SCRIPT_NAME']), '/') . '/';
    if (PHP_VERSION_ID >= 70300) session_set_cookie_params(array('lifetime' => 0, 'path' => $path, 'secure' => is_https(), 'httponly' => true, 'samesite' => 'Strict'));
    else session_set_cookie_params(0, $path . '; samesite=Strict', '', is_https(), true);
    session_start();
}

function users() { return store_get('tai-khoan', array()); }

function user_by($u) { foreach (users() as $x) if ($x['u'] === $u) return $x; return null; }

function current_user() {
    static $cur = false;
    if ($cur !== false) return $cur;
    $cur = null;
    if (session_status() !== PHP_SESSION_ACTIVE || empty($_SESSION['u'])) return null;
    $x = user_by($_SESSION['u']);
    $now = time();
    if (!$x || empty($x['bat']) || (int)$x['pv'] !== (int)$_SESSION['pv'] || $now - $_SESSION['ta'] > 4 * 3600 || $now - $_SESSION['t0'] > 24 * 3600) {
        $_SESSION = array();
        return null;
    }
    $_SESSION['ta'] = $now;
    $cur = $x;
    return $cur;
}

function is_owner() { $u = current_user(); return $u && $u['vai'] === 'chu'; }

function need_owner() { if (!is_owner()) throw new QtError('Việc này chỉ tài khoản chủ làm được.', 403); }

function csrf_token() {
    if (empty($_SESSION['csrf'])) $_SESSION['csrf'] = bin2hex(random_bytes(32));
    return $_SESSION['csrf'];
}

function csrf_check() {
    $t = isset($_SERVER['HTTP_X_CSRF']) ? $_SERVER['HTTP_X_CSRF'] : (isset($_POST['csrf']) ? $_POST['csrf'] : '');
    if (empty($_SESSION['csrf']) || !is_string($t) || !hash_equals($_SESSION['csrf'], $t)) throw new QtError('Phiên làm việc đã hết hạn, chị tải lại trang rồi thử lại.', 403);
    $o = isset($_SERVER['HTTP_ORIGIN']) ? $_SERVER['HTTP_ORIGIN'] : '';
    if ($o && parse_url($o, PHP_URL_HOST) !== parse_url('http://' . $_SERVER['HTTP_HOST'], PHP_URL_HOST)) throw new QtError('Yêu cầu không đến từ trang quản trị.', 403);
}

// giới hạn số lần nhập sai: 5 lần cho mỗi tên đăng nhập (khoá 15 phút), 20 lần cho mỗi địa chỉ mạng (khoá 1 giờ)
function throttle_check($keys) {
    $t = store_get('luot-sai', array());
    $now = time();
    foreach ($keys as $k) {
        if (isset($t[$k]['den']) && $t[$k]['den'] > $now) {
            throw new QtError('Nhập sai nhiều lần. Chị thử lại sau ' . max(1, ceil(($t[$k]['den'] - $now) / 60)) . ' phút.', 429);
        }
    }
}

function throttle_fail($keys) {
    store_edit('luot-sai', function ($t) use ($keys) {
        $now = time();
        foreach ($t as $k => $v) if ($v['t'] < $now - 86400) unset($t[$k]);
        foreach ($keys as $k) {
            $lim = strpos($k, 'ip:') === 0 ? array(20, 3600) : array(5, 900);
            $v = isset($t[$k]) && $t[$k]['t'] > $now - $lim[1] ? $t[$k] : array('n' => 0, 't' => $now);
            $v['n']++;
            if ($v['n'] >= $lim[0]) { $v['den'] = $now + $lim[1]; $v['n'] = 0; $v['t'] = $now; }
            $t[$k] = $v;
        }
        return $t;
    });
}

function throttle_clear($k) { store_edit('luot-sai', function ($t) use ($k) { unset($t[$k]); return $t; }); }

function check_password($pw) {
    if (!is_string($pw) || mb_strlen($pw) < 10) throw new QtError('Mật khẩu cần ít nhất 10 ký tự.');
    if (mb_strlen($pw) > 200) throw new QtError('Mật khẩu quá dài.');
    if (preg_match('~^(.)\1+$~u', $pw) || preg_match('~^(0123456789|1234567890|abcdefghij)~i', $pw)) throw new QtError('Mật khẩu quá dễ đoán.');
}

function login($u, $pw) {
    $u = strtolower(trim((string)$u));
    $keys = array('u:' . $u, 'ip:' . client_ip());
    throttle_check($keys);
    $x = user_by($u);
    $ok = $x && !empty($x['bat']) && password_verify((string)$pw, $x['hash']);
    if (!$ok) {
        if (!$x) password_hash('x', PASSWORD_DEFAULT);   // thời gian chờ như khi có tài khoản
        throttle_fail($keys);
        throw new QtError('Sai tên đăng nhập hoặc mật khẩu.', 400);
    }
    throttle_clear('u:' . $u);
    if (password_needs_rehash($x['hash'], PASSWORD_DEFAULT)) {
        store_edit('tai-khoan', function ($L) use ($u, $pw) { foreach ($L as &$y) if ($y['u'] === $u) $y['hash'] = password_hash($pw, PASSWORD_DEFAULT); return $L; });
    }
    session_regenerate_id(true);
    $_SESSION = array('u' => $u, 'pv' => (int)$x['pv'], 't0' => time(), 'ta' => time(), 'csrf' => bin2hex(random_bytes(32)));
}

function logout() {
    $_SESSION = array();
    if (session_status() === PHP_SESSION_ACTIVE) session_destroy();
}

// ---------------------------------------------------------------- GitHub
function gh_token() { $c = store_get('cau-hinh', array()); return isset($c['token']) ? $c['token'] : ''; }

// $opt: raw (đọc nội dung tệp), token, infile (gửi thân từ tệp), timeout
function gh($method, $path, $body = null, $opt = array()) {
    $tok = isset($opt['token']) ? $opt['token'] : gh_token();
    $url = (strpos($path, 'http') === 0 ? $path : gh_api() . $path);
    $ch = curl_init($url);
    $hd = array('User-Agent: medili-quan-tri (medili.vn)', 'X-GitHub-Api-Version: 2022-11-28',
                'Accept: ' . (!empty($opt['raw']) ? 'application/vnd.github.raw' : 'application/vnd.github+json'));
    if ($tok) $hd[] = 'Authorization: Bearer ' . $tok;
    $o = array(CURLOPT_RETURNTRANSFER => true, CURLOPT_CUSTOMREQUEST => $method, CURLOPT_CONNECTTIMEOUT => 15,
               CURLOPT_TIMEOUT => isset($opt['timeout']) ? $opt['timeout'] : 60, CURLOPT_HEADER => true, CURLOPT_FOLLOWLOCATION => !empty($opt['raw']));
    if (!empty($opt['infile'])) {
        $fh = fopen($opt['infile'], 'rb');
        $o[CURLOPT_UPLOAD] = true; $o[CURLOPT_INFILE] = $fh; $o[CURLOPT_INFILESIZE] = filesize($opt['infile']);
        $hd[] = 'Content-Type: application/json';
    } elseif ($body !== null) {
        $o[CURLOPT_POSTFIELDS] = json_encode($body, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
        $hd[] = 'Content-Type: application/json';
    }
    $o[CURLOPT_HTTPHEADER] = $hd;
    curl_setopt_array($ch, $o);
    $res = curl_exec($ch);
    $err = curl_error($ch);
    $code = (int)curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $hs = (int)curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    curl_close($ch);
    if (isset($fh)) fclose($fh);
    if ($res === false) throw new QtError('Không kết nối được GitHub (' . $err . '). Chị thử lại sau ít phút.', 502);
    $head = substr($res, 0, $hs); $raw = substr($res, $hs);
    $hdrs = array();
    foreach (explode("\n", $head) as $l) if (strpos($l, ':')) { list($k, $v) = explode(':', $l, 2); $hdrs[strtolower(trim($k))] = trim($v); }
    return array($code, !empty($opt['raw']) && $code < 300 ? $raw : json_decode($raw, true), $hdrs);
}

function gh_ok($r, $what) {
    list($code, $j) = $r;
    if ($code >= 200 && $code < 300) return $j;
    if ($code === 401) throw new QtError('Khoá GitHub không còn dùng được (hết hạn hoặc đã bị thu hồi). Chị vào Cài đặt để dán khoá mới.', 502);
    if ($code === 403 || $code === 404) {
        $m = is_array($j) && isset($j['message']) ? $j['message'] : '';
        if (stripos($m, 'rate limit') !== false) throw new QtError('GitHub đang giới hạn số lần gọi, chị thử lại sau ít phút.', 503);
        throw new QtError("GitHub từ chối khi $what (mã $code). Khoá GitHub cần quyền Contents: Read and write và Actions: Read cho kho " . GH_REPO . '.', 502);
    }
    throw new QtError("GitHub báo lỗi khi $what (mã $code).", 502);
}

function repo_path($p) { return '/repos/' . GH_OWNER . '/' . GH_REPO . $p; }

function enc_path($p) { return implode('/', array_map('rawurlencode', explode('/', $p))); }

function gh_head() {
    $j = gh_ok(gh('GET', repo_path('/git/ref/heads/' . GH_BRANCH)), 'đọc nhánh main');
    return $j['object']['sha'];
}

// đọc tệp trong kho ở một commit; tệp chưa có thì trả null
function gh_read($path, $ref) {
    $r = gh('GET', repo_path('/contents/' . enc_path($path) . '?ref=' . $ref), null, array('raw' => true));
    if ($r[0] === 404) return null;
    return gh_ok($r, "đọc $path");
}

function gh_json($path, $ref = null) {
    $ref = $ref ?: gh_head();
    $s = gh_read($path, $ref);
    if ($s === null) return null;
    $v = json_decode($s, true);
    if ($v === null) throw new QtError("Tệp $path trên GitHub bị lỗi định dạng.", 500);
    return $v;
}

// dữ liệu cho các trang quản trị: đọc ở commit mới nhất của main, giữ bản sao theo mã commit để mở trang nhanh
function head_now() { static $h = null; if ($h === null) $h = gh_head(); return $h; }

function data_json($path) {
    $head = head_now();
    $dir = qt_dir('data') . '/bo-nho';
    $f = "$dir/" . substr($head, 0, 12) . '-' . substr(md5($path), 0, 10) . '.json';
    if (is_file($f)) { $v = json_decode(file_get_contents($f), true); if (is_array($v)) return $v; }
    $s = gh_read($path, $head);
    if ($s === null) return null;
    $v = json_decode($s, true);
    if (!is_array($v)) throw new QtError("Tệp $path trên GitHub bị lỗi định dạng.", 500);
    if (!is_dir($dir)) @mkdir($dir, 0700);
    @file_put_contents($f, $s);
    $old = glob("$dir/*.json") ?: array();
    if (count($old) > 80) { usort($old, function ($a, $b) { return filemtime($a) - filemtime($b); }); foreach (array_slice($old, 0, count($old) - 60) as $x) @unlink($x); }
    return $v;
}

// tạo blob từ tệp lớn (ảnh, video) mà không nạp hết vào bộ nhớ
function gh_blob_file($file) {
    @set_time_limit(600);
    $tmp = qt_dir('data') . '/tam/blob-' . bin2hex(random_bytes(6)) . '.json';
    $out = fopen($tmp, 'wb');
    fwrite($out, '{"encoding":"base64","content":"');
    $in = fopen($file, 'rb');
    while (!feof($in)) { $b = fread($in, 3 * 262144); if ($b === '' || $b === false) break; fwrite($out, base64_encode($b)); }
    fclose($in);
    fwrite($out, '"}');
    fclose($out);
    try {
        $j = gh_ok(gh('POST', repo_path('/git/blobs'), null, array('infile' => $tmp, 'timeout' => 300)), 'tải tệp lên');
    } finally { @unlink($tmp); }
    return $j['sha'];
}

// Ghi một lần lên main. $paths: các tệp JSON cần đọc; $fn($cur) trả về [đường dẫn => nội dung mới] (bỏ qua tệp không đổi).
// $files: [đường dẫn trong kho => tệp trong máy] cho ảnh, video. Nếu main vừa đổi (người khác cùng lưu), đọc lại và làm lại.
function gh_commit($msg, $paths, $fn, $files = array()) {
    $blobs = array();
    foreach ($files as $p => $f) $blobs[$p] = gh_blob_file($f);
    for ($try = 1; $try <= 5; $try++) {
        $head = gh_head();
        $c = gh_ok(gh('GET', repo_path('/git/commits/' . $head)), 'đọc commit');
        $cur = array();
        foreach ($paths as $p) $cur[$p] = gh_read($p, $head);
        $new = $fn($cur);
        $tree = array();
        foreach ($new as $p => $s) {
            if ($s === null || (isset($cur[$p]) && $cur[$p] === $s)) continue;
            $b = gh_ok(gh('POST', repo_path('/git/blobs'), array('content' => $s, 'encoding' => 'utf-8')), 'ghi dữ liệu');
            $tree[] = array('path' => $p, 'mode' => '100644', 'type' => 'blob', 'sha' => $b['sha']);
        }
        foreach ($blobs as $p => $sha) $tree[] = array('path' => $p, 'mode' => '100644', 'type' => 'blob', 'sha' => $sha);
        if (!$tree) return null;   // không có gì thay đổi
        $t = gh_ok(gh('POST', repo_path('/git/trees'), array('base_tree' => $c['tree']['sha'], 'tree' => $tree)), 'ghi dữ liệu');
        $u = current_user();
        $k = gh_ok(gh('POST', repo_path('/git/commits'), array('message' => "Quản trị: $msg", 'tree' => $t['sha'], 'parents' => array($head))), 'ghi dữ liệu');
        $r = gh('PATCH', repo_path('/git/refs/heads/' . GH_BRANCH), array('sha' => $k['sha'], 'force' => false));
        if ($r[0] === 200) {
            store_put('lan-dua', array('c' => $k['sha'], 't' => time(), 'u' => $u ? $u['u'] : '', 'viec' => $msg, 'xong' => false));
            return $k['sha'];
        }
        if ($r[0] !== 422 && $r[0] !== 409) gh_ok($r, 'ghi dữ liệu');
        usleep(400000 * $try);
    }
    throw new QtError('GitHub đang bận vì có nhiều thay đổi cùng lúc, chị bấm Lưu lại một lần nữa.', 503);
}

// ---------------------------------------------------------------- dựng web và đưa lên medili.vn
function build_runs() {
    $j = gh_ok(gh('GET', repo_path('/actions/workflows/' . GH_WORKFLOW . '/runs?branch=' . GH_BRANCH . '&per_page=6')), 'xem tiến độ dựng web');
    $out = array();
    foreach ($j['workflow_runs'] as $r) {
        $out[] = array('sha' => $r['head_sha'], 'st' => $r['status'], 'kq' => $r['conclusion'], 't' => strtotime($r['created_at']), 'url' => $r['html_url']);
    }
    return $out;
}

// tiến độ của lần lưu gần nhất: cho (GitHub chưa nhận) | dung (đang dựng) | loi | dua (dựng xong, đang đưa lên hosting) | xong
function deploy_status() {
    $d = store_get('lan-dua', null);
    if (!$d) return array('buoc' => 'xong');
    $base = array('viec' => $d['viec'], 't' => $d['t'], 'c' => substr($d['c'], 0, 7));
    if (!empty($d['xong'])) return $base + array('buoc' => 'xong');
    $runs = build_runs();
    $mine = null;
    foreach ($runs as $r) if ($r['sha'] === $d['c'] || (!empty($d['run']) && $r['sha'] === $d['run'])) { $mine = $r; break; }
    if (!$mine || $mine['kq'] === 'cancelled') {
        // lần dựng của thay đổi này bị gộp vào một lần dựng mới hơn (nhiều lần lưu liền nhau): tìm lần dựng có chứa commit này
        foreach ($runs as $r) {
            if ($r['sha'] === $d['c'] || $r['kq'] === 'cancelled') continue;
            if ($r['t'] < $d['t'] - 120) break;
            $cmp = gh('GET', repo_path('/compare/' . $d['c'] . '...' . $r['sha']));
            if ($cmp[0] === 200 && in_array($cmp[1]['status'], array('ahead', 'identical'), true)) {
                $mine = $r; $d['run'] = $r['sha']; store_put('lan-dua', $d); break;
            }
        }
    }
    if (!$mine) return $base + array('buoc' => time() - $d['t'] > 300 ? 'loi' : 'cho', 'loi' => 'GitHub chưa nhận việc dựng web. Chị mở mục Actions của kho để xem.');
    if ($mine['st'] !== 'completed') return $base + array('buoc' => 'dung', 'url' => $mine['url']);
    if ($mine['kq'] !== 'success') return $base + array('buoc' => 'loi', 'url' => $mine['url'], 'loi' => 'Dựng web bị lỗi nên web vẫn giữ bản trước. Chị chụp màn hình gửi em (Claude) để em xem lại dữ liệu vừa lưu.');
    return $base + array('buoc' => 'dua', 'url' => $mine['url']);
}

// Tải các tệp trong site-new4/ đã đổi về public_html, tối đa $budget giây mỗi lần gọi. Dùng chung khoá và state.json với sync.php.
function sync_step($budget = 20) {
    $sd = qt_dir('sync'); $root = qt_dir('site');
    if (!is_dir($sd) && !@mkdir($sd, 0755, true)) throw new QtError('Không thấy thư mục đồng bộ medili-sync trên hosting.', 500);
    $lock = fopen("$sd/sync.lock", 'c');
    if (!$lock || !flock($lock, LOCK_EX | LOCK_NB)) return array('ban' => true, 'con' => -1);
    try {
        @set_time_limit($budget + 40);
        $t0 = microtime(true);
        $tree = gh_ok(gh('GET', repo_path('/git/trees/' . GH_BRANCH . '?recursive=1')), 'đọc danh sách tệp');
        $sf = "$sd/state.json";
        $state = is_file($sf) ? json_decode(file_get_contents($sf), true) : array();
        if (!is_array($state)) $state = array();
        $todo = array();
        foreach ($tree['tree'] as $it) {
            if ($it['type'] !== 'blob' || strpos($it['path'], GH_SRC) !== 0) continue;
            $p = substr($it['path'], strlen(GH_SRC));
            if ($p === '' || !preg_match('~^[A-Za-z0-9._/-]+$~', $p) || strpos($p, '..') !== false) continue;
            if (isset($state[$p]) && $state[$p] === $it['sha'] && is_file("$root/$p")) continue;
            $todo[] = array($p, $it['sha']);
        }
        $done = 0; $bad = 0;
        foreach ($todo as $i => $x) {
            if (microtime(true) - $t0 > $budget) break;
            list($p, $sha) = $x;
            $r = gh('GET', repo_path('/git/blobs/' . $sha), null, array('raw' => true, 'timeout' => 120));
            $data = $r[0] === 200 ? $r[1] : null;
            if ($data === null || sha1('blob ' . strlen($data) . "\0" . $data) !== $sha) { $bad++; continue; }
            $dst = "$root/$p";
            if (!is_dir(dirname($dst))) mkdir(dirname($dst), 0755, true);
            file_put_contents("$dst.tmp", $data);
            rename("$dst.tmp", $dst);
            @chmod($dst, 0644);
            $state[$p] = $sha;
            $done++;
            if ($done % 25 === 0) file_put_contents($sf, json_encode($state));
        }
        file_put_contents($sf, json_encode($state));
        $left = count($todo) - $done;
        if ($done || $bad) {
            $f = "$sd/sync.log";
            file_put_contents($f, date('Y-m-d H:i:s') . " Trang quản trị: cập nhật $done file" . ($bad ? ", $bad file chờ lần sau" : '') . "\n", FILE_APPEND);
        }
        if ($left <= $bad) {   // xong lượt này
            $d = store_get('lan-dua', null);
            if ($d && empty($d['xong'])) { $st = deploy_status(); if ($st['buoc'] === 'dua') { $d['xong'] = true; store_put('lan-dua', $d); } }
        }
        return array('con' => max(0, $left - $bad), 'loi' => $bad, 'xong' => $done);
    } finally { flock($lock, LOCK_UN); fclose($lock); }
}

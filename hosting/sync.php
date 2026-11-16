<?php
// MeDili: đồng bộ web từ GitHub về medili.vn.
// Chạy trên hosting bằng Cron (mỗi 30 phút). Đọc danh sách file của kho, so với lần chạy trước,
// tải file mới hoặc đã đổi trong thư mục site-new4/ và ghi vào public_html.
// Chỉ thêm và cập nhật; không xoá file nào khác trong public_html.
// Mỗi file tải về đều được kiểm tra mã băm (sha) của git trước khi ghi, file lỗi sẽ được thử lại ở lần sau.

$OWNER  = 'minekohuynh-sarus';
$REPO   = 'medili-web';
$BRANCH = 'main';
$SRC    = 'site-new4/';

$DIR  = __DIR__;                          // .../domains/medili.vn/medili-sync
$ROOT = dirname($DIR) . '/public_html';   // .../domains/medili.vn/public_html

$lock = fopen("$DIR/sync.lock", 'c');
if (!$lock || !flock($lock, LOCK_EX | LOCK_NB)) exit;   // đang có lần chạy khác
set_time_limit(900);

function logm($m) {
    $f = __DIR__ . '/sync.log';
    if (is_file($f) && filesize($f) > 200000) rename($f, $f . '.1');   // giữ log gọn
    file_put_contents($f, date('Y-m-d H:i:s') . " $m\n", FILE_APPEND);
}

function get($url, $api = false) {
    $ch = curl_init($url);
    $h = array('User-Agent: medili-sync (medili.vn)');
    if ($api) $h[] = 'Accept: application/vnd.github+json';
    curl_setopt_array($ch, array(
        CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_CONNECTTIMEOUT => 15, CURLOPT_TIMEOUT => 120, CURLOPT_HTTPHEADER => $h,
    ));
    $body = curl_exec($ch);
    $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    return array($code, (string)$body);
}

// 1. Danh sách file của nhánh main (một lần gọi API)
list($c, $b) = get("https://api.github.com/repos/$OWNER/$REPO/git/trees/$BRANCH?recursive=1", true);
$tree = json_decode($b, true);
if ($c != 200 || !is_array($tree) || empty($tree['tree'])) { logm("Không đọc được kho GitHub (mã $c)"); exit; }

$stateFile = "$DIR/state.json";
$state = is_file($stateFile) ? json_decode(file_get_contents($stateFile), true) : array();
if (!is_array($state)) $state = array();

// 2. Lưu trang mặc định của hosting một lần, để trả lại được nếu cần
if (!is_dir("$DIR/backup")) {
    @mkdir("$DIR/backup", 0755);
    foreach (array('index.html', 'logo.png') as $f) if (is_file("$ROOT/$f")) @copy("$ROOT/$f", "$DIR/backup/$f");
}

// 3. Tải file mới hoặc đã đổi
$ok = 0; $bad = 0;
foreach ($tree['tree'] as $it) {
    if ($it['type'] !== 'blob' || strpos($it['path'], $SRC) !== 0) continue;
    $p = substr($it['path'], strlen($SRC));
    if ($p === '' || !preg_match('~^[A-Za-z0-9._/-]+$~', $p) || strpos($p, '..') !== false) continue;
    if (isset($state[$p]) && $state[$p] === $it['sha'] && is_file("$ROOT/$p")) continue;

    list($c, $data) = get("https://raw.githubusercontent.com/$OWNER/$REPO/$BRANCH/" . $it['path']);
    // mã sha của git = sha1("blob <độ dài>\0<nội dung>")
    if ($c != 200 || sha1('blob ' . strlen($data) . "\0" . $data) !== $it['sha']) { $bad++; logm("Chưa tải được $p (mã $c), thử lại lần sau"); continue; }

    $dst = "$ROOT/$p";
    if (!is_dir(dirname($dst))) mkdir(dirname($dst), 0755, true);
    file_put_contents("$dst.tmp", $data);
    rename("$dst.tmp", $dst);
    @chmod($dst, 0644);
    $state[$p] = $it['sha'];
    $ok++;
}

file_put_contents($stateFile, json_encode($state));
if ($ok || $bad) logm("Cập nhật $ok file" . ($bad ? ", $bad file chờ lần sau" : ''));

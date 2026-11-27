<?php
// Trang quản trị MeDili: đọc, kiểm tra và ghi các tệp dữ liệu art/data/*.json trên GitHub.
// Mỗi mục sửa kèm "v" (dấu phiên bản lúc mở trang). Ai đó vừa sửa cùng mục thì không ghi đè, báo tải lại trang.
defined('MDQ') or exit;

const F_CAIDAT = 'art/data/cai-dat.json';
const F_SP = 'art/data/san-pham.json';
const F_TIN = 'art/data/tin-tuc.json';
const F_GO = 'art/data/tin-tuc-go.json';
const F_ANH = 'art/data/anh-vuon.json';
const F_CLIP = 'art/data/clip-vuon.json';

// trang được phép gắn vào thông báo (link nội bộ)
const TRANG = array('cua-hang.html' => 'Cửa hàng', 'gio-hang.html' => 'Giỏ hàng', 'tin-tuc.html' => 'Tin tức', 'giao-hang.html' => 'Giao hàng & đổi trả',
    'chinh-sach.html' => 'Chính sách MeDili', 'lien-he.html' => 'Liên hệ', 'quan-medili.html' => 'Quán MeDili Café', 'horeca.html' => 'Giải pháp HORECA',
    'dong-hanh-cung-quan.html' => 'Đồng hành cùng quán', 'mua-hang.html' => 'Phòng chọn mua', 'gia-ca-phe.html' => 'Giá cà phê hôm nay',
    'anh-vuon.html' => 'Ảnh vườn', 'vung-trong.html' => 'Vùng trồng Di Linh', 'tim-gu.html' => 'Tìm gu cà phê', 'thanh-toan.html' => 'Thanh toán');

function conflict($what) { throw new QtError("$what vừa được người khác sửa. Chị tải lại trang để xem bản mới rồi sửa tiếp.", 409); }

function dec($s, $what) {
    $v = json_decode((string)$s, true);
    if (!is_array($v)) throw new QtError("Tệp $what trên GitHub bị lỗi định dạng, em (Claude) cần sửa trước.", 500);
    return $v;
}

function day_ok($d) { return is_string($d) && preg_match('~^20\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$~', $d) && checkdate((int)substr($d, 5, 2), (int)substr($d, 8, 2), (int)substr($d, 0, 4)); }

function vn_date($d) { return day_ok($d) ? ((int)substr($d, 8, 2)) . '/' . ((int)substr($d, 5, 2)) . '/' . substr($d, 0, 4) : ''; }

// ---------------------------------------------------------------- thông báo và liên hệ
function save_notice($in) {
    $bat = !empty($in['bat']);
    $chu = txt(isset($in['chu']) ? $in['chu'] : '', 220);
    if ($bat && mb_strlen($chu) < 5) throw new QtError('Chị nhập nội dung thông báo (ít nhất 5 ký tự).');
    $link = trim((string)(isset($in['link']) ? $in['link'] : ''));
    if ($link !== "" && !array_key_exists($link, TRANG) && !https_url($link)) throw new QtError('Link cần là một trang trong danh sách hoặc địa chỉ bắt đầu bằng https://');
    $tu = (string)(isset($in['tu']) ? $in['tu'] : ''); $den = (string)(isset($in['den']) ? $in['den'] : '');
    if (($tu !== '' && !day_ok($tu)) || ($den !== '' && !day_ok($den))) throw new QtError('Ngày không đúng.');
    if ($tu !== '' && $den !== '' && $den < $tu) throw new QtError('Ngày kết thúc phải sau ngày bắt đầu.');
    $new = array('bat' => $bat, 'chu' => $chu, 'link' => $link, 'chu_link' => txt(isset($in['chu_link']) ? $in['chu_link'] : '', 40),
                 'tu' => $tu, 'den' => $den, 'kieu' => (isset($in['kieu']) && $in['kieu'] === 'quan-trong') ? 'quan-trong' : 'thuong');
    $v = isset($in['v']) ? $in['v'] : '';
    return gh_commit($bat ? 'Bật thông báo "' . mb_substr($chu, 0, 50) . '"' : 'Tắt thông báo', array(F_CAIDAT), function ($cur) use ($new, $v) {
        $d = dec($cur[F_CAIDAT], 'cai-dat.json');
        if (item_ver($d['thong_bao']) !== $v) conflict('Thông báo');
        $d['thong_bao'] = $new;
        return array(F_CAIDAT => json_py($d));
    });
}

function save_contact($in) {
    need_owner();
    $ph = preg_replace('~\D~', '', (string)(isset($in['dien_thoai']) ? $in['dien_thoai'] : ''));
    if (strlen($ph) === 11 && substr($ph, 0, 2) === '84') $ph = '0' . substr($ph, 2);
    if (!preg_match('~^0[1-9]\d{8}$~', $ph)) throw new QtError('Số điện thoại cần 10 số, bắt đầu bằng 0.');
    $zalo = https_url(isset($in['zalo']) ? $in['zalo'] : '');
    if (!preg_match('~^https://(www\.)?zalo\.me/[A-Za-z0-9_./-]+$~', $zalo)) throw new QtError('Link Zalo cần có dạng https://zalo.me/…');
    $fb = https_url(isset($in['facebook']) ? $in['facebook'] : '');
    if (!preg_match('~^https://(www\.|m\.|web\.)?(facebook\.com|fb\.com|fb\.me)/~', $fb)) throw new QtError('Link Facebook cần có dạng https://www.facebook.com/…');
    $em = trim((string)(isset($in['email']) ? $in['email'] : ''));
    if (!preg_match('~^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$~', $em) || strlen($em) > 120) throw new QtError('Email chưa đúng.');
    $g = array();
    foreach (array('gio0', 'gio1') as $k) {
        $x = trim((string)(isset($in[$k]) ? $in[$k] : ''));
        if (!preg_match('~^([01]?\d|2[0-3]):[0-5]\d$~', $x)) throw new QtError('Giờ cần có dạng 6:30 hoặc 22:30.');
        $g[] = ltrim(substr($x, 0, -3), '0') === '' ? '0' . substr($x, -3) : ltrim(substr($x, 0, -3), '0') . substr($x, -3);
    }
    $m = function ($x) { list($a, $b) = explode(':', $x); return $a * 60 + $b; };
    if ($m($g[1]) <= $m($g[0])) throw new QtError('Giờ kết thúc phải sau giờ bắt đầu.');
    $new = array('dien_thoai' => substr($ph, 0, 4) . ' ' . substr($ph, 4, 3) . ' ' . substr($ph, 7), 'zalo' => $zalo, 'facebook' => $fb, 'email' => $em, 'gio_zalo' => $g);
    $v = isset($in['v']) ? $in['v'] : '';
    return gh_commit('Sửa thông tin liên hệ', array(F_CAIDAT), function ($cur) use ($new, $v) {
        $d = dec($cur[F_CAIDAT], 'cai-dat.json');
        if (item_ver($d['lien_he']) !== $v) conflict('Thông tin liên hệ');
        $d['lien_he'] = $new;
        return array(F_CAIDAT => json_py($d));
    });
}

// ---------------------------------------------------------------- sản phẩm và giá
// Giá nhận vào bằng đồng (vd. 280000). Dữ liệu lưu nghìn đồng mỗi kg; Ngũ Hành nhận giá túi 250 g.
function price_in($v, $what) {
    if ($v === null || $v === '') return null;
    $n = (int)preg_replace('~\D~', '', (string)$v);
    if ($n < 10000 || $n > 5000000) throw new QtError("$what: giá cần từ 10.000 đến 5.000.000 đ.");
    return $n;
}

function product_input($id, $old, $in) {
    $loai = $old['loai'];
    $o = $old;
    $name = $old['ten'];
    if ($loai === 'ngu') {
        $bag = price_in(isset($in['p'][0]) ? $in['p'][0] : null, $name);
        if (!$bag) throw new QtError("$name: chị nhập giá túi 250 g.");
        if ($bag % 250) throw new QtError("$name: giá túi cần chia hết cho 250 đ.");
        $o['p'] = array(intdiv($bag, 250));
    } else {
        $p = array();
        foreach (array(0, 1, 2) as $i) {
            $x = price_in(isset($in['p'][$i]) ? $in['p'][$i] : null, $name);
            if ($x !== null && $x % 1000) throw new QtError("$name: giá theo kg cần tròn nghìn đồng (vd. 285.000).");
            $p[] = $x === null ? null : intdiv($x, 1000);
        }
        if ($loai === 'core') {
            if (in_array(null, $p, true)) throw new QtError("$name: dòng này cần đủ giá lẻ và hai mức giá sỉ (trang HORECA, Đồng hành cùng quán, Tìm gu dùng các giá này).");
        } elseif ($loai === 'le') {
            if ($p[0] === null && ($p[1] !== null || $p[2] !== null)) throw new QtError("$name: có giá sỉ thì cần có giá lẻ.");
            if (($p[1] === null) !== ($p[2] === null)) throw new QtError("$name: nhập cả hai mức giá sỉ, hoặc để trống cả hai.");
        } else {   // sap: chỉ một giá lẻ
            $p = array($p[0], null, null);
        }
        if ($p[1] !== null && $p[1] > $p[0]) throw new QtError("$name: giá sỉ 5–20 kg không cao hơn giá lẻ.");
        if ($p[2] !== null && $p[1] !== null && $p[2] > $p[1]) throw new QtError("$name: giá sỉ trên 20 kg không cao hơn giá sỉ 5–20 kg.");
        if ($loai === 'sap') $o['p'] = $p[0] === null ? null : array($p[0]);
        else $o['p'] = $p[0] === null ? null : $p;
    }
    $st = isset($in['st']) ? $in['st'] : $old['st'];
    $ok = $loai === 'sap' ? array('sap', 'ban', 'het') : array('ban', 'het');
    if (!in_array($st, $ok, true)) $st = $old['st'];
    if ($o['p'] === null) $st = $loai === 'sap' ? 'sap' : 'lh';
    elseif ($st === 'lh') $st = 'ban';
    $o['st'] = $st;
    foreach (array('taste' => 'Hương vị', 'use' => 'Cách dùng', 'fit' => 'Phù hợp với', 'head' => 'Câu giới thiệu') as $f => $lab) {
        if ($loai === 'sap' && $f === 'use') continue;
        if (!isset($in[$f])) continue;
        $t = txt($in[$f], 200);
        if ($t === '' && $old[$f] !== '') throw new QtError("$name: chị nhập $lab.");
        $o[$f] = $t;
    }
    return $o;
}

function save_products($in) {
    $sp = isset($in['sp']) && is_array($in['sp']) ? $in['sp'] : array();
    if (!$sp || count($sp) > 30) throw new QtError('Chưa có dòng nào thay đổi.');
    $names = array();
    $sha = gh_commit('Sửa giá và sản phẩm', array(F_SP), function ($cur) use ($sp, &$names) {
        $d = dec($cur[F_SP], 'san-pham.json');
        $names = array();
        foreach ($sp as $id => $x) {
            if (!isset($d[$id])) throw new QtError('Không có sản phẩm ' . h($id) . '.');
            if (item_ver($d[$id]) !== (isset($x['v']) ? $x['v'] : '')) conflict($d[$id]['ten']);
            $d[$id] = product_input($id, $d[$id], $x);
            $names[] = $d[$id]['ten'];
        }
        return array(F_SP => json_py($d));
    });
    return array($sha, $names);
}

// ---------------------------------------------------------------- tin tức
function news_body($text) {
    $out = array();
    foreach (preg_split('~\n\s*\n~u', para($text, 30000)) as $b) {
        $b = trim($b);
        if ($b === '') continue;
        if (preg_match('~^#{1,3}\s*(.+)$~us', $b, $m)) $out[] = array('h' => txt($m[1], 160));
        else $out[] = array('p' => txt($b, 4000));
    }
    return $out;
}

function news_text($body) {
    $s = array();
    foreach ($body as $b) $s[] = isset($b['h']) ? '## ' . $b['h'] : (isset($b['p']) ? $b['p'] : '');
    return implode("\n\n", $s);
}

function save_post($in) {
    $title = txt(isset($in['title']) ? $in['title'] : '', 120);
    if (mb_strlen($title) < 8) throw new QtError('Chị nhập tiêu đề bài (ít nhất 8 ký tự).');
    $date = isset($in['date']) ? (string)$in['date'] : '';
    if (!day_ok($date)) throw new QtError('Ngày đăng chưa đúng.');
    $body = news_body(isset($in['body']) ? $in['body'] : '');
    $np = 0; foreach ($body as $b) if (isset($b['p'])) $np++;
    if ($np < 1) throw new QtError('Bài cần ít nhất một đoạn văn.');
    $kw = array();
    foreach (preg_split('~[,;\n]~u', (string)(isset($in['keywords']) ? $in['keywords'] : '')) as $k) { $k = txt($k, 40); if ($k !== '' && count($kw) < 8) $kw[] = $k; }
    $src = array();
    foreach ((array)(isset($in['sources']) ? $in['sources'] : array()) as $s) {
        $n = txt(isset($s['name']) ? $s['name'] : '', 200); $u = https_url(isset($s['url']) ? $s['url'] : '');
        if (isset($s['url']) && trim($s['url']) !== '' && !$u) throw new QtError('Link nguồn cần bắt đầu bằng https://');
        if ($n !== '' && count($src) < 10) $src[] = $u ? array('name' => $n, 'url' => $u) : array('name' => $n);
    }
    $post = array('date' => $date, 'title' => $title, 'desc' => txt(isset($in['desc']) ? $in['desc'] : '', 200), 'keywords' => $kw,
                  'body' => $body, 'cta' => txt(isset($in['cta']) ? $in['cta'] : '', 300), 'sources' => $src);
    $slug = isset($in['slug']) ? (string)$in['slug'] : '';
    $nhap = !empty($in['nhap']);
    $v = isset($in['v']) ? $in['v'] : '';
    $final = '';
    $msg = ($slug ? 'Sửa bài: ' : ($nhap ? 'Bài nháp: ' : 'Đăng bài: ')) . mb_substr($title, 0, 60);
    $sha = gh_commit($msg, array(F_TIN), function ($cur) use ($post, $slug, $nhap, $v, $date, $title, &$final) {
        $L = $cur[F_TIN] === null ? array() : dec($cur[F_TIN], 'tin-tuc.json');
        if ($slug !== '') {
            foreach ($L as $i => $p) if (isset($p['slug']) && $p['slug'] === $slug) {
                if (item_ver($p) !== $v) conflict('Bài này');
                $q = array('slug' => $slug) + $post;
                foreach (array('an') as $k) if (!empty($p[$k])) $q[$k] = true;
                if ($nhap) $q['nhap'] = true;   // bài nháp vẫn là nháp đến khi bấm Đăng
                foreach ($p as $k => $x) if (!isset($q[$k]) && !in_array($k, array('nhap', 'an'), true)) $q[$k] = $x;   // giữ trường khác (vd. image)
                $L[$i] = $q;
                $final = $slug;
                return array(F_TIN => json_py($L));
            }
            throw new QtError('Không thấy bài này nữa, có thể vừa bị xóa.', 409);
        }
        $base = slugify($title, 66) ?: 'tin-medili';
        $base .= '-' . substr($date, 8, 2) . substr($date, 5, 2);
        $taken = array();
        foreach ($L as $p) if (isset($p['slug'])) $taken[$p['slug']] = 1;
        $s = $base; $k = 2;
        while (isset($taken[$s])) $s = $base . '-' . $k++;
        $q = array('slug' => $s) + $post;
        if ($nhap) $q['nhap'] = true;
        $L[] = $q;
        $final = $s;
        return array(F_TIN => json_py($L));
    });
    return array($sha, $final);
}

function post_flag($slug, $act, $v) {
    $names = array('an' => 'Ẩn bài', 'hien' => 'Hiện lại bài', 'dang' => 'Đăng bài nháp', 'xoa' => 'Xóa bài');
    if (!isset($names[$act])) throw new QtError('Việc không hợp lệ.');
    if ($act === 'xoa') need_owner();
    $title = '';
    $paths = $act === 'xoa' ? array(F_TIN, F_GO) : array(F_TIN);
    $sha = gh_commit($names[$act] . ': ' . $slug, $paths, function ($cur) use ($slug, $act, $v, &$title) {
        $L = dec($cur[F_TIN], 'tin-tuc.json');
        foreach ($L as $i => $p) if (isset($p['slug']) && $p['slug'] === $slug) {
            if (item_ver($p) !== $v) conflict('Bài này');
            $title = $p['title'];
            $out = array();
            if ($act === 'an') $L[$i]['an'] = true;
            if ($act === 'hien') unset($L[$i]['an']);
            if ($act === 'dang') { unset($L[$i]['nhap']); unset($L[$i]['an']); }
            if ($act === 'xoa') {
                $was_live = empty($p['nhap']);
                array_splice($L, $i, 1);
                if ($was_live) {
                    $G = $cur[F_GO] === null ? array() : dec($cur[F_GO], 'tin-tuc-go.json');
                    if (!in_array($slug, $G, true)) $G[] = $slug;
                    $out[F_GO] = json_encode(array_values($G), JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES);
                }
            }
            $out[F_TIN] = json_py(array_values($L));
            return $out;
        }
        throw new QtError('Không thấy bài này nữa, có thể vừa bị xóa.', 409);
    });
    return array($sha, $title);
}

// ---------------------------------------------------------------- ảnh tải lên (đã thu nhỏ, đóng logo trong trình duyệt)
function temp_dir() { return qt_dir('data') . '/tam'; }

function temp_clean() {
    foreach (glob(temp_dir() . '/*') ?: array() as $f) if (is_file($f) && filemtime($f) < time() - 86400) @unlink($f);
}

// kiểm tra một ảnh JPEG tải lên; vẽ lại bằng GD (nếu có) để chắc chỉ còn điểm ảnh
function take_jpeg($tmp, $maxSide, $minSide, $maxBytes) {
    if (!is_uploaded_file($tmp) && !getenv('MEDILI_QT_TEST')) throw new QtError('Tệp tải lên không hợp lệ.');
    if (filesize($tmp) > $maxBytes) throw new QtError('Ảnh quá nặng.');
    $info = @getimagesize($tmp);
    if (!$info || $info[2] !== IMAGETYPE_JPEG) throw new QtError('Ảnh cần ở dạng JPEG.');
    list($w, $hh) = $info;
    if (max($w, $hh) > $maxSide || min($w, $hh) < $minSide) throw new QtError('Kích thước ảnh không đúng.');
    $id = bin2hex(random_bytes(8));
    $dst = temp_dir() . "/$id.jpg";
    if (function_exists('imagecreatefromjpeg')) {
        $im = @imagecreatefromjpeg($tmp);
        if (!$im) throw new QtError('Ảnh bị lỗi, chị chọn ảnh khác.');
        imageinterlace($im, true);
        imagejpeg($im, $dst, 84);
        imagedestroy($im);
    } else {
        move_uploaded_file($tmp, $dst) || copy($tmp, $dst);
    }
    @chmod($dst, 0600);
    return array($id, $w, $hh);
}

function temp_path($id, $ext = 'jpg') {
    if (!preg_match('~^[a-f0-9]{16}$~', (string)$id)) throw new QtError('Mã tệp tạm không đúng.');
    $f = temp_dir() . "/$id.$ext";
    if (!is_file($f)) throw new QtError('Tệp tạm đã hết hạn, chị tải lại ảnh.');
    return $f;
}

// ---------------------------------------------------------------- ảnh vườn
function save_gallery($in) {
    $them = isset($in['them']) && is_array($in['them']) ? $in['them'] : array();
    $sua = isset($in['sua']) && is_array($in['sua']) ? $in['sua'] : array();
    $xoa = isset($in['xoa']) && is_array($in['xoa']) ? $in['xoa'] : array();
    if ($xoa) need_owner();
    $files = array(); $new = array();
    foreach ($them as $x) {
        $ten = 'u-' . date('ymd') . '-' . substr(bin2hex(random_bytes(3)), 0, 5);
        $files[GH_SRC . "assets/g-$ten.jpg"] = temp_path(isset($x['lon']) ? $x['lon'] : '');
        $files[GH_SRC . "assets/g-$ten-s.jpg"] = temp_path(isset($x['nho']) ? $x['nho'] : '');
        $alt = txt(isset($x['alt']) ? $x['alt'] : '', 200);
        if (mb_strlen($alt) < 5) throw new QtError('Mỗi ảnh cần một câu mô tả (cho người khiếm thị và Google), ít nhất 5 ký tự.');
        $new[] = array('nhom' => (string)(isset($x['nhom']) ? $x['nhom'] : ''), 'ten' => $ten, 'nguon' => null, 'ty_le' => null, 'x' => 0.5, 'y' => 0.5,
                       'alt' => $alt, 'cap' => txt(isset($x['cap']) ? $x['cap'] : '', 120));
    }
    if (count($new) > 20) throw new QtError('Mỗi lần tải tối đa 20 ảnh.');
    $order = isset($in['thu_tu']) && is_array($in['thu_tu']) ? array_values(array_filter($in['thu_tu'], 'is_string')) : null;
    $vt = isset($in['vung_trong']) && is_array($in['vung_trong']) ? array_values(array_filter($in['vung_trong'], 'is_string')) : null;
    if ($vt !== null && count($vt) > 12) throw new QtError('Trang Vùng trồng hiện tối đa 12 ảnh.');
    $parts = array();
    if ($new) $parts[] = 'thêm ' . count($new) . ' ảnh';
    if ($sua) $parts[] = 'sửa ' . count($sua) . ' ảnh';
    if ($xoa) $parts[] = 'xóa ' . count($xoa) . ' ảnh';
    if ($order !== null) $parts[] = 'đổi thứ tự';
    if ($vt !== null) $parts[] = 'chọn ảnh trang Vùng trồng';
    if (!$parts) throw new QtError('Chưa có thay đổi nào.');
    $sha = gh_commit('Ảnh vườn: ' . implode(', ', $parts), array(F_ANH), function ($cur) use ($new, $sua, $xoa, $order, $vt) {
        $d = dec($cur[F_ANH], 'anh-vuon.json');
        $groups = array(); foreach ($d['nhom'] as $g) $groups[$g['ma']] = 1;
        $by = array(); foreach ($d['anh'] as $i => $a) $by[$a['ten']] = $i;
        foreach ($sua as $ten => $x) {
            if (!isset($by[$ten])) conflict('Ảnh ' . h($ten));
            $a = &$d['anh'][$by[$ten]];
            if (item_ver($a) !== (isset($x['v']) ? $x['v'] : '')) conflict('Ảnh này');
            if (isset($x['nhom'])) { if (!isset($groups[$x['nhom']])) throw new QtError('Nhóm ảnh không đúng.'); $a['nhom'] = $x['nhom']; }
            if (isset($x['alt'])) { $t = txt($x['alt'], 200); if (mb_strlen($t) < 5) throw new QtError('Mô tả ảnh cần ít nhất 5 ký tự.'); $a['alt'] = $t; }
            if (isset($x['cap'])) $a['cap'] = txt($x['cap'], 120);
            if (isset($x['an'])) { if ($x['an']) $a['an'] = true; else unset($a['an']); }
            unset($a);
        }
        foreach ($new as $a) { if (!isset($groups[$a['nhom']])) throw new QtError('Chị chọn nhóm cho ảnh mới.'); $d['anh'][] = $a; }
        if ($xoa) {
            $d['anh'] = array_values(array_filter($d['anh'], function ($a) use ($xoa) { return !in_array($a['ten'], $xoa, true); }));
            $d['vung_trong'] = array_values(array_filter($d['vung_trong'], function ($n) use ($xoa) { return !in_array($n, $xoa, true); }));
        }
        if ($order !== null) {
            $pos = array_flip($order); $n = count($order);
            $idx = array_keys($d['anh']);
            usort($idx, function ($i, $j) use ($d, $pos, $n) {
                $a = isset($pos[$d['anh'][$i]['ten']]) ? $pos[$d['anh'][$i]['ten']] : $n + $i;
                $b = isset($pos[$d['anh'][$j]['ten']]) ? $pos[$d['anh'][$j]['ten']] : $n + $j;
                return $a - $b;
            });
            $d['anh'] = array_map(function ($i) use ($d) { return $d['anh'][$i]; }, $idx);
        }
        if ($vt !== null) {
            $names = array(); foreach ($d['anh'] as $a) $names[$a['ten']] = 1;
            foreach ($vt as $n) if (!isset($names[$n])) throw new QtError('Ảnh ' . h($n) . ' không còn trong danh sách.');
            $d['vung_trong'] = $vt;
        }
        return array(F_ANH => json_py($d));
    }, $files);
    foreach ($files as $f) @unlink($f);
    return array($sha, $parts);
}

// ---------------------------------------------------------------- clip Vùng trồng
function save_clip($in) {
    $v = isset($in['v']) ? $in['v'] : '';
    $new_video = isset($in['moi']) && is_array($in['moi']) ? $in['moi'] : null;
    $files = array();
    $canh = array();
    $name = null;
    if ($new_video) {
        $name = 'v-vuon-' . date('ymd') . '-' . substr(bin2hex(random_bytes(3)), 0, 4);
        $vid = temp_path(isset($new_video['video']) ? $new_video['video'] : '', 'mp4');
        $files[GH_SRC . "assets/$name.mp4"] = $vid;
        $files[GH_SRC . "assets/$name.jpg"] = temp_path(isset($new_video['poster']) ? $new_video['poster'] : '');
    }
    $list = isset($in['canh']) && is_array($in['canh']) ? $in['canh'] : array();
    if (count($list) > 8) throw new QtError('Tối đa 8 cảnh.');
    foreach ($list as $k => $c) {
        $cap = txt(isset($c['cap']) ? $c['cap'] : '', 90);
        if (mb_strlen($cap) < 3) throw new QtError('Mỗi cảnh cần một tên ngắn.');
        $t = round((float)(isset($c['t']) ? $c['t'] : 0), 2);
        if ($t < 0 || $t > 600) throw new QtError('Mốc giây của cảnh không đúng.');
        $row = array('t' => $t, 's' => $t, 'cap' => $cap);
        if ($new_video) {
            $files[GH_SRC . "assets/$name-c" . ($k + 1) . '.jpg'] = temp_path(isset($c['anh']) ? $c['anh'] : '');
            $row['anh'] = "$name-c" . ($k + 1) . '.jpg';
        } else {
            $row['i'] = (int)(isset($c['i']) ? $c['i'] : -1);
        }
        $canh[] = $row;
    }
    $lead = txt(isset($in['lead']) ? $in['lead'] : '', 400);
    $label = txt(isset($in['label']) ? $in['label'] : '', 300);
    $an = !empty($in['an']);
    $msg = $new_video ? 'Thay clip trang Vùng trồng' : ($an ? 'Ẩn clip trang Vùng trồng' : 'Sửa clip trang Vùng trồng');
    $info = $new_video ? array('w' => (int)$new_video['w'], 'h' => (int)$new_video['h'], 'dai' => round((float)$new_video['dai'], 2)) : null;
    if ($info && ($info['w'] < 320 || $info['w'] > 4096 || $info['h'] < 240 || $info['h'] > 4096 || $info['dai'] <= 0 || $info['dai'] > 600)) throw new QtError('Thông tin video không đúng.');
    $sha = gh_commit($msg, array(F_CLIP), function ($cur) use ($v, $canh, $lead, $label, $an, $name, $info) {
        $d = dec($cur[F_CLIP], 'clip-vuon.json');
        if (item_ver($d) !== $v) conflict('Clip');
        if ($name) {
            $d['hd'] = "$name.mp4"; $d['sd'] = "$name.mp4"; $d['poster'] = "$name.jpg";
            $d['w'] = $info['w']; $d['h'] = $info['h']; $d['dai'] = $info['dai'];
            $d['canh'] = $canh;
        } elseif ($canh) {
            $old = $d['canh'];
            $out = array();
            foreach ($canh as $c) {
                if (!isset($old[$c['i']])) conflict('Clip');
                $o = $old[$c['i']];
                $o['cap'] = $c['cap'];
                if (abs($o['t'] - $c['t']) > 0.001) { $o['t'] = $c['t']; $o['s'] = $c['t']; }
                $out[] = $o;
            }
            usort($out, function ($a, $b) { return $a['s'] < $b['s'] ? -1 : 1; });
            $d['canh'] = $out;
        }
        $d['lead'] = $lead;
        if ($label !== '') $d['label'] = $label;
        $d['an'] = $an;
        return array(F_CLIP => json_py($d));
    }, $files);
    foreach ($files as $f) @unlink($f);
    return $sha;
}

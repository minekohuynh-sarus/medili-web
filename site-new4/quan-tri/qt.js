// Trang quản trị MeDili: phần chung (gọi máy chủ, biểu mẫu, thông báo, tiến độ đưa lên web).
'use strict';
const QT = window.QT = {};
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
QT.$ = $; QT.$$ = $$;
const CSRF = document.body.dataset.csrf || '';

QT.toast = (msg, err) => {
  const t = $('#qt-toast'); if (!t) return;
  t.textContent = msg; t.className = 'qt-toast' + (err ? ' loi' : ''); t.hidden = false;
  clearTimeout(t._h); t._h = setTimeout(() => { t.hidden = true }, err ? 9000 : 4200);
};

async function call(url, opt) {
  let r;
  try { r = await fetch(url, Object.assign({ credentials: 'same-origin', headers: {} }, opt)) }
  catch (e) { throw new Error('Mất kết nối mạng. Chị kiểm tra mạng rồi thử lại.') }
  let j = null;
  try { j = await r.json() } catch (e) { }
  if (!j) throw new Error(r.status === 413 ? 'Tệp quá lớn so với giới hạn của hosting.' : 'Máy chủ trả lời không đúng (mã ' + r.status + ').');
  if (!j.ok) { const e = new Error(j.loi || 'Có lỗi.'); e.code = r.status; throw e }
  return j;
}
QT.api = (name, data) => call('?api=' + name, { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-CSRF': CSRF }, body: JSON.stringify(data || {}) });
QT.get = name => call('?api=' + name, { method: 'GET' });
// tải tệp, có tiến độ
QT.upload = (name, fd, onp) => new Promise((ok, no) => {
  const x = new XMLHttpRequest();
  x.open('POST', '?api=' + name); x.setRequestHeader('X-CSRF', CSRF); x.responseType = 'json';
  x.upload.onprogress = e => { if (onp && e.lengthComputable) onp(e.loaded / e.total) };
  x.onload = () => { const j = x.response; if (j && j.ok) ok(j); else no(new Error(j && j.loi ? j.loi : x.status === 413 ? 'Tệp quá lớn so với giới hạn tải lên của hosting.' : 'Tải lên lỗi (mã ' + x.status + ').')) };
  x.onerror = () => no(new Error('Mất kết nối khi tải lên.'));
  x.send(fd);
});
QT.busy = (btn, on) => { if (!btn) return; btn.disabled = on; btn.setAttribute('aria-busy', on ? 'true' : 'false') };
QT.money = s => { const d = String(s || '').replace(/\D/g, ''); return d ? +d : null };
QT.fmt = n => n == null ? '' : String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, '.');
QT.esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

// thu giá trị biểu mẫu: hộp chọn -> true/false, còn lại là chữ
QT.collect = f => {
  const o = {};
  for (const el of f.elements) {
    if (!el.name || el.disabled || el.type === 'submit' || el.type === 'button') continue;
    if (el.type === 'checkbox') o[el.name] = el.checked;
    else if (el.type === 'radio') { if (el.checked) o[el.name] = el.value }
    else o[el.name] = el.value;
  }
  return o;
};
QT.hooks = {};   // QT.hooks[api] = (form, data) => data  (trang riêng bổ sung dữ liệu)

// ---------------------------------------------------------------- biểu mẫu chung
document.addEventListener('submit', async e => {
  const f = e.target.closest('form[data-api]'); if (!f) return;
  e.preventDefault();
  const btn = e.submitter || $('button[type=submit]', f);
  let data = QT.collect(f);
  if (btn && btn.name) data[btn.name] = btn.value === '1' ? true : btn.value === '0' ? false : btn.value;
  for (const k of ['pw2', 'moi2']) {
    const a = k === 'pw2' ? data.pw : data.moi;
    if (k in data && a !== data[k]) { QT.toast('Hai lần nhập mật khẩu chưa khớp.', true); return }
  }
  if (f.dataset.confirm && !confirm(f.dataset.confirm)) return;
  try {
    if (QT.hooks[f.dataset.api]) data = await QT.hooks[f.dataset.api](f, data);
    if (data === false) return;
    QT.busy(btn, true);
    const j = await QT.api(f.dataset.api, data);
    if (j.bao) QT.toast(j.bao);
    if (f.dataset.reset) f.reset();
    if (j.c) { QT.track(true); if (f.dataset.next) setTimeout(() => { location.href = f.dataset.next }, 900); else setTimeout(() => location.reload(), 900); return }
    if (f.dataset.next) { location.href = f.dataset.next; return }
    if (f.dataset.reload) { setTimeout(() => location.reload(), 600); return }
    if (!j.bao && !j.c) QT.toast('Không có gì thay đổi.');
  } catch (err) {
    QT.toast(err.message, true);
    if (err.code === 401) setTimeout(() => location.reload(), 1800);
  } finally { QT.busy(btn, false) }
});

// đếm ký tự
const counter = el => { const f = el.closest('.qt-f'), inp = f && $('input,textarea', f); if (!inp) return; const n = +el.dataset.dem, upd = () => { el.textContent = inp.value.length + '/' + n }; inp.addEventListener('input', upd); upd() };
$$('[data-dem]').forEach(counter);

// đăng xuất
document.addEventListener('click', async e => {
  const b = e.target.closest('[data-act="dang-xuat"]'); if (!b) return;
  try { await QT.api('dang-xuat') } catch (err) { }
  location.href = './';
});

// ---------------------------------------------------------------- cài đặt lần đầu: kiểm tra khoá
document.addEventListener('click', async e => {
  const b = e.target.closest('[data-act="khoa-kiem"]'); if (!b) return;
  const f = b.closest('form'), out = $('[data-khoa-kq]', f), tok = f.elements.token.value.trim();
  if (!tok) { f.elements.token.focus(); return }
  QT.busy(b, true); out.className = 'qt-note'; out.textContent = 'Đang kiểm tra với GitHub…';
  try {
    const j = await QT.api('khoa-kiem', { token: tok });
    out.className = 'qt-note ok';
    out.textContent = 'Khoá dùng được: tài khoản ' + j.gh_user + (j.het_han ? ', hết hạn ' + j.het_han : '') + (j.actions ? '.' : '. Chưa thấy quy trình dựng web trên GitHub, em (Claude) sẽ kiểm tra.');
  } catch (err) { out.className = 'qt-note loi'; out.textContent = err.message }
  finally { QT.busy(b, false) }
});

// ---------------------------------------------------------------- thông báo: link và xem trước
(() => {
  const f = $('form[data-api="thong-bao"]'); if (!f) return;
  const sel = f.elements.link_chon, other = $('[data-link-khac]', f), prev = $('[data-tb-prev] .mdtb', f);
  const draw = () => {
    other.hidden = sel.value !== '*';
    const chu = f.elements.chu.value.trim(), lab = f.elements.chu_link.value.trim() || 'Xem chi tiết';
    const quan = f.elements.kieu.value === 'quan-trong';
    prev.className = 'mdtb' + (quan ? ' qt' : '') + (f.elements.bat.checked ? '' : ' tat');
    $('p', prev).innerHTML = QT.esc(chu || 'Nội dung thông báo hiện ở đây.') + (sel.value ? ' <a href="#" tabindex="-1">' + QT.esc(lab) + '</a>' : '');
  };
  f.addEventListener('input', draw); f.addEventListener('change', draw); draw();
})();

// ---------------------------------------------------------------- đồng bộ ngay (Cài đặt)
document.addEventListener('click', async e => {
  const b = e.target.closest('[data-act="dong-bo"]'); if (!b) return;
  QT.busy(b, true);
  try {
    let tong = 0;
    for (let k = 0; k < 60; k++) {
      const j = await QT.api('dong-bo');
      if (j.ban) { QT.toast('Hosting đang tự đồng bộ, chị chờ một chút…'); await sleep(6000); continue }
      tong += j.xong || 0;
      if (!j.con) break;
      QT.toast('Đã đưa lên ' + tong + ' tệp, còn ' + j.con + ' tệp…');
    }
    QT.toast(tong ? 'Đã đồng bộ ' + tong + ' tệp. Web đang chạy bản mới nhất.' : 'Web đã là bản mới nhất.');
  } catch (err) { QT.toast(err.message, true) }
  finally { QT.busy(b, false) }
});

// ---------------------------------------------------------------- tiến độ đưa lên web
const sleep = ms => new Promise(r => setTimeout(r, ms));
QT.sleep = sleep;
let tracking = false;
QT.track = async fresh => {
  const box = $('#qt-trk'); if (!box || tracking) return;
  tracking = true;
  const steps = ['Đã lưu lên GitHub', 'Dựng lại web (khoảng 1–2 phút)', 'Đưa lên medili.vn'];
  const state = ['xong', 'dang', ''];
  let note = '', url = '';
  const draw = (title) => {
    box.innerHTML = `<button type="button" class="x" aria-label="Ẩn bảng tiến độ">×</button><h3>${title}</h3><ol>${steps.map((s, i) => `<li class="${state[i]}"><i></i><span>${s}</span></li>`).join('')}</ol>`
      + (note ? `<p>${note}</p>` : '') + (url ? `<p><a href="${url}" target="_blank" rel="noopener">Xem chi tiết trên GitHub ↗</a></p>` : '');
    box.hidden = false;
    $('.x', box).onclick = () => { box.hidden = true };
  };
  draw('Đang cập nhật web…');
  if (fresh) await sleep(4000);
  let fail = 0, synced = false;
  for (let k = 0; k < 240; k++) {
    let j;
    try { j = await QT.get('tien-do'); fail = 0 } catch (err) { if (++fail > 4) { note = QT.esc(err.message); draw('Tạm dừng theo dõi'); break } await sleep(6000); continue }
    url = j.url || '';
    if (j.buoc === 'cho' || j.buoc === 'dung') { state[1] = 'dang'; note = j.buoc === 'cho' ? 'GitHub đang nhận việc…' : ''; draw('Đang cập nhật web…'); await sleep(5000); continue }
    if (j.buoc === 'loi') { state[1] = 'loi'; note = QT.esc(j.loi || 'Có lỗi.'); draw('Chưa cập nhật được'); break }
    state[1] = 'xong';
    if (j.buoc === 'xong' || synced) { state[2] = 'xong'; note = 'Web medili.vn đã chạy bản mới. Chữ mới viết sẽ được dịch sang tiếng Anh, Nhật, Trung tối nay.'; url = ''; draw('Đã cập nhật web'); setTimeout(() => { box.hidden = true }, 15000); break }
    // dua: tải các trang đã dựng về hosting
    state[2] = 'dang'; note = 'Đang tải các trang mới về hosting…'; draw('Đang cập nhật web…');
    let tong = 0, ok = false;
    for (let s = 0; s < 80; s++) {
      let r;
      try { r = await QT.api('dong-bo') } catch (err) { note = QT.esc(err.message) + ' Hosting sẽ tự lấy bản mới trong vòng 30 phút.'; state[2] = 'loi'; draw('Chưa đưa lên hết'); tracking = false; return }
      if (r.ban) { note = 'Hosting đang tự đồng bộ, chờ một chút…'; draw('Đang cập nhật web…'); await sleep(6000); continue }
      tong += r.xong || 0;
      if (!r.con) { ok = true; break }
      note = `Đã tải ${tong} tệp, còn ${r.con} tệp…`; draw('Đang cập nhật web…');
    }
    if (ok) { synced = true; continue }   // hỏi lại tiến độ để đánh dấu xong
    break;
  }
  tracking = false;
};
if (document.body.dataset.dangDua) QT.track(false);
// menu trên điện thoại: cuộn tới mục đang mở
(() => { const a = $('.qt-nav a[aria-current]'); if (a && a.offsetLeft + a.offsetWidth > innerWidth - 40) a.parentNode.scrollLeft = a.offsetLeft - 16 })();

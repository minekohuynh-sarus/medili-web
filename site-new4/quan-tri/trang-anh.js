// Trang Ảnh vườn: thêm ảnh (thu nhỏ, đóng logo chìm MeDili ngay trên máy, không mang vị trí chụp), sửa chú thích, nhóm, thứ tự, ẩn,
// chọn 12 ảnh cho trang Vùng trồng. Logo chìm giống art/make_photos.py: logo kem mờ 62% góc dưới phải, có bóng mềm.
(() => {
  const { $, $$ } = QT;

  const LONG = 1600, SMALL = 760;
  let logo = null;
  const getLogo = () => logo || (logo = new Promise((ok, no) => { const i = new Image(); i.onload = () => ok(i); i.onerror = () => no(new Error('Không tải được logo MeDili.')); i.src = '../assets/logo-kem.png' }));
  const loadImg = file => new Promise((ok, no) => {
    const u = URL.createObjectURL(file), i = new Image();
    i.onload = () => { ok(i) }; i.onerror = () => { URL.revokeObjectURL(u); no(new Error('Máy này không mở được ảnh (ảnh HEIC của iPhone: chị chọn ảnh JPG, hoặc gửi ảnh qua Zalo rồi lưu lại).')) };
    i.src = u;
  });
  const toBlob = (c, q) => new Promise(ok => c.toBlob(ok, 'image/jpeg', q));
  function watermark(ctx, W, H, lg) {
    const r = W / H, k = r >= 2.5 ? .13 : r >= 1.2 ? .19 : r >= .95 ? .22 : .24;
    const lw = Math.round(W * k), lh = Math.round(lg.height * lw / lg.width);
    let x, y;
    if (r >= 2.5) { x = Math.floor((W - lw) / 2); y = H - lh - Math.round(H * .07) }
    else if (r < .95) { x = W - lw - Math.round(W * .05); y = H - lh - Math.round(H * .085) }
    else { const m = Math.round(Math.min(W, H) * .045); x = W - lw - m; y = H - lh - m }
    const off = W + lw + 50;
    ctx.save();
    ctx.shadowColor = 'rgba(20,12,8,.38)'; ctx.shadowBlur = 2 * Math.max(2, lw * .018);
    ctx.shadowOffsetX = off; ctx.shadowOffsetY = Math.max(1, Math.round(lw * .006));
    ctx.drawImage(lg, x - off, y, lw, lh);
    ctx.restore();
    ctx.globalAlpha = .62; ctx.drawImage(lg, x, y, lw, lh); ctx.globalAlpha = 1;
  }
  async function prepare(file) {
    const [img, lg] = await Promise.all([loadImg(file), getLogo()]);
    const w0 = img.naturalWidth, h0 = img.naturalHeight;
    if (Math.min(w0, h0) < 400) throw new Error('Ảnh quá nhỏ (' + w0 + '×' + h0 + '), chị chọn ảnh gốc rõ hơn.');
    const s = Math.min(1, LONG / Math.max(w0, h0)), W = Math.round(w0 * s), H = Math.round(h0 * s);
    const c = document.createElement('canvas'); c.width = W; c.height = H;
    const ctx = c.getContext('2d'); ctx.imageSmoothingEnabled = true; ctx.imageSmoothingQuality = 'high';
    ctx.drawImage(img, 0, 0, W, H);
    URL.revokeObjectURL(img.src);
    watermark(ctx, W, H, lg);
    const t = Math.min(1, SMALL / Math.max(W, H)), c2 = document.createElement('canvas');
    c2.width = Math.round(W * t); c2.height = Math.round(H * t);
    const x2 = c2.getContext('2d'); x2.imageSmoothingQuality = 'high'; x2.drawImage(c, 0, 0, c2.width, c2.height);
    const [big, small] = await Promise.all([toBlob(c, .8), toBlob(c2, .78)]);
    c.width = c.height = 0;
    return { big, small, w: W, h: H };
  }

  // ---- ảnh mới
  const up = $('[data-up]'), list = $('[data-up-list]'), act = $('[data-up-act]'), pick = $('[data-chon-anh]'), grp = $('[data-nhom-moi]');
  let items = [];
  const drop = $('.qt-drop', up);
  ['dragenter', 'dragover'].forEach(t => drop.addEventListener(t, () => drop.classList.add('keo')));
  ['dragleave', 'drop'].forEach(t => drop.addEventListener(t, () => drop.classList.remove('keo')));
  pick.addEventListener('change', async () => {
    const files = [...pick.files].slice(0, 20 - items.length);
    if (pick.files.length > files.length) QT.toast('Mỗi lần tối đa 20 ảnh.', true);
    pick.value = '';
    for (const f of files) {
      const it = { file: f, el: document.createElement('div') };
      it.el.className = 'qt-up-it';
      it.el.innerHTML = `<div class="qt-up-ph"></div><div class="qt-form" style="gap:8px"><p class="qt-up-st">Đang thu nhỏ và đóng logo… <small>${QT.esc(f.name)}</small></p>
        <label class="qt-f"><span>Mô tả ảnh <small>(cho người khiếm thị và Google, bắt buộc)</small></span><input name="alt" maxlength="200" placeholder="Vd. Bàn tay hái chùm Robusta chín đỏ"></label>
        <label class="qt-f"><span>Chú thích <small>(hiện khi xem ảnh lớn)</small></span><input name="cap" maxlength="120" placeholder="Vd. Hái chùm Robusta chín."></label>
        <button type="button" class="qt-btn small ghost" data-act="bo-1">Bỏ ảnh này</button></div>`;
      list.append(it.el); items.push(it); act.hidden = false;
      try {
        Object.assign(it, await prepare(f));
        const im = document.createElement('img'); im.src = URL.createObjectURL(it.small); im.alt = '';
        $('.qt-up-ph', it.el).replaceWith(im);
        $('.qt-up-st', it.el).innerHTML = `Đã sẵn sàng: ${it.w}×${it.h}, ${Math.round(it.big.size / 1024)} KB, có logo MeDili. <small>${QT.esc(f.name)}</small>`;
      } catch (err) { it.err = err.message; it.el.classList.add('loi'); $('.qt-up-st', it.el).textContent = err.message }
    }
  });
  up.addEventListener('click', async e => {
    const b = e.target.closest('[data-act]'); if (!b) return;
    if (b.dataset.act === 'bo-1') { const el = b.closest('.qt-up-it'); items = items.filter(i => i.el !== el); el.remove(); act.hidden = !items.length }
    if (b.dataset.act === 'bo-anh-moi') { items = []; list.innerHTML = ''; act.hidden = true }
    if (b.dataset.act !== 'tai-anh') return;
    const ok = items.filter(i => !i.err && i.big);
    if (!ok.length) { QT.toast('Chưa có ảnh nào sẵn sàng.', true); return }
    for (const i of ok) { const a = $('[name=alt]', i.el); if (a.value.trim().length < 5) { a.setAttribute('aria-invalid', 'true'); a.focus(); QT.toast('Mỗi ảnh cần một câu mô tả, ít nhất 5 ký tự.', true); return } a.removeAttribute('aria-invalid') }
    QT.busy(b, true);
    try {
      const them = [];
      for (const [k, i] of ok.entries()) {
        $('.qt-up-st', i.el).textContent = `Đang tải lên (${k + 1}/${ok.length})…`;
        const fd = new FormData(); fd.append('lon', i.big, 'lon.jpg'); fd.append('nho', i.small, 'nho.jpg');
        const j = await QT.upload('anh-tai', fd, p => { $('.qt-up-st', i.el).textContent = `Đang tải lên (${k + 1}/${ok.length}): ${Math.round(p * 100)}%` });
        them.push({ lon: j.lon, nho: j.nho, nhom: grp.value, alt: $('[name=alt]', i.el).value.trim(), cap: $('[name=cap]', i.el).value.trim() });
        $('.qt-up-st', i.el).textContent = 'Đã tải lên, đang lưu…';
      }
      await QT.api('anh-luu', { them });
      QT.toast('Đã thêm ' + them.length + ' ảnh. Web cập nhật sau khoảng 3–5 phút.');
      QT.track(true); items = []; setTimeout(() => location.reload(), 1200);
    } catch (err) { QT.toast(err.message, true) }
    finally { QT.busy(b, false) }
  });

  // ---- sửa ảnh đang có
  const figs = () => $$('.qt-ph'), bar = $('#qt-savebar');
  const vt0 = JSON.parse($('#qt-vt').textContent); let vt = vt0.slice();
  const order0 = figs().map(f => f.dataset.ten).join('|');
  const val = f => JSON.stringify([$('[name=cap]', f).value, $('[name=alt]', f).value, $('[name=nhom]', f).value, f.classList.contains('an')]);
  const init = new Map(figs().map(f => [f.dataset.ten, val(f)]));
  const recount = () => {
    $$('.qt-gal').forEach(s => { $('[data-dem-nhom]', s).textContent = $$('.qt-ph:not(.xoa)', s).length + ' ảnh' });
    const d = $('[data-dem-vt]'); if (d) d.textContent = vt.length;
  };
  const changes = () => {
    const sua = {}, xoa = [];
    figs().forEach(f => {
      const t = f.dataset.ten;
      if (f.classList.contains('xoa')) { xoa.push(t); return }
      const ch = val(f) !== init.get(t); f.classList.toggle('sua', ch);
      if (ch) sua[t] = { v: f.dataset.v, cap: $('[name=cap]', f).value, alt: $('[name=alt]', f).value, nhom: $('[name=nhom]', f).value, an: f.classList.contains('an') };
    });
    const order = figs().map(f => f.dataset.ten).join('|');
    return { sua, xoa, thu_tu: order !== order0 ? order.split('|') : null, vung_trong: vt.join('|') !== vt0.join('|') ? vt : null };
  };
  const mark = () => {
    const c = changes(), n = Object.keys(c.sua).length + c.xoa.length + (c.thu_tu ? 1 : 0) + (c.vung_trong ? 1 : 0);
    bar.hidden = !n; $('[data-dem-sua]', bar).textContent = n ? 'Có thay đổi chưa lưu' : '';
    recount();
  };
  document.addEventListener('input', e => { if (e.target.closest('.qt-ph')) mark() });
  document.addEventListener('change', e => {
    const f = e.target.closest('.qt-ph'); if (!f) return;
    if (e.target.name === 'nhom') { const s = $(`.qt-gal[data-nhom="${CSS.escape(e.target.value)}"] .qt-phs`); if (s) { s.append(f); f.scrollIntoView({ block: 'nearest' }) } }
    mark();
  });
  document.addEventListener('click', async e => {
    const b = e.target.closest('[data-act]'); if (!b) return;
    const f = b.closest('.qt-ph'), a = b.dataset.act;
    if (f) {
      if (a === 'len' && f.previousElementSibling) f.parentNode.insertBefore(f, f.previousElementSibling);
      if (a === 'xuong' && f.nextElementSibling) f.parentNode.insertBefore(f.nextElementSibling, f);
      if (a === 'an') { f.classList.toggle('an'); b.setAttribute('aria-pressed', f.classList.contains('an')) }
      if (a === 'vt') {
        const t = f.dataset.ten, on = vt.includes(t);
        if (!on && vt.length >= 12) { QT.toast('Trang Vùng trồng hiện tối đa 12 ảnh. Chị bỏ sao một ảnh khác trước.', true); return }
        vt = on ? vt.filter(x => x !== t) : vt.concat(t);
        f.classList.toggle('vt', !on); b.setAttribute('aria-pressed', !on);
      }
      if (a === 'xoa') {
        if (!f.classList.contains('xoa') && !confirm('Xóa ảnh này khỏi danh sách? (Nếu chỉ muốn tạm gỡ, chị bấm nút con mắt để ẩn.)')) return;
        f.classList.toggle('xoa'); f.style.opacity = f.classList.contains('xoa') ? .35 : '';
        if (f.classList.contains('xoa')) vt = vt.filter(x => x !== f.dataset.ten);
      }
      if (['len', 'xuong', 'an', 'vt', 'xoa'].includes(a)) { mark(); return }
    }
    if (a === 'bo-sua') { if (confirm('Bỏ mọi thay đổi chưa lưu?')) location.reload(); return }
    if (a !== 'luu-anh') return;
    const c = changes();
    for (const t in c.sua) if (c.sua[t].alt.trim().length < 5) { QT.toast('Mô tả ảnh cần ít nhất 5 ký tự.', true); return }
    if (c.xoa.length && !confirm('Xóa ' + c.xoa.length + ' ảnh khỏi danh sách?')) return;
    const data = { sua: c.sua }; if (c.xoa.length) data.xoa = c.xoa; if (c.thu_tu) data.thu_tu = c.thu_tu; if (c.vung_trong) data.vung_trong = c.vung_trong;
    QT.busy(b, true);
    try { await QT.api('anh-luu', data); QT.toast('Đã lưu. Web cập nhật sau khoảng 3–5 phút.'); QT.track(true); bar.hidden = true; setTimeout(() => location.reload(), 1200) }
    catch (err) { QT.toast(err.message, true) }
    finally { QT.busy(b, false) }
  });
  recount();
  addEventListener('beforeunload', e => { if (!bar.hidden || items.length) { e.preventDefault(); e.returnValue = '' } });
})();

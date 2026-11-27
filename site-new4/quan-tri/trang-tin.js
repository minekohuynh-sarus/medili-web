// Trang Tin tức: tìm bài, ẩn/hiện/đăng/xóa; soạn bài: nguồn tin, xem trước, đường dẫn.
(() => {
  const { $, $$ } = QT;
  // ---- danh sách
  const q = $('[data-loc]');
  if (q) q.addEventListener('input', () => {
    const t = q.value.trim().toLowerCase();
    $$('.qt-post').forEach(li => { li.hidden = !!t && !li.dataset.q.includes(t) });
  });
  const ask = { an: 'Ẩn bài này khỏi web? Đường dẫn cũ sẽ hiện trang báo bài không còn. Chị hiện lại được bất cứ lúc nào.', dang: 'Đăng bài nháp này lên web?',
    xoa: 'Xóa hẳn bài này? Không lấy lại được ở trang quản trị. Nếu chỉ muốn tạm gỡ, chị bấm Ẩn.' };
  document.addEventListener('click', async e => {
    const b = e.target.closest('[data-bai]'); if (!b) return;
    const li = b.closest('.qt-post'), viec = b.dataset.bai;
    if (ask[viec] && !confirm(ask[viec])) return;
    QT.busy(b, true);
    try { await QT.api('bai-co', { slug: li.dataset.slug, viec, v: li.dataset.v }); QT.track(true); setTimeout(() => location.reload(), 900) }
    catch (err) { QT.toast(err.message, true) }
    finally { QT.busy(b, false) }
  });

  // ---- soạn bài
  const f = $('form[data-api="bai-luu"]'); if (!f) return;
  const srcs = $('.qt-srcs', f);
  const row = () => { const d = srcs.firstElementChild.cloneNode(true); $$('input', d).forEach(i => { i.value = '' }); return d };
  f.addEventListener('click', e => {
    const b = e.target.closest('[data-act]'); if (!b) return;
    if (b.dataset.act === 'them-nguon') { if (srcs.children.length < 10) srcs.append(row()); $('input', srcs.lastElementChild).focus() }
    if (b.dataset.act === 'bo-nguon') { const r = b.closest('.qt-src'); if (srcs.children.length > 1) r.remove(); else $$('input', r).forEach(i => { i.value = '' }) }
  });
  // đường dẫn tự tạo theo tiêu đề (bài mới)
  const out = $('[data-slug-out]', f), slug = f.dataset.slug;
  const mk = s => s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/đ/g, 'd').replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 66).replace(/-+$/, '');
  const upd = () => { if (slug) return; const d = f.elements.date.value, t = mk(f.elements.title.value); out.textContent = t ? `tin-tuc-${t}-${d.slice(8, 10)}${d.slice(5, 7)}.html` : 'tự tạo theo tiêu đề' };
  f.elements.title.addEventListener('input', upd); f.elements.date.addEventListener('change', upd); upd();
  // xem trước
  const prev = $('[data-xem-truoc]', f);
  const draw = () => {
    const blocks = f.elements.body.value.replace(/\r/g, '').split(/\n\s*\n/).map(s => s.trim()).filter(Boolean);
    $('.qt-preview', prev).innerHTML = `<h2 style="font-size:1.6rem;margin-top:4px">${QT.esc(f.elements.title.value || 'Tiêu đề bài')}</h2>`
      + blocks.map(b => b.replace(/<[^<>]*>|[<>]/g, '')).map(b => /^#{1,3}\s*/.test(b) ? `<h2>${QT.esc(b.replace(/^#{1,3}\s*/, ''))}</h2>` : `<p>${QT.esc(b.replace(/\s*\n\s*/g, ' '))}</p>`).join('');
  };
  prev.addEventListener('toggle', () => { if (prev.open) draw() });
  f.addEventListener('input', () => { if (prev.open) draw() });
  // dữ liệu gửi đi: nguồn theo từng dòng
  QT.hooks['bai-luu'] = (form, d) => {
    d.slug = slug;
    d.sources = $$('.qt-src', form).map(r => ({ name: $('[name=src_name]', r).value.trim(), url: $('[name=src_url]', r).value.trim() })).filter(s => s.name || s.url);
    if (d.sources.some(s => !s.name)) { QT.toast('Nguồn nào cũng cần có tên báo.', true); return false }
    delete d.src_name; delete d.src_url;
    if (!slug && d.nhap === false && !confirm('Đăng bài này lên web?')) return false;
    return d;
  };
  let dirty = false;
  f.addEventListener('input', () => { dirty = true });
  f.addEventListener('submit', () => { dirty = false });
  addEventListener('beforeunload', e => { if (dirty) { e.preventDefault(); e.returnValue = '' } });
})();

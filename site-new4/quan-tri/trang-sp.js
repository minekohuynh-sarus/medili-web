// Trang Sản phẩm & giá: đánh dấu dòng đã sửa, kiểm tra giá, lưu một lần.
(() => {
  const { $, $$ } = QT;
  const cards = $$('.qt-prod'), bar = $('#qt-savebar');
  const snap = c => JSON.stringify($$('input,select', c).map(e => e.value));
  const init = new Map(cards.map(c => [c, snap(c)]));
  // ô giá: tự chấm phân cách nghìn khi gõ
  $$('.qt-money input').forEach(inp => {
    inp.addEventListener('input', () => {
      const pos = inp.value.length - inp.selectionStart, v = QT.money(inp.value);
      inp.value = v == null ? '' : QT.fmt(v);
      const p = Math.max(0, inp.value.length - pos); try { inp.setSelectionRange(p, p) } catch (e) { }
    });
  });
  const mark = () => {
    let n = 0;
    cards.forEach(c => {
      const ch = snap(c) !== init.get(c); c.classList.toggle('sua', ch); if (ch) n++;
      c.classList.toggle('het', $('select[name=st]', c).value === 'het');
    });
    bar.hidden = !n; $('[data-dem-sua]', bar).textContent = n + ' dòng đã sửa';
  };
  document.addEventListener('input', e => { if (e.target.closest('.qt-prod')) mark() });
  document.addEventListener('change', e => { if (e.target.closest('.qt-prod')) mark() });
  mark();
  const check = c => {
    const loai = c.dataset.loai, name = $('h3', c).textContent, g = n => { const e = $(`[name=${n}]`, c); return e ? QT.money(e.value) : null };
    const p = [g('p0'), g('p1'), g('p2')], st = $('select[name=st]', c).value;
    $$('.qt-money input', c).forEach(e => e.removeAttribute('aria-invalid'));
    const bad = (n, msg) => { const e = $(`[name=${n}]`, c); if (e) { e.setAttribute('aria-invalid', 'true'); e.focus() } throw new Error(name + ': ' + msg) };
    for (let i = 0; i < 3; i++) if (p[i] != null && (p[i] < 10000 || p[i] > 5000000)) bad('p' + i, 'giá cần từ 10.000 đến 5.000.000 đ.');
    if (loai === 'ngu') { if (p[0] == null) bad('p0', 'chị nhập giá túi 250 g.'); if (p[0] % 250) bad('p0', 'giá túi cần chia hết cho 250 đ.') }
    else for (let i = 0; i < 3; i++) if (p[i] != null && p[i] % 1000) bad('p' + i, 'giá theo kg cần tròn nghìn đồng (vd. 285.000).');
    if (loai === 'core') for (let i = 0; i < 3; i++) if (p[i] == null) bad('p' + i, 'dòng này cần đủ giá lẻ và hai mức giá sỉ.');
    if (loai === 'le') {
      if (p[0] == null && (p[1] != null || p[2] != null)) bad('p0', 'có giá sỉ thì cần có giá lẻ.');
      if ((p[1] == null) !== (p[2] == null)) bad(p[1] == null ? 'p1' : 'p2', 'nhập cả hai mức giá sỉ, hoặc để trống cả hai.');
    }
    if (loai !== 'ngu' && loai !== 'sap') {
      if (p[1] != null && p[1] > p[0]) bad('p1', 'giá sỉ 5–20 kg không cao hơn giá lẻ.');
      if (p[2] != null && p[1] != null && p[2] > p[1]) bad('p2', 'giá sỉ trên 20 kg không cao hơn giá sỉ 5–20 kg.');
    }
    if (loai === 'sap' && st !== 'sap' && p[0] == null) bad('p0', 'mở bán thì cần nhập giá lẻ.');
    const o = { v: c.dataset.v, st, p };
    $$('.qt-more input', c).forEach(e => { o[e.name] = e.value });
    return o;
  };
  document.addEventListener('click', async e => {
    const b = e.target.closest('[data-act]'); if (!b) return;
    if (b.dataset.act === 'bo-sua') { if (confirm('Bỏ mọi thay đổi chưa lưu?')) location.reload(); return }
    if (b.dataset.act !== 'luu-sp') return;
    const sp = {};
    try { cards.filter(c => c.classList.contains('sua')).forEach(c => { sp[c.dataset.id] = check(c) }) } catch (err) { QT.toast(err.message, true); return }
    if (!Object.keys(sp).length) return;
    QT.busy(b, true);
    try {
      await QT.api('san-pham', { sp });
      QT.track(true);
      cards.forEach(c => init.set(c, snap(c))); mark();
      QT.toast('Đã lưu. Web cập nhật sau khoảng 3–5 phút.');
      setTimeout(() => location.reload(), 1200);
    } catch (err) { QT.toast(err.message, true) }
    finally { QT.busy(b, false) }
  });
  addEventListener('beforeunload', e => { if (cards.some(c => c.classList.contains('sua'))) { e.preventDefault(); e.returnValue = '' } });
})();

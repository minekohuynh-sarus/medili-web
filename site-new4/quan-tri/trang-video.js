// Trang Video: sửa clip đang dùng (hiện/ẩn, lời giới thiệu, tên và mốc giây từng cảnh); thay clip mới (tải từng phần,
// lấy ảnh chờ và ảnh từng cảnh ngay trong trình duyệt). Video gửi từng phần 1,5 MB.
(() => {
  const { $, $$ } = QT;
  const form = $('form[data-api="clip-luu"]');
  QT.hooks['clip-luu'] = (f, d) => {
    d.v = f.dataset.v;
    d.canh = $$('[data-scenes] .qt-scene', f).map(r => ({ i: +r.dataset.i, t: parseFloat(String($('[name=t]', r).value).replace(',', '.')) || 0, cap: $('[name=cap]', r).value.trim() }));
    delete d.t; delete d.cap;
    if (d.canh.some(c => c.cap.length < 3)) { QT.toast('Mỗi cảnh cần một tên ngắn.', true); return false }
    return d;
  };

  // ---- clip mới
  const box = $('[data-newvid]'); if (!box) return;
  const pick = $('[data-chon-video]', box), body = $('[data-nv-body]', box), vid = $('[data-nv-video]', box), pcv = $('[data-nv-poster]', box),
        list = $('[data-nv-scenes]', box), prog = $('[data-nv-prog]', box);
  let file = null, poster = null, scenes = [];
  // đọc hộp moov của MP4 để biết chuẩn nén: H.264 (avc1) xem được trên mọi máy; HEVC (hvc1, hev1) của iPhone nhiều máy không xem được
  async function codec(f) {
    const rd = async (a, n) => new Uint8Array(await f.slice(a, a + n).arrayBuffer());
    let off = 0;
    for (let k = 0; k < 64 && off < f.size; k++) {
      const h = await rd(off, 16), dv = new DataView(h.buffer);
      let size = dv.getUint32(0), type = String.fromCharCode(...h.slice(4, 8));
      if (size === 1) size = Number(dv.getBigUint64(8)); else if (size === 0) size = f.size - off;
      if (size < 8) break;
      if (type === 'moov') {
        const m = await rd(off, Math.min(size, 8e6)), s = new TextDecoder('latin1').decode(m);
        if (/hvc1|hev1/.test(s)) return 'hevc';
        if (/avc1|avc3/.test(s)) return 'h264';
        return 'khac';
      }
      off += size;
    }
    return 'khac';
  }
  const grab = (w, h) => { const c = document.createElement('canvas'); c.width = w; c.height = h; const x = c.getContext('2d'), vw = vid.videoWidth, vh = vid.videoHeight, r = Math.max(w / vw, h / vh);
    x.imageSmoothingQuality = 'high'; x.drawImage(vid, (w - vw * r) / 2, (h - vh * r) / 2, vw * r, vh * r); return c };
  const blob = c => new Promise(ok => c.toBlob(ok, 'image/jpeg', .82));
  const seekTo = t => new Promise(ok => { const done = () => { vid.removeEventListener('seeked', done); ok() }; vid.addEventListener('seeked', done); vid.currentTime = t });
  const setPoster = async () => { const c = grab(1280, 720); poster = await blob(c); pcv.getContext('2d').drawImage(c, 0, 0, pcv.width, pcv.height) };
  const drawScenes = () => {
    list.innerHTML = scenes.length ? '' : '<p class="qt-note">Phát video, dừng ở đầu mỗi cảnh rồi bấm “Đánh dấu cảnh tại đây”. Không đánh dấu thì clip hiện một mình, không có danh sách cảnh.</p>';
    scenes.sort((a, b) => a.t - b.t).forEach((s, i) => {
      const r = document.createElement('div'); r.className = 'qt-scene';
      r.innerHTML = `<span></span><label class="qt-f qt-sec"><span>Giây</span><input value="${s.t.toFixed(1)}" readonly></label><label class="qt-f"><span>Tên cảnh ${i + 1}</span><input maxlength="90" value="${QT.esc(s.cap)}" placeholder="Vd. Hoa cà phê nở trắng trên cành."></label><button type="button" class="qt-ic danger" aria-label="Bỏ cảnh này"><svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 7h14M10 7V5h4v2M7 7l1 12h8l1-12"/></svg></button>`;
      r.firstElementChild.replaceWith(s.cv);
      $('input[maxlength]', r).addEventListener('input', e => { s.cap = e.target.value });
      $('button', r).addEventListener('click', () => { scenes = scenes.filter(x => x !== s); drawScenes() });
      list.append(r);
    });
  };
  pick.addEventListener('change', async () => {
    const f = pick.files[0]; pick.value = ''; if (!f) return;
    if (f.size > 40 * 1048576) { QT.toast('Video ' + (f.size / 1048576).toFixed(1) + ' MB, quá 40 MB. Chị cắt ngắn lại hoặc gửi em (Claude) ghép giúp.', true); return }
    const c = await codec(f);
    if (c === 'hevc') { QT.toast('Video dùng chuẩn nén HEVC của iPhone, nhiều máy Android và Windows không xem được. Chị đặt Camera › Định dạng › “Tương thích nhất” rồi quay lại, hoặc gửi video cho em (Claude).', true); return }
    if (c !== 'h264') { QT.toast('Không đọc được chuẩn nén của video này. Chị chọn video MP4 quay từ điện thoại hoặc máy ảnh.', true); return }
    file = f; poster = null; scenes = [];
    vid.src = URL.createObjectURL(f); body.hidden = false;
    vid.addEventListener('loadedmetadata', async () => {
      if (vid.duration > 600) { QT.toast('Video dài quá 10 phút.', true); return }
      await seekTo(Math.min(2, vid.duration / 4)); await setPoster(); await seekTo(0); drawScenes();
    }, { once: true });
  });
  box.addEventListener('click', async e => {
    const b = e.target.closest('[data-act]'); if (!b || !file) return;
    const a = b.dataset.act;
    if (a === 'nv-poster') { await setPoster(); QT.toast('Đã lấy ảnh chờ ở giây ' + vid.currentTime.toFixed(1) + '.') }
    if (a === 'nv-canh') {
      if (scenes.length >= 8) { QT.toast('Tối đa 8 cảnh.', true); return }
      const t = Math.round(vid.currentTime * 10) / 10;
      if (scenes.some(s => Math.abs(s.t - t) < .5)) { QT.toast('Đã có cảnh ở gần giây này.', true); return }
      const cv = grab(384, 216); scenes.push({ t, cap: '', cv }); drawScenes();
    }
    if (a === 'nv-bo') { file = null; body.hidden = true; vid.removeAttribute('src'); vid.load() }
    if (a !== 'nv-luu') return;
    if (scenes.some(s => s.cap.trim().length < 3)) { QT.toast('Mỗi cảnh cần một tên ngắn.', true); return }
    if (!confirm('Thay clip đang dùng ở trang Vùng trồng bằng video này?')) return;
    QT.busy(b, true); prog.hidden = false;
    const bar = $('i', prog), txt = $('span', prog), show = (p, t) => { bar.style.width = Math.round(p * 100) + '%'; txt.textContent = t };
    try {
      const CH = 1536 * 1024, n = Math.ceil(file.size / CH);
      let id = '';
      for (let i = 0; i < n; i++) {
        const fd = new FormData(); fd.append('id', id); fd.append('i', i); fd.append('n', n); fd.append('phan', file.slice(i * CH, (i + 1) * CH), 'phan.bin');
        const j = await QT.upload('video-tai', fd, p => show((i + p) / n * .9, `Đang tải video ${Math.round((i + p) / n * 100)}%`));
        id = j.id;
      }
      show(.92, 'Đang tải ảnh chờ và ảnh từng cảnh…');
      const one = async bl => { const fd = new FormData(); fd.append('anh', bl, 'anh.jpg'); return (await QT.upload('video-anh', fd)).anh };
      const p = await one(poster);
      const canh = [];
      for (const s of scenes) canh.push({ t: s.t, cap: s.cap.trim(), anh: await one(await blob(s.cv)) });
      show(.97, 'Đang lưu…');
      await QT.api('clip-luu', { v: form.dataset.v, hien: form.elements.hien.checked, lead: form.elements.lead.value, label: form.elements.label.value,
        moi: { video: id, poster: p, w: vid.videoWidth, h: vid.videoHeight, dai: vid.duration }, canh });
      show(1, 'Đã lưu. Web cập nhật sau khoảng 3–5 phút.');
      QT.track(true); file = null; setTimeout(() => location.reload(), 1500);
    } catch (err) { QT.toast(err.message, true); show(0, '') ; prog.hidden = true }
    finally { QT.busy(b, false) }
  });
  addEventListener('beforeunload', e => { if (file) { e.preventDefault(); e.returnValue = '' } });
})();

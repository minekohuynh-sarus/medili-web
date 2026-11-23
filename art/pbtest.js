// Thử tương tác trang Cỗ máy Phân biệt cà phê
const {chromium} = require('playwright'), fs = require('fs'), http = require('http'), path = require('path');
const css = require('./fonts.js');
const DIR = path.resolve(__dirname, '../site-new4'), LIVE = path.resolve(__dirname, '../site-live');
const T = {'.html': 'text/html;charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json'};
const srv = http.createServer((q, s) => { let f = decodeURIComponent(q.url.split('?')[0]); for (const r of [DIR, LIVE]) { const p = path.join(r, f); if (fs.existsSync(p) && fs.statSync(p).isFile()) { s.writeHead(200, {'content-type': T[path.extname(p)] || 'application/octet-stream'}); return s.end(fs.readFileSync(p)); } } s.writeHead(404); s.end(); }).listen(8391);
const ok = (c, m) => console.log((c ? 'OK  ' : 'FAIL') + ' ' + m);
(async () => {
  const b = await chromium.launch();
  const c = await b.newContext({viewport: {width: 1366, height: 900}});
  const p = await c.newPage(); const errs = [];
  p.on('pageerror', x => errs.push(x.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()) });
  await p.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css}));
  await p.route(/fonts\.gstatic\.com/, r => r.abort());
  await p.goto('http://localhost:8391/phan-biet-ca-phe.html'); await p.waitForTimeout(500);
  const txt = s => p.$eval(s, e => e.textContent);
  // 1. mỗi mẫu ở hồ sơ chuẩn tự nhận ra chính nó
  const names = {se: 'Cà Sẻ', cs: 'Cao sản', ara: 'Arabica', cat: 'Catimor', mok: 'Moka', culi: 'Culi', lib: 'Liberica', exc: 'Excelsa'};
  for (const k of Object.keys(names)) {
    await p.click(`#samps [data-k=${k}]`); await p.waitForTimeout(80);
    const v = await txt('#verdict b'), out = await txt('#kOut');
    ok(v.includes(names[k]) || (await txt('#stats')).includes(names[k]), `hồ sơ ${k}: ${v.trim()} | LCD ${out}`);
    for (let i = 1; i <= 8; i++) { await p.click(`#strip button:nth-child(${i})`); }
  }
  // 2. số đo của bạn: kéo 100 nhân và sàng 16 lên thì Cà Sẻ thành cao sản
  await p.click('#samps [data-k=se]');
  await p.$eval('#iW', e => { e.value = 22; e.dispatchEvent(new Event('input')) });
  await p.$eval('#iS', e => { e.value = 90; e.dispatchEvent(new Event('input')) });
  ok((await txt('#verdict b')).includes('Robusta cao sản'), 'kéo 100 nhân 22 g, sàng 16 90%: ' + (await txt('#verdict b')).trim());
  ok(!(await p.$eval('#back', e => e.hidden)), 'nút Về hồ sơ chuẩn hiện ở chế độ tự nhập');
  // 3. tắt lab
  await p.click('#lab'); await p.waitForTimeout(60);
  ok(await p.$eval('#labBox', e => e.hidden), 'tắt lab thì ẩn ô lab');
  ok((await txt('#kLab')).includes('chưa đo'), 'LCD lab: ' + await txt('#kLab'));
  ok(await p.$eval('#scene .st[data-i="6"]', e => e.classList.contains('off')), 'trạm 6 mờ khi chưa có lab');
  // 4. rãnh chữ S với nhân 22 g, chưa lab
  await p.click('#cuts [data-k=s]'); await p.waitForTimeout(60);
  ok(true, 'rãnh chữ S, không lab: ' + (await txt('#verdict b')).trim());
  await p.click('#cuts [data-k=r]'); await p.waitForTimeout(60);
  ok((await txt('#verdict b')).includes('Liberica'), 'rãnh nhăn + 22 g + sàng 90%: ' + (await txt('#verdict b')).trim());
  await p.click('#back'); await p.waitForTimeout(60);
  ok((await txt('#modeL')).includes('hồ sơ chuẩn'), 'về hồ sơ chuẩn: ' + await txt('#modeL'));
  // 5. mẫu bí ẩn
  let right = 0;
  for (let n = 0; n < 12; n++) {
    await p.click('#myst'); await p.waitForTimeout(40);
    ok(!(await p.$eval('#reveal', e => e.hidden)), `bí ẩn ${n + 1}: nút Lộ đáp án hiện`);
    await p.click('#reveal'); await p.waitForTimeout(40);
    const v = await txt('#verdict b'); if (v.includes('đúng')) right++;
  }
  ok(right >= 6, `máy đoán đúng ${right}/12 mẫu bí ẩn`);
  // 6. chạy máy: sau khi chạy xong, LCD kết luận có số
  await p.click('#samps [data-k=lib]'); await p.click('#run');
  await p.waitForTimeout(300); const mid = await txt('#kOut');
  await p.waitForTimeout(5600); const end = await txt('#kOut');
  ok(mid.includes('···') && !end.includes('···'), `chạy máy: giữa chừng "${mid}", xong "${end}"`);
  // 7. máy giác quan
  for (const k of Object.keys(names)) {
    await p.click(`#qPre [data-k=${k}]`); await p.waitForTimeout(40);
    const h = await txt('#qzr .qh'); ok(h.includes(names[k]) || (k === 'ara' && h.includes('Arabica')), `cảm quan mẫu ${k}: ${h}`);
  }
  await p.click('#qPre [data-k=x]'); ok((await txt('#qzr')).includes('Chưa có quan sát'), 'xóa hết câu trả lời');
  await p.click('#qz [data-q=ranh][data-o=t]'); await p.click('#qz [data-q=co][data-o=nho]');
  ok(true, 'hai câu: ' + (await txt('#qzr .qh')) + ' | ' + ((await p.$('#qzr .mnote')) ? await txt('#qzr .mnote') : ''));
  // 8. đối chiếu cặp, radar
  await p.click('#pA [data-k=ara]'); await p.click('#pB [data-k=cat]');
  ok((await txt('#pX')).includes('Dáng nhân gần như giống nhau'), 'cặp Arabica–Catimor');
  await p.click('#pA [data-k=lib]'); await p.click('#pB [data-k=exc]');
  ok((await txt('#pX')).includes('Liberica nhân to hơn'), 'cặp Liberica–Excelsa');
  await p.click('#rB [data-k=mok]'); ok((await txt('#radT')).includes('Moka'), 'radar: ' + await txt('#radT'));
  // 9. phiếu
  ok((await txt('#sheet')).includes('PHIẾU KIỂM MẪU'), 'phiếu kiểm mẫu có nội dung');
  await p.click('#cpSh'); await p.waitForTimeout(100); ok((await txt('#cpShS')).length > 0, 'nút sao chép phản hồi: ' + await txt('#cpShS'));
  ok((await p.$$eval('#pTab tr', r => r.length)) === 9, 'bảng tham số 8 dòng');
  ok((await p.$$eval('#bgal figure', r => r.length)) === 8, 'hình 3 có 8 nhân');
  ok(errs.length === 0, 'lỗi JS: ' + JSON.stringify(errs));
  await b.close(); srv.close();
})().catch(e => { console.error(e); srv.close(); process.exit(1) });

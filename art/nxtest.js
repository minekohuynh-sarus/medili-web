// Thử tương tác trang Chọn nhân xanh
const {chromium} = require('playwright'), fs = require('fs'), http = require('http'), path = require('path');
const css = require('./fonts.js');
const DIR = path.resolve(__dirname, '../site-new4'), LIVE = path.resolve(__dirname, '../site-live');
const T = {'.html': 'text/html;charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json'};
const srv = http.createServer((q, s) => { let f = decodeURIComponent(q.url.split('?')[0]); for (const r of [DIR, LIVE]) { const p = path.join(r, f); if (fs.existsSync(p) && fs.statSync(p).isFile()) { s.writeHead(200, {'content-type': T[path.extname(p)] || 'application/octet-stream'}); return s.end(fs.readFileSync(p)); } } s.writeHead(404); s.end(); }).listen(8397);
let nf = 0; const ok = (c, m) => { if (!c) nf++; console.log((c ? 'OK  ' : 'FAIL') + ' ' + m) };
(async () => {
  const html = fs.readFileSync(path.join(DIR, 'nhan-xanh.html'), 'utf8');
  // (bản công khai) kiểm tra không còn ký hiệu giá trên trang
  ok(!html.includes('₫'), 'không có ký hiệu ₫ trong mã trang');
  const b = await chromium.launch();
  const c = await b.newContext({viewport: {width: 1366, height: 900}});
  const p = await c.newPage(); const errs = [];
  p.on('pageerror', x => errs.push(x.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()) });
  await p.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css}));
  await p.route(/fonts\.gstatic\.com/, r => r.abort());
  await p.goto('http://localhost:8397/nhan-xanh.html'); await p.waitForTimeout(500);
  const txt = s => p.$eval(s, e => e.textContent);
  const pick = async (k, v) => { await p.click(`#q-${k} input[value="${v}"]`); };
  const reset = async () => { await p.click('#nx-rs'); await p.waitForTimeout(80); };
  const top = () => p.$$eval('#nx-sug .sg-n', a => a.map(x => x.dataset.id));
  ok((await txt('#nx-cnt')).trim() === '0 / 13', 'ban đầu 0/13');
  ok((await txt('#nx-sug')).includes('Trả lời vài câu'), 'ban đầu chưa có gợi ý');
  // kịch bản
  const S = [
    [[['gu','dam'],['loai','R'],['ro','cs'],['sang','16'],['sc','tm']], 'r16bm', 'đậm truyền thống, cao sản, S16'],
    [[['gu','chua'],['loai','A'],['chin','99'],['sc','washed'],['sang','18']], 'a18w99', 'Arabica washed 99 % S18'],
    [[['loai','A'],['vu','26']], 'a18w98m', 'Arabica vụ mới'],
    [[['loai','R'],['ro','culi']], 'rc18bm', 'Culi'],
    [[['loai','R'],['ro','se'],['gu','ngot']], 'rse', 'Ro Sẻ'],
    [[['loai','R'],['ro','fine'],['sc','natural'],['chin','99']], 'r18n99', 'Fine Robusta natural 99 %'],
    [[['loai','R'],['ro','fine'],['sc','honey'],['chin','97']], 'r18h97', 'Fine Robusta honey 97–98 %'],
    [[['gu','trai'],['loai','A'],['sc','natural']], 'a18n89', 'Arabica natural'],
    [[['loai','A'],['sang','14']], 'a14w97', 'Arabica S14'],
    [[['muc','sx'],['gu','dam']], 'r18bm', 'chế biến, gu đậm'],
  ];
  for (const [ans, want, name] of S) {
    await reset(); for (const [k, v] of ans) await pick(k, v); await p.waitForTimeout(40);
    const t = await top(); ok(t[0] === want, `${name}: hợp nhất ${t[0]} (mong ${want}) | ${t.join(', ')}`);
  }
  // Arabica thì câu Robusta bị khoá, tổng còn 12
  await reset(); await pick('loai', 'A');
  ok(await p.$eval('#q-ro', e => e.disabled), 'chọn Arabica thì khoá câu Robusta');
  ok((await txt('#nx-cnt')).trim() === '1 / 12', 'tổng còn 12 câu: ' + await txt('#nx-cnt'));
  await pick('loai', 'R'); ok(!(await p.$eval('#q-ro', e => e.disabled)), 'đổi sang Robusta thì mở lại');
  // phối: nền Robusta + hương Arabica
  await reset(); await pick('loai', 'RA'); await pick('gu', 'can');
  const ks = await p.$$eval('#nx-sug .sg-k', a => a.map(x => x.textContent));
  const ids = await top();
  ok(ks[0] === 'Nền Robusta' && ks[1] === 'Hương Arabica', 'phối blend: ' + ks.join(' / '));
  ok(ids[0].startsWith('r') && ids[1].startsWith('a'), 'nền là Robusta, hương là Arabica: ' + ids.join(', '));
  ok((await txt('#nx-tips')).includes('9 : 1'), 'có lưu ý tỉ lệ phối');
  // lưu ý
  const tipCase = [[[['loai','A'],['gu','dam']], 'thường cần Robusta'], [[['loai','R'],['ro','se'],['sang','18']], 'hiếm khi đạt S18'],
    [[['muc','sx'],['sc','honey']], 'chế biến công nghiệp'], [[['loai','R'],['sc','washed']], 'Robusta washed chưa có sẵn'],
    [[['loai','A'],['sc','honey']], 'Arabica honey chưa có sẵn'], [[['sl','tan'],['mau','khong']], 'nên thử mẫu'],
    [[['ro','fine'],['chin','0']], 'Fine Robusta cần hái chín'], [[['sc','tm'],['chin','99']], 'không cam kết tỉ lệ chín']];
  for (const [ans, frag] of tipCase) { await reset(); for (const [k, v] of ans) await pick(k, v); await p.waitForTimeout(30);
    ok((await txt('#nx-tips')).includes(frag) && !(await p.$eval('#nx-tipw', e => e.hidden)), 'lưu ý: ' + frag); }
  // phiếu: đầy đủ 13 câu, đánh dấu dòng, liên hệ
  await reset();
  for (const [k, v] of [['muc','xr'],['gu','ngot'],['loai','R'],['ro','fine'],['chin','97'],['sc','honey'],['sang','18'],['vu','25'],['sl','bao'],['tan','thang'],['mau','nhan'],['giao','hcm'],['ben','dn']]) await pick(k, v);
  ok((await txt('#nx-cnt')).trim() === '13 / 13', 'đủ 13 câu');
  ok((await txt('#nx-sum .gia')).includes('Liên hệ để nhận báo giá mỗi ngày'), 'phiếu ghi: liên hệ để nhận báo giá mỗi ngày');
  await p.click('#l-r18h98 input[name=pick]'); await p.click('#l-a18w99 input[name=pick]');
  ok((await txt('#nx-pk')).includes('MD-R18-H98') && (await txt('#nx-pk')).includes('MD-A18-W99'), 'dòng đánh dấu vào phiếu');
  ok(await p.$eval('#nx-gf', e => e.classList.contains('off') && !e.getAttribute('href')), 'chưa có tên, số thì nút gửi tắt');
  await p.click('#nx-gf'); ok((await txt('#nx-st')).includes('mục D'), 'bấm nút tắt thì nhắc nhập liên hệ');
  await p.fill('#nx-name', 'Anh Minh'); await p.fill('#nx-ph', '0901 234 567'); await p.fill('#nx-org', 'Xưởng rang Mộc'); await p.fill('#nx-note', 'Cần độ ẩm dưới 12,5 %');
  const href = await p.$eval('#nx-gf', e => e.getAttribute('href') || '');
  ok(href.startsWith('https://docs.google.com/forms/') && href.includes('entry.1445823936=Anh%20Minh') && href.includes('entry.907299194=0901234567'), 'mở phiếu Google Form có tên và số');
  ok(href.length < 7000, 'độ dài link phiếu ' + href.length);
  const m = await txt('#nx-msg');
  for (const f of ['PHIẾU CHỌN NHÂN XANH · MEDILI', 'Đơn vị: Xưởng rang Mộc', 'Gu: Đậm mà ngọt hậu', 'Robusta: Fine Robusta', 'Độ chín: Chín 97–98 %', 'Sơ chế: Honey', 'Sàng: S18',
    'Mỗi lần mua: 1–16 bao', 'Bên mua: Doanh nghiệp', 'Dòng quan tâm: MD-R18-H98', 'MeDili gợi ý: MD-R18-H97', 'Ghi chú: Cần độ ẩm', 'Liên hệ: Anh Minh | 0901234567'])
    ok(m.includes(f), 'tin nhắn có: ' + f);
  // lưu và tải lại
  await p.reload(); await p.waitForTimeout(400);
  ok((await txt('#nx-cnt')).trim() === '13 / 13' && (await p.$eval('#nx-name', e => e.value)) === 'Anh Minh' && await p.$eval('#l-r18h98 input[name=pick]', e => e.checked), 'tải lại trang vẫn giữ câu trả lời');
  // lọc danh mục
  await p.click('#nx-fl [data-f=A]'); ok(await p.$eval('#l-r18bm', e => e.hidden) && !(await p.$eval('#l-a18w99', e => e.hidden)), 'lọc Arabica');
  await p.click('#nx-fl [data-f=all]'); ok(!(await p.$eval('#l-r18bm', e => e.hidden)), 'lọc tất cả');
  // gợi ý đánh dấu ★ trong danh mục, bấm gợi ý nhảy tới dòng
  ok(await p.$eval('#l-r18h97', e => e.classList.contains('sugd')), 'dòng gợi ý có dấu sao');
  await p.click('#nx-sug .sg-n'); await p.waitForTimeout(200); ok(await p.$eval('#l-r18h97', e => e.classList.contains('hl')), 'bấm gợi ý thì sáng dòng trong danh mục');
  // làm lại
  await reset(); ok((await txt('#nx-cnt')).trim() === '0 / 13' && !(await p.$eval('#l-r18h98 input[name=pick]', e => e.checked)), 'làm lại xoá hết');
  await p.reload(); await p.waitForTimeout(300); ok((await txt('#nx-cnt')).trim() === '0 / 13', 'sau làm lại, tải lại vẫn trống');
  const vis = await p.evaluate(() => document.body.innerText);
  ok(!vis.includes('₫') && !/\d[\d.]*\s?(đ|đồng)\/kg/.test(vis), 'trang không hiện con số giá hay ký hiệu ₫');
  for (const sel of ['.p-head .lead', '#nx-sum .gia', '#danh-muc .nxprice', '#bao-gia .nxquote'])
    ok((await txt(sel)).includes('Liên hệ để nhận báo giá mỗi ngày'), 'có câu liên hệ báo giá ở ' + sel);
  const ho = fs.readFileSync(path.join(DIR, 'horeca.html'), 'utf8');
  ok(ho.includes('Liên hệ để nhận báo giá mỗi ngày.') && !ho.includes('hq-gx'), 'HORECA: ô nhân xanh chỉ ghi liên hệ báo giá');
  ok(errs.length === 0, 'lỗi JS: ' + JSON.stringify(errs));
  // điện thoại: thanh tiến độ dưới đáy
  const m2 = await (await b.newContext({viewport: {width: 390, height: 844}, isMobile: true, hasTouch: true})).newPage();
  await m2.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css})); await m2.route(/fonts\.gstatic\.com/, r => r.abort());
  await m2.goto('http://localhost:8397/nhan-xanh.html'); await m2.waitForTimeout(300);
  ok(await m2.$eval('#nx-bar', e => e.hidden), 'điện thoại: đầu trang chưa hiện thanh');
  await m2.evaluate(() => document.querySelector('#q-sc').scrollIntoView()); await m2.waitForTimeout(400);
  ok(!(await m2.$eval('#nx-bar', e => e.hidden)), 'điện thoại: đang trả lời thì hiện thanh tiến độ');
  await m2.evaluate(() => document.querySelector('#nx-sum').scrollIntoView()); await m2.waitForTimeout(400);
  ok(await m2.$eval('#nx-bar', e => e.hidden), 'điện thoại: tới phiếu thì ẩn thanh');
  console.log(nf ? `${nf} lỗi` : 'TẤT CẢ ĐẠT');
  await b.close(); srv.close();
})().catch(e => { console.error(e); srv.close(); process.exit(1) });

const {chromium} = require('playwright'), fs = require('fs'), http = require('http'), path = require('path');
const css = require('./fonts.js');
const DIR = path.resolve(__dirname, '../site-new4'), LIVE = path.resolve(__dirname, '../site-live');
const T = {'.html': 'text/html;charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json'};
const srv = http.createServer((q, s) => { let f = decodeURIComponent(q.url.split('?')[0]); for (const r of [DIR, LIVE]) { const p = path.join(r, f); if (fs.existsSync(p) && fs.statSync(p).isFile()) { s.writeHead(200, {'content-type': T[path.extname(p)] || 'application/octet-stream'}); return s.end(fs.readFileSync(p)); } } s.writeHead(404); s.end(); }).listen(8396);
(async () => {
  const b = await chromium.launch(); const c = await b.newContext({viewport: {width: 1200, height: 900}}); const p = await c.newPage();
  await p.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css}));
  await p.route(/fonts\.gstatic\.com/, r => r.abort());
  await p.goto('http://localhost:8396/nhan-xanh.html'); await p.waitForTimeout(500);
  if (process.argv[2] === 'filled') await p.evaluate(() => {
    for (const [k, v] of [['muc','xr'],['gu','ngot'],['loai','R'],['ro','fine'],['chin','97'],['sc','honey'],['sang','18'],['vu','25'],['sl','bao'],['tan','thang'],['mau','nhan'],['giao','hcm'],['ben','dn']]) document.querySelector(`#q-${k} input[value="${v}"]`).click();
    document.querySelector('#nx-name').value = 'Anh Minh'; document.querySelector('#nx-ph').value = '0901234567'; document.querySelector('#nx-org').value = 'Xưởng rang Mộc';
    document.querySelector('#nx-name').dispatchEvent(new Event('input', {bubbles: true}));
  });
  await p.waitForTimeout(300);
  await p.pdf({path: path.join(__dirname, 'shots', 'nx-print-' + (process.argv[2] || 'blank') + '.pdf'), format: 'A4', printBackground: false, preferCSSPageSize: true});
  await b.close(); srv.close();
})();

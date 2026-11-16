// Chụp khung nhìn (không full page) sau khi cuộn, để thấy phiếu dính bên phải
const {chromium} = require('playwright'), fs = require('fs'), http = require('http'), path = require('path');
const css = require('./fonts.js');
const DIR = path.resolve(__dirname, '../site-new4'), LIVE = path.resolve(__dirname, '../site-live');
const T = {'.html': 'text/html;charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json'};
const [,, out, width, height, dark, scrollSel, action] = process.argv;
const srv = http.createServer((q, s) => { let f = decodeURIComponent(q.url.split('?')[0]); for (const r of [DIR, LIVE]) { const p = path.join(r, f); if (fs.existsSync(p) && fs.statSync(p).isFile()) { s.writeHead(200, {'content-type': T[path.extname(p)] || 'application/octet-stream'}); return s.end(fs.readFileSync(p)); } } s.writeHead(404); s.end(); }).listen(8394);
(async () => {
  const b = await chromium.launch(); const w = +width, mob = w < 600;
  const c = await b.newContext({viewport: {width: w, height: +height}, isMobile: mob, hasTouch: mob, colorScheme: dark === 'dark' ? 'dark' : 'light'});
  const p = await c.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css}));
  await p.route(/fonts\.gstatic\.com/, r => r.abort());
  await p.goto('http://localhost:8394/nhan-xanh.html'); await p.waitForTimeout(500);
  if (action) { await p.evaluate(action); await p.waitForTimeout(300); }
  if (scrollSel) { await p.evaluate(s => document.querySelector(s).scrollIntoView({block: 'start'}), scrollSel); await p.waitForTimeout(700); }
  await p.screenshot({path: path.join(__dirname, 'shots', out)});
  console.log(out, 'errors', JSON.stringify(errs));
  await b.close(); srv.close();
})().catch(e => { console.error(e); srv.close(); process.exit(1) });

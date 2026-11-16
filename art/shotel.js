// node shotel.js <page> <selector> <out> <width> [dark] [scale] [action]
const {chromium} = require('playwright'), fs = require('fs'), http = require('http'), path = require('path');
const css = require('./fonts.js');
const [,, page, sel, outName, width, dark, scale, action] = process.argv;
const DIR = path.resolve(__dirname, '../site-new4'), LIVE = path.resolve(__dirname, '../site-live');
const T = {'.html': 'text/html;charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json'};
const port = 8700 + Math.floor(Math.random()*500);
const srv = http.createServer((q, s) => { let f = decodeURIComponent(q.url.split('?')[0]); for (const r of [DIR, LIVE]) { const p = path.join(r, f); if (fs.existsSync(p) && fs.statSync(p).isFile()) { s.writeHead(200, {'content-type': T[path.extname(p)] || 'application/octet-stream'}); return s.end(fs.readFileSync(p)); } } s.writeHead(404); s.end(); }).listen(port);
(async () => {
  const b = await chromium.launch(); const w = +width, mob = w < 600;
  const c = await b.newContext({viewport: {width: w, height: mob ? 844 : 900}, deviceScaleFactor: +(scale || 1), isMobile: mob, hasTouch: mob, colorScheme: dark === 'dark' ? 'dark' : 'light'});
  const p = await c.newPage(); const errs = [];
  p.on('pageerror', x => errs.push(x.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()) });
  await p.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css}));
  await p.route(/fonts\.gstatic\.com/, r => r.abort());
  await p.goto(`http://localhost:${port}/${page}`); await p.waitForTimeout(700);
  if (action) { await p.evaluate(action); await p.waitForTimeout(900); }
  const el = await p.$(sel); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(200);
  await el.screenshot({path: path.join(__dirname, 'shots', outName)});
  console.log(outName, 'errors', errs);
  await b.close(); srv.close();
})().catch(e => { console.error(e); srv.close(); process.exit(1) });

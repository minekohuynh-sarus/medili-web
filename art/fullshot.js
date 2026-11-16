const {chromium} = require('playwright'), fs = require('fs'), http = require('http'), path = require('path');
const css = require('./fonts.js');
const DIR = path.resolve(__dirname, '../site-new4'), LIVE = path.resolve(__dirname, '../site-live');
const T = {'.html': 'text/html;charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json'};
const [,, page, out, width, dark, action] = process.argv;
const srv = http.createServer((q, s) => { let f = decodeURIComponent(q.url.split('?')[0]); for (const r of [DIR, LIVE]) { const p = path.join(r, f); if (fs.existsSync(p) && fs.statSync(p).isFile()) { s.writeHead(200, {'content-type': T[path.extname(p)] || 'application/octet-stream'}); return s.end(fs.readFileSync(p)); } } s.writeHead(404); s.end(); }).listen(8392);
(async () => {
  const b = await chromium.launch(); const w = +width;
  const c = await b.newContext({viewport: {width: w, height: 900}, colorScheme: dark === 'dark' ? 'dark' : 'light'});
  const p = await c.newPage();
  await p.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css}));
  await p.route(/fonts\.gstatic\.com/, r => r.abort());
  await p.goto('http://localhost:8392/' + page); await p.waitForTimeout(600);
  if (action) { await p.evaluate(action); await p.waitForTimeout(800); }
  await p.addStyleTag({content: '.mnav{position:static!important}'});
  await p.screenshot({path: path.join(__dirname, 'shots', out), fullPage: true});
  await b.close(); srv.close();
})().catch(e => { console.error(e); srv.close(); process.exit(1) });

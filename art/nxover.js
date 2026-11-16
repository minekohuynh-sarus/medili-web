const {chromium} = require('playwright'), fs = require('fs'), http = require('http'), path = require('path');
const css = require('./fonts.js');
const DIR = path.resolve(__dirname, '../site-new4'), LIVE = path.resolve(__dirname, '../site-live');
const T = {'.html': 'text/html;charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json'};
const srv = http.createServer((q, s) => { let f = decodeURIComponent(q.url.split('?')[0]); for (const r of [DIR, LIVE]) { const p = path.join(r, f); if (fs.existsSync(p) && fs.statSync(p).isFile()) { s.writeHead(200, {'content-type': T[path.extname(p)] || 'application/octet-stream'}); return s.end(fs.readFileSync(p)); } } s.writeHead(404); s.end(); }).listen(8395);
(async () => {
  const b = await chromium.launch();
  for (const w of [360, 390, 700, 1024]) {
    const c = await b.newContext({viewport: {width: w, height: 800}, isMobile: w < 600, hasTouch: w < 600});
    const p = await c.newPage();
    await p.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css}));
    await p.route(/fonts\.gstatic\.com/, r => r.abort());
    await p.goto('http://localhost:8395/nhan-xanh.html'); await p.waitForTimeout(400);
    const r = await p.evaluate((W) => {
      const out = []; const sw = document.documentElement.scrollWidth;
      document.querySelectorAll('body *').forEach(e => { const b = e.getBoundingClientRect(); if (b.right > W + 1 && b.width > 0) { const par = e.parentElement.getBoundingClientRect(); if (par.right <= W + 1) out.push((e.tagName + '.' + e.className + '#' + e.id).slice(0, 70) + ' right=' + Math.round(b.right) + ' w=' + Math.round(b.width)) } });
      return {sw, out: out.slice(0, 12)};
    }, w);
    console.log(w, 'scrollWidth', r.sw); r.out.forEach(x => console.log('   ', x));
    await c.close();
  }
  await b.close(); srv.close();
})();

// Kiểm tra toàn site sau khi gộp Manus: tràn khung, lỗi, link nội bộ, menu, Tìm gu, HORECA
const {chromium} = require('playwright'), fs = require('fs'), http = require('http'), path = require('path');
const css = require('./fonts.js');
const NEW = path.resolve(__dirname, '../site-new4'), LIVE = path.resolve(__dirname, '../site-live');
const SK = p => `<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light;box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}html{scroll-padding-top:env(safe-area-inset-top,0px)}body{margin:0;padding:0;font:14px -apple-system,BlinkMacSystemFont,sans-serif;background:#fff;color:#000}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style></head><body>${p}</body></html>`;
const T = {'.html': 'text/html;charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json'};
const srv = http.createServer((q, s) => {
  let f = decodeURIComponent(q.url.split('?')[0].split('#')[0]);
  if (f === '/' || f === '/index.html') { s.writeHead(200, {'content-type': T['.html']}); return s.end(SK(fs.readFileSync(NEW + '/index.html', 'utf8'))); }
  for (const r of [NEW, LIVE]) { const p = path.join(r, f); if (fs.existsSync(p) && fs.statSync(p).isFile()) { s.writeHead(200, {'content-type': T[path.extname(p)] || 'application/octet-stream'}); return s.end(fs.readFileSync(p)); } }
  s.writeHead(404); s.end();
}).listen(8144);
const out = path.join(__dirname, 'shots5'); fs.mkdirSync(out, {recursive: true});
const pages = fs.readdirSync(NEW).filter(f => f.endsWith('.html'));
const only = process.argv[2];
(async () => {
  const b = await chromium.launch();
  const mk = async (o, url) => {
    const c = await b.newContext({...o, hasTouch: !!o.isMobile}); const p = await c.newPage(); p._e = [];
    p.on('pageerror', x => p._e.push(x.message)); p.on('console', m => { if (m.type() === 'error') p._e.push(m.text()) });
    p.on('requestfailed', r => { if (!/fonts\.g/.test(r.url())) p._e.push('FAIL ' + r.url()) });
    p.on('response', r => { if (r.status() >= 400) p._e.push(r.status() + ' ' + r.url()) });
    await p.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css}));
    await p.route(/fonts\.gstatic\.com/, r => r.abort());
    await p.goto('http://localhost:8144/' + (url === 'index.html' ? '' : url)); await p.waitForTimeout(450); return p;
  };
  const over = p => p.evaluate(() => { const W = document.documentElement.clientWidth; const bad = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.width && r.right > W + 1 && !e.closest('.tw,.scroller,.trip,.mh-pan,.histw,.strip,.pfs') }).slice(0, 4).map(e => e.tagName + '.' + (e.className.baseVal ?? e.className)); return [document.documentElement.scrollWidth - W, bad] });
  const links = new Set();
  for (const f of pages) {
    if (only && f !== only) continue;
    for (const [w, dark] of [[390, false], [1366, false], [360, true]]) {
      const p = await mk({viewport: {width: w, height: w < 600 ? 844 : 900}, deviceScaleFactor: 1, isMobile: w < 600, colorScheme: dark ? 'dark' : 'light'}, f);
      const o = await over(p);
      if (o[0] > 0 || o[1].length || p._e.length) console.log('!!', f, w, dark ? 'dark' : '', JSON.stringify(o), p._e.slice(0, 4));
      if (w === 1366) (await p.evaluate(() => [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')))).forEach(h => links.add(f + ' -> ' + h));
      await p.context().close();
    }
  }
  // link nội bộ
  const bad = [...links].filter(x => { const h = x.split(' -> ')[1]; if (/^(https?:|tel:|mailto:|#)/.test(h)) return false; const f = h.split('#')[0]; if (f === './' || f === '') return false; return !fs.existsSync(path.join(NEW, f)) && !fs.existsSync(path.join(LIVE, f)) });
  console.log('link hỏng', bad.length, bad.slice(0, 10));
  console.log('link ngoài', [...new Set([...links].map(x => x.split(' -> ')[1]).filter(h => /^https?:/.test(h)).map(h => h.replace(/(\?|#).*/, '')))].join(' | '));
  await b.close(); srv.close();
})().catch(e => { console.error(e); srv.close(); process.exit(1) });

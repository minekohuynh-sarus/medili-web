// Quét chữ hiển thị (innerText) + mọi link ra ngoài trên bản đã đăng
const {chromium} = require('playwright'), fs = require('fs'), http = require('http'), path = require('path');
const css = require('./fonts.js');
const DIR = path.resolve(__dirname, '../live21'), LIVE = path.resolve(__dirname, '../site-live');
const T = {'.html': 'text/html;charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.json': 'application/json'};
const srv = http.createServer((q, s) => { let f = decodeURIComponent(q.url.split('?')[0]); for (const r of [DIR, LIVE]) { const p = path.join(r, f); if (fs.existsSync(p) && fs.statSync(p).isFile()) { s.writeHead(200, {'content-type': T[path.extname(p)] || 'application/octet-stream'}); return s.end(fs.readFileSync(p)); } } s.writeHead(404); s.end(); }).listen(8393);
const PAT = /Fuller|\bRao\b|Hofmann|Clarke|Buffo|Avallone|Marraccini|De Castro|Moroney|Cordoba|Toddy|Wisconsin|IARC|Phan 2017|Gross|Báo Lâm Đồng|Tuổi Trẻ|Dân Trí|VietNamNet|cộng sự|et al/g;
(async () => {
  const b = await chromium.launch(); const p = await (await b.newContext({viewport: {width: 1366, height: 900}})).newPage();
  await p.route(/fonts\.googleapis\.com/, r => r.fulfill({status: 200, contentType: 'text/css', body: css}));
  await p.route(/fonts\.gstatic\.com/, r => r.abort());
  let n = 0;
  for (const f of fs.readdirSync(DIR).filter(x => x.endsWith('.html')).sort()) {
    await p.goto('http://localhost:8393/' + f); await p.waitForTimeout(250);
    const r = await p.evaluate(() => {
      document.querySelectorAll('details').forEach(d => d.open = true);
      const ext = [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')).filter(h => /^https?:/.test(h) && !/zalo|facebook|maps|tel:|mailto:/.test(h));
      return {t: document.body.innerText, ext};
    });
    const hits = [...new Set(r.t.match(PAT) || [])];
    const src = (r.t.match(/Nguồn tổng hợp\./g) || []).length;
    if (hits.length || r.ext.length) { console.log('XEM LAI', f, hits, r.ext); n++; }
    else console.log('OK', f, src ? '· có “Nguồn tổng hợp.”' : '');
  }
  console.log(n ? `${n} trang cần xem` : 'Tất cả sạch');
  await b.close(); srv.close();
})().catch(e => { console.error(e); srv.close(); process.exit(1) });

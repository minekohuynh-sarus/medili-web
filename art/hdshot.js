// Chụp ảnh dự phòng cho trang Hướng dẫn pha: site-new4/assets/hd-<mô hình>.webp (720 × 720, nền trong suốt).
// Ảnh này hiện khi trình duyệt không chạy được 3D. Chạy lại sau khi sửa mô hình trong hd3d.js và dựng web:
//   cd art && python3 build_manus.py && node hdshot.js
const http = require('http'), fs = require('fs'), path = require('path');
const {chromium} = require('playwright');

const ROOT = path.join(__dirname, '..', 'site-new4');
const MODELS = ['bean', 'grinder', 'phin', 'pour-over', 'espresso', 'cold-brew'];
const TYPES = {'.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json',
  '.webp': 'image/webp', '.jpg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml', '.woff2': 'font/woff2'};

function serve() {
  const srv = http.createServer((req, res) => {
    const p = path.normalize(decodeURIComponent(req.url.split('?')[0])).replace(/^(\.\.[\/\\])+/, '');
    const f = path.join(ROOT, p.endsWith('/') ? p + 'index.html' : p);
    if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
    res.writeHead(200, {'content-type': TYPES[path.extname(f)] || 'application/octet-stream'});
    fs.createReadStream(f).pipe(res);
  });
  return new Promise(r => srv.listen(0, '127.0.0.1', () => r(srv)));
}

(async () => {
  const srv = await serve(), base = `http://127.0.0.1:${srv.address().port}/`;
  const browser = await chromium.launch({args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist']});
  const page = await browser.newPage({viewport: {width: 800, height: 800}});
  page.on('pageerror', e => console.log('lỗi trang:', e.message));
  const only = process.argv.slice(2);
  for (const m of only.length ? only : MODELS) {
    await page.goto(base + 'huong-dan-pha.html?shot=' + m);
    await page.waitForFunction(() => window.__shot, null, {timeout: 60000});
    const url = await page.evaluate(() => window.__shot);
    const buf = Buffer.from(url.split(',')[1], 'base64');
    if (!url.startsWith('data:image/webp')) throw new Error('trình duyệt không xuất được WebP');
    fs.writeFileSync(path.join(ROOT, 'assets', `hd-${m}.webp`), buf);
    console.log(`hd-${m}.webp`, Math.round(buf.length / 1024), 'KB');
  }
  await browser.close(); srv.close();
})().catch(e => { console.error(e); process.exit(1); });

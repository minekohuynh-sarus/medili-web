// CSS phông cục bộ thay cho Google Fonts khi chụp thử
const fs = require('fs'), path = require('path');
const base = path.join(__dirname, 'node_modules/@fontsource');
const want = [
  ['be-vietnam-pro', 'Be Vietnam Pro', ['400', '500', '600', '700']],
  ['big-shoulders-display', 'Big Shoulders Display', ['700', '800']],
  ['jetbrains-mono', 'JetBrains Mono', ['500', '700']],
  ['playfair-display', 'Playfair Display', ['600-italic']],
];
let css = '';
for (const [dir, fam, files] of want) {
  for (const f of files) {
    const src = fs.readFileSync(path.join(base, dir, f + '.css'), 'utf8');
    const re = /\/\*\s*(\S+)\s*\*\/\s*@font-face\s*\{([^}]*)\}/g;
    let m;
    while ((m = re.exec(src))) {
      if (!/-(vietnamese|latin|latin-ext)-\d/.test(m[1])) continue;
      const body = m[2];
      const file = /url\(\.\/files\/([^)]+?\.woff2)\)/.exec(body)[1];
      const ur = /unicode-range:\s*([^;]+);/.exec(body);
      const w = /font-weight:\s*(\d+)/.exec(body)[1];
      const st = /font-style:\s*(\w+)/.exec(body)[1];
      const data = fs.readFileSync(path.join(base, dir, 'files', file)).toString('base64');
      css += `@font-face{font-family:"${fam}";font-style:${st};font-weight:${w};font-display:block;src:url(data:font/woff2;base64,${data}) format("woff2")${ur ? ';unicode-range:' + ur[1].trim() : ''}}\n`;
    }
  }
}
module.exports = css;

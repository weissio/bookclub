// Rendert die Konzepte über einen eigenen Server auf Port 8801.
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const dir = __dirname;
const srv = http.createServer((q, r) => {
  const f = path.join(dir, decodeURIComponent(q.url.split('?')[0].split('#')[0]));
  if (!f.startsWith(dir) || !fs.existsSync(f)) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' }); fs.createReadStream(f).pipe(r);
}).listen(8801, async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  const jobs = process.argv.slice(2).length ? process.argv.slice(2) : ['a', 'b'];
  for (const k of jobs) {
    for (const [hash, out] of [['', `konzept-${k}.png`], ['#4', `konzept-${k}-4buecher.png`]]) {
      await p.goto(`http://localhost:8801/konzept-${k}.html${hash}`, { waitUntil: 'networkidle' });
      await p.reload({ waitUntil: 'networkidle' });
      await p.evaluate(() => document.fonts.ready);
      // Flächenanteil "Am Lesen" messen
      const r = await p.evaluate(() => { const e = document.querySelector('.lesen').getBoundingClientRect(); return { top: e.top, h: e.height }; });
      console.log(out, 'Am Lesen', Math.round(r.top), '+', Math.round(r.h), '=', (r.h / 844 * 100).toFixed(1) + '%');
      await p.screenshot({ path: path.join(dir, out) });
    }
  }
  await b.close(); srv.close();
});

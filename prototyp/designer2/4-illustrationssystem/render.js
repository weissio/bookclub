const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const dir = __dirname, PORT = 8804;
const srv = http.createServer((q, r) => { const f = path.join(dir, decodeURIComponent(q.url.split('?')[0])); fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, {'Content-Type': 'text/html; charset=utf-8'}); r.end(d); } }); });
srv.listen(PORT, async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  for (const [html, png] of process.argv.slice(2).map(x => x.split(':'))) {
    await p.goto(`http://localhost:${PORT}/${html}`, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    const m = await p.evaluate(() => { const e = document.querySelector('[data-mess]'); if (!e) return null; const r = e.getBoundingClientRect(); return {top: r.top, bottom: r.bottom, h: r.height, pct: (r.height / 844 * 100).toFixed(1)}; });
    await p.screenshot({ path: path.join(dir, png) });
    console.log(png, JSON.stringify(m));
  }
  await b.close(); srv.close();
});

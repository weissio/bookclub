// Rendert die Konzepte über einen eigenen Server auf Port 8802.
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const dir = __dirname;

// 4-Bücher-Varianten aus den Hauptdateien ableiten
for (const k of ['a', 'b']) {
  const src = path.join(dir, `konzept-${k}.html`);
  if (!fs.existsSync(src)) continue;
  const html = fs.readFileSync(src, 'utf8')
    .replace('<body class="zwei">', '<body class="vier">');
  fs.writeFileSync(path.join(dir, `konzept-${k}-4buecher.html`), html);
}

const server = http.createServer((req, res) => {
  const f = path.join(dir, decodeURIComponent(req.url.split('?')[0]));
  if (!f.startsWith(dir) || !fs.existsSync(f)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  fs.createReadStream(f).pipe(res);
}).listen(8802, async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  for (const name of ['konzept-a', 'konzept-a-4buecher', 'konzept-b', 'konzept-b-4buecher']) {
    if (!fs.existsSync(path.join(dir, name + '.html'))) continue;
    await page.goto(`http://localhost:8802/${name}.html`, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const m = await page.evaluate(() => {
      const r = document.querySelector('.lesen').getBoundingClientRect();
      return { top: Math.round(r.top), h: Math.round(r.height) };
    });
    console.log(name, 'Am Lesen', m, 'Anteil Bildschirm', (m.h / 844 * 100).toFixed(1) + '%', 'Anteil Inhalt (54-754)', (m.h / 700 * 100).toFixed(1) + '%');
    await page.screenshot({ path: path.join(dir, name + '.png') });
  }
  await browser.close();
  server.close();
});

// Rendert die Konzepte über einen eigenen lokalen Server auf Port 8803.
const http = require('http');
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const dir = __dirname;
const server = http.createServer((req, res) => {
  const f = path.join(dir, decodeURIComponent(req.url.split('?')[0]));
  if (!f.startsWith(dir) || !fs.existsSync(f)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(fs.readFileSync(f));
});

const jobs = [
  ['konzept-a.html', 'konzept-a.png'],
  ['konzept-a-4buecher.html', 'konzept-a-4buecher.png'],
  ['konzept-b.html', 'konzept-b.png'],
  ['konzept-b-4buecher.html', 'konzept-b-4buecher.png'],
];

server.listen(8803, async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  for (const [html, png] of jobs) {
    if (!fs.existsSync(path.join(dir, html))) continue;
    await page.goto('http://localhost:8803/' + html, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const fonts = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family));
    await page.screenshot({ path: path.join(dir, png) });
    console.log(png, 'Schriften:', [...new Set(fonts)].join(', ') || 'keine');
  }
  await browser.close();
  server.close();
});

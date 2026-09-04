// Render an intro's GSAP timeline to MP4, frame by frame, in landscape and portrait.
// usage: node scripts/render-video.js intros/02-walk-in-reveal.html [fps]
// Needs: playwright (npm i playwright), ffmpeg on PATH, and `python3 -m http.server 8765` running in the repo root.
const { chromium } = require('playwright');
const { execSync } = require('child_process');
const fs = require('fs'), path = require('path');

const file = process.argv[2] || 'intros/02-walk-in-reveal.html';
const fps = +(process.argv[3] || 30);
const HOLD = 0.6;   // seconds to hold on the final frame
const SIZES = [{ name: 'landscape', w: 1920, h: 1080 }, { name: 'portrait', w: 1080, h: 1920 }];
const GSAP_LOCAL = process.env.GSAP_LOCAL;   // optional path to gsap.min.js when the CDN is unreachable

(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined, args: ['--no-sandbox'] });
  for (const s of SIZES) {
    const ctx = await browser.newContext({ viewport: { width: s.w, height: s.h }, deviceScaleFactor: 1 });
    if (GSAP_LOCAL) await ctx.route(/cdnjs\.cloudflare\.com.*gsap/, r => r.fulfill({ path: GSAP_LOCAL, contentType: 'application/javascript' }));
    await ctx.route(/fonts\.(googleapis|gstatic)\.com/, r => r.fulfill({ status: 200, contentType: 'text/css', body: '' }));
    const page = await ctx.newPage();
    await page.goto(`http://localhost:8765/${file}?render`);
    for (let k = 0; k < 100; k++) { if (await page.evaluate(() => !!window.__tl)) break; await page.waitForTimeout(200); }
    await page.evaluate(() => Promise.all([...document.images].map(i => i.decode().catch(() => {}))));
    const dur = await page.evaluate(() => window.__tl.duration());
    const n = Math.ceil((dur + HOLD) * fps);
    const dir = path.join('video', 'frames', s.name); fs.rmSync(dir, { recursive: true, force: true }); fs.mkdirSync(dir, { recursive: true });
    for (let i = 0; i < n; i++) {
      const t = Math.min(i / fps, dur);
      await page.evaluate(t => { window.__tl.seek(t, true); return true; }, t);   // suppressEvents so onComplete never fires; return a scalar, the timeline itself does not serialize
      await page.screenshot({ path: path.join(dir, String(i).padStart(4, '0') + '.jpg'), type: 'jpeg', quality: 94 });
    }
    const base = path.basename(file, '.html');
    const out = `video/out/${base}-${s.name}.mp4`;
    execSync(`ffmpeg -y -loglevel error -framerate ${fps} -i ${dir}/%04d.jpg -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart ${out}`);
    console.log(out, `${n} frames, ${(dur + HOLD).toFixed(2)}s`);
    await ctx.close();
  }
  await browser.close();
})();

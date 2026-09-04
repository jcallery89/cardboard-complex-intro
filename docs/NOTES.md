# Working notes

Short entries, newest at the top. What was tried, what worked, what to do next.

## 2026-09-04, second pass: assets, type, wordmark, video (Cowork session)
- Steve's seven walk-in frames (street to interior) are in `assets/source/walk-in/`. They are not continuous with each other (sign, door type, posters, people change), so they are used as an establishing shot only. `docs/PROMPT-PACK.md` has the regeneration plan and prompts to fix that properly.
- 2x upscales (Lanczos plus unsharp) of the seven frames and the closed-door plate are in `assets/img/2x/`. Modest gain, no generative upscaler is reachable from the sandbox. Treat as a stopgap.
- Type trials: `docs/type-specimen.html` shows three systems on the real copy (A Alfa Slab/Oswald/Lora, B Fraunces/Barlow Condensed/Source Serif 4, C Bricolage/DM Sans). B matches the 3D logo best. Decision pending with JC and Steve. Intros still use the reference page fonts until then.
- Flat wordmarks: `scripts/make-wordmark.py` outlines "CardBoard / Complex / TRADING CARD COLLECTIBLES" from local font files into `assets/logo/wordmark-{A,B,C}*.svg` (plus transparent variants and PNGs). The B in CardBoard carries a corrugation stripe pattern as a flat nod to the 3D logo.
- `intros/02-walk-in-reveal.html`: street frame registered on the door in plate pixels (`#street` at -445, -411), camera starts pulled back so the whole street frame fills the viewport, dollies in over 2.6s, street dissolves to the plate during the last second, then the 01 door reveal. `?render` builds the timeline paused and exposes `window.__tl`.
- `scripts/render-video.js` seeks that timeline frame by frame in headless Chromium and encodes with ffmpeg: `video/out/02-walk-in-reveal-{landscape,portrait}.{mp4,webm}`, 1920x1080 and 1080x1920 at 30fps, 6.2s. Gotcha: `page.evaluate` must return a scalar, returning the timeline object hangs Playwright; and seek with suppressEvents true or onComplete fires during capture.
- `intros/03-video-intro.html` plays the render (orientation picks the file, mp4 then webm) and hands off to the room. The film's last frame is the interior cropped to the film's aspect, so on handoff the room camera starts on that crop and settles to rest over 0.9s instead of jumping. Autoplay refusal or a decode error drops straight into the room.
- Still open: the man with the box is still cut off by the interior during the door open (visible in the video). Mobile swipe navigation in the room. Vault label off frame at 16:10.

## 2026-09-04, baseline check of 01 (Cowork session)
- Opened 01 in headless Chromium at 1440x900 and 390x844, screenshots at t=0, 1.5s, 2.2s, final, plus a station move. Reveal timing reads well and the final frame lands exactly on the idle room, handoff is invisible.
- Door slab was a hair left and low. Remeasured the opening from the plate with a dark-pixel mask: left .386, right .621, top .376, bottom .843 (was .373 / .613 / .385 / .849). Verified with a green overlay of the slab rectangle; edges now sit on the frame.
- Stations were positioned in viewport percent, so they drifted badly: at 16:10 "Collectors only" sat on the helmets (vault door is cropped off the right edge), and at 390 wide every label piled onto the TV. Rewrote the room so the render lives in a 2400x1018 box (#room-img) that JS cover-fits to the viewport; stations and camera anchors are now fractions of the render, and labels counter-scale so they stay readable. goTo() clamps the move so the render edges never show.
- Still open: on 16:10 and narrower the idle crop hides the vault door, so its label is off frame; on phones only the TV station is visible in the idle view. The brief calls for swipe between stations on mobile, which now has the right foundation (image-space anchors). Consider a slight idle pan so the vault peeks in on 16:10.
- Headless note: cdnjs and Google Fonts are blocked in the cloud sandbox, so the screenshot script intercepts the GSAP request and serves a local npm copy. Fonts fall back in screenshots only.

## 2026-09-04, project scaffolded
- Split Steve's 4-up door mock into single frames in `assets/img/`. Only `exterior-door-closed.jpg` is used; the others are reference.
- Built `intros/01-door-reveal.html`: door slab shrinks upward with a scrolling corrugation, light spill on the sidewalk, camera pushes through the opening and lands on the interior render at cover fit. Five station hotspots with a glide-to-station camera and a caption panel.
- Known issues in 01: the man carrying the box is covered by the interior once the door starts opening (he is baked into the exterior plate). Station positions are percentages of the viewport, so they drift on unusual aspect ratios; pin them to image pixels when the interior is split into layers. Door geometry variables have not been checked in a browser yet.
- Door opening on the plate measured at left .373, right .613, top .385, bottom .849.

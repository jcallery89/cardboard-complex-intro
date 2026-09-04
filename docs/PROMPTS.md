# Prompts to try in Claude Code

Start every session with `claude` in the repo root. Claude Code reads `CLAUDE.md` automatically. Good first prompts:

**Check the baseline**
> Open intros/01-door-reveal.html in the browser, screenshot it at t=0, t=1.5s and after the intro completes, and tell me whether the door slab lines up with the door opening in the exterior plate. Adjust the --door-* variables if it is off.

**Fix the foreground man**
> The man carrying the box in exterior-door-closed.jpg gets covered when the door opens. Cut him out into assets/img/exterior-man.png with a transparent background, add him as a foreground layer above the door in 01, and make sure he scales with the camera push.

**Make a second take**
> Copy 01 to 02-door-reveal-parallax.html. Split interior-wide.jpg into three depth layers (back wall, side walls, floor and foreground) with the gaps inpainted, save them in assets/img/, and make the room camera move them at different rates so station moves read as a dolly. Add 02 to intros/index.html and note what you did in docs/NOTES.md.

**Try a different opener**
> Make 03-sign-first.html: start on a tight shot of the "Cardboard" sign, tilt down to the door, then run the same door reveal. Same final frame as 01.

**Wire the TV**
> In the current best intro, when the visitor picks The screen, play assets/video/demo.mp4 mapped onto the TV in the render with a subtle screen glow. Fall back to a still if the video is missing.

**Put it in the real page**
> Create site/index.html from reference/cardboard-complex-landing.html with the hero replaced by intro 02 and the room. Keep every section below the hero untouched. The "Back to the room" button should also offer "Read more" which scrolls to the matching section.

**Render a video version**
> Scaffold a Remotion project in video/ that reproduces the door reveal from 01 with the same timing at 1920x1080, 30fps, and renders to video/out/door-reveal.mp4.

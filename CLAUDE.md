# Cardboard Complex intro

Read `docs/BRIEF.md` before doing anything. It has the station map, camera rules, door timing, and palette. This file covers how to work in the repo.

## Layout

```
assets/img/        cropped plates used by the intros (exterior-*.jpg, interior-wide.jpg)
assets/source/     Steve's originals, never edit
intros/            one self-contained HTML file per intro variation
intros/index.html  picker page that links every intro
reference/         the current live landing page, read-only reference for copy and tokens
docs/              brief, prompt ideas, notes
```

## Rules

- Every intro is a single HTML file in `intros/` with inline CSS and JS. Load GSAP from cdnjs. Reference images by relative path (`../assets/img/...`). No build step, so any file can be opened directly in a browser or dropped on Netlify.
- Name intros with a number and a slug: `01-door-reveal.html`, `02-door-reveal-parallax.html`. Never overwrite an existing intro to try an idea; copy it to a new number. Add every new intro to `intros/index.html`.
- Use the CSS custom properties from the brief for colors and the same three Google Fonts as the reference page. Do not introduce new type or a new palette.
- The door opening rectangle on the exterior plate is left 37.3%, right 61.3%, top 38.5%, bottom 84.9%. Keep these as CSS variables at the top of each intro so they can be tuned by eye.
- Every intro must: work at 390px wide, expose a Skip control, respect `prefers-reduced-motion`, and land on the same final frame (the idle room view) so the room navigation can be shared across intros.
- Motion should feel like a camera, not a slideshow. Use `power2.inOut` or `power3.inOut` for camera moves and never a linear ease for anything a viewer sees.
- After building or changing an intro, open it in a browser (or take a screenshot with Playwright if available) and check the door edge alignment before reporting done.
- Log what was tried and what did or did not work in `docs/NOTES.md`, a few lines per session. Future sessions read it.

## Writing style for anything user-facing

No em dashes in copy, code comments, or commit messages. Use commas, parentheses, or a period.

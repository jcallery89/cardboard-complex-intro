# Cardboard Complex intro

Landing page opener and room navigation for Cardboard Complex. Built as plain HTML files driven by GSAP so every intro can be opened directly, compared side by side, and dropped on any static host.

- `docs/BRIEF.md` is the creative brief. Read it first.
- `CLAUDE.md` tells Claude Code how to work in this repo.
- `docs/PROMPTS.md` has starter prompts.
- `intros/index.html` lists every intro.

## Run it locally

No build step. Open `intros/index.html` in a browser, or serve the folder so fonts and paths behave exactly as they will online:

```
npx serve .
```

Then visit `http://localhost:3000/intros/`.

## Work on it with Claude Code

```
cd cardboard-complex-intro
claude
```

Claude Code picks up `CLAUDE.md` on its own. Ask it to read `docs/BRIEF.md` if it seems to be guessing.

## Share with Steve

Fastest: drag the whole folder onto https://app.netlify.com/drop and send the link. Every intro is reachable at `/intros/`.

For a permanent link, run `git init && git add -A && git commit -m "Start"`, push to GitHub, and turn on GitHub Pages (Settings, Pages, deploy from `main`, root). Same paths.

## Source assets

`assets/source/` holds Steve's originals untouched. `assets/img/` holds the crops the intros actually use. Regenerate the crops with `scripts/split-mock.py` if the source changes.

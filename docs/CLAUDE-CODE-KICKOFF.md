# Claude Code kickoff

Two ways to start, same prompt either way:

- **Claude desktop app**: open the Code section, start a new session, choose `P:\Claude\Cardboard Complex\cardboard-complex-intro` as the project folder (this folder, not the parent), and paste the prompt below as the first message.
- **Terminal**: `cd` into that folder, run `claude`, paste the prompt.

Claude Code reads `CLAUDE.md` on its own; the prompt points it at the notes and gets the repo online before any new work starts.

Before you run it: the 1 GB mockup zip and the other archives at the top of the Cardboard Complex folder are outside the project and ignored by pattern, so they will not be committed. Git must be installed on this PC. Step 1 uses the GitHub CLI (`gh`) to create the repo; if you don't have it, create an empty private repo named `cardboard-complex-intro` on github.com first and replace the "create a private GitHub repo" line in step 1 with:

```
   - Add https://github.com/YOUR-USERNAME/cardboard-complex-intro.git as origin and push main. If the push asks for credentials, stop and tell me.
```

---

## The prompt

```
This is the Cardboard Complex intro project. Read CLAUDE.md, docs/BRIEF.md and docs/NOTES.md before doing anything, then work through the steps below in order and stop after each one to show me the result.

1. Put the project under version control and push it to GitHub.
   - git init on main if there is no .git yet.
   - A .gitignore is already in place; keep it as is. It ignores node_modules/, video/frames/, archives and PSDs. video/out/ (the MP4 and WebM renders, about 16 MB), assets/source/ and reference/ are all meant to be tracked. Before committing, run git status and confirm nothing over 50 MB is staged.
   - Commit everything as "Start: intros 01 to 03, type trials, wordmarks, video pipeline".
   - Create a private GitHub repo named cardboard-complex-intro under my account with gh, set it as origin, and push main.
   - Turn on GitHub Pages from the main branch root so intros/ is reachable at the Pages URL, and give me the URL for intros/index.html and docs/type-specimen.html so I can send them to Steve.

2. Make the repo runnable for someone who just cloned it.
   - Add a package.json with playwright and gsap as devDependencies and these scripts: "serve" (npx serve . or python -m http.server 8765), "render" (node scripts/render-video.js intros/02-walk-in-reveal.html 30), "wordmarks" (python3 scripts/make-wordmark.py node_modules/@fontsource assets/logo).
   - scripts/render-video.js currently expects a server on port 8765 and optional CHROME_PATH and GSAP_LOCAL env vars; document that in README.md under a "Render the video" heading. scripts/make-wordmark.py needs the @fontsource packages listed at the top of the file; add them to devDependencies too.
   - Update README.md so the run, render and share instructions match what is actually in the repo now (intros 01 to 03, docs/type-specimen.html, docs/PROMPT-PACK.md, assets/logo/).
   - Commit and push.

3. Fix the man with the box. In assets/img/exterior-door-closed.jpg the man carrying the box overlaps the left edge of the door opening, so he gets covered by the interior as soon as the door starts to open (visible in video/out/02-walk-in-reveal-landscape.mp4 around 3 to 4 seconds). Cut him out into assets/img/exterior-man.png with a transparent background (use rembg or an OpenCV grabCut with a hand-tuned rectangle, whichever is available; install what you need), inpaint the plate where he stood into assets/img/exterior-door-closed-clean.jpg, then in intros/02-walk-in-reveal.html layer him above the door so he stays in front of the opening and scales with the camera push. Re-render the video with npm run render, check frames at 3.0s and 3.6s, and commit.

4. Log what you did in docs/NOTES.md (newest entry at the top, a few lines) and push.

Rules that apply throughout: never overwrite an existing intro to try an idea, copy it to a new number and add it to intros/index.html. Use the palette and fonts from the brief until I tell you which type system won (docs/type-specimen.html has the three candidates; B is the current favorite). No em dashes anywhere, in copy, comments or commit messages.
```

---

## After that

Good follow-up prompts, one per session:

- "Apply type system B from docs/type-specimen.html to intros/01 to 03 and intros/index.html. Swap the Google Fonts link and the CSS font variables only, nothing else changes. Screenshot the room view before and after."
- "Add swipe navigation between stations on screens narrower than 700px in intros/03-video-intro.html, using the image-space station anchors that are already there. Left and right swipes move to the next and previous station in the order shelves, screen, counter, phone, vault. Test at 390x844 with Playwright."
- "Create site/index.html from reference/cardboard-complex-landing.html with the hero replaced by intros/03-video-intro.html and the room. Keep every section below the hero untouched. Each station's caption gets a Read more link that scrolls to its matching section."
- "Steve's regenerated plates are in assets/source/regen/ (see docs/PROMPT-PACK.md for the shot list). Swap them in for exterior-door-closed.jpg and interior-wide.jpg, re-measure the door rectangle and update the --door-* variables, re-render the video."

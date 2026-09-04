# Cardboard Complex: image regeneration prompt pack

Why this exists: Steve's current frames are good individually but do not agree with each other. The sign, the door, the posters, the people and even the building change from shot to shot, so any walk-in built from them reads as a slideshow, not one camera move. This pack regenerates the set as one continuous world. The 2x upscales in `assets/img/2x/` are a stopgap only; they sharpen, they do not fix continuity.

Works in Midjourney (v7), Flux (Kontext or Pro), Firefly, or Ideogram. Notes per tool are at the end.

## The rules that make the set hold together

1. Generate the **anchor** first (shot 5, the closed roll-up door). Every other shot references it. Do not move on until the anchor is right, because everything inherits from it.
2. Use the anchor as an image reference on every shot (Midjourney `--cref` for the storefront is not a person, so use `--sref` plus a style reference weight of 100 and the anchor as an image prompt; Flux Kontext takes it as the edit source; Firefly uses Structure + Style reference).
3. Same seed on every shot in a tool that supports it. Change only the camera phrase.
4. Lock these facts in every prompt, word for word:
   - red brick two-story warehouse, steel factory windows, a rusted riveted steel header beam above the door
   - one roll-up garage door, dark charcoal corrugated steel, centered under the beam
   - the sign reads "Cardboard" in tan cardboard letters with a stitched edge, mounted above the beam, and the "b" is a curled corrugated flap
   - a grey steel side door to the right with a small "TEAM MEMBERS ONLY" plate
   - late afternoon, low warm sun from camera left, long soft shadows, clear sky
   - photoreal 3D render, architectural visualization, 35mm lens, eye level, straight on
5. No people in the regenerated plates. People are what changed most between Steve's frames and they fight the camera move. If Steve wants them, add them as separate cutout layers later (the man with the box is already flagged in the brief).
6. Aspect ratio 2.36:1 (Midjourney `--ar 64:27`), then upscale to at least 4800 wide. Portrait crops for mobile are cut from these, never generated separately.
7. Negative prompt everywhere: text other than the sign, extra signs, banners, posters, awnings, cars, people, lens flare, HDR look, vignette, watermark.

## Shot list

The camera is one continuous dolly from across the street to inside the shop. Shots 1 to 5 are the exterior; 6 is the interior. Shots 2 to 4 are only needed if you want real parallax between them; a clean 1, 5 and 6 with the animated door already makes the whole video.

| # | Name | Camera phrase to append | Notes |
|---|---|---|---|
| 1 | street | "wide establishing shot from across the street, full building in frame, sidewalk and curb in the foreground, one young tree either side of the door" | Hold at 0.0s |
| 2 | mid-street | "medium wide, camera has crossed halfway over the street, top of the building cropped, sign fully in frame" | Optional |
| 3 | approaching | "medium shot from the sidewalk, sign and door fill the frame, beam edge to edge" | Optional |
| 4 | at the door | "tight on the door, the corrugated steel fills most of the frame, sign cropped at the top" | Optional |
| 5 | **anchor: door closed** | "medium shot, straight on, the sign, beam and full door in frame, warm light leaking under the door onto the sidewalk" | Replaces `exterior-door-closed.jpg`. Generate first |
| 6 | interior | "inside the shop looking in from the door, one point perspective" plus the interior description below | Replaces `interior-wide.jpg` |

Interior description for shot 6, keep it exact so the station map still works:

> a trading card shop interior, one point perspective from the doorway, polished concrete floor with two wood inlay stripes leading in, exposed black steel trusses and silver ducts with caged Edison bulbs, left wall is floor to ceiling wood shelving of card boxes and slabbed singles, back wall is a reclaimed wood panel with a large blank flat screen TV centered and warm backlight, framed jerseys and helmets either side, right side is a glass and wood display counter with a register, far right a green steel vault door with a small brass "COLLECTORS ONLY" plate and a red velvet rope on brass stanchions, warm tungsten light, photoreal 3D render

If the tool supports it, run shot 6 twice more with "the same room" and the camera phrases "pushed in toward the left shelving" and "pushed in toward the counter" so the station moves have real depth plates later. Not required for launch.

## Base prompt (paste, then append the camera phrase)

```
photoreal 3D architectural render of a red brick two-story warehouse storefront, steel factory windows, a rusted riveted steel header beam above a single centered roll-up garage door of dark charcoal corrugated steel, above the beam a sign reading "Cardboard" in tan cardboard letters with a stitched edge where the "b" is a curled corrugated flap, a grey steel side door to the right with a small "TEAM MEMBERS ONLY" plate, late afternoon low warm sun from camera left with long soft shadows, clear sky, 35mm lens, eye level, straight on, no people, [CAMERA PHRASE] --ar 64:27 --style raw --stylize 50 --seed 4471 --no text, banners, posters, awnings, cars, people, lens flare, watermark
```

Change `4471` to whatever seed produced your best anchor and keep it.

## The 3D logo

Steve's `logo.png` is 355 x 160, which is why it goes soft above thumbnail size. Regenerate it at poster size and keep the flat SVG wordmarks in `assets/logo/` for everything that has to be crisp (favicon, nav, print, embroidery).

Spec: 4000 x 1600 minimum, transparent background (or flat #1B1512 that you can key out), the word "CardBoard" as extruded letters cut from tan corrugated cardboard, stitched edges, the "b" as a flap folded back to show the corrugation, "Complex" below in a clean serif, "TRADING CARD COLLECTIBLES" as a thin wide caps line under that.

```
logo render, the word "CardBoard" in thick extruded letters cut from tan corrugated cardboard with visible flute edges and a stitched border, the "b" is a folded flap peeled back to show the corrugation, below it the word "Complex" in a heavy soft serif with a subtle bevel in warm ivory, below that "TRADING CARD COLLECTIBLES" in thin wide gold capitals, centered, front view, soft studio light from upper left, dark warm brown background #1B1512, product photography, ultra sharp, 8k --ar 5:2 --style raw --stylize 30 --no extra text, gradient background, glow, bokeh
```

Expect the model to misspell on the first tries. Ideogram and Flux hold text best; Midjourney needs a few rerolls or a vary-region pass on the word.

## Tool notes

- **Midjourney**: `--sref <anchor url> --sw 100` plus the anchor as an image prompt at `--iw 1.5` on every non-anchor shot. Use `--seed` and `--style raw`. Upscale with "Upscale (Subtle)".
- **Flux Kontext**: give the anchor as the source image and phrase each shot as an edit, for example "same building, same lighting, move the camera across the street for a wide establishing shot, remove all people". This is the most reliable way to keep continuity.
- **Firefly**: Structure reference = anchor at strength 60 to 80, Style reference = anchor at 50. Content type Photo.
- **Ideogram**: best for the sign text and the logo. Use Realistic, Magic Prompt off, and paste the anchor as a style reference.

## Hand back

Drop results in `assets/source/regen/` with the shot number in the name (`05-door-closed.png`). Run `scripts/split-mock.py` only if you regenerate the 4-up mock; otherwise the intros reference the plates directly and the door rectangle in `intros/*.html` (`--door-*` variables) will need one re-measure.

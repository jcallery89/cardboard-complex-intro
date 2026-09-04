# Cardboard Complex: Intro and Room Navigation Brief

## What this is

A landing page opener for Cardboard Complex, Steve's platform for card shop owners, collectors, and (later) trade show organizers. The page already exists (`reference/cardboard-complex-landing.html`). This project replaces its static hero with two connected pieces:

1. **The door reveal.** The shop's roll-up door opens and the camera moves through it into the store. This is the "intro." It runs once on load, takes about 3 seconds, and can be skipped.
2. **The room.** After the reveal, the visitor is standing inside the store. Each feature of the platform lives at a physical station in the room. Choosing a station glides the camera to it (never a hard cut) and shows that feature. This is the 2K Sports "Crib" idea applied to a card shop.

The rest of the existing page (waitlist, copy sections) stays below the room, reachable by scrolling or from a station.

## Source material

- `assets/img/exterior-door-closed.jpg` (1500 x 636). Brick storefront, "Cardboard" sign, roll-up door shut. Base plate for the exterior.
- `assets/img/exterior-door-40.jpg`, `-75.jpg`, `-100.jpg`. Steve's mock of the door at three open states. The interiors visible through the door are not consistent frame to frame, so do not use these as an animation sequence. Use them only as a reference for how Steve pictured it.
- `assets/img/interior-wide.jpg` (2400 x 1018). The store interior, shot straight on from the door. This is the room.

Door opening on the exterior plate (as a fraction of the image): left 0.373, right 0.613, top 0.385, bottom 0.849. The man carrying the box overlaps the left edge of the door; he is baked into the plate, so at some point he should be cut out as a separate foreground layer (see Open items).

## Station map

The interior render is already laid out as a menu. Each station below maps to a section that exists in the current landing page, so the copy is already written.

| Station | Where in the render | Page section it opens | What plays there |
|---|---|---|---|
| Shelves | Left wall, card boxes and singles | "Two doors. One shop." | Inventory listing for store owners; the shop's stock as one searchable database |
| Counter | Right side, glass display cases and register | "Live at the counter." | Scan a card, get a price, list it. The in-store moment |
| TV | Center wall, blank screen on the wood panel | "The AIssistants." | The screen is blank in the render on purpose. Play product UI or a short demo on it |
| Phone | Small tablet or phone on the counter (add as an overlay, not in the render) | "All on your phone." | Mobile app for collectors and sellers |
| Vault | Far right, steel door, "Collectors Only," velvet rope | Trade shows (coming soon) | Camera moves to the door, it stays shut, a plate reads "Opening soon." Nothing else |

The vault is the one station that is deliberately a dead end. Resist filling it.

## The camera

- One continuous shot. The camera never cuts. It glides between stations with an ease-in-out curve of 0.9 to 1.3 seconds depending on distance.
- Idle state is the wide view of the room, exactly the interior render, at rest.
- A station move is a translate plus a scale (roughly 1.6x to 2.2x) toward that station's anchor point, with the room's depth layers moving at different rates so the move reads as a dolly, not a zoom.
- Depth layers, from back to front: back wall (TV, wood panel, jerseys), side walls (shelves, counter, vault), floor, foreground props (nearest counter corner, rope stanchion). Until the render is split into layers, the whole image can move as one plane; it will still feel right at small parallax amounts.
- On mobile: swipe between stations instead of free navigation. Same camera moves, portrait crop.

## The door reveal, beat by beat

0.0s Exterior, door closed. Hold for a breath.
0.4s Door begins to roll up. The corrugated texture scrolls upward and a warm light spills out the bottom edge and onto the sidewalk.
0.4s to 2.2s Door rises. As it clears the halfway point, the camera starts a slow push in toward the opening.
2.2s to 3.0s Door is fully up. The camera continues through the opening; the exterior plate scales past the frame edges and the interior fills the viewport. The interior should land exactly on the idle room view so the handoff is invisible.
3.0s Room navigation is live. Station hotspots fade in.

A "Skip" control is visible from 0.0s. Returning visitors (localStorage flag or a `?skip` param) go straight to the room. Reduced-motion users get a cross-dissolve instead.

## Look and feel

Take the palette and type from the existing page so the room and the copy below it feel like one site:

- Ground `#1B1512`, panel `#26201B`, line `#3E352E`
- Text `#F3ECD8`, muted `#B5A996`, dim `#7E7264`
- Brick `#8F2C2C`, tan `#C89B62`, gold `#C9A227`, gold highlight `#E7C55A`, navy `#14213D`
- Display: Playfair Display. Labels: Oswald. Body: Lora.

Station labels should feel like the shop's own signage (the "Collectors Only" plate is the reference), not like software tooltips. Warm light from inside the store is the main visual motif; lean on it for the door spill, hotspot glow, and focus states.

## Deliverables

- `intros/` holds one HTML file per intro variation so they can be compared side by side. Each is self-contained (assets by relative path, GSAP from CDN).
- The chosen intro plus the room become the new hero in a copy of the reference page.
- Optional: a Remotion project that renders the door reveal to MP4 for Instagram and the pitch deck. Same beats, same timing.

## Open items

- Cut the man with the box out of the exterior plate as a foreground layer so he stays in front of the opening door.
- Split `interior-wide.jpg` into 3 or 4 depth layers with the gaps inpainted.
- Get a product screenshot or short screen recording from Steve for the TV.
- Decide whether the phone station is a real object in the room or an overlay UI.
- Confirm with Steve that trade shows stay "coming soon" at launch.

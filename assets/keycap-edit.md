# Keycap asset

- Source: `keycap.avif` (preserved unchanged).
- Initial edit: `keycap-forest.png`, resized to 640 pixels wide with transparency preserved.
- Current output: `keycaps-teng.png`, resized to 800 pixels wide with transparency preserved. Four matching keys in a 2 by 2 arrangement, with ivory T, E, N, and G top legends.
- Edit tool: built-in imagegen.
- Used by: `hero.svg`, `hero-mobile.svg`, and `keycaps.svg`.
- Rebuild the SVGs with `python scripts/build_assets.py`. The PNG is embedded so the artwork is self-contained.

## Initial recolor prompt

Use case: precise-object-edit. Edit target: the attached keycap image, converted losslessly from assets/keycap.avif. Recolor this exact single translucent orange mechanical keycap to the profile's forest green palette: primary resin #42634B, deep green shadows #233E31, restrained sage highlights #89947A and warm paper #F0EFE7 reflections. Preserve the exact silhouette, perspective, recessed wavy emblem, translucent resin material, internal structure, and lighting. Keep the entire single keycap visible, centered and nearly filling the canvas, with a genuinely transparent background. No extra objects, no text, no new symbols, no framing. Change only the colors. This will be placed on a warm paper #F0EFE7 background with muted brass #B39B59 accents.

## Four-key edit prompt

Use case: precise-object-edit. Input image: the existing translucent forest green resin keycap, the edit target and material reference. Create exactly FOUR matching keycaps in a compact 2 by 2 arrangement, all fully visible, with clear small gaps, viewed from a consistent elevated three-quarter camera angle so every top face and letter is clearly readable. Preserve the reference's rounded sculpted keycap shape, translucent forest green resin #42634B, deep green #233E31 shadows, sage highlights, subtle visible internal structure, realistic soft studio lighting. Replace the wave emblem entirely with a single large uppercase block sans-serif letter inset into the center of each keycap's TOP face in warm ivory #F0EFE7 for excellent readability. Exact letters and reading order: top-left T, top-right E, bottom-left N, bottom-right G. The letters must sit physically on the top surfaces with correct perspective, not float above them. Four keys spell TENG in reading order. No wave symbols, no other letters, no extra objects, no keyboard base, no text outside the keys. Transparent background with genuine alpha. Center the whole group in a nearly square canvas with a small transparent margin around every edge. Output one polished cutout of the four keycaps for placement on warm paper with brass accents.

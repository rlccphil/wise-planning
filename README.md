# Wise Hours (RLCC)

1. The RLCC logo is already in place (originals are in `brand/`). If you ever change it, replace the files in `brand/` and run `python3 make_assets.py`.
2. In `index.html`, replace `https://YOUR-USERNAME.github.io/wise-hours/` (appears in the og:url, og:image, and twitter:image tags) with your real GitHub Pages address.
3. Create a GitHub repository (e.g., `wise-hours`), upload everything in this folder, and turn on Settings > Pages > Deploy from branch > main > root.
4. Open the page on a phone and choose Add to Home Screen. After the first visit it also works offline.
5. When you edit the app, change `V` in `sw.js` (e.g., wise-hours-v2) so phones fetch the update.

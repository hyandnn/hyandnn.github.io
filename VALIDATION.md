# Second-version validation

Completed locally:

- Generated 12 static pages: homepage, four cases and 404 in two languages.
- JavaScript syntax checks and local page/asset references.
- Language metadata and paired links: switching preserves the current case.
- Public text and filenames checked for employer and internal-engine identifiers.
- Stereo sampling checked against forward field of view and depth limits.
- LiDAR ray checks: first-surface occlusion, no fabricated free-space returns, and changing target visibility.
- Climbing checks: immutable wall points, an upward-moving window, changing visible subsets, invertible local-to-template mapping and speed derived from the same trajectory.
- Dedicated cover compositions and all collision/climbing phase panels rendered and inspected at desktop and narrow widths.
- Actual app behavior checked with a DOM shim: English/Chinese controls, shared phase playback, scrubbing, replay, reduced-motion pause and saved language selection.
- Offline preview shell checked for navigation to the same case across languages.
- Exact pages packaged into the self-contained bilingual `preview.html`.

Live deployment and desktop browser verification (2026-10-03):

- GitHub Pages serves the website from the independent `hyandnn/hyandnn.github.io` repository, review branch `portfolio/merci-site`, root directory.
- Opened both homepages and all four case pages in both languages at the actual public address.
- Verified switching languages keeps the same case, and an explicit Chinese choice is retained when navigating to the English root URL.
- Verified Chinese font rendering and the visible language control in a live desktop browser at 1363 CSS pixels. No horizontal page overflow was observed in the inspected homepage and case layouts.
- Verified stereo play/pause and geometry toggle, LiDAR time scrubbing and track toggle, and the collision/climbing three-panel layout and shared time control.
- Climbing playback restarts from the end on user interaction; fixed wall geometry and changing frame subsets are also covered by source-level checks above.
- Site-origin error/warning log filtering returned no entries; extension-origin metadata messages are outside the website implementation.
- Captured the live Chinese homepage with its language switch visible.

Remaining QA scope:

- Narrow-width canvas compositions were rendered and inspected locally, but actual mobile-browser layout and accessibility/reduced-motion preferences have not been rechecked in this cloud browser session. `tools/check.mjs` is an optional full-browser suite and has not passed in the local environment.
- After the website PR is merged, switch the Pages publishing branch from `portfolio/merci-site` to `main`, keeping `/(root)`.

Source and canvas checks are distinguished from actual browser checks. Synthetic illustrations are not product recordings or benchmark evidence.

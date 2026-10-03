# Portfolio validation record

## System-level case studies (2026-10-03)

- Editorial/layout refinement: replaced model-observation wording with model outputs, made homepage summaries concrete, clarified the established LiDAR framework and named the collision-query stages and climbing-analysis outputs in the profile. Project context and results use system subjects; contribution labels retain ownership.
- Reduced repeated scope/result paragraphs while preserving all functional views and contribution cards. All six numbered sections now share a heading-above-content structure in both languages. Height illustrations label ground and upward height direction. These structure/source checks do not establish browser rendering.
- Generated all twelve paired pages and checked headings, local references, fragment targets, language metadata and same-case language links.
- Expanded homepage cards and case studies to cover system scope before individual contributions. The ground capability is separate from carpet recognition and supports plane-structure understanding, online calibration and point-cloud correction during bumpy motion.
- Added three grouped functional views and the complete climbing research pipeline, plus an independent LiDAR height-structure illustration. Company views regroup responsibilities rather than reproduce implementation order or module boundaries.
- Reviewed public copy for identifying employer/engine names, private code identifiers, unverified measurements and product-specific implementation details.
- JavaScript syntax, canvas scene checks and state/language regressions passed. Existing covers and interactive illustrations were retained.
- Responsive CSS stacks functional groups, contribution cards, research branches and height views on narrow screens. Browser rendering of this revision has not been verified: the available cloud browser rejects local-file previews. The offline HTML preview is available for review; the optional full-browser suite was not run. Earlier live-browser results below apply to the previous deployed revision.
- Production publishing remains `main` → `/(root)`. These changes are proposed in a review branch, not deployed.

## Earlier versions

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

- Narrow browser layouts were subsequently checked through actual site pages in 390px and 320px iframe viewports (see the repair verification below). Physical devices, Safari and assistive-technology behavior remain outside this session. `tools/check.mjs` is an optional full-browser suite and has not passed in the local environment.
- The earlier website PR was merged and the Pages publishing branch was subsequently switched to `main`, keeping `/(root)`.

Source and canvas checks are distinguished from actual browser checks. Synthetic illustrations are not product recordings or benchmark evidence.

## Language and editorial refinement (2026-10-03)

- Explicit English/Chinese URLs now take precedence over the saved preference. Only `/` uses a valid saved choice; `/index.html` remains explicit English. Root redirects and manual language switches preserve URL fragments.
- Behavior regressions cover all twelve explicit routes with an opposite saved preference, both valid root preferences, no preference, invalid preference, fragment preservation and the existing playback checks.
- All twelve generated pages passed heading and local-reference checks. Chinese pages contain neither the old climbing-hold term nor the mixed-language LiDAR project title.
- Live verification: an English choice followed by a direct Chinese climbing-case URL stayed Chinese; a Chinese choice followed by a direct English stereo-case URL stayed English. The default root honored both preferences. Same-case switching and `#work` preservation passed.
- The updated Chinese homepage was visually inspected at desktop width; the title fits its two-line layout without horizontal page overflow.
- Outcomes in both languages now state the concrete added representation, cross-frame state, selectable query options or shared wall reference. No unverified metrics or publication links were added.

## QA mock, typography and cover repair (2026-10-03)

- Reproduced and fixed the canvas script crash: its mock window now includes location and a consistent parent window. JavaScript syntax, canvas geometry/scene checks and state/language regression checks passed.
- Let’s contains no extra space. In the cloud browser, the curly apostrophe occupied about 43px at the desktop heading size. Adding Helvetica Neue / Arial before Chinese font fallbacks reduced the same glyph to 9px while preserving the typographic apostrophe. The repaired heading was visually inspected.
- LiDAR cover now enlarges the same target returns and track in a local inset. Climbing cover enlarges the local frame, pose and its correspondences to the fixed wall template. Native canvas covers were rendered and inspected at narrow and desktop widths.
- CSS and JavaScript references include content hashes, preventing previous versions in browser caches from masking a deployed update. All twelve generated routes and local references passed; the offline preview still embeds assets without remote runtime dependencies.
- Live narrow-layout checks used tools/responsive-review.html, which loads actual site pages in 390px and 320px iframe browser viewports. Both homepages and all eight case pages passed at both widths (20 layouts), with no horizontal document overflow. Collision/climbing panels used a single column. Climbing scrubbing, playback/pause and same-case language switching passed at 390px.
- This is live browser layout verification at phone-sized widths, not a physical-phone or Safari test.

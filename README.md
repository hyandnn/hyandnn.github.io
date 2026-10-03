# Merci portfolio

A dependency-free static portfolio for GitHub Pages, with full English and Simplified Chinese versions. Public project descriptions and independently created synthetic demonstrations. No analytics or third-party runtime services.

## Content and development

- `index.html` and `projects/*.html`: English homepage and four case studies.
- `zh/index.html` and `zh/projects/*.html`: equivalent Chinese pages.
- `tools/content.py`: bilingual interface and homepage copy.
- `tools/case_content.py`: paired case studies, functional views and contribution scope.
- `tools/build.py`: static HTML generation.
- `assets/app.js`: independent interactive diagrams and four dedicated cover compositions.
- `assets/style.css`: responsive visual system and system-font stack.
- `tools/preview.py`: self-contained offline preview with navigation between both language versions.

Run `python3 tools/build.py`, then `python3 tools/preview.py` after editing. Generated pages are checked in, so deployment needs no package installation or build service. CSS and JavaScript are edited directly.

This website lives at the root of the public `hyandnn/hyandnn.github.io` repository. GitHub Pages publishes `main` → `/(root)`. Review changes on their pull-request branch or generate the offline preview before merging. The `handoff` folder is local review material and is excluded from this repository.

## Interaction and accessibility

The EN / 中文 switch preserves the current case and URL fragment, and remembers explicit choices when browser storage is available. Explicit language-specific URLs take priority over saved preferences. Only the default root entrance (`/`) uses a saved language preference; `/index.html` is an explicit English homepage and `/zh/index.html` an explicit Chinese homepage. Ordinary navigation works without JavaScript. English and Chinese page metadata are generated independently. Both languages use system fonts, including SF / Segoe UI, Helvetica Neue / Arial for Western glyphs, and Chinese sans-serif fallbacks. The Western fallbacks precede Chinese families so English punctuation retains proportional spacing.

All four case illustrations support playback and time scrubbing, starting paused. Stereo and LiDAR also have layer switches. The collision and climbing phase panels share one clock; desktop layouts are horizontal, narrow layouts vertical. At the end of a scan, replay restarts on request. Reduced-motion preferences are respected. Navigation and controls support keyboard operation.

For narrow-layout review, open `tools/responsive-review.html` on the published site. It loads the actual homepage and cases in 390px and 320px iframe viewports, with a page selector. This checks browser layout and interactions at those widths; it is not a physical-device test.

## Diagram model

Functional views are readable HTML, adapting from grouped columns to a single column on narrow screens. Company-project views regroup capabilities by responsibility; they do not reproduce internal module boundaries, processing order or implementation. Contribution cards distinguish shared design, capability development and led integration. The research pipeline connects wall-reference and athlete observations to spatial mapping and movement analysis. The LiDAR height illustration compares plan-view and vertical structure using independent toy geometry.

All six numbered case sections use the same heading-above-content layout. Prose stays at a readable line length; functional groups and illustrations can use the full content width. The height study labels its ground reference and upward height direction.

The climbing wall holds have immutable coordinates. An upward-moving camera window determines the visible subset and local frame coordinates. Correspondences link those same local points to fixed template points. The pose is projected from the same wall reference, and normalized speed is derived from the same synthetic trajectory.

The diagrams contain illustrative geometry and synthetic time. They do not reproduce product implementations or provide performance measurements. See `VALIDATION.md` for completed checks and remaining browser/deployment verification.

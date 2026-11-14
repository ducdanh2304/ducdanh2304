# Signal Atlas V2

The profile uses a dark navy editorial system with an amber signal line, teal data paths and modern sans-serif typography. The hero establishes the identity; a logo-led toolkit and three compact project covers carry the portfolio. Each cover has a distinct composition and one dominant result.

## Build and maintenance

- Run `python build_v2.py` to regenerate the SVG assets. `build_cards.py` contains the three project covers. Each SVG is self-contained and has a static state plus optional motion that respects reduced-motion preferences.
- The README references static assets through immutable GitHub raw URLs because repository-relative SVG references did not display reliably on the profile page.
- Technology icons come from [Devicon](https://github.com/devicons/devicon) through jsDelivr. Their labels remain visible if an icon is unavailable.
- The profile no longer displays the public activity chart; GitHub's contribution view remains available on the profile page.
- Earlier artwork is retained as source history and can be removed in a later cleanup.

## Evidence

- [LexViet repository](https://github.com/ducdanh2304/lexviet-retrieval)
- [3LC detection repository](https://github.com/ducdanh2304/3lc-vehicle-detection-1st-place)
- [Springer publication](https://link.springer.com/chapter/10.1007/978-981-92-2597-2_36)
- [3LC Kaggle competition](https://www.kaggle.com/competitions/3-lc-multi-vehicle-detection-challenge)

The research artwork links to the publication because no public code repository for that project was verified. LexViet's 0.9428 is labeled as a competition score, since the private evaluator does not define it as Recall@5. The public repository contains a synthetic API demo alongside research artifacts; the cover represents the competition system described in its documentation.

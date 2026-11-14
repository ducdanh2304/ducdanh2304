# Signal Atlas — editorial system

The existing hero remains the entry point. The body now follows a Swiss editorial rhythm: large sans-serif headings, generous breathing room, warm paper and muted blue surfaces, and one strong visual idea per project. The project artwork communicates the subject before the metrics.

## Project art

- **LexViet:** a query fans out into legal passages and a selected result. The 0.9428 value is labeled as a competition score, matching the public repository's evaluation caveat.
- **Multi-Vehicle Detection:** a road scene with detection boxes and one dashed missing-label candidate. Predictions surface candidates; human review accepts corrections.
- **Multimodal Video Retrieval:** video frames connect to visual, text, OCR and speech representations. The artwork links to the actual Springer publication.

Each project has a 900 × 270 desktop illustration and a 480 × 390 mobile composition. README `picture` elements select the mobile art at narrow viewport widths. The images have descriptive alt text and are wrapped in direct links. Motion is limited to subtle retrieval traces and stops when reduced motion is requested.

## Toolkit

The README uses recognisable Devicon marks with their names, grouped into Programming, Machine Learning, Computer Vision & NLP, Data & Engineering, and Deployment. Methods without a suitable logo remain text, separate from software brands.

## Sources and maintenance

- [LexViet](https://github.com/ducdanh2304/lexviet-retrieval)
- [3LC Multi-Vehicle Detection](https://github.com/ducdanh2304/3lc-vehicle-detection-1st-place)
- [Springer publication](https://link.springer.com/chapter/10.1007/978-981-92-2597-2_36)
- [Devicon](https://github.com/devicons/devicon)

Run `python build_v2.py` to regenerate the hero, navigation and project art; `build_cards.py` contains the project compositions. Static artwork is referenced through immutable raw GitHub URLs because repository-relative SVGs did not display reliably on this profile. Old assets remain in the repository for history but are not rendered by the README.

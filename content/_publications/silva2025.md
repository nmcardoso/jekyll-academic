---
title: "Dummy Publication 03: Markdown and Components"
venue: Archive of Dummy Results
authors: |
  Bruno R Silva, Diego M Rocha, Elisa F Souza and Felipe G Lima
year: 2025
pdf: https://example.org/dummy-publication-03.pdf
ads: https://ui.adsabs.harvard.edu/abs/2026dummy0003/abstract
files:
  - resource: Main Catalog
    name: dummy_publication_03_catalog.csv
    url: https://example.org/datasets/dummy_publication_03_catalog.csv
  - resource: Supplement
    name: dummy_publication_03_supplement.pdf
    url: https://example.org/datasets/dummy_publication_03_supplement.pdf
abstract: >
  This synthetic publication emphasizes compatibility between markdown structures and
  embedded HTML components in the publication page.
bibtex: |
  @article{dummy2026c,
    author = {Silva, Bruno R and Rocha, Diego M and Souza, Elisa F and Lima, Felipe G},
    title = {Dummy Publication 03: Markdown and Components},
    journal = {Archive of Dummy Results},
    year = {2026},
    pages = {21--30},
    doi = {10.0000/dummy.2026.003}
  }
---

Introductory text with **bold text**, *italic text*, and `inline code`.

## Heading Test

### Table Test

| Component | Expected |
| --- | --- |
| Headings | Proper scale |
| Table | Aligned columns |
| Code | Syntax highlight |

<figure class="text-center">
  <img src="https://picsum.photos/seed/dummy-pub-03/820/320" alt="Dummy publication figure 03" class="img-thumbnail" />
  <figcaption class="small">Figure 3. Figure and caption spacing verification.</figcaption>
</figure>

```bash
echo "running publication ui test"
bundle exec jekyll build
```

```mermaid
classDiagram
  class Publication {
    +title
    +journal
    +render()
  }
```

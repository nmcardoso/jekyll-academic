---
title: "Dummy Publication 02: Layout Stress Scenario"
venue: Proceedings of Synthetic Experiments
authors: |
  Elisa F Souza, Felipe G Lima, Gabriela V Castro and Ana M Ferreira
year: 2025
pdf: https://example.org/dummy-publication-02.pdf
ads: https://ui.adsabs.harvard.edu/abs/2026dummy0002/abstract
files:
  - resource: Table A
    name: dummy_publication_02_tableA.parquet
    url: https://example.org/datasets/dummy_publication_02_tableA.parquet
  - resource: Script
    name: dummy_publication_02_analysis.py
    url: https://example.org/code/dummy_publication_02_analysis.py
abstract: >
  A compact synthetic publication used to stress typography, table rendering,
  and syntax-highlighted code blocks in the publication template.
bibtex: |
  @article{dummy2026b,
    author = {Souza, Elisa F and Lima, Felipe G and Castro, Gabriela V and Ferreira, Ana M},
    title = {Dummy Publication 02: Layout Stress Scenario},
    journal = {Proceedings of Synthetic Experiments},
    year = {2026},
    pages = {11--20},
    doi = {10.0000/dummy.2026.002}
  }
---

Short paragraph to validate default publication text styles.

## Visual Elements

### Data Table

| Metric | Run A | Run B |
| --- | ---: | ---: |
| Precision | 0.91 | 0.93 |
| Recall | 0.90 | 0.92 |
| F1-score | 0.90 | 0.92 |

<figure>
  <img src="https://picsum.photos/seed/dummy-pub-02/900/340" alt="Dummy publication figure 02" class="w-100 rounded" />
  <figcaption>Figure 2. Wide placeholder image for responsive behavior checks.</figcaption>
</figure>

```javascript
const metrics = [0.91, 0.90, 0.92];
const mean = metrics.reduce((a, b) => a + b, 0) / metrics.length;
console.log(mean.toFixed(3));
```

```mermaid
sequenceDiagram
  participant R as Researcher
  participant S as Site
  R->>S: Open publication page
  S-->>R: Render metadata + content
```

---
title: "Dummy Publication 04: Complete Frontmatter Example"
venue: apj
authors: |
  Carla P Pereira, Gabriela V Castro, Ana M Ferreira and Felipe G Lima
date: 2026-12-31
status: submitted
pdf: https://example.org/dummy-publication-04.pdf
ads: https://ui.adsabs.harvard.edu/abs/2026dummy0004/abstract
files:
  - resource: Derived Table
    name: dummy_publication_04_table.tsv
    url: https://example.org/datasets/dummy_publication_04_table.tsv
  - resource: Notebook
    name: dummy_publication_04_notebook.ipynb
    url: https://example.org/code/dummy_publication_04_notebook.ipynb
abstract: >
  A fully populated dummy publication meant to verify metadata rendering in cards,
  archives, and detail pages while also testing mixed markdown content.
bibtex: |
  @article{dummy2026d,
    author = {Pereira, Carla P and Castro, Gabriela V and Ferreira, Ana M and Lima, Felipe G},
    title = {Dummy Publication 04: Complete Frontmatter Example},
    journal = {Synthetic Astronomy Notes},
    year = {2026},
    pages = {31--40},
    doi = {10.0000/dummy.2026.004}
  }
---

This paragraph validates baseline body typography for publication entries.

## Results Snapshot

### Metrics Table

| Case | Value |
| --- | ---: |
| Signal-to-noise | 32.4 |
| Throughput | 1.87 |
| Error rate | 0.03 |

<figure>
  <img src="https://picsum.photos/seed/dummy-pub-04/880/360" alt="Dummy publication figure 04" class="img-fluid rounded" />
  <figcaption>Figure 4. Placeholder chart panel for visual QA.</figcaption>
</figure>

```ruby
def normalize(x, min, max)
  (x - min) / (max - min)
end

puts normalize(12, 0, 24)
```

```mermaid
gantt
  title Dummy Experiment Timeline
  dateFormat  YYYY-MM-DD
  section Pipeline
  Collect data     :done,    a1, 2026-03-01,2026-03-05
  Process data     :active,  a2, 2026-03-06,2026-03-11
  Validate outputs :         a3, 2026-03-12,2026-03-16
```

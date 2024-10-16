# TP Report

## Distance Matrix of Jaccard Indices (Original)

|                 | **(1) GCA_000013265.1** | **(2) GCA_000005845.2** | **(3) GCA_000069965.1** | **(4) GCA_000008865.2** | **(5) GCA_030271835.1** |
|:---------------:|:-----------------------:|:-----------------------:|:-----------------------:|:-----------------------:|:-----------------------:|
| **(1) GCA_000013265.1** | **1.0000**              | 0.3410                  | 0.0024                  | 0.3071                  | 0.0024                  |
| **(2) GCA_000005845.2** | 0.3410                  | **1.0000**              | 0.0026                  | 0.4365                  | 0.0026                  |
| **(3) GCA_000069965.1** | 0.0024                  | 0.0026                  | **1.0000**              | 0.0023                  | 0.0311                  |
| **(4) GCA_000008865.2** | 0.3071                  | 0.4365                  | 0.0023                  | **1.0000**              | 0.0023                  |
| **(5) GCA_030271835.1** | 0.0024                  | 0.0026                  | 0.0311                  | 0.0023                  | **1.0000**              |

## Distance Matrix of Jaccard Indices (Using Sketches)

|                 | **(1) GCA_000013265.1** | **(2) GCA_000005845.2** | **(3) GCA_000069965.1** | **(4) GCA_000008865.2** | **(5) GCA_030271835.1** |
|:---------------:|:-----------------------:|:-----------------------:|:-----------------------:|:-----------------------:|:-----------------------:|
| **(1) GCA_000013265.1** | **1.0000**              | 0.3207                  | 0.0021                  | 0.2884                  | 0.0021                  |
| **(2) GCA_000005845.2** | 0.3207                  | **1.0000**              | 0.0032                  | 0.3864                  | 0.0029                  |
| **(3) GCA_000069965.1** | 0.0021                  | 0.0032                  | **1.0000**              | 0.0017                  | 0.0300                  |
| **(4) GCA_000008865.2** | 0.2884                  | 0.3864                  | 0.0017                  | **1.0000**              | 0.0018                  |
| **(5) GCA_030271835.1** | 0.0021                  | 0.0029                  | 0.0300                  | 0.0018                  | **1.0000**              |

## Observations

The results show varying levels of genetic similarity between the samples. For example, **GCA_000013265.1** and **GCA_000008865.2** exhibit moderate similarity with a Jaccard index of 0.3071, suggesting they may share some conserved genetic regions, possibly due to evolutionary relationships. In contrast, pairs such as **GCA_000008865.2** and **GCA_000069965.1** have very low similarity (0.0023), indicating significant genetic divergence, likely reflecting distant evolutionary backgrounds or substantial genome structural differences.

The relatively high distance observed between **GCA_000008865.2** and **GCA_000005845.2** (0.4365) suggests substantial genetic variation, which could be due to different evolutionary adaptations or genome content. The choice of k-mers (`k = 21`) helps to capture specific conserved regions, as longer k-mers reduce the chances of random matches and highlight more significant similarities.

Using sketches (`s = 10,000`) provides an efficient approximation of Jaccard similarity, enabling scalable analysis of large genomic datasets with slight deviations from exact calculations. This approach allows for faster comparisons while still maintaining a reasonable level of accuracy in estimating genetic relationships.

## Description of Methods

The Jaccard similarity was computed using k-mers (`k = 21`). Each sequence from the `.fasta` files was processed to generate k-mers. Two methods were used:
1. **Exact Method**: The Jaccard similarity was calculated based on the intersection and union of all k-mers.
2. **Sketching Method**: The sequences were represented using sketches (`s = 10,000`) to reduce memory usage and computational cost. The approximate Jaccard similarity was then computed based on these sketches. This approach provides a balance between computational efficiency and the accuracy of similarity estimation.


by Md Imran Hossain
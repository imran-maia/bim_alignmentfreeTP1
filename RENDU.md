# TP Report

## Distance Matrix of Jaccard Indices

|               | GCA_000013265.1 | GCA_000008865.2 | GCA_000069965.1 | GCA_030271835.1 | GCA_000005845.2 |
|---------------|-----------------|-----------------|-----------------|-----------------|-----------------|
| **GCA_000013265.1** | 0.0               | 0.3048            | 0.0008            | 0.0008            | 0.3360          |
| **GCA_000008865.2** | 0.3048            | 0.0               | 0.0008            | 0.0008            | 0.4460          |
| **GCA_000069965.1** | 0.0008            | 0.0008            | 0.0               | 0.0262            | 0.0009          |
| **GCA_030271835.1** | 0.0008            | 0.0008            | 0.0262            | 0.0               | 0.0009          |
| **GCA_000005845.2** | 0.3360            | 0.4460            | 0.0009            | 0.0009            | 0.0             |

## Comment on Matrix

The distance matrix shows that:

- Samples like **GCA_000013265.1** and **GCA_000008865.2** have a moderate distance (0.3048), indicating moderate similarity.
- Some pairs, such as **GCA_000008865.2** and **GCA_030271835.1**, show very small distances (0.0008), indicating they are almost identical.
- **GCA_000008865.2** and **GCA_000005845.2** have a larger distance (0.4460), suggesting less similarity.

## Description of Methods

The Jaccard similarity was computed using k-mers (with `k=21`). For each pair of samples, k-mers were generated, and the Jaccard similarity was calculated based on the intersection and union of these k-mers. The similarity was then converted into a distance using the formula:


Distance = 1 - Jaccard Similarity


The matrix above represents these distances.

Md Imran Hossain

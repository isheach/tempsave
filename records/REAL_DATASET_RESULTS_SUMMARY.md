# Real-Dataset Benchmark Summary

## Scope

The completed fixed runner processed **634/634 datasets** across multiple collections. The generic benchmark lacks a physical exogenous input for most series, so it uses an automatically selected autoregressive/VAR-style one-step predictor. This benchmark tests the detection frameworks on heterogeneous time series; it does **not** directly validate continuous-time transfer-function identification.

Collections include KDD-TSAD, GutenTAG, NAB, NASA-SMAP, NASA-MSL, NormA, TODS-synthetic, MGAB, CalIt2, and Dodgers.

## F1 convention issue

The workbook contains blank/NaN F1 values when `TP=0` and both Precision and Recall are zero, because the direct formula becomes `0/0`.

For datasets that contain true outliers, the conventional classification treatment is to report F1=0 in this zero-detection case. Normal-only datasets should be evaluated separately with FPR/specificity rather than forcing an F1 value.

## Corrected macro means over 625 anomalous datasets

| Metric | Downsampling | Patch |
|---|---:|---:|
| Precision | 0.26075 | 0.20417 |
| Recall | 0.28282 | 0.21712 |
| Specificity | 0.94448 | 0.93439 |
| F1 | 0.18887 | 0.13924 |
| Accuracy | 0.91750 | 0.90569 |
| Balanced Accuracy | 0.61365 | 0.57576 |
| MCC | 0.18383 | 0.12573 |

Paired corrected F1 across the 625 anomalous datasets: Downsampling wins 342, Patch wins 245, ties 38. The mean paired difference (Downsampling - Patch) is about 0.0496.

## Interpretation

The two methods exhibit different detection characteristics. Downsampling provides stronger overall robustness across heterogeneous sequences, particularly for extended deviations, whereas Patch is advantageous for several localized and pointwise outlier patterns.

A useful observed limitation is that Patch can degrade on long contiguous abnormal segments because a local robust polynomial Patch can begin to absorb an extended abnormal region as local trend. On TODS-style pointwise/contextual patterns, Patch can be stronger.

Do not publish one unqualified 634-dataset grand-average table without explicitly defining the F1 convention and separating the 9 normal-only datasets.

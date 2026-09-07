# Synthetic Experiment Summary

System: `G(s)=1/(s^2+2s+1)`; `T_s=0.01 s`; 500 samples; unit-step input; 100 experiments per condition.

Outlier counts: 5, 10, 15. Amplitude multipliers: 0.25, 0.5, 1, 2, 4.

## Aggregated verified results used in the manuscript work

### Downsampling

| Outliers | Mean TP | Mean TN | Mean FP | Mean FN | Precision | Recall | F1 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5.00 | 494.59 | 0.41 | 0.00 | 0.9242 | 1.0000 | 0.9606 |
| 10 | 10.00 | 488.45 | 1.55 | 0.00 | 0.8658 | 1.0000 | 0.9281 |
| 15 | 15.00 | 483.95 | 1.05 | 0.00 | 0.9346 | 1.0000 | 0.9662 |

### Patch

| Outliers / condition | Mean TP | Mean TN | Mean FP | Mean FN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 5 | 5.00 | 494.96 | 0.04 | 0.00 | 0.9921 | 1.0000 | 0.9960 |
| 10, multipliers 0.25/0.5/1 | 10.00 | 489.98 | 0.02 | 0.00 | 0.9980 | 1.0000 | 0.9990 |
| 10, multipliers 2/4 | 10.00 | 489.96 | 0.04 | 0.00 | 0.9960 | 1.0000 | 0.9980 |
| 15 | 14.99 | 484.78 | 0.22 | 0.01 | 0.9855 | 0.9993 | 0.9924 |

`Exact Match Rate` was deliberately removed from the manuscript-facing metric set. Before changing any numeric table, regenerate or verify the values from the current MATLAB implementation.

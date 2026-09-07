# Current MATLAB code

This directory contains the current MATLAB implementations used as the code-side reference for the paper handoff.

## Files

- `current/all_in_one_outlier_experiment_500_verified_baseline.m.gz` — current synthetic continuous-time implementation; primary authority for the paper's Downsampling and Patch method logic.
- `current/run_real_dataset_two_methods_fixed.m.gz` — generic real-dataset benchmark adaptation using autoregressive/VAR-style prediction when physical input is unavailable.
- `restore_current_code.py` — restores the exact `.m` files and verifies SHA-256.

Restore with:

```bash
python code/restore_current_code.py
```

Expected restored SHA-256:

- `all_in_one_outlier_experiment_500_verified_baseline.m`: `b29434e9cbe537800395c5e03fab85a03811ca6af05ea9031c47f707b14deb06`
- `run_real_dataset_two_methods_fixed.m`: `1a0dbccfb3317f1a961e039df63ce8c938ace59406e5bcc0aaa36ed9b80afa51`

Do not infer the continuous-time identification formulation from the real-data runner. The synthetic implementation is the primary method reference for the manuscript.

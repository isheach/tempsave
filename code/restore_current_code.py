from pathlib import Path
import gzip
import hashlib
import shutil
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "current"
OUT = ROOT / "restored"
OUT.mkdir(exist_ok=True)

EXPECTED = {
    "all_in_one_outlier_experiment_500_verified_baseline.m": "b29434e9cbe537800395c5e03fab85a03811ca6af05ea9031c47f707b14deb06",
    "run_real_dataset_two_methods_fixed.m": "1a0dbccfb3317f1a961e039df63ce8c938ace59406e5bcc0aaa36ed9b80afa51",
}

ok = True
for name, expected in EXPECTED.items():
    src = SRC / f"{name}.gz"
    dst = OUT / name
    if not src.exists():
        print(f"MISSING: {src}")
        ok = False
        continue
    with gzip.open(src, "rb") as fi, dst.open("wb") as fo:
        shutil.copyfileobj(fi, fo)
    actual = hashlib.sha256(dst.read_bytes()).hexdigest()
    status = "OK" if actual == expected else "HASH MISMATCH"
    print(f"{status}: {dst}  sha256={actual}")
    ok &= actual == expected

sys.exit(0 if ok else 1)

"""Format batting stats for display."""
import pandas as pd


def fmt_leading_dot(precision=3, zero_str='.000'):
    "Format floats to leave off leading zeros."
    def _fmt(x):
        if pd.isna(x):
            return ""
        if x == 0:
            return zero_str
        s = f'{x:.{precision}f}'
        if s.startswith("0."):
            return s[1:]
        if s.startswith("-0."):
            return '-' + s[2:]
        return s
    return _fmt

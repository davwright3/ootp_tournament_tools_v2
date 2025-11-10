"""
Script to ensure an entry is set to a float, with default entry if it
 is invalid.
 """
import tkinter as tk
import math


def coerce_float(sv: tk.StringVar, default=1.0) -> float:
    """Return a float or default if invalid entry."""
    try:
        s = sv.get()
        if s is None:
            return default
        s = s.strip()
        if not s:
            return default
        v = float(s)
        if math.isnan(v) or math.isinf(v):
            return default
        return v
    except Exception:
        return default

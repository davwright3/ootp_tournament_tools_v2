import pytest
import tkinter as tk
from utils.stats_utils import coerce_float as mod

root = tk.Tk()

def test_coerce_float_returns_correct_float_valid_entry():
    num = tk.StringVar(value='2.3')
    result = mod.coerce_float(num, default=1.0)
    assert result == 2.3

def test_coerce_float_returns_default_invalid_entry():
    num = tk.StringVar(value='hello')
    result = mod.coerce_float(num, default=1.0)
    assert result is 1.0

def test_coerce_float_returns_default_null_entry():
    num = tk.StringVar(value=None)
    result = mod.coerce_float(num, default=1.0)
    assert result is 1.0

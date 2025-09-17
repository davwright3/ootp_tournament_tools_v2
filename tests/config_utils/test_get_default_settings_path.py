"""Test that the default settings path works across environments."""
import sys
from pathlib import Path
import importlib

import utils.config_utils.get_default_settings_path as mod

def test_non_frozen_uses_module_dir(monkeypatch):
    """
    When not frozen (running in dev environment), the path should be:
        dirname(__file__)/'..'/'settings_default.ini'
    """
    # Ensure program is not frozen
    monkeypatch.setattr(sys, 'frozen', False, raising=False)

    out = Path(mod.get_default_settings_path()).resolve()

    expected = (Path(mod.__file__).resolve().parent/".."/"settings_default.ini").resolve()
    assert out == expected
    assert out.is_absolute()
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

def test_frozen_uses_meipass(monkeypatch, tmp_path):
    """
    When frozen (running in PyInstaller environment),
    the path should be sys._MEIPASS / 'settings_default.ini'
    """
    bundle_root = tmp_path / 'bundle'
    bundle_root.mkdir()

    monkeypatch.setattr(sys, 'frozen', True, raising=False)
    monkeypatch.setattr(sys, '_MEIPASS', str(bundle_root), raising=False)

    out = Path(mod.get_default_settings_path())
    assert out == bundle_root / 'settings_default.ini'
    assert out.is_absolute()
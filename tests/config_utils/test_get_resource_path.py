"""
Test that the resource path which checks for usable assets
is following the right path in development and PyInstaller environments."""
import os
import sys
from pathlib import Path
import pytest
from utils.config_utils import get_resource_path as mod


@pytest.mark.parametrize('rel', ['data/file.txt', 'images/logo.png', ""])
@pytest.mark.parametrize('use_frozen', [False, True])
def test_non_frozen_uses_module_path(monkeypatch, tmp_path, rel, use_frozen):
    """
    Tests that non-frozen (development environment) path is set to module path.
    """
    if use_frozen:
        bundle_root = tmp_path / 'bundle_root'
        bundle_root.mkdir()
        monkeypatch.setattr(sys, 'frozen', True, raising=False)
        monkeypatch.setattr(sys, '_MEIPASS', str(bundle_root), raising=False)

        out = Path(mod.get_resource_path(rel))
        expected = (bundle_root / rel).resolve()

        assert out == expected
        assert out.is_absolute()
    else:
        monkeypatch.setattr(sys, 'frozen', False, raising=False)

        module_dir = Path(mod.__file__).resolve().parent
        dev_base = (module_dir / '..' / '..'/'..').resolve()

        out = Path(mod.get_resource_path(rel))
        expected = (dev_base / rel).resolve()
        assert out == expected
        assert out.is_absolute()


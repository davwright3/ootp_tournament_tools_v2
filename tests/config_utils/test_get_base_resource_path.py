"""
Tests utility to get the base resource path depending on
development or pyinstaller run environment.
"""
import os
import sys
from pathlib import Path
import types
from utils.config_utils.get_base_resource_path import get_base_resource_path
import importlib
import platform
import pytest

def test_uses_meipass_when_present(tmp_path, monkeypatch, caplog):
    # Arrange the path
    import utils.config_utils.get_base_resource_path as mod
    importlib.reload(mod)

    fake_bundle_root = tmp_path / "bundle"
    fake_bundle_root.mkdir()
    stub_sys = types.SimpleNamespace(frozen=True, _MEIPASS=str(fake_bundle_root))

    monkeypatch.setattr(mod, 'sys', stub_sys, raising=False)

    rel = os.path.join('images', 'logo.png')
    with caplog.at_level('INFO'):
        out = mod.get_base_resource_path(rel)

    assert Path(out) == fake_bundle_root / rel
    assert any(str(fake_bundle_root / rel) in r.message for r in caplog.records)


def test_uses_cwd_when_no_meipass(tmp_path, monkeypatch, caplog):
    rel = os.path.join('data', 'file.txt')
    monkeypatch.chdir(tmp_path) # Simulates CWD being the tmp_path
    with caplog.at_level("INFO"):
        out = get_base_resource_path(rel)

    assert Path(out) == tmp_path / rel
    assert any(str(tmp_path / rel) in r.message for r in caplog.records)


def test_empty_rel_path_is_base_dir_when_no_meipass(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    out = get_base_resource_path("")
    assert Path(out) == tmp_path


@pytest.mark.parametrize('use_meipass', [True, False])
def test_get_base_resource_path_portable(tmp_path, monkeypatch, caplog, use_meipass):
    """
    Runs on all OSes and verifies:
    - without _MEIPASS  => base is CWD
    - with _MEIPASS     => base is that bundle dir
    - absolute path returned
    - captures logging
    """
    # Arrange: choose base dir depending on case
    rel = os.path.join('images', 'logo.png')

    if use_meipass:
        bundle_root = tmp_path / "bundle_root"
        bundle_root.mkdir()
        monkeypatch.setattr(sys, "_MEIPASS", str(bundle_root), raising=False)
        expected_base = bundle_root
    else:
        monkeypatch.chdir(tmp_path)
        expected_base = tmp_path

    # Action
    with caplog.at_level("INFO"):
        out = get_base_resource_path(rel)

    #Assert for path correctness
    out_path = Path(out)
    assert out_path == expected_base / rel

    # Assert: is absolute path on all platforms
    assert out_path.is_absolute()

    # Verify path on all sytems
    if platform.system() == "Windows":
        # Windows should always lead with a drive letter
        assert out_path.drive != ""
    else:
        # POSIX systems start with a '/' or os.sep
        assert str(out_path).startswith(os.sep)

    # Assert that logging is working properly
    assert any(str(out_path) in r.message for r in caplog.records)


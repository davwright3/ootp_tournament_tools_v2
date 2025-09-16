"""Base for configuration testing."""
import os
import sys
import tempfile
import configparser
import pytest
import tkinter as tk
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

@pytest.fixture(scope='session', autouse=True)
def _headless_env():
    """Hide some API warnings on macOS."""
    os.environ.setdefault("TK_SILENCE_DEPRECATION", '1')


@pytest.fixture
def tk_root():
    """Provide a tk root for widget testing."""
    root = tk.Tk()
    root.withdraw()
    yield root
    # Make sure pending after callbacks get cleared
    try:
        root.update_idletasks()
    except tk.TclError:
        pass
    root.destroy()


@pytest.fixture
def temp_settings_files(tmp_path, monkeypatch):
    """
    Create a temp settings.ini file and settings_default.ini to point
    config_utils to use during testing.
    Redirects settings.ini and settings_defaults.ini to a temporary folder.
    """
    app_dir = tmp_path / "settings_dir"
    app_dir.mkdir()

    user_ini = app_dir / "settings.ini"
    default_ini = app_dir / "settings_default.ini"

    # Override the path-returning functions before import
    monkeypatch.setattr(
        "utils.config_utils.get_user_settings_path.get_user_settings_path",
        lambda app_name: str(user_ini)
    )
    monkeypatch.setattr(
        "utils.config_utils.get_default_settings_path.get_default_settings_path",
        lambda: str(default_ini)
    )

    # Return paths so tests can use them
    return {"user": user_ini, "default": default_ini}

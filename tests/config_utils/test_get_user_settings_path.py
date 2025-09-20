"""
Test to verify that user settings on different OS's are discovered properly.

Expected return values:
Windows: */AppData/Roaming/au_otp_tournament_utilities_v2/settings.ini
macOS: */Library/Application Support/au_ootp_tournament_utilities_v2/settings.ini
Linux/other: config/{appname{
"""
from pathlib import Path, PureWindowsPath
import ntpath
# TODO 3: test macOS
# TODO 4: text other

import os
import sys
from utils.config_utils import get_user_settings_path as mod

def normpath(p) -> str:
    # Normalize paths
    return ntpath.normcase(ntpath.normpath(os.fspath(p)))

def test_nt_returns_appdata_path(monkeypatch, tmp_path):
    """Test that Windows system returns settings in AppData folder."""
    monkeypatch.setattr(os, 'name', 'nt', raising=False)
    monkeypatch.setattr(sys, 'platform', 'win32', raising=False)

    appdata_path = tmp_path / 'AppData' / "Roaming"
    monkeypatch.setenv('APPDATA', str(appdata_path))

    expected = PureWindowsPath(str(appdata_path)) / 'MyApp' / 'settings.ini'

    out = mod.get_user_settings_path('MyApp')
    assert normpath(out) == normpath(expected)
    assert ntpath.isabs(os.fspath(out))

def test_macos_returns_application_support_path(monkeypatch, tmp_path):
    """Test that macos returns settings in AppSupport folder."""
    monkeypatch.setattr(os, 'name', 'posix', raising=False)
    monkeypatch.setattr(sys, 'platform', 'darwin', raising=False)

    app_name = 'MyApp'
    fake_home_path = tmp_path / 'home'
    monkeypatch.setenv('HOME', str(fake_home_path))

    out = mod.get_user_settings_path(app_name)

    expected = os.path.join(
        os.path.expanduser(f'~/Library/Application Support/{app_name}/'),
        'settings.ini'
    )

    # Normalize separators and case for cross platform comparison
    def norm(p):
        return os.path.normcase(os.path.normpath(p))

    assert norm(out) == norm(expected)
    assert os.path.isdir(os.path.dirname(out))

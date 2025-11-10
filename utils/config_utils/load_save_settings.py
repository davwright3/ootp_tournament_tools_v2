"""Script for loading user settings."""
from configparser import ConfigParser
from pathlib import Path
import tempfile
import os
from utils.config_utils.get_user_settings_path import (
    get_user_settings_path
)
from utils.config_utils.get_default_settings_path import (
    get_default_settings_path
)
from utils.config_utils.verify_settings_up_to_date import (
    verify_settings_up_to_date
)

APP_NAME = 'AU OOTP Tournament Utilities v2'

SETTINGS_PATH = Path(get_user_settings_path(APP_NAME))
DEFAULT_SETTINGS_PATH = Path(get_default_settings_path())


# Internal methods
def _load_settings() -> ConfigParser:
    """
    Load settings from user's settings.ini file.
    If the user settings do not exist, will create a new settings.ini file =
    from the programs default_settings.ini.
    If the settings exist, will create a _settings session for use during
    program running.
    """

    config = ConfigParser()
    # Ensure file exists and crate if necessary
    if not SETTINGS_PATH.exists():
        SETTINGS_PATH.parent.mkdir(parents=True, exist_ok=True)
        if DEFAULT_SETTINGS_PATH.exists():
            config.read(DEFAULT_SETTINGS_PATH, encoding='utf-8')
            _atomic_write(config, SETTINGS_PATH)
        else:
            _atomic_write(config, SETTINGS_PATH)
    else:
        verify_settings_up_to_date(DEFAULT_SETTINGS_PATH, SETTINGS_PATH)
        config.read(SETTINGS_PATH, encoding='utf-8')

    return config


def _ensure_section(config: ConfigParser, section: str) -> None:
    if not config.has_section(section):
        config.add_section(section)


def _atomic_write(config: ConfigParser, path: Path) -> None:
    """Write config to disk"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
            'w',
            delete=False,
            encoding='utf-8',
            dir=str(path.parent)
    ) as tmp:
        config.write(tmp)
        tmp_path = Path(tmp.name)
    os.replace(tmp_path, path)


# Public API's
_settings = _load_settings()


def get_setting(section: str, option: str, fallback=None):
    """Safe read with fallbacks"""
    return _settings.get(section, option, fallback=fallback)


def update_setting(
        section: str,
        option: str,
        value: str,
        autosave: bool = True) -> None:
    _ensure_section(_settings, section)
    _settings.set(section, option, str(value))
    if autosave:
        save_settings()


def save_settings() -> None:
    """Sent current in memory settings to users settings.ini."""
    _atomic_write(_settings, SETTINGS_PATH)


def reload_settings() -> None:
    """Reload settings from users settings.ini."""
    global _settings
    _settings = _load_settings()


settings = _settings

"""Script for loading user settings."""
from configparser import ConfigParser
from config_utils.get_user_settings_path import get_user_settings_path
from config_utils.get_default_settings_path import get_default_settings_path
from config_utils.varify_settings_up_to_date import verify_settings_up_to_date

APP_NAME = 'AU OOTP Tournament Utilities v2'

SETTINGS_PATH = get_user_settings_path(APP_NAME)
DEFAULT_SETTINGS_PATH = get_default_settings_path()

def _load_settings():
    """Load settings from user's settings.ini file."""
    verify_settings_up_to_date(SETTINGS_PATH, DEFAULT_SETTINGS_PATH)

    config = ConfigParser()
    try:
        config.read(SETTINGS_PATH)
    except FileNotFoundError:
        print(f'No valid settings file found at {SETTINGS_PATH}')

    return config

settings = _load_settings()







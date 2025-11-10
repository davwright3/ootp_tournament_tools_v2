"""Script for comparing current user settings with
defaults to determine if required settings have been updated."""
import os
import logging
from configparser import ConfigParser


def new_cfg():
    # No interpolation
    cfg = ConfigParser(interpolation=None)
    cfg.optionxform = str
    return cfg


def verify_settings_up_to_date(default_path, user_settings_path):
    """
    Ensure that the user's settings file exists and is up to date.

    Args:
        default_path: path to the *default file*
        user_settings_path: path to the where the user settings should exist
        filename: name of the settings file

    Returns:
        Message letting the user know whether the settings were up to date
        or needed to be updated.
    """
    logger = logging.getLogger(__name__)
    # Normalize the string
    default_path = os.fspath(default_path)
    user_file = os.fspath(user_settings_path)

    # Make sure the parent directory exists
    os.makedirs(os.path.dirname(user_file) or ".", exist_ok=True)

    default_cfg = new_cfg()
    user_cfg = new_cfg()

    default_cfg.read(default_path, encoding='utf-8')
    user_cfg.read(user_file, encoding='utf-8')

    # Merge missing sections (preserving user values)
    updated = False

    for section in default_cfg.sections():
        if not user_cfg.has_section(section):
            user_cfg.add_section(section)
            logger.info(
                f'User settings file {user_file} was successfully updated.'
            )
            updated = True

        for key, value in default_cfg.items(section):
            if not user_cfg.has_option(section, key):
                user_cfg.set(section, key, value)
                logger.info(f'Setting {key} to {value}.')
                updated = True

    if updated:
        with open(user_file, 'w', encoding='utf-8') as f:
            user_cfg.write(f)
        logger.info(
            f'User settings file {user_file} was successfully updated.'
        )
        return True

    logger.info(f'User settings file {user_file} up to date.')
    return False

"""Script for comparing current user settings with
defaults to determine if required settings have been updated."""
import os
import shutil
from configparser import ConfigParser

def verify_settings_up_to_date(default_path, user_settings_path):
    """Check that user has most up to date settings file."""
    user_config = ConfigParser()
    default_config = ConfigParser()

    default_config.read(default_path)

    if not os.path.exists(user_settings_path):
        try:
            shutil.copyfile(default_path, user_settings_path)
            print(f'Created users settings at {user_settings_path}')
            return
        except FileNotFoundError or Exception as e:
            print(f'Could not copy default settings to {user_settings_path}, {e}')
            return

    user_config.read(user_settings_path)

    updated = False

    for section in default_config.sections():
        if not user_config.has_section(section):
            user_config.add_section(section)
            print(f'Adding section {section}')
            updated = True
        for key, value in default_config.items(section):
            if not user_config.has_option(section, key):
                user_config.set(section, key, value)
                print(f'Setting {key} to {value}')
                updated = True

    if updated:
        with open(user_settings_path, 'w') as configfile:
            user_config.write(configfile)
            print(f'User settings updated with missing defaults')
    else:
        print(f'Users settings up to date')
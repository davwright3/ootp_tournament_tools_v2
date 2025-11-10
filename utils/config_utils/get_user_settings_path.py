"""Utility to check which operating system is running
and adjust user settings path as necessary."""

import os
import sys


def get_user_settings_path(app_name):
    """
    Check OS and route program to user settings path.
    If program is installed on Windows, will use APPDATA as the root settings
    path.
    If program is installed on Linux, will use config as the root settings
    path.
    If program is installed on macOS, will use /Library/Application Suppoer
    as the root settings path.
    :param app_name: the name of the application for settings.ini location, str
    :return: the OS dependent path to the user's settings file, str
    """
    if os.name == 'nt':
        # Running in Windows
        # Uses Windows APPDATA roaming folder
        base_dir = os.path.join(
            os.getenv('APPDATA', os.path.expanduser('~')),
            app_name
        )
    elif sys.platform == 'darwin':
        # Running in macOS
        base_dir = os.path.expanduser(
            f'~/Library/Application Support/{app_name}/'
        )
    else:
        # Running on Linux or other OS
        base_dir = os.path.expanduser(f'~/.config/{app_name}/')

    os.makedirs(base_dir, exist_ok=True)
    return os.path.join(base_dir, 'settings.ini')

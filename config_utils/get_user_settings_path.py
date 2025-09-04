"""Utility to check which operating system is running
and adjust user settings path as necessary."""

import os
import sys

def get_user_settings_path(app_name):
    """Check OS and route program to user settings path."""
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

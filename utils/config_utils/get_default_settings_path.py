"""Get the default setting path based on python status."""
import os
import sys

def get_default_settings_path():
    """Find the path to the default settings.ini file."""
    if getattr(sys, 'frozen', False):
        # running as installed executable
        return os.path.join(sys._MEIPASS, 'settings_default.ini')
    else:
        # running as Python app
        return os.path.join(
            os.path.dirname(__file__),
            '..',
            'settings_default.ini'
        )
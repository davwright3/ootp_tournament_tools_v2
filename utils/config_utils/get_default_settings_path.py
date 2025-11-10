"""Get the default setting path based on python status."""
import os
import sys


def get_default_settings_path():
    """
    Find the path to the default settings.ini file.
    Checks the program to see if it is running in a frozen (PyInstaller)
    environment, and if so, joins the settings path with the temporary
    _MEIPASS directory created while the program is running.
    If not frozen (development environment), the default settings path to
    the base directory of the program is used.
    :return: the path to the default settings file, str
    """
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

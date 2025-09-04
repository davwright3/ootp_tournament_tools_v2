"""
Check current environment.

Utility for checking which environment is running and
adjusting resource path as necessary.
"""

import sys
import os

def get_resource_path(relative_path):
    """Get absolute resource path.

     Compatible with PyInstaller/Development environments."""
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        base_path = sys._MEIPASS
    else:
        # Running in development mode.
        base_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../..'))
    return os.path.join(base_path, relative_path)


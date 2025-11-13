"""
Check current environment.

Utility for checking which environment is running and
adjusting resource path as necessary.
"""
import sys
import os


def get_resource_path(relative_path):
    """
    Get absolute resource path.

    Compatible with PyInstaller/Development environments.
    Checks if system is frozen (PyInstaller environment), and if so, returns
    the base _MEIPASS root for resource discovery.
    If not frozen (development environment), the absolute path of the project
    is joined with the relative path of the file.
    :param relative_path: the relative path of the resource, str
    :return: the environment dependent path to the resource, str

     """
    if getattr(sys, 'frozen', False):
        # Running in PyInstaller bundle
        # On Mac the _MEIPASS may not appear as expected
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.dirname(sys.executable)
    else:
        # Running in development mode.
        base_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../../..'))
    return os.path.join(base_path, relative_path)

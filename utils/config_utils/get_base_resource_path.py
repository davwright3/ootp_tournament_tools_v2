import os
import sys
import logging


def get_base_resource_path(relative_path: str) -> str:
    """
    Examines program path to determine if it is running in a development
    or production (PyInstaller) environment.
    If _MEIPASS is in the directory, the program is in a PyInstaller
    environment and the base_path for resources will be joined into _MEIPASS
    directory.
    If no _MEIPASS is present, returns the absolute path for the program data
    joins the program relative path for the resource directory.
    :param relative_path: the relative path of the program, str
    :return: the base_path for resources, str
    """
    base_path = ""

    logger = logging.getLogger(__name__)

    if hasattr(sys, '_MEIPASS'):
        base_path = os.path.join(sys._MEIPASS, relative_path)
        logger.info(f'Path: {base_path}')
        return base_path
    base_path = os.path.join(os.path.abspath('.'), relative_path)
    logger.info(f'Base resource path set to: {base_path}')
    return base_path

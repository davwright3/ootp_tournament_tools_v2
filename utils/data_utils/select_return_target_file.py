"""Script for selecting and returning the path to the target file."""
from tkinter import filedialog
import os
from utils.config_utils import load_save_settings as settings_module
import logging


def select_return_target_file(parent, file_path=None):
    """
    Selects a returns the target file for concatenation, sets the
    path to a string variable on the parent window for display.
    :param parent: Parent window, tk.TkToplevel
    :param file_path: File path to be set, tk.StringVar
    :return: None
    """
    logger = logging.getLogger('apps.fileproc.data_utils')

    path = filedialog.askopenfilename(
        parent=parent,
        initialdir=settings_module.settings.get(
            'InitialTargetDirs',
            'starting_target_folder',
            fallback=os.getcwd()
        ),
        title="Choose target card list",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
    )

    if not path:
        logger.info('No target file selected')
    else:
        logger.info(f'{path} selected as target file')
        file_path.set(path)

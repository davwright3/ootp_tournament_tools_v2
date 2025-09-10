"""Script for selecting and returning the path to the target file."""
from tkinter import filedialog
import os
from utils.config_utils import load_save_settings as settings_module
import logging


def select_return_target_file(parent, file_path=None):
    logger = logging.getLogger('apps.fileproc.data_utils')

    path = filedialog.askopenfilename(
        parent=parent,
        initialdir=settings_module.settings.get('TargetFiles', 'target_card_list', fallback=os.getcwd()),
        title="Choose target card list",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
    )

    if not path:
        logger.info('No target file selected')
    else:
        logger.info(f'{path} selected as target file')
        file_path.set(path)
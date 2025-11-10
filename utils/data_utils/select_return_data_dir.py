"""Script for selecting and returning the raw data directory."""
from tkinter import filedialog
import logging
from utils.config_utils.load_save_settings import settings as loaded_settings


def select_return_data_dir(parent, dir_path=None):
    """
    Returns the raw data directory, and sets it to a StringVar on the
    parent window for display.
    :param parent: Parent window, tk.TkToplevel
    :param dir_path: Path to set, tk.StringVar
    :return: None
    """
    initial_dir = loaded_settings['InitialTargetDirs']['starting_data_folder']
    logger = logging.getLogger('apps.fileproc.data_utils')
    path = filedialog.askdirectory(
        parent=parent,
        initialdir=initial_dir,
        title='Select Raw Data Folder'
    )

    if not path:
        logger.info('No directory selected.')
        return
    else:
        try:
            dir_path.set(path)
            logger.info(f'Raw directory selected {dir_path.get()}.')
        except Exception as e:
            logger.info('Error while selecting data folder: {}'.format(e))
            return

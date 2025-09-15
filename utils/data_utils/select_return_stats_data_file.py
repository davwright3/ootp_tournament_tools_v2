"""Scripts for selecting file to load into DataFrame."""
import os
import logging
from tkinter import filedialog
from utils.config_utils import load_save_settings as settings_module

def select_return_stats_data_file(parent):
    """Select and return the file to be loaded into DataFrame."""
    logger = logging.getLogger('apps.basic_stats_app.data_utils')
    logger.info('Loading DataFrame')

    filepath = filedialog.askopenfilename(
        parent=parent,
        filetypes=(('CSV Files', '*.csv'), ('All Files', '*.*')),
        title="Choose Target File",
        initialdir=settings_module.settings.get('InitialTargetDirs', 'starting_target_folder'),
    )

    if not filepath:
        logger.info('No file selected')
        return

    logger.info(f'Loading data from from: {filepath}')


"""Scripts for selecting file to load into DataFrame."""
import logging
from tkinter import filedialog
from utils.config_utils import load_save_settings as settings_module
from utils.data_utils.data_store import data_store
from utils.data_utils.league_stats_store import league_stats_store


def select_load_stats_data_file(parent, loaded_file_var, file_loaded_bool):
    """
    Select the file to be loaded into DataFrame.
    :param parent: Parent window, tkTkToplevel
    :param loaded_file_var: Variable for displaying selected file, tkStringVar
    """
    logger = logging.getLogger('apps.basic_stats_app.data_utils')
    logger.info('Loading DataFrame')

    filepath = filedialog.askopenfilename(
        parent=parent,
        filetypes=(('CSV Files', '*.csv'), ('All Files', '*.*')),
        title="Choose Target File",
        initialdir=settings_module.settings.get(
            'InitialTargetDirs',
            'starting_target_folder'
        ),
    )

    if not filepath:
        logger.info('No file selected please select a file to load.')
        return

    logger.info(f'Loading data from from: {filepath}')
    try:
        data_store.load_data(filepath)
        loaded_file_var.set(filepath)
        file_loaded_bool.set(True)
        league_stats_store.load_stats()
        logger.info(f'Data loaded from {filepath}')
        logger.info(f'Loaded file contains {len(data_store.get_data())} rows'
                    f' of data.')
    except Exception as e:
        logger.error(f'Failed to load data from {filepath}: {e}')
        file_loaded_bool.set(False)

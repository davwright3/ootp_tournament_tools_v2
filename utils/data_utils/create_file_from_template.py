"""Script for creating new ready file from template."""
import logging
import os
import shutil
import re
from pathlib import Path
from utils.config_utils.load_save_settings import settings as loaded_settings
from utils.config_utils.get_resource_path import get_resource_path
from utils.dialog_utils.custom_input_dialog import CustomInputDialog


def sanitize_filename(filename):
    """
    Remove characters not allowed in the filename.
    :param filename: Input filename, string
    :return: Sanitized filename, removing any character not
     allowed in filename.
    """
    return re.sub(r'[^\w\s-]', '', filename.strip())


def create_file_from_template(parent):
    """
    Create a new empty csv (with headers) from a template file.
    File will be copied to the location set as the user's ready
    file folder in the settings from the main menu.
    :param parent: Parent Window, tk.TkToplevel
    :return: None
    """
    logger = logging.getLogger("apps.fileproc.data_utils")

    target_folder = (
        loaded_settings['InitialTargetDirs']['starting_target_folder']
    )
    template_path = get_resource_path(
        os.path.join('au_ootp_tournament_utilities_v2/image_assets',
                     'data_template.csv'
                     )
    )

    root_window = parent.winfo_toplevel()
    dialog = CustomInputDialog(
        root_window,
        title='Create New Ready File',
        prompt='Enter new file name (without extension):'
    )

    user_input = dialog.get_input()
    if not user_input:
        return
    sanitized_filename = sanitize_filename(user_input)

    name_only = Path(sanitized_filename).name
    stem = Path(name_only).stem
    base = Path(target_folder)
    destination_path = base / f"{stem}.csv"

    if os.path.isfile(template_path):
        if template_path.lower().endswith('.csv'):
            try:
                shutil.copy(template_path, destination_path)
                logger.info(f"Created new file at {destination_path}")
            except Exception as e:
                logger.error(f"Failed to copy template file: {e}")
        else:
            logger.error('Template is not valid')
    else:
        logger.error(f"Template file not found: {template_path}")

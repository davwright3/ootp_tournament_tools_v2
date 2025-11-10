"""Script for selecting and saving target start folder."""
from tkinter import filedialog
import os
from utils.config_utils import load_save_settings as settings_module


def select_initial_target_folder(parent, target_var):
    """
    Save new settings for the initial folder for the location of the user's
    ready (processed) data files.
    :param parent: the parent window instance, tkTopLevel
    :param target_var: the name of the target location to display, tk.StringVar
    :return: none
    """
    try:
        initial_directory = settings_module.settings.get(
            'InitialTargetDirs', 'starting_target_folder'
        )
        if not initial_directory or not os.path.isdir(initial_directory):
            raise Exception('Initial target folder not found')
    except Exception:
        initial_directory = os.getcwd()

    old_cwd = os.getcwd()
    try:
        path = filedialog.askdirectory(
            parent=parent,
            initialdir=initial_directory
        )
    finally:
        os.chdir(old_cwd)

    if path:
        settings_module.update_setting(
            'InitialTargetDirs',
            'starting_target_folder',
            path
        )
        target_var.set(path)


def select_initial_raw_data_folder(parent, target_var):
    """
    Save new settings for the initial folder for the location of the user's
    raw (downloaded, unprocessed) data files.
    :param parent: the parent window instance, tkTopLevel
    :param target_var: the name of the target location to display, tk.StringVar
    :return: none
    """
    try:
        initial_directory = settings_module.settings.get(
            'InitialTargetDirs', 'starting_data_folder'
        )
        if not initial_directory or not os.path.isdir(initial_directory):
            raise Exception('Initial data folder not found')
    except Exception:
        initial_directory = os.getcwd()

    old_cwd = os.getcwd()
    try:
        path = filedialog.askdirectory(
            parent=parent,
            initialdir=initial_directory
        )
    finally:
        os.chdir(old_cwd)

    if path:
        settings_module.update_setting(
            'InitialTargetDirs',
            'starting_data_folder',
            path
        )
        target_var.set(path)

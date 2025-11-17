"""Script for selecting a target file."""
from tkinter import filedialog
import os
from utils.config_utils import load_save_settings as settings_module


def select_target_file():
    """
    Select the target card list file, and save it to the settings file.
    This module allows the user to set the target of
    their OOTP Baseball Perfect Team card list dump from the card shop in game.
    This is a requirement for the statistics portion of the program to
    function.
    # :param target_var: The target card list file name for display, tk.StringVar
    :return: none
    """
    path = filedialog.askopenfilename(
        initialdir=settings_module.settings.get(
            'TargetFiles',
            'target_card_list',
            fallback=os.getcwd()
        ),
        title="Choose target card list",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
    )
    if path:
        settings_module.update_setting(
            'TargetFiles',
            'target_card_list',
            path
        )
        # target_var.set(path)
        return path

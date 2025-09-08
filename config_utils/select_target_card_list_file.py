"""Script for selecting a target file."""
from tkinter import filedialog
import os
from config_utils import load_save_settings as settings_module

def select_target_file(target_var):
    path = filedialog.askopenfilename(
        initialdir=settings_module.settings.get('TargetFiles', 'target_card_list', fallback=os.getcwd()),
        title="Choose target card list",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
    )
    if path:
        settings_module.update_setting('TargetFiles', 'target_card_list', path)
        target_var.set(path)

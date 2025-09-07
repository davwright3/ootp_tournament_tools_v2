"""Script for selecting a target file."""
from tkinter import filedialog
from config_utils.load_save_settings import update_setting, get_setting, reload_settings

def select_target_file(target_var):
    path = filedialog.askopenfilename(
        title="Choose target card list",
        filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
    )
    if path:
        update_setting('TargetFiles', 'target_card_list', path)
        target_var.set(path)
        reload_settings()
        print(f'Saved target card list to {path}')


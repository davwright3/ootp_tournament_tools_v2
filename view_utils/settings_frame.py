import os
import tkinter as tk
from configparser import ConfigParser
from config_utils.load_save_settings import settings as current_settings

class SettingsFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        settings = current_settings

        target_card_list_path = settings['TargetFiles']['target_card_list']
        if not os.path.isfile(target_card_list_path):
            target_card_list_path = None

        row=0





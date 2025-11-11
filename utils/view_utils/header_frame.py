"""Custom reusable header class for entire app."""
import tkinter as tk
from PIL import Image, ImageTk
import os
from utils.config_utils.get_resource_path import get_resource_path


class Header(tk.Frame):
    """Reusable header class for entire app."""
    def __init__(self, parent, app_name="AU Tournament Utilities V2"):
        """Initialize the header frame."""
        super().__init__(parent, bd=3, relief='groove', bg='lightgray')

        # File path for image
        logo_image_path = get_resource_path(
            os.path.join(
                'au_ootp_tournament_utilities_v2/image_assets',
                'unicorn_logo_nobg2.png')
        )
        self.name_text = app_name
        try:
            self.logo = Image.open(logo_image_path)
            self.logo = self.logo.resize((125, 125), Image.LANCZOS)
            self.reverse_logo = self.logo.transpose(Image.FLIP_LEFT_RIGHT)
            self.logo_tk_image = ImageTk.PhotoImage(self.logo)
            self.reverse_logo_tk_image = ImageTk.PhotoImage(self.reverse_logo)
        except FileNotFoundError:
            self.logo_tk_image = None
            self.reverse_logo_tk_image = None

        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)

        if self.logo_tk_image:
            self.logo_label = tk.Label(
                self, image=self.logo_tk_image, background='lightgray')
            self.logo_label.grid(row=0, column=0, sticky="w")

            self.title_label = tk.Label(
                self,
                text=self.name_text,
                font=("Arial", 16, "bold"),
                background='lightgray')
            self.title_label.grid(row=0, column=1, sticky="nsew")

            self.reverse_logo_label = tk.Label(
                self, image=self.reverse_logo_tk_image, background='lightgray')
            self.reverse_logo_label.grid(row=0, column=2, sticky="e")
        else:
            self.title_label = tk.Label(
                self,
                text=self.name_text,
                font=("Arial", 16, "bold"),
                background='lightgray')
            self.title_label.grid(row=0, column=1, sticky="nsew")

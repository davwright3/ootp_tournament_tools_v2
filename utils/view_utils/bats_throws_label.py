import tkinter as tk
from utils.view_utils import program_fonts as fonts


class BatsThrowsLabel(tk.Label):
    def __init__(self, parent, label_type: str=None, side_id=None):
        super().__init__(parent)

        self.configure(font=fonts.slideshow_label_font)
        self.update_rating(label_type, side_id)

    def update_rating(self, label_type, side_id):
        match label_type:
            case 'Bats':
                if int(side_id) == 1:
                    side_id = 'Right'
                elif int(side_id) == 2:
                    side_id = 'Left'
                else:
                    side_id = 'Switch'
            case 'Throws':
                if int(side_id) == 1:
                    side_id = 'Right'
                elif int(side_id) == 2:
                    side_id = 'Left'

        self.configure(text=f'{label_type}: {side_id}')
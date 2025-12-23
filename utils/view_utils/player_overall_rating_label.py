import tkinter as tk
from utils.view_utils import program_colors as colors
from utils.view_utils import program_fonts as fonts


class PlayerOverallRatingLabel(tk.Label):
    def __init__(self, parent, value):
        super().__init__(parent)

        self.update_overall_rating_label(value)

    def update_overall_rating_label(self, value):
        if value < 60:
            self.config(text=str(value))
            self.config(font=fonts.slideshow_label_font)
            self.config(bg=colors.IRON_BACKGROUND_COLOR)
            self.config(fg=colors.IRON_FONT_COLOR)
            self.config(borderwidth=2)
        elif value < 70:
            self.config(text=str(value))
            self.config(font=fonts.slideshow_label_font)
            self.config(bg=colors.BRONZE_BACKGROUND_COLOR)
            self.config(fg=colors.BRONZE_FONT_COLOR)
            self.config(borderwidth=2)
        elif value < 80:
            self.config(text=str(value))
            self.config(font=fonts.slideshow_label_font)
            self.config(bg=colors.SILVER_BACKGROUND_COLOR)
            self.config(fg=colors.SILVER_FONT_COLOR)
            self.config(borderwidth=2)
        elif value < 90:
            self.config(text=str(value))
            self.config(font=fonts.slideshow_label_font)
            self.config(bg=colors.GOLD_BACKGROUND_COLOR)
            self.config(fg=colors.GOLD_FONT_COLOR)
            self.config(borderwidth=2)
        elif value < 100:
            self.config(text=str(value))
            self.config(font=fonts.slideshow_label_font)
            self.config(bg=colors.DIAMOND_BACKGROUND_COLOR)
            self.config(fg=colors.DIAMOND_FONT_COLOR)
            self.config(borderwidth=2)
        else:
            self.config(text=str(value))
            self.config(font=fonts.slideshow_label_font)
            self.config(bg=colors.PERFECT_BACKGROUND_COLOR)
            self.config(fg=colors.PERFECT_FONT_COLOR)
            self.config(borderwidth=2)

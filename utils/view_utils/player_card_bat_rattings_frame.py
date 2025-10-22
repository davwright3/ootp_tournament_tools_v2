"""Frame for displaying batter ratings on player card."""
import tkinter as tk
import pandas as pd
from utils.view_utils.color_rating_code_label import ColorRatingLabel
from utils.view_utils import program_fonts as fonts

class BatterRatingFrame(tk.Frame):
    def __init__(self, parent, df=None):
        super().__init__(parent, relief='groove', bd=3)

        self.font = ('Arial', 18)

        self.columnconfigure(0, weight=1, minsize=80)
        self.columnconfigure(1, weight=1, minsize=80)
        self.columnconfigure(2, weight=1, minsize=80)
        self.columnconfigure(3, weight=1, minsize=80)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        # Set outer labels
        self.label = tk.Label(self, text='Batter Ratings', font=fonts.frame_title_font)
        self.label.grid(column=0, row=0, columnspan=4)

        self.overall_label = tk.Label(self, text='OA', font=fonts.basic_font)
        self.overall_label.grid(column=1, row=1)

        self.vs_left_label = tk.Label(self, text='vL', font=fonts.basic_font)
        self.vs_left_label.grid(column=2, row=1)

        self.vs_right_label = tk.Label(self, text='vR', font=fonts.basic_font)
        self.vs_right_label.grid(column=3, row=1)

        self.babip_label = tk.Label(self, text='BABIP', font=fonts.basic_font)
        self.babip_label.grid(column=0, row=2)

        self.avoid_k_label = tk.Label(self, text='AvoidK', font=fonts.basic_font)
        self.avoid_k_label.grid(column=0, row=3)

        self.gap_label = tk.Label(self, text='Gap', font=fonts.basic_font)
        self.gap_label.grid(column=0, row=4)

        self.power_label = tk.Label(self, text='Power', font=fonts.basic_font)
        self.power_label.grid(column=0, row=5)

        self.eye_label = tk.Label(self, text='Eye', font=fonts.basic_font)
        self.eye_label.grid(column=0, row=6)

        # Ratings labels
        self.babip_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['BABIP']
        )
        self.babip_rating_label.grid(column=1, row=2, sticky='nsew')

        self.avoid_k_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Avoid Ks']
        )
        self.avoid_k_rating_label.grid(column=1, row=3, sticky='nsew')

        self.gap_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Gap']
        )
        self.gap_rating_label.grid(column=1, row=4, sticky='nsew')

        self.power_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Power']
        )
        self.power_rating_label.grid(column=1, row=5, sticky='nsew')

        self.eye_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Eye']
        )
        self.eye_rating_label.grid(column=1, row=6, sticky='nsew')

        self.babip_vL_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['BABIP vL']
        )
        self.babip_vL_rating_label.grid(column=2, row=2, sticky='nsew')

        self.avoid_k_vL_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Avoid K vL']
        )
        self.avoid_k_vL_rating_label.grid(column=2, row=3, sticky='nsew')

        self.gap_vL_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Gap vL']
        )
        self.gap_vL_rating_label.grid(column=2, row=4, sticky='nsew')

        self.power_vL_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Power vL']
        )
        self.power_vL_label.grid(column=2, row=5, sticky='nsew')

        self.eye_vL_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Eye vL']
        )
        self.eye_vL_label.grid(column=2, row=6, sticky='nsew')

        self.babip_vR_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['BABIP vR']
        )
        self.babip_vR_rating_label.grid(column=3, row=2, sticky='nsew')

        self.avoid_k_vR_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Avoid K vR']
        )
        self.avoid_k_vR_rating_label.grid(column=3, row=3, sticky='nsew')

        self.gap_vR_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Gap vR']
        )
        self.gap_vR_rating_label.grid(column=3, row=4, sticky='nsew')

        self.power_vR_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Power vR']
        )
        self.power_vR_rating_label.grid(column=3, row=5, sticky='nsew')

        self.eye_vR_rating_label = ColorRatingLabel(
            self,
            font=fonts.basic_font,
            rating=df.iloc[0]['Eye vR']
        )
        self.eye_vR_rating_label.grid(column=3, row=6, sticky='nsew')

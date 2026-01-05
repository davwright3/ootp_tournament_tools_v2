import tkinter as tk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.color_rating_code_label import ColorRatingLabel
from utils.view_utils import program_fonts as fonts


class PlayerCardPitcherRatingsFrame(tk.Frame):
    def __init__(self, parent, df=None):
        super().__init__(parent, relief='groove', bd=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.label = tk.Label(
            self, text="Pitcher Ratings", font=fonts.frame_title_font)
        self.label.grid(row=0, column=0, sticky='nsew', columnspan=4)

        # Set up labels
        self.stuff_label = tk.Label(self, text="Stuff", font=fonts.basic_font)
        self.stuff_label.grid(row=2, column=0, sticky='nsew')

        self.p_hr_label = tk.Label(self, text="pHR", font=fonts.basic_font)
        self.p_hr_label.grid(row=3, column=0, sticky='nsew')

        self.pbabip_label = tk.Label(
            self, text="pBABIP", font=fonts.basic_font)
        self.pbabip_label.grid(row=4, column=0, sticky='nsew')

        self.control_label = tk.Label(
            self, text="Control", font=fonts.basic_font)
        self.control_label.grid(row=5, column=0, sticky='nsew')

        self.overall_label = tk.Label(self, text="OVR", font=fonts.basic_font)
        self.overall_label.grid(row=1, column=1, sticky='nsew')

        self.v_left_label = tk.Label(self, text="vL", font=fonts.basic_font)
        self.v_left_label.grid(row=1, column=2, sticky='nsew')

        self.v_right_label = tk.Label(self, text="vR", font=fonts.basic_font)
        self.v_right_label.grid(row=1, column=3, sticky='nsew')

        # Rating labels
        self.stuff_overall_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['Stuff']))
        self.stuff_overall_rating_label.grid(row=2, column=1, sticky='nsew')

        self.stuff_vl_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['Stuff vL']))
        self.stuff_vl_rating_label.grid(row=2, column=2, sticky='nsew')

        self.stuff_vr_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['Stuff vR']))
        self.stuff_vr_rating_label.grid(row=2, column=3, sticky='nsew')

        self.phr_overall_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['pHR']))
        self.phr_overall_rating_label.grid(row=3, column=1, sticky='nsew')

        self.phr_vl_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['pHR vL']))
        self.phr_vl_rating_label.grid(row=3, column=2, sticky='nsew')

        self.phr_vr_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['pHR vR']))
        self.phr_vr_rating_label.grid(row=3, column=3, sticky='nsew')

        self.pbabip_overall_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['pBABIP']))
        self.pbabip_overall_rating_label.grid(row=4, column=1, sticky='nsew')

        self.pbabib_vl_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['pBABIP vL']))
        self.pbabib_vl_rating_label.grid(row=4, column=2, sticky='nsew')

        self.pbabip_vr_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['pBABIP vR']))
        self.pbabip_vr_rating_label.grid(row=4, column=3, sticky='nsew')

        self.control_overall_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['Control']))
        self.control_overall_rating_label.grid(row=5, column=1, sticky='nsew')

        self.control_vl_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['Control vL']))
        self.control_vl_rating_label.grid(row=5, column=2, sticky='nsew')

        self.control_vr_rating_label = (
            ColorRatingLabel(
                self, font=fonts.basic_font, rating=df.iloc[0]['Control vR']))
        self.control_vr_rating_label.grid(row=5, column=3, sticky='nsew')


    def update_frame(self, player_df):
        self.stuff_overall_rating_label.update_label(
            player_df.iloc[0]['Stuff'],
            font=fonts.basic_font
        )
        self.stuff_vl_rating_label.update_label(
            player_df.iloc[0]['Stuff vL'],
            font=fonts.basic_font
        )
        self.stuff_vr_rating_label.update_label(
            player_df.iloc[0]['Stuff vR'],
            font=fonts.basic_font
        )
        self.phr_overall_rating_label.update_label(
            player_df.iloc[0]['pHR'],
            font=fonts.basic_font
        )
        self.phr_vl_rating_label.update_label(
            player_df.iloc[0]['pHR vL'],
            font=fonts.basic_font
        )
        self.phr_vr_rating_label.update_label(
            player_df.iloc[0]['pHR vR'],
            font=fonts.basic_font
        )
        self.pbabip_overall_rating_label.update_label(
            player_df.iloc[0]['pBABIP'],
            font=fonts.basic_font
        )
        self.pbabib_vl_rating_label.update_label(
            player_df.iloc[0]['pBABIP vL'],
            font=fonts.basic_font
        )
        self.pbabip_vr_rating_label.update_label(
            player_df.iloc[0]['pBABIP vR'],
            font=fonts.basic_font
        )
        self.control_overall_rating_label.update_label(
            player_df.iloc[0]['Control'],
            font=fonts.basic_font
        )
        self.control_vl_rating_label.update_label(
            player_df.iloc[0]['Control vL'],
            font=fonts.basic_font
        )
        self.control_vr_rating_label.update_label(
            player_df.iloc[0]['Control vR'],
            font=fonts.basic_font
        )


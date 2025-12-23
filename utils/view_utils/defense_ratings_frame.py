import tkinter as tk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.color_rating_code_label import ColorRatingLabel


class DefenseRatingsFrame(tk.Frame):
    def __init__(self, parent, df):
        super().__init__(parent, relief='groove', bd=3)

        catch_abil = int(df.iloc[0, df.columns.get_loc('CatcherAbil')])
        catch_frame = int(df.iloc[0, df.columns.get_loc('CatcherFrame')])
        catch_arm = int(df.iloc[0, df.columns.get_loc('Catcher Arm')])
        if_range = int(df.iloc[0, df.columns.get_loc('Infield Range')])
        if_error = int(df.iloc[0, df.columns.get_loc('Infield Error')])
        if_arm = int(df.iloc[0, df.columns.get_loc('Infield Arm')])
        turn_dp = int(df.iloc[0, df.columns.get_loc('DP')])
        of_range = int(df.iloc[0, df.columns.get_loc('OF Range')])
        of_error = int(df.iloc[0, df.columns.get_loc('OF Error')])
        of_arm = int(df.iloc[0, df.columns.get_loc('OF Arm')])

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        # Catcher Section
        self.catcher_label = tk.Label(
            self, text='Catcher', font=fonts.basic_font_bold)
        self.catcher_label.grid(row=1, column=0)

        self.catch_abil_label = tk.Label(
            self, text='Abil', font=fonts.basic_font_bold)
        self.catch_abil_label.grid(row=0, column=1)

        self.catch_frame_label = tk.Label(
            self, text='Frame', font=fonts.basic_font_bold)
        self.catch_frame_label.grid(row=0, column=2)

        self.catch_arm_label = tk.Label(
            self, text='Arm', font=fonts.basic_font_bold)
        self.catch_arm_label.grid(row=0, column=3)

        # Positions Section
        self.range_label = tk.Label(
            self, text='Range', font=fonts.basic_font_bold)
        self.range_label.grid(row=2, column=1)

        self.error_label = tk.Label(
            self, text='Error', font=fonts.basic_font_bold)
        self.error_label.grid(row=2, column=2)

        self.arm_label = tk.Label(
            self, text='Arm', font=fonts.basic_font_bold)
        self.arm_label.grid(row=2, column=3)

        self.turn_dp_label = tk.Label(
            self, text='DP', font=fonts.basic_font_bold)
        self.turn_dp_label.grid(row=2, column=4)

        self.infield_label = tk.Label(
            self, text='Infield', font=fonts.basic_font_bold)
        self.infield_label.grid(row=3, column=0)

        self.outfield_label = tk.Label(
            self, text='Outfield', font=fonts.basic_font_bold)
        self.outfield_label.grid(row=4, column=0)

        # Ratings
        self.catch_abil_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=catch_abil)
        self.catch_abil_rating_label.grid(row=1, column=1, sticky='ew')

        self.catch_frame_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=catch_frame)
        self.catch_frame_rating_label.grid(row=1, column=2, sticky='ew')

        self.catch_arm_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=catch_arm)
        self.catch_arm_rating_label.grid(row=1, column=3, sticky='ew')

        self.infield_range_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=if_range)
        self.infield_range_rating_label.grid(row=3, column=1, sticky='ew')

        self.infield_error_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=if_error)
        self.infield_error_rating_label.grid(row=3, column=2, sticky='ew')

        self.infield_arm_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=if_arm)
        self.infield_arm_rating_label.grid(row=3, column=3, sticky='ew')

        self.turn_dp_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=turn_dp)
        self.turn_dp_rating_label.grid(row=3, column=4, sticky='ew')

        self.outfield_range_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=of_range)
        self.outfield_range_rating_label.grid(row=4, column=1, sticky='ew')

        self.outfield_error_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=of_error)
        self.outfield_error_rating_label.grid(row=4, column=2, sticky='ew')

        self.outfield_arm_rating_label = ColorRatingLabel(
            self, font=fonts.basic_font, rating=of_arm)
        self.outfield_arm_rating_label.grid(row=4, column=3, sticky='ew')

    def update_frame(self, df):
        self.catch_abil_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['CatcherAbil'])
        self.catch_frame_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['CatcherFrame'])
        self.catch_arm_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['Catcher Arm'])

        self.infield_range_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['Infield Range'])
        self.infield_error_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['Infield Error'])
        self.infield_arm_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['Infield Arm'])
        self.turn_dp_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['DP'])

        self.outfield_range_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['OF Range'])
        self.outfield_error_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['OF Error'])
        self.outfield_arm_rating_label.update_label(font=fonts.basic_font, rating=df.iloc[0]['OF Arm'])

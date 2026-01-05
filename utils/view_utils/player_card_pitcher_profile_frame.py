import tkinter as tk
from tkinter import ttk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.color_rating_code_label import ColorRatingLabel


class PlayerCardPitcherProfileFrame(tk.Frame):
    def __init__(self, parent, df):
        super().__init__(parent, relief='groove', bd=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        pitcher_type = self.format_pitcher_type(df.iloc[0]['GB'])
        arm_slot = self.format_arm_slot(df.iloc[0]['Arm Slot'])

        self.pitcher_profile_label = tk.Label(
            self, text='Profile', font=fonts.frame_title_font)
        self.pitcher_profile_label.grid(
            row=0, column=0, sticky='nsew', columnspan=2)

        self.gb_type_label = tk.Label(
            self, text='GB/FB', font=fonts.basic_font)
        self.gb_type_label.grid(row=1, column=0, sticky='nsew')

        self.gb_type_rating_label = tk.Label(
            self, text=pitcher_type, font=fonts.basic_font)
        self.gb_type_rating_label.grid(row=1, column=1, sticky='nsew')

        self.arm_slot_label = tk.Label(
            self, text='Arm Slot', font=fonts.basic_font)
        self.arm_slot_label.grid(row=2, column=0, sticky='nsew')

        self.arm_slot_rating_label = tk.Label(
            self, text=arm_slot, font=fonts.basic_font)
        self.arm_slot_rating_label.grid(row=2, column=1, sticky='nsew')

        self.velocity_label = tk.Label(
            self, text='Velocity', font=fonts.basic_font)
        self.velocity_label.grid(row=3, column=0, sticky='nsew')

        self.velocity_rating_label = tk.Label(
            self, text=df.iloc[0]['Velocity'], font=fonts.basic_font)
        self.velocity_rating_label.grid(row=3, column=1, sticky='nsew')

        ttk.Separator(self, orient="horizontal").grid(
            row=4, column=0, sticky='nsew', columnspan=2)

        self.stamina_label = tk.Label(
            self, text='Stamina', font=fonts.basic_font)
        self.stamina_label.grid(row=5, column=0, sticky='nsew')

        self.stamina_frame = ColorRatingLabel(
            self, font=fonts.basic_font, rating=df.iloc[0]['Stamina'])
        self.stamina_frame.grid(row=5, column=1, sticky='nsew')

        self.hold_runners_label = tk.Label(
            self, text='Hold', font=fonts.basic_font)
        self.hold_runners_label.grid(row=6, column=0, sticky='nsew')

        self.hold_runners_frame = ColorRatingLabel(
            self, font=fonts.basic_font, rating=df.iloc[0]['Hold'])
        self.hold_runners_frame.grid(row=6, column=1, sticky='nsew')

    def format_pitcher_type(self, gb_type):
        match gb_type:
            case 0:
                return 'XGB'
            case 1:
                return 'GB'
            case 2:
                return 'Neu'
            case 3:
                return 'FB'
            case 4:
                return 'XFB'
            case _:
                return 'None'

    def format_arm_slot(self, arm_slot_id):
        match arm_slot_id:
            case 1:
                return 'Submarine'
            case 2:
                return 'Sidearm'
            case 3:
                return 'Normal (3/4)'
            case 4:
                return 'Over the Top'

    def update_frame(self, player_df):
        pitcher_type = self.format_pitcher_type(player_df.iloc[0]['GB'])
        arm_slot = self.format_arm_slot(player_df.iloc[0]['Arm Slot'])

        self.gb_type_rating_label.configure(text=pitcher_type)
        self.arm_slot_label.configure(text=arm_slot)
        self.velocity_label.configure(text=player_df.iloc[0]['Velocity'])
        self.stamina_frame.update_label(player_df.iloc[0]['Stamina'], font=fonts.basic_font)
        self.hold_runners_frame.update_label(player_df.iloc[0]['Hold'], font=fonts.basic_font)

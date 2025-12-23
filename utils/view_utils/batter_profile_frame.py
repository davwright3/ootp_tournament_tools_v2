import tkinter as tk
from utils.view_utils import program_fonts as fonts


class BatterProfileFrame(tk.Frame):
    def __init__(self, parent, df):
        super().__init__(parent, relief='groove', bd=3)

        self.update_frame(df)

    def update_frame(self, df):
        self.gb_profile = df.iloc[0]['GB Hitter Type']
        self.fb_profile = df.iloc[0]['FB Hitter Type']
        self.batted_ball_profile = df.iloc[0]['BattedBallType']

        match self.gb_profile:
            case 0:
                self.gb_profile_string = "Normal"
            case 1:
                self.gb_profile_string = "Spray"
            case 2:
                self.gb_profile_string = "Pull"
            case 3:
                self.gb_profile_string = "Ex. Pull"

        match self.fb_profile:
            case 0:
                self.fb_profile_string = "Normal"
            case 1:
                self.fb_profile_string = "Spray"
            case 2:
                self.fb_profile_string = "Pull"

        match self.batted_ball_profile:
            case 0:
                self.batted_ball_profile_string = "Normal"
            case 1:
                self.batted_ball_profile_string = "GB"
            case 2:
                self.batted_ball_profile_string = "FB"
            case 3:
                self.batted_ball_profile_string = "LD"

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=1)

        row = 1
        self.label = tk.Label(self,
                              text='Batter Profile',
                              font=fonts.frame_title_font)
        self.label.grid(row=row, column=0, sticky='nsew', columnspan=2)
        row += 1

        self.gb_profile_label = tk.Label(self,
                                         text='GB Profile:',
                                         font=fonts.basic_font)
        self.gb_profile_label.grid(row=row, column=0, sticky='e', padx=5)

        self.gb_profile_string_label = tk.Label(
            self,
            text=self.gb_profile_string,
            font=fonts.basic_font,
        )
        self.gb_profile_string_label.grid(row=row, column=1, sticky='nsew')
        row += 1

        self.fb_profile_label = tk.Label(self,
                                         text='FB Profile:',
                                         font=fonts.basic_font)
        self.fb_profile_label.grid(row=row, column=0, sticky='e', padx=5)

        self.fb_profile_string_label = tk.Label(
            self,
            text=self.fb_profile_string,
            font=fonts.basic_font,
        )
        self.fb_profile_string_label.grid(row=row, column=1, sticky='nsew')
        row += 1

        self.batted_ball_profile_label = tk.Label(self,
                                                  text='Batted Ball:',
                                                  font=fonts.basic_font)

        self.batted_ball_profile_label.grid(
            row=row, column=0, sticky='e', padx=5)
        self.batted_ball_profile_string_label = tk.Label(
            self,
            text=self.batted_ball_profile_string,
            font=fonts.basic_font,
        )
        self.batted_ball_profile_string_label.grid(
            row=row, column=1, sticky='nsew')
        row += 1

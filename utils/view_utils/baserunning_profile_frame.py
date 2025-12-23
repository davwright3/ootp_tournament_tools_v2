import tkinter as tk
from utils.view_utils.color_rating_code_label import ColorRatingLabel
from utils.view_utils import program_fonts as fonts


class BaserunningProfileFrame(tk.Frame):
    def __init__(self, parent, df):
        super().__init__(parent, relief='groove', bd=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)
        self.rowconfigure(6, weight=1)

        self.update_frame(df)

    def update_frame(self, df):
        self.speed = df.iloc[0]['Speed']
        self.steal_agg = df.iloc[0]['Steal Rate']
        self.stealing = df.iloc[0]['Stealing']
        self.baserunning = df.iloc[0]['Baserunning']

        row = 1
        self.label = tk.Label(
            self,
            text="Baserunning Profile",
            font=fonts.frame_title_font)
        self.label.grid(row=row, column=0, sticky='nsew', columnspan=2)
        row += 1

        self.speed_label = tk.Label(self,
                                    text="Speed",
                                    font=fonts.basic_font)
        self.speed_label.grid(row=row, column=0, sticky='nsew')

        self.speed_rating_label = ColorRatingLabel(
            self,
            rating=self.speed,
            font=fonts.basic_font,
        )
        self.speed_rating_label.grid(row=row, column=1, sticky='nsew')
        row += 1

        self.steal_rate_label = tk.Label(self,
                                         text="Steal Rate",
                                         font=fonts.basic_font)
        self.steal_rate_label.grid(row=row, column=0, sticky='nsew')

        self.steal_rate_rating_label = ColorRatingLabel(
            self,
            rating=self.stealing,
            font=fonts.basic_font,
        )
        self.steal_rate_rating_label.grid(row=row, column=1, sticky='nsew')
        row += 1

        self.stealing_label = tk.Label(self,
                                       text="Stealing",
                                       font=fonts.basic_font)
        self.stealing_label.grid(row=row, column=0, sticky='nsew')

        self.stealing_rating_label = ColorRatingLabel(
            self,
            rating=self.stealing,
            font=fonts.basic_font,
        )
        self.stealing_rating_label.grid(row=row, column=1, sticky='nsew')
        row += 1

        self.baserunning_label = tk.Label(self,
                                          text="Baserunning",
                                          font=fonts.basic_font)
        self.baserunning_label.grid(row=row, column=0, sticky='nsew')

        self.baserunning_rating_label = ColorRatingLabel(
            self,
            rating=self.baserunning,
            font=fonts.basic_font,
        )
        self.baserunning_rating_label.grid(row=row, column=1, sticky='nsew')
        row += 1

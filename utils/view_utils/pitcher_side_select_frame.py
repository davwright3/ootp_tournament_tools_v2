"""Frame for selecting the pitcher's arm side."""
import tkinter as tk


class PitcherSideSelectFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.pitcher_side_var = tk.StringVar(value='All')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.label = tk.Label(self, text='Pitcher Side')
        self.label.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.right_side_select_radio = tk.Radiobutton(
            self,
            text='RHP',
            value='R',
            variable=self.pitcher_side_var,
        )
        self.right_side_select_radio.grid(
            column=0,
            row=1,
            sticky='nsew'
        )

        self.left_side_select_radio = tk.Radiobutton(
            self,
            text='LHP',
            value='L',
            variable=self.pitcher_side_var,
        )
        self.left_side_select_radio.grid(
            column=1,
            row=1,
            sticky='nsew'
        )

        self.all_side_select_radio = tk.Radiobutton(
            self,
            text='All',
            value='All',
            variable=self.pitcher_side_var,
        )
        self.all_side_select_radio.grid(
            column=2,
            row=1,
            sticky='nsew'
        )

    def get_pitcher_side_select(self):
        return self.pitcher_side_var.get()

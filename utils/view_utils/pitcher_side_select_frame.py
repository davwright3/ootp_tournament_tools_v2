"""Frame for selecting the pitcher's arm side."""
import tkinter as tk

class PitcherSideSelectFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pitcher_side_var = tk.StringVar(value='All')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.right_side_select_radio = tk.Radiobutton(
            self,
            text='RHP',
            value='R',
        )
        self.right_side_select_radio.grid(
            column=0,
            row=0,
            sticky='nsew'
        )

        self.left_side_select_radio = tk.Radiobutton(
            self,
            text='LHP',
            value='L',
        )
        self.left_side_select_radio.grid(
            column=1,
            row=0,
            sticky='nsew'
        )

        self.all_side_select_radio = tk.Radiobutton(
            self,
            text='All',
            value='All',
        )
        self.all_side_select_radio.grid(
            column=2,
            row=0,
            sticky='nsew'
        )

    def get_pitcher_side_select(self):
        return self.pitcher_side_var.get()

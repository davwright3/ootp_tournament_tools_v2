"""Custom frame for selecting the type of pitcher."""
import tkinter as tk


class PitcherTypeSelectFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.pitcher_type_var = tk.StringVar(value='All')
        self.pitcher_type_cutoff = tk.StringVar(value='4.0')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.label = tk.Label(self, text="Pitcher Type")
        self.label.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.starter_select_radio = tk.Radiobutton(
            self,
            text='SP',
            variable=self.pitcher_type_var,
            value='SP',
        )
        self.starter_select_radio.grid(
            column=0,
            row=1,
            sticky="ew",
        )

        self.reliever_select_radio = tk.Radiobutton(
            self,
            text='RP',
            variable=self.pitcher_type_var,
            value='RP',

        )
        self.reliever_select_radio.grid(
            column=1,
            row=1,
            sticky="ew",
        )

        self.all_select_radio = tk.Radiobutton(
            self,
            text='All',
            variable=self.pitcher_type_var,
            value='All',

        )
        self.all_select_radio.grid(
            column=2,
            row=1,
            sticky="ew",
        )

        self.cutoff_select_label = tk.Label(self, text="SP/RP Cutoff")
        self.cutoff_select_label.grid(row=2, column=0, sticky="e")

        self.cutoff_select_entry = tk.Entry(
            self,
            width=10,
            textvariable=self.pitcher_type_cutoff
        )
        self.cutoff_select_entry.grid(row=2, column=1, sticky="w")

    def get_pitcher_type(self):
        return self.pitcher_type_var.get()

    def get_pitcher_type_cutoff(self):
        try:
            cutoff = float(self.cutoff_select_entry.get())
            return cutoff
        except ValueError:
            cutoff = 4.0

        return cutoff

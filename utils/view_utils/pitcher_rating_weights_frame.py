"""Custom frame for user entry of weights for pitcher ratings."""
import tkinter as tk
from utils.stats_utils.coerce_float import coerce_float


class PitcherWeightsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        # Variables for frame
        self.stuff_oa_weight = tk.StringVar(value='1.0')
        self.phr_oa_weight = tk.StringVar(value='1.0')
        self.pbabip_oa_weight = tk.StringVar(value='1.0')
        self.control_oa = tk.StringVar(value='1.0')

        self.stuff_vL_weight = tk.StringVar(value='1.0')
        self.phr_vL_weight = tk.StringVar(value='1.0')
        self.pbabip_vL_weight = tk.StringVar(value='1.0')
        self.control_vL_weight = tk.StringVar(value='1.0')

        self.stuff_vR_weight = tk.StringVar(value='1.0')
        self.phr_vR_weight = tk.StringVar(value='1.0')
        self.pbabip_vR_weight = tk.StringVar(value='1.0')
        self.control_vR_weight = tk.StringVar(value='1.0')

        # Set up rows and columns
        # Top rows are OA, vL, vR
        # Side rows are Stuff, pHR, pBABIP, Control
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        self.label = tk.Label(self, text="Pitcher Weights")
        self.label.grid(row=0, column=0, sticky='nsew', columnspan=4)

        # Top labels
        self.overall_label = tk.Label(self, text="OA")
        self.overall_label.grid(row=1, column=1, sticky='nsew')

        self.vL_label = tk.Label(self, text="vL")
        self.vL_label.grid(row=1, column=2, sticky='nsew')

        self.vR_label = tk.Label(self, text="vR")
        self.vR_label.grid(row=1, column=3, sticky='nsew')

        # Side labels
        self.stuff_label = tk.Label(self, text="Stuff")
        self.stuff_label.grid(row=2, column=0, sticky='nsew')

        self.phr_label = tk.Label(self, text="pHR")
        self.phr_label.grid(row=3, column=0, sticky='nsew')

        self.pbabip_label = tk.Label(self, text="pBABIP")
        self.pbabip_label.grid(row=4, column=0, sticky='nsew')

        self.control_label = tk.Label(self, text="Control")
        self.control_label.grid(row=5, column=0, sticky='nsew')

        # Entries
        self.stuff_oa_entry = tk.Entry(
            self, textvariable=self.stuff_oa_weight, width=2)
        self.stuff_oa_entry.grid(row=2, column=1, sticky='nsew')

        self.stuff_vL_entry = tk.Entry(
            self, textvariable=self.stuff_vL_weight, width=2)
        self.stuff_vL_entry.grid(row=2, column=2, sticky='nsew')

        self.stuff_vR_entry = tk.Entry(
            self, textvariable=self.stuff_vR_weight, width=2)
        self.stuff_vR_entry.grid(row=2, column=3, sticky='nsew')

        self.phr_oa_entry = tk.Entry(
            self, textvariable=self.phr_oa_weight, width=2)
        self.phr_oa_entry.grid(row=3, column=1, sticky='nsew')

        self.phr_vL_entry = tk.Entry(
            self, textvariable=self.phr_vL_weight, width=2)
        self.phr_vL_entry.grid(row=3, column=2, sticky='nsew')

        self.phr_vR_entry = tk.Entry(
            self, textvariable=self.phr_vR_weight, width=2)
        self.phr_vR_entry.grid(row=3, column=3, sticky='nsew')

        self.pbabip_oa_entry = tk.Entry(
            self, textvariable=self.pbabip_oa_weight, width=2)
        self.pbabip_oa_entry.grid(row=4, column=1, sticky='nsew')

        self.pbabip_vL_entry = tk.Entry(
            self, textvariable=self.pbabip_vL_weight, width=2)
        self.pbabip_vL_entry.grid(row=4, column=2, sticky='nsew')

        self.pbabip_vR_entry = tk.Entry(
            self, textvariable=self.pbabip_vR_weight, width=2)
        self.pbabip_vR_entry.grid(row=4, column=3, sticky='nsew')

        self.control_oa_entry = tk.Entry(
            self, textvariable=self.control_oa, width=2)
        self.control_oa_entry.grid(row=5, column=1, sticky='nsew')

        self.control_vL_entry = tk.Entry(
            self, textvariable=self.control_vL_weight, width=2)
        self.control_vL_entry.grid(row=5, column=2, sticky='nsew')

        self.control_vR_entry = tk.Entry(
            self, textvariable=self.control_vR_weight, width=2)
        self.control_vR_entry.grid(row=5, column=3, sticky='nsew')

    def get_pitcher_rating_weights(self):
        weight_vars = {
            'stuff': self.stuff_oa_weight,
            'stuff_vL': self.stuff_vL_weight,
            'stuff_vR': self.stuff_vR_weight,
            'phr': self.phr_oa_weight,
            'phr_vL': self.phr_vL_weight,
            'phr_vR': self.phr_vR_weight,
            'pbabip': self.pbabip_oa_weight,
            'pbabip_vL': self.pbabip_vL_weight,
            'pbabip_vR': self.pbabip_vR_weight,
            'control': self.control_oa,
            'control_vL': self.control_vL_weight,
            'control_vR': self.control_vR_weight,
        }

        weights = {
            f"weight_{name}": coerce_float(var, default=1.0)
            for name, var in weight_vars.items()
        }
        return weights

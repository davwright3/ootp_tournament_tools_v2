"""Modular frame for user to set weights for batting ratings."""
import tkinter as tk
from utils.stats_utils.coerce_float import coerce_float


class BatterWeightsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        # Variables for each rating
        self.babip_weight = tk.StringVar(value='1')
        self.avoidk_weight = tk.StringVar(value='1')
        self.gap_weight = tk.StringVar(value='1')
        self.power_weight = tk.StringVar(value='1')
        self.eye_weight = tk.StringVar(value='1')

        self.babip_vL_weight = tk.StringVar(value='1')
        self.avoidk_vL_weight = tk.StringVar(value='1')
        self.gap_vL_weight = tk.StringVar(value='1')
        self.power_vL_weight = tk.StringVar(value='1')
        self.eye_vL_weight = tk.StringVar(value='1')

        self.babip_vR_weight = tk.StringVar(value='1')
        self.avoidk_vR_weight = tk.StringVar(value='1')
        self.gap_vR_weight = tk.StringVar(value='1')
        self.power_vR_weight = tk.StringVar(value='1')
        self.eye_vR_weight = tk.StringVar(value='1')

        # Frame column and row setup
        # Top labels are OA, vL, vR
        # Side labels BABIP, Avoid K, Gap, Power, Eye
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
        self.rowconfigure(6, weight=1)

        self.label = tk.Label(self, text='Batter Weights')
        self.label.grid(column=0, row=0, sticky='nsew', columnspan=4)

        # Top labels
        self.overall_label = tk.Label(self, text="OA")
        self.overall_label.grid(row=1, column=1, sticky='nsew')

        self.vL_label = tk.Label(self, text="vL")
        self.vL_label.grid(row=1, column=2, sticky='nsew')

        self.vR_label = tk.Label(self, text="vR")
        self.vR_label.grid(row=1, column=3, sticky='nsew')

        # Side Labels
        self.babip_label = tk.Label(self, text="BABIP")
        self.babip_label.grid(row=2, column=0, sticky='nsew')

        self.avoidk_label = tk.Label(self, text="AvoidK")
        self.avoidk_label.grid(row=3, column=0, sticky='nsew')

        self.gap_label = tk.Label(self, text="Gap")
        self.gap_label.grid(row=4, column=0, sticky='nsew')

        self.power_label = tk.Label(self, text="Power")
        self.power_label.grid(row=5, column=0, sticky='nsew')

        self.eye_label = tk.Label(self, text="Eye")
        self.eye_label.grid(row=6, column=0, sticky='nsew')

        # Entries
        self.babip_oa_entry = tk.Entry(
            self, textvariable=self.babip_weight, width=2)
        self.babip_oa_entry.grid(
            row=2, column=1, sticky='nsew', padx=2, pady=2)

        self.babip_vL_entry = tk.Entry(
            self, textvariable=self.babip_vL_weight, width=2)
        self.babip_vL_entry.grid(
            row=2, column=2, sticky='nsew', padx=2, pady=2)

        self.babip_vR_entry = tk.Entry(
            self, textvariable=self.babip_vR_weight, width=2)
        self.babip_vR_entry.grid(
            row=2, column=3, sticky='nsew', padx=2, pady=2)

        self.avoidk_oa_entry = tk.Entry(
            self, textvariable=self.avoidk_weight, width=2)
        self.avoidk_oa_entry.grid(
            row=3, column=1, sticky='nsew', padx=2, pady=2)

        self.avoidk_vL_entry = tk.Entry(
            self, textvariable=self.avoidk_vL_weight, width=2)
        self.avoidk_vL_entry.grid(
            row=3, column=2, sticky='nsew', padx=2, pady=2)

        self.avoidk_vR_entry = tk.Entry(
            self, textvariable=self.avoidk_vR_weight, width=2)
        self.avoidk_vR_entry.grid(
            row=3, column=3, sticky='nsew', padx=2, pady=2)

        self.gap_oa_entry = tk.Entry(
            self, textvariable=self.gap_weight, width=2)
        self.gap_oa_entry.grid(row=4, column=1, sticky='nsew')

        self.gap_vL_entry = tk.Entry(
            self, textvariable=self.gap_vL_weight, width=2)
        self.gap_vL_entry.grid(row=4, column=2, sticky='nsew')

        self.gap_vR_entry = tk.Entry(
            self, textvariable=self.gap_vR_weight, width=2)
        self.gap_vR_entry.grid(row=4, column=3, sticky='nsew')

        self.power_oa_entry = tk.Entry(
            self, textvariable=self.power_weight, width=2)
        self.power_oa_entry.grid(row=5, column=1, sticky='nsew')

        self.power_vL_entry = tk.Entry(
            self, textvariable=self.power_vL_weight, width=2)
        self.power_vL_entry.grid(row=5, column=2, sticky='nsew')

        self.power_vR_entry = tk.Entry(
            self, textvariable=self.power_vR_weight, width=2)
        self.power_vR_entry.grid(row=5, column=3, sticky='nsew')

        self.eye_oa_entry = tk.Entry(
            self, textvariable=self.eye_weight, width=2)
        self.eye_oa_entry.grid(row=6, column=1, sticky='nsew')

        self.eye_vL_entry = tk.Entry(
            self, textvariable=self.eye_vL_weight, width=2)
        self.eye_vL_entry.grid(row=6, column=2, sticky='nsew')

        self.eye_vR_entry = tk.Entry(
            self, textvariable=self.eye_vR_weight, width=2)
        self.eye_vR_entry.grid(row=6, column=3, sticky='nsew')

    def get_batter_rating_weights(self):
        weight_vars = {
            'babip': self.babip_weight,
            'babip_vL': self.babip_vL_weight,
            'babip_vR': self.babip_vR_weight,
            'avoidk': self.avoidk_weight,
            'avoidk_vL': self.avoidk_vL_weight,
            'avoidk_vR': self.avoidk_vR_weight,
            'gap': self.gap_weight,
            'gap_vL': self.gap_vL_weight,
            'gap_vR': self.gap_vR_weight,
            'power': self.power_weight,
            'power_vL': self.power_vL_weight,
            'power_vR': self.power_vR_weight,
            'eye': self.eye_weight,
            'eye_vL': self.eye_vL_weight,
            'eye_vR': self.eye_vR_weight,
        }

        weights = {
            f'weight_{name}': coerce_float(var, default=1.0)
            for name, var in weight_vars.items()
        }
        return weights

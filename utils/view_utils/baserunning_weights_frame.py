"""Modular frame for user to select baserunning weights."""
import tkinter as tk
from utils.stats_utils.coerce_float import coerce_float


class BaserunningWeightFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        # Variables for frame
        self.speed_weight = tk.StringVar(value='1.0')
        self.steal_agg_weight = tk.StringVar(value='1.0')
        self.steal_ability_weight = tk.StringVar(value='1.0')
        self.baserunning_weight = tk.StringVar(value='1.0')

        # Set up columns and rows
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # Labels
        self.label = tk.Label(self, text='Baserunning Weights')
        self.label.grid(row=0, column=0, sticky='nsew', columnspan=2)

        self.speed_label = tk.Label(self, text='Speed')
        self.speed_label.grid(row=1, column=0, sticky='nsew')

        self.steal_agg_label = tk.Label(self, text='Steal Agg')
        self.steal_agg_label.grid(row=2, column=0, sticky='nsew')

        self.steal_ability_label = tk.Label(self, text='Steal Ability')
        self.steal_ability_label.grid(row=3, column=0, sticky='nsew')

        self.baserunning_label = tk.Label(self, text='BSR')
        self.baserunning_label.grid(row=4, column=0, sticky='nsew')

        # Entries
        self.speed_weight_entry = tk.Entry(self,
                                           textvariable=self.speed_weight)
        self.speed_weight_entry.grid(row=1, column=1, sticky='nsew')

        self.steal_agg_weight_entry = (
            tk.Entry(self, textvariable=self.steal_agg_weight))
        self.steal_agg_weight_entry.grid(row=2, column=1, sticky='nsew')

        self.steal_ability_weight_entry = (
            tk.Entry(self, textvariable=self.steal_ability_weight))
        self.steal_ability_weight_entry.grid(row=3, column=1, sticky='nsew')

        self.baserunning_weight_entry = (
            tk.Entry(self, textvariable=self.baserunning_weight))
        self.baserunning_weight_entry.grid(row=4, column=1, sticky='nsew')

    def get_baserunning_weights(self):
        weight_vars = {
            'speed': self.speed_weight,
            'steal_agg': self.steal_agg_weight,
            'steal_ability': self.steal_ability_weight,
            'baserunning': self.baserunning_weight
        }

        weights = {
            f'weight_{name}': coerce_float(var, default=1.0)
            for name, var in weight_vars.items()
        }
        return weights

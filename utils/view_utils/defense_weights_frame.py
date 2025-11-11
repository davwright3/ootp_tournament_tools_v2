"""Modular frame for user to set weights for defense."""
import tkinter as tk
from utils.stats_utils.coerce_float import coerce_float


class DefenseWeightsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        # Variables for weights
        self.catch_abil_weight = tk.StringVar(value='1.0')
        self.catch_frame_weight = tk.StringVar(value='1.0')
        self.catch_arm_weight = tk.StringVar(value='1.0')

        self.infield_range_weight = tk.StringVar(value='1.0')
        self.infield_error_weight = tk.StringVar(value='1.0')
        self.infield_arm_weight = tk.StringVar(value='1.0')
        self.turn_dp_weight = tk.StringVar(value='1.0')

        self.outfield_range_weight = tk.StringVar(value='1.0')
        self.outfield_error_weight = tk.StringVar(value='1.0')
        self.outfield_arm_weight = tk.StringVar(value='1.0')

        # Set up columns and rows
        # Two sections, catchers and infield/outfield with title at top
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        # Set up outer labels
        self.label = tk.Label(self, text='Defensive Weights')
        self.label.grid(row=0, column=0, sticky='nsew', columnspan=5)

        self.catcher_abil_label = tk.Label(self, text='Abil')
        self.catcher_abil_label.grid(row=1, column=1, sticky='nsew')

        self.catcher_frame_label = tk.Label(self, text='Frame')
        self.catcher_frame_label.grid(row=1, column=2, sticky='nsew')

        self.catch_arm_label = tk.Label(self, text='Arm')
        self.catch_arm_label.grid(row=1, column=3, sticky='nsew')

        self.catcher_label = tk.Label(self, text='Catcher')
        self.catcher_label.grid(row=2, column=0, sticky='nsew')

        self.range_label = tk.Label(self, text='Range')
        self.range_label.grid(row=3, column=1, sticky='nsew')

        self.error_label = tk.Label(self, text='Error')
        self.error_label.grid(row=3, column=2, sticky='nsew')

        self.arm_label = tk.Label(self, text='Arm')
        self.arm_label.grid(row=3, column=3, sticky='nsew')

        self.dp_label = tk.Label(self, text='DP')
        self.dp_label.grid(row=3, column=4, sticky='nsew')

        self.infield_label = tk.Label(self, text='INF')
        self.infield_label.grid(row=4, column=0, sticky='nsew')

        self.outfield_label = tk.Label(self, text='OF')
        self.outfield_label.grid(row=5, column=0, sticky='nsew')

        # Entries
        self.catcher_abil_entry = tk.Entry(
            self, textvariable=self.catch_abil_weight, width=2)
        self.catcher_abil_entry.grid(row=2, column=1, sticky='nsew')

        self.catcher_frame_entry = tk.Entry(
            self, textvariable=self.catch_frame_weight, width=2)
        self.catcher_frame_entry.grid(row=2, column=2, sticky='nsew')

        self.catcher_arm_entry = tk.Entry(
            self, textvariable=self.catch_arm_weight, width=2)
        self.catcher_arm_entry.grid(row=2, column=3, sticky='nsew')

        self.infield_range_entry = tk.Entry(
            self, textvariable=self.infield_range_weight, width=2)
        self.infield_range_entry.grid(row=4, column=1, sticky='nsew')

        self.infield_error_entry = tk.Entry(
            self, textvariable=self.infield_error_weight, width=2)
        self.infield_error_entry.grid(row=4, column=2, sticky='nsew')

        self.infield_arm_entry = tk.Entry(
            self, textvariable=self.infield_arm_weight, width=2)
        self.infield_arm_entry.grid(row=4, column=3, sticky='nsew')

        self.turn_dp_entry = tk.Entry(
            self, textvariable=self.turn_dp_weight, width=2)
        self.turn_dp_entry.grid(row=4, column=4, sticky='nsew')

        self.outfield_range_entry = tk.Entry(
            self, textvariable=self.outfield_range_weight, width=2)
        self.outfield_range_entry.grid(row=5, column=1, sticky='nsew')

        self.outfield_error_entry = tk.Entry(
            self, textvariable=self.outfield_error_weight, width=2)
        self.outfield_error_entry.grid(row=5, column=2, sticky='nsew')

        self.outfield_arm_entry = tk.Entry(
            self, textvariable=self.outfield_arm_weight, width=2)
        self.outfield_arm_entry.grid(row=5, column=3, sticky='nsew')

    def get_defense_ratings_weights(self):
        weight_vars = {
            'catch_abil': self.catch_abil_weight,
            'catch_frame': self.catch_frame_weight,
            'catch_arm': self.catch_arm_weight,
            'infield_range': self.infield_range_weight,
            'infield_error': self.infield_error_weight,
            'infield_arm': self.infield_arm_weight,
            'turn_dp': self.turn_dp_weight,
            'outfield_range': self.outfield_range_weight,
            'outfield_error': self.outfield_error_weight,
            'outfield_arm': self.outfield_arm_weight,
        }

        weights = {
            f'weight_{name}': coerce_float(var, default=1.0)
            for name, var in weight_vars.items()
        }
        return weights

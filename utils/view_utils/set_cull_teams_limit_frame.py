"""Modular frame for setting the runs per game at which teams get removed."""
import tkinter as tk


class SetCullTeamsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.cull_teams_var = tk.StringVar(value='8')

        self.label = tk.Label(self, text='Cull Teams Limit', justify='center')
        self.label.grid(row=0, column=0, sticky='ew')

        self.limit_label = tk.Label(self, text='Limit', justify='right')
        self.limit_label.grid(row=1, column=0, sticky='ew')

        self.limit_entry = tk.Entry(
            self,
            width=10,
            textvariable=self.cull_teams_var,
        )
        self.limit_entry.grid(row=1, column=1, sticky='w')

    def get_cull_teams_limit(self):
        try:
            limit = int(self.limit_entry.get())
        except ValueError:
            limit = 8
        return limit

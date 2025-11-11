"""Custom frame for selecting minimum team games."""
import tkinter as tk


class MinTeamGamesFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.min_team_games_var = tk.StringVar(value='20')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = tk.Label(
            self,
            text='Min Games'
        )
        self.label.grid(row=0, column=0, sticky='e')

        self.min_games_entry = tk.Entry(
            self,
            textvariable=self.min_team_games_var,
        )
        self.min_games_entry.grid(row=0, column=1, sticky='w')

    def get_min_games(self):
        try:
            min_games = int(self.min_games_entry.get())
        except ValueError:
            min_games = 20

        return min_games

import tkinter as tk
import customtkinter as ctk
from utils.data_utils.data_store import data_store


class TeamSelectFrame(tk.Frame):
    def __init__(self, parent, df=None):
        super().__init__(parent, relief='groove', bd=3)

        self.team_search_term = tk.StringVar(value='')
        self.selected_team = tk.StringVar(value='No Team Selected')
        self.team_list = ['No Team Selected']

        self.label = tk.Label(self, text='Select Team')
        self.label.grid(row=0, column=0, pady=(5, 0), padx=(5, 0))

        self.entry = tk.Entry(self, textvariable=self.team_search_term)
        self.entry.grid(row=0, column=1, pady=(5, 0), padx=(5, 0))

        self.team_select_dropdown = ctk.CTkOptionMenu(
            self,
            variable=self.selected_team,
            values=self.team_list,
            fg_color='white',
            button_color=('blue', 'darkblue'),
            text_color='black',
        )
        self.team_select_dropdown.grid(
            row=0, column=2, pady=(5, 0), padx=(5, 0))

        def on_enter_pressed(event):
            self.update_list()

        self.entry.bind('<Return>', on_enter_pressed)

    def update_list(self):
        try:
            df = data_store.get_data().copy()

            if self.team_search_term.get() != '':
                df = df[df['ORG'].str.lower().str.contains(
                    self.team_search_term.get().lower())]

            self.team_list = df['ORG'].unique().tolist()
            self.team_select_dropdown.configure(values=self.team_list)
            del df
        except Exception:
            return

    def get_selected_team(self):
        return self.selected_team.get()

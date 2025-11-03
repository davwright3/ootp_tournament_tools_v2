import tkinter as tk

from pygments.lexers import q


class TeamOnlyCheckboxFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.selected_team_bool = tk.BooleanVar(value=False)

        self.label = tk.Label(self, text='Selected Team Only: ')
        self.label.grid(column=0, row=0, padx=10, pady=10, sticky='e')

        self.checkbox = tk.Checkbutton(
            self,
            variable=self.selected_team_bool,
            onvalue=True,
            offvalue=False,
        )
        self.checkbox.grid(column=1, row=0, padx=10, pady=10, sticky='w')

    def get_selected_team_bool(self):
        return self.selected_team_bool.get()
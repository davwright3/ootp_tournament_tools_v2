import tkinter as tk

from pygments.lexers import q


class TeamOnlyCheckboxFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.selected_team_bool = tk.BooleanVar(value=False)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = tk.Label(self, text='Selected Team Only')
        self.label.grid(column=1, row=0, padx=3, pady=3, sticky='w')

        self.checkbox = tk.Checkbutton(
            self,
            variable=self.selected_team_bool,
            onvalue=True,
            offvalue=False,
        )
        self.checkbox.grid(column=0, row=0, padx=3, pady=3, sticky='e')

    def get_selected_team_bool(self):
        return self.selected_team_bool.get()

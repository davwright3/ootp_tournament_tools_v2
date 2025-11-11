"""Frame to allow user to select the minimum plate appearances."""
import tkinter as tk


class MinPlateAppearanceFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(
            self, parent, relief='ridge', borderwidth=3, padx=3, pady=3)

        self.min_plate_app_select = tk.IntVar(value=600)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = tk.Label(self, text="Min PA", justify='right')
        self.label.grid(column=0, row=0, padx=4, sticky='e')

        self.min_plate_app_entry = tk.Entry(
            self,
            textvariable=self.min_plate_app_select,
            width=10,
            justify='left',
        )
        self.min_plate_app_entry.grid(column=1, row=0, padx=4, sticky='w')

    def get_min_plate_app(self):
        try:
            min_plate_app = int(self.min_plate_app_entry.get())
        except ValueError:
            min_plate_app = 600

        return min_plate_app

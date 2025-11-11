"""Frame for selecting which side of batter to display."""
import tkinter as tk


class BattingSideSelectFrame(tk.Frame):
    """Frame for selecting which side of batter to display."""
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, relief='ridge', bd=3)

        self.selected_side_var = tk.StringVar(value='All')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.label = tk.Label(self, text="Batting Side", justify='center')
        self.label.grid(row=0, column=0, columnspan=4, sticky='ew')

        self.left_side_select = tk.Radiobutton(
            self,
            text='Left',
            variable=self.selected_side_var,
            value='L'
        )
        self.left_side_select.grid(row=1, column=0, sticky='ew')

        self.right_side_select = tk.Radiobutton(
            self,
            text='Right',
            variable=self.selected_side_var,
            value='R'
        )
        self.right_side_select.grid(row=1, column=1, sticky='ew')

        self.switch_select = tk.Radiobutton(
            self,
            text='Switch',
            variable=self.selected_side_var,
            value='S'
        )
        self.switch_select.grid(row=1, column=2, sticky='ew')

        self.all_select = tk.Radiobutton(
            self,
            text='All',
            variable=self.selected_side_var,
            value='All'
        )
        self.all_select.grid(row=1, column=3, sticky='ew')

    def get_selected_side(self):
        return self.selected_side_var.get()

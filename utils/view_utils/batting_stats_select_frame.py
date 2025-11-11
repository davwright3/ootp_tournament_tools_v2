"""Frame for selecting which batting stats to view."""
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkCheckBox


class BattingStatsSelectFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, relief='ridge', bd=3)

        self.available_stats = [
            'PA', 'AVG', 'OBP', 'SLG', 'OPS', 'wOBA', 'RCrate', 'HRrate',
            'Krate', 'BBrate', 'SBrate', 'SBpct', 'WARrate', 'ZRrate', 'Fld%'
        ]

        self.selected_stats = []

        def set_active_stats():
            self.selected_stats.clear()
            for child in self.winfo_children():
                if isinstance(child, CTkCheckBox):
                    if child.get() != 'off':
                        self.selected_stats.append(child.get())

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.label = tk.Label(
            self, text="Select Batting Stats", justify='center')
        self.label.grid(column=0, row=0, columnspan=3, sticky='nsew')

        stat_num = 0
        for stat in self.available_stats:
            checkbox = ctk.CTkCheckBox(
                master=self,
                text=stat,
                onvalue=stat,
                offvalue='off',
                command=set_active_stats,
            )
            checkbox.grid(
                row=stat_num // 3 + 1,
                column=stat_num % 3,
                padx=5,
                pady=5,
                sticky='nsew',
            )
            stat_num += 1

    def get_selected_stats(self):
        return self.selected_stats

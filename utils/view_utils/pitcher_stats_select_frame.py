"""Custom frame for checkboxes to select desired pitching stats to view."""
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkCheckBox


class PitcherStatsSelectFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.available_stats = ['IPC', 'ERA', 'FIP', 'WHIP', 'K%', 'BB%',
                                'K-BB', 'HR/9', 'SV%', 'SD/MD', 'IRS%',
                                'GB%', 'WAR/200', 'IP/G', 'QS%', 'oBABIP']

        self.selected_stats = []

        def set_active_stats():
            self.selected_stats.clear()
            for widget in self.winfo_children():
                if isinstance(widget, CTkCheckBox):
                    if widget.get() != 'off':
                        self.selected_stats.append(widget.get())

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.label = tk.Label(self, text='Pitching Stats Select')
        self.label.grid(row=0, column=0, columnspan=3, sticky='nsew')

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

    def get_active_stats(self):
        return self.selected_stats

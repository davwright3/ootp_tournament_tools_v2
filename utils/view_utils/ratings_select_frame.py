"""Modular frame for selecting ratings to view."""
import tkinter as tk
import customtkinter as ctk


class RatingsSelectFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        ratings_list = ['BatOA', 'BatvL', 'BatvR', 'BatSplit', 'Catch Def',
                        'IF Def', 'OF Def', 'Bsr', 'PitOA', 'PitvL', 'PitvR',
                        'PitSplit', 'Stamina', 'GB', 'BABIP', 'BABIP vL',
                        'BABIP vR', 'Gap', 'Gap vL', 'Gap vR', 'Power',
                        'Power vL', 'Power vR', 'Eye', 'Eye vL', 'Eye vR',
                        'Avoid Ks', 'Avoid K vL', 'Avoid K vR', 'date']
        self.selected_ratings_list = []

        def set_active_ratings():
            self.selected_ratings_list.clear()
            for widget in self.winfo_children():
                if isinstance(widget, ctk.CTkCheckBox):
                    if widget.get() != 'off':
                        self.selected_ratings_list.append(widget.get())

        self.label = tk.Label(self, text='Select ratings:')
        self.label.grid(column=0, row=0, sticky='nsew', columnspan=3)

        item = 0
        for rating in ratings_list:
            checkbox = ctk.CTkCheckBox(
                self,
                text=rating,
                onvalue=rating,
                offvalue='off',
                command=set_active_ratings,
            )
            checkbox.grid(row=item//3 + 1, column=item % 3, sticky='nsew')
            item += 1

    def get_active_ratings(self):
        return self.selected_ratings_list

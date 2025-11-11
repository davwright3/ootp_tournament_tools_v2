"""Modular frame for selecting general card info."""
import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkCheckBox


class GeneralInfoFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, relief='ridge', bd=3)

        self.available_items = ['owned', 'L10', 'VL10', 'B', 'T']
        self.selected_items = []

        def set_active_items():
            self.selected_items.clear()
            for widget in self.winfo_children():
                if isinstance(widget, CTkCheckBox):
                    if widget.get() != 'off':
                        self.selected_items.append(widget.get())

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.label = tk.Label(self, text='General Items', justify='center')
        self.label.grid(row=0, column=0, columnspan=3, sticky='nsew')

        item_num = 0
        for item in self.available_items:
            checkbox = ctk.CTkCheckBox(
                master=self,
                text=item,
                onvalue=item,
                offvalue='off',
                command=set_active_items,
            )
            checkbox.grid(
                column=item_num % 3, row=item_num // 3 + 1, sticky='nsew')
            item_num += 1

    def get_selected_items(self):
        return self.selected_items

"""
Custom frame for selecting which card types to view in the ratings
 comparison app.
 """
import tkinter as tk
import customtkinter as ctk


class CardTypeSelectFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Configure rows and columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        card_types = ['Live', 'NEL', 'Rookie', 'Legend', 'AS', 'FL',
                      'Snapshot', 'Unsung', 'Hardware']
        self.selected_card_types = []

        def update_selected_card_types():
            self.selected_card_types.clear()
            for widget in self.winfo_children():
                if isinstance(widget, ctk.CTkCheckBox):
                    if widget.get() != 'off':
                        self.selected_card_types.append(widget.get())

        self.label = tk.Label(self, text="Card Types")
        self.label.grid(column=0, row=0, sticky='nsew', columnspan=3)

        num = 1
        for item in card_types:
            checkbox = ctk.CTkCheckBox(
                self,
                text=item,
                command=update_selected_card_types,
                onvalue=num,
                offvalue='off',
            )
            checkbox.grid(
                row=((num - 1) // 3) + 1, column=(num - 1) % 3, sticky='nsew')
            num += 1

    def get_selected_card_types(self):
        if not self.selected_card_types:
            return None
        else:
            return self.selected_card_types

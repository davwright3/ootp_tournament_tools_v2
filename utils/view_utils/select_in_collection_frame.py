"""Custom frame for users to select card in collection only."""
import tkinter as tk


class SelectInCollectionFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='groove', bd=3)

        self.only_in_collection_var = tk.BooleanVar(value=False)

        self.columnconfigure(0, weight=1)

        self.collection_checkbox = tk.Checkbutton(
            self,
            text='Collection Only: ',
            variable=self.only_in_collection_var,
            onvalue=True,
            offvalue=False,
        )
        self.collection_checkbox.grid(column=0, row=0, padx=10, pady=10)

    def get_collection_only_value(self):
        return self.only_in_collection_var.get()

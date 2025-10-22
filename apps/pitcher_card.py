"""App for displaying individual pitcher data."""
import tkinter as tk


class PitcherCard(tk.Toplevel):
    def __init__(self, card_id=None):
        super().__init__()

        self.title(f'Pitcher Card for {card_id}')
        self.geometry('1920x1080')
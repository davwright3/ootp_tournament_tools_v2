"""Batter card for displaying individual batter stats."""
import tkinter as tk

class BatterCard(tk.Toplevel):
    def __init__(self, card_id=None):
        super().__init__()

        self.title(f'Batter Card for {card_id}')
        self.geometry('1920x1080')


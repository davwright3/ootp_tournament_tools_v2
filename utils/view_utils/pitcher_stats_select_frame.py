"""Custom frame for checkboxes to select desired pitching stats to view."""
import tkinter as tk

class PitcherStatsSelectFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        available_stats = ['']

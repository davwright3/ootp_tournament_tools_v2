"""
Main app for displaying batting stats for all players.

Opens a tkinter TopLevel app, and gets data from the
loaded data store to display in a custom frame for
displaying DataFrames.
"""
import tkinter as tk


class BattingStatsApp(tk.Toplevel):
    def __init__(self):
        super().__init__()


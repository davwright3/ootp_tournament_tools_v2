"""
App for viewing basic hitting, pitching and team stats.
Loads a dataframe singleton for opening apps for specific categories.
"""
import tkinter as tk

class BasicStatsApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Basic Stats Views")
        self.geometry("1920x1080")


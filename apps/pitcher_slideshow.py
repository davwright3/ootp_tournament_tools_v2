import tkinter as tk


class PitcherSlideshowApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry('1920x1080')
        self.title('Pitching Leaders')
"""Custom label that codes based off of rating."""
import tkinter as tk


class ColorRatingLabel(tk.Label):
    def __init__(self, parent, font=None, rating: int = 0):
        super().__init__(parent)

        self.font = font
        self.rating = rating

        self.update_label(self.rating, self.font)


    def update_label(self, rating, font):
        self.configure(text=rating)
        self.configure(font=font)

        if rating == 0:
            self.configure(text='-')
            self.configure(bg='white')
        elif rating < 50:
            self.configure(bg='#ff5959')
        elif rating < 60:
            self.configure(bg='#ff9700')
        elif rating < 75:
            self.configure(bg='#ffe10b')
        elif rating < 85:
            self.configure(bg='#65e212')
        elif rating < 100:
            self.configure(bg='#00c6a2')
        elif rating < 125:
            self.configure(bg='#0099ff')
        elif rating < 150:
            self.configure(bg='#9f73ff')
        else:
            self.configure(bg='#bf4dff')
"""Frame for selecting which position to view."""
import tkinter as tk
from tkinter import Radiobutton


class PositionSelectFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='ridge', bd=3, bg='lightgrey')

        self.selected_position = tk.StringVar(value='All')

        self.label = tk.Label(
            self, text="Position Selection", justify='center')
        self.label.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        item = 0
        self.catcher_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='C',
            value='LearnC'
        )
        self.catcher_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

        self.firstbase_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='1B',
            value='Learn1B'
        )
        self.firstbase_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

        self.secondbase_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='2B',
            value='Learn2B'
        )
        self.secondbase_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

        self.thirdbase_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='3B',
            value='Learn3B'
        )
        self.thirdbase_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

        self.shortstop_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='SS',
            value='LearnSS'
        )
        self.shortstop_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

        self.leftfield_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='LF',
            value='LearnLF'
        )
        self.leftfield_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

        self.centerfield_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='CF',
            value='LearnCF',
        )
        self.centerfield_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

        self.rightfield_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='RF',
            value='LearnRF'
        )
        self.rightfield_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

        self.pitcher_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='P',
            value='Pitcher Role'
        )
        self.pitcher_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

        self.allbatters_select = Radiobutton(
            self,
            variable=self.selected_position,
            text='All',
            value='All'
        )
        self.allbatters_select.grid(
            row=item // 3 + 1, column=item % 3, sticky='nsew')
        item += 1

    def get_position_select(self):
        if self.selected_position.get() == 'All':
            return None
        else:
            return self.selected_position.get()

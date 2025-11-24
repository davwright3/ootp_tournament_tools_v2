import tkinter as tk
from utils.stats_utils.get_run_environment import get_run_environment


class RunEnvironmentFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.selected_year = tk.StringVar(value='2000')

        self.babip_var = tk.StringVar(value='0')
        self.hrrate_var = tk.StringVar(value='0')
        self.xbhrate_var = tk.StringVar(value='0')
        self.krate_var = tk.StringVar(value='0')
        self.bbrate_var = tk.StringVar(value='0')
        self.sbrate_var = tk.StringVar(value='0')
        self.sbpctrate_var = tk.StringVar(value='0')

        def update_run_environment():
            try:
                selected_year = int(self.selected_year.get())
                df = get_run_environment(selected_year)
                self.babip_var.set(df.iloc[0]['BABIP'])
                self.hrrate_var.set(df.iloc[0]['HRrate'])
                self.xbhrate_var.set(df.iloc[0]['XBHrate'])
                self.krate_var.set(df.iloc[0]['Krate'])
                self.bbrate_var.set(df.iloc[0]['BBrate'])
                self.sbrate_var.set(df.iloc[0]['SBrate'])
                self.sbpctrate_var.set(df.iloc[0]['SBPct'])
            except ValueError:
                print("Error setting run environment")
                return

        column = 0
        self.rerun_environment_button = tk.Button(self, text='RERUN', command=update_run_environment)
        self.rerun_environment_button.grid(row=0, column=column, sticky='nsew')
        column += 1

        self.select_run_environment_label = tk.Label(self, text='Select Year')
        self.select_run_environment_label.grid(row=0, column=column, padx=1, pady=1)
        column += 1

        self.select_run_environment_entry = tk.Entry(
            self, textvariable=self.selected_year, width=10)
        self.select_run_environment_entry.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.label = tk.Label(self, text=f"{self.selected_year.get()} Run Environment")
        self.label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.babip_label = tk.Label(self, text='BABIP: ')
        self.babip_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.babip_stat_label = tk.Label(self, textvariable=self.babip_var)
        self.babip_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.hrrate_label = tk.Label(self, text='HRrate: ')
        self.hrrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.hrrate_stat_label = tk.Label(self, textvariable=self.hrrate_var)
        self.hrrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.xbhrate_label = tk.Label(self, text='XBHrate: ')
        self.xbhrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.xbhrate_stat_label = tk.Label(self, textvariable=self.xbhrate_var)
        self.xbhrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.krate_label = tk.Label(self, text='Krate: ')
        self.krate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.krate_stat_label = tk.Label(self, textvariable=self.krate_var)
        self.krate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.bbrate_label = tk.Label(self, text='BBRate: ')
        self.bbrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.bbrate_stat_label = tk.Label(self, textvariable=self.bbrate_var)
        self.bbrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.sbrate_label = tk.Label(self, text='SBRate: ')
        self.sbrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.sbrate_stat_label = tk.Label(self, textvariable=self.sbrate_var)
        self.sbrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.sbpctrate_label = tk.Label(self, text='SBPct: ')
        self.sbpctrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.sbpctrate_stat_label = tk.Label(self, textvariable=self.sbpctrate_var)
        self.sbpctrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        update_run_environment()

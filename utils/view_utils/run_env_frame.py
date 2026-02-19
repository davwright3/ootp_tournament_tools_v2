import tkinter as tk
import customtkinter as ctk
from utils.stats_utils.get_run_environment import (
    get_run_environment, get_park_factors)
from utils.view_utils import program_fonts as fonts


class RunEnvironmentFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.selected_year = tk.StringVar(value='2010')
        self.selected_stadium = tk.StringVar(value='Heinsohn Ballpark 2025')

        self.stadiums = get_park_factors()

        # Year ennvironment variables
        self.babip_var = tk.StringVar(value='0')
        self.hrrate_var = tk.StringVar(value='0')
        self.xbhrate_var = tk.StringVar(value='0')
        self.krate_var = tk.StringVar(value='0')
        self.bbrate_var = tk.StringVar(value='0')
        self.sbrate_var = tk.StringVar(value='0')
        self.sbpctrate_var = tk.StringVar(value='0')

        # Stadium environment variables
        self.avg_lhb_var = tk.StringVar(value='0')
        self.avg_rhb_var = tk.StringVar(value='0')
        self.hr_lhb_var = tk.StringVar(value='0')
        self.hr_rhb_var = tk.StringVar(value='0')
        self.doubles_var = tk.StringVar(value='0')
        self.triples_var = tk.StringVar(value='0')

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

        def get_park_list():
            stadium_list = list(self.stadiums['name_and_year'])
            return stadium_list

        def set_park_factors():
            try:
                selected_stadium = self.selected_stadium.get()
                condition = self.stadiums['name_and_year'] == selected_stadium
                row = self.stadiums.loc[condition]
                self.avg_lhb_var.set(row.iloc[0]['Avg LHB'])
                self.avg_rhb_var.set(row.iloc[0]['Avg RHB'])
                self.hr_lhb_var.set(row.iloc[0]['HR LHB'])
                self.hr_rhb_var.set(row.iloc[0]['HR RHB'])
                self.doubles_var.set(row.iloc[0]['2B'])
                self.triples_var.set(row.iloc[0]['3B'])
            except Exception:
                print("Failed to set park factors")

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

        self.babip_label = tk.Label(self, text='BABIP: ', font=fonts.basic_font)
        self.babip_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.babip_stat_label = tk.Label(self, textvariable=self.babip_var, font=fonts.basic_font)
        self.babip_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.hrrate_label = tk.Label(self, text='HRrate: ', font=fonts.basic_font)
        self.hrrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.hrrate_stat_label = tk.Label(self, textvariable=self.hrrate_var, font=fonts.basic_font)
        self.hrrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.xbhrate_label = tk.Label(self, text='XBHrate: ', font=fonts.basic_font)
        self.xbhrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.xbhrate_stat_label = tk.Label(self, textvariable=self.xbhrate_var, font=fonts.basic_font)
        self.xbhrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.krate_label = tk.Label(self, text='Krate: ', font=fonts.basic_font)
        self.krate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.krate_stat_label = tk.Label(self, textvariable=self.krate_var, font=fonts.basic_font)
        self.krate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.bbrate_label = tk.Label(self, text='BBRate: ', font=fonts.basic_font)
        self.bbrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.bbrate_stat_label = tk.Label(self, textvariable=self.bbrate_var, font=fonts.basic_font)
        self.bbrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.sbrate_label = tk.Label(self, text='SBRate: ', font=fonts.basic_font)
        self.sbrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.sbrate_stat_label = tk.Label(self, textvariable=self.sbrate_var, font=fonts.basic_font)
        self.sbrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.sbpctrate_label = tk.Label(self, text='SBPct: ', font=fonts.basic_font)
        self.sbpctrate_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        self.sbpctrate_stat_label = tk.Label(self, textvariable=self.sbpctrate_var, font=fonts.basic_font)
        self.sbpctrate_stat_label.grid(column=column, row=0, sticky='nsew')
        column += 1

        update_run_environment()
        set_park_factors()

        column = 0
        self.stadium_dropdown = ctk.CTkOptionMenu(
            self,
            values=get_park_list(),
            variable=self.selected_stadium,
        )
        self.stadium_dropdown.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.set_park_factors_button = tk.Button(self, text='Set Park Factors', command=set_park_factors)
        self.set_park_factors_button.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.avg_lhb_label = tk.Label(self, text='Avg LHB: ', font=fonts.basic_font)
        self.avg_lhb_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.avg_lhb_stat_label = tk.Label(self, textvariable=self.avg_lhb_var, font=fonts.basic_font)
        self.avg_lhb_stat_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.avg_rhb_label = tk.Label(self, text='Avg RHB: ', font=fonts.basic_font)
        self.avg_rhb_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.avg_rhb_stat_label = tk.Label(self, textvariable=self.avg_rhb_var, font=fonts.basic_font)
        self.avg_rhb_stat_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.hr_lhb_label = tk.Label(self, text='HR LHB: ', font=fonts.basic_font)
        self.hr_lhb_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.hr_lhb_stat_label = tk.Label(self, textvariable=self.hr_lhb_var, font=fonts.basic_font)
        self.hr_lhb_stat_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.hr_rhb_label = tk.Label(self, text='HR RHB: ', font=fonts.basic_font)
        self.hr_rhb_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.hr_rhb_stat_label = tk.Label(self, textvariable=self.hr_rhb_var, font=fonts.basic_font)
        self.hr_rhb_stat_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.double_label = tk.Label(self, text='2B: ', font=fonts.basic_font)
        self.double_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.double_stat_label = tk.Label(self, textvariable=self.doubles_var, font=fonts.basic_font)
        self.double_stat_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.triples_label = tk.Label(self, text='3B: ', font=fonts.basic_font)
        self.triples_label.grid(column=column, row=1, sticky='nsew')
        column += 1

        self.triples_stat_label = tk.Label(self, textvariable=self.triples_var, font=fonts.basic_font)
        self.triples_stat_label.grid(column=column, row=1, sticky='nsew')

    def get_run_environment_factors(self):
        try:
            avg_lhb_calc = round(float(self.babip_var.get()) * float(self.avg_lhb_var.get()), 3)
        except ValueError:
            avg_lhb_calc = 1.0

        try:
            avg_rhb_calc = round(float(self.babip_var.get()) * float(self.avg_rhb_var.get()), 3)
        except ValueError:
            avg_rhb_calc = 1.0

        try:
            hr_lhb_calc = round(float(self.babip_var.get()) * float(self.hr_lhb_var.get()), 3)
        except ValueError:
            hr_lhb_calc = 1.0

        try:
            hr_rhb_calc = round(float(self.babip_var.get()) * float(self.hr_rhb_var.get()), 3)
        except ValueError:
            hr_rhb_calc = 1.0

        try:
            doubles_calc = round(float(self.babip_var.get()) * float(self.doubles_var.get()), 3)
        except ValueError:
            doubles_calc = 1.0

        try:
            triples_calc = round(float(self.babip_var.get()) * float(self.triples_var.get()), 3)
        except ValueError:
            triples_calc = 1.0

        run_env_factors = {
            'avg_lhb': avg_lhb_calc,
            'avg_rhb': avg_rhb_calc,
            'hr_lhb': hr_lhb_calc,
            'hr_rhb': hr_rhb_calc,
            'doubles': doubles_calc,
            'triples': triples_calc,
        }
        return run_env_factors


import tkinter as tk
from tkinter import ttk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.data_vis_scatter_frame_2d import DataVisScatterFrame2d
from utils.view_utils.data_vis_scatter_frame_3d import DataVisualScatterFrame3D
from utils.data_vis_utils.generate_babip_vis_df import generate_babip_vis_df
from utils.data_vis_utils.generate_hr_fb_vis_df import generate_hr_bip_vis
from utils.data_vis_utils.generate_bip_rate_df import generate_bip_rate_df
from utils.data_vis_utils.generate_k_rate_df import generate_k_rate_df


class DataVisualizationApp(tk.Toplevel):
    def __init__(self, selected_team=None):
        super().__init__()

        # Methods for displaying data vis frames
        def clear_display_frame():
            for widget in self.display_frame.winfo_children():
                widget.destroy()

        def display_babip_vis():
            clear_display_frame()
            babip_df = generate_babip_vis_df()
            self.babip_frame = DataVisScatterFrame2d(self.display_frame,
                                                     df=babip_df)
            self.babip_frame.grid(row=0, column=0, sticky='nsew')

        def display_hr_bip_vis():
            clear_display_frame()
            hr_df = generate_hr_bip_vis()
            self.hr_scatter_frame = DataVisScatterFrame2d(self.display_frame, df=hr_df)
            self.hr_scatter_frame.grid(row=0, column=0, sticky='nsew')

        def display_k_rate_vis():
            clear_display_frame()
            krate_df = generate_k_rate_df()
            self.krate_scatter_frame = DataVisualScatterFrame3D(
                self.display_frame, df=krate_df)
            self.krate_scatter_frame.grid(row=0, column=0, sticky='nsew')

        def display_bip_rate_vis():
            clear_display_frame()
            bip_df = generate_bip_rate_df()
            self.bip_scatter_frame = DataVisualScatterFrame3D(self.display_frame,
                                                              df=bip_df)
            self.bip_scatter_frame.grid(row=0, column=0, sticky='nsew')


        self.geometry('1920x1080')
        self.title('Data Visualization')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        self.header_frame = Header(self, app_name='Data Visualization')
        self.header_frame.grid(row=0, column=0, sticky='nsew')

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky='nsew')

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)
        self.main_frame.rowconfigure(0, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, sticky='nsew')

        # Options frame
        self.display_frame = tk.Frame(self.main_frame)
        self.display_frame.grid(row=0, column=0, sticky='nsew')
        self.display_frame.columnconfigure(0, weight=1)
        self.display_frame.rowconfigure(0, weight=1)

        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.grid(row=0, column=1, sticky='nsew')

        row = 0
        self.batter_vis_label = tk.Label(self.options_frame, text='Batters')
        self.batter_vis_label.grid(row=row, column=0, sticky='ew')
        row += 1

        self.babip_button = tk.Button(self.options_frame, text='BABIP', width=40, command=display_babip_vis)
        self.babip_button.grid(row=row, column=0, sticky='nsew', padx=5, pady=5)
        row += 1

        self.hr_fb_button = tk.Button(self.options_frame, text='HR/BIP', width=40, command=display_hr_bip_vis)
        self.hr_fb_button.grid(row=row, column=0, sticky='nsew', padx=5, pady=5)
        row += 1

        self.k_rate_button = tk.Button(self.options_frame, text='K/600', width=40, command=display_k_rate_vis)
        self.k_rate_button.grid(row=row, column=0, sticky='nsew', padx=5, pady=5)
        row += 1

        self.bip_button = tk.Button(self.options_frame, text='BIP Rate', width=40, command=display_bip_rate_vis)
        self.bip_button.grid(row=row, column=0, sticky='nsew', padx=5, pady=5)
        row += 1




        #

        #


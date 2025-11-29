import tkinter as tk
from tkinter import ttk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.data_vis_scatter_frame_2d import DataVisScatterFrame2d
from utils.view_utils.data_vis_scatter_frame_3d import DataVisualScatterFrame3D
from utils.data_vis_utils.generate_babip_vis_df import generate_babip_vis_df
from utils.data_vis_utils.generate_hr_fb_vis_df import generate_hr_fb_vis
from utils.data_vis_utils.generate_bip_rate_df import generate_bip_rate_df


class DataVisualizationApp(tk.Toplevel):
    def __init__(self, selected_team=None):
        super().__init__()

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
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, sticky='nsew')

        babip_df = generate_babip_vis_df()
        self.babip_scatter_frame = DataVisScatterFrame2d(self.main_frame, df=babip_df)
        self.babip_scatter_frame.grid(row=0, column=0, sticky='nsew')

        hr_df = generate_hr_fb_vis()
        self.hr_scatter_frame = DataVisScatterFrame2d(self.main_frame, df=hr_df)
        self.hr_scatter_frame.grid(row=0, column=1, sticky='nsew')

        # bip_df = generate_bip_rate_df()
        # self.bip_scatter_frame = DataVisualScatterFrame3D(self.main_frame, df=bip_df)
        # self.bip_scatter_frame.grid(row=0, column=2, sticky='nsew')

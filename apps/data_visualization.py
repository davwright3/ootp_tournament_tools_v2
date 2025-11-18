import tkinter as tk
from tkinter import ttk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.data_vis_scatter_frame import DataVisScatterFrame
from utils.data_vis_utils.generate_babip_vis_df import generate_babip_vis_df


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
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, sticky='nsew')

        babip_df = generate_babip_vis_df()
        self.babip_scatter_frame = DataVisScatterFrame(self.main_frame, df=babip_df)
        self.babip_scatter_frame.grid(row=0, column=0, sticky='nsew')

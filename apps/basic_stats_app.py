"""
App for viewing basic hitting, pitching and team stats.
Loads a dataframe singleton for opening apps for specific categories.
"""
import tkinter as tk
import logging
import os
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.data_utils.select_load_stats_data_file import select_load_stats_data_file
from utils.view_utils.message_panel import MessagePanel
from utils.view_utils.team_select_frame import TeamSelectFrame
from utils.data_utils.card_list_store import card_list_store
from utils.log_utils.attach import attach_panel
from apps.batting_stats import BattingStatsApp
from apps.pitching_stats import PitchStatsApp
from apps.team_stats import TeamStatsApp
from apps.ratings_comparison import RatingsComparisonApp
from apps.data_visualization import DataVisualizationApp
from apps.batter_slideshow import BatterSlideshowApp
from apps.pitcher_slideshow import PitcherSlideshowApp



class BasicStatsApp(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)

        self.title("Basic Stats Views")
        self.geometry("1920x1080")

        def set_active_buttons(frame):
            buttons = []
            for widget in frame.winfo_children():
                if isinstance(widget, tk.Button):
                    buttons.append(widget)

            for button in buttons:
                if self.is_dataframe_loaded.get():
                    button.configure(state=tk.NORMAL)
                else:
                    button.configure(state=tk.DISABLED)

        # Variables for page
        self.data_file_select_var = tk.StringVar(value=None)
        self.dataframe_loaded_var = tk.StringVar(value="No file selected.")
        self.is_dataframe_loaded = tk.BooleanVar(value=False)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=0)

        self.columnconfigure(0, weight=1)

        # Main frames for page (header, footer, data file selection, app select)
        self.header_frame = Header(self)
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.select_data_file_frame = tk.Frame(
            self,
            bg='lightgray',
            relief='ridge',
            bd=3
        )
        self.select_data_file_frame.grid(row=1, column=0, sticky="nsew")

        self.select_data_file_frame.columnconfigure(0, weight=0)
        self.select_data_file_frame.columnconfigure(1, weight=1)
        self.select_data_file_frame.columnconfigure(2, weight=1)
        self.select_data_file_frame.columnconfigure(3, weight=1)

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=2, column=0, sticky="nsew")

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=3, column=0, sticky="nsew")

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Data for file selection frame
        self.data_file_select_button = tk.Button(
            self.select_data_file_frame,
            text="File Select",
            command=lambda: (
                select_load_stats_data_file(
                    self,
                    loaded_file_var=self.dataframe_loaded_var,
                    file_loaded_bool=self.is_dataframe_loaded,
                ),
                set_active_buttons(self.app_select_frame),
                self.team_select_entry.update_list()
            )
        )
        self.data_file_select_button.grid(row=0, column=0, sticky="e")

        self.data_file_select_info_label = tk.Label(
            self.select_data_file_frame,
            text="Select data file to load.  File must be CSV, and will be set as a DataFrame singleton.",
            font=("Arial", 12),
            bg="lightgray",
        )
        self.data_file_select_info_label.grid(row=0, column=1, sticky="w")

        self.valid_file_label = tk.Label(
            self.select_data_file_frame,
            textvariable=self.dataframe_loaded_var,
            font=("Arial", 12),
            bg="lightgray",
        )
        self.valid_file_label.grid(row=0, column=3, sticky="e")

        self.team_select_entry = TeamSelectFrame(self.select_data_file_frame)
        self.team_select_entry.grid(row=1, column=0, sticky="w", padx=(10, 0), pady=(5, 0), columnspan=3)

        # Data for main frame
        self.app_select_frame = tk.Frame(
            self.main_frame,
        )
        self.app_select_frame.grid(row=0, column=0, sticky="nsew")

        self.app_select_frame.columnconfigure(0, weight=1)
        self.app_select_frame.columnconfigure(1, weight=1)
        self.app_select_frame.columnconfigure(2, weight=1)
        self.app_select_frame.rowconfigure(0, weight=1)
        self.app_select_frame.rowconfigure(1, weight=1)
        self.app_select_frame.rowconfigure(2, weight=1)


        self.batting_app_select_button = tk.Button(
            self.app_select_frame,
            text="Batting Stats",
            command=self.open_batting_stats
        )
        self.batting_app_select_button.grid(row=0, column=0, sticky="nsew")

        self.pitching_app_select_button = tk.Button(
            self.app_select_frame,
            text="Pitching Stats",
            command=self.open_pitching_stats
        )
        self.pitching_app_select_button.grid(row=0, column=1, sticky="nsew")

        self.team_app_select_button = tk.Button(
            self.app_select_frame,
            text="Team Stats",
            command=self.open_team_stats
        )
        self.team_app_select_button.grid(row=0, column=2, sticky="nsew")

        self.ratings_comparison_app_select_button = tk.Button(
            self.app_select_frame,
            text="Ratings Comparison",
            command=open_ratings_comparison
        )
        self.ratings_comparison_app_select_button.grid(row=1, column=0, sticky="nsew")

        self.data_visualization_app_select_button = tk.Button(
            self.app_select_frame,
            text="Data Visualization",
            command=self.open_data_visualization
        )
        self.data_visualization_app_select_button.grid(row=1, column=1, sticky="nsew")

        self.batter_slideshow_button = tk.Button(
            self.app_select_frame,
            text='Batter Slideshow',
            command=open_batter_slideshow
        )
        self.batter_slideshow_button.grid(row=2, column=0, sticky="nsew")

        self.pitcher_slideshow_button = tk.Button(
            self.app_select_frame,
            text='Pitcher Slideshow',
            command=open_pitcher_slideshow
        )
        self.pitcher_slideshow_button.grid(row=2, column=1, sticky="nsew")

        self.message_panel = MessagePanel(self.main_frame, height=12)
        self.message_panel.grid(row=0, column=1, sticky="nsew")
        attach_panel(self.message_panel, 'apps.basic_stats_app')
        self.log = logging.getLogger("apps.basic_stats_app")
        self.log.info("Initializing Basic Stats App")

        set_active_buttons(self.app_select_frame)
        card_list_store.load_card_list()


    def open_batting_stats(self):
        team_select = self.team_select_entry.get_selected_team()
        BattingStatsApp(selected_team=team_select)

    def open_pitching_stats(self):
        team_select = self.team_select_entry.get_selected_team()
        PitchStatsApp(selected_team=team_select)

    def open_team_stats(self):
        team_select = self.team_select_entry.get_selected_team()
        TeamStatsApp(team_select=team_select)

    def open_data_visualization(self):
        team_select = self.team_select_entry.get_selected_team()
        DataVisualizationApp(selected_team=team_select)

def open_ratings_comparison():
    RatingsComparisonApp()

def open_batter_slideshow():
    BatterSlideshowApp()

def open_pitcher_slideshow():
    PitcherSlideshowApp()

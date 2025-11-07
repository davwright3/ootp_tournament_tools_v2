"""App for displaying basic team stats from loaded tournament file."""
import tkinter as tk
import pandas as pd
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.dataframe_table_frame import DataFrameTableFrame
from utils.view_utils.scrollable_frame import ScrollableFrame
from utils.view_utils.batting_stats_select_frame import BattingStatsSelectFrame
from utils.view_utils.pitcher_stats_select_frame import PitcherStatsSelectFrame
from utils.view_utils.min_team_games_frame import MinTeamGamesFrame
from apps.team_card import TeamCard
from utils.stats_utils.generate_basic_team_stats_df import generate_basic_team_stats_df

class TeamStatsApp(tk.Toplevel):
    def __init__(self, master=None, team_select=None):
        super().__init__(master)

        self.geometry('1920x1080')
        self.title('Team Stats')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)

        # Basic page setup
        self.header_frame = Header(
            self,
            app_name='Team Stats',
        )
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.footer_frame = Footer(
            self
        )
        self.footer_frame.grid(row=2, column=0, sticky="nsew")

        # Main frame setup
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)
        self.main_frame.rowconfigure(0, weight=1)

        stats_df = generate_basic_team_stats_df()
        self.stats_frame = DataFrameTableFrame(
            self.main_frame,
            df=stats_df,
            selected_team=team_select,
            on_row_double_click=self.open_team_card
        )
        self.stats_frame.grid(row=0, column=0, sticky="nsew")

        self.options_panel = tk.Frame(
            self.main_frame
        )
        self.options_panel.grid(row=0, column=1, sticky="nsew")
        self.options_panel.rowconfigure(0, weight=0)
        self.options_panel.rowconfigure(1, weight=1)
        self.options_panel.columnconfigure(0, weight=1)

        self.button_frame = tk.Frame(
            self.options_panel,
        )
        self.button_frame.grid(row=0, column=0, sticky="nsew")

        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=0)
        self.button_frame.columnconfigure(2, weight=1)

        self.load_button = tk.Button(
            self.button_frame,
            text='Reload',
            command=self.reload_data
        )
        self.load_button.grid(row=0, column=1, sticky="nsew")

        self.options_frame = ScrollableFrame(
            self.options_panel,
        )
        self.options_frame.grid(row=1, column=0, sticky="nsew")

        inner_frame = self.options_frame.inner
        row = 0

        self.min_team_games_frame = MinTeamGamesFrame(
            inner_frame,
        )
        self.min_team_games_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.batting_stats_select = BattingStatsSelectFrame(
            inner_frame,
        )
        self.batting_stats_select.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.pitching_stats_select = PitcherStatsSelectFrame(
            inner_frame
        )
        self.pitching_stats_select.grid(row=row, column=0, sticky="nsew")
        row += 1


    def reload_data(self):
        batting_stats_list = self.batting_stats_select.get_selected_stats()
        pitching_stats_list = self.pitching_stats_select.get_active_stats()
        min_games_select = self.min_team_games_frame.get_min_games()

        stats_df = generate_basic_team_stats_df(
            selected_batting_stats=batting_stats_list,
            selected_pitching_stats=pitching_stats_list,
            min_games=min_games_select,
        )
        self.stats_frame.set_dataframe(stats_df)

    def open_team_card(self, row: pd.Series):
        selected_team = row.get('ORG') if 'ORG' in row else None

        if selected_team is None:
            return
        else:
            TeamCard(selected_team=selected_team)
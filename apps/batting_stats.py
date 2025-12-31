"""
Main app for displaying batting stats for all players.

Opens a tkinter TopLevel app, and gets data from the
loaded data store to display in a custom frame for
displaying DataFrames.
"""
import tkinter as tk
from tkinter import ttk
import pandas as pd
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.stats_utils.generate_basic_batting_stats_df import generate_basic_batting_stats_df
from utils.view_utils.dataframe_table_frame import DataFrameTableFrame
from utils.data_utils.data_store import data_store
from utils.view_utils.table_formatters import fmt_leading_dot
from utils.view_utils.min_max_rating_frame import MinMaxFrame
from utils.view_utils.scrollable_frame import ScrollableFrame
from utils.view_utils.position_select_frame import PositionSelectFrame
from utils.view_utils.batting_stats_select_frame import BattingStatsSelectFrame
from utils.view_utils.general_info_select_frame import GeneralInfoFrame
from utils.view_utils.batting_side_select_frame import BattingSideSelectFrame
from utils.view_utils.min_plate_appearance_frame import MinPlateAppearanceFrame
from utils.view_utils.select_in_collection_frame import SelectInCollectionFrame
from utils.view_utils.set_cull_teams_limit_frame import SetCullTeamsFrame
from utils.view_utils.team_only_checkbox_frame import TeamOnlyCheckboxFrame
from utils.view_utils.search_frame import SearchFrame
from utils.view_utils.split_variants_frame import SplitVariantsFrame
from apps.batter_card import BatterCard
from utils.view_utils.data_cutoff_by_days_frame import DataCutoffByDaysFrame
from utils.view_utils.team_select_frame import TeamSelectFrame


class BattingStatsApp(tk.Toplevel):
    def __init__(self, selected_team=None):
        super().__init__()

        self.geometry('1920x1080')
        self.title('Batting Stats')
        self.selected_team = selected_team

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        self.header_frame = Header(self, app_name='Batting Stats App')
        self.header_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky='nsew')

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)
        self.main_frame.rowconfigure(0, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, columnspan=2, sticky='nsew')

        # Set up the options frame
        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.grid(row=0, column=1, sticky='nsew')

        self.options_frame.columnconfigure(0, weight=1)
        self.options_frame.rowconfigure(0, weight=0)
        self.options_frame.rowconfigure(1, weight=1)

        self.options_button_frame = ttk.Frame(self.options_frame)
        self.options_button_frame.grid(row=0, column=0, sticky='nsew')
        self.options_button_frame.columnconfigure(0, weight=1)
        self.options_button_frame.columnconfigure(1, weight=0)
        self.options_button_frame.columnconfigure(2, weight=1)

        self.load_data_button = tk.Button(
            self.options_button_frame,
            text='Reload',
            command=self.reload_data,
            width=5,
            height=1,
        )
        self.load_data_button.grid(row=0, column=1, ipadx=5, ipady=5, sticky='nsew')

        # Frame for the various user options to select
        self.options_select_frame = ScrollableFrame(
            self.options_frame,
            yscroll=True,
            xscroll=False,
            auto_width=True
        )
        self.options_select_frame.grid(row=1, column=0, sticky='nsew')

        inner_frame = self.options_select_frame.inner
        inner_frame.grid_columnconfigure(0, weight=1)
        inner_frame.rowconfigure(0, weight=0)
        inner_frame.rowconfigure(1, weight=0)
        inner_frame.rowconfigure(2, weight=0)
        inner_frame.rowconfigure(3, weight=1)

        item = 0
        print(data_store.get_tournament_type())
        if data_store.get_tournament_type() == 'daily':
            self.days_cutoff_frame = DataCutoffByDaysFrame(
                inner_frame,
            )
            self.days_cutoff_frame.grid(row=item, column=0, sticky='nsew')
            item += 1

        self.search_frame = SearchFrame(inner_frame)
        self.search_frame.grid(row=item, column=0, sticky='nsew')
        item += 1

        self.split_variants_frame = SplitVariantsFrame(
            inner_frame,
        )
        self.split_variants_frame.grid(row=item, column=0, sticky='nsew')
        item += 1

        self.min_max_frame = MinMaxFrame(inner_frame)
        self.min_max_frame.grid(row=item, column=0, sticky='ew')
        item += 1

        self.min_plate_app_frame = MinPlateAppearanceFrame(inner_frame)
        self.min_plate_app_frame.grid(row=item, column=0, sticky='ew')
        item += 1

        self.batting_side_frame = BattingSideSelectFrame(inner_frame)
        self.batting_side_frame.grid(row=item, column=0, sticky='ew')
        item += 1

        self.position_select_frame = PositionSelectFrame(inner_frame)
        self.position_select_frame.grid(row=item, column=0, sticky='ew')
        item += 1

        self.batting_stats_select_frame = BattingStatsSelectFrame(inner_frame)
        self.batting_stats_select_frame.grid(row=item, column=0, sticky='ew')
        item += 1

        self.general_info_select_frame = GeneralInfoFrame(inner_frame)
        self.general_info_select_frame.grid(row=item, column=0, sticky='ew')
        item += 1

        self.collection_only_frame = SelectInCollectionFrame(inner_frame)
        self.collection_only_frame.grid(row=item, column=0, sticky='ew')
        item += 1

        self.selected_team_only_frame = TeamOnlyCheckboxFrame(inner_frame)
        self.selected_team_only_frame.grid(row=item, column=0, sticky='ew')
        item += 1

        self.cull_teams_limit_frame = SetCullTeamsFrame(inner_frame)
        self.cull_teams_limit_frame.grid(row=item, column=0, sticky='ew')
        item += 1



        # Set up initial dataframe for the table
        stats_df = generate_basic_batting_stats_df()


        fmt = {
            'AVG': fmt_leading_dot(3, '.000'),
            'OBP': fmt_leading_dot(3, '.000'),
            'SLG': fmt_leading_dot(3, '.000'),
            'OPS': fmt_leading_dot(3, '.000'),
            'wOBA': fmt_leading_dot(3, '.000'),
            'HRrate': fmt_leading_dot(1, '.0'),
            'Krate': fmt_leading_dot(1, '.0'),
            'BBrate': fmt_leading_dot(1, '.0'),
            'SBrate': fmt_leading_dot(1, '.0'),
            'SBpct': fmt_leading_dot(3, '.000'),
            'WARrate': fmt_leading_dot(1, '.0')
        }

        self.dataframe_frame = DataFrameTableFrame(self.main_frame, df=stats_df, formatters=fmt, on_row_double_click=self.open_batter_card)
        self.dataframe_frame.grid(row=0, column=0, sticky='nsew')

    def reload_data(self):
        """Reload the data to the dataframe."""
        min_rating, max_rating = self.min_max_frame.get_min_max_rating()
        selected_position = self.position_select_frame.get_position_select()
        selected_stats = self.batting_stats_select_frame.get_selected_stats()
        selected_general_items = self.general_info_select_frame.get_selected_items()
        selected_batting_side = self.batting_side_frame.get_selected_side()
        min_plate_app = self.min_plate_app_frame.get_min_plate_app()
        collection_only_sel = self.collection_only_frame.get_collection_only_value()
        cull_teams_limit = self.cull_teams_limit_frame.get_cull_teams_limit()
        search_term = self.search_frame.get_search_term()
        split_variants_select = self.split_variants_frame.get_variant_split()
        num_cutoff_days = self.days_cutoff_frame.get_cutoff_days()
        
        if self.selected_team_only_frame.get_selected_team_bool():
            selected_team = self.selected_team
        else:
            selected_team = None
        stats_df = generate_basic_batting_stats_df(
            stat_list=selected_stats,
            position_select=selected_position,
            general_list=selected_general_items,
            min_value=min_rating,
            max_value=max_rating,
            bat_side_select=selected_batting_side,
            min_pa=min_plate_app,
            collection_only_select=collection_only_sel,
            cull_team_limit_select=cull_teams_limit,
            selected_search_term=search_term,
            variant_split_select=split_variants_select,
            team_select=selected_team,
            cutoff_days=num_cutoff_days
        )
        self.dataframe_frame.set_dataframe(stats_df)

    def open_batter_card(self, row: pd.Series):
        cid = int(row.get('CID')) if 'CID' in row else None
        team_select = self.selected_team
        BatterCard(cid, team_select)


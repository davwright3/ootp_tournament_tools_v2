"""Display pitching stats from CSV file."""
import tkinter as tk
import pandas as pd
from utils.data_utils.data_store import data_store
from utils.stats_utils.generate_basic_pitching_stats_df import generate_basic_pitching_stats
from utils.view_utils import pitcher_type_select_frame
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.table_formatters import fmt_leading_dot
from utils.view_utils.dataframe_table_frame import DataFrameTableFrame
from utils.view_utils.scrollable_frame import ScrollableFrame
from utils.view_utils.min_max_rating_frame import MinMaxFrame
from utils.view_utils.min_ip_frame import MinIPFrame
from utils.view_utils.pitcher_side_select_frame import PitcherSideSelectFrame
from utils.view_utils.pitcher_type_select_frame import PitcherTypeSelectFrame
from utils.view_utils.pitcher_stats_select_frame import PitcherStatsSelectFrame
from utils.view_utils.general_info_select_frame import GeneralInfoFrame
from utils.view_utils.select_in_collection_frame import SelectInCollectionFrame
from utils.view_utils.set_cull_teams_limit_frame import SetCullTeamsFrame
from utils.view_utils.search_frame import SearchFrame
from utils.view_utils.team_only_checkbox_frame import TeamOnlyCheckboxFrame
from utils.view_utils.split_variants_frame import SplitVariantsFrame
from utils.view_utils.data_cutoff_by_days_frame import DataCutoffByDaysFrame


class PitchStatsApp(tk.Toplevel):
    def __init__(self, selected_team=None):
        super().__init__()

        self.title("Pitching Stats")
        self.geometry("1920x1080")

        self.selected_team = selected_team

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)

        self.header_frame = Header(
            self,
            app_name="Pitching Stats",
        )
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)
        self.main_frame.rowconfigure(0, weight=1)

        self.footer_frame = Footer(
            self
        )
        self.footer_frame.grid(row=2, column=0, sticky="nsew")

        # Main Frame details
        fmt = {
            'ERA': fmt_leading_dot(2, '.00'),
            'FIP': fmt_leading_dot(2, '.00'),
            'WHIP': fmt_leading_dot(3, '.000'),
            'K%': fmt_leading_dot(3, '.000'),
            'BB%': fmt_leading_dot(3, '.000'),
            'K-BB': fmt_leading_dot(3, '.000'),
            'HR/9': fmt_leading_dot(1, '.0'),
            'SV%': fmt_leading_dot(3, '.000'),
            'SD:MD': fmt_leading_dot(2, '.00'),
            'IRS%': fmt_leading_dot(3, '.000'),
            'GB%': fmt_leading_dot(3, '.000'),
            'WAR/200': fmt_leading_dot(1, '.0'),
            'IP/G': fmt_leading_dot(1, '.0'),
            'QS%': fmt_leading_dot(3, '.000'),
            'oBABIP': fmt_leading_dot(3, '.000'),
        }
        self.stats_frame = DataFrameTableFrame(
            self.main_frame,
            formatters=fmt,
            on_row_double_click=self.open_pitcher_card
        )
        self.stats_frame.grid(row=0, column=0, sticky="nsew")

        self.options_frame = tk.Frame(
            self.main_frame,
        )
        self.options_frame.grid(row=0, column=1, sticky="nsew")

        self.options_frame.columnconfigure(0, weight=1)
        self.options_frame.rowconfigure(0, weight=0)
        self.options_frame.rowconfigure(1, weight=1)

        self.options_button_frame = tk.Frame(self.options_frame)
        self.options_button_frame.grid(row=0, column=0, sticky='nsew')
        self.options_button_frame.columnconfigure(0, weight=1)
        self.options_button_frame.columnconfigure(1, weight=0)
        self.options_button_frame.columnconfigure(2, weight=1)

        self.reload_button = tk.Button(
            self.options_button_frame,
            text="Reload",
            command=self.reload_data,
            width=5,
            height=1
        )
        self.reload_button.grid(row=0, column=1, sticky="nsew")

        self.settings_options_frame = ScrollableFrame(
            self.options_frame,
        )
        self.settings_options_frame.grid(row=1, column=0, sticky="nsew")

        inner_frame = self.settings_options_frame.inner

        inner_frame.grid_columnconfigure(0, weight=1)
        inner_frame.rowconfigure(0, weight=0)
        inner_frame.rowconfigure(1, weight=0)
        inner_frame.rowconfigure(2, weight=0)
        inner_frame.rowconfigure(3, weight=0)
        inner_frame.rowconfigure(4, weight=0)
        inner_frame.rowconfigure(5, weight=0)

        row = 0
        if data_store.get_tournament_type() == 'daily':
            self.date_cutoff_frame = DataCutoffByDaysFrame(
                inner_frame,
            )
            self.date_cutoff_frame.grid(row=row, column=0, sticky="nsew")
            row += 1

        self.search_frame = SearchFrame(
            inner_frame,
        )
        self.search_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.split_variants_frame = SplitVariantsFrame(
            inner_frame
        )
        self.split_variants_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.min_max_ratings_frame = MinMaxFrame(
            inner_frame,
        )
        self.min_max_ratings_frame.grid(row=row, column=0, sticky="ew")
        row += 1

        self.min_innings_frame = MinIPFrame(
            inner_frame
        )
        self.min_innings_frame.grid(row=row, column=0, sticky="ew")
        row += 1

        self.pitcher_side_select_frame = PitcherSideSelectFrame(
            inner_frame,
        )
        self.pitcher_side_select_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.pitcher_type_select_frame = PitcherTypeSelectFrame(
            inner_frame,
        )
        self.pitcher_type_select_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.pitcher_stats_select_frame = PitcherStatsSelectFrame(
            inner_frame,
        )
        self.pitcher_stats_select_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.general_items_frame = GeneralInfoFrame(
            inner_frame
        )
        self.general_items_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.collection_only_frame = SelectInCollectionFrame(
            inner_frame,
        )
        self.collection_only_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.selected_team_only_checkbox_frame = TeamOnlyCheckboxFrame(inner_frame)
        self.selected_team_only_checkbox_frame.grid(row=row, column=0, sticky="nsew")
        row += 1

        self.cull_teams_frame = SetCullTeamsFrame(
            inner_frame,
        )
        self.cull_teams_frame.grid(row=row, column=0, sticky="nsew")
        row += 1


        stats_df = generate_basic_pitching_stats()
        self.stats_frame.set_dataframe(stats_df)

    def reload_data(self):
        min_ip_select = self.min_innings_frame.get_min_innings()
        start_relief_cutoff_select = self.pitcher_type_select_frame.get_pitcher_type_cutoff()
        min_select, max_select = self.min_max_ratings_frame.get_min_max_rating()
        stat_list_select = self.pitcher_stats_select_frame.get_active_stats()
        general_list_select = self.general_items_frame.get_selected_items()
        throws_side_select = self.pitcher_side_select_frame.get_pitcher_side_select()
        pitcher_type_select = self.pitcher_type_select_frame.get_pitcher_type()
        collection_only_select = self.collection_only_frame.get_collection_only_value()
        cull_team_var_select = self.cull_teams_frame.get_cull_teams_limit()
        search_term = self.search_frame.get_search_term()
        variant_split_select = self.split_variants_frame.get_variant_split()
        selected_cutoff_days = self.date_cutoff_frame.get_cutoff_days()
        if self.selected_team_only_checkbox_frame.get_selected_team_bool():
            selected_team = self.selected_team
        else:
            selected_team = None

        stats = generate_basic_pitching_stats(
            min_ip=min_ip_select,
            start_relief_cutoff=start_relief_cutoff_select,
            min_value=min_select,
            max_value=max_select,
            stat_list=stat_list_select,
            general_list=general_list_select,
            throws_side_select=throws_side_select,
            pitcher_type_select=pitcher_type_select,
            collection_only_select=collection_only_select,
            cull_team_limit_select=cull_team_var_select,
            selected_search_term=search_term,
            selected_variant_split=variant_split_select,
            team_select=selected_team,
            cutoff_days=selected_cutoff_days,
        )
        self.stats_frame.set_dataframe(stats)

    def open_pitcher_card(self, row: pd.Series):
        from apps.pitcher_card import PitcherCard
        cid = int(row.get('CID')) if 'CID' in row else None
        selected_team = self.selected_team
        PitcherCard(cid, selected_team)

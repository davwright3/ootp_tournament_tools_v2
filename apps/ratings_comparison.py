"""App for comparing ratings of selected players."""
import tkinter as tk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.dataframe_table_frame import DataFrameTableFrame
from utils.view_utils.scrollable_frame import ScrollableFrame
from utils.view_utils.min_max_rating_frame import MinMaxFrame
from utils.view_utils.min_max_years import MinMaxYearsFrame
from utils.view_utils.ratings_select_frame import RatingsSelectFrame
from utils.stats_utils.generate_ratings_df import generate_ratings_df
from utils.view_utils.batter_rating_weights_frame import BatterWeightsFrame
from utils.view_utils.pitcher_rating_weights_frame import PitcherWeightsFrame
from utils.view_utils.defense_weights_frame import DefenseWeightsFrame
from utils.view_utils.baserunning_weights_frame import BaserunningWeightFrame
from utils.view_utils.position_select_frame import PositionSelectFrame


class RatingsComparisonApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Ratings Comparison")
        self.geometry("1920x1080")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)

        self.header_frame = Header(self)
        self.header_frame.grid(column=0, row=0, sticky='nsew')

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(column=0, row=1, sticky='nsew')

        self.footer_frame = Footer(self)
        self.footer_frame.grid(column=0, row=2, sticky='nsew')

        # Main frame sub-frames and setup
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)
        self.main_frame.rowconfigure(0, weight=1)

        self.dataview_frame = DataFrameTableFrame(self.main_frame)
        self.dataview_frame.grid(column=0, row=0, sticky='nsew')

        self.options_frame = tk.Frame(self.main_frame)
        self.options_frame.grid(column=1, row=0, sticky='nsew')

        # Setup for options frame
        self.options_frame.columnconfigure(0, weight=1)
        self.options_frame.rowconfigure(0, weight=0)
        self.options_frame.rowconfigure(1, weight=1)

        self.button_frame = tk.Frame(self.options_frame)
        self.button_frame.grid(column=0, row=0, sticky='nsew')
        self.button_frame.columnconfigure(0, weight=1)
        self.button_frame.columnconfigure(1, weight=0)
        self.button_frame.columnconfigure(2, weight=1)
        self.reload_button = tk.Button(
            self.button_frame,
            text="Reload",
            width=10,
            height=1,
            command=self.reload_data
        )
        self.reload_button.grid(column=1, row=0, sticky='nsew')

        self.option_selections_frame = ScrollableFrame(self.options_frame)
        self.option_selections_frame.grid(column=0, row=1, sticky='nsew')

        inner_frame = self.option_selections_frame.inner

        row = 0
        self.min_max_select = MinMaxFrame(inner_frame)
        self.min_max_select.grid(column=0, row=row, sticky='nsew')
        row += 1

        self.year_range_select = MinMaxYearsFrame(inner_frame)
        self.year_range_select.grid(column=0, row=row, sticky='nsew')
        row += 1

        self.rating_select_frame = RatingsSelectFrame(inner_frame)
        self.rating_select_frame.grid(column=0, row=row, sticky='nsew')
        row += 1

        self.bat_ratings_weight_frame = BatterWeightsFrame(inner_frame)
        self.bat_ratings_weight_frame.grid(column=0, row=row, sticky='nsew')
        row += 1

        self.pitch_ratings_weight_frame = PitcherWeightsFrame(inner_frame)
        self.pitch_ratings_weight_frame.grid(column=0, row=row, sticky='nsew')
        row += 1

        self.defense_weights_frame = DefenseWeightsFrame(inner_frame)
        self.defense_weights_frame.grid(column=0, row=row, sticky='nsew')
        row += 1

        self.baserunning_weight_frame = BaserunningWeightFrame(inner_frame)
        self.baserunning_weight_frame.grid(column=0, row=row, sticky='nsew')
        row += 1

        self.position_select_frame = PositionSelectFrame(inner_frame)
        self.position_select_frame.grid(column=0, row=row, sticky='nsew')
        row += 1

        ratings_df = generate_ratings_df()
        self.dataview_frame.set_dataframe(ratings_df)

    def reload_data(self):
        selected_min_year, selected_max_year = self.year_range_select.get_min_max_years()
        selected_min_rating, selected_max_rating = self.min_max_select.get_min_max_rating()
        selected_ratings = self.rating_select_frame.get_active_ratings()
        selected_batter_weights = self.bat_ratings_weight_frame.get_batter_rating_weights()
        selected_pitcher_weights = self.pitch_ratings_weight_frame.get_pitcher_rating_weights()
        selected_defense_weights = self.defense_weights_frame.get_defense_ratings_weights()
        selected_baserunning_weights = self.baserunning_weight_frame.get_baserunning_weights()
        selected_position = self.position_select_frame.get_position_select()
        ratings_df = generate_ratings_df(
            min_year=selected_min_year,
            max_year=selected_max_year,
            min_rating=selected_min_rating,
            max_rating=selected_max_rating,
            selected_ratings_list=selected_ratings,
            batter_weights=selected_batter_weights,
            pitcher_weights=selected_pitcher_weights,
            defense_weights=selected_defense_weights,
            baserunning_weights=selected_baserunning_weights,
            selected_position=selected_position,
        )
        self.dataview_frame.set_dataframe(ratings_df)
        del ratings_df



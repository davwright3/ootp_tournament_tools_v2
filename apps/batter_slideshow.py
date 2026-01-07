import tkinter as tk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils import program_fonts as fonts
from utils.stats_utils.generate_batter_slide_df import generate_batter_slide_df
from utils.view_utils.player_card_bat_ratings_frame import BatterRatingFrame
from utils.view_utils.player_overall_rating_label import PlayerOverallRatingLabel
from utils.view_utils.bats_throws_label import BatsThrowsLabel
from utils.view_utils.player_card_defense_ratings_frame import PlayerCardDefenseRatingsFrame
from utils.view_utils.batter_profile_frame import BatterProfileFrame
from utils.view_utils.batter_slideshow_stats_frame import BatterSlideshowStatsFrame
from utils.view_utils.baserunning_profile_frame import BaserunningProfileFrame


class BatterSlideshowApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry('1920x1080')
        self.title('Batting Leaders')

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=0)
        self.columnconfigure(0, weight=1)

        self.header_frame = Header(
            self,
            app_name="Batting Leaders"
        )
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew")

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.columnconfigure(3, weight=1)

        self.main_frame.rowconfigure(0, weight=0)
        self.main_frame.rowconfigure(1, weight=0)
        self.main_frame.rowconfigure(2, weight=0)
        self.main_frame.rowconfigure(3, weight=0)
        self.main_frame.rowconfigure(4, weight=0)
        self.main_frame.rowconfigure(5, weight=0)
        self.main_frame.rowconfigure(6, weight=0)
        self.main_frame.rowconfigure(7, weight=0)
        self.main_frame.rowconfigure(8, weight=1)

        self.footer_frame = Footer(self)
        self.footer_frame.grid(row=2, column=0, sticky="nsew")

        self.rank_var = tk.IntVar(value=5)
        self.updating = False

        row = 0
        self.player_title = tk.Label(self.main_frame, text=f'{self.rank_var.get()}:', font=fonts.slideshow_header_font)
        self.player_title.grid(row=row, column=0, sticky="nsew", columnspan=4)
        row += 1

        self.slide_df = generate_batter_slide_df(position_select='LearnC')
        if len(self.slide_df) >= self.rank_var.get():
            self.batter_df = self.slide_df.iloc[[4]]
        else:
            try:
                self.batter_df = self.slide_df.iloc[len(self.slide_df) - 1]
            except IndexError:
                self.player_title.config(text='No batters available')

        self.bat_side_label = BatsThrowsLabel(self.main_frame, label_type='Bats', side_id=self.batter_df.iloc[0]['Bats'])
        self.bat_side_label.grid(row=row, column=0, sticky="nsew")

        self.player_value_label = PlayerOverallRatingLabel(self.main_frame, self.batter_df.iloc[0]['Val'])
        self.player_value_label.grid(row=row, column=1, sticky="nsew")

        self.throws_label = BatsThrowsLabel(self.main_frame, 'Throws', self.batter_df.iloc[0]['Throws'])
        self.throws_label.grid(row=row, column=2, sticky="nsew")
        row += 1

        self.batting_ratings_frame = BatterRatingFrame(self.main_frame, self.batter_df)
        self.batting_ratings_frame.grid(row=row, column=0, sticky="nsew")

        self.defense_positions_frame = PlayerCardDefenseRatingsFrame(self.main_frame, self.batter_df)
        self.defense_positions_frame.grid(row=row, column=1, sticky="nsew")

        self.batter_profile_frame = BatterProfileFrame(self.main_frame, self.batter_df)
        self.batter_profile_frame.grid(row=row, column=2, sticky="nsew")

        self.baserunning_profile_frame = BaserunningProfileFrame(self.main_frame, self.batter_df)
        self.baserunning_profile_frame.grid(row=row, column=3, sticky="nsew")
        row += 1

        self.batter_stats_frame = BatterSlideshowStatsFrame(self.main_frame, self.batter_df)
        self.batter_stats_frame.grid(row=row, column=0, sticky="nsew", columnspan=4)
        row += 1

        self.previous_button = tk.Button(self.main_frame, text="PREVIOUS",
                                         command=self.previous_batter)
        self.previous_button.grid(row=row, column=0, sticky="nsew")

        self.next_button = tk.Button(self.main_frame, text="NEXT", command=self.next_batter)
        self.next_button.grid(row=row, column=2, sticky="nsew")
        row += 1

        self.catcher_button = tk.Button(self.main_frame, text="CATCH", command= lambda: self.change_position(position='LearnC'))
        self.catcher_button.grid(row=row, column=0, sticky="nsew")

        self.first_base_button = tk.Button(self.main_frame, text='1B', command= lambda: self.change_position(position='Learn1B'))
        self.first_base_button.grid(row=row, column=1, sticky="nsew")

        self.second_base_button = tk.Button(self.main_frame, text='2B', command= lambda: self.change_position(position='Learn2B'))
        self.second_base_button.grid(row=row, column=2, sticky="nsew")
        row += 1

        self.third_base_button = tk.Button(self.main_frame, text='3B', command= lambda: self.change_position(position='Learn3B'))
        self.third_base_button.grid(row=row, column=0, sticky="nsew")

        self.shortstop_button = tk.Button(self.main_frame, text='SS', command= lambda: self.change_position(position='LearnSS'))
        self.shortstop_button.grid(row=row, column=1, sticky="nsew")

        self.left_field_button = tk.Button(self.main_frame, text='LF', command= lambda: self.change_position(position='LearnLF'))
        self.left_field_button.grid(row=row, column=2, sticky="nsew")
        row += 1

        self.center_field_button = tk.Button(self.main_frame, text='CF', command= lambda: self.change_position(position='LearnCF'))
        self.center_field_button.grid(row=row, column=0, sticky="nsew")

        self.right_field_button = tk.Button(self.main_frame, text='RF', command= lambda: self.change_position(position='LearnRF'))
        self.right_field_button.grid(row=row, column=1, sticky="nsew")

        self.all_batters_button = tk.Button(self.main_frame, text='ALL', command= lambda: self.change_position(position=None))
        self.all_batters_button.grid(row=row, column=2, sticky="nsew")

        if len(self.slide_df) >= self.rank_var.get():
            self.update_batter(self.rank_var.get())

    def update_batter(self, rank):
        if not self.updating:
            self.updating = True
            num_qualifiers = len(self.slide_df)
            self.batter_df = self.slide_df.iloc[[rank - 1]]
            self.player_title.configure(text=f"{self.rank_var.get()}: {self.batter_df.iloc[0]['Title']}")
            self.player_value_label.update_overall_rating_label(self.batter_df.iloc[0]['Val'])
            self.bat_side_label.update_rating('Bats', self.batter_df.iloc[0]['Bats'])
            self.throws_label.update_rating('Throws', self.batter_df.iloc[0]['Throws'])
            self.batting_ratings_frame.update_frame(self.batter_df)
            self.baserunning_profile_frame.update_frame(self.batter_df)
            self.defense_positions_frame.update_frame(self.batter_df)
            self.batter_profile_frame.update_frame(self.batter_df)
            self.batter_stats_frame.update_batter(self.batter_df, quals=num_qualifiers)
            self.updating = False

    def next_batter(self):
        if self.rank_var.get() > 1:
            self.rank_var.set(self.rank_var.get() - 1)
            self.update_batter(self.rank_var.get())

    def previous_batter(self):
        if self.rank_var.get() < len(self.slide_df):
            self.rank_var.set(self.rank_var.get() + 1)
            self.update_batter(self.rank_var.get())

    def change_position(self, position):
        self.slide_df = generate_batter_slide_df(position_select=position)
        if len(self.slide_df) > 4:
            self.rank_var.set(5)
            self.update_batter(self.rank_var.get())
        else:
            self.rank_var.set(len(self.slide_df) - 1)
            self.update_batter(self.rank_var.get())

import tkinter as tk


class BatterSlideshowStatsFrame(tk.Frame):
    def __init__(self, parent, batter_df):
        super().__init__(parent)

        self.average_label = tk.Label(self, text="AVG:")
        self.average_label.grid(row=0, column=0, sticky="nsew")

        self.obp_label = tk.Label(self, text="OBP:")
        self.obp_label.grid(row=1, column=0, sticky="nsew")

        self.slg_label = tk.Label(self, text="SLG:")
        self.slg_label.grid(row=2, column=0, sticky="nsew")

        self.ops_label = tk.Label(self, text="OPS:")
        self.ops_label.grid(row=3, column=0, sticky="nsew")

        self.woba_label = tk.Label(self, text="wOBA:")
        self.woba_label.grid(row=4, column=0, sticky="nsew")

        self.hr_label = tk.Label(self, text="HR:")
        self.hr_label.grid(row=0, column=1, sticky="nsew")

        self.bb_label = tk.Label(self, text="BB:")
        self.bb_label.grid(row=1, column=1, sticky="nsew")

        self.k_label = tk.Label(self, text="K:")
        self.k_label.grid(row=2, column=1, sticky="nsew")

        self.rc_label = tk.Label(self, text="RC:")
        self.rc_label.grid(row=3, column=1, sticky="nsew")

        self.war_label = tk.Label(self, text="WAR:")
        self.war_label.grid(row=4, column=1, sticky="nsew")

        self.sb_label = tk.Label(self, text="SB:")
        self.sb_label.grid(row=0, column=2, sticky="nsew")

        self.sb_pct_label = tk.Label(self, text="SB PCT:")
        self.sb_pct_label.grid(row=1, column=2, sticky="nsew")

        self.zr_label = tk.Label(self, text="ZR:")
        self.zr_label.grid(row=2, column=2, sticky="nsew")

        self.fld_pct_label = tk.Label(self, text="FLD PCT:")
        self.fld_pct_label.grid(row=3, column=2, sticky="nsew")

        self.pa_label = tk.Label(self, text="PA:")
        self.pa_label.grid(row=4, column=2, sticky="nsew")

        self.catch_label = tk.Label(self, text="Catch:")
        self.catch_label.grid(row=0, column=3, sticky="nsew")

        self.infield_label = tk.Label(self, text="INFIELD:")
        self.infield_label.grid(row=1, column=3, sticky="nsew")

        self.outfield_label = tk.Label(self, text="OUTFIELD:")
        self.outfield_label.grid(row=2, column=3, sticky="nsew")

        self.baserunning_label = tk.Label(self, text="Baserunning:")
        self.baserunning_label.grid(row=3, column=3, sticky="nsew")

        self.update_batter(batter_df)



    def update_batter(self, batter_df):
        self.average_label.configure(text=f'AVG: {batter_df.iloc[0]['AVG']} ( {int(batter_df.iloc[0]['avg_rank'])} )')
        self.obp_label.configure(text=f'OBP: {batter_df.iloc[0]['OBP']} ( {batter_df.iloc[0]['obp_rank']} )')
        self.slg_label.configure(text=f'SLG: {batter_df.iloc[0]['SLG']} ( {batter_df.iloc[0]['slg_rank']} )')
        self.ops_label.configure(text=f'OPS: {batter_df.iloc[0]['OPS']} ( {batter_df.iloc[0]['ops_rank']} )')
        self.woba_label.configure(text=f'wOBA: {batter_df.iloc[0]['wOBA']} ( {batter_df.iloc[0]['woba_rank']} )')
        self.hr_label.configure(text=f'HR/600: {batter_df.iloc[0]['HRrate']} ( {batter_df.iloc[0]['hr_rate_rank']} )')
        self.bb_label.configure(text=f'BB/600: {batter_df.iloc[0]['BBrate']} ( {batter_df.iloc[0]['bb_rate_rank']} )')
        self.k_label.configure(text=f'K/600: {batter_df.iloc[0]['Krate']} ( {batter_df.iloc[0]['k_rate_rank']} )')
        self.rc_label.configure(text=f'RC/600: {batter_df.iloc[0]['RCrate']} ( {batter_df.iloc[0]['rc_rate_rank']} )')
        self.war_label.configure(text=f'WAR/600: {batter_df.iloc[0]['WARrate']} ( {batter_df.iloc[0]['war_rate_rank']} )')
        self.sb_label.configure(text=f'SB/600: {batter_df.iloc[0]['SBrate']} ( {batter_df.iloc[0]['sb_rate_rank']} )')
        self.sb_pct_label.configure(text=f'SB%: {batter_df.iloc[0]['SBpct']} ( {batter_df.iloc[0]['sb_pct_rank']} )')
        self.zr_label.configure(text=f'ZR/600: {batter_df.iloc[0]['ZRrate']} ( {batter_df.iloc[0]['zr_rank']} )')
        self.fld_pct_label.configure(text=f'Fld%: {batter_df.iloc[0]['Fld%']} ( {batter_df.iloc[0]['fld_pct_rank']} )')
        self.pa_label.configure(text=f'PA: {batter_df.iloc[0]['PA']} ( {batter_df.iloc[0]['pa_rank']} )')
        self.catch_label.configure(text=f'Catch: {batter_df.iloc[0]['catch_score']} ( {batter_df.iloc[0]['catch_rank']} )')
        self.infield_label.configure(text=f'Infield: {batter_df.iloc[0]['infield_score']} ( {batter_df.iloc[0]['infield_rank']} )')
        self.outfield_label.configure(text=f'Outfield: {batter_df.iloc[0]['outfield_score']} ( {batter_df.iloc[0]['outfield_rank']} )')
        self.baserunning_label.configure(text=f'Baserunning: {batter_df.iloc[0]['baserunning_score']} ( {batter_df.iloc[0]['baserunning_rank']} )')
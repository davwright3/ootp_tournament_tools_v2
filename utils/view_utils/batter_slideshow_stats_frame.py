import tkinter as tk
from tkinter import ttk
from utils.view_utils import program_fonts as fonts
from utils.view_utils.open_bref import open_bref

LABEL_PADX = 5
LABEL_PADY = 5
SEP_PADX = 10
LABEL_STICKY = 'e'

class BatterSlideshowStatsFrame(tk.Frame):
    def __init__(self, parent, batter_df, quals=0):
        super().__init__(parent, relief='groove', bd=5)

        self.columnconfigure(1, minsize=400)
        self.columnconfigure(3, minsize=400)
        self.columnconfigure(5, minsize=400)
        self.columnconfigure(7, minsize=400)

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=1)

        self.bref_id = tk.StringVar(value="")


        self.average_label = tk.Label(self, text="AVG:", font=fonts.slideshow_label_font)
        self.average_label.grid(row=0, column=1, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.obp_label = tk.Label(self, text="OBP:", font=fonts.slideshow_label_font)
        self.obp_label.grid(row=1, column=1, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.slg_label = tk.Label(self, text="SLG:", font=fonts.slideshow_label_font)
        self.slg_label.grid(row=2, column=1, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.ops_label = tk.Label(self, text="OPS:", font=fonts.slideshow_label_font)
        self.ops_label.grid(row=3, column=1, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.woba_label = tk.Label(self, text="wOBA:", font=fonts.slideshow_label_font)
        self.woba_label.grid(row=4, column=1, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.woba_score_label = tk.Label(self, text="wOBA:", font=fonts.slideshow_label_font)
        self.woba_score_label.grid(row=5, column=1, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        ttk.Separator(
            self,
            orient='vertical').grid(
            row=0,
            column=2,
            sticky="ns",
            rowspan=6,
            padx=SEP_PADX
        )

        self.hr_label = tk.Label(self, text="HR:", font=fonts.slideshow_label_font)
        self.hr_label.grid(row=0, column=3, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.bb_label = tk.Label(self, text="BB:", font=fonts.slideshow_label_font)
        self.bb_label.grid(row=1, column=3, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.k_label = tk.Label(self, text="K:", font=fonts.slideshow_label_font)
        self.k_label.grid(row=2, column=3, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.rc_label = tk.Label(self, text="RC:", font=fonts.slideshow_label_font)
        self.rc_label.grid(row=3, column=3, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.war_label = tk.Label(self, text="WAR:", font=fonts.slideshow_label_font)
        self.war_label.grid(row=4, column=3, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        ttk.Separator(
            self,
            orient='vertical').grid(
            row=0,
            column=4,
            sticky="ns",
            rowspan=6,
            padx=SEP_PADX
        )

        self.sb_label = tk.Label(self, text="SB:", font=fonts.slideshow_label_font)
        self.sb_label.grid(row=0, column=5, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.sb_pct_label = tk.Label(self, text="SB PCT:", font=fonts.slideshow_label_font)
        self.sb_pct_label.grid(row=1, column=5, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.zr_label = tk.Label(self, text="ZR:", font=fonts.slideshow_label_font)
        self.zr_label.grid(row=2, column=5, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.fld_pct_label = tk.Label(self, text="FLD PCT:", font=fonts.slideshow_label_font)
        self.fld_pct_label.grid(row=3, column=5, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.pa_label = tk.Label(self, text="PA:", font=fonts.slideshow_label_font)
        self.pa_label.grid(row=4, column=5, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.variant_label = tk.Label(self, text="VARIANT:", font=fonts.slideshow_label_font)
        self.variant_label.grid(row=5, column=5, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        ttk.Separator(
            self,
            orient='vertical').grid(
            row=0,
            column=6,
            sticky="ns",
            rowspan=6,
            padx=SEP_PADX
        )

        self.catch_label = tk.Label(self, text="Catch:", font=fonts.slideshow_label_font)
        self.catch_label.grid(row=0, column=7, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.infield_label = tk.Label(self, text="INFIELD:", font=fonts.slideshow_label_font)
        self.infield_label.grid(row=1, column=7, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.outfield_label = tk.Label(self, text="OUTFIELD:", font=fonts.slideshow_label_font)
        self.outfield_label.grid(row=2, column=7, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.baserunning_label = tk.Label(self, text="Baserunning:", font=fonts.slideshow_label_font)
        self.baserunning_label.grid(row=3, column=7, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.total_label = tk.Label(self, text="Total:", font=fonts.slideshow_label_font)
        self.total_label.grid(row=4, column=7, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.quals_label = tk.Label(self, text="Quals:", font=fonts.slideshow_label_font)
        self.quals_label.grid(row=5, column=7, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.bref_button = tk.Button(self, text="B-Ref", command=lambda: open_bref(self.bref_id.get()))
        self.bref_button.grid(row=0, column=8, sticky=LABEL_STICKY, pady=LABEL_PADY, padx=LABEL_PADX)

        self.update_batter(batter_df, quals)



    def update_batter(self, batter_df, quals):
        self.average_label.configure(text=f"AVG: {batter_df.iloc[0]['AVG']} ( {int(batter_df.iloc[0]['avg_rank'])} )")
        self.obp_label.configure(text=f"OBP: {batter_df.iloc[0]['OBP']} ( {batter_df.iloc[0]['obp_rank']} )")
        self.slg_label.configure(text=f"SLG: {batter_df.iloc[0]['SLG']} ( {batter_df.iloc[0]['slg_rank']} )")
        self.ops_label.configure(text=f"OPS: {batter_df.iloc[0]['OPS']} ( {batter_df.iloc[0]['ops_rank']} )")
        self.woba_label.configure(text=f"wOBA: {batter_df.iloc[0]['wOBA']} ( {batter_df.iloc[0]['woba_rank']} )")
        self.woba_score_label.configure(text=f"wOBA Score: {batter_df.iloc[0]['woba_score']}")
        self.hr_label.configure(text=f"HR/600: {batter_df.iloc[0]['HRrate']} ( {batter_df.iloc[0]['hr_rate_rank']} )")
        self.bb_label.configure(text=f"BB/600: {batter_df.iloc[0]['BBrate']} ( {batter_df.iloc[0]['bb_rate_rank']} )")
        self.k_label.configure(text=f"K/600: {batter_df.iloc[0]['Krate']} ( {batter_df.iloc[0]['k_rate_rank']} )")
        self.rc_label.configure(text=f"RC/600: {batter_df.iloc[0]['RCrate']} ( {batter_df.iloc[0]['rc_rate_rank']} )")
        self.war_label.configure(text=f"WAR/600: {batter_df.iloc[0]['WARrate']} ( {batter_df.iloc[0]['war_rate_rank']} )")
        self.sb_label.configure(text=f"SB/600: {batter_df.iloc[0]['SBrate']} ( {batter_df.iloc[0]['sb_rate_rank']} )")
        self.sb_pct_label.configure(text=f"SB%: {batter_df.iloc[0]['SBpct']} ( {batter_df.iloc[0]['sb_pct_rank']} )")
        self.zr_label.configure(text=f"ZR/600: {batter_df.iloc[0]['ZRrate']} ( {batter_df.iloc[0]['zr_rank']} )")
        self.fld_pct_label.configure(text=f"Fld%: {batter_df.iloc[0]['Fld%']} ( {batter_df.iloc[0]['fld_pct_rank']} )")
        self.pa_label.configure(text=f"PA: {batter_df.iloc[0]['PA']} ( {batter_df.iloc[0]['pa_rank']} )")
        self.variant_label.configure(text=f"Var: {batter_df.iloc[0]['VLvl']}")
        self.catch_label.configure(text=f"Catch: {batter_df.iloc[0]['catch_score']} ( {batter_df.iloc[0]['catch_rank']} )")
        self.infield_label.configure(text=f"Infield: {batter_df.iloc[0]['infield_score']} ( {batter_df.iloc[0]['infield_rank']} )")
        self.outfield_label.configure(text=f"Outfield: {batter_df.iloc[0]['outfield_score']} ( {batter_df.iloc[0]['outfield_rank']} )")
        self.baserunning_label.configure(text=f"Baserunning: {batter_df.iloc[0]['baserunning_score']} ( {batter_df.iloc[0]['baserunning_rank']} )")
        self.total_label.configure(text=f"Total: {batter_df.iloc[0]['total_score']} ( {batter_df.iloc[0]['total_rank']} )")
        self.quals_label.configure(text=f"Qualifed: {quals}")
        self.bref_id.set(batter_df.iloc[0]['brefid'])

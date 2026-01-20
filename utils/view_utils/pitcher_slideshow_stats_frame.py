import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Separator
from utils.view_utils.open_bref import open_bref

from utils.view_utils import program_fonts as fonts


class PitcherSlideshowStatsFrame(tk.Frame):
    def __init__(self, parent, player_df, numquals=0):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=0)
        self.columnconfigure(4, weight=1)

        self.bref_id = tk.StringVar(value='')

        self.innings_pitched_label = tk.Label(self, text="IP", font=fonts.slideshow_label_font)
        self.innings_pitched_label.grid(row=0, column=0, sticky='e')

        self.fip_label = tk.Label(self, text="FIP", font=fonts.slideshow_label_font)
        self.fip_label.grid(row=1, column=0, sticky='e')

        self.era_label = tk.Label(self, text="ERA", font=fonts.slideshow_label_font)
        self.era_label.grid(row=2, column=0, sticky='e')

        self.whip_label = tk.Label(self, text="WHIP", font=fonts.slideshow_label_font)
        self.whip_label.grid(row=3, column=0, sticky='e')

        self.gb_pct_label = tk.Label(self, text="GB%", font=fonts.slideshow_label_font)
        self.gb_pct_label.grid(row=4, column=0, sticky='e')

        self.qs_pct_label = tk.Label(self, text="QS%", font=fonts.slideshow_label_font)
        self.qs_pct_label.grid(row=5, column=0, sticky='e')

        ttk.Separator(self, orient='vertical').grid(row=0, column=1, rowspan=6, sticky='ns')

        self.k_min_bb_label = tk.Label(self, text="K-BB%", font=fonts.slideshow_label_font)
        self.k_min_bb_label.grid(row=0, column=2, sticky='nsew')

        self.k_pct_label = tk.Label(self, text="K%", font=fonts.slideshow_label_font)
        self.k_pct_label.grid(row=1, column=2, sticky='nsew')

        self.bb_pct_label = tk.Label(self, text="BB%", font=fonts.slideshow_label_font)
        self.bb_pct_label.grid(row=2, column=2, sticky='nsew')

        self.hr_pct_label = tk.Label(self, text="HR%", font=fonts.slideshow_label_font)
        self.hr_pct_label.grid(row=3, column=2, sticky='nsew')

        self.hr_rate_label = tk.Label(self, text="HR/9", font=fonts.slideshow_label_font)
        self.hr_rate_label.grid(row=4, column=2, sticky='nsew')

        self.obabip_label = tk.Label(self, text="OBABIP", font=fonts.slideshow_label_font)
        self.obabip_label.grid(row=5, column=2, sticky='nsew')

        ttk.Separator(self, orient='vertical').grid(row=0, column=3, rowspan=6, sticky='ns')

        self.sd_md_label = tk.Label(self, text="SD/MD:", font=fonts.slideshow_label_font)
        self.sd_md_label.grid(row=0, column=4, sticky='w')

        self.irs_pct_label = tk.Label(self, text="IRS%", font=fonts.slideshow_label_font)
        self.irs_pct_label.grid(row=1, column=4, sticky='w')

        self.sv_pct_label = tk.Label(self, text="SV%", font=fonts.slideshow_label_font)
        self.sv_pct_label.grid(row=2, column=4, sticky='w')

        self.ip_game_label = tk.Label(self, text="IP", font=fonts.slideshow_label_font)
        self.ip_game_label.grid(row=3, column=4, sticky='w')

        self.score_label = tk.Label(self, text="Score:", font=fonts.slideshow_label_font)
        self.score_label.grid(row=4, column=4, sticky='w')

        self.qualifiers_label = tk.Label(self, text="Qual:", font=fonts.slideshow_label_font)
        self.qualifiers_label.grid(row=5, column=4, sticky='w')

        self.variant_label = tk.Label(self, text="Variant:", font=fonts.slideshow_label_font)
        self.variant_label.grid(row=6, column=4, sticky='w')

        self.bref_button = tk.Button(self, text="B-Ref", command=lambda: open_bref(self.bref_id.get()))
        self.bref_button.grid(row=0, column=5, sticky='w')

        self.update_frame(player_df, num_quals=numquals)



    def update_frame(self, player_df, num_quals):
        self.innings_pitched_label.configure(text=f"IP: {player_df.iloc[0]['IPC']}")
        self.fip_label.configure(text=f"FIP: {player_df.iloc[0]['FIP']} ( {player_df.iloc[0]['fip_rank']} )")
        self.era_label.configure(text=f"ERA: {player_df.iloc[0]['ERA']} ( {player_df.iloc[0]['era_rank']} )")
        self.whip_label.configure(text=f"WHIP: {player_df.iloc[0]['WHIP']} ( {player_df.iloc[0]['whip_rank']} )")
        self.gb_pct_label.configure(text=f"GBP: {player_df.iloc[0]['GB%']} ( {player_df.iloc[0]['gb_pct_rank']} )")
        self.qs_pct_label.configure(text=f"QS: {player_df.iloc[0]['QS%']} ( {player_df.iloc[0]['qs_pct_rank']} )")
        self.k_min_bb_label.configure(text=f"K-BB%: {player_df.iloc[0]['K-BB']} ( {player_df.iloc[0]['k_minus_bb_rank']} )")
        self.k_pct_label.configure(text=f"K%: {player_df.iloc[0]['K%']} ( {player_df.iloc[0]['k_pct_rank']} )")
        self.bb_pct_label.configure(text=f"BB%: {player_df.iloc[0]['BB%']} ( {player_df.iloc[0]['bb_pct_rank']} )")
        self.hr_pct_label.configure(text=f"HR%: {player_df.iloc[0]['HR%']} ( {player_df.iloc[0]['hr_pct_rank']} )")
        self.hr_rate_label.configure(text=f"HR/9: {player_df.iloc[0]['HR/9']} ( {player_df.iloc[0]['hr_per_9_rank']} )")
        self.obabip_label.configure(text=f"OBABIP: {player_df.iloc[0]['oBABIP']} ( {player_df.iloc[0]['obabip_rank']} )")
        self.sd_md_label.configure(text=f"SD/MD: {player_df.iloc[0]['SD/MD']} ( {player_df.iloc[0]['sd_md_rank']} )")
        self.irs_pct_label.configure(text=f"IRS%: {player_df.iloc[0]['IRS%']} ( {player_df.iloc[0]['irs_pct_rank']} )")
        self.sv_pct_label.configure(text=f"SV%: {player_df.iloc[0]['SV%']} ( {player_df.iloc[0]['sv_pct_rank']} )")
        self.ip_game_label.configure(text=f"IP/G: {player_df.iloc[0]['IP/G']} ( {player_df.iloc[0]['ip_game_rank']} )")
        self.score_label.configure(text=f"Score: {player_df.iloc[0]['pit_score']} ( {player_df.iloc[0]['score_rank']} )")
        self.qualifiers_label.configure(text=f'Qual: {num_quals}')
        self.variant_label.configure(text=f"Variant: {player_df.iloc[0]['VLvl']}")
        self.bref_id.set(player_df.iloc[0]['brefid'])


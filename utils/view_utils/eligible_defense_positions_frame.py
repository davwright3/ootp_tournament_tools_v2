import tkinter as tk
from utils.view_utils import program_fonts as fonts


class EligibleDefensePositionsFrame(tk.Frame):
    def __init__(self, parent, df):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.update_frame(df)

        # positions = [
        #     ('C', df.iloc[0]['LearnC']),
        #     ('1B', df.iloc[0]['Learn1B']),
        #     ('2B', df.iloc[0]['Learn2B']),
        #     ('3B', df.iloc[0]['Learn3B']),
        #     ('SS', df.iloc[0]['LearnSS']),
        #     ('LF', df.iloc[0]['LearnLF']),
        #     ('CF', df.iloc[0]['LearnCF']),
        #     ('RF', df.iloc[0]['LearnRF']),
        # ]
        #
        # class EligibilityFrame(tk.Frame):
        #     def __init__(self, master, position_string, sel_eligibility):
        #         super().__init__(master)
        #         self.columnconfigure(0, weight=1)
        #         self.columnconfigure(1, weight=1)
        #
        #         self.pos_label = tk.Label(
        #             self, text=position, font=fonts.basic_font, width=3)
        #         self.pos_label.grid(row=0, column=0, sticky='ew')
        #
        #         if sel_eligibility:
        #             self.eligible_label = tk.Label(
        #                 self,
        #                 text='X',
        #                 bg='green',
        #                 font=fonts.basic_font, width=3)
        #             self.eligible_label.grid(row=0, column=1, sticky='ew')
        #         else:
        #             self.eligible_label = tk.Label(
        #                 self,
        #                 text='-',
        #                 bg='white',
        #                 font=fonts.basic_font, width=3)
        #             self.eligible_label.grid(row=0, column=1, sticky='ew')
        #
        # item = 0
        # for position, eligibility in positions:
        #     label = EligibilityFrame(self, position, eligibility)
        #     label.grid(row=item % 4, column=item // 4, sticky='nsew')
        #     item += 1

    def update_frame(self, df):
        positions = [
            ('C', df.iloc[0]['LearnC']),
            ('1B', df.iloc[0]['Learn1B']),
            ('2B', df.iloc[0]['Learn2B']),
            ('3B', df.iloc[0]['Learn3B']),
            ('SS', df.iloc[0]['LearnSS']),
            ('LF', df.iloc[0]['LearnLF']),
            ('CF', df.iloc[0]['LearnCF']),
            ('RF', df.iloc[0]['LearnRF']),
        ]

        class EligibilityFrame(tk.Frame):
            def __init__(self, master, position_string, sel_eligibility):
                super().__init__(master)
                self.columnconfigure(0, weight=1)
                self.columnconfigure(1, weight=1)

                self.pos_label = tk.Label(
                    self, text=position, font=fonts.basic_font, width=3)
                self.pos_label.grid(row=0, column=0, sticky='ew')

                if sel_eligibility:
                    self.eligible_label = tk.Label(
                        self,
                        text='X',
                        bg='green',
                        font=fonts.basic_font, width=3)
                    self.eligible_label.grid(row=0, column=1, sticky='ew')
                else:
                    self.eligible_label = tk.Label(
                        self,
                        text='-',
                        bg='white',
                        font=fonts.basic_font, width=3)
                    self.eligible_label.grid(row=0, column=1, sticky='ew')

        item = 0
        for position, eligibility in positions:
            label = EligibilityFrame(self, position, eligibility)
            label.grid(row=item % 4, column=item // 4, sticky='nsew')
            item += 1

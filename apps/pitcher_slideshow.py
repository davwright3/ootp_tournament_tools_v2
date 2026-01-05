import tkinter as tk
from utils.view_utils.header_frame import Header
from utils.view_utils.footer_frame import Footer
from utils.view_utils.pitcher_slide_frame import PitcherSlideFrame

# TODO 2: Create dataframe for slideshow
# TODO 3: Create individual player frame
# TODO 4: Add custom frames for ratings displays
# TODO 5: Create stats display frame
# TODO 6: Create buttons and methods for navigation

class PitcherSlideshowApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.geometry('1920x1080')
        self.title('Pitching Leaders')

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.header_frame = Header(self, app_name="Pitching Leaders")
        self.header_frame.grid(column=0, row=0, sticky='nsew')

        self.main_frame = PitcherSlideFrame(self)
        self.main_frame.grid(column=0, row=1, sticky='nsew')

        self.footer_frame = Footer(self)
        self.footer_frame.grid(column=0, row=2, sticky='nsew')
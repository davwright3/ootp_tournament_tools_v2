"""
Displays scatter plot of calculated dataframe for datavisualization.

Sent dataframe should have x values at column index 0 and
 y values at column index 1.
"""

import tkinter as tk
from tkinter import messagebox

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np



class DataVisScatterFrame(tk.Frame):
    def __init__(self, parent, df=None):
        super().__init__(parent)

        self.df = df

        def plot():
            fig = Figure(figsize=(5, 5), dpi=100)
            x = df.iloc[:, 0]
            y = df.iloc[:, 1]

            ax = fig.add_subplot(111)
            ax.set_title('BABIP')
            ax.set_xlabel('BABIP')
            ax.set_ylabel('BABIP_calc')

            scatter = ax.scatter(x, y, s=40, picker=True)

            annot = ax.annotate(
                "",
                xy=(0,0),
                xytext=(10, 10),
                textcoords="offset points",
                bbox=dict(boxstyle='round', fc='w'),
                arrowprops=dict(arrowstyle='->'),
            )
            annot.set_visible(False)

            def update_annot(ind):
                """Update annotation position from the scatter index dict."""
                idx = ind['ind'][0]
                pos = scatter.get_offsets()[idx]
                annot.xy = pos

                # Build the annotations
                lines = []
                if 'Title' in self.df.columns:
                    lines.append(self.df['Title'].iloc[idx])
                if 'PA' in self.df.columns:
                    lines.append('PA: ' + str(self.df['PA'].iloc[idx]))
                if 'vL' in self.df.columns:
                    lines.append('vL: ' + str(self.df['vL'].iloc[idx]))
                if 'vR' in self.df.columns:
                    lines.append('vR: ' + str(self.df['vR'].iloc[idx]))
                lines.append('Val: ' + str(self.df.iloc[idx, 1]))
                annot.set_text("\n".join(lines))

                ax_bbox = ax.get_window_extent(renderer=fig.canvas.get_renderer())
                disp_pt = ax.transData.transform(pos)

                cx = (ax_bbox.x0 + ax_bbox.x1) / 2
                cy = (ax_bbox.y0 + ax_bbox.y1) / 2

                off_x = 40 if disp_pt[0] < cx else -300
                off_y = 40 if disp_pt[1] < cy else -80

                annot.set_position((off_x, off_y))
                annot.get_bbox_patch().set_alpha(0.9)

            def hover(event):
                """Show annotation when mouse is over a point."""
                if event.inaxes == ax:
                    cont, ind = scatter.contains(event)
                    if cont:
                        update_annot(ind)
                        annot.set_visible(True)
                        canvas.draw_idle()
                    else:
                        if annot.get_visible():
                            annot.set_visible(False)
                            canvas.draw_idle()

            def on_pick(event):
                """Handle click events."""
                if hasattr(event, 'ind') and len(event.ind) > 0:
                    idx = event.ind[0]
                    point_id = str(self.df['Title'].iloc[idx] + 'PA: ' + self.df['PA'].iloc[idx])
                    print('Clicked id:', point_id)
                    messagebox.showinfo('Clicked id:', point_id)

            canvas = FigureCanvasTkAgg(fig, self)
            canvas.draw()
            canvas.get_tk_widget().pack(fill='both', expand=True)

            toolbar = NavigationToolbar2Tk(canvas, self)
            toolbar.update()
            toolbar.pack(side='top', fill='x')

            canvas.mpl_connect('motion_notify_event', hover)
            canvas.mpl_connect('pick_event', on_pick)

        plot()



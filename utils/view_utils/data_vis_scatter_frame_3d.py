import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import messagebox
from mpl_toolkits.mplot3d import Axes3D


class DataVisualScatterFrame3D(tk.Frame):
    def __init__(self, parent, df=None):
        super().__init__(parent)

        self.df = df

        self.canvas = None
        self.fig = None

        def plot():
            xs = df.iloc[:, 0]
            ys = df.iloc[:, 1]
            zs = df.iloc[:, 2]

            self.fig = plt.figure(figsize=(5, 5))
            ax = self.fig.add_subplot(111)

            colormap = plt.get_cmap('plasma')

            scatter = ax.scatter(xs, ys, c=zs, cmap=colormap, s=100, alpha=.7, edgecolors='black', linewidth=1)
            colorbar= plt.colorbar(scatter, ax=ax, label='Result Value')

            ax.set_xlabel('Avoid Ks')
            ax.set_ylabel('Eye')

            ax.set_title(df.columns.tolist()[2])
            ax.grid(True, alpha=0.3, linestyle='--')

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
                if 'BIP' in self.df.columns:
                    lines.append(str(self.df['BIP'].iloc[idx]))
                if 'Krate' in self.df.columns:
                    lines.append(str(self.df['Krate'].iloc[idx]))
                if 'PA' in self.df.columns:
                    lines.append('PA: ' + str(self.df['PA'].iloc[idx]))
                if 'vL' in self.df.columns:
                    lines.append('vL: ' + str(self.df['vL'].iloc[idx]))
                if 'vR' in self.df.columns:
                    lines.append('vR: ' + str(self.df['vR'].iloc[idx]))
                lines.append('Val: ' + str(self.df.iloc[idx, 1]))
                annot.set_text("\n".join(lines))

                ax_bbox = ax.get_window_extent(renderer=self.fig.canvas.get_renderer())
                disp_pt = ax.transData.transform(pos)

                cx = (ax_bbox.x0 + ax_bbox.x1) / 2
                cy = (ax_bbox.y0 + ax_bbox.y1) / 2

                off_x = 40 if disp_pt[0] < cx else -100
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
                        self.canvas.draw_idle()
                    else:
                        if annot.get_visible():
                            annot.set_visible(False)
                            self.canvas.draw_idle()

            def on_pick(event):
                """Handle click events."""
                if hasattr(event, 'ind') and len(event.ind) > 0:
                    idx = event.ind[0]
                    point_id = str(self.df['Title'].iloc[idx] + 'PA: ' + self.df['PA'].iloc[idx])
                    print('Clicked id:', point_id)
                    messagebox.showinfo('Clicked id:', point_id)

            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill='both', expand=True)

            toolbar = NavigationToolbar2Tk(self.canvas, self)
            toolbar.update()
            toolbar.pack(side='top', fill='x')

            self.canvas.mpl_connect('motion_notify_event', hover)
            self.canvas.mpl_connect('pick_event', on_pick)

        plot()

    def destroy(self):
        """Clean up matplotlib resources before destroying the frame"""
        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()
        if hasattr(self, 'fig'):
            plt.close(self.fig)
        super().destroy()

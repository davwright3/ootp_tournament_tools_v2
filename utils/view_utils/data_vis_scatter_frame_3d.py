import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D


class DataVisualScatterFrame3D(tk.Frame):
    def __init__(self, parent, df=None):
        super().__init__(parent)

        xs = df['Avoid Ks']
        ys = df['Eye']
        zs = df['BIP']

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(xs, ys, zs)

        ax.set_xlabel('Avoid Ks')
        ax.set_ylabel('Eye')
        ax.set_zlabel('BIP')

        ax.set_title('Balls in Play from AvK/Eye')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

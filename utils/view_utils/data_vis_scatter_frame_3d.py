import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D


class DataVisualScatterFrame3D(tk.Frame):
    def __init__(self, parent, df=None):
        super().__init__(parent)

        self.label = tk.Label(self, text='Label label')
        self.label.grid(row=0, column=0, sticky='nsew')

        def poly_terms_2d(x, y, degree):
            """
            Build matrix for 2S polynomial terms up to a total degree.
            Order of columns matches i, k with i+j degree.
            """
            x = np.asarray(x)
            y = np.asarray(y)
            cols = []
            for total in range(degree+1):
                for i in range(total+1):
                    j = total - i
                    cols.append((x ** i) * (y ** j))
            return np.vstack(cols).T # shape n_samples n_terms

        def polyfit2d(x, y, z, degree):
            """
            Fit z = sum a_k * term_k(x, y) where terms are monomials up to degree
            Returns coefficient vector and a predict function
            """
            A = poly_terms_2d(x, y, degree)
            # Solve least squares
            coeffs, *_ = np.linalg.lstsq(A, z, rcond=None)
            def predict(xg, yg):
                Xg = poly_terms_2d(np.asarray(xg).ravel(), np.asarray(yg).ravel(), degree)
                zg = Xg.dot(coeffs)
            return coeffs, predict

        # Sample data to get the frame running
        np.random.seed(42)
        N = 180
        x_data = np.random.uniform(-3, 3, N)
        y_data = np.random.uniform(-3, 3, N)

        z_data = 0.8 * x_data + -0.5* (y_data**2) + 0.3 * x_data * y_data + np.random.normal(scale=1.0, size=N)

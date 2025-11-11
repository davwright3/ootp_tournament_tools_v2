"""Custom reusable footer frame for entire app."""
import tkinter as tk
import webbrowser


class Footer(tk.Frame):
    """Custom footer class, insertable into all apps."""
    def __init__(self, parent):
        """Initialization of footer class."""
        super().__init__(parent, bd=3, relief='groove', bg='lightgray')

        def open_link(url):
            webbrowser.open_new(url)

        def on_enter(event):
            self.github_button.configure(bg='violet', cursor='hand2')

        def on_leave(event):
            self.github_button.configure(bg='lightgray', cursor='')

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)

        self.au_label = tk.Label(
            self,
            text="Created by David Wright",
            font=("Arial", 12),
            padx=5,
            pady=5,
            background='lightgray',
        )
        self.au_label.grid(row=0, column=0, sticky="e")

        self.github_button_frame = tk.Frame(
            self, padx=5, pady=5, bg='lightgray')
        self.github_button_frame.grid(row=0, column=1, sticky="e")

        self.github_button = tk.Button(
            self.github_button_frame,
            text="Other Projects on Github",
            font=("Arial", 12),
            borderwidth=2,
            relief="solid",
            padx=10,
            pady=10,
            background='lightgray',
            command=lambda: webbrowser.open_new(
                "https://github.com/davwright3")
        )
        self.github_button.grid(row=0, column=2, sticky='w')
        self.github_button.bind("<Enter>", on_enter)
        self.github_button.bind("<Leave>", on_leave)

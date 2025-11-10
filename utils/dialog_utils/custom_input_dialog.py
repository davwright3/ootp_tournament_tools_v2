"""Class for a custom dialog accepting user input."""
import tkinter as tk


class CustomInputDialog(tk.Toplevel):
    """
    CustomInputDialog to get string input information
    from the user.
    """

    def __init__(self, parent, title="Input", prompt="Enter value"):
        """
        Initialize custom input dialog, used to retrieve string information
        from the user for various parts of the program.
        When user presses the confirm button, the string data will be returned
        to the requesting app.
        :param parent: Parent window, tkTkToplevel
        :param title: Title of the dialog, string
        :param prompt: Prompt to display, string
        """
        super().__init__(parent)
        self.title(title)
        self.geometry("300x150")
        self.grab_set()
        self.transient(parent)

        self.user_input = None

        self.label = tk.Label(self, text=prompt)
        self.label.pack(pady=(20, 10))

        self.entry = tk.Entry(self)
        self.entry.pack(pady=5, padx=20)
        self.entry.focus_set()

        self.confirm_button = tk.Button(
            self,
            text="Confirm",
            command=self._on_confirm
        )
        self.confirm_button.pack(pady=10)

        self.bind("<Return>", self._on_confirm)

    def _on_confirm(self, event=None):
        """
        Confirm the user input.
        return: user_input if user input is confirmed, None otherwise.
        """
        self.user_input = self.entry.get()
        self.destroy()

    def get_input(self):
        """Return user input."""
        self.wait_window()
        return self.user_input

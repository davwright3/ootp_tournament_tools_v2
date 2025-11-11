import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    """
    Contains canvas + inner frame with vertical scrollbars.
    """
    def __init__(
            self,
            parent,
            *,
            yscroll=True,
            xscroll=False,
            auto_width=True,
            **kwargs):
        super().__init__(parent, **kwargs)

        self.canvas = tk.Canvas(
            self, highlightthickness=0, borderwidth=0, bg='white')

        self.vsb = ttk.Scrollbar(
            self,
            orient='vertical',
            command=self.canvas.yview
        ) if yscroll else None
        self.hsb = ttk.Scrollbar(
            self,
            orient='horizontal',
            command=self.canvas.xview
        ) if xscroll else None

        # Wire canvas <-> scroll bars
        if yscroll:
            self.canvas.configure(yscrollcommand=self.vsb.set)
        if xscroll:
            self.canvas.configure(xscrollcommand=self.hsb.set)

        # Layout canvas
        self.canvas.grid(row=0, column=0, sticky='nsew')
        if yscroll:
            self.vsb.grid(row=0, column=1, sticky='ns')
        if xscroll:
            self.hsb.grid(row=1, column=0, sticky='ew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.inner = ttk.Frame(self.canvas)

        # Put inner frame in canvas
        self._win_id = self.canvas.create_window(
            (0, 0), window=self.inner, anchor='nw')

        # Keep scroll region in sync
        self.inner.bind("<Configure>", self._on_inner_configure)

        # Make inner frame follow canvas
        if auto_width:
            self.canvas.bind("<Configure>", self._on_canvas_configure)

        self.inner.grid_columnconfigure(0, weight=1)

        if yscroll:
            self._bind_mousewheel(self.canvas)

    # Helpers
    def _bind_mousewheel(self, widget):
        # Windows and Mac
        widget.bind_all("<MouseWheel>", self._on_mousewheel)
        # Linux
        widget.bind_all("<Button-4>", self._on_mousewheel)
        widget.bind_all("<Button-5>", self._on_mousewheel)

    def _on_mousewheel(self, event):
        if event.num == 4:  # Linux scroll up
            self.canvas.yview_scroll(-1, 'units')
        elif event.num == 5:
            self.canvas.yview_scroll(1, 'units')
        else:
            self.canvas.yview_scroll(
                int(-1 * (event.delta / 120)), 'units')

    def _on_inner_configure(self, event):
        # Update the scrollable area to the bounding box
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def _on_canvas_configure(self, event):
        # Make the inner frame match canvas width
        self.canvas.itemconfigure(self._win_id, width=event.width)

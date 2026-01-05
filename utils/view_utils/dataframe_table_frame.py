from tkinter import ttk
from tkinter import font as tkfont
from typing import Dict, Callable, List, Optional
import pandas as pd
import logging


class DataFrameTableFrame(ttk.Frame):
    def __init__(
            self,
            parent=None,
            df: Optional[pd.DataFrame] = None,
            columns: Optional[List[str]] = None,
            formatters: Optional[Dict[str, Callable]] = None,
            sort_keys: Optional[
                Dict[str, Callable[[pd.Series], pd.Series]]
            ] = None,
            height: int = 18,
            show_index: bool = False,
            on_row_double_click: Optional[Callable[[pd.Series], None]] = None,
            selected_team=None,
            **kwargs,
    ):
        super().__init__(parent, **kwargs)
        self._df: pd.DataFrame = pd.DataFrame() if df is None else df.copy()
        self._formatters = formatters or {}
        self._sort_keys = sort_keys or {}
        self._show_index = show_index
        self._sort_state = {'col': None, 'reverse': False}
        self._on_row_double_click_cb = on_row_double_click
        self._iid_to_row: Dict[str, pd.Series] = {}

        self.selected_team = selected_team

        # Decide columns
        if columns is None:
            columns = self._df.columns.tolist()
        self._columns = columns

        # Create the tree and scroll bars
        self.tree = ttk.Treeview(
            self,
            columns=self._tree_columns(),
            show='headings',
            height=height
        )
        self.vsb = ttk.Scrollbar(
            self,
            orient='vertical',
            command=self.tree.yview
        )
        self.hsb = ttk.Scrollbar(
            self,
            orient='horizontal',
            command=self.tree.xview
        )
        self.tree.configure(
            yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)

        # Setting up the grids, main panel (tree) should expand fully)
        self.tree.grid(row=0, column=0, sticky='nsew')
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.hsb.grid(row=1, column=0, sticky='ew')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Setting up styles
        style = ttk.Style(self)
        # ---------- Set Treeview Font Size ----------
        tree_font = ("Segoe UI", 16)  # increase size here
        header_font = ("Segoe UI", 18, "bold")

        style.configure('Treeview', font=tree_font, padding=(0, 4))
        style.configure('Treeview.Heading', font=header_font)

        style.configure('Treeview', rowheight=28)
        self.tree.tag_configure('odd', background='#f7f7f7')
        self.tree.tag_configure('even', background='#ffffff')
        self.tree.tag_configure('selected_team', background='#AFE1AF')
        self.tree.tag_configure('right', anchor='e')
        self.tree.bind("<Double-1>", self._on_row_double_click)

        # Set headings and widths
        for col in self._tree_columns():
            self.tree.heading(
                col, text=col, command=lambda c=col: self._on_heading_click(c))
            if col == 'Title':
                self.tree.column(col, width=700, minwidth=200, stretch=True, anchor='w')
            else:
                self.tree.column(col, width=50, minwidth=30, stretch=False, anchor='w')


        self._refresh_all()

    # Public API for apps to use
    def set_dataframe(
            self,
            df: pd.DataFrame,
            columns: Optional[List[str]] = None):
        """Replace the current dataframe and redraw the tree."""
        self._df = df.copy()
        if columns is None:
            self._columns = self._df.columns.tolist()
        else:
            self._columns = [c for c in self._df.columns if c in columns]
        self._formatters = {
            k: v for k, v in (self._formatters or {}).items()
            if k in self._columns
        }
        if hasattr(self, '_sort_keys'):
            self._sort_keys = {k: v for k, v in self._sort_keys.items()
                               if k in self._columns}

        self._refresh_all()

    def clear(self):
        """Clear the tree."""
        self.tree.delete(*self.tree.get_children())

    # Internal methods
    def _tree_columns(self) -> List[str]:
        if self._show_index:
            return ['#'] + self._columns
        return self._columns

    def _format_value(self, col: str, val):
        if pd.isna(val):
            return ""
        if col in self._formatters:
            try:
                return self._formatters[col](val)
            except Exception:
                return str(val)
        return str(val)

    def _refresh_all(self):
        # Reset headings to match new columns
        current_cols = self._tree_columns()
        self.tree.configure(columns=current_cols)
        for col in current_cols:
            self.tree.heading(
                col,
                text=col,
                command=lambda c=col: self._on_heading_click(c))
            # Numeric hueristic for alignment and width
            anchor = 'e' if self._is_numeric_column(col) else 'w'
            self.tree.column(col, anchor=anchor)
        self._load_rows()
        self._autosize_columns(sample_rows=200)

    def _is_numeric_column(self, col: str) -> bool:
        if self._show_index and col == '#':
            return False
        series = self._df.index if\
            (self._show_index and col == '#') else self._df[col]
        return pd.api.types.is_numeric_dtype(series)

    def _load_rows(self):
        self.clear()
        if self._df.empty:
            return
        use_cols = self._columns
        for i, (idx, row) in enumerate(self._df.iterrows()):
            if ('ORG' in list(self._columns)
                    and row['ORG'] == self.selected_team):
                tags = ('selected_team',)
            elif i % 2:
                tags = ('odd',)
            else:
                tags = ('even',)
            values = []
            if self._show_index:
                values.append(idx)
            for col in use_cols:
                values.append(self._format_value(col, row.get(col)))
            iid = self.tree.insert(
                '',
                'end',
                values=values,
                tags=tags)
            self._iid_to_row[iid] = row

            # Add right align tag for numeric
            if self._show_index:
                start = 1
            else:
                start = 0
            for j, col in enumerate(use_cols, start=start):
                if self._is_numeric_column(col):
                    self.tree.set(
                        iid,
                        self._tree_columns()[j],
                        self.tree.set(iid, self._tree_columns()[j]))

    def _on_heading_click(self, col: str):
        """Sort by a column.  Toggles asc/desc."""
        if self._show_index and col == '#':
            # Sort by index
            by = None
        else:
            by = col

        prev_col = self._sort_state['col']
        reverse = self._sort_state['reverse']
        if prev_col == col:
            reverse = not reverse
        else:
            reverse = not False

        if by is None:
            sorted_df = self._df.sort_index(ascending=not reverse)
        else:
            sorted_df = self._df.sort_values(
                by=by,
                ascending=not reverse,
                kind='mergesort',
                na_position='last'
            )

        self._sort_state = {'col': col, 'reverse': reverse}
        self.set_dataframe(sorted_df)

    def _autosize_columns(self, sample_rows: int = 200):
        """Rough autosize based on header and sample rows."""
        cols = self._tree_columns()
        # Minimums
        min_w = {c: 50 for c in cols}
        min_w['Title'] = 700
        for c in cols:
            # Header width hint
            min_w[c] = max(min_w[c], int(len(c) * 8.0) + 24)

        # Sample some rows for content width
        kids = self.tree.get_children()
        sample_ids = kids[:sample_rows]
        for c in cols:
            idx = cols.index(c)
            max_len = len(c)
            for iid in sample_ids:
                v = self.tree.item(iid, 'values')
                if idx < len(v):
                    max_len = max(max_len, len(str(v[idx])))
            # Char -> pixel adjustment
            width = int(max_len * 8.0) + 24
            self.tree.column(c, width=max(min_w[c], min(width, 420)))

    def _on_row_double_click(self, event=None):
        iid = None
        if event is not None:
            # Ignore headers and empty regions
            region = self.tree.identify('region', event.x, event.y)
            if region != 'cell':
                return
            iid = self.tree.identify_row(event.y)

        if not iid:
            iid = self.tree.focus()

        if not iid:
            return

        row = self._iid_to_row.get(iid)
        if row is None:
            try:
                pos = list(self.tree.get_children()).index(iid)
                row = self._df.iloc[pos]
            except Exception:
                return

        if callable(self._on_row_double_click_cb):
            try:
                self._on_row_double_click_cb(row)
            except Exception as e:
                (logging.getLogger('apps.basic_stats_app.data_utils').
                 exception("Double click callback failed", e))

"""Singleton pattern data frame for basic stats app use."""
import pandas as pd
from datetime import datetime as dt
import numpy as np
from pandas.api.types import is_datetime64_any_dtype


class DataStore:
    """
    Singleton pattern data frame for basic stats app use.
    Intended to be loaded when the user selects a target file from
    one of the main statistics apps.
    If no instance is present, a new instance of the class is created.
    """

    _instance = None
    _main_dataframe = None
    _tournament_type = None

    def __new__(cls):
        """Set singleton instance."""
        if cls._instance is None:
            cls._instance = super(DataStore, cls).__new__(cls)
        return cls._instance

    def check_tourney_type(self, df):
        # Get the tourney column to check
        col = df['Trny']
        col = col.dropna()

        if len(col) == 0:
            return 'empty'

        # Check for all integers first
        if pd.api.types.is_integer_dtype(col):
            return 'quick'

        if col.dtype == 'object' or pd.api.types.is_string_dtype(col):
            try:
                for val in col:
                    dt.strptime(str(val), '%d %b')
                return 'daily'
            except (ValueError, TypeError):
                pass

            date_formats = [
                "%d %B",  # "15 December"
                "%d-%b",  # "15-Dec"
                "%d/%b",  # "15/Dec"
                "%b %d",  # "Dec 15"
                "%B %d",
            ]

            for fmt in date_formats:
                try:
                    for val in col:
                        dt.strptime(str(val), fmt)
                    return 'daily'
                except (ValueError, TypeError):
                    continue

            return 'na'



    def load_data(self, filepath):
        """
        Load the file into the dataframe from the target CSV.
        :param filepath: Path to the CSV file, string.
        :return: None
        """
        df = pd.read_csv(filepath)
        self._tournament_type = self.check_tourney_type(df)
        self._main_dataframe = df

    def get_data(self):
        """
        Return the dataframe for use in app.
        :return: Dataframe
        """
        return self._main_dataframe

    def get_tournament_type(self):
        return self._tournament_type

    def set_data(self, df):
        """
        Set dataframe instance to new dataframe.
        :param df: Dataframe
        :return: None
        """
        self._main_dataframe = df

    def clear_data(self):
        """Clear the dataframe."""
        self._main_dataframe = None


data_store = DataStore()

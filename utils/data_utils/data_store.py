"""Singleton pattern data frame for basic stats app use."""
import pandas as pd


class DataStore:
    """
    Singleton pattern data frame for basic stats app use.
    Intended to be loaded when the user selects a target file from
    one of the main statistics apps.
    If no instance is present, a new instance of the class is created.
    """

    _instance = None
    _main_dataframe = None

    def __new__(cls):
        """Set singleton instance."""
        if cls._instance is None:
            cls._instance = super(DataStore, cls).__new__(cls)
        return cls._instance

    def load_data(self, filepath):
        """
        Load the file into the dataframe from the target CSV.
        :param filepath: Path to the CSV file, string.
        :return: None
        """
        df = pd.read_csv(filepath)
        self._main_dataframe = df

    def get_data(self):
        """
        Return the dataframe for use in app.
        :return: Dataframe
        """
        return self._main_dataframe

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

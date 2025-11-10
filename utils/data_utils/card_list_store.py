"""
Singleton for storing the card list from the user's
target_card_list path.
"""
from utils.config_utils.load_save_settings import settings
import pandas as pd
import os


class CardListStore:
    """
    Singleton pattern for loading the card list.
    Targets the user's target_card_list path.
    If no instance of the class exists, it creates a new instance.
    Creates a dataframe in RAM from the csv located at the target path.
    """
    _instance = None
    _card_list_dataframe = None

    card_list_path = settings['TargetFiles']['target_card_list']

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CardListStore, cls).__new__(cls)
        return cls._instance

    def load_card_list(self, filepath=None):
        """
        Load card list from target path into a DataFrame.
        :param filepath: The path of the csv file, str.
        """
        if filepath is None:
            filepath = settings.get(
                'TargetFiles',
                'target_card_list',
                fallback=None
            )
        filepath = os.path.normpath(filepath)

        if not filepath or not os.path.isfile(filepath):
            raise FileNotFoundError(
                f'File {filepath} not found.'
            )
        df = pd.read_csv(filepath)
        self._card_list_dataframe = df
        return df

    def get_card_list(self):
        """Return the loaded DataFrame for use by other apps."""
        return self._card_list_dataframe

    def set_data(self, df):
        """
        Simple overwrite of previous DataFrame with a new one.
        :param df: The new DataFrame, pd.DataFrame.
        """
        self._card_list_dataframe = df

    def clear_data(self):
        """
        Delete the loaded DataFrame.
        """
        self._card_list_dataframe = None


card_list_store = CardListStore()

"""
Singleton for storing the card list from the user's
target_card_list path.
"""
from utils.data_utils.select_return_target_file import select_return_target_file
from utils.config_utils.load_save_settings import settings
import pandas as pd

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

    def __init__(self):
        if self._card_list_dataframe is None and self.card_list_path:
            self.load_card_list(self.card_list_path)

    def load_card_list(self, filepath):
        """
        Load card list from target path into a DataFrame.
        :param filepath: The path of the csv file, str.
        """
        df = pd.read_csv(filepath)
        self._card_list_dataframe = df

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






"""
Singleton for storing the card list from the user's
target_card_list path.
"""
from utils.data_utils.select_return_target_file import select_return_target_file
from utils.config_utils.load_save_settings import settings
import pandas as pd

class CardListStore:
    """Singleton pattern for loading the card list."""
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
        df = pd.read_csv(filepath)
        self._card_list_dataframe = df

    def get_card_list(self):
        return self._card_list_dataframe

    def set_data(self, df):
        self._card_list_dataframe = df

    def clear_data(self):
        self._card_list_dataframe = None

card_list_store = CardListStore()






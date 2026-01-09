import pandas as pd
from utils.config_utils.get_resource_path import get_resource_path
import os


class StadiumFactorsStore:
    _instance = None
    _park_factors_dataframe = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StadiumFactorsStore, cls).__new__(cls)
            cls._instance._load_park_factors_dataframe()
        return cls._instance

    def _load_park_factors_dataframe(self):
        """Load stats dataframe if it exists."""
        file_path = get_resource_path(os.path.join(
            'au_ootp_tournament_utilities_v2/image_assets',
            'pt_26_ballparks.csv')
        )

        try:
            self._park_factors_dataframe = pd.read_csv(file_path)
            self._park_factors_dataframe['name_and_year'] = (
                    self._park_factors_dataframe['Ballpark'].astype(str) + ' ' +
                    self._park_factors_dataframe['Year'].astype(str))
        except FileNotFoundError:
            print("Parks file not found")

    def get_park_factors(self):
        return self._park_factors_dataframe

stadium_factors_store = StadiumFactorsStore()


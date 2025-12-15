"""
Singleton for storing MLB season stats for run environment settings.
"""
import pandas as pd
import os
from utils.config_utils.get_resource_path import get_resource_path

class MLBSeasonStatsStore:
    """
    Singleton pattern for storing MLB season stats.
    """
    _instance = None
    _stats_dataframe = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MLBSeasonStatsStore, cls).__new__(cls)
            cls._instance._load_stats_dataframe()
        return cls._instance

    def _load_stats_dataframe(self):
        """Load stats dataframe if it exists."""
        file_path = get_resource_path(os.path.join(
            'au_ootp_tournament_utilities_v2/image_assets',
            'all_mlb_season_stats.csv')
        )

        try:
            self._stats_dataframe = pd.read_csv(file_path)
        except Exception as e:
            print("Unable to load stats dataframe from", e)
            return


    def get_stats_dataframe(self):
        return self._stats_dataframe

mlb_stats_store = MLBSeasonStatsStore()



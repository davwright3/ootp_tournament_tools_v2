from utils.stats_utils.calc_league_stats import calc_league_stats

class LeagueStatsStore:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(LeagueStatsStore, cls).__new__(cls)
        return cls._instance

    def load_stats(self):
        self._instance = calc_league_stats()

    def get_stats(self):
        return self._instance

league_stats_store = LeagueStatsStore()
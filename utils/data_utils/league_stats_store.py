from utils.stats_utils.calc_league_stats import calc_league_stats


class LeagueStatsStore:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super().__new__(cls)
        return cls._singleton

    def __init__(self):
        if not hasattr(self, '_stats'):
            self._stats = None

    def load_stats(self):
        self._stats = calc_league_stats()

    def get_stats(self):
        if self._stats is None:
            self.load_stats()
        return self._stats


league_stats_store = LeagueStatsStore()

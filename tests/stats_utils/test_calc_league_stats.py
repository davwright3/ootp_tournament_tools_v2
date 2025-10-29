import utils.stats_utils.calc_league_stats as mod


def test_calc_league_stats(monkeypatch, patched_batting_data_store):
    monkeypatch.setattr( mod.data_store, 'get_data', lambda: patched_batting_data_store)

    stats = mod.calc_league_stats()

    assert stats['lg_avg'] == '.338'
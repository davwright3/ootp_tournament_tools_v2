import utils.stats_utils.get_player_batting_stats as mod

def test_get_player_batting_stats_return_accurate_results(patched_batting_data_store):
    player_stats = mod.get_player_batting_stats(card_id=73691)

    assert player_stats['ply_pa'] == '50'
    assert player_stats['ply_avg'] == '.318'


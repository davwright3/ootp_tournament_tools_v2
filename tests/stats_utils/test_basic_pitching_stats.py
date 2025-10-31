"""Test pitching stats return accurate results."""
import utils.stats_utils.generate_basic_pitching_stats_df as mod
import utils.stats_utils.calc_pitching_stats as calc
# TODO 7: test collection only works

def test_basic_pitching_stats_return_accurate_calcs(monkeypatch, patched_pitching_data_store):

    monkeypatch.setattr(calc.data_store, 'get_data', lambda: patched_pitching_data_store)

    df = mod.generate_basic_pitching_stats(min_ip=1, cull_team_limit_select=12)

    assert df.loc[df['CID'] == 73691, 'ERA'].squeeze() == 2.25
    assert df.loc[df['CID'] == 73691, 'WHIP'].squeeze() == 1.00
    assert df.loc[df['CID'] == 73691, 'K%'].squeeze() == .222
    assert df.loc[df['CID'] == 73691, 'BB%'].squeeze() == .067
    assert df.loc[df['CID'] == 73691, 'K-BB'].squeeze() == .155
    assert df.loc[df['CID'] == 73691, 'HR/9'].squeeze() == 1.50
    assert df.loc[df['CID'] == 73691, 'SV%'].squeeze() == .50
    assert df.loc[df['CID'] == 73691, 'SD/MD'].squeeze() == 2.00
    assert df.loc[df['CID'] == 73691, 'IRS%'].squeeze() == .50
    assert df.loc[df['CID'] == 73691, 'GB%'].squeeze() == .667
    assert df.loc[df['CID'] == 73691, 'WAR/200'].squeeze() == 11.7

    assert not df.empty

def test_min_max_pitcher_ratings(monkeypatch, patched_pitching_data_store):
    monkeypatch.setattr(calc.data_store, 'get_data', lambda: patched_pitching_data_store)

    df = mod.generate_basic_pitching_stats(min_ip=10, min_value=50, max_value=75, cull_team_limit_select=12)

    assert 73691 not in df['CID'].tolist()
    assert 73885 in df['CID'].tolist()

def test_min_ip_returns_properly(monkeypatch, patched_pitching_data_store):
    monkeypatch.setattr(calc.data_store, 'get_data', lambda: patched_pitching_data_store)

    df = mod.generate_basic_pitching_stats(min_ip=14, cull_team_limit_select=12)

    assert 73691 not in df['CID'].tolist()
    assert 73885 in df['CID'].tolist()

def test_pitcher_side_choice_returns_properly(monkeypatch, patched_pitching_data_store):
    monkeypatch.setattr(calc.data_store, 'get_data', lambda: patched_pitching_data_store)

    df = mod.generate_basic_pitching_stats(throws_side_select='L', min_ip=1, cull_team_limit_select=12)

    assert 73691 not in df['CID'].tolist()
    assert 73885 in df['CID'].tolist()

def test_pitcher_type_returns_properly(monkeypatch, patched_pitching_data_store):
    monkeypatch.setattr(calc.data_store, 'get_data', lambda: patched_pitching_data_store)

    df = mod.generate_basic_pitching_stats(min_ip=1, cull_team_limit_select=12, start_relief_cutoff=5.5, pitcher_type_select='SP')

    assert 73691 in df['CID'].tolist()
    assert 73885 not in df['CID'].tolist()

def test_stats_select_returns_correct_columns(monkeypatch, patched_pitching_data_store):
    monkeypatch.setattr(calc.data_store, 'get_data', lambda: patched_pitching_data_store)

    df = mod.generate_basic_pitching_stats(min_ip=1, cull_team_limit_select=12, stat_list=['ERA', 'HR/9'])

    assert 'ERA', 'HR/9' in df.columns.tolist()
    assert 'WHIP', 'BB%' not in df.columns.tolist()

    df = mod.generate_basic_pitching_stats(min_ip=1, cull_team_limit_select=12)

    assert 'ERA', 'BB%' in df.columns.tolist()

def test_general_items_return_properly(monkeypatch, patched_pitching_data_store):
    monkeypatch.setattr(calc.data_store, 'get_data', lambda: patched_pitching_data_store)

    df = mod.generate_basic_pitching_stats(min_ip=1, cull_team_limit_select=12, general_list=['owned'])

    assert 'owned' in df.columns.tolist()
    assert 'L10' not in df.columns.tolist()



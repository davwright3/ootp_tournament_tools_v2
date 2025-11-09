"""
Test to ensure basic batting stats return expected values.
Uses fixture from conftest.py file for basic stats.
"""
import utils.stats_utils.generate_basic_batting_stats_df as mod
from tests.conftest import sample_stats_df


def test_basic_batting_stats_return_correct_values(patched_batting_data_store):
    """
    Tests that all stats return the correct values.
    :param patched_batting_data_store:
    :return:
    """
    df = mod.generate_basic_batting_stats_df(min_pa=1, cull_team_limit_select=12)

    assert not df.empty
    assert df.loc[df['CID'] == 73691, 'AVG'].squeeze() == .318
    assert df.loc[df['CID'] == 73885, 'AVG'].squeeze() == .361
    assert df.loc[df['CID'] == 73691, 'OBP'].squeeze() == .340
    assert df.loc[df['CID'] == 73885, 'OBP'].squeeze() == .390
    assert df.loc[df['CID'] == 73691, 'SLG'].squeeze() == .545
    assert df.loc[df['CID'] == 73885, 'SLG'].squeeze() == .611
    assert df.loc[df['CID'] == 73691, 'OPS'].squeeze() == .885
    assert df.loc[df['CID'] == 73885, 'OPS'].squeeze() == 1.001
    assert df.loc[df['CID'] == 73691, 'wOBA'].squeeze() == .369
    assert df.loc[df['CID'] == 73885, 'wOBA'].squeeze() == .420
    assert df.loc[df['CID'] == 73691, 'HRrate'].squeeze() == 24.0
    assert df.loc[df['CID'] == 73885, 'HRrate'].squeeze() == 30.0
    assert df.loc[df['CID'] == 73691, 'Krate'].squeeze() == 84.0
    assert df.loc[df['CID'] == 73885, 'Krate'].squeeze() == 120.0
    assert df.loc[df['CID'] == 73691, 'BBrate'].squeeze() == 36.0
    assert df.loc[df['CID'] == 73885, 'BBrate'].squeeze() == 30.0
    assert df.loc[df['CID'] == 73691, 'SBrate'].squeeze() == 24.0
    assert df.loc[df['CID'] == 73885, 'SBrate'].squeeze() == 15.0
    assert df.loc[df['CID'] == 73691, 'SBpct'].squeeze() == .667
    assert df.loc[df['CID'] == 73885, 'SBpct'].squeeze() == .500
    assert df.loc[df['CID'] == 73691, 'WARrate'].squeeze() == 10.8
    assert df.loc[df['CID'] == 73885, 'WARrate'].squeeze() == 6.0

def test_returns_only_eligible_cards(patched_batting_data_store):
    df = mod.generate_basic_batting_stats_df(min_pa=1, position_select='Learn2B', cull_team_limit_select=12)

    assert 73691 in df['CID'].tolist()
    assert 73885 not in df['CID'].tolist()

def test_returns_only_selected_stats(patched_batting_data_store):
    df = mod.generate_basic_batting_stats_df(min_pa=1, stat_list=['PA', 'AVG'], cull_team_limit_select=12)

    header_list = df.columns.tolist()
    assert 'PA' in header_list
    assert 'AVG' in header_list
    assert 'OBP' not in header_list

def test_returns_only_higher_than_min_pa(patched_batting_data_store):
    df = mod.generate_basic_batting_stats_df(min_pa=45, cull_team_limit_select=12)

    assert 73691 in df['CID'].tolist()
    assert 73885 not in df['CID'].tolist()

def test_returns_cards_within_selected_value_range(patched_batting_data_store):
    df = mod.generate_basic_batting_stats_df(min_pa=1, min_value=51, max_value=63, cull_team_limit_select=12)

    assert 73691 not in df['CID'].tolist()
    assert 73885 in df['CID'].tolist()

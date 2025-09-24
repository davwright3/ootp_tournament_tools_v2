"""
Test to ensure basic batting stats return expected values.
Uses fixture from conftest.py file for basic stats.
"""
import utils.stats_utils.calc_basic_batting_stats_df as mod
from tests.conftest import sample_stats_df


def test_basic_batting_stats_return_correct_values(patched_batting_data_store):
    df = mod.calc_basic_batting_stats_df()

    assert not df.empty
    assert df.loc[df['CID'] == 11111, 'AVG'].squeeze() == '.318'
    assert df.loc[df['CID'] == 22222, 'AVG'].squeeze() == '.361'
    assert df.loc[df['CID'] == 11111, 'OBP'].squeeze() == '.340'
    assert df.loc[df['CID'] == 22222, 'OBP'].squeeze() == '.390'
    assert df.loc[df['CID'] == 11111, 'SLG'].squeeze() == '.545'
    assert df.loc[df['CID'] == 22222, 'SLG'].squeeze() == '.611'
    assert df.loc[df['CID'] == 11111, 'OPS'].squeeze() == '.885'
    assert df.loc[df['CID'] == 22222, 'OPS'].squeeze() == '1.001'
    assert df.loc[df['CID'] == 11111, 'wOBA'].squeeze() == '.369'
    assert df.loc[df['CID'] == 22222, 'wOBA'].squeeze() == '.420'
    assert df.loc[df['CID'] == 11111, 'HRrate'].squeeze() == '24.0'
    assert df.loc[df['CID'] == 22222, 'HRrate'].squeeze() == '30.0'
    assert df.loc[df['CID'] == 11111, 'Krate'].squeeze() == '84.0'
    assert df.loc[df['CID'] == 22222, 'Krate'].squeeze() == '120.0'
    assert df.loc[df['CID'] == 11111, 'BBrate'].squeeze() == '36.0'
    assert df.loc[df['CID'] == 22222, 'BBrate'].squeeze() == '30.0'
    assert df.loc[df['CID'] == 11111, 'SBrate'].squeeze() == '24.0'
    assert df.loc[df['CID'] == 22222, 'SBrate'].squeeze() == '15.0'
    assert df.loc[df['CID'] == 11111, 'SBpct'].squeeze() == '.667'
    assert df.loc[df['CID'] == 22222, 'SBpct'].squeeze() == '.500'
    assert df.loc[df['CID'] == 11111, 'WARrate'].squeeze() == '10.8'
    assert df.loc[df['CID'] == 22222, 'WARrate'].squeeze() == '6.0'





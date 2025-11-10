"""Test for ensuring that the right teams get removed for missing data issues."""
from utils.stats_utils import cull_teams as mod

def test_cull_teams(patched_batting_data_store):
    """Use testing data store to ensure proper teams are returned."""
    df = mod.cull_teams(patched_batting_data_store)
    print(df)
    assert not df.empty
    assert 73691 in df['CID'].tolist() and 73885 not in df['CID'].tolist()


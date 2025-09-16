"""
Test module for data utilities.
"""
import pandas as pd
import os
from utils.data_utils.process_fiies import add_file

def test_add_file_appends_and_tags(tmp_path, caplog):
    # Create a small CSV
    f = tmp_path / 'tournamentA.csv'
    f.write_text("col1,col2\n1,1\n3,4\n")

    target = pd.DataFrame()

    with caplog.at_level("INFO"):
        out = add_file(target_df=target, file_to_add=str(f))

    # Should add a 'Trny' column with base filename
    assert 'Trny' in out.columns
    assert set(out['Trny']) == {'tournamentA'}
    assert len(out) == 2

    assert any("Adding file tournamentA, 2 rows added" in r.message for r in caplog.records)
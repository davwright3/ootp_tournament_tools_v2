"""Test for proper normalization of innings pitched."""

import utils.stats_utils.normalize_innings_pitched as mod
import pandas as pd

from tests.conftest import sample_stats_df


def test_individual_innings_calcs(sample_stats_df):
    df = sample_stats_df
    df['IPC'] = mod.normalize_innings_pitched(df['IP'])

    assert (df.iloc[0]['IPC'].round(4)) == 6.3333
    assert (df.iloc[1]['IPC'].round(4)) == 5.6667

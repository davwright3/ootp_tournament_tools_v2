import pandas as pd

def test_team_stats_core_columns_and_filter(monkeypatch, patched_team_data_store):
    """
    Ensures function returns core columns.
    """
    import utils.stats_utils.generate_basic_team_stats_df as mod

    monkeypatch.setattr(mod, 'cull_teams', lambda df: df, raising=True)

    def fake_calc_batting_stats(df):
        return pd.DataFrame({
            'ORG': ['A', 'B'],
            'OPS': [0.800, 0.700],
            'OBP': [0.350, 0.330],
        })

    def fake_calc_pitching_stats(df):
        return pd.DataFrame({
            'ORG': ['A', 'B'],
            'ERA': [3.50, 4.20],
            'FIP': [3.80, 4.10],
        })

    # Patch the calc functions so they are small (these are tested in other modules)
    monkeypatch.setattr(mod, 'calc_batting_stats', fake_calc_batting_stats, raising=True)
    monkeypatch.setattr(mod, 'calculate_pitching_stats', fake_calc_pitching_stats, raising=True)

    df = mod.generate_basic_team_stats_df(
        selected_batting_stats=['OPS'],
        selected_pitching_stats=['ERA'],
        min_games=1
    )
    print(df)

    expected_cols = {'ORG', 'GS.1', 'W', 'L', 'Win%', 'OPS', 'ERA'}
    assert expected_cols.issubset(df.columns), f"Missing columns: {expected_cols - set(df.columns)}"

    assert len(df) == 2

    row_a = df.loc[df['ORG'] == 'A'].iloc[0]
    row_b = df.loc[df['ORG'] == 'B'].iloc[0]
    assert row_a['Win%'] == round(1 / (1 + 2), 3)
    assert row_b['Win%'] == round(1 / (1 + 1), 3)
    assert row_a['OPS'] == 0.800
    assert row_b['ERA'] == 4.20

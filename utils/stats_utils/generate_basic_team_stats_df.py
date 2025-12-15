"""Generate and return a dataframe for team stats display."""
import pandas as pd
from utils.data_utils.data_store import data_store
from utils.stats_utils.cull_teams import cull_teams
from utils.stats_utils.normalize_innings_pitched import (
    normalize_innings_pitched)
from utils.stats_utils.calc_batting_stats import calc_batting_stats
from utils.stats_utils.calc_pitching_stats import calculate_pitching_stats


def generate_basic_team_stats_df(
        selected_batting_stats=None,
        selected_pitching_stats=None,
        min_games=20,
):
    df1 = cull_teams(data_store.get_data().copy())
    df1['IPC'] = df1['IP'].apply(normalize_innings_pitched)
    df1 = df1[['ORG', 'PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'TB', 'SO', 'R',
               'HP', 'BB', 'IBB', 'SF', 'SB', 'RC', 'ZR', 'PO', 'A', 'E', 'CS',
               'WAR', 'IPC', 'G.1', 'GS.1', 'W', 'L', 'BF', 'AB.1', 'R.1', 'ER', 'K',
               'BB.1', 'IBB.1', 'HA', '1B.1', '2B.1', '3B.1', 'HR.1', 'SV',
               'SVO', 'SD', 'MD', 'HP.1', 'SH.1', 'SF.1', 'QS', 'IR', 'IRS',
               'GB', 'FB', 'WAR.1', 'Trny']].groupby(['ORG'],
                                                     as_index=False).sum()
    df1['Win%'] = (df1['W'] / (df1['W'] + df1['L'])).round(3)
    df1['Rdif'] = ((df1['R'] - df1['R.1']) / (df1['W'] + df1['L'])).round(1)

    df2 = df1[['ORG', 'GS.1', 'W', 'L', 'Rdif', 'Win%']]

    df3 = calc_batting_stats(df1)
    df4 = calculate_pitching_stats(df1)

    return_batting_stats = ['ORG']
    if selected_batting_stats:
        return_batting_stats.extend(selected_batting_stats)
        df2 = pd.merge(df2, df3[return_batting_stats], on=['ORG'], how='inner')
    return_pitching_stats = ['ORG']
    if selected_pitching_stats:
        return_pitching_stats.extend(selected_pitching_stats)
        df2 = pd.merge(
            df2,
            df4[return_pitching_stats],
            on=['ORG'],
            how='inner')

    df2 = df2[df2['GS.1'] >= min_games]

    del df1, df3, df4
    return df2

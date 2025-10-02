"""Calculates and returns a dataframe with basic pitching stats."""
import pandas as pd
from utils.stats_utils.normalize_innings_pitched import normalize_innings_pitched

def calculate_pitching_stats(df, min_ip_sel=200):
    df1 = df.copy()
    df1 = df1[['CID', 'IPC', 'G.1', 'GS.1', 'BF', 'ER', 'K', 'BB.1', 'IBB.1',
               'HA', '1B.1', '2B.1', '3B.1', 'HR.1', 'SV', 'SVO', 'SD',
               'MD', 'HP.1', 'SH.1', 'SF.1', 'QS', 'IR', 'IRS', 'GB',
               'FB', 'WAR.1', 'Trny']].groupby(['CID'], as_index=False).sum()

    df1['ERA'] = ((df1['ER'] / df1['IPC'])*9).round(2)

    df1['WHIP'] = ((df1['BB.1'] + df1['HA']) / df1['IPC']).round(3)

    df1['Kpct'] = (df1['K'] / df1['BF']).round(3)

    df1['BBpct'] = (df1['BB.1'] / df1['BF']).round(3)

    df1['KmBB'] = (df1['Kpct'] - df1['BBpct']).round(3)

    df1['HR/9'] = ((df1['HR.1'] / df1['IPC']) * 9).round(3)

    df1['SV%'] = (df1['SV'] / df1['SVO']).round(3)

    df1['SDpMD'] = (df1['SD'] / df1['MD']).round(3)

    df1['IRS%'] = (df1['IRS'] / df1['IR']).round(3)

    df1['GB%'] = (df1['GB'] / (df1['GB'] + df1['FB'])).round(3)

    df1['WAR/200'] = ((df1['WAR.1'] / df1['IPC']) * 200).round(1)

    df1['IP/G'] = (df1['IPC'] / df1['G.1']).round(2)


    df1['IPC'] = df1['IPC'].round(2)
    df2 = df1[['CID', 'IPC', 'ERA', 'WHIP', 'Kpct', 'BBpct', 'KmBB', 'HR/9',
               'SV%', 'SDpMD', 'IRS%', 'GB%', 'WAR/200', 'IP/G']]
    df2 = df2[df2['IPC'] >= min_ip_sel]
    return df2





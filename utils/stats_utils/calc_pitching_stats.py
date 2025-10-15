"""Calculates and returns a dataframe with basic pitching stats."""
import pandas as pd
from utils.stats_utils.normalize_innings_pitched import normalize_innings_pitched

def calculate_pitching_stats(df1, min_ip_sel=200):
    lg_era = (df1['ER'].sum()/df1['IPC'].sum())*9
    fip_const = (lg_era -
                (
                    ((13 * df1['HR.1'].sum()) + (3 * (df1['BB.1'].sum() + df1['HP.1'].sum())) - (2 * df1['K'].sum())) /
                    df1['IPC'].sum())
                )

    df1['ERA'] = ((df1['ER'] / df1['IPC'])*9).round(2)

    df1['FIP'] = ((((13 * df1['HR.1']) + (3 * (df1['BB.1'] + df1['HP.1'])) - (2 * df1['K'])) /
                   df1['IPC']) + fip_const).round(2)

    df1['WHIP'] = ((df1['BB.1'] + df1['HA']) / df1['IPC']).round(3)

    df1['K%'] = (df1['K'] / df1['BF']).round(3)

    df1['BB%'] = (df1['BB.1'] / df1['BF']).round(3)

    df1['K-BB'] = (df1['K%'] - df1['BB%']).round(3)

    df1['HR/9'] = ((df1['HR.1'] / df1['IPC']) * 9).round(3)

    df1['SV%'] = (df1['SV'] / df1['SVO']).round(3)

    df1['SD/MD'] = (df1['SD'] / df1['MD']).round(3)

    df1['IRS%'] = (df1['IRS'] / df1['IR']).round(3)

    df1['GB%'] = (df1['GB'] / (df1['GB'] + df1['FB'])).round(3)

    df1['WAR/200'] = ((df1['WAR.1'] / df1['IPC']) * 200).round(1)

    df1['IP/G'] = (df1['IPC'] / df1['G.1']).round(2)


    df1['IPC'] = df1['IPC'].round(2)
    df2 = df1.copy()
    if 'CID' in df1.columns:
        if 'VLvl' in df1.columns:
            df2 = df2[['CID', 'VLvl', 'IPC', 'ERA', 'FIP', 'WHIP', 'K%', 'BB%', 'K-BB', 'HR/9',
                       'SV%', 'SD/MD', 'IRS%', 'GB%', 'WAR/200', 'IP/G']]
        else:
            df2 = df2[['CID', 'IPC', 'ERA', 'FIP', 'WHIP', 'K%', 'BB%', 'K-BB', 'HR/9',
                       'SV%', 'SD/MD', 'IRS%', 'GB%', 'WAR/200', 'IP/G']]
        df2 = df2[df2['IPC'] >= min_ip_sel]
    else:
        df2 = df2[['ORG', 'IPC', 'ERA', 'FIP', 'WHIP', 'K%', 'BB%', 'K-BB', 'HR/9',
                   'SV%', 'SD/MD', 'IRS%', 'GB%', 'WAR/200', 'IP/G']]


    del df1
    return df2





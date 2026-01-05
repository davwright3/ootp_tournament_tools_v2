"""Calculates and returns a dataframe with basic pitching stats."""
import numpy as np
from utils.data_utils.data_store import data_store
from utils.data_utils.league_stats_store import league_stats_store


def calculate_pitching_stats(df1, min_ip_sel=200):
    lg_stats = league_stats_store.get_stats()
    fip_constant = lg_stats['lg_fip_const']

    df1['ERA'] = np.where(df1['IPC'] != 0,
                          ((df1['ER'] / df1['IPC'])*9).round(2),
                          0.00)

    df1['FIP'] = np.where(df1['IPC'] != 0,
                          ((((13 * df1['HR.1']) +
                             (3 * (df1['BB.1'] + df1['HP.1'])) -
                             (2 * df1['K'])) / df1['IPC']) +
                           fip_constant).round(2), 0.00)

    df1['WHIP'] = np.where(df1['IPC'] != 0,
                           ((df1['BB.1'] + df1['HA']) /
                            df1['IPC']).round(3), 0.00)

    df1['K%'] = np.where(df1['BF'] != 0,
                         (df1['K'] / df1['BF']).round(3),
                         .000)

    df1['BB%'] = np.where(df1['BF'] != 0,
                          (df1['BB.1'] / df1['BF']).round(3), .000)

    df1['K-BB'] = (df1['K%'] - df1['BB%']).round(3)

    df1['HR%'] = np.where(df1['BF'] != 0,
                          (df1['HR.1'] / df1['BF']).round(3),
                          .000)

    df1['HR/9'] = np.where(df1['IPC'] != 0,
                           ((df1['HR.1'] / df1['IPC']) * 9).round(3), 0.0)

    df1['SV%'] = np.where(df1['SVO'] != 0,
                          (df1['SV'] / df1['SVO']).round(3), .000)

    df1['SD/MD'] = np.where(df1['MD'] != 0,
                            (df1['SD'] / df1['MD']).round(3), .000)

    df1['IRS%'] = np.where(df1['IR'] != 0,
                           (df1['IRS'] / df1['IR']).round(3), .000)

    df1['GB%'] = np.where((df1['GB'] + df1['FB']) != 0,
                          (df1['GB'] / (df1['GB'] + df1['FB'])).round(3), 0.00)

    df1['WAR/200'] = np.where(df1['IPC'] != 0,
                              ((df1['WAR.1'] / df1['IPC']) * 200).round(1),
                              0.0)

    df1['IP/G'] = np.where(df1['G.1'] != 0,
                           (df1['IPC'] / df1['G.1']).round(2), 0.0)

    df1['QS%'] = np.where(
        df1['GS.1'] == 0,
        .000,
        (df1['QS'] / df1['GS.1']).round(2)
    )

    df1['oBABIP'] = ((df1['HA'] - df1['HR.1']) /
                     (df1['AB.1'] - df1['K'] - df1['HR.1'] + df1['SF.1'])
                     ).round(3)

    df1['IPC'] = df1['IPC'].round(2)
    df2 = df1.copy()
    if 'CID' in df1.columns:
        if 'VLvl' in df1.columns:
            df2 = df2[['CID', 'VLvl', 'IPC', 'ERA', 'FIP', 'WHIP', 'K%', 'BB%',
                       'K-BB', 'HR/9', 'HR%', 'SV%', 'SD/MD', 'IRS%', 'GB%',
                       'WAR/200', 'IP/G', 'QS%', 'oBABIP']]
        else:
            df2 = df2[['CID', 'IPC', 'ERA', 'FIP', 'WHIP', 'K%', 'BB%', 'K-BB',
                       'HR/9', 'HR%', 'SV%', 'SD/MD', 'IRS%', 'GB%', 'WAR/200',
                       'IP/G', 'QS%', 'oBABIP']]
        df2 = df2[df2['IPC'] >= min_ip_sel]
    else:
        df2 = df2[['ORG', 'IPC', 'ERA', 'FIP', 'WHIP', 'K%', 'BB%', 'K-BB',
                   'HR/9', 'HR%', 'SV%', 'SD/MD', 'IRS%', 'GB%', 'WAR/200', 'IP/G',
                   'QS%', 'oBABIP']]

    del df1
    return df2

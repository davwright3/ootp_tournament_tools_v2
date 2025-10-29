"""Script for returning calculated basic batting stats."""
import pandas as pd
import numpy as np

def calc_batting_stats(df, min_pa=0):
    """
    Calculate and return the basic batting stats for the return data frame.
    :param df: The DataFrame to be processed, pd.DataFrame
    :param min_pa: Return players with at least the min_pa, int
    :return player_stats: DataFrame containing calculated basic batting stats, pd.DataFrame
    """
    df1 = df.copy()

    df1['AVG'] = (
        (df1['H'] / df1['AB']).round(3)
    )

    df1['OBP'] = (
            (df1['H'] + df1['BB'] + df1['HP']) /
            (df1['AB'] + df1['BB'] + df1['HP'] + df1['SF'])
    )

    df1['SLG'] = (
        (df1['TB'] / df1['AB'])
    )

    df1['OPS'] = (
        (df1['OBP'] + df1['SLG']).round(3)
    )

    df1['OBP'] = df1['OBP'].round(3)

    df1['SLG'] = df1['SLG'].round(3)

    df1['wOBA'] = (
        (((.701 * df1['BB']) + (.732 * df1['HP']) + (.895 * df1['1B']) +
          (1.27 * df1['2B']) + (1.608 * df1['3B']) + (2.072 * df1['HR'])) /
         (df1['AB'] + df1['BB'] - df1['IBB'] + df1['SF'] + df1['HP'])).round(3)
    )

    df1['HRrate'] = (
        ((df1['HR'] / df1['PA']) * 600).round(1)
    )

    df1['Krate'] = (
        ((df1['SO'] / df1['PA']) * 600).round(1)
    )

    df1['BBrate'] = (
        ((df1['BB'] / df1['PA']) * 600).round(1)
    )

    df1['SBrate'] = (
        ((df1['SB'] / df1['PA']) * 600).round(1)
    )

    den = df1['SB'] + df1 ['CS']
    rate = df1['SB'] / den

    df1['SBpct'] = np.where(
        den.eq(0),
        .000,
        rate.round(3)
    )

    df1['WARrate'] = (
        ((df1['WAR'] / df1['PA']) * 600).round(1)
    )

    if 'CID' in df1.columns:
        if 'VLvl' in df1.columns:
            df2 = df1[['CID', 'VLvl', 'PA', 'AVG', 'OBP', 'SLG', 'OPS', 'wOBA', 'HRrate', 'Krate', 'BBrate', 'SBrate', 'SBpct',
                       'WARrate']]
        else:
            df2 = df1[['CID', 'PA', 'AVG', 'OBP', 'SLG', 'OPS', 'wOBA', 'HRrate', 'Krate', 'BBrate', 'SBrate', 'SBpct', 'WARrate']]
        df2 = df2[df2['PA'] >= min_pa]
    else:
        df2 = df1[['ORG', 'PA', 'AVG', 'OBP', 'SLG', 'OPS', 'wOBA', 'HRrate', 'Krate', 'BBrate', 'SBrate', 'SBpct',
                   'WARrate']]

    del df1
    return df2
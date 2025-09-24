"""
Script for calculating and returning basic stats from a data frame.
Will copy the dataframe from the datastore, and calculate
 stats based on user selections.
The result will be sent back to the stats app for display in a custom frame.
"""
from utils.data_utils.data_store import data_store

def calc_basic_batting_stats_df():
    df = data_store.get_data().copy()

    df = df[['CID', 'PA', 'AB', 'H', '1B', '2B', '3B',
             'HR','TB', 'SO', 'HP', 'BB', 'IBB', 'SF', 'SB',
             'CS', 'WAR' ]].groupby(['CID'], as_index=False).sum()
    print(df.head())

    df['AVG'] = (
        (df['H'] / df['AB']).
        apply(lambda x: f'{x:.3f}'.lstrip('0') if x < 1 else f'{x:.3f}')
    )

    df['OBP'] = (
            (df['H'] + df['BB'] + df['HP']) /
            (df['AB'] + df['BB'] + df['HP'] + df['SF'])
    )

    df['SLG'] = (
        (df['TB'] / df['AB'])
    )

    df['OPS'] = (
        (df['OBP'] + df['SLG']).
        apply(lambda x: f'{x:.3f}'.lstrip('0') if x < 1 else f'{x:.3f}')
    )

    df['OBP'] = df['OBP'].apply(lambda x: f'{x:.3f}'.lstrip('0') if x < 1 else f'{x:.3f}')

    df['SLG'] = df['SLG'].apply(lambda x: f'{x:.3f}'.lstrip('0') if x < 1 else f'{x:.3f}')

    df['wOBA'] = (
        (((.701*df['BB']) + (.732*df['HP']) + (.895*df['1B']) +
          (1.27*df['2B']) + (1.608*df['3B']) + (2.072*df['HR'])) /
        (df['AB'] + df['BB'] - df['IBB'] + df['SF'] + df['HP'])).
        apply(lambda x: f'{x:.3f}'.lstrip('0') if x < 1 else f'{x:.3f}')
    )

    df['HRrate'] = (
        ((df['HR'] / df['PA']) * 600).
        apply(lambda x: f'{x:.1f}'.lstrip('0') if x < 1 else f'{x:.1f}')
    )

    df['Krate'] = (
        ((df['SO'] /df['PA']) * 600).
        apply(lambda x: f'{x:.1f}'.lstrip('0') if x < 1 else f'{x:.1f}')
    )

    df['BBrate'] = (
        ((df['BB'] / df['PA']) * 600).
        apply(lambda x: f'{x:.1f}'.lstrip('0') if x < 1 else f'{x:.1f}')
    )

    df['SBrate'] = (
        ((df['SB'] / df['PA']) * 600).
        apply(lambda x: f'{x:.1f}'.lstrip('0') if x < 1 else f'{x:.1f}')
    )

    df['SBpct'] = (
        ((df['SB']) / (df['SB'] + df['CS'])).
        apply(lambda x: f'{x:.3f}'.lstrip('0') if x < 1 else f'{x:.3f}')
    )

    df['WARrate'] = (
        ((df['WAR'] / df['PA'])*600).
        apply(lambda x: f'{x:.1f}'.lstrip('0') if x < 1 else f'{x:.1f}')
    )


    df2 = df[['CID', 'PA', 'AVG', 'OBP', 'SLG', 'OPS', 'wOBA', 'HRrate', 'Krate', 'BBrate', 'SBrate', 'SBpct', 'WARrate']]
    print(df2)
    del df
    return df2

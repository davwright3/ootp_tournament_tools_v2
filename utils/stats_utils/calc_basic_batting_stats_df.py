"""
Script for calculating and returning basic stats from a data frame.
Will copy the dataframe from the datastore, and calculate
 stats based on user selections.
The result will be sent back to the stats app for display in a custom frame.
"""
from utils.data_utils.data_store import data_store
from utils.data_utils.card_list_store import card_list_store
import pandas as pd

def calc_basic_batting_stats_df(
        min_pa=0,
        min_value=40,
        max_value=105,
        stat_list = None,
        position_select: str= None
):
    """
    Calculates basic batting stats and returns a dataframe with the
    selected stats and players for display in a custom frame.
    :param min_pa: Minimum plate appearances for display, int
    :param stat_list: list of stats the user wants to view, list(str)
    :param position_select: The position that the user wants to view, str
    :return: Dataframe
    """
    df = data_store.get_data().copy()
    card_list = card_list_store.get_card_list().copy()

    eligible_player_set = get_eligible_players(card_list, position_select=position_select, min_value=min_value, max_value=max_value)
    del card_list
    player_stats = get_player_stats(df, min_pa)
    del df

    # If stat list is not empty
    if stat_list:
        return_list = ['CID']
        return_list.extend(stat_list)
        player_stats = player_stats[return_list]

    stats_df = pd.merge(eligible_player_set[['CID', 'Title', 'Val']], player_stats, how='inner', on='CID')

    return stats_df


def get_eligible_players(player_list: pd.DataFrame, position_select: str = None, min_value=40, max_value=105):
    """
    Returns eligible players based on user selections.
    :param player_list: Dataframe complaining the list of all available cards
    :param position_select: The position that the user wants to view, str
    :param min_value: Minimum value of cards to view, int
    :param max_value: Maximum value of cards to view, int
    :return: DataFrame
    """
    if position_select is None:
        eligible_players = player_list[[
            'Card ID', '//Card Title', 'Card Value', 'Bats', 'Throws', 'owned', 'Last 10 Price', 'Last 10 Price(VAR)'
        ]]
    else:
        eligible_players = player_list[
            player_list[position_select] == 1
        ][['Card ID', '//Card Title', 'Card Value', 'Bats', 'Throws', 'owned', 'Last 10 Price', 'Last 10 Price(VAR)']]


    eligible_players = eligible_players.rename(
        columns= {'Card ID': 'CID', '//Card Title': 'Title', 'Card Value': 'Val',
                  'Last 10 Price': 'L10', 'Last 10 Price(VAR)': 'VL10'})
    eligible_players = eligible_players[(eligible_players['Val'] <= max_value) & (eligible_players['Val'] >= min_value)]
    return eligible_players

def get_player_stats(df, min_pa=0):
    df = df[['CID', 'PA', 'AB', 'H', '1B', '2B', '3B',
             'HR','TB', 'SO', 'HP', 'BB', 'IBB', 'SF', 'SB',
             'CS', 'WAR' ]].groupby(['CID'], as_index=False).sum()

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
    df2 = df2[df2['PA'] >= min_pa]
    del df
    return df2
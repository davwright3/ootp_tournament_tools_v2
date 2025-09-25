"""
Script for calculating and returning basic stats from a data frame.
Will copy the dataframe from the datastore, and calculate
 stats based on user selections.
The result will be sent back to the stats app for display in a custom frame.
"""
import numpy as np

from utils.data_utils.data_store import data_store
from utils.data_utils.card_list_store import card_list_store
import pandas as pd

def calc_basic_batting_stats_df(
        min_pa=600,
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
    """
    Calculate and return the basic batting stats for the return data frame.
    :param df: The DataFrame to be processed, pd.DataFrame
    :param min_pa: Return players with at least the min_pa, int
    :return player_stats: DataFrame containing calculated basic batting stats, pd.DataFrame
    """
    df1 = df.copy()
    df1 = df1[['CID', 'PA', 'AB', 'H', '1B', '2B', '3B',
             'HR','TB', 'SO', 'HP', 'BB', 'IBB', 'SF', 'SB',
             'CS', 'WAR']].groupby(['CID'], as_index=False).sum()


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
        ((df1['SB'] / df1['PA']) * 600).round(3)
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

    df2 = df1[['CID', 'PA', 'AVG', 'OBP', 'SLG', 'OPS', 'wOBA', 'HRrate', 'Krate', 'BBrate', 'SBrate', 'SBpct', 'WARrate']]
    df2 = df2[df2['PA'] >= min_pa]
    del df1
    return df2


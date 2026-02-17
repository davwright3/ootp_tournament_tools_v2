"""
Script for calculating and returning basic stats from a data frame.
Will copy the dataframe from the datastore, and calculate
 stats based on user selections.
The result will be sent back to the stats app for display in a custom frame.
"""
from utils.data_utils.data_store import data_store
from utils.data_utils.card_list_store import card_list_store
from utils.stats_utils.calc_batting_stats import calc_batting_stats
from utils.stats_utils.get_eligible_players import get_eligible_players
from utils.stats_utils.cull_teams import cull_teams
import pandas as pd
from datetime import datetime, timedelta, date


def generate_basic_batting_stats_df(
        min_pa=600,
        min_value=40,
        max_value=105,
        stat_list=None,
        general_list=None,
        bat_side_select='All',
        position_select: str = None,
        collection_only_select: bool = False,
        cull_team_limit_select: int = 8,
        selected_search_term: str = None,
        variant_split_select: bool = False,
        card_id_select: int = None,
        team_select: str = None,
        cutoff_days: int = None,
):
    """
    Calculates basic batting stats and returns a dataframe with the
    selected stats and players for display in a custom frame.
    :param min_pa: Minimum plate appearances for display, int
    :param min_value: Minimum plate appearances for display, int
    :param max_value: Maximum plate appearances for display, int
    :param stat_list: list of stats the user wants to view, list(str)
    :param general_list: list of general items the user wants to view,
     list(str)
    :param bat_side_select: selected batting side, str
    :param position_select: The position that the user wants to view, str
    :param collection_only_select: whether to display only cards in collection,
     bool
    :param cull_team_limit_select: runs limit for where teams get removed, int
    :param selected_search_term: player to search for, str
    :param variant_split_select: whether to split variant selection, bool
    :param card_id_select: the id of the card, int
    :param team_select: the name of the team, str
    :param cutoff_days: the number of days to cut off the batting stats, int
    :return: Dataframe
    """
    df = cull_teams(
        data_store.get_data().copy(),
        run_cutoff=cull_team_limit_select)
    df1 = df.copy()

    if cutoff_days is not None:
        try:
            cutoff = datetime.now() - timedelta(days=cutoff_days)
            df1['Trny'] = pd.to_datetime(df1['Trny'] + ' 2026', format='%d %b %Y')
            df1 = df1[df1['Trny'] >= cutoff]

            if df1.empty:
                print("Not enough data, using full dataset")
                df1 = df
        except TypeError:
            return
    del df

    if team_select is not None:
        df1 = df1[df1['ORG'] == team_select]

    if card_id_select is not None:
        df1 = df1[df1['CID'] == card_id_select]

    if variant_split_select:
        df1 = df1[['CID', 'VLvl', 'PA', 'AB', 'H', '1B', '2B', '3B', 'HR',
                   'TB', 'SO', 'HP', 'BB', 'IBB', 'SF', 'SB', 'CS', 'WAR',
                   'RC', 'TC', 'A', 'PO', 'E', 'ZR', 'SBA',
                   'RTO']].groupby(['CID', 'VLvl'], as_index=False).sum()
    else:
        df1 = df1[['CID', 'PA', 'AB', 'H', '1B', '2B', '3B', 'HR', 'TB', 'SO',
                   'HP', 'BB', 'IBB', 'SF', 'SB', 'CS', 'WAR', 'RC', 'TC', 'A',
                   'PO', 'E', 'ZR', 'SBA',
                   'RTO']].groupby(['CID'], as_index=False).sum()

    card_list = card_list_store.get_card_list().copy()

    eligible_player_set = get_eligible_players(
        card_list,
        position_select=position_select,
        min_value=min_value,
        max_value=max_value,
        bats_side=bat_side_select,
        collection_only=collection_only_select,
        selected_search_term=selected_search_term,
    )
    del card_list
    player_stats = calc_batting_stats(df1, min_pa)
    del df1

    # If stat list is not empty
    if stat_list:
        return_list = ['CID']
        return_list.extend(stat_list)
        player_stats = player_stats[return_list]

    if general_list:
        return_list = ['CID', 'Title', 'Val']
        return_list.extend(general_list)
        eligible_player_set = eligible_player_set[return_list]
    else:
        return_list = ['CID', 'Title', 'Val']
        eligible_player_set = eligible_player_set[return_list]

    stats_df = pd.merge(
        eligible_player_set,
        player_stats,
        how='inner',
        on='CID')

    return stats_df

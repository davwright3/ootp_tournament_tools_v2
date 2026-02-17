"""
Generates DataFrame with basic player pitching stats for display.
"""
from utils.data_utils.data_store import data_store
from utils.data_utils.card_list_store import card_list_store
from utils.stats_utils.cull_teams import cull_teams
from utils.stats_utils.normalize_innings_pitched import (
    normalize_innings_pitched)
from utils.stats_utils.calc_pitching_stats import calculate_pitching_stats
from utils.stats_utils.get_eligible_players import get_eligible_players
import pandas as pd
from datetime import datetime, timedelta, date


def generate_basic_pitching_stats(
        min_ip=200,
        start_relief_cutoff=4.0,
        min_value=40,
        max_value=105,
        stat_list=None,
        general_list=None,
        throws_side_select='All',
        pitcher_type_select='All',
        collection_only_select=False,
        cull_team_limit_select=8,
        selected_search_term=None,
        selected_variant_split=False,
        card_id=None,
        team_select=None,
        cutoff_days=None,
):
    df = cull_teams(
        data_store.get_data().copy(),
        run_cutoff=cull_team_limit_select)
    stats_df = df.copy()

    if cutoff_days is not None:
        cutoff = datetime.now() - timedelta(days=cutoff_days)
        stats_df['Trny'] = pd.to_datetime(stats_df['Trny'] + ' 2026', format='%d %b %Y')
        stats_df = stats_df[stats_df['Trny'] >= cutoff]
        if stats_df.empty:
            print("Not enough seven day data, using full dataset")
            stats_df = df.copy()

    if card_id is not None:
        stats_df = stats_df[stats_df['CID'] == card_id]

    if team_select is not None:
        stats_df = stats_df[stats_df['ORG'] == team_select]

    stats_df['IPC'] = stats_df['IP'].apply(normalize_innings_pitched)
    stats_df1 = stats_df.copy()
    del stats_df
    if selected_variant_split:
        stats_df1 = stats_df1[['CID', 'VLvl', 'IPC', 'G.1', 'GS.1', 'BF',
                               'AB.1', 'ER', 'K', 'BB.1', 'IBB.1', 'HA',
                               '1B.1', '2B.1', '3B.1', 'HR.1', 'SV', 'SVO',
                               'SD', 'MD', 'HP.1', 'SH.1', 'SF.1', 'QS', 'IR',
                               'IRS', 'GB', 'FB', 'WAR.1']].groupby(['CID', 'VLvl'],
                                                as_index=False).sum()
    else:
        stats_df1 = stats_df1[['CID', 'IPC', 'G.1', 'GS.1', 'BF', 'AB.1', 'ER',
                               'K', 'BB.1', 'IBB.1', 'HA', '1B.1', '2B.1',
                               '3B.1', 'HR.1', 'SV', 'SVO', 'SD', 'MD', 'HP.1',
                               'SH.1', 'SF.1', 'QS', 'IR', 'IRS', 'GB', 'FB',
                               'WAR.1']].groupby(['CID'],
                                                         as_index=False).sum()

    card_list = card_list_store.get_card_list().copy()
    eligible_player_set = get_eligible_players(
        card_list,
        min_value=min_value,
        max_value=max_value,
        throws_side=throws_side_select,
        collection_only=collection_only_select,
        selected_search_term=selected_search_term,
    )

    calculated_stats_df = calculate_pitching_stats(
        stats_df1,
        min_ip_sel=float(min_ip))
    del stats_df1

    if pitcher_type_select == 'SP':
        calculated_stats_df = (
            calculated_stats_df[calculated_stats_df['IP/G'] >=
                                start_relief_cutoff])
    elif pitcher_type_select == 'RP':
        calculated_stats_df = (
            calculated_stats_df[calculated_stats_df['IP/G'] <
                                start_relief_cutoff])

    if stat_list is not None:
        stat_return_columns = ['CID']
        if selected_variant_split:
            stat_return_columns.extend(['VLvl'])
        stat_return_columns.extend(stat_list)
        calculated_stats_df = calculated_stats_df[stat_return_columns]

    if general_list is not None:
        general_return_columns = ['CID', 'Title', 'Val']
        general_return_columns.extend(general_list)
        eligible_player_set = eligible_player_set[general_return_columns]

    pitching_df = pd.merge(
        eligible_player_set,
        calculated_stats_df,
        how='inner',
        on='CID')

    return pitching_df

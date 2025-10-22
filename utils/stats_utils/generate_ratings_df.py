"""Return dataframe with selected calculated ratings to be viewed."""
import pandas as pd
from utils.data_utils.card_list_store import card_list_store
from utils.stats_utils.calc_ratings import calc_ratings

def generate_ratings_df(
        min_rating=40,
        max_rating=105,
        min_year=1871,
        max_year=2025,
        selected_ratings_list=None,
        selected_general_list=None,
        batter_weights=None,
        pitcher_weights=None,
        defense_weights=None,
        baserunning_weights=None,
        selected_position=None,
        collection_only=False,
        selected_card_types=None,
):
    return_columns = ['CID', 'Title', 'Val']
    if selected_ratings_list:
        return_columns.extend(selected_ratings_list)
    if selected_general_list:
        return_columns.extend(selected_general_list)

    card_df = card_list_store.get_card_list().copy()
    card_df = card_df.rename(columns={'Card ID': 'CID', '//Card Title': 'Title', 'Card Value': 'Val',
                                      'Card Type': 'Type', 'Last 10 Price': 'L10',
                                      'Last 10 Price(VAR)': 'VL10'})
    card_df = card_df[['CID', 'Title', 'Val', 'Year', 'Type', 'Bats', 'Throws', 'Contact', 'Gap',
                       'Power', 'Eye', 'Avoid Ks', 'BABIP', 'Contact vL', 'Gap vL', 'Power vL',
                       'Eye vL', 'Avoid K vL', 'BABIP vL', 'Contact vR', 'Gap vR', 'Power vR',
                       'Eye vR', 'Avoid K vR', 'BABIP vR', 'Speed', 'Steal Rate', 'Stealing',
                       'Baserunning', 'Stuff', 'Movement', 'Control', 'pHR', 'pBABIP',
                       'Stuff vL', 'Movement vL', 'Control vL', 'pHR vL', 'pBABIP vL',
                       'Stuff vR', 'Movement vR', 'Control vR', 'pHR vR', 'pBABIP vR', 'Stamina',
                       'Hold', 'GB', 'Infield Range', 'Infield Error', 'Infield Arm', 'DP',
                       'CatcherAbil', 'CatcherFrame', 'Catcher Arm', 'OF Range', 'OF Error',
                       'OF Arm', 'LearnC', 'Learn1B', 'Learn2B', 'Learn3B', 'LearnSS', 'LearnLF',
                       'LearnCF', 'LearnRF', 'era', 'tier', 'owned', 'L10', 'VL10',
                       'Pitcher Role', 'date']]
    if selected_card_types:
        card_df = card_df[card_df['Type'].isin(selected_card_types)]

    if collection_only:
        card_df = card_df[card_df['owned'] != 0]
    card_df = card_df[(card_df['Val'] >= min_rating) & (card_df['Val'] <= max_rating)]
    card_df = card_df[(card_df['Year'] >= min_year) & (card_df['Year'] <= max_year)]

    if selected_position is not None:
        card_df = card_df[card_df[selected_position] != 0]

    ratings_df = calc_ratings(
        card_df,
        batter_weights=batter_weights,
        pitcher_weights=pitcher_weights,
        defense_weights=defense_weights,
        baserunning_weights=baserunning_weights
    )
    ratings_df = ratings_df[return_columns]
    del card_df

    return ratings_df
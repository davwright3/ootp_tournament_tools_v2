"""Script for setting data for display on the batter card."""
from utils.data_utils.card_list_store import card_list_store


def set_batter_card_data(card_id: int):
    df = card_list_store.get_card_list().copy()
    filtered = df[df['Card ID'] == card_id]
    ratings_df = filtered[['Card ID', '//Card Title', 'Card Value', 'Bats',
                           'Throws', 'BABIP', 'Avoid Ks', 'Gap', 'Power',
                           'Eye', 'BABIP vL', 'Avoid K vL', 'Gap vL',
                           'Power vL', 'Eye vL', 'BABIP vR', 'Avoid K vR',
                           'Gap vR', 'Power vR', 'Eye vR', 'Speed',
                           'Steal Rate', 'Stealing', 'Baserunning', 'Sac bunt',
                           'Bunt for hit', 'GB Hitter Type', 'FB Hitter Type',
                           'BattedBallType', 'Infield Range', 'Infield Error',
                           'Infield Arm', 'DP', 'CatcherAbil', 'CatcherFrame',
                           'Catcher Arm', 'OF Range', 'OF Error', 'OF Arm',
                           'LearnC', 'Learn1B', 'Learn2B', 'Learn3B',
                           'LearnSS', 'LearnLF', 'LearnCF', 'LearnRF']]
    ratings_df = ratings_df.rename(columns={'Card ID': 'CID'})

    return ratings_df

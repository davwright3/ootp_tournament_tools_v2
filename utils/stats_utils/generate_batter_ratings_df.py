from utils.data_utils.card_list_store import card_list_store
import pandas as pd


def generate_batter_ratings_df(position_select=None):
    df = card_list_store.get_card_list().copy()
    if position_select is not None:
        df = df[df[position_select]==1]

    ratings_df = (
        df[['Card ID', '//Card Title', 'BABIP', 'BABIP vL', 'BABIP vR',
            "Avoid Ks", 'Avoid K vL', 'Avoid K vR', 'Gap', 'Gap vL',
            'Gap vR', 'Power', 'Power vL', 'Power vR', 'Eye', 'Eye vL',
            'Eye vR', 'GB Hitter Type', 'FB Hitter Type', 'BattedBallType',
            'Speed', 'Steal Rate', 'Stealing', 'Baserunning', 'Sac bunt',
            'Bunt for hit', 'Infield Range', 'Infield Error', 'Infield Arm',
            'DP', 'CatcherAbil', 'CatcherFrame', 'Catcher Arm', 'OF Range',
            'OF Error', 'OF Arm', 'LearnC', 'Learn1B', 'Learn2B', 'Learn3B',
            'LearnSS', 'LearnLF', 'LearnCF', 'LearnRF', 'Bats', 'Throws',
            'brefid']]
    )
    ratings_df = ratings_df.rename(columns={'//Card Title': 'Title', 'Card ID': 'CID',})

    return ratings_df
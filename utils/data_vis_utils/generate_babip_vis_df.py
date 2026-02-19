import pandas as pd
from utils.data_utils.data_store import data_store
from utils.data_utils.card_list_store import card_list_store


def generate_babip_vis_df():
    cards = card_list_store.get_card_list()[
        ['Card ID', '//Card Title', 'BABIP', 'BABIP vL', 'BABIP vR',
         'BattedBallType']].copy()
    cards = cards.rename(columns={'Card ID': 'CID', '//Card Title': 'Title',
                                  'BABIP vL': 'vL', 'BABIP vR': 'vR'})

    data = data_store.get_data()[
        ['CID', 'PA', 'AB', 'H', 'HR', 'SO', 'SF']].copy()
    data = data.groupby(['CID']).sum()
    data = data[data['PA'] >= 1000]

    merge_df = (pd.merge(cards, data, on='CID', how='right')
                .reset_index(drop=True))
    merge_df['BABIP_calc'] = (
            (merge_df['H'] - merge_df['HR']) /
            (merge_df['AB'] - merge_df['SO'] - merge_df['HR'] +
             merge_df['SF'])).round(3)
    final_df = merge_df[['BABIP', 'BABIP_calc', 'Title', 'PA', 'vL',
                         'vR', 'BattedBallType']]
    return final_df

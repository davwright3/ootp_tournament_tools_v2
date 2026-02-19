import pandas as pd
from utils.data_utils.data_store import data_store
from utils.data_utils.card_list_store import card_list_store


def generate_bip_rate_df():
    cards = card_list_store.get_card_list()[
        ['Card ID', '//Card Title', 'Avoid Ks', 'Eye',]].copy()
    cards = cards.rename(columns={'Card ID': 'CID', '//Card Title': 'Title'})

    data = data_store.get_data()[
        ['CID', 'PA', 'HR', 'SO', 'BB', 'IBB', 'HP']].copy()
    data = data.groupby(['CID']).sum()
    data = data[data['PA'] >= 600]
    # Get total balls in play
    data['BIP'] = (
            ((data['PA'] - data['SO'] - data['BB'] -
              data['HP'] - data['IBB']) / data['PA']) * 600).round(0)

    data = pd.merge(cards, data, how='left', on=['CID'])
    final_df = data[['Avoid Ks', 'Eye', 'BIP', 'Title']].copy()
    return final_df
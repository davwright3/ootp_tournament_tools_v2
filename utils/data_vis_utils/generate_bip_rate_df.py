import pandas as pd
from utils.data_utils.data_store import data_store
from utils.data_utils.card_list_store import card_list_store


def generate_bip_rate_df():
    cards = card_list_store.get_card_list()[['Card ID', '//Card Title', 'Power', 'Power vL', 'Power vR', 'BattedBallType']].copy()
    cards = cards.rename(columns={'Card ID': 'CID', '//Card Title': 'Title', 'Power': 'POW', 'Power vL': 'vL', 'Power vR': 'vR'})
    data = data_store.get_data()[['CID', 'PA', 'HR', 'SO', 'BB', 'IBB', 'HP']].copy()
    data = data.groupby(['CID']).sum()
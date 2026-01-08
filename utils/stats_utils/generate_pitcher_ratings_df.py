import pandas as pd
from utils.data_utils.card_list_store import card_list_store


def generate_pitcher_ratings_df():
    df = card_list_store.get_card_list().copy()
    df = df[['Card ID', '//Card Title', 'Card Value', 'Stuff', 'Movement', 'Control', 'pHR',
             'pBABIP', 'Stuff vL', 'Movement vL', 'Control vL', 'pHR vL',
             'pBABIP vL', 'Stuff vR', 'Movement vR', 'Control vR', 'pHR vR',
             'pBABIP vR', 'Fastball', 'Slider', 'Curveball', 'Changeup',
             'Cutter', 'Sinker', 'Splitter', 'Forkball', 'Screwball',
             'Circlechange', 'Knucklecurve', 'Knuckleball', 'Stamina', 'Hold',
             'GB', 'Velocity', 'Arm Slot', 'brefid']]
    df = df.rename(columns={'Card ID': 'CID', '//Card Title': 'Title'})
    return df
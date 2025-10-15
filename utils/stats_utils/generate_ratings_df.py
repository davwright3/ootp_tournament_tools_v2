"""Return dataframe with selected calculated ratings to be viewed."""
import pandas as pd
from utils.data_utils.card_list_store import card_list_store

def generate_ratings_df(
        min_rating=40,
        max_rating=105,
        min_year=1871,
        max_year=2025,
        selected_ratings_list=None
):
    card_df = card_list_store.get_card_list().copy()
    card_df = card_df.rename(columns={'Card ID': 'CID', '//Card Title': 'Title', 'Card Value': 'Val'})

    card_df = card_df[(card_df['Val'] >= min_rating) & (card_df['Val'] <= max_rating)]
    card_df = card_df[(card_df['Year'] >= min_year) & (card_df['Year'] <= max_year)]


    card_df = card_df[['CID', 'Title', 'Year']]

    return card_df
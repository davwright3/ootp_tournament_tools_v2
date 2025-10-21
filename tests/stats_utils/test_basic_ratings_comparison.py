import pandas as pd
import pytest
from utils.stats_utils.generate_ratings_df import generate_ratings_df

def test_returns_selected_columns_and_respects_ranges(
        stub_card_list_store,
        stub_calc_ratings
):
    selected_ratings = ['Contact', 'Power']
    selected_general = ['L10']

    df = generate_ratings_df(
        selected_ratings_list=selected_ratings,
        selected_general_list=selected_general,
    )

    assert len(df) == 1
    assert set(df.columns) == {'CID', 'Title', 'Val', 'Contact', 'Power', 'L10'}

    row = df.iloc[0]
    assert row['CID'] == 11111
    assert row['Title'] == 'Player A'

def test_collection_only_filters_owned_zero(
        stub_card_list_store,
        stub_calc_ratings
):
    df = generate_ratings_df(
        collection_only=True,
    )

    assert len(df) == 1
    assert df.iloc[0]['CID'] == 11111


def test_selected_position_filters(
        stub_card_list_store,
        stub_calc_ratings
):
    df = generate_ratings_df(
        selected_position='LearnCF'
    )

    assert len(df) == 1
    assert df.iloc[0]['CID'] == 11111
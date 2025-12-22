"""Test the ratings calculation module."""
import pandas as pd
import utils.stats_utils.calc_ratings as mod

card_df = {
    'Contact': 1,
    'Gap': 1,
    'Power': 1,
    'Eye': 1,
    'Avoid Ks': 1,
    'BABIP': 1,
    'Contact vL': 1,
    'Gap vL': 1,
    'Power vL': 1,
    'Eye vL': 1,
    'Avoid K vL': 1,
    'BABIP vL': 1,
    'Contact vR': 1,
    'Gap vR': 1,
    'Power vR': 1,
    'Eye vR': 1,
    'Avoid K vR': 1,
    'BABIP vR': 1,
    'Speed': 1,
    'Steal Rate': 1,
    'Stealing': 1,
    'Baserunning': 1,
    'Stuff': 1,
    'Movement': 1,
    'Control': 1,
    'pHR': 1,
    'pBABIP': 1,
    'Stuff vL': 1,
    'Movement vL': 1,
    'Control vL': 1,
    'pHR vL': 1,
    'pBABIP vL': 1,
    'Stuff vR': 1,
    'Movement vR': 1,
    'Control vR': 1,
    'pHR vR': 1,
    'pBABIP vR': 1,
    'Infield Range': 1,
    'Infield Error': 1,
    'Infield Arm': 1,
    'DP': 1,
    'CatcherAbil': 1,
    'CatcherFrame': 1,
    'Catcher Arm': 1,
    'OF Range': 1,
    'OF Error': 1,
    'OF Arm': 1
}

bat_weights = {
    'weight_babip': 2.1,
    'weight_babip_vL': 2.1,
    'weight_babip_vR': 2.1,
    'weight_avoidk': 2,
    'weight_avoidk_vL': 2,
    'weight_avoidk_vR': 2,
    'weight_gap': 2,
    'weight_gap_vL': 2,
    'weight_gap_vR': 2,
    'weight_power': 2,
    'weight_power_vL': 2,
    'weight_power_vR': 2,
    'weight_eye': 2,
    'weight_eye_vL': 2,
    'weight_eye_vR': 2,
}

pit_weights = {
    'weight_stuff': 2.1,
    'weight_phr': 2.1,
    'weight_pbabip': 2.1,
    'weight_control': 2,
    'weight_stuff_vL': 2,
    'weight_stuff_vR': 2,
    'weight_phr_vL':2,
    'weight_phr_vR': 2,
    'weight_pbabip_vL': 2,
    'weight_pbabip_vR': 2,
    'weight_control_vL': 2,
    'weight_control_vR': 2,
}


def test_ratings_no_weights():
    df = mod.calc_ratings(card_df)

    assert df['BatOA'] == 5
    assert df['BatvL'] == 5
    assert df['Catch Def'] == 3
    assert df['IF Def'] == 4
    assert df['PitOA'] == 4
    assert df['PitvL'] == 4

def test_ratings_weighted(
):
    df = mod.calc_ratings(card_df, batter_weights=bat_weights, pitcher_weights=pit_weights)

    assert df['BatOA'] == 10.1
    assert df['BatvL'] == 10.1
    assert df['Catch Def'] == 3
    assert df['PitOA'] == 8.3
    assert df['PitvL'] == 8


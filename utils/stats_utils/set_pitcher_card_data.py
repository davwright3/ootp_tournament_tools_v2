from utils.data_utils.card_list_store import card_list_store


def set_pitcher_card_data(card_id=None):
    if card_id is None:
        return

    df = card_list_store.get_card_list().copy()
    player_df = df[df['Card ID'] == card_id]
    player_df = player_df[['Card ID', '//Card Title', 'Card Value', 'Bats',
                           'Throws', 'Stuff', 'Movement', 'Control', 'pHR',
                           'pBABIP', 'Stuff vL', 'Movement vL', 'Control vL',
                           'pHR vL', 'pBABIP vL', 'Stuff vR', 'Movement vR',
                           'Control vR', 'pHR vR', 'pBABIP vR', 'Fastball',
                           'Slider', 'Curveball', 'Changeup', 'Cutter',
                           'Sinker', 'Splitter', 'Forkball', 'Screwball',
                           'Circlechange', 'Knucklecurve', 'Knuckleball',
                           'Stamina', 'Hold', 'GB', 'Velocity', 'Arm Slot']]
    player_df = player_df.rename(columns={'Card ID': 'CID'})

    return player_df

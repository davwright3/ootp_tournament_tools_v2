"""Return dataframe with eligible players based on inputs."""
import pandas as pd


def get_eligible_players(
        player_list: pd.DataFrame,
        position_select: str = None,
        min_value=40,
        max_value=105,
        bats_side='All',
        throws_side='All',
        collection_only=False,
        selected_search_term: str = None,
):
    """
    Returns eligible players based on user selections.
    :param player_list: Dataframe complaining the list of all available cards
    :param position_select: The position that the user wants to view, str
    :param min_value: Minimum value of cards to view, int
    :param max_value: Maximum value of cards to view, int
    :param bats_side: Bats side, str
    :param throws_side: Throws side, str
    :param collection_only: If true, only return eligible players
    :param selected_search_term: Search term to filter by, str
    :return: DataFrame
    """
    eligible_players = player_list.copy()
    if position_select is None:
        eligible_players = eligible_players[[
            'Card ID', '//Card Title', 'Card Value', 'Bats', 'Throws', 'owned',
            'Last 10 Price', 'Last 10 Price(VAR)']]
    else:
        eligible_players = eligible_players[
            eligible_players[position_select] != 0
        ][['Card ID', '//Card Title', 'Card Value', 'Bats', 'Throws', 'owned',
           'Last 10 Price', 'Last 10 Price(VAR)']]

    eligible_players.loc[:, 'B'] = eligible_players['Bats'].apply(
        lambda x: 'R' if x == 1 else 'L' if x == 2 else 'S')
    eligible_players.loc[:, 'T'] = eligible_players['Throws'].apply(
        lambda x: 'R' if x == 1 else 'L')

    if collection_only:
        eligible_players = eligible_players[eligible_players['owned'] > 0]

    if bats_side != 'All':
        eligible_players = eligible_players[eligible_players['B'] == bats_side]

    if throws_side != 'All':
        eligible_players = (
            eligible_players[eligible_players['T'] == throws_side])

    if selected_search_term is not None:
        eligible_players = (
            eligible_players[eligible_players['//Card Title'].str.contains(
                selected_search_term, case=False, na=False)])

    eligible_players = eligible_players.rename(
        columns={'Card ID': 'CID', '//Card Title': 'Title',
                 'Card Value': 'Val', 'Last 10 Price': 'L10',
                 'Last 10 Price(VAR)': 'VL10'})
    eligible_players = (
        eligible_players[(eligible_players['Val'] <= max_value) &
                         (eligible_players['Val'] >= min_value)])
    return eligible_players

"""
Return the proper format for innings pitched.
Takes the innings pitched in each tournament by the pitchers and adjusts
due to factoring by thirds.
"""


def normalize_innings_pitched(innings_pitched):
    """
    Normalize the innings pitched from an individual tournament.
    Adjusts innings to account for MLB innings being in thirds, while normal
    floats are in tenths.
    :param innings_pitched: The innings pitched from a DataFrame entry, float
    :return: whole_innings + fractional innings, float
    """
    whole_innings = round(innings_pitched)
    fractional_innings = (innings_pitched - whole_innings) / .3
    return whole_innings + fractional_innings

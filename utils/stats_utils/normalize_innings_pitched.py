"""
Return the proper format for innings pitched.
Takes the innings pitched in each tournament by the pitchers and adjusts
due to factoring by thirds.
"""

def normalize_innings_pitched(innings_pitched):
    whole_innings = round(innings_pitched)
    fractional_innings = (innings_pitched - whole_innings) / .3
    return whole_innings + fractional_innings
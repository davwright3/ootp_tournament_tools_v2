"""Calculate a return a dataframe with the ratings calculated."""
import pandas as pd

def calc_ratings(df, batter_weights=None):
    # Batter ratings
    if batter_weights is None:
        df['BatOA'] = df['Gap'] + df['Power'] + df['Eye'] + df['Avoid Ks'] + df['BABIP']
        df['BatvL'] = df['Gap vL'] + df['Power vL'] + df['Eye vL'] + df['Avoid K vL'] + df['BABIP vL']
        df['BatvR'] = df['Gap vR'] + df['Power vR'] + df['Eye vR'] + df['Avoid K vR'] + df['BABIP vR']
    else:
        df['BatOA'] = ((df['Gap'] * batter_weights['weight_gap']) +
                       (df['Power'] * batter_weights['weight_power'])  +
                       (df['Eye'] * batter_weights['weight_eye']) +
                       (df['Avoid Ks'] * batter_weights['weight_avoidk']) +
                       (df['BABIP'] * batter_weights['weight_babip'])
                       )
        df['BatvL'] = ((df['Gap vL'] * batter_weights['weight_gap_vL']) +
                       (df['Power vL'] * batter_weights['weight_power_vL']) +
                       (df['Eye vL'] * batter_weights['weight_eye_vL']) +
                       (df['Avoid K vL'] * batter_weights['weight_avoidk_vL']) +
                       (df['BABIP vL'] * batter_weights['weight_babip_vL'])
                       )
        df['BatvR'] = ((df['Gap vR'] * batter_weights['weight_gap_vR']) +
                       (df['Power vR'] * batter_weights['weight_power_vR']) +
                       (df['Eye vR'] * batter_weights['weight_eye_vR']) +
                       (df['Avoid K vR'] * batter_weights['weight_avoidk_vR']) +
                       (df['BABIP vR'] * batter_weights['weight_babip_vR'])
                       )

    df['Bsr'] = df['Speed'] + df['Steal Rate'] + df['Stealing'] + df['Baserunning']

    # Fielder ratings
    df['Catch Def'] = df['CatcherAbil'] + df['CatcherFrame'] + df['Catcher Arm']
    df['IF Def'] = df['Infield Range'] + df['Infield Error'] + df['Infield Arm'] + df['DP']
    df['OF Def'] = df['OF Range'] + df['OF Error'] + df['OF Arm']

    # Pitcher ratings
    df['PitchOA'] = df['Stuff'] + df['pHR'] + df['pBABIP'] + df['Control']
    df['PitchvL'] = df['Stuff vL'] + df['pHR vL'] + df['pBABIP vL'] + df['Control vL']
    df['PitchvR'] = df['Stuff vR'] + df['pHR vR'] + df['pBABIP vR'] + df['Control vR']

    return df
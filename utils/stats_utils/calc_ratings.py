"""Calculate a return a dataframe with the ratings calculated."""


def calc_ratings(
        df,
        batter_weights=None,
        pitcher_weights=None,
        defense_weights=None,
        baserunning_weights=None
):
    # Batter ratings
    if batter_weights is None:
        df['BatOA'] = (df['Gap'] + df['Power'] + df['Eye'] +
                       df['Avoid Ks'] + df['BABIP'])
        df['BatvL'] = (df['Gap vL'] + df['Power vL'] + df['Eye vL'] +
                       df['Avoid K vL'] + df['BABIP vL'])
        df['BatvR'] = (df['Gap vR'] + df['Power vR'] + df['Eye vR'] +
                       df['Avoid K vR'] + df['BABIP vR'])
    else:
        df['BatOA'] = ((df['Gap'] * batter_weights['weight_gap']) +
                       (df['Power'] * batter_weights['weight_power']) +
                       (df['Eye'] * batter_weights['weight_eye']) +
                       (df['Avoid Ks'] * batter_weights['weight_avoidk']) +
                       (df['BABIP'] * batter_weights['weight_babip'])
                       )
        df['BatvL'] = ((df['Gap vL'] * batter_weights['weight_gap_vL']) +
                       (df['Power vL'] * batter_weights['weight_power_vL']) +
                       (df['Eye vL'] * batter_weights['weight_eye_vL']) +
                       (df['Avoid K vL'] *
                        batter_weights['weight_avoidk_vL']) +
                       (df['BABIP vL'] * batter_weights['weight_babip_vL'])
                       )
        df['BatvR'] = ((df['Gap vR'] * batter_weights['weight_gap_vR']) +
                       (df['Power vR'] * batter_weights['weight_power_vR']) +
                       (df['Eye vR'] * batter_weights['weight_eye_vR']) +
                       (df['Avoid K vR'] *
                        batter_weights['weight_avoidk_vR']) +
                       (df['BABIP vR'] * batter_weights['weight_babip_vR'])
                       )
    df['BatSplit'] = df['BatvL'] - df['BatvR']

    # Pitcher ratings

    if pitcher_weights is None:
        df['PitOA'] = df['Stuff'] + df['pHR'] + df['pBABIP'] + df['Control']
        df['PitvL'] = (df['Stuff vL'] + df['pHR vL'] +
                       df['pBABIP vL'] + df['Control vL'])
        df['PitvR'] = (df['Stuff vR'] + df['pHR vR'] +
                       df['pBABIP vR'] + df['Control vR'])
    else:
        df['PitOA'] = ((df['Stuff'] * pitcher_weights['weight_stuff']) +
                       (df['pHR'] * pitcher_weights['weight_phr']) +
                       (df['pBABIP'] * pitcher_weights['weight_pbabip']) +
                       (df['Control'] * pitcher_weights['weight_control']))
        df['PitvL'] = ((df['Stuff vL'] * pitcher_weights['weight_stuff_vL']) +
                       (df['pHR vL'] * pitcher_weights['weight_phr_vL']) +
                       (df['pBABIP vL'] *
                        pitcher_weights['weight_pbabip_vL']) +
                       (df['Control vL'] *
                        pitcher_weights['weight_control_vL']))
        df['PitvR'] = ((df['Stuff vR'] * pitcher_weights['weight_stuff_vR']) +
                       (df['pHR vR'] * pitcher_weights['weight_phr_vR']) +
                       (df['pBABIP vR'] *
                        pitcher_weights['weight_pbabip_vR']) +
                       (df['Control vR'] *
                        pitcher_weights['weight_control_vR']))

    df['PitSplit'] = df['PitvL'] - df['PitvR']

    # Fielder ratings
    if defense_weights is None:
        df['Catch Def'] = (df['CatcherAbil'] + df['CatcherFrame'] +
                           df['Catcher Arm'])
        df['IF Def'] = (df['Infield Range'] + df['Infield Error'] +
                        df['Infield Arm'] + df['DP'])
        df['OF Def'] = df['OF Range'] + df['OF Error'] + df['OF Arm']
    else:
        df['Catch Def'] = ((df['CatcherAbil'] *
                            defense_weights['weight_catch_abil']) +
                           (df['CatcherFrame'] *
                            defense_weights['weight_catch_frame']) +
                           (df['Catcher Arm'] *
                            defense_weights['weight_catch_arm'])
                           )
        df['IF Def'] = ((df['Infield Range'] *
                         defense_weights['weight_infield_range']) +
                        (df['Infield Error'] *
                         defense_weights['weight_infield_error']) +
                        (df['Infield Arm'] *
                         defense_weights['weight_infield_arm']) +
                        (df['DP'] * defense_weights['weight_turn_dp'])
                        )
        df['OF Def'] = ((df['OF Range'] *
                         defense_weights['weight_outfield_range']) +
                        (df['OF Error'] *
                         defense_weights['weight_outfield_error']) +
                        (df['OF Arm'] * defense_weights['weight_outfield_arm'])
                        )

    # Baserunning ratings
    if baserunning_weights is None:
        df['Bsr'] = (df['Speed'] + df['Steal Rate'] + df['Stealing'] +
                     df['Baserunning'])
    else:
        df['Bsr'] = ((df['Speed'] * baserunning_weights['weight_speed']) +
                     (df['Steal Rate'] *
                      baserunning_weights['weight_steal_agg']) +
                     (df['Stealing'] *
                      baserunning_weights['weight_steal_ability']) +
                     (df['Baserunning'] *
                      baserunning_weights['weight_baserunning'])
                     )

    return df

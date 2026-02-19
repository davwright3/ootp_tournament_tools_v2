"""Calculate a return a dataframe with the ratings calculated."""
import numpy as np


def calc_ratings(
        df,
        batter_weights=None,
        pitcher_weights=None,
        defense_weights=None,
        baserunning_weights=None,
        run_env_weights=None,
):

    #Set weights from run environment
    if run_env_weights:
        bat_vl_mask = df['B'].isin(['R', 'S'])
        df['BABIP vL'] = np.where(
            bat_vl_mask,
            round(df['BABIP vL'] * run_env_weights['avg_rhb'], 1),
            round(df['BABIP vL'] * run_env_weights['avg_lhb'], 1)
        )
        df['Power vL'] = np.where(
            bat_vl_mask,
            round(df['Power vL'] * run_env_weights['hr_rhb'], 1),
            round(df['Power vL'] * run_env_weights['hr_lhb'], 1)
        )
        df['Gap vL'] = np.where(
            bat_vl_mask,
            round(df['Gap vL'] * run_env_weights['avg_rhb'] * run_env_weights[
                'doubles'], 1),
            round(df['Gap vL'] * run_env_weights['avg_lhb'] * run_env_weights[
                'doubles'], 1),
        )
        bat_vr_mask = df['B'].isin(['L', 'S'])
        df['BABIP vR'] = np.where(
            bat_vr_mask,
            round(df['BABIP vR'] * run_env_weights['avg_lhb'],1),
            round(df['BABIP vR'] * run_env_weights['avg_rhb'], 1)
        )
        df['Power vR'] = np.where(
            bat_vr_mask,
            round(df['Power vR'] * run_env_weights['hr_lhb'], 1),
            round(df['Power vR'] * run_env_weights['hr_rhb'], 1)
        )
        df['Gap vR'] = np.where(
            bat_vr_mask,
            round(df['Gap vR'] * run_env_weights['avg_lhb'] * run_env_weights['doubles'], 1),
            round(df['Gap vR'] * run_env_weights['avg_rhb'] * run_env_weights['doubles'], 1)
        )

    # Batter ratings
    if batter_weights is None:
        df['BatOA'] = (df['Gap'] + df['Power'] + df['Eye'] +
                       df['Avoid Ks'] + df['BABIP'])
        df['BatvL'] = (df['Gap vL'] + df['Power vL'] + df['Eye vL'] +
                       df['Avoid K vL'] + df['BABIP vL'])
        df['BatvR'] = (df['Gap vR'] + df['Power vR'] + df['Eye vR'] +
                       df['Avoid K vR'] + df['BABIP vR'])
    else:
        df['BatOA'] = round(((df['Gap'] * batter_weights['weight_gap']) +
                       (df['Power'] * batter_weights['weight_power']) +
                       (df['Eye'] * batter_weights['weight_eye']) +
                       (df['Avoid Ks'] * batter_weights['weight_avoidk']) +
                       (df['BABIP'] * batter_weights['weight_babip'])
                       ), 2)
        df['BatvL'] = round(((df['Gap vL'] * batter_weights['weight_gap_vL']) +
                       (df['Power vL'] * batter_weights['weight_power_vL']) +
                       (df['Eye vL'] * batter_weights['weight_eye_vL']) +
                       (df['Avoid K vL'] *
                        batter_weights['weight_avoidk_vL']) +
                       (df['BABIP vL'] * batter_weights['weight_babip_vL'])
                       ), 2)
        df['BatvR'] = round(((df['Gap vR'] * batter_weights['weight_gap_vR']) +
                       (df['Power vR'] * batter_weights['weight_power_vR']) +
                       (df['Eye vR'] * batter_weights['weight_eye_vR']) +
                       (df['Avoid K vR'] *
                        batter_weights['weight_avoidk_vR']) +
                       (df['BABIP vR'] * batter_weights['weight_babip_vR'])
                       ),2)
    df['BatSplit'] = round((df['BatvL'] - df['BatvR']), 2)

    # Pitcher ratings

    if pitcher_weights is None:
        df['PitOA'] = df['Stuff'] + df['pHR'] + df['pBABIP'] + df['Control']
        df['PitvL'] = (df['Stuff vL'] + df['pHR vL'] +
                       df['pBABIP vL'] + df['Control vL'])
        df['PitvR'] = (df['Stuff vR'] + df['pHR vR'] +
                       df['pBABIP vR'] + df['Control vR'])
    else:
        df['PitOA'] = round(((df['Stuff'] * pitcher_weights['weight_stuff']) +
                       (df['pHR'] * pitcher_weights['weight_phr']) +
                       (df['pBABIP'] * pitcher_weights['weight_pbabip']) +
                       (df['Control'] * pitcher_weights['weight_control'])
                       ), 2)
        df['PitvL'] = round(((df['Stuff vL'] * pitcher_weights['weight_stuff_vL']) +
                       (df['pHR vL'] * pitcher_weights['weight_phr_vL']) +
                       (df['pBABIP vL'] *
                        pitcher_weights['weight_pbabip_vL']) +
                       (df['Control vL'] *
                        pitcher_weights['weight_control_vL'])), 2)
        df['PitvR'] = round(((df['Stuff vR'] * pitcher_weights['weight_stuff_vR']) +
                       (df['pHR vR'] * pitcher_weights['weight_phr_vR']) +
                       (df['pBABIP vR'] *
                        pitcher_weights['weight_pbabip_vR']) +
                       (df['Control vR'] *
                        pitcher_weights['weight_control_vR'])), 2)

    df['PitSplit'] = round((df['PitvL'] - df['PitvR']), 2)

    # Fielder ratings
    if defense_weights is None:
        df['Catch Def'] = (df['CatcherAbil'] + df['CatcherFrame'] +
                           df['Catcher Arm'])
        df['IF Def'] = (df['Infield Range'] + df['Infield Error'] +
                        df['Infield Arm'] + df['DP'])
        df['OF Def'] = df['OF Range'] + df['OF Error'] + df['OF Arm']
    else:
        df['Catch Def'] = round(((df['CatcherAbil'] *
                            defense_weights['weight_catch_abil']) +
                           (df['CatcherFrame'] *
                            defense_weights['weight_catch_frame']) +
                           (df['Catcher Arm'] *
                            defense_weights['weight_catch_arm'])
                           ), 2)
        df['IF Def'] = round(((df['Infield Range'] *
                         defense_weights['weight_infield_range']) +
                        (df['Infield Error'] *
                         defense_weights['weight_infield_error']) +
                        (df['Infield Arm'] *
                         defense_weights['weight_infield_arm']) +
                        (df['DP'] * defense_weights['weight_turn_dp'])
                        ), 2)
        df['OF Def'] = round(((df['OF Range'] *
                         defense_weights['weight_outfield_range']) +
                        (df['OF Error'] *
                         defense_weights['weight_outfield_error']) +
                        (df['OF Arm'] * defense_weights['weight_outfield_arm'])
                        ), 2)

    # Baserunning ratings
    if baserunning_weights is None:
        df['Bsr'] = (df['Speed'] + df['Steal Rate'] + df['Stealing'] +
                     df['Baserunning'])
    else:
        df['Bsr'] = round(((df['Speed'] * baserunning_weights['weight_speed']) +
                     (df['Steal Rate'] *
                      baserunning_weights['weight_steal_agg']) +
                     (df['Stealing'] *
                      baserunning_weights['weight_steal_ability']) +
                     (df['Baserunning'] *
                      baserunning_weights['weight_baserunning'])
                     ), 2)

    return df

import pandas as pd
from utils.stats_utils.generate_basic_batting_stats_df import generate_basic_batting_stats_df
from utils.stats_utils.generate_batter_ratings_df import generate_batter_ratings_df
from utils.data_utils.data_store import data_store
from utils.data_utils.card_list_store import card_list_store


def generate_batter_slide_df(position_select=None):
    stats_df = generate_basic_batting_stats_df(min_pa=600,
                                               position_select='LearnC')
    ratings_df = generate_batter_ratings_df(position_select=position_select)
    full_df = pd.merge(ratings_df, stats_df, how='inner', on=['CID', 'Title'])

    # Build defensive and baserunning values
    full_df['InfValue'] = full_df['Infield Range'] + full_df['Infield Error'] + \
                          full_df['Infield Arm'] + full_df['DP']
    full_df['OFValue'] = full_df['OF Range'] + full_df['OF Error'] + full_df[
        'OF Arm']
    full_df['CatchValue'] = full_df['CatcherAbil'] + full_df['CatcherFrame'] + \
                          full_df['Catcher Arm']
    full_df['BaserunningVal'] = full_df['Speed'] + full_df['Steal Rate'] + \
                                full_df['Stealing']

    # Get max values for player values
    woba_max = full_df['wOBA'].max()
    catch_max = full_df['CatchValue'].max()
    infield_max = full_df['InfValue'].max()
    of_max = full_df['OFValue'].max()
    baserunning_max = full_df['BaserunningVal'].max()

    full_df['woba_score'] = round(((full_df['wOBA'] * 10) ** 2) / ((woba_max * 10) ** 2), 2)
    full_df['catch_score'] = round((full_df['CatchValue'] ** 2) / (catch_max ** 2), 2)
    full_df['infield_score'] = round((full_df['InfValue'] ** 2) / (infield_max ** 2), 2)
    full_df['outfield_score'] = round((full_df['OFValue'] ** 2) / (of_max ** 2), 2)
    full_df['baserunning_score'] = round((full_df['BaserunningVal'] ** 2) / (baserunning_max ** 2), 2)

    if position_select is None:
        full_df['total_score'] = (full_df['woba_score'] * 8) + (full_df['baserunning_score'] * 2)
    elif position_select == 'LearnC':
        full_df['total_score'] = (full_df['woba_score'] * 7) + (full_df['baserunning_score'] * 1.5) + (full_df['catch_score'] * 1.5)
    elif position_select == '1B' or position_select == '3B':
        full_df['total_score'] = (full_df['woba_score'] * 7) + (full_df['baserunning_score'] * 1.5) + (full_df['infield_score'] * 1.5)
    elif position_select == '2B' or position_select == 'SS':
        full_df['total_score'] = (full_df['woba_score'] * 6) + (full_df['baserunning_score'] * 1.5) + (full_df['infield_score'] * 2.5)
    else:
        full_df['total_score'] = (full_df['woba_score'] * 6) + (full_df['baserunning_score'] * 1.5) + (full_df['outfield_score'] * 2.5)

    full_df = full_df.sort_values(by=['total_score'], ascending=False)

    # Set rankings
    full_df['pa_rank'] = full_df['PA'].rank(ascending=False, method='first').astype(int)
    full_df['avg_rank'] = full_df['AVG'].rank(ascending=False, method='first').astype(int)
    full_df['obp_rank'] = full_df['OBP'].rank(ascending=False, method='first').astype(int)
    full_df['slg_rank'] = full_df['SLG'].rank(ascending=False, method='first').astype(int)
    full_df['ops_rank'] = full_df['OPS'].rank(ascending=False, method='first').astype(int)
    full_df['woba_rank'] = full_df['wOBA'].rank(ascending=False, method='first').astype(int)
    full_df['rc_rate_rank'] = full_df['RCrate'].rank(ascending=False, method='first').astype(int)
    full_df['hr_rate_rank'] = full_df['HRrate'].rank(ascending=False, method='first').astype(int)
    full_df['k_rate_rank'] = full_df['Krate'].rank(ascending=True, method='first').astype(int)
    full_df['bb_rate_rank'] = full_df['BBrate'].rank(ascending=False, method='first').astype(int)
    full_df['sb_rate_rank'] = full_df['SBrate'].rank(ascending=False, method='first').astype(int)
    full_df['sb_pct_rank'] = full_df['SBpct'].rank(ascending=False, method='first').astype(int)
    full_df['war_rate_rank'] = full_df['WARrate'].rank(ascending=False, method='first').astype(int)
    full_df['zr_rank'] = full_df['ZRrate'].rank(ascending=False, method='first').astype(int)
    full_df['fld_pct_rank'] = full_df['Fld%'].rank(ascending=False, method='first').astype(int)
    full_df['catch_rank'] = full_df['catch_score'].rank(ascending=False, method='first').astype(int)
    full_df['infield_rank'] = full_df['infield_score'].rank(ascending=False, method='first').astype(int)
    full_df['outfield_rank'] = full_df['outfield_score'].rank(ascending=False, method='first').astype(int)
    full_df['baserunning_rank'] = full_df['baserunning_score'].rank(ascending=False, method='first').astype(int)
    full_df['total_rank'] = full_df['total_score'].rank(ascending=False, method='first').astype(int)

    return full_df

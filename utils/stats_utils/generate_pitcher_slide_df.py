import pandas as pd
from utils.stats_utils.generate_basic_pitching_stats_df import generate_basic_pitching_stats
from utils.stats_utils.generate_pitcher_ratings_df import generate_pitcher_ratings_df


def generate_pitcher_slide_df(pitcher_type=None, selected_cutoff_days=7):
    ratings_df = generate_pitcher_ratings_df()
    if pitcher_type == 'SP':
        stats_df = generate_basic_pitching_stats(min_ip=200, cutoff_days=selected_cutoff_days, pitcher_type_select='SP', selected_variant_split=True)
    elif pitcher_type == 'RP':
        stats_df = generate_basic_pitching_stats(min_ip=200, cutoff_days=selected_cutoff_days, pitcher_type_select='RP', selected_variant_split=True)
    else:
        stats_df = generate_basic_pitching_stats(min_ip=200, cutoff_days=selected_cutoff_days, selected_variant_split=True)

    slide_df = pd.merge(ratings_df, stats_df, on=['CID', 'Title'], how='inner')
    slide_df['pit_val'] = (slide_df['K%'] - (slide_df['BB%'] + (slide_df['HR%'] * 3)))
    pit_val_max = slide_df['pit_val'].max()
    pit_val_min = slide_df['pit_val'].min()
    pit_val_max_norm = pit_val_max - pit_val_min
    pit_val_min_norm = 0

    slide_df['pit_val_norm'] = slide_df['pit_val'] - pit_val_min
    slide_df['pit_score'] = round((slide_df['pit_val_norm'] / pit_val_max_norm)*10, 2)
    slide_df = slide_df.sort_values(by=['pit_score'], ascending=False)

    # Generate the rankings
    slide_df['era_rank'] = slide_df['ERA'].rank(ascending=True, method='first').astype(int)
    slide_df['fip_rank'] = slide_df['FIP'].rank(ascending=True, method='first').astype(int)
    slide_df['whip_rank'] = slide_df['WHIP'].rank(ascending=True, method='first').astype(int)
    slide_df['k_pct_rank'] = slide_df['K%'].rank(ascending=False, method='first').astype(int)
    slide_df['bb_pct_rank'] = slide_df['BB%'].rank(ascending=True, method='first').astype(int)
    slide_df['k_minus_bb_rank'] = slide_df['K-BB'].rank(ascending=False, method='first').astype(int)
    slide_df['hr_pct_rank'] = slide_df['HR%'].rank(ascending=True, method='first').astype(int)
    slide_df['hr_per_9_rank'] = slide_df['HR/9'].rank(ascending=True, method='first').astype(int)
    slide_df['sv_pct_rank'] = slide_df['SV%'].rank(ascending=False, method='first').astype(int)
    slide_df['sd_md_rank'] = slide_df['SD/MD'].rank(ascending=False, method='first').astype(int)
    slide_df['irs_pct_rank'] = slide_df['IRS%'].rank(ascending=True, method='first').astype(int)
    slide_df['gb_pct_rank'] = slide_df['GB%'].rank(ascending=False, method='first').astype(int)
    slide_df['war_rank'] = slide_df['WAR/200'].rank(ascending=False, method='first').astype(int)
    slide_df['ip_game_rank'] = slide_df['IP/G'].rank(ascending=False, method='first').astype(int)
    slide_df['qs_pct_rank'] = slide_df['QS%'].rank(ascending=False, method='first').astype(int)
    slide_df['obabip_rank'] = slide_df['oBABIP'].rank(ascending=True, method='first').astype(int)
    slide_df['score_rank'] = slide_df['pit_score'].rank(ascending=False, method='first').astype(int)
    return slide_df
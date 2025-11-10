from utils.data_utils.data_store import data_store
from utils.stats_utils.normalize_innings_pitched import (
    normalize_innings_pitched
)


def calc_league_stats():
    df = data_store.get_data().copy()
    df['IPC'] = df['IP'].apply(normalize_innings_pitched)

    # Batting stats
    lg_pa = df['PA'].sum()
    lg_ab = df['AB'].sum()
    lg_hits = df['H'].sum()
    lg_single = df['1B'].sum()
    lg_double = df['2B'].sum()
    lg_triple = df['3B'].sum()
    lg_hr = df['HR'].sum()
    lg_tb = df['TB'].sum()
    lg_sb = df['SB'].sum()
    lg_cs = df['CS'].sum()
    lg_so = df['SO'].sum()
    lg_bb = df['BB'].sum()
    lg_sf = df['SF'].sum()
    lg_ibb = df['IBB'].sum()
    lg_hp = df['HP'].sum()

    # Pitching stats
    lg_gs = df['GS.1'].sum()
    lg_ip = df['IPC'].sum()
    lg_er = df['ER'].sum()
    lg_ir = df['IR'].sum()
    lg_irs = df['IRS'].sum()
    lg_qs = df['QS'].sum()
    lg_gb = df['GB'].sum()
    lg_fb = df['FB'].sum()
    lg_sd = df['SD'].sum()
    lg_md = df['MD'].sum()

    # Defense stats
    lg_assists = df['A'].sum()
    lg_putouts = df['PO'].sum()
    lg_error = df['E'].sum()

    # Calculated batting stats
    lg_avg = (lg_hits / lg_ab).round(3)
    lg_obp = ((lg_hits + lg_bb + lg_hp) /
              (lg_ab + lg_bb + lg_hp + lg_sf)).round(3)
    lg_slg = (lg_tb / lg_ab).round(3)
    lg_woba = (((.701 * lg_bb) + (.732 * lg_hp) + (.895 * lg_single) +
                (1.27 * lg_double) + (1.608 * lg_triple) + (2.072 * lg_hr)) /
               (lg_ab + lg_bb - lg_ibb + lg_sf + lg_hp)).round(3)
    lg_ops = (lg_obp + lg_slg).round(3)
    lg_so_rate = (lg_so / lg_pa).round(3)
    lg_bb_rate = (lg_bb / lg_pa).round(3)
    lg_hr_rate = ((lg_hr / lg_pa) * 600).round(1)
    lg_sb_rate = ((lg_sb / lg_pa)*600).round(1)
    lg_sb_pct = (lg_sb / (lg_sb + lg_cs)).round(3)

    # Calculated pitching stats
    lg_era = ((lg_er / lg_ip) * 9).round(2)
    fip_const = lg_era - (((13 * lg_hr) + (3 * (lg_bb + lg_hp)) -
                           (2 * lg_so)) / lg_ip).round(2)
    lg_fip = ((((13 * lg_hr) + (3 * (lg_bb + lg_hp)) -
                (2 * lg_so)) / lg_ip) + fip_const).round(2)
    lg_irs_pct = (lg_irs / lg_ir).round(3)
    lg_sd_per_md = (lg_sd / lg_md).round(2)
    lg_qs_pct = (lg_qs / lg_gs).round(3)
    lg_gb_per_fb = (lg_gb / lg_fb).round(2)

    # Calculated fielding stats
    lg_fld_pct = ((lg_putouts + lg_assists) /
                  (lg_putouts + lg_assists + lg_error)).round(3)

    lg_avg_string = f'{lg_avg:.3f}'.lstrip('0')
    lg_obp_string = f'{lg_obp:.3f}'.lstrip('0')
    lg_slg_string = f'{lg_slg:.3f}'.lstrip('0')
    lg_woba_string = f'{lg_woba:.3f}'.lstrip('0')
    lg_ops_string = f'{lg_ops:.3f}'.lstrip('0')
    lg_so_rate_string = f'{lg_so_rate:.3f}'.lstrip('0')
    lg_bb_rate_string = f'{lg_bb_rate:.3f}'.lstrip('0')
    lg_hr_rate_string = f'{lg_hr_rate:.1f}'.lstrip('0')
    lg_sb_rate_string = f'{lg_sb_rate:.1f}'.lstrip('0')
    lg_sb_pct_string = f'{lg_sb_pct:.3f}'.lstrip('0')

    lg_era_string = f'{lg_era:.2f}'.lstrip('0')
    lg_fip_string = f'{lg_fip:.2f}'.lstrip('0')
    lg_irs_pct_string = f'{lg_irs_pct:.3f}'.lstrip('0')
    lg_sd_per_md_string = f'{lg_sd_per_md:.3f}'.lstrip('0')
    lg_qs_pct_string = f'{lg_qs_pct:.3f}'.lstrip('0')
    lg_gb_per_fb_string = f'{lg_gb_per_fb:.3f}'.lstrip('0')

    lg_fld_pct_string = f'{lg_fld_pct:.3f}'.lstrip('0')

    lg_stats = {
        'lg_fip_const': fip_const,
        'lg_avg': lg_avg_string,
        'lg_obp': lg_obp_string,
        'lg_slg': lg_slg_string,
        'lg_ops': lg_ops_string,
        'lg_woba': lg_woba_string,
        'lg_so_rate': lg_so_rate_string,
        'lg_bb_rate': lg_bb_rate_string,
        'lg_hr_rate': lg_hr_rate_string,
        'lg_sb_rate': lg_sb_rate_string,
        'lg_sb_pct': lg_sb_pct_string,
        'lg_era': lg_era_string,
        'lg_fip': lg_fip_string,
        'lg_irs_pct': lg_irs_pct_string,
        'lg_sd_per_md': lg_sd_per_md_string,
        'lg_qs_pct': lg_qs_pct_string,
        'lg_gb_rate': lg_gb_per_fb_string,
        'lg_fld_pct': lg_fld_pct_string,
    }
    return lg_stats

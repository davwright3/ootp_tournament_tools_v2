from utils.stats_utils.generate_basic_pitching_stats_df import (
    generate_basic_pitching_stats)


def get_player_pitching_stats(card_id, team_select=None, cutoff_days=None):
    if team_select is None and cutoff_days is None:
        df = generate_basic_pitching_stats(min_ip=1, card_id=card_id)
    elif team_select is None:
        df = generate_basic_pitching_stats(min_ip=1, card_id=card_id, cutoff_days=cutoff_days)
    else:
        df = generate_basic_pitching_stats(
            min_ip=1, card_id=card_id, team_select=team_select)

    if df.empty:
        stats = {
            'ply_ip': '0.00',
            'ply_era': '0.00',
            'ply_fip': '0.00',
            'ply_k_pct': '0.00',
            'ply_bb_pct': '0.00',
            'ply_k-bb': '0.00',
            'ply_hr_rate': '0.00',
            'ply_sv_pct': '0.00',
            'ply_sd_md': '0.00',
            'ply_irs_pct': '0.00',
            'ply_ipg': '0.00',
            'ply_gb_pct': '0.00',
            'ply_qs_pct': '0.00',
            'ply_war_rate': '0.00',
            'ply_babip': '0.00',
        }
    else:
        stats = {
            'ply_ip': f"{df.iloc[0]['IPC']}",
            'ply_era': f"{df.iloc[0]['ERA']}".lstrip('0'),
            'ply_fip': f"{df.iloc[0]['FIP']}".lstrip('0'),
            'ply_k_pct': f"{df.iloc[0]['K%']}".lstrip('0'),
            'ply_bb_pct': f"{df.iloc[0]['BB%']}".lstrip('0'),
            'ply_k-bb': f"{df.iloc[0]['K-BB']}".lstrip('0'),
            'ply_hr_rate': f"{df.iloc[0]['HR/9']}".lstrip('0'),
            'ply_sv_pct': f"{df.iloc[0]['SV%']}".lstrip('0'),
            'ply_sd_md': f"{df.iloc[0]['SD/MD']}".lstrip('0'),
            'ply_irs_pct': f"{df.iloc[0]['IRS%']}".lstrip('0'),
            'ply_ipg': f"{df.iloc[0]['IP/G']}".lstrip('0'),
            'ply_gb_pct': f"{df.iloc[0]['GB%']}".lstrip('0'),
            'ply_qs_pct': f"{df.iloc[0]['QS%']}".lstrip('0'),
            'ply_war_rate': f"{df.iloc[0]['WAR/200']}".lstrip('0'),
            'ply_babip': f"{df.iloc[0]['oBABIP']}".lstrip('0'),
        }

    return stats

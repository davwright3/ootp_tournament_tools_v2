from utils.stats_utils.generate_basic_batting_stats_df import (
    generate_basic_batting_stats_df)


def get_player_batting_stats(card_id, selected_team=None, cutoff_days=None):
    if selected_team is None and cutoff_days is None:
        df = generate_basic_batting_stats_df(
            min_pa=1,
            card_id_select=card_id
        )
    elif selected_team is None:
        df = generate_basic_batting_stats_df(
            min_pa=1,
            cutoff_days=cutoff_days,
            card_id_select=card_id
        )
    else:
        df = generate_basic_batting_stats_df(
            min_pa=1,
            card_id_select=card_id,
            team_select=selected_team
        )

    if df.empty:
        stats = {
            'ply_pa': '0',
            'ply_avg': '.000',
            'ply_obp': '.000',
            'ply_slg': '.000',
            'ply_ops': '.000',
            'ply_woba': '.000',
            'ply_hr_rate': '0.0',
            'ply_k': '0.0',
            'ply_bb': '0.0',
            'ply_sb': '0.0',
            'ply_sb_pct': '.000',
            'ply_war': '0.0',
        }
    else:
        player_pa = f"{df['PA'].iloc[0]}".lstrip('0')
        player_avg = f"{df['AVG'].iloc[0]}".lstrip('0')
        player_obp = f"{df['OBP'].iloc[0]}".lstrip('0')
        player_slg = f"{df['SLG'].iloc[0]}".lstrip('0')
        player_ops = f"{df['OPS'].iloc[0]}".lstrip('0')
        player_woba = f"{df['wOBA'].iloc[0]}".lstrip('0')
        player_hr = f"{df['HRrate'].iloc[0]}".lstrip('0')
        player_k = f"{df['Krate'].iloc[0]}".lstrip('0')
        player_bb = f"{df['BBrate'].iloc[0]}".lstrip('0')
        player_sb = f"{df['SBrate'].iloc[0]}".lstrip('0')
        player_sb_pct = f"{df['SBpct'].iloc[0]}".lstrip('0')
        player_war = f"{df['WARrate'].iloc[0]}".lstrip('0')

        stats = {
            'ply_pa': player_pa,
            'ply_avg': player_avg,
            'ply_obp': player_obp,
            'ply_slg': player_slg,
            'ply_ops': player_ops,
            'ply_woba': player_woba,
            'ply_hr_rate': player_hr,
            'ply_k': player_k,
            'ply_bb': player_bb,
            'ply_sb': player_sb,
            'ply_sb_pct': player_sb_pct,
            'ply_war': player_war,
        }

    return stats

"""Util for cutting teams that faced empty teams (Joe Unknowns)."""
import logging


def cull_teams(df, run_cutoff=8):
    """
    Cull teams based on runs scored per game.
    Base cut off point will be 8 runs per game.
    User will have the opportunity to set based on need.
    """
    logger = logging.getLogger('apps.basic_stats_app')

    df1 = df.copy()
    # Create a new dataframe which will create a list of teams that are okay.
    df1 = df1.groupby(['ORG', 'Trny'], as_index=False)[['GS.1', 'R']].sum()
    df1['R/G'] = (df1['R'] / df1['GS.1']).round(2)
    teams_ok = df1.loc[df1['R/G'] < run_cutoff, ['ORG', 'Trny']]

    # Merge by ignoring the rows to drop
    df_filtered = df.merge(teams_ok, on=['ORG', 'Trny'], how='inner')
    removed_count = len(df) - len(df_filtered)
    removed_pct = (removed_count / len(df))
    if removed_pct > .35:
        logger.warning(f'''
        Removed {removed_count} out of {len(df)} rows.
        This is a {round(removed_pct, 2) * 100}% removal rate.
        Please check data set for valid data.
        ''')
    else:
        logger.info(f'''
        Removed {removed_count} out of {len(df)} rows of data.
        This is a {round(removed_pct, 2) * 100}% removal rate..
        ''')
    return df_filtered

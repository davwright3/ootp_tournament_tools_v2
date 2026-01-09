import pandas as pd
import numpy as np
from utils.data_utils.mlb_season_stats_store import mlb_stats_store
from utils.data_utils.stadium_factors_store import stadium_factors_store

def get_run_environment(selected_year=2010):
    seasons_df = mlb_stats_store.get_stats_dataframe().copy()

    df_2010 = seasons_df[seasons_df.Season == 2010].copy()
    df_selected_year = seasons_df[seasons_df.Season == selected_year].copy()

    def babip(df):
        denom = (df['AB'] - df['SO'] - df['HR'] + df['SF'])
        return np.where(denom != 0, (df['H'] - df['HR']) / denom, np.nan)

    df_2010['BABIP'] = babip(df_2010)
    df_selected_year['BABIP'] = babip(df_selected_year)

    df_2010['HRrate'] = np.where(df_2010['PA'] !=0, (df_2010['HR'] / df_2010['PA']) * 600, np.nan)
    df_selected_year['HRrate'] = np.where(df_selected_year['PA'] != 0, (df_selected_year['HR'] / df_selected_year['PA']) * 600, np.nan)

    df_2010['XBHrate'] = np.where(df_2010['PA'] != 0, ((df_2010['2B'] + df_2010['3B']) / df_2010['PA']) * 600, np.nan)
    df_selected_year['XBHrate'] = np.where(df_selected_year['PA'] != 0, ((df_selected_year['2B'] + df_selected_year['3B']) / df_selected_year['PA']) * 600, np.nan)

    df_2010['Krate'] = np.where(df_2010['PA'] != 0,
                                (df_2010['SO'] / df_2010['PA']) * 600, np.nan)
    df_selected_year['Krate'] = np.where(df_selected_year['PA'] != 0, (df_selected_year['SO'] / df_selected_year['PA']) * 600, np.nan)

    df_2010['BBrate'] = np.where(df_2010['PA'] != 0,
                                (df_2010['BB'] / df_2010['PA']) * 600, np.nan)
    df_selected_year['BBrate'] = np.where(df_selected_year['PA'] != 0, (
                df_selected_year['BB'] / df_selected_year['PA']) * 600, np.nan)

    df_2010['SBrate'] = np.where(df_2010['PA'] != 0, (df_2010['SB'] / df_2010['PA']) * 600, np.nan)
    df_selected_year['SBrate'] = np.where(df_selected_year['PA'] != 0, (df_selected_year['SB'] / df_selected_year['PA']) * 600, np.nan)

    df_2010['SBPct'] = np.where((df_2010['SB'] + df_2010['CS']) != 0, (df_2010['SB'] / (df_2010['SB'] + df_2010['CS'])).round(3), np.nan)
    df_selected_year['SBPct'] = np.where((df_selected_year['SB'] + df_selected_year['CS']) != 0, (
                df_selected_year['SB'] / (df_selected_year['SB'] + df_selected_year['CS'])).round(3),
                                np.nan)

    if len(df_selected_year) == 0 or len(df_2010) == 0:
        raise ValueError('Missing rows from selected year')

    babip_ratio = np.nan
    hr_ratio = np.nan
    xbh_ratio = np.nan
    k_ratio = np.nan
    bb_ratio = np.nan
    sb_ratio = np.nan
    sb_pct_ratio = np.nan
    if pd.notna(df_2010.iloc[0]['BABIP']) and df_2010.iloc[0]['BABIP'] != 0:
        babip_ratio = (df_selected_year.iloc[0]['BABIP'] / df_2010.iloc[0]['BABIP']).round(3)
    if pd.notna(df_2010.iloc[0]['HRrate']) and df_2010.iloc[0]['HRrate'] != 0:
        hr_ratio = (df_selected_year.iloc[0]['HRrate'] / df_2010.iloc[0]['HRrate']).round(3)
    if pd.notna(df_2010.iloc[0]['XBHrate']) and df_2010.iloc[0]['XBHrate'] != 0:
        xbh_ratio = (df_selected_year.iloc[0]['XBHrate'] / df_2010.iloc[0]['XBHrate']).round(3)
    if pd.notna(df_2010.iloc[0]['Krate']) and df_2010.iloc[0]['Krate'] != 0:
        k_ratio = (df_selected_year.iloc[0]['Krate'] / df_2010.iloc[0]['Krate']).round(3)
    if pd.notna(df_2010.iloc[0]['BBrate']) and df_2010.iloc[0]['BBrate'] != 0:
        bb_ratio = (df_selected_year.iloc[0]['BBrate'] / df_2010.iloc[0]['BBrate']).round(3)
    if pd.notna(df_2010.iloc[0]['SBrate']) and df_2010.iloc[0]['SBrate'] != 0:
        sb_ratio = (df_selected_year.iloc[0]['SBrate'] / df_2010.iloc[0]['SBrate']).round(3)
    if pd.notna(df_2010.iloc[0]['SBPct']) and df_2010.iloc[0]['SBPct'] != 0:
        sb_pct_ratio = (df_selected_year.iloc[0]['SBPct'] / df_2010.iloc[0]['SBPct']).round(3)

    return_df = pd.DataFrame([
        {'BABIP': babip_ratio,
         'HRrate': hr_ratio,
         'XBHrate': xbh_ratio,
         'Krate': k_ratio,
         'BBrate': bb_ratio,
         'SBrate': sb_ratio,
         'SBPct': sb_pct_ratio,}])

    return return_df


def get_park_factors():
    stadium_df = stadium_factors_store.get_park_factors()

    return stadium_df
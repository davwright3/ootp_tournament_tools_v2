"""Base for configuration testing."""
import os
import sys
import tempfile
import configparser
import pytest
import tkinter as tk
from pathlib import Path
import pandas as pd
import types

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

collect_ignore_glob = ['utils/view_utils/*.py']

REQUIRED_COLS = [
    'CID', '//Card Title', 'Card Value', 'Year', 'Card Type', 'Bats', 'Throws',
    'Contact', 'Gap', 'Power', 'Eye', 'Avoid Ks', 'BABIP',
    'Contact vL', 'Gap vL', 'Power vL', 'Eye vL', 'Avoid K vL', 'BABIP vL',
    'Contact vR', 'Gap vR', 'Power vR', 'Eye vR', 'Avoid K vR', 'BABIP vR',
    'Speed', 'Steal Rate', 'Stealing', 'Baserunning',
    'Stuff', 'Movement', 'Control', 'pHR', 'pBABIP',
    'Stuff vL', 'Movement vL', 'Control vL', 'pHR vL', 'pBABIP vL',
    'Stuff vR', 'Movement vR', 'Control vR', 'pHR vR', 'pBABIP vR',
    'Stamina', 'Hold', 'GB',
    'Infield Range', 'Infield Error', 'Infield Arm', 'DP',
    'CatcherAbil', 'CatcherFrame', 'Catcher Arm',
    'OF Range', 'OF Error', 'OF Arm',
    'LearnC', 'Learn1B', 'Learn2B', 'Learn3B', 'LearnSS', 'LearnLF', 'LearnCF', 'LearnRF',
    'era', 'tier', 'owned', 'Last 10 Price', 'Last 10 Price(VAR)',
    'Pitcher Role', 'date'
]

def pytest_configure(config):
    """Configuration for global testing."""
    df_default = pd.DataFrame(
        {
            'Card ID': [73691, 73885],
            '//Card Title': ['Card A', 'Card B'],
            'Card Value': [48, 59],
            'Bats': [1, 2],
            'Throws': [1, 2],
            'owned': [0, 1],
            'Last 10 Price': [125, 2000],
            'Last 10 Price(VAR)': [1234, 250],
            'Learn2B': [1, 0],
        }
    )

    fake_module = types.ModuleType('utils.data_utils.card_list_store')
    fake_store = types.SimpleNamespace(
        get_card_list=lambda: df_default.copy(),
        load_card_list=lambda *a, **k: None
    )
    fake_module.card_list_store = fake_store

    sys.modules['utils.data_utils.card_list_store'] = fake_module

@pytest.fixture(scope='session', autouse=True)
def _headless_env():
    """Hide some API warnings on macOS."""
    os.environ.setdefault("TK_SILENCE_DEPRECATION", '1')


@pytest.fixture
def tk_root():
    """Provide a tk root for widget testing."""
    root = tk.Tk()
    root.withdraw()
    yield root
    # Make sure pending after callbacks get cleared
    try:
        root.update_idletasks()
    except tk.TclError:
        pass
    root.destroy()


@pytest.fixture
def temp_settings_files(tmp_path, monkeypatch):
    """
    Create a temp settings.ini file and settings_default.ini to point
    config_utils to use during testing.
    Redirects settings.ini and settings_defaults.ini to a temporary folder.
    """
    app_dir = tmp_path / "settings_dir"
    app_dir.mkdir()

    user_ini = app_dir / "settings.ini"
    default_ini = app_dir / "settings_default.ini"

    # Override the path-returning functions before import
    monkeypatch.setattr(
        "utils.config_utils.get_user_settings_path.get_user_settings_path",
        lambda app_name: str(user_ini)
    )
    monkeypatch.setattr(
        "utils.config_utils.get_default_settings_path.get_default_settings_path",
        lambda: str(default_ini)
    )

    # Return paths so tests can use them
    return {"user": user_ini, "default": default_ini}

@pytest.fixture
def sample_stats_df():
    """
    Fixture for testing of basic batting stats.
    Creates a small, clean dataframe for stat testing.
    Note: CID 73691 is Yosver Zulueta, 2B eligible for testing purposes.
    Note: CID 73885 is Mke Zunino, 2B INELIGIBLE for testing purposes.
    :return: Dataframe containing batting stats.
    """

    data = {
        'CID': [73691, 73691, 73885, 73885],
        'ORG': ['A', 'A', 'B', 'B'],
        'PA': [20, 30, 30, 10],
        'AB': [18, 26, 27, 9],
        'H': [6, 8, 11, 2],
        '1B': [4, 5, 7, 2],
        '2B': [1, 1, 1, 0],
        '3B': [0, 1, 1, 0],
        'HR': [1, 1, 2, 0],
        'TB': [10, 14, 20, 2],
        'SO': [4, 3, 6, 2],
        'HP': [0, 0, 0, 1],
        'BB': [1, 2, 1, 1],
        'IBB': [0, 0, 0, 0],
        'SF': [1, 2, 2, 0],
        'SB': [2, 0, 1, 0],
        'CS': [1, 0, 1, 0],
        'WAR': [.3, .6, .1, .3],
        'RC': [1, 2, 3, 4],
        'ZR': [0.1, 0.2, 0.3, 0.4],
        'SBA': [1, 1, 2, 0],
        'RTO': [1, 1, 0, 1],
        'R': [3, 3, 2, 9],
        'IP': [6.1, 5.2, 7.1, 8.0],
        'G.1': [1, 1, 1, 2],
        'GS.1': [1, 0, 1, 0],
        'BF': [24, 21, 30, 34],
        'AB.1': [18, 16, 26, 30],
        'ER': [1, 2, 1, 3],
        'R.1': [3, 2, 3, 6],
        'W': [1, 0, 1, 0],
        'L': [0, 2, 1, 0],
        'K': [4, 6, 5, 3],
        'BB.1': [1, 2, 0, 1],
        'IBB.1': [0, 0, 0, 0],
        'HA': [5, 4, 3, 6],
        '1B.1': [3, 2, 2, 3],
        '2B.1': [1, 0, 1, 1],
        '3B.1': [0, 1, 0, 0],
        'HR.1': [1, 1, 0, 2],
        'SV': [1, 0, 2, 0],
        'SVO': [2, 0, 3, 0],
        'SD': [1, 1, 1, 2],
        'MD': [0, 1, 0, 1],
        'HP.1': [0, 1, 0, 0],
        'SH.1': [0, 0, 1, 0],
        'SF.1': [1, 0, 0, 0],
        'QS': [0, 0, 1, 0],
        'IR': [0, 2, 0, 3],
        'IRS': [0, 1, 0, 1],
        'GB': [8, 4, 7, 9],
        'FB': [4, 2, 3, 4],
        'WAR.1': [.4, .3, .6, .7],
        'TC': [1, 1, 1, 1],
        'PO': [1, 1, 1, 1],
        'A': [0, 0, 0, 0],
        'E': [0, 0, 0, 0],
        'Trny': [1, 1, 1, 1]
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def patched_batting_data_store(monkeypatch, sample_stats_df):
    import utils.stats_utils.generate_basic_batting_stats_df as mod

    fake_df = types.SimpleNamespace(
        get_data= lambda: sample_stats_df.copy(),
    )
    monkeypatch.setattr(mod, 'data_store', fake_df, raising=True)
    return sample_stats_df

@pytest.fixture
def patched_pitching_data_store(monkeypatch, sample_stats_df):
    import utils.stats_utils.generate_basic_pitching_stats_df as mod

    fake_df = types.SimpleNamespace(
        get_data= lambda: sample_stats_df.copy(),
    )
    monkeypatch.setattr(mod, 'data_store', fake_df, raising=True)
    return sample_stats_df

@pytest.fixture
def patched_team_data_store(monkeypatch, sample_stats_df):
    import utils.stats_utils.generate_basic_team_stats_df as mod

    fake_df = types.SimpleNamespace(
        get_data= lambda: sample_stats_df.copy(),
    )
    monkeypatch.setattr(mod, 'data_store', fake_df, raising=True)
    return sample_stats_df


@pytest.fixture
def sample_card_df():
    base = {c: 0 for c in REQUIRED_COLS}

    # Row A
    a = base.copy()
    a.update({
        'CID': 11111,
        '//Card Title': 'Player A',
        'Card Value': 50,
        'Year': 1999,
        'Card Type': 5,
        'Bats': 2,
        'Throws': 1,
        'Contact': 60,
        'Power': 55,
        'Gap': 50,
        'LearnCF': 1,
        'owned': 1,
        'Last 10 Price': 125,
        'Last 10 Price(VAR)': 250
    })

    b = base.copy()
    b.update({
        'CID': 22222,
        '//Card Title': 'Player B',
        'Card Value': 30,
        'Year': 2010,
        'Card Type': 5,
        'Bats': 1,
        'Throws': 2,
        'Contact': 60,
        'Power': 55,
        'Gap': 50,
        'LearnCF': 0,
        'owned': 0,
        'Last 10 Price': 125,
        'Last 10 Price(VAR)': 250
    })

    return pd.DataFrame([a, b])


@pytest.fixture
def stub_card_list_store(monkeypatch, sample_card_df):
    from types import SimpleNamespace
    fake_store = SimpleNamespace(get_card_list=lambda: sample_card_df)
    monkeypatch.setattr(
        'utils.stats_utils.generate_ratings_df.card_list_store',
        fake_store,
        raising=True
    )

@pytest.fixture
def stub_calc_ratings(monkeypatch):
    def _fake(df, **kwargs):
        return df.copy()

    monkeypatch.setattr(
        'utils.stats_utils.calc_ratings.calc_ratings',
        _fake,
        raising=True
    )

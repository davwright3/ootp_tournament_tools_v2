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
        'ORG': ['A', 'A', 'A', 'A'],
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
        'R': [3, 4, 2, 6],
        'IP': [6.1, 5.2, 7.1, 8.0]
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def sample_card_df():
    """
    Fixture for testing modules that require the card databse.
    Creates a small dataframe for card testing.
    :return: dataframe containing card data.
    """
    cards = {
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
    df = pd.DataFrame(cards)
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
def patched_card_list_store(monkeypatch, sample_card_df):
    """Patches the card list inside the stats module."""
    fake_df = sample_card_df.copy()

    import utils.stats_utils.generate_basic_batting_stats_df as mod
    fake_df = types.SimpleNamespace(
        get_card_list= lambda: sample_card_df.copy(),
    )
    monkeypatch.setattr(mod, 'card_list_store', fake_df, raising=True)
    return sample_card_df




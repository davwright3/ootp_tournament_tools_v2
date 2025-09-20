import sys
import importlib
from pathlib import Path
import configparser
from pickle import FALSE

import pytest

CONFIG_MOD = 'utils.config_utils.load_save_settings'

@pytest.fixture
def patched_paths_imported(monkeypatch, tmp_path):
    """
    Redirect SETTINGS_PATH and DEFAULT SETTINGS PATH into a temp dir
    by patching the helpers before importing the module.
    Stub verify_settings_up_to_date to avoid side effects.
    """
    base = tmp_path / 'settings_sandbox'
    base.mkdir()

    user_ini = base / 'settings.ini'
    defaults_ini = base / 'default.ini'

    # PAtch the helper functions to compute the paths
    monkeypatch.setattr(
        "utils.config_utils.get_user_settings_path.get_user_settings_path",
        lambda app_name: str(user_ini),
        raising=False
    )
    monkeypatch.setattr(
        'utils.config_utils.get_default_settings_path.get_default_settings_path',
        lambda: str(defaults_ini),
        raising=False
    )
    monkeypatch.setattr(
        'utils.config_utils.verify_settings_up_to_date.verify_settings_up_to_date',
        lambda *_args, **_kw: None,
        raising=False
    )

    # Ensure clean import state per test
    sys.modules.pop(CONFIG_MOD, None)
    mod = importlib.import_module(CONFIG_MOD)
    importlib.reload(mod)

    return {'mod': mod, 'user': user_ini, 'default': defaults_ini, 'base': base}

@pytest.fixture
def patched_paths_no_import(monkeypatch, tmp_path):
    """Patch path helpers.  Does not import module."""
    base = tmp_path / 'settings_sandbox'
    base.mkdir()
    user_ini = base / 'settings.ini'
    default_ini = base / 'settings_default.ini'

    monkeypatch.setattr(
        'utils.config_utils.get_user_settings_path.get_user_settings_path',
        lambda app_name: str(user_ini),
        raising=False
    )
    monkeypatch.setattr(
        'utils.config_utils.get_default_settings_path.get_default_settings_path',
        lambda: str(default_ini),
        raising=False
    )
    monkeypatch.setattr(
        'utils.config_utils.verify_settings_up_to_date.verify_settings_up_to_date',
        lambda *_args, **_kw: None,
        raising=False
    )

    sys.modules.pop(CONFIG_MOD, None)

    return {'user': user_ini, 'default': default_ini, 'base': base}



def test_first_import_creates_user_ini_when_default_missing(patched_paths_no_import):
    user = patched_paths_no_import['user']
    default = patched_paths_no_import['default']

    # Ensure no files exist
    assert not user.exists()
    assert not default.exists()

    # Import the module
    mod = importlib.import_module(CONFIG_MOD)
    importlib.reload(mod)

    assert user.exists()

    cfg = configparser.ConfigParser()
    cfg.read(user, encoding='utf-8')
    assert cfg.sections() == []


def test_reads_defaults_when_present_first_import(patched_paths_no_import):
    import importlib, configparser
    from pathlib import Path
    CONFIG_MOD = 'utils.config_utils.load_save_settings'

    user = patched_paths_no_import['user']
    default = patched_paths_no_import['default']

    dcfg = configparser.ConfigParser()
    dcfg['TargetFiles'] = {'target_card_list': 'mycards.csv'}
    with default.open('w', encoding='utf-8') as f:
        dcfg.write(f)

    mod = importlib.import_module(CONFIG_MOD)
    importlib.reload(mod)

    assert user.exists()
    assert mod.get_setting('TargetFiles', 'target_card_list') == 'mycards.csv'


def test_save_settings_persists_current_state(patched_paths_imported):
    mod = patched_paths_imported['mod']
    user = patched_paths_imported['user']

    mod.update_setting('General', 'theme', 'dark', autosave=False)
    mod.save_settings()

    cfg = configparser.ConfigParser()
    cfg.read(user, encoding='utf-8')
    assert cfg.get('General', 'theme') == 'dark'

def test_reload_settings_pulls_external_changes(patched_paths_imported):
    mod = patched_paths_imported['mod']
    user = patched_paths_imported['user']

    cfg = configparser.ConfigParser()
    cfg['General'] = {'font_size': '16'}
    with user.open('w', encoding='utf-8') as f:
        cfg.write(f)

    mod.reload_settings()
    assert mod.get_setting('General', 'font_size') == '16'

def test_get_settings_fallback_for_missing_key(patched_paths_imported):
    mod = patched_paths_imported['mod']
    assert mod.get_setting('General', 'font_size', fallback='N/A') == 'N/A'

def test_ensure_section_called_by_update_setting(patched_paths_imported):
    mod = patched_paths_imported['mod']

    mod.update_setting('NewSection', 'foo', 'bar', autosave=False)
    mod.save_settings()
    path = patched_paths_imported['user']
    cfg = configparser.ConfigParser()
    cfg.read(path, encoding='utf-8')
    assert 'NewSection' in cfg.sections()
    assert cfg.get('NewSection', 'foo') == 'bar'

def test_atomic_write_creates_file_without_temp_leftovers(patched_paths_imported):
    mod = patched_paths_imported['mod']
    user = patched_paths_imported['user']
    base = patched_paths_imported['base']

    mod.update_setting('S', 'k', 'v', autosave=False)
    mod.save_settings()

    assert user.exists()
    leftovers = list(base.glob('*.tmp')) + list(base.glob('tmp'))
    assert leftovers == []


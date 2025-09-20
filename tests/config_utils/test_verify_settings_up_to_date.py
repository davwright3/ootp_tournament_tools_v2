import os
from configparser import ConfigParser
import shutil
import pytest

import utils.config_utils.verify_settings_up_to_date as mod

# Helper functions for later use
def write_ini(path, data: dict):
    cfg = ConfigParser()
    for section, kv in data.items():
        cfg[section] = kv
    with open(path, 'w', encoding='utf-8') as f:
        cfg.write(f)

def read_ini(path):
    cfg = ConfigParser()
    cfg.read(path, encoding='utf-8')
    return cfg

# Testing methods
def test_copies_when_user_missing(tmp_path, capsys):
    defaults = tmp_path / 'settings_default.ini'
    user = tmp_path / 'settings.ini'
    print('User path: ', user)

    write_ini(defaults, {
        'InitialTargetDirs': {
            'starting_target_folder': '/home/x/',
            'starting_data_folder': '/data/x'
        },
        'Other': {'foo': 'bar'}
    })

    assert defaults.exists() and defaults.is_file()
    assert user.parent.exists()
    assert os.access(user.parent, os.W_OK)

    mod.verify_settings_up_to_date(str(defaults), str(user))

    assert user.exists()
    ucfg = read_ini(str(user))
    assert ucfg.get('InitialTargetDirs', 'starting_target_folder') == '/home/x/'
    assert ucfg.get('Other', 'foo') == 'bar'


def test_adds_missing_keys(tmp_path):
    defaults = tmp_path / 'settings_default.ini'
    user_dir = tmp_path / 'settings.ini'
    write_ini(defaults, {'A': {'k1': 'v1', 'k2': 'v2'}})
    write_ini(user_dir, {'A': {'k1': 'custom'}})

    updated = mod.verify_settings_up_to_date(str(defaults), str(user_dir))
    assert updated is True
    cfg = read_ini(str(user_dir))
    assert cfg.get('A', 'k1') == 'custom'
    assert cfg.get('A', 'k2') == 'v2'


def test_up_to_date_returns_false(tmp_path):
    defaults = tmp_path / 'settings_default.ini'
    user = tmp_path / 'settings.ini'
    write_ini(defaults, {'A': {'k1': 'v1'}})
    write_ini(user, {'A': {'k1': 'v1'}})

    assert mod.verify_settings_up_to_date(str(defaults), str(user)) is False


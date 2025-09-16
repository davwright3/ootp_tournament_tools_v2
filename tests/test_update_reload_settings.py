"""Tests settings and reloading settings."""
def test_update_and_reload_settings(temp_settings_files):
    # Import after monkeypatch so it uses fake paths
    import importlib

    # User settings should not exist initially
    assert not temp_settings_files['user'].exists()

    import utils.config_utils.load_save_settings as lss
    importlib.reload(lss)

    # Update a settings
    lss.update_setting('TargetFiles', 'target_card_list', 'mycards.csv')
    assert temp_settings_files['user'].exists()

    val = lss.get_setting('TargetFiles', 'target_card_list')
    assert val == 'mycards.csv'

    lss.reload_settings()
    assert lss.get_setting('TargetFiles', 'target_card_list') == 'mycards.csv'



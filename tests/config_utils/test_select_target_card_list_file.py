"""
Test the scripts for selecting the target card list.
"""
import pytest
from unittest.mock import patch, MagicMock

import utils.config_utils.select_target_card_list_file as mod

@pytest.fixture
def fake_target_var():
    return MagicMock()

@pytest.fixture
def mock_settings():
    with patch(f'{mod.__name__}.settings_module') as mock_settings:
        mock_settings.get.return_value = None
        yield mock_settings


def test_select_target_card_list_file_happy_path(mock_settings, fake_target_var):
    # Simulate the path being selected
    with patch(f'{mod.__name__}.filedialog.askopenfilename', return_value='/tmp/filename.csv'):
        mod.select_target_file()

    # With valid file selected it should update the settings
    mock_settings.update_setting.assert_called_once_with('TargetFiles', 'target_card_list', '/tmp/filename.csv')


def test_select_target_card_list_file_cancel(mock_settings, fake_target_var):
    with patch(f'{mod.__name__}.filedialog.askopenfilename', return_value=''):
        mod.select_target_file()

    # No valid path, should not update
    mock_settings.update_setting.assert_not_called()
    fake_target_var.set.assert_not_called()
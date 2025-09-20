"""Script for testing that select starting folder updates settings properly."""
import pytest
from unittest.mock import patch, MagicMock
import os

import utils.config_utils.select_starting_folder_dirs as mod

@pytest.fixture
def fake_target_var():
    return MagicMock()

@pytest.fixture
def mock_settings():
    with patch(f'{mod.__name__}.settings_module') as mock:
        mock.settings.get.return_value = None
        yield mock

def test_select_initial_target_folder_happy_path(fake_target_var, mock_settings):
    # patch simulates running the file dialog for the user to select a file, and returns a
    # directory for the purposes of testing
    with patch(f'{mod.__name__}.filedialog.askdirectory', return_value='/tmp/folder'):
        mod.select_initial_target_folder(None, fake_target_var)

    # Check that the settings file and target variable get updated when the file is selected
    mock_settings.update_setting.assert_called_once_with(
        'InitialTargetDirs', 'starting_target_folder', '/tmp/folder'
    )
    fake_target_var.set.assert_called_once_with('/tmp/folder')


def test_select_initial_target_folder_cancel(fake_target_var, mock_settings):
    # patch will do the same thing as above, but return an empty string simulating
    # the user canceling the file select
    with patch(f'{mod.__name__}.filedialog.askdirectory', return_value=''):
        mod.select_initial_target_folder(None, fake_target_var)

    # Check that update settings does not get called when the folder select is canceled
    mock_settings.update_settings.assert_not_called()
    # Also assert that the target variable (used for display) is not updated
    fake_target_var.set.assert_not_called()


def test_select_initial_target_folder_no_setting(fake_target_var, mock_settings):
    # Test what happens when an exception occurs
    mock_settings.settings.get.side_effect = Exception("Not found")

    with patch(f"{mod.__name__}.filedialog.askdirectory", return_value="/fallback"), \
         patch(f"{mod.__name__}.os.getcwd", return_value="/cwd"), \
         patch(f"{mod.__name__}.os.chdir") as _mock_chdir:  # no-op so we don't try to chdir to /cwd
        mod.select_initial_target_folder(None, fake_target_var)

    # Verify that the methods get called with the fallback, which should read /fallback
    mock_settings.update_setting.assert_called_once_with(
        'InitialTargetDirs', 'starting_target_folder', '/fallback'
    )
    fake_target_var.set.assert_called_once_with('/fallback')


def test_select_initial_raw_data_folder_happy_path(fake_target_var, mock_settings):
    with patch(f'{mod.__name__}.filedialog.askdirectory', return_value='/tmp/folder'):
        mod.select_initial_raw_data_folder(None, fake_target_var)

        mock_settings.update_setting.assert_called_once_with(
            'InitialTargetDirs', 'starting_data_folder', '/tmp/folder'
        )
        fake_target_var.set.assert_called_once_with('/tmp/folder')

def test_select_initial_raw_data_folder_cancel(fake_target_var, mock_settings):
    with patch(f'{mod.__name__}.filedialog.askdirectory', return_value=''):
        mod.select_initial_raw_data_folder(None, fake_target_var)

        mock_settings.update_settings.assert_not_called()
        fake_target_var.set.assert_not_called()

def test_select_initial_raw_data_folder_no_setting(fake_target_var, mock_settings):
    mock_settings.settings.get.side_effect = Exception("Not found")

    with patch(f'{mod.__name__}.filedialog.askdirectory', return_value='/fallback'), \
         patch(f'{mod.__name__}.os.getcwd', return_value='/cwd'), \
         patch(f"{mod.__name__}.os.chdir") as _mock_chdir:
        mod.select_initial_raw_data_folder(None, fake_target_var)

    mock_settings.update_setting.assert_called_once_with(
        'InitialTargetDirs', 'starting_data_folder', '/fallback'
    )
    fake_target_var.set.assert_called_once_with('/fallback')




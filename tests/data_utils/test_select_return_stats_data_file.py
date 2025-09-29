# tests/test_select_return_stats_data_file.py
from unittest.mock import MagicMock
import pytest
import tkinter as tk

# 🔁 CHANGE THIS to the actual module path
import utils.data_utils.select_load_stats_data_file as mod


def test_happy_path_logs_and_uses_initialdir(monkeypatch, caplog):
    caplog.set_level("INFO", logger="apps.basic_stats_app.data_utils")

    # Make settings return a specific initial dir
    calls = {}
    def fake_get(section, key):
        assert section == "InitialTargetDirs"
        assert key == "starting_target_folder"
        return "C:/init"
    monkeypatch.setattr(mod.settings_module.settings, "get", fake_get)

    # Capture kwargs passed to askopenfilename and return a file
    def fake_askopenfilename(**kwargs):
        calls["kwargs"] = kwargs
        return "C:/chosen/file.csv"
    monkeypatch.setattr(mod.filedialog, "askopenfilename", fake_askopenfilename)

    parent = MagicMock()

    result = mod.select_load_stats_data_file(parent, MagicMock(), MagicMock())
    assert result is None  # current implementation does not return the path

    # Verify dialog args
    k = calls["kwargs"]
    assert k["parent"] is parent
    assert k["initialdir"] == "C:/init"
    assert k["title"] == "Choose Target File"
    assert ("CSV Files", "*.csv") in k["filetypes"]

    # Verify logs
    msgs = [r.message for r in caplog.records]
    assert any("Loading DataFrame" in m for m in msgs)
    assert any("Loading data from from: C:/chosen/file.csv" in m for m in msgs)


def test_cancel_logs_no_file(monkeypatch, caplog):
    caplog.set_level("INFO", logger="apps.basic_stats_app.data_utils")

    monkeypatch.setattr(mod.settings_module.settings, "get",
                        lambda s, k: "C:/init")
    monkeypatch.setattr(mod.filedialog, "askopenfilename",
                        lambda **kw: "")  # simulate cancel

    result = mod.select_load_stats_data_file(MagicMock(), MagicMock(), MagicMock())
    assert result is None

    msgs = [r.message for r in caplog.records]
    assert any("Loading DataFrame" in m for m in msgs)
    assert any("No file selected" in m for m in msgs)
    assert not any("Loading data from from:" in m for m in msgs)

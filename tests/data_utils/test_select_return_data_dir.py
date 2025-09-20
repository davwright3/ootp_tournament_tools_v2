# tests/test_select_return_data_dir.py
from pathlib import Path
from unittest.mock import MagicMock
import pytest

# 👇 change this to your actual module path
import utils.data_utils.select_return_data_dir as mod


class FakeVar:
    def __init__(self, val=""):
        self._v = val
        self.calls = 0
    def set(self, v):
        self.calls += 1
        self._v = v
    def get(self):
        return self._v


def test_happy_path_sets_var_and_logs(monkeypatch, caplog):
    caplog.set_level("INFO", logger="apps.fileproc.data_utils")

    # settings & askdirectory
    monkeypatch.setattr(mod, "loaded_settings", {
        "InitialTargetDirs": {"starting_data_folder": "C:/init"}
    })
    chosen = "C:/chosen"
    def fake_askdirectory(**kwargs):
        # assert the dialog is called with expected args
        assert kwargs["initialdir"] == "C:/init"
        assert kwargs["title"] == "Select Raw Data Folder"
        assert "parent" in kwargs
        return chosen
    monkeypatch.setattr(mod.filedialog, "askdirectory", fake_askdirectory)

    parent = MagicMock()
    var = FakeVar()

    mod.select_return_data_dir(parent, var)

    assert var.get() == chosen
    assert any("Raw directory selected" in r.message for r in caplog.records)


def test_cancel_selection_does_nothing(monkeypatch, caplog):
    caplog.set_level("INFO", logger="apps.fileproc.data_utils")

    monkeypatch.setattr(mod, "loaded_settings", {
        "InitialTargetDirs": {"starting_data_folder": "C:/init"}
    })
    monkeypatch.setattr(mod.filedialog, "askdirectory", lambda **kw: "")  # simulate cancel

    var = FakeVar("unchanged")
    parent = MagicMock()

    mod.select_return_data_dir(parent, var)

    assert var.get() == "unchanged"           # no change
    assert var.calls == 0                      # set() not called
    assert any("No directory selected." in r.message for r in caplog.records)


def test_set_raises_is_caught_and_logged(monkeypatch, caplog):
    caplog.set_level("INFO", logger="apps.fileproc.data_utils")

    monkeypatch.setattr(mod, "loaded_settings", {
        "InitialTargetDirs": {"starting_data_folder": "C:/init"}
    })
    monkeypatch.setattr(mod.filedialog, "askdirectory", lambda **kw: "C:/picked")

    class ExplodeVar(FakeVar):
        def set(self, v):
            raise RuntimeError("boom")

    var = ExplodeVar()
    parent = MagicMock()

    # Should not raise; logs an error message instead
    mod.select_return_data_dir(parent, var)

    msgs = [r.message for r in caplog.records]
    assert any("Error while selecting data folder:" in m for m in msgs)
    assert not any("Raw directory selected" in m for m in msgs)

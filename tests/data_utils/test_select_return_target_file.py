# tests/test_select_return_target_file.py
from unittest.mock import MagicMock
import os
import pytest

# ⬇️ change to your actual module path
import utils.data_utils.select_return_target_file as mod


class FakeVar:
    def __init__(self, v=""):
        self._v = v
        self.set_calls = 0
    def set(self, v):
        self.set_calls += 1
        self._v = v
    def get(self):
        return self._v


def test_happy_path_sets_var_and_logs(monkeypatch, caplog, tmp_path):
    caplog.set_level("INFO", logger="apps.fileproc.data_utils")

    # settings -> initialdir (via .get)
    monkeypatch.setattr(
        mod.settings_module.settings,
        "get",
        lambda section, key, **kw: str(tmp_path),  # ignore fallback; return our tmp path
    )

    chosen = str(tmp_path / "target.csv")
    def fake_openfilename(**kwargs):
        # verify dialog kwargs
        assert kwargs["parent"] is not None
        assert kwargs["initialdir"] == str(tmp_path)
        assert kwargs["title"] == "Choose target card list"
        assert ("CSV Files", "*.csv") in kwargs["filetypes"]
        return chosen

    monkeypatch.setattr(mod.filedialog, "askopenfilename", fake_openfilename)

    parent = MagicMock()
    var = FakeVar()

    res = mod.select_return_target_file(parent, var)
    assert res is None  # function doesn't return
    assert var.get() == chosen
    assert var.set_calls == 1

    msgs = [r.message for r in caplog.records]
    assert any(chosen in m and "selected as target file" in m for m in msgs)


def test_cancel_selection_logs_and_does_not_set(monkeypatch, caplog, tmp_path):
    caplog.set_level("INFO", logger="apps.fileproc.data_utils")

    monkeypatch.setattr(
        mod.settings_module.settings, "get",
        lambda s, k, **kw: str(tmp_path)
    )
    monkeypatch.setattr(mod.filedialog, "askopenfilename", lambda **kw: "")  # simulate cancel

    var = FakeVar("unchanged")
    mod.select_return_target_file(MagicMock(), var)

    assert var.get() == "unchanged"
    assert var.set_calls == 0
    assert any("No target file selected" in r.message for r in caplog.records)


def test_fallback_initialdir_used_when_setting_missing(monkeypatch, caplog, tmp_path):
    caplog.set_level("INFO", logger="apps.fileproc.data_utils")

    # Make settings.get return its provided fallback to mimic ConfigParser fallback behavior
    def fake_get(section, option, **kw):
        # We expect caller to pass fallback=os.getcwd()
        return kw.get("fallback")

    monkeypatch.setattr(mod.settings_module.settings, "get", fake_get)

    captured = {}
    def fake_openfilename(**kwargs):
        captured["initialdir"] = kwargs["initialdir"]
        return str(tmp_path / "x.csv")

    monkeypatch.setattr(mod.filedialog, "askopenfilename", fake_openfilename)

    var = FakeVar()
    mod.select_return_target_file(MagicMock(), var)

    # initialdir should be whatever fallback was (current cwd at call time)
    assert captured["initialdir"] == os.getcwd()
    assert var.get().endswith("x.csv")

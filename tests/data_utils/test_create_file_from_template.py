import io
from pathlib import Path
from unittest.mock import MagicMock
import pytest

import utils.data_utils.create_file_from_template as mod

@pytest.mark.parametrize(
    'raw, expected', [
        ('report 01', 'report 01'),
        (' weird*name?.csv ', 'weirdnamecsv'),
        ('name-with-dashes', 'name-with-dashes')
    ]
)
def test_sanitize_filename(raw, expected):
    assert mod.sanitize_filename(raw) == expected


# Helper functions
class FakeDialog:
    def __init__(self, *_args, **_kwargs):
        self._value = 'new_file'
    def get_input(self):
        return self._value

def _write(p: Path, text: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding='utf-8')


# Happy Path
def test_create_file_from_template_happy_path(tmp_path, monkeypatch, caplog):
    caplog.set_level('INFO')

    template = tmp_path / 'assets' / 'data_template.csv'
    _write(template, 'col1,col2\nA,B\n')

    out_dir = tmp_path / 'out'
    out_dir.mkdir()

    # Patch
    monkeypatch.setattr(mod, 'get_resource_path', lambda rel: str(template))
    monkeypatch.setattr(mod, 'CustomInputDialog', FakeDialog)
    # Mimic settings: starting target folder
    monkeypatch.setattr(
        mod,
        'loaded_settings',
        {'InitialTargetDirs': {'starting_target_folder': str(out_dir)}}
    )

    # Fake parent
    parent = MagicMock()
    parent.winfo_toplevel.return_value = object()

    # Act
    mod.create_file_from_template(parent)

    dest = out_dir / 'new_file.csv'
    assert dest.exists()
    assert dest.read_text(encoding='utf-8') == 'col1,col2\nA,B\n'
    assert any('Created new file' in rec.message for rec in caplog.records)


# User cancels
def test_create_file_from_template_cancel(tmp_path, monkeypatch, caplog):
    caplog.set_level("INFO")

    template = tmp_path / "assets" / "data_template.csv"
    _write(template, "x,y\n1,2\n")
    out_dir = tmp_path / "out"; out_dir.mkdir()

    class CancelDialog(FakeDialog):
        def get_input(self): return ""  # simulate cancel/empty

    monkeypatch.setattr(mod, "get_resource_path", lambda rel: str(template))
    monkeypatch.setattr(mod, "CustomInputDialog", CancelDialog)
    monkeypatch.setattr(mod, "loaded_settings", {
        "InitialTargetDirs": {"starting_target_folder": str(out_dir)}
    })
    parent = MagicMock(); parent.winfo_toplevel.return_value = object()

    mod.create_file_from_template(parent)

    # No files created
    assert list(out_dir.glob("*.csv")) == []
    # No "Created new file" log line
    assert not any("Created new file at" in rec.message for rec in caplog.records)


# ---------- non-csv template ----------
def test_create_file_from_template_non_csv_template_logs_error(tmp_path, monkeypatch, caplog):
    caplog.set_level("ERROR")

    template = tmp_path / "assets" / "data_template.txt"
    _write(template, "not csv")
    out_dir = tmp_path / "out"; out_dir.mkdir()

    class NameDialog(FakeDialog):
        def get_input(self): return "ok"

    monkeypatch.setattr(mod, "get_resource_path", lambda rel: str(template))
    monkeypatch.setattr(mod, "CustomInputDialog", NameDialog)
    monkeypatch.setattr(mod, "loaded_settings", {
        "InitialTargetDirs": {"starting_target_folder": str(out_dir)}
    })
    parent = MagicMock(); parent.winfo_toplevel.return_value = object()

    mod.create_file_from_template(parent)

    assert any("Template is not valid" in rec.message for rec in caplog.records)
    assert not (out_dir / "ok.csv").exists()


# ---------- template missing ----------
def test_create_file_from_template_missing_template_logs_error(tmp_path, monkeypatch, caplog):
    caplog.set_level("ERROR")

    missing = tmp_path / "assets" / "data_template.csv"  # not created
    out_dir = tmp_path / "out"; out_dir.mkdir()

    class NameDialog(FakeDialog):
        def get_input(self): return "ok"

    monkeypatch.setattr(mod, "get_resource_path", lambda rel: str(missing))
    monkeypatch.setattr(mod, "CustomInputDialog", NameDialog)
    monkeypatch.setattr(mod, "loaded_settings", {
        "InitialTargetDirs": {"starting_target_folder": str(out_dir)}
    })
    parent = MagicMock(); parent.winfo_toplevel.return_value = object()

    mod.create_file_from_template(parent)

    assert any("Template file not found" in rec.message for rec in caplog.records)
    assert not (out_dir / "ok.csv").exists()

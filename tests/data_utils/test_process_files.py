# tests/test_file_processing.py
from pathlib import Path
import pandas as pd
import pytest

# ⬇️ CHANGE THIS to the actual path of the module you pasted
import utils.data_utils.process_files as mod   # e.g., utils.fileproc.data_utils


# ---------- add_file ----------
def test_add_file_when_target_empty(tmp_path):
    raw = tmp_path / "T1.csv"
    pd.DataFrame({"col": [1, 2]}).to_csv(raw, index=False)

    target_df = pd.DataFrame()  # empty
    out = mod.add_file(target_df, str(raw))

    assert list(out.columns) == ["col", "Trny"]
    assert out.shape == (2, 2)
    assert set(out["Trny"]) == {"T1"}


def test_add_file_appends_to_existing(tmp_path):
    raw = tmp_path / "T2.csv"
    pd.DataFrame({"col": [10, 20]}).to_csv(raw, index=False)

    # target already has same columns (including Trny)
    target_df = pd.DataFrame({"col": [99], "Trny": ["Existing"]})
    out = mod.add_file(target_df, str(raw))

    assert set(out["Trny"]) == {"Existing", "T2"}
    assert out.shape[0] == 3   # 1 existing + 2 new


# ---------- process_files: happy path ----------
def test_process_files_adds_new_and_skips_existing(tmp_path, caplog):
    caplog.set_level("INFO", logger="apps.fileproc.data_utils")

    target = tmp_path / "target.csv"
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()

    # initial target has one row, already contains 'Trny' column with "Game2"
    pd.DataFrame({"col": [111], "Trny": ["Game2"]}).to_csv(target, index=False)

    # raw files: Game1 (new), Game2 (duplicate)
    pd.DataFrame({"col": [1, 2]}).to_csv(raw_dir / "Game1.csv", index=False)
    pd.DataFrame({"col": [3]}).to_csv(raw_dir / "Game2.csv", index=False)

    mod.process_files(str(target), str(raw_dir))

    # target should now contain original + Game1 rows; Game2 skipped
    df = pd.read_csv(target)
    # Expect 1 existing + 2 from Game1 = 3 rows
    assert df.shape[0] == 3
    # Trny values should include both original and the new one
    assert set(df["Trny"]) == {"Game2", "Game1"}

    # logs
    logs = "\n".join(r.message for r in caplog.records)
    assert "Target file read into Dataframe" in logs
    assert "Skipping Game2, already in dataset" in logs
    assert "Processed 1 files." in logs


# ---------- process_files: error paths ----------
def test_process_files_errors_when_target_missing(tmp_path, caplog):
    caplog.set_level("ERROR", logger="apps.fileproc.data_utils")
    target = tmp_path / "nope.csv"
    raw_dir = tmp_path / "raw"; raw_dir.mkdir()

    mod.process_files(str(target), str(raw_dir))

    assert any("Target file does not exist" in r.message for r in caplog.records)


def test_process_files_errors_when_target_not_csv(tmp_path, caplog):
    caplog.set_level("ERROR", logger="apps.fileproc.data_utils")
    target = tmp_path / "target.txt"
    target.write_text("not csv", encoding="utf-8")
    raw_dir = tmp_path / "raw"; raw_dir.mkdir()

    mod.process_files(str(target), str(raw_dir))

    assert any("Target file must end with .csv" in r.message for r in caplog.records)


def test_process_files_errors_when_raw_dir_missing(tmp_path, caplog):
    caplog.set_level("ERROR", logger="apps.fileproc.data_utils")
    target = tmp_path / "target.csv"
    pd.DataFrame({"col": [], "Trny": []}).to_csv(target, index=False)

    missing_dir = tmp_path / "no_such_dir"

    mod.process_files(str(target), str(missing_dir))

    assert any("Raw directory does not exist" in r.message for r in caplog.records)

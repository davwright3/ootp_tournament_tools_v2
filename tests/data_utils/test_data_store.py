# tests/test_datastore.py
import importlib
from pathlib import Path
import pandas as pd
import pytest

import utils.data_utils.data_store as mod  # <-- change this to your module


# --- Keep tests isolated: reset the singleton before each test ---
@pytest.fixture(autouse=True)
def reset_datastore():
    # Clear class-level singleton state
    mod.DataStore._instance = None
    mod.DataStore._main_dataframe = None
    # Recreate the module-level singleton for callers that use `mod.data_store`
    mod.data_store = mod.DataStore()
    yield
    # Clean again (useful if a test mutates further)
    mod.DataStore._instance = None
    mod.DataStore._main_dataframe = None
    mod.data_store = mod.DataStore()


def test_singleton_identity():
    a = mod.DataStore()
    b = mod.DataStore()
    assert a is b  # same instance every time

def test_module_level_instance_is_singleton():
    # The exported `data_store` should be that same singleton
    assert mod.data_store is mod.DataStore()

def test_set_get_data_roundtrip():
    df = pd.DataFrame({"x": [1, 2], "y": [3, 4]})
    store = mod.DataStore()
    store.set_data(df)
    got = store.get_data()
    # same object, not a copy
    assert got is df
    assert list(got.columns) == ["x", "y"]

def test_clear_data():
    store = mod.DataStore()
    store.set_data(pd.DataFrame({"a": [1]}))
    store.clear_data()
    assert store.get_data() is None

def test_load_data_reads_csv(tmp_path: Path):
    csv = tmp_path / "example.csv"
    csv.write_text("a,b,Trny\n1,2,3\n3,4,5\n", encoding="utf-8")

    store = mod.DataStore()
    store.load_data(str(csv))

    df = store.get_data()
    assert list(df.columns) == ["a", "b", "Trny"]
    assert df.shape == (2, 3)
    assert df.iloc[0].to_dict() == {"Trny": 3, "a": 1, "b": 2}

# tests/test_readme_messaging.py
import logging
from pathlib import Path
import pytest

# 👉 adjust this import to your module path
import utils.log_utils.readme_messaging as mod


def write_md(path: Path, text: str):
    path.write_text(text, encoding="utf-8")


# ----------------- _sluggify_github -----------------
@pytest.mark.parametrize("src, expected", [
    ("Updated:", "updated"),
    ("What's New?", "whats-new"),
    ("  Major  Changes  ", "major-changes"),
    ("A & B / C", "a-b-c"),
    ("many---dashes", "many-dashes"),        # requires r'-{2,}'
])
def test_sluggify_github(src, expected, monkeypatch):
    # If you haven’t fixed the typo yet, this test will fail on the last case.
    assert mod._sluggify_github(src) == expected


# ----------------- extract_markdown_section -----------------
def test_extract_section_by_exact_heading(tmp_path: Path):
    md = tmp_path / "README.md"
    write_md(md, """
# Project

## Updated:
Line 1
Line 2

## Other
content
""".lstrip("\n"))

    out = mod.extract_markdown_section(str(md), "Updated:")
    assert out == "Line 1\nLine 2"


def test_extract_section_by_slug_match(tmp_path: Path):
    md = tmp_path / "README.md"
    write_md(md, """
# Title

## What's New?
This is new.

### Nested
Still part of What's New?

## Changelog
- something
""".lstrip("\n"))

    # Query using a GitHub-like anchor/slug
    out = mod.extract_markdown_section(str(md), "whats-new")
    # Should include the nested H3, and stop at the next H2
    assert out == "This is new.\n\n### Nested\nStill part of What's New?"


def test_extract_section_empty_returns_sentinel(tmp_path: Path):
    md = tmp_path / "README.md"
    write_md(md, """
# Title

## Updated:
## Next
Body
""".lstrip("\n"))

    out = mod.extract_markdown_section(str(md), "Updated:")
    assert out == "section is empty"


def test_extract_section_missing_file_returns_none(tmp_path: Path):
    md = tmp_path / "MISSING.md"
    assert mod.extract_markdown_section(str(md), "Updated:") is None


def test_extract_section_heading_not_found_returns_none(tmp_path: Path):
    md = tmp_path / "README.md"
    write_md(md, "# Only Title\n\nSome text\n")
    assert mod.extract_markdown_section(str(md), "Updated:") is None


# ----------------- log_readme_section -----------------
def test_log_readme_section_happy_path_logs_lines(tmp_path: Path, caplog: pytest.LogCaptureFixture):
    md = tmp_path / "README.md"
    write_md(md, """
# Title

## Updated:
Line A

Line B
""".lstrip("\n"))

    logger = logging.getLogger("test.readme")
    caplog.set_level(logging.INFO, logger="test.readme")

    ok = mod.log_readme_section(str(md), "Updated:", log=logger, level=logging.INFO)
    assert ok is True

    messages = [r.message for r in caplog.records if r.name == "test.readme"]
    # First a border, then the header line, then content (including a blank-line placeholder), then closing border
    assert any("README * Updated:" in m for m in messages)
    assert "Line A" in "\n".join(messages)
    # Blank line becomes a single space
    assert " " in messages
    assert messages[0].startswith("-" * 10)  # border present somewhere at top


def test_log_readme_section_not_found_logs_warning(tmp_path: Path, caplog: pytest.LogCaptureFixture):
    md = tmp_path / "README.md"
    write_md(md, "# Nothing here\n")

    logger = logging.getLogger("test.readme")
    caplog.set_level(logging.WARNING, logger="test.readme")

    ok = mod.log_readme_section(str(md), "Updated:", log=logger, level=logging.INFO)
    assert ok is False

    warn_msgs = [r.message for r in caplog.records if r.levelno >= logging.WARNING]
    assert any("README section not found for Updated:" in m for m in warn_msgs)

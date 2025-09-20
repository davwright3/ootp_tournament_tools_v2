# tests/test_tk_text_handler.py
import logging
import types
import pytest

# ⬇️ change this to your actual module path
import utils.log_utils.tk_handler as mod


class FakeSink:
    """Minimal Tk-like sink with .after and .append."""
    def __init__(self):
        self.after_calls = []   # list of (ms, callback)
        self.append_calls = []  # list of (text, tag)

    def after(self, ms, callback):
        self.after_calls.append((ms, callback))

    def append(self, text, tag):
        self.append_calls.append((text, tag))


@pytest.fixture
def logger():
    lg = logging.getLogger("test.tkhandler")
    lg.handlers[:] = []
    lg.setLevel(logging.DEBUG)
    lg.propagate = False
    yield lg
    lg.handlers[:] = []


def run_scheduled(sink: FakeSink):
    """Run the most recent scheduled callback (simulates Tk's event loop tick)."""
    assert sink.after_calls, "No scheduled drain"
    _, cb = sink.after_calls.pop(0)
    cb()


def test_emit_schedules_single_drain_and_drains_messages(logger):
    sink = FakeSink()
    h = mod.TkTextHandler(sink, poll_ms=1)
    h.setFormatter(logging.Formatter("%(levelname)s:%(message)s"))
    logger.addHandler(h)

    # First emit → one schedule
    logger.info("hello")
    assert len(sink.after_calls) == 1
    assert h._polling is True

    # While polling, more emits should NOT schedule extra drains
    logger.warning("warn")
    logger.error("err")
    assert len(sink.after_calls) == 1  # still just the first schedule

    # Run scheduled drain (process all queued records)
    run_scheduled(sink)

    # Messages drained in FIFO order, formatted, with expected tags
    msgs = sink.append_calls
    assert msgs == [
        ("INFO:hello", "INFO"),
        ("WARNING:warn", "WARNING"),
        ("ERROR:err", "ERROR"),
    ]
    assert h._polling is False  # queue empty → polling stops


def test_new_emit_after_empty_reschedules(logger):
    sink = FakeSink()
    h = mod.TkTextHandler(sink, poll_ms=1)
    h.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(h)

    # First batch
    logger.info("first")
    assert len(sink.after_calls) == 1
    run_scheduled(sink)
    assert [c[0] for c in sink.append_calls] == ["first"]
    assert h._polling is False

    # Emit again after drain → schedules again
    logger.info("second")
    assert len(sink.after_calls) == 1  # new schedule
    run_scheduled(sink)
    assert [c[0] for c in sink.append_calls] == ["first", "second"]


def test_non_info_warning_error_have_no_tag(logger):
    sink = FakeSink()
    h = mod.TkTextHandler(sink, poll_ms=1)
    h.setFormatter(logging.Formatter("%(levelname)s"))
    logger.addHandler(h)

    logger.debug("x")  # tag should be None
    run_scheduled(sink)

    assert sink.append_calls == [("DEBUG", None)]

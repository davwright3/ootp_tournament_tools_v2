# tests/test_attach_panel.py
import logging
import types
import pytest

# ⬇️ change to the module that contains attach_panel/detach_panel/NameSpaceFiler
import utils.log_utils.attach as mod


class FakeTkHandler(logging.Handler):
    def __init__(self, panel):
        super().__init__()
        self.panel = panel
        self.records = []
        self.closed = False
    def emit(self, record):
        self.records.append(record)
    # keep base behavior for setFormatter/addFilter
    def close(self):
        self.closed = True
        super().close()


class FakePanel:
    def __init__(self):
        self._callbacks = {}
        self.bind_calls = []
    def bind(self, event, cb):
        self.bind_calls.append((event, cb))
        self._callbacks[event] = cb


@pytest.fixture(autouse=True)
def clean_logging():
    # keep root and named loggers clean per test
    root = logging.getLogger()
    prev_handlers = list(root.handlers)
    prev_level = root.level
    yield
    # remove handlers added during the test
    for lg in list(logging.Logger.manager.loggerDict.values()):
        if isinstance(lg, logging.Logger):
            lg.handlers[:] = []
            lg.setLevel(logging.NOTSET)
    root.handlers[:] = prev_handlers
    root.setLevel(prev_level)


def test_attach_to_root_and_emit(monkeypatch):
    monkeypatch.setattr(mod, "TkTextHandler", FakeTkHandler)

    panel = FakePanel()
    logging.getLogger().setLevel(logging.INFO)

    mod.attach_panel(panel)  # logger_name=None -> root

    # fetch the handler we just attached
    logger, handler = mod._handlers_by_panel[panel]
    assert logger is logging.getLogger()
    assert isinstance(handler, FakeTkHandler)
    # destroy binding installed
    assert any(evt == "<Destroy>" for evt, _ in panel.bind_calls)

    # logging to any logger propagates to root
    logging.getLogger("anywhere").info("hello root")
    assert any("hello root" in r.getMessage() for r in handler.records)


def test_attach_with_namespace_filters_to_that_tree(monkeypatch):
    monkeypatch.setattr(mod, "TkTextHandler", FakeTkHandler)

    panel = FakePanel()
    lg = logging.getLogger("apps.fileproc")
    lg.setLevel(logging.INFO)
    logging.getLogger("apps.fileproc.child").setLevel(logging.INFO)
    logging.getLogger("apps.other").setLevel(logging.INFO)

    mod.attach_panel(panel, logger_name="apps.fileproc")

    attached_logger, handler = mod._handlers_by_panel[panel]
    # handler is attached to the named logger
    assert attached_logger.name == "apps.fileproc"

    logging.getLogger("apps.fileproc").info("msg A")
    logging.getLogger("apps.fileproc.child").info("msg B")
    logging.getLogger("apps.other").info("msg C")

    msgs = [rec.getMessage() for rec in handler.records]
    assert "msg A" in msgs
    assert "msg B" in msgs
    assert "msg C" not in msgs  # different namespace → not handled


def test_detach_removes_handler_and_closes(monkeypatch):
    monkeypatch.setattr(mod, "TkTextHandler", FakeTkHandler)

    panel = FakePanel()
    lg = logging.getLogger("apps.fileproc")
    lg.setLevel(logging.INFO)

    mod.attach_panel(panel, logger_name="apps.fileproc")
    logger, handler = mod._handlers_by_panel[panel]

    mod.detach_panel(panel)

    # handler removed and closed
    assert handler not in logger.handlers
    assert handler.closed is True

    # further logs do not go to the (detached) handler
    logging.getLogger("apps.fileproc").info("after detach")
    assert not any("after detach" in r.getMessage() for r in handler.records)


def test_destroy_event_triggers_detach(monkeypatch):
    monkeypatch.setattr(mod, "TkTextHandler", FakeTkHandler)

    panel = FakePanel()
    logging.getLogger().setLevel(logging.INFO)

    mod.attach_panel(panel)
    logger, handler = mod._handlers_by_panel[panel]

    # simulate Tk’s destroy event
    cb = dict(panel.bind_calls)["<Destroy>"] if isinstance(panel.bind_calls, dict) else None
    if cb is None:
        # bind_calls is a list[(event, cb)] above; extract the callback
        cb = {e: c for e, c in panel.bind_calls}["<Destroy>"]
    cb(types.SimpleNamespace())  # invoke the callback

    assert panel not in mod._handlers_by_panel
    assert handler not in logger.handlers
    assert handler.closed is True

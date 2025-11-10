import logging
import queue


class TkTextHandler(logging.Handler):
    """
    Thread safe handler: queue records and let the UI drain the via .after()
    'sink' must expose an .append(text, tag) method (e.g., MessagePanel
    """
    def __init__(self, sink, poll_ms=50):
        super().__init__()
        self.sink = sink
        self.q = queue.Queue()
        self.poll_ms = poll_ms
        self._polling = False

    def emit(self, record):
        try:
            self.q.put_nowait(record)
            if not self._polling:
                self._polling = True
                self._schedule_drain()
        except Exception:
            self.handleError(record)

    def _schedule_drain(self):
        # Parent widget: use the sink widget itself
        self.sink.after(self.poll_ms, self._drain)

    def _drain(self):
        try:
            while True:
                record = self.q.get_nowait()
                try:
                    msg = self.format(record)
                except Exception:
                    msg = f"Logging error: {record}"
                tag = record.levelname if record.levelname in (
                    "INFO", "WARNING", "ERROR") else None
                self.sink.append(msg, tag)
        except queue.Empty:
            self._polling = False
        finally:
            if not self.q.empty():
                self._polling = True
                self._schedule_drain()

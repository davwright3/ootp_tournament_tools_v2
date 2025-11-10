"""Script for attaching a namespace to new app logger."""
import logging
import weakref
from .tk_handler import TkTextHandler


class NameSpaceFiler(logging.Filter):
    def __init__(self, prefix: str):
        super().__init__()
        self.prefix = prefix

    def filter(self, record: logging.LogRecord) -> bool:
        return record.name.startswith(self.prefix)


_handlers_by_panel = weakref.WeakKeyDictionary()


def attach_panel(panel_widget, logger_name: str | None = None):
    """
    Attach a TkTextHandler that writes to the panel.
    If logger_name is given, only logs from that namespace are shown.
    """

    logger = (logging.getLogger() if logger_name is None
              else logging.getLogger(logger_name)
              )
    handler = TkTextHandler(panel_widget)
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    ))
    if logger_name is not None:
        handler.addFilter(NameSpaceFiler(logger_name))

    logger.addHandler(handler)
    _handlers_by_panel[panel_widget] = (logger, handler)

    # Detach when the panel is destroyed
    panel_widget.bind("<Destroy>", lambda e: detach_panel(panel_widget))


def detach_panel(panel_widget):
    pair = _handlers_by_panel.pop(panel_widget, None)
    if not pair:
        return
    logger, handler = pair
    try:
        logger.removeHandler(handler)
    finally:
        handler.close()

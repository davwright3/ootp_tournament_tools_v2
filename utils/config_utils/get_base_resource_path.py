import os
import sys
import logging

def get_base_resource_path(relative_path: str) -> str:
    base_path = ""

    logger = logging.getLogger(__name__)

    if hasattr(sys, '_MEIPASS'):
        base_path = os.path.join(sys._MEIPASS, relative_path)
        logger.info(f'Path: {base_path}')
        return base_path
    base_path = os.path.join(os.path.abspath('.'), relative_path)
    logger.info(f'Path: {base_path}')
    return base_path
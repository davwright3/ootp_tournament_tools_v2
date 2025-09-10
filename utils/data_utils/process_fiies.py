"""Script for file processing app to process CSV files."""
import logging
import pandas as pd

def process_files(target_file=None, raw_dir=None):
    """Process the files."""
    logger = logging.getLogger("apps.fileproc.data_utils")
    logger.info('Processing files')
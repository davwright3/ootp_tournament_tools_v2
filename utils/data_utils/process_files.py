"""Script for file processing app to process CSV files."""
import logging
import os
import glob
import pandas as pd


logger = logging.getLogger("apps.fileproc.data_utils")
logger.info('Beginning file processing')


def add_file(target_df, file_to_add):
    """
    Add current file to the end of the df.
    :param target_df: Target dataframe, dataframe
    :param file_to_add: Path to file addition, string
    :return: Concatenated dataframe with added file to end, dataframe
    """
    file_name = os.path.splitext(os.path.basename(file_to_add))[0]
    addition = pd.read_csv(file_to_add)
    addition['Trny'] = file_name
    addition_len = len(addition)
    logger.info(f'Adding file {file_name}, {addition_len} rows added')

    if target_df.empty:
        return addition
    else:
        return pd.concat([target_df, addition])


def process_files(target_file_path: str, raw_dir: str):
    """
    Process the files from the raw directory into a single, concatenated file.
    File names get added to the concatenated file under the heading 'Trny',
    and each file is checked against the list from the 'Trny' heading to ensure
    that duplicate files are not added to the concatenated file.
    :param target_file_path: Target file path, string
    :param raw_dir: Raw directory path, string
    :return: None
    """
    target_dataframe = None
    raw_data_dir = None

    # Check if the target file is a valid csv.
    if not os.path.exists(target_file_path):
        # File is not a real file
        logger.error('Target file does not exist.')
        return
    elif not target_file_path.lower().endswith('.csv'):
        logger.error('Target file must end with .csv.')
        return
    else:
        target_dataframe = pd.read_csv(target_file_path, low_memory=False)
        logger.info('Target file read into Dataframe.')

    # Check if the raw_dir is a valid directory.
    if not os.path.isdir(raw_dir):
        logger.error(
            'Raw directory does not exist, please choose valid directory.'
        )
        return
    else:
        raw_data_dir = raw_dir

    # Create the list for tracking whether the file has already been added.
    existing_files = set(target_dataframe['Trny'].unique())
    existing_files = set(str(x) for x in existing_files)
    num_files_added = 0
    for file_path in glob.glob(os.path.join(raw_data_dir, '*.csv')):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        if file_name not in existing_files:
            addition = add_file(target_dataframe, file_path)
            target_dataframe = addition
            num_files_added += 1
        else:
            logger.info(f'Skipping {file_name}, already in dataset')

    total_len = len(target_dataframe)
    logger.info(
        f'Processed {num_files_added} files.  Total'
        f' entries in dataset: {total_len}')
    target_dataframe.to_csv(target_file_path, index=False)

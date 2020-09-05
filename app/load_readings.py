import json
import logging
import os.path

from typing import Optional


def get_readings(data_source: Optional[str] = None):
    """ Loads readings from local file system or provided path.

    There's no need to refactor this function.
    The JSON library reads until EOF and then loads into memory.
    Returns a dictionary.

    :param str data_source: Path to the readings file (optional).

    :returns: Current readings.
    :rtype: dict
    """
    if not data_source:
        file_path = os.path.join('data', 'readings.json')
    else:
        file_path = os.path.join('data', data_source)
    try:
        with open(file_path, 'r') as f:
            readings = json.load(f)
    except FileNotFoundError:
        logging.error(f'Error: {file_path} was not found.')
        raise FileNotFoundError(f'Error: {file_path} was not found.')
    except IOError:
        logging.error(f'Error: Could not read {file_path}.')
        raise IOError(f'Error: Could not read {file_path}.')

    return readings

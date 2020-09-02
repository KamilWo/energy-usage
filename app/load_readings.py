import json
import logging
import os.path


def get_readings():
    """ Loads readings from local file system.

    There's no need to refactor this function.
    The JSON library reads until EOF and then loads into memory.
    Returns a dictionary.

    :returns: Current readings.
    :rtype: dict
    """

    file_path = os.path.join('data', 'readings.json')
    try:

        with open(file_path, 'r') as f:
            readings = json.load(f)
    except FileNotFoundError:
        logging.error(f'Error: {file_path} was not found.')
    except IOError:
        logging.error(f'Error: Could not read {file_path}.')

    return readings

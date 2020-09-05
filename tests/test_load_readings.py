import pytest
import os

from app.load_readings import (
    get_readings
)
from .consts import (
    TEST_LOAD_READINGS_DB_GET_READINGS_ORIGINAL,
    TEST_LOAD_READINGS_DB_GET_READINGS_CUSTOM,
)
from unittest.mock import Mock


class TestLoadReadings(object):
    """ Testing LoadReadings. """

    def test_get_readings(self):
        """ Testing get_readings function. """

        db = get_readings()
        print(db)
        assert db == TEST_LOAD_READINGS_DB_GET_READINGS_ORIGINAL

    def test_get_new_readings(self):
        """ Testing get_new_readings function. """

        db1 = get_readings()

        assert db1 == TEST_LOAD_READINGS_DB_GET_READINGS_ORIGINAL

        data_source = os.path.join('..', 'data', 'test_readings.json')

        db2 = get_readings(data_source=data_source)

        assert db2 == TEST_LOAD_READINGS_DB_GET_READINGS_CUSTOM

        with pytest.raises(FileNotFoundError) as fnfe_exception:
            get_readings(data_source='invalid_path.json')
        assert type(fnfe_exception.value) is FileNotFoundError

        io_error_mock = Mock(side_effect=IOError(f'Error: Could not read '
                                                 f'{data_source}'))
        with pytest.raises(IOError) as ioe_exception:
            get_readings(data_source=data_source)
            io_error_mock()
        assert type(ioe_exception.value) is IOError

import app.main
import pytest
import unittest
from pytest_mock import mocker


class TestApp:
    '''test class for rover app'''

    def test_main_init(self):
        '''test main entry point for app'''
        with unittest.mock.patch.object(app.main, "__name__", "__main__"):
            # with pytest.raises(SystemExit):
            assert app.main.init() == 42


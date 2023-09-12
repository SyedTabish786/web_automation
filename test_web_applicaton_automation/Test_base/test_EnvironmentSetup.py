import datetime
import pytest
import unittest
from requests.exceptions import ConnectionError


class EnvironmentSetup(unittest.TestCase):

    @pytest.fixture(scope="class")
    def setup_teardown(self):
        print("Run Started at:", datetime.datetime.now())
        print("Environment Set Up")
        print("------------------------------------------------------------------")

        yield

        print("------------------------------------------------------------------")
        print("Environment Tear Down")
        print("Run Completed at:", datetime.datetime.now())

        try:
            # Your teardown actions can go here
            pass
        except ConnectionError as e:
            print("Error occurred during environment teardown:", str(e))


if __name__ == '__main__':
    pytest.main([__file__])

import unittest
from unittest import skip
# from tests.test_buildings import *
# from tests.test_vehicles import *

class InitializationTests(unittest.TestCase):

    def test_import_motorsports(self):
        """
        Ensure the test suite can import the motorsports module
        """
        try:
            import motorsports
        except ImportError:
            self.fail("Was not able to import the motorsports")

    def test_import_buildings(self):
        """
        Ensure the test suite can import the buildings module
        """
        try:
            import motorsports.buildings
        except ImportError:
            self.fail("Was not able to import the motorsports")

    # @skip("pending test code")
    def test_import_vehicles(self):
        """
        Ensure the test suite can import the vehicles module
        """
        pass

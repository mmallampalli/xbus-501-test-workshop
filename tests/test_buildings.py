# tests.test_buildings
# test module to evaluate the classes in the buildings module
#
# to execute tests, run the following command from project root:
#   nosetests -v --with-coverage --cover-package=motorsports \
#   --cover-inclusive --cover-erase tests
#
# for a list of available asserts:
# https://docs.python.org/2/library/unittest.html#assert-methods
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_buildings.py [] allen.leis@georgetown.edu $

"""
Test cases for buildings module
"""

##########################################################################
## Imports
##########################################################################

import unittest
from unittest import skip
from motorsports.buildings import Garage
from motorsports.buildings import Car

##########################################################################
## Tests
##########################################################################

class GarageTests(unittest.TestCase):

    def test_has_name(self):
        """
        Ensure the garage returns the name provided at creation
        """
        name = 'Bob\'s Garage'
        g = Garage(name)
        self.assertEqual(name, g.name)

    def test_allows_cars_to_enter(self):
        """
        Ensure the garage allows Car object to enter
        """
        name = "Test Garage"
        g = Garage(name)
        c = Car("Red", "some_make", "some_model")
        g.enter(c)

    def test_ensure_cars_enter_fully(self):
        """
        Ensure vehicle is in garage after it enters (eg: vehicle in garage == True)
        """
        name = "Test Garage"
        g = Garage(name)
        c = Car("Red", "some_make", "some_model")
        g.enter(c)
        self.assertEqual(g.vehicles[-1], c)

    def test_only_allows_cars_to_enter(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to enter
        """
        name = "Test Garage"
        g = Garage(name)
        with self.assertRaises(TypeError):
            g.enter(42)

    def test_only_allows_cars_to_exit(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to exit
        """
        name = "Test Garage"
        g = Garage(name)
        with self.assertRaises(TypeError):
            g.exit(42)

    def test_allows_cars_to_exit(self):
        """
        Ensure vehicles can leave the garage
        """
        name = "Test Garage"
        g = Garage(name)
        c = Car("Red", "some_make", "some_model")
        g.enter(c)
        g.exit(c)

    def test_ensure_cars_exit_fully(self):
        """
        Ensure vehicle is not in garage after it exits
        """
        name = "Test Garage"
        g = Garage(name)
        c = Car("Red", "some_make", "some_model")
        previous = list(g.vehicles)
        g.enter(c)
        g.exit(c)
        self.assertEqual(previous, g.vehicles)

    def test_raise_lookup_error_on_exit(self):
        """
        Ensure that garage raises LookupError if vehicle attempts
        to exit but was never in garage.
        """
        name = "Test Garage"
        g = Garage(name)
        c = Car("Red", "some_make", "some_model")
        with self.assertRaises(LookupError):
            g.exit(c)

    def test_iter_builtin(self):
        """
        Ensure we can iterate over garage vehicles by trying to
        iterate over the garage itself
        """
        name = "Test Garage"
        g = Garage(name)
        c = Car("Red", "some_make", "some_model")
        g.enter(c)
        for car in g:
            pass

    def test_len_builtin(self):
        """
        Ensure that the length of the garage matches the number
        of vehicles parked in it
        """
        name = "Test Garage"
        g = Garage(name)
        c = Car("Red", "some_make", "some_model")
        g.enter(c)
        l = len(g)

    def test_main(self):
        """
        Ensure the entry point works
        """
        result = imp.load_source('__main__', 'motorsports/buildings.py')

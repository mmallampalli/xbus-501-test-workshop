# tests.test_vehicles
# test module to evaluate the classes in the vehicles module
#
# for a list of available asserts:
# https://docs.python.org/2/library/unittest.html#assert-methods
#
# to execute tests, run the following command from project root:
#   nosetests -v --with-coverage --cover-package=motorsports \
#   --cover-inclusive --cover-erase tests
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_vehicles.py [] allen.leis@georgetown.edu $

"""
Test cases for vehicles module
"""

##########################################################################
## Imports
##########################################################################

import unittest
from unittest import skip
from motorsports.buildings import Car, BaseVehicle

##########################################################################
## Tests
##########################################################################

class VehicleTests(unittest.TestCase):

    def test_description(self):
        """
        Ensure the car description return a string of: "color, make model"
        """
        c = Car("red", "Ford", "Taurus")
        self.assertEqual(c.description, "red Ford Taurus")

    def test_initial_state_is_stopped(self):
        """
        Ensure the a car's initial state is "stopped"
        """
        c = Car("red", "Ford", "Taurus")
        self.assertEqual(c.state, "stopped")

    def test_state_after_start(self):
        """
        Ensure the car's state is "started" after using start method
        """
        c = Car("red", "Ford", "Taurus")
        c.start()
        self.assertEqual(c.state, "started")

    def test_state_after_stop(self):
        """
        Ensure the car's state is "stopped" after using shutdown method
        """
        c = Car("red", "Ford", "Taurus")
        c.shutdown()
        self.assertEqual(c.state, "stopped")

    def test_str_builtin(self):
        """
        Ensure the car evaluates to a string of
        "I am a <car color>, <car make>, <car model>."
        """
        c = Car("red", "Ford", "Taurus")
        self.assertEqual("I am a red Ford Taurus.", str(c))

    def test_color_requirement(self):
        """
        Ensure the car requires a color argument during instantiation
        """
        parameters = inspect.getargspec(Car.__init__).args
        self.assertIn("color", parameters)

    def test_make_requirement(self):
        """
        Ensure the car requires a make argument during instantiation
        """
        parameters = inspect.getargspec(Car.__init__).args
        self.assertIn("make", parameters)

    def test_model_requirement(self):
        """
        Ensure the car requires a model argument during instantiation
        """
        parameters = inspect.getargspec(Car.__init__).args
        self.assertIn("make", parameters)

    def test_state_read_only(self):
        """
        Ensure the car state attribute is read only and throws
        AttributeError if someone tries to assign a value directly
        """
        c = Car("red", "make_a", "model_b")
        with self.assertRaises(AttributeError):
            c.state = "stopped"

    def test_car_is_a_vehicle(self):
        """
        Ensure a car object is also an instance of BaseVehicle
        """
        c = Car("red", "make_a", "model_b")
        self.assertIsInstance(c, BaseVehicle)
        self.assertEqual(super(Car, c).description, "Car")

    def test_main(self):
        """
        Ensure the entry point works
        """
        result = imp.load_source('__main__', 'motorsports/vehicles.py')

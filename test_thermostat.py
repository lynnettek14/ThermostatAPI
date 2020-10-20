"""This script is a unit test to validate functionality of thermostat.py"""

import unittest
import web
from thermostat import Thermostat


class TestThermostat(unittest.TestCase):
    """Test class for unit testing thermostat.py"""


    def setUp(self):
        print('Set up thermostats')
        self.thermostat_1 = Thermostat(100)
        self.thermostat_2 = Thermostat(101)


    def tearDown(self):
        pass

    def test_intialization(self):
        self.assertEqual(self.thermostat_1.identifier, 100)
        self.assertEqual(self.thermostat_1.name, '')
        self.assertTrue(self.thermostat_1.current_temp > Thermostat.lowest_allowed_set_point)
        self.assertTrue(self.thermostat_1.current_temp < Thermostat.highest_allowed_set_point)
        self.assertEqual(self.thermostat_1.operating_mode, Thermostat.operating_states[2]) 
        self.assertEqual(self.thermostat_1.cooling_set_point, Thermostat.lowest_allowed_set_point)
        self.assertEqual(self.thermostat_1.heating_set_point, Thermostat.highest_allowed_set_point)
        self.assertEqual(self.thermostat_1.fan_mode, Thermostat.fan_operating_states[0])

        self.assertEqual(self.thermostat_2.identifier, 101)
        self.assertEqual(self.thermostat_2.name, '')
        self.assertTrue(self.thermostat_2.current_temp > Thermostat.lowest_allowed_set_point)
        self.assertTrue(self.thermostat_2.current_temp < Thermostat.highest_allowed_set_point)
        self.assertEqual(self.thermostat_2.operating_mode, Thermostat.operating_states[2])
        self.assertEqual(self.thermostat_2.cooling_set_point, Thermostat.lowest_allowed_set_point)
        self.assertEqual(self.thermostat_2.heating_set_point, Thermostat.highest_allowed_set_point)
        self.assertEqual(self.thermostat_2.fan_mode, Thermostat.fan_operating_states[0])


    def test_to_string(self):
        self.assertIsNotNone(self.thermostat_1.__str__())
        print(self.thermostat_1.__str__())

        self.assertIsNotNone(self.thermostat_2.__str__())
        print(self.thermostat_2.__str__())


    def test_set_thermostat_name(self):
        self.thermostat_1.set_thermostat_name('Mary')
        self.thermostat_2.set_thermostat_name('John')
        self.assertEqual(self.thermostat_1.name, 'Mary')
        self.assertEqual(self.thermostat_2.name, 'John')


    def test_read_temperature(self):
        last_read_temp_1 = self.thermostat_1.current_temp
        self.thermostat_1.read_temperature()
        temp_diff = abs(last_read_temp_1 - self.thermostat_1.current_temp)
        self.assertTrue(temp_diff > 0.01)

        last_read_temp_2 = self.thermostat_2.current_temp
        self.thermostat_2.read_temperature()
        temp_diff = abs(last_read_temp_2 - self.thermostat_2.current_temp)
        self.assertTrue(temp_diff > 0.01)



    def test_set_operating_mode(self):
        self.thermostat_1.set_operating_mode('cool')
        self.assertEqual(self.thermostat_1.operating_mode, Thermostat.operating_states[0])
        self.thermostat_1.set_operating_mode('COOL')
        self.assertEqual(self.thermostat_1.operating_mode, Thermostat.operating_states[0])
        self.thermostat_1.set_operating_mode('heat')
        self.assertEqual(self.thermostat_1.operating_mode, Thermostat.operating_states[1])
        self.thermostat_1.set_operating_mode('HEAT')
        self.assertEqual(self.thermostat_1.operating_mode, Thermostat.operating_states[1])
        self.thermostat_1.set_operating_mode('off')
        self.assertEqual(self.thermostat_1.operating_mode, Thermostat.operating_states[2])
        self.thermostat_1.set_operating_mode('OFF')
        self.assertEqual(self.thermostat_1.operating_mode, Thermostat.operating_states[2])

#        with self.assertRaises(web.NotAcceptable)
#            self.thermostat_1.set_operating_mode('none')

        self.thermostat_2.set_operating_mode('cool')
        self.assertEqual(self.thermostat_2.operating_mode, Thermostat.operating_states[0])
        self.thermostat_2.set_operating_mode('COOL')
        self.assertEqual(self.thermostat_2.operating_mode, Thermostat.operating_states[0])
        self.thermostat_2.set_operating_mode('heat')
        self.assertEqual(self.thermostat_2.operating_mode, Thermostat.operating_states[1])
        self.thermostat_2.set_operating_mode('HEAT')
        self.assertEqual(self.thermostat_2.operating_mode, Thermostat.operating_states[1])
        self.thermostat_2.set_operating_mode('off')
        self.assertEqual(self.thermostat_2.operating_mode, Thermostat.operating_states[2])
        self.thermostat_2.set_operating_mode('OFF')
        self.assertEqual(self.thermostat_2.operating_mode, Thermostat.operating_states[2])

#        with self.assertRaises(web.NotAcceptable)
#            self.thermostat_2.set_operating_mode('none')


    def test_set_fan_mode(self):
        self.thermostat_1.set_fan_mode('off')
        self.assertEqual(self.thermostat_1.fan_mode, Thermostat.fan_operating_states[0])
        self.thermostat_1.set_fan_mode('OFF')
        self.assertEqual(self.thermostat_1.fan_mode, Thermostat.fan_operating_states[0])
        self.thermostat_1.set_fan_mode('auto')
        self.assertEqual(self.thermostat_1.fan_mode, Thermostat.fan_operating_states[1])
        self.thermostat_1.set_fan_mode('AUTO')
        self.assertEqual(self.thermostat_1.fan_mode, Thermostat.fan_operating_states[1])

#        with self.assertRaises(web.NotAcceptable)
#            self.thermostat_1.set_fan_mode('none')

        self.thermostat_2.set_fan_mode('off')
        self.assertEqual(self.thermostat_2.fan_mode, Thermostat.fan_operating_states[0])
        self.thermostat_2.set_fan_mode('OFF')
        self.assertEqual(self.thermostat_2.fan_mode, Thermostat.fan_operating_states[0])
        self.thermostat_2.set_fan_mode('auto')
        self.assertEqual(self.thermostat_2.fan_mode, Thermostat.fan_operating_states[1])
        self.thermostat_2.set_fan_mode('AUTO')
        self.assertEqual(self.thermostat_2.fan_mode, Thermostat.fan_operating_states[1])

#        with self.assertRaises(web.NotAcceptable)
#            self.thermostat_2.set_fan_mode('none')


    def test_set_cooling_set_point(self):
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_1.set_cooling_set_point(-10)
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_1.set_cooling_set_point(0)
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_1.set_cooling_set_point(500)
        self.thermostat_1.set_cooling_set_point(75)
        self.assertTrue(self.thermostat_1.cooling_set_point > Thermostat.lowest_allowed_set_point)
        self.assertTrue(self.thermostat_1.cooling_set_point < Thermostat.highest_allowed_set_point)

#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_2.set_cooling_set_point(-10)
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_2.set_cooling_set_point(0)
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_2.set_cooling_set_point(500)
        self.thermostat_2.set_cooling_set_point(65.0)
        self.assertTrue(self.thermostat_2.cooling_set_point > Thermostat.lowest_allowed_set_point)
        self.assertTrue(self.thermostat_2.cooling_set_point < Thermostat.highest_allowed_set_point)


    def test_set_heating_set_point(self):
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_1.set_heating_set_point(-10)
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_1.set_heating_set_point(0)
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_1.set_heating_set_point(500)
        self.thermostat_1.set_heating_set_point(75)
        self.assertTrue(self.thermostat_1.heating_set_point > Thermostat.lowest_allowed_set_point)
        self.assertTrue(self.thermostat_1.heating_set_point < Thermostat.highest_allowed_set_point)

#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_2.set_heating_set_point(-10)
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_2.set_heating_set_point(0)
#        with self.assertRaises(web.NotAcceptable):
#            self.thermostat_2.set_heating_set_point(500)
        self.thermostat_2.set_heating_set_point(65.0)
        self.assertTrue(self.thermostat_2.heating_set_point > Thermostat.lowest_allowed_set_point)
        self.assertTrue(self.thermostat_2.heating_set_point < Thermostat.highest_allowed_set_point)


if __name__ == '__main__':
    unittest.main()

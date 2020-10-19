"""This script uses web.py to control and retreive the state of thermostats in a home.
"""
import json
import random
import web


# web.py definition that maps /anything to the Index class defined below
urls = ('/(.*)', 'Index')

# In memory database for existing sensors
sensor_devices_in_home = {}


def setup_devices():
    """Creating sensors for in memory database."""
    sensor_devices_in_home['100'] = Thermostat(100)
    sensor_devices_in_home['101'] = Thermostat(101)


class Thermostat:
    """Thermostat object."""

    # Static members
    operating_states = ('cool', 'heat', 'off')
    fan_operating_states = ('off', 'auto')
    lowest_allowed_set_point = 30.0
    highest_allowed_set_point = 100.0

    def __init__(self, thermostat_id):
        self.identifier = thermostat_id
        self.name = ''
        self.read_temperature()
        self.operating_mode = Thermostat.operating_states[2]
        self.cooling_set_point = Thermostat.lowest_allowed_set_point
        self.heating_set_point = Thermostat.highest_allowed_set_point
        self.fan_mode = Thermostat.fan_operating_states[0]

    def __str__(self):
        return json.dumps(self.__dict__)

    def set_thermostat_name(self, thermostat_name):
        """Personalizing the name of the thermostat."""
        self.name = thermostat_name

    def read_temperature(self):
        """Reads the temperate for a random double generator bound by 30.0-100.0."""
        self.current_temp = random.uniform(
            Thermostat.lowest_allowed_set_point,
            Thermostat.highest_allowed_set_point)

    def set_operating_mode(self, mode):
        """Sets the Thermostat operating mode (heat, cool, off)."""
        if mode.lower() in Thermostat.operating_states:
            self.operating_mode = mode.lower()
        else:
            raise web.notacceptable(
                '{' +
                f'"Error": "The Mode entered: {mode} was not found in Thermostat operating states"' +
                '}')

    def set_fan_mode(self, mode):
        """Sets the Thermostat fan mode (auto, off)."""
        if mode.lower() in Thermostat.fan_operating_states:
            self.fan_mode = mode.lower()
        else:
            raise web.notacceptable(
                '{' +
                f'"Error": "Fan mode entered: {mode} was not found in Thermostat fan operating states"' +
                '}')

    def set_cooling_set_point(self, temperature):
        """Sets the cooling set point bound by 30.0-100.0."""
        if temperature < Thermostat.lowest_allowed_set_point or temperature > Thermostat.highest_allowed_set_point:
            raise web.notacceptable(
                '{' +
                f'"Error": " The temperature {temperature} exceeds allowed temperature range of {Thermostat.lowest_allowed_set_point} to {Thermostat.highest_allowed_set_point}"' +
                '}')
        self.cooling_set_point = temperature

    def set_heating_set_point(self, temperature):
        """Sets the heating set point bound by 30.0-100.0."""
        if temperature < Thermostat.lowest_allowed_set_point or temperature > Thermostat.highest_allowed_set_point:
            raise web.notacceptable(
                '{' +
                f'"Error": "The temperature {temperature} exceeds allowed temperature range of {Thermostat.lowest_allowed_set_point} to {Thermostat.highest_allowed_set_point}"' +
                '}')
        self.heating_set_point = temperature


class Index:
    """Index class called by web.py."""

    def GET(self, thermostat_id):
        """GET functionality for web.py; interaction with web browser. Returns Thermostat object."""
        if thermostat_id not in sensor_devices_in_home:
            raise web.notfound(
                '{' + f'"Error": "Could not find device by this thermostat ID: {thermostat_id}"' + '}')
        return sensor_devices_in_home[thermostat_id]

    def POST(self, thermostat_id):
        """POST functionality for web.py; interaction with web browser. Returns Thermostat object."""
        if thermostat_id not in sensor_devices_in_home:
            raise web.notfound(
                '{' + f'"Error": "Could not find device by this ID: {thermostat_id}"' + '}')
        sensor = sensor_devices_in_home[thermostat_id]
        data = json.loads(web.data())
        if 'name' in data:
            sensor.set_thermostat_name(data['name'])
        if 'current_temp' in data:
            sensor.read_temperature()
        if 'operating_mode' in data:
            sensor.set_operating_mode(data['operating_mode'])
        if 'cooling_set_point' in data:
            sensor.set_cooling_set_point(data['cooling_set_point'])
        if 'heating_set_point' in data:
            sensor.set_heating_set_point(data['heating_set_point'])
        if 'fan_mode' in data:
            sensor.set_fan_mode(data['fan_mode'])
        return sensor


setup_devices()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

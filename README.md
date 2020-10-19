# ThermostatAPI
API for controlling the state of thermostats in a home

This is a web.py ( http://webpy.org) app that exposes a RESTful API for controlling and retrieving the state of the thermostats in a home. For this app, it will simply set and store the thermostat’s state within the app and return that state when requested. Everything is done in memory (there is no need for persistence) and it is assumed access from a single client (there is no dealing with concurrency problems).

Thermostats have the following properties:
 ID (read only): unique system identifier for this thermostat (i.e 100 or 101) and assigned in the code at this time
 Name (read-write): display name (i.e “Upstairs Thermostat” and “Downstairs Thermostat”)
 Current Temp (read-only): since this is not a real home with real thermostats an appropriate random value is returned if current_temp is passed into web.data
 Operating Mode (read-write): one of “cool”, “heat”, “off”
 Cool SetPoint (read-write): a value between 30-100 degrees fahrenheit
 Heat SetPoint (read-write): a value between 30-100 degrees fahrenheit
 Fan Mode (read-write): either “off” or “auto”
 
 The url address has in the first /{} space the identifying number(ID) of the Thermostat and this is how the data is accessed and returned. These are currently hard coded values.
 
This app is controlling the thermostats of a single home and that home has 2 thermostats. Appropriate errors are returned for accessing non-existent thermostats and non-existent properties.

No method is given for changing the ID.
To change the Name, call set_thermostat_name(name). Any string is acceptable.
To get read the Current Temperature, call read_temperature(). This generates a random double between 30.0 F and 100.0F. There is no default, the default is also randomly generated.
To change the Operating Mode, call set_operating_mode(mode). Modes are "cool", "heat", or "off". Default value is "off". Currently case insensitive too, but all entries are forced to lower casing. Values outside of these three are not accepted and generate this error ("Error": "The Mode entered: {mode} was not found in Thermostat operating states").
To change the Cool SetPoint, call set_cooling_set_point(temperature). Default value is 30.0F. Values outside of the range 30.0F - 100.0F are not accepted and generate this error ("Error": " The temperature {temperature} exceeds allowed temperature range of {Thermostat.lowest_allowed_set_point} to {Thermostat.highest_allowed_set_point}").
To change the Heat SetPoint, call set_heating_set_point(temperature). Default value is 100.0F. Values outside of the range 30.0F - 100.0F are not accepted and generate this error ("Error": "The temperature {temperature} exceeds allowed temperature range of {Thermostat.lowest_allowed_set_point} to {Thermostat.highest_allowed_set_point}").
To change the fan mode, call set_fan_mode(mode). Modes are "off" and "auto". Default value is "off". Currently case insensitive too, but all entries are forced to lower casing. Values outside of these 2 are not accepted and generate this error ("Error": "Fan mode entered: {mode} was not found in Thermostat fan operating states".)

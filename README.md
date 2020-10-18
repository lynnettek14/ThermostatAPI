# ThermostatAPI
API for controlling the state of thermostats in a home

Write a web.py ( http://webpy.org) app that exposes a RESTful API for controlling and retrieving the state of the thermostats in a home. In a real-world app you would be issuing commands to real thermostats. For this app, you can simply set and store the thermostat’s state within the app and return that state when requested. Everything can be done in memory (there is no need for persistence) and you can assume access from a single client (there is no need to deal with concurrency problems).
Welcome to web.py! (web.py)
webpy.org
web.py is a web framework for Python that is as simple as it is powerful. web.py is in the public domain; you can use it for whatever purpose with absolutely no ...
Thermostats have the following properties:
 ID (read only): unique system identifier for this thermostat (i.e 100 or 101)
 Name (read-write): display name (i.e “Upstairs Thermostat” and “Downstairs Thermostat”)
 Current Temp (read-only): since this is not a real home with real thermostats an appropriate random value can be returned for this property
 Operating Mode (read-write): one of “cool”, “heat”, “off”
 Cool SetPoint (read-write): a value between 30-100 degrees fahrenheit
 Heat SetPoint (read-write): a value between 30-100 degrees fahrenheit
 Fan Mode (read-write): either “off” or “auto”
You can assume this app is only controlling the thermostats of a single home and that home has 2 thermostats. You need to provide an API to list all the thermostats in the home and their current state (you can hard-code appropriate defaults at app startup). You need to provide APIs to edit the properties of each thermostat and query the state of those properties individually. Appropriate errors should get returned for accessing non-existent thermostats and non-existent properties.

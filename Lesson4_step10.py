class Device:
    __slots__ = ("_name", "_location", "_status")
    def __init__(self, name, location, status = 'ON'):
        self._name = name
        self._location = location
        self._status = status

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def status(self):
        return self._status

    @location.setter
    def location(self, value):
        self._location = value
    @status.setter
    def status(self, value):
        self._status = value

    def turn_on(self):
        self._status = "ON"

    def turn_off(self):
        self._status = "OFF"

class Light(Device):
    __slots__ = ("_brightness", "_color")
    def __init__(self, brightness, color, name, location):
        super().__init__(name, location)
        self._brightness = brightness
        self._color = color

    @property
    def brightness(self):
        return self._brightness

    @property
    def color(self):
        return self._color

    @brightness.setter
    def brightness(self, value):
        self._brightness = value

class Thermostat(Device):
    __slots__ = ("_current_temperature", "_target_temperature")
    def __init__(self, current_temperature, target_temperature, name, location):
        super().__init__(name, location)
        self._current_temperature = current_temperature
        self._target_temperature = target_temperature

    @property
    def current_temperature(self):
        return self._current_temperature

    @current_temperature.setter
    def current_temperature(self, value):
        self._current_temperature = value

    @property
    def target_temperature(self):
        return self._target_temperature

    @target_temperature.setter
    def target_temperature(self, value):
        self._target_temperature = value


class SmartTV(Device):
    __slots__ = ('_channel')

    def __init__(self, channel, name, location):
        super().__init__(name, location)
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value


















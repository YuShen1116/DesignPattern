from abc import ABC, abstractmethod


class Display(ABC):
    def __init__(self, temp=None, humidity=None, pressure=None):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure

    @abstractmethod
    def update(self, temp, humidity, pressure):
        raise NotImplementedError


class CurrentConditionsDisplay(Display):
    def update(self, temp, humidity, pressure):
        pass


class StatisticsDisplay(Display):
    def update(self, temp, humidity, pressure):
        pass


class ForecastDisplay(Display):
    def update(self, temp, humidity, pressure):
        pass


class WeatherData(object):
    def __init__(self):
        self.current_condition_display = CurrentConditionsDisplay()
        self.statistics_display = StatisticsDisplay()
        self.forecast_display = ForecastDisplay()

    def get_temperature(self):
        pass

    def get_humidity(self):
        pass

    def get_pressure(self):
        pass

    def measurements_changed(self):
        temp = self.get_temperature()
        humidity = self.get_humidity()
        pressure = self.get_pressure()

        self.current_condition_display.update(temp, humidity, pressure)
        self.statistics_display.update(temp, humidity, pressure)
        self.forecast_display.update(temp, humidity, pressure)

from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def register_observer(self, o):
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, o):
        raise NotImplementedError

    @abstractmethod
    def notify_observer(self):
        raise NotImplementedError


class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, o):
        self.observers.append(o)

    def remove_observer(self, o):
        self.observers.remove(o)

    def notify_observer(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measuerments_changed(self):
        self.notify_observer()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measuerments_changed()

    # Other methods


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        raise NotImplementedError


class Observer(ABC):
    @abstractmethod
    def update(self, temp, humidity, pressure):
        raise NotImplementedError


class CurrentConditionsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.weather_data = weather_data

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current conditions: {}F degress and {} humidity".format(self.temperature, self.humidity))

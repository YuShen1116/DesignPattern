from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError


class LightOnCommand(Command):

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class SimpleRemoteControl(object):

    def __init__(self):
        self.slot = None

    def set_command(self, command):
        self.slot = command

    def botton_was_pressed(self):
        self.slot.execute()

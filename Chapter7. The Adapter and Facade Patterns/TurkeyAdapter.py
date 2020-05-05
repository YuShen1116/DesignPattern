from abc import ABC, abstractmethod


class Duck(ABC):

    @abstractmethod
    def quack(self):
        raise NotImplementedError

    @abstractmethod
    def fly(self):
        raise NotImplementedError


class MallardDuck(Duck):

    def quack(self):
        print('Quack')

    def fly(self):
        print('Flying')


class Turkey(ABC):

    @abstractmethod
    def gobble(self):
        raise NotImplementedError

    @abstractmethod
    def fly(self):
        raise NotImplementedError


class WildTurkey(Turkey):

    def gobble(self):
        print('Gobble gobble')

    def fly(self):
        print('Flying short distance')


class TurkeyAdapter(Duck):

    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        self.turkey.fly()

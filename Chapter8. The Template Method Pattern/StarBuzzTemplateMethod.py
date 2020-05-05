from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    @abstractmethod
    def brew(self):
        raise NotImplementedError

    @abstractmethod
    def add_condiments(self):
        raise NotImplementedError

    @staticmethod
    def boil_water():
        print('Boiling water')

    @staticmethod
    def pour_in_cup():
        print('Pouring into cup')

    @staticmethod
    def customer_wants_condiments():
        return True


class Tea(CaffeineBeverage):
    def brew(self):
        print('Steeping the tea')

    def add_condiments(self):
        print('Adding Lemon')


class Coffee(CaffeineBeverage):
    def brew(self):
        print('Brewing coffee')

    def add_condiments(self):
        print('Adding sugar and milk')

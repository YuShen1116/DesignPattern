from abc import ABC, abstractmethod


class Beverage(ABC):

    def __init__(self):
        self.description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        raise NotImplementedError


class CondimentDecorator(Beverage):

    @abstractmethod
    def get_description(self):
        raise NotImplementedError


# Section of Beverage
class Espresso(Beverage):

    def __init__(self):
        super().__init__()
        self.description = 'Espresso'

    def cost(self):
        return 1.99


class HouseBlend(Beverage):

    def __init__(self):
        super().__init__()
        self.description = 'HouseBlend'

    def cost(self):
        return 0.89


# Section of Condiments
class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + 0.2


def main():
    beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.cost()))

    beverage = Mocha(beverage)
    print(beverage.get_description() + " $" + str(beverage.cost()))
    beverage = Mocha(beverage)
    print(beverage.get_description() + " $" + str(beverage.cost()))


if __name__ == "__main__":
    main()

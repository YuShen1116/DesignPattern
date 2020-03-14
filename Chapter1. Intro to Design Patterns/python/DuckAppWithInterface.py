from abc import ABC, abstractmethod


class FlyBehavior(ABC):

    @abstractmethod
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):

    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):

    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):

    def fly(self):
        print("I'm flying with a rocket!")


class QuackBehavior(ABC):

    @abstractmethod
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehavior):

    def quack(self):
        print("Quack")


class Squeak(QuackBehavior):

    def quack(self):
        print("Squeak")


class MuteQuack(QuackBehavior):

    def quack(self):
        print("<< Silence >>")


class Duck(ABC):
    """This implementation is focusing on the inferface instead of implementation,
    Duck class only need to how the interface for quack and fly, but careless on how they
    are implemented
    """

    def __init__(self, fly_behavior, quack_behavior):
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_fly(self):
        self.fly_behavior.fly()

    @property
    def fly_behavior(self):
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fb):
        self._fly_behavior = fb

    @property
    def quack_behavior(self):
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, qb):
        self._quack_behavior = qb

    @staticmethod
    def swim():
        print("All ducks float, even decoys!")

    @abstractmethod
    def display(self):
        raise NotImplementedError


class MallardDuck(Duck):

    def __init__(self, fly_behavior=FlyWithWings(), quack_behavior=Quack()):
        super().__init__(fly_behavior, quack_behavior)
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def display(self):
        print("I'm a real Mallard duck")


if __name__ == "__main__":
    mallard = MallardDuck()

    mallard.fly_behavior = FlyNoWay()
    mallard.perform_fly()

    mallard.fly_behavior = FlyRocketPowered()
    mallard.perform_fly()

    mallard.perform_quack()

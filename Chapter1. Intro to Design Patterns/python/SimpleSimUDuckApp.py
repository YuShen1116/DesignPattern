from abc import ABC, abstractmethod


class Duck(ABC):

    def quack(self):
        # do quack action
        raise NotImplementedError

    def swim(self):
        # do swim action
        raise NotImplementedError

    def fly(self):
        raise NotImplementedError

    # add other duck like methods

    @abstractmethod
    def display(self):
        raise NotImplementedError


class MallardDuck(Duck):

    def quack(self):
        pass

    def swim(self):
        pass

    def fly(self):
        pass

    def display(self):
        print("It looks like a mallard")


class RedHeadDuck(Duck):

    def quack(self):
        pass

    def swim(self):
        pass

    def fly(self):
        pass

    def display(self):
        print("It looks like a red head")


class RubberDuck(Duck):

    def swim(self):
        pass

    def quack(self):
        # overridden to Squeak
        pass

    def fly(self):
        # do not fly
        pass

    def display(self):
        print("It looks like a rubber duck")


"""
The key idea of this design: Inheritance

What's the disadvantage of it?

When you have more and more duck like instance, you'll have to override all the methods you need.
That makes future maintance become a nightmare
"""

if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.display()

from abc import ABC, abstractmethod


class PizzaIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self, dough_type):
        raise NotImplementedError

    @abstractmethod
    def create_cheese(self):
        raise NotImplementedError

    @abstractmethod
    def create_veggies(self):
        raise NotImplementedError

    @abstractmethod
    def create_pepperoni(self):
        raise NotImplementedError

    @abstractmethod
    def create_clam(self):
        raise NotImplementedError


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self, dough_type):
        return Dough()(dough_type)

    def create_cheese(self):
        pass

    def create_veggies(self):
        pass

    def create_pepperoni(self):
        pass

    def create_clam(self):
        pass


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self, dough_type):
        pass

    def create_cheese(self):
        pass

    def create_veggies(self):
        pass

    def create_pepperoni(self):
        pass

    def create_clam(self):
        pass


class Dough(object):
    def __call__(self, dough_type):
        if dough_type == 'thin_crust':
            return ThinCrustDough()
        elif dough_type == 'thick_crust':
            return ThickCrustDough


class ThinCrustDough(object):
    pass


class ThickCrustDough(object):
    pass

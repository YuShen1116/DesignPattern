from abc import ABC, abstractmethod


class Pizza(ABC):

    @abstractmethod
    def prepare(self):
        raise NotImplementedError

    @abstractmethod
    def bake(self):
        raise NotImplementedError

    @abstractmethod
    def cut(self):
        raise NotImplementedError

    @abstractmethod
    def box(self):
        raise NotImplementedError


class CheesePizza(Pizza):
    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class GreekPizza(Pizza):

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class PepperoniPizza(Pizza):

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class ClamPizza(Pizza):

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class VeggiePizza(Pizza):

    def prepare(self):
        pass

    def bake(self):
        pass

    def cut(self):
        pass

    def box(self):
        pass


class SimplePizzaFactory(object):

    def create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            pizza = CheesePizza()
        elif pizza_type == 'greek':
            pizza = GreekPizza()
        elif pizza_type == 'pipperoni':
            pizza = PepperoniPizza()
        elif pizza_type == 'clam':
            pizza = ClamPizza()
        elif pizza_type == 'veggie':
            pizza = VeggiePizza()
        else:
            raise NotImplementedError
        return pizza


class PizzaStore(ABC):

    def __init__(self, factory):
        self.factory = factory

    @abstractmethod
    def create_pizza(self, pizza_type):
        raise NotImplementedError

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.cut()
        return pizza


class NYStyleCheesePizza(object):
    pass


class NYStyleVeggiePizza(object):
    pass


class NYStylePizzaStore(PizzaStore):

    def create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            return NYStyleCheesePizza()
        elif pizza_type == 'veggie':
            return NYStyleVeggiePizza()
        else:
            return None


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        pass

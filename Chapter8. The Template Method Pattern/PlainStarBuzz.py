class Coffee(object):

    def prepare_recipe(self):
        self.boiling_water()
        self.brew_coffee()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    @staticmethod
    def boiling_water():
        print('Boiling Water')

    @staticmethod
    def brew_coffee():
        print('Brewing Coffee')

    @staticmethod
    def pour_in_cup():
        print('Pouring into cup')

    @staticmethod
    def add_sugar_and_milk():
        print('Adding Sugar and Milk')


class Tea(object):

    def prepare_recipe(self):
        self.boiling_water()
        self.steep_tea_bag()
        self.pour_in_cup()
        self.add_lemon()

    @staticmethod
    def boiling_water():
        print('Boiling Water')

    @staticmethod
    def steep_tea_bag():
        print('Steeping the tea')

    @staticmethod
    def pour_in_cup():
        print('Pouring into cup')

    @staticmethod
    def add_lemon():
        print('Adding lemon')

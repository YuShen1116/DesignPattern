from abc import ABC, abstractmethod


class Character(ABC):

    def __init__(self, weapon_behavior):
        self.weapon_behavior = weapon_behavior

    @abstractmethod
    def fight(self):
        raise NotImplementedError


class Queen(Character):

    def fight(self):
        self.weapon_behavior.use_weapon()


class King(Character):

    def fight(self):
        self.weapon_behavior.use_weapon()


class Troll(Character):

    def fight(self):
        self.weapon_behavior.use_weapon()


class Knight(Character):

    def fight(self):
        self.weapon_behavior.use_weapon()


class WeaponBehavior(ABC):

    @abstractmethod
    def use_weapon(self):
        raise NotImplementedError


class KnifeBehavior(WeaponBehavior):

    def use_weapon(self):
        print("Cutting with a knife")


class BowAndArrowBehavior(WeaponBehavior):

    def use_weapon(self):
        print("Shooting arrow with a bow")


class AxeBehavior(WeaponBehavior):

    def use_weapon(self):
        print("Chopping with an axe")


class SwordBehavior(WeaponBehavior):

    def use_weapon(self):
        print("Swinging a sword")


if __name__ == "__main__":

    axe = AxeBehavior()
    queen = Queen(axe)
    queen.fight()

    knife = KnifeBehavior()
    queen.weapon_behavior = knife
    queen.fight()

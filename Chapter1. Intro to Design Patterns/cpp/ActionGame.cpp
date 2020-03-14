#include <iostream>
#include "Character.h"
#include "WeaponBehavior.h"

int main() {

    KnifeBehavior knife;
    AxeBehavior axe;
    SwordBehavior sword;
    BowAndArrowBehavior bow_and_arror;

    Queen queen(knife);
    queen.info();
    queen.fight();
    queen.set_weapon(axe);
    queen.fight();

    Knight knight(sword);
    knight.info();
    knight.fight();
    knight.set_weapon(bow_and_arror);
    knight.fight();

    return 0;
}

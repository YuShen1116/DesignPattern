//
// Created by Yu Shen on 3/13/20.
//

#ifndef CPP_CHARACTER_H
#define CPP_CHARACTER_H

#include "WeaponBehavior.h"


class Character {
// _weapon_behavior should be a pointer, because all concrete weapon implementations are the child of
// WeaponBehavior, if _weapon_behavior is not a pointer, no matter what child behavior you pass in the contractor,
// you will call the function in parent class
    WeaponBehavior *_weapon_behavior;
public:
    explicit Character(WeaponBehavior &weapon_behavior);

    void fight();

    void set_weapon(WeaponBehavior &weapon_behavior);

    virtual void info();
};


class Queen : public Character {
public:
    using Character::Character;

    void info() override;
};

class King : public Character {
public:
    using Character::Character;

    void info() override;
};

class Knight : public Character {
public:
    using Character::Character;

    void info() override;
};

class Troll : public Character {
public:
    using Character::Character;

    void info() override;
};

#endif //CPP_CHARACTER_H

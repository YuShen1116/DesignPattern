//
// Created by Yu Shen on 3/13/20.
//

#include "Character.h"
#include "iostream"


Character::Character(WeaponBehavior &weapon_behavior) {
    this->_weapon_behavior = &weapon_behavior;
}

void Character::set_weapon(WeaponBehavior &weapon_behavior) {
    this->_weapon_behavior = &weapon_behavior;
}

void Character::fight() {
    this->_weapon_behavior->use_weapon();
}

void Character::info() {
    std::cout << "Not Implemented." << std::endl;
}

void Queen::info() {
    std::cout << "This is Queen." << std::endl;
}

void King::info() {
    std::cout << "This is King." << std::endl;
}

void Knight::info() {
    std::cout << "This is Knight." << std::endl;
}

void Troll::info() {
    std::cout << "This is Troll." << std::endl;
}
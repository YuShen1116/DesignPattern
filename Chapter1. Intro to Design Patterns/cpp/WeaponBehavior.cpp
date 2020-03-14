//
// Created by Yu Shen on 3/13/20.
//

#include "WeaponBehavior.h"
#include "iostream"

void WeaponBehavior::use_weapon() {
    std::cout << "Not Implemented." << std::endl;
}


void KnifeBehavior::use_weapon() {
    std::cout << "Fight with knife." << std::endl;
}

void AxeBehavior::use_weapon() {
    std::cout << "Fight with axe." << std::endl;
}

void BowAndArrowBehavior::use_weapon() {
    std::cout << "Fight with bow and arrow." << std::endl;
}

void SwordBehavior::use_weapon() {
    std::cout << "Fight with sword." << std::endl;
}
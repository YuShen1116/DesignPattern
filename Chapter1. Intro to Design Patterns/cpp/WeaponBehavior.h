//
// Created by Yu Shen on 3/13/20.
//

#ifndef CPP_WEAPONBEHAVIOR_H
#define CPP_WEAPONBEHAVIOR_H


class WeaponBehavior {
public:
    WeaponBehavior() = default;

    ~WeaponBehavior() = default;

    virtual void use_weapon();
};


class KnifeBehavior : public WeaponBehavior {
    void use_weapon() override;
};

class AxeBehavior : public WeaponBehavior {
    void use_weapon() override;
};

class SwordBehavior : public WeaponBehavior {
    void use_weapon() override;
};

class BowAndArrowBehavior : public WeaponBehavior {
    void use_weapon() override;
};

#endif //CPP_WEAPONBEHAVIOR_H

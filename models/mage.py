from fighters import Fighters
from attacks import *
from pprint import pprint


class Mage(Fighters):
    def __init__(self, name="Mediv", hp=100):
        super().__init__(name, hp)
        self.append_attacks(WeakAttack("Fireball"))
        self.append_attacks(MediumAttack("Solar Flare"))
        self.append_attacks(SpecialAttack("Void Vortex"))


if __name__ == "__main__":
    test_mage = Mage()
    print(test_mage)#Object
    print(test_mage.get_info)#Infos
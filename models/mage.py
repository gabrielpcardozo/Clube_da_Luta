from fighters import Fighters
from attacks import *
from pprint import pprint


class Mage(Fighters):
    def __init__(self, name="Mediv", hp=100):
        super().__init__(name, hp)
        self.append_attacks(WeakAttack("Fireball"))
        self.append_attacks(MediumAttack("Solar Flare"))
        self.append_attacks(SpecialAttack("Void Vortex"))
        
        """
        self.append_attacks(WeakAttack("Fireball"))
        self.append_attacks(MediumAttack("Solar Flare Burst"))
        self.append_attacks(SpecialAttack("Void Vortex"))
        """

    def show_atacks(self):
        attacks = {self.weakattack:self.weakattack}
        return attacks

if __name__ == "__main__":
    print("Um mage em sua tela")
    mage = Mage()
    pprint(mage.get_info)
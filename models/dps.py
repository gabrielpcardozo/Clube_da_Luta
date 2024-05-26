from fighters import Fighters
from attacks import *

class Dps(Fighters):
    def __init__(self, name="Katarina", hp=100):
        super().__init__(name, hp)
        self.append_attacks(WeakAttack("Eagle's Mark"))
        self.append_attacks(MediumAttack("Shadowstrike"))
        self.append_attacks(SpecialAttack("Viper's Kiss"))


if __name__ == "__main__":
    a = Dps()
    print(a.get_info)
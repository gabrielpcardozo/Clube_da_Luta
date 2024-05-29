from .fighters import Fighters
from .attacks import Attack, WeakAttack, MediumAttack, SpecialAttack

class Warrior(Fighters):
    def __init__(self, name="Arthur", hp=100):
        super().__init__(name, hp)
        self.append_attacks(WeakAttack("Blade Dance"))
        self.append_attacks(MediumAttack("Shadow Veil"))
        self.append_attacks(SpecialAttack("Soul Reaver"))


if __name__ == "__main__":
    a = Warrior()
    print(a.get_info)
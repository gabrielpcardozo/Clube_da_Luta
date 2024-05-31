#from attacks import Attack, WeakAttack, MediumAttack, SpecialAttack
from .attacks import Attack, WeakAttack, MediumAttack, SpecialAttack

class Fighters:
    
    def __init__(self, name, hp =100):
        self.__name = name
        self.__hp = hp
        self.__attacks = []
    
    #Criando os getters.
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_hp(self):
        return self.__hp

    @property
    def get_attacks(self):
        return self.__attacks
    
    @property
    def get_habilitie(self):
        all_attacks = [attack.get_info() for attack in self.__attacks]
        return all_attacks

    @property
    def get_habilitie_names(self):
        return [attack.get_name() for attack in self.__attacks]

    @property
    def get_habilitie_damages(self):
        return [attack.get_damage() for attack in self.__attacks]

    @property
    def get_info(self):
        attacks_info = [attack.get_info() for attack in self.__attacks]
        return {
            'name': self.__name,
            'hp': self.__hp,
            'attacks': attacks_info
        }


    def append_attacks(self, attack):
        self.__attacks.append(attack)


    def receive_damage(self, damage):
        print(f"{self.__name} recebendo {damage} de dano.")  # Debug print
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0
        print(f"{self.__name} agora tem {self.__hp} de HP.")  # Debug print

    def combat(self,target, attack_index):
        if 0 <= attack_index < len(self.__attacks):
            damage = self.get_habilitie[attack_index]["damage"]
            target.receive_damage(damage)
            return damage
        else:
            return "Damage: 0"

    """def __str__(self):
        return f"Fighter(name={self.__name}, hp={self.__hp}, attacks={[str(attack) for attack in self.__attacks]})"
    
    def __repr__(self):
        return self.__str__()"""

if __name__ == "__main__":
    pass
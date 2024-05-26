from attacks import Attack, WeakAttack, MediumAttack, SpecialAttack

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
        return self._Lutadores__hp

    
    @property
    def get_attack(self):
        return self.__attacks
    
    @property
    def get_damage(self):
        return[attack.dano for attack in self.__attacks]

    @property
    def get_habilities(self):
        abilities_list = [f"{index + 1}. {attack.nome} - Dano: {attack.dano}" for index, attack in enumerate(self.__attacks)]
        return "\n".join(abilities_list)

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
        self.__hp -= damage
        if self.__hp < 0:
            self.__hp = 0

    def damage(self,target, attack_index):
        if 0 <= attack_index < len(self.__attacks):
            damage = self.__attacks[attack_index].dano
            target.receive_damage(damage)
            return damage
        else:
            return "Damage: 0"

if __name__ == "__main__":
    a = Fighters("Gabriel")
    print(a.get_name)
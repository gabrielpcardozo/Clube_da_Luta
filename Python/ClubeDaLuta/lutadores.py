
class Attacks:
    
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano

    def __str__(self) -> str:
        return f"Habilidade:{self.nome}, dano:{self.dano}"
    
    def get_habiliti(self):
        return self.nome
    
    def get_damage(self):
        return self.dano

class Lutadores:
    
    def __init__(self, name, hp =100):
        self.__name = name
        self.__hp = hp
        self.__attacks = []

    def __str__(self):
        list_attacks = ", ".join([str(attack) for attack in self.__attacks])
        return f"Name: {self.__name}, HP: {self.__hp}, Golpes: [{list_attacks}]"

    #Criando os getters.
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_hp(self):
        return self._Lutadores__hp

    def append_attacks(self, attack):
        self.__attacks.append(attack)
    
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


class Mage(Lutadores):
    def __init__(self, name="Mediv", hp=100):
        super().__init__(name, hp)
        self.append_attacks(Attacks("Fireball",5))
        self.append_attacks(Attacks("Solar Flare Burst", 10))
        self.append_attacks(Attacks("Void Vortex", 30))
    
class Warrior(Lutadores):
    def __init__(self, name="Arthur", hp=100):
        super().__init__(name, hp)
        self.append_attacks(Attacks("Blade Dance", 5))
        self.append_attacks(Attacks("Shadow Veil", 10))
        self.append_attacks(Attacks("Soul Reaver", 30))

class Archer(Lutadores):
    def __init__(self, name="Katarina", hp=100):
        super().__init__(name, hp)
        self.append_attacks(Attacks("Eagle's Mark", 5))
        self.append_attacks(Attacks("Shadowstrike", 10))
        self.append_attacks(Attacks("Viper's Kiss", 30))

if __name__ == "__main__":
    test_mage = Mage()
    test_warrior = Warrior()
    print(f"vida do mago:{test_mage.get_hp} <--> vida do guerreiro:{test_warrior.get_hp}")
    test_mage.damage(test_warrior,2)
    print(f"vida do mago{test_mage.get_hp} <--> vida do guerreiro:{test_warrior.get_hp}")
    pass
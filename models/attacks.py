class Attack:
    def __init__(self, name, damage = int):
        self.__name = name
        self.__damage = damage


    def __str__(self) -> str:
        return f"Habilidade:{self.__name}, dano:{self.__damage}"
    

    def get_info(self):
        return {
            'name': self.__name,
            'damage': self.__damage
        }

    def get_name(self):
        return self.__name
    
    def get_damage(self):
        return self.__damage
    
    def set_attacks(self, attack_name = None, damege_1= None):
        self.nome = attack_name
        self.dano = damege_1
        return f'Nome :{attack_name}' + f'Damage:{damege_1}'


class WeakAttack(Attack):
    def __init__(self, name):
        super().__init__(name, 10)

    def set_name(self, attack_name):
        self.__name = attack_name
        return attack_name
    
    def __repr__(self):
        return self.__str__()

class MediumAttack(Attack):
    def __init__(self, name):
        super().__init__(name, 20)

    def set_name(self, attack_name):
        self.__name = attack_name
        return attack_name
    
    def __repr__(self):
        return self.__str__()

class SpecialAttack(Attack):
    def __init__(self, name):
        super().__init__(name, 30)

    def set_name(self, attack_name):
        self.__name = attack_name
        return attack_name
    
    def __repr__(self):
        return self.__str__()


if __name__ == "__main__": 
    print(Attack("Classe Attack", 000))
    print(WeakAttack("Classe Attack Fraco"))
    print(MediumAttack("Classe Attack Medio"))
    print(SpecialAttack("Classe Attack Especial"))

#Sistema de batalhas com as as instancias e a possivel escolha de uma das classes dos lutadores. 
"""
Temos tres classes de personagens:
    Lutadores 
        Mago -> Mediv
        Warrior -> Arthur
        Archer -> Katarina
"""

import  random
from lutadores import Lutadores, Attacks, Mage, Warrior, Archer
import time

def choose_class():
    #Opcoes disponiveis das classes.
    print("Com qual dessas classes você deseja lutar?\n")
    print("1. Mage")
    print("2. Warrior")
    print("3. Archer")
    choice = int(input("\nEscolha um:\n"))
    #escolha das classes
    if choice == 1:
        return Mage()
    elif choice == 2:
        return Warrior()
    elif choice == 3:
        return Archer()
    else:
        return "Classe não encontrada"
    
player = choose_class()
choose_pc = [Mage(), Warrior(), Archer()]
pc = random.choice(choose_pc)


def battle(player, pc):
    #Introdução do sistema de batalhas. 
    print(f"Seja bem vindo Lutador!\n")
    print(f"\nSeu opnonente vai ser {pc.get_name}")
    print("\nVamos começar a Luta!!")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Lutem!!")
    #Loop que só vai parar quando o HP de um lutador foir <= a 0
    while player.get_hp >= 0 or pc.get_hp >= 0:
        turn = 1
        #Mostra a vida dos players
        live_status = f"\nPlayer:{player.get_name} | HP:{player.get_hp} ==================== PC:{pc.get_name} | HP:{pc.get_hp}"
        print(live_status)
        print(f"\nEscolha um:\n{player.get_habilities}")
        #Escolhas de atauqes
        #Ataques do player
        choice = int(input("Qual o seu ataque?\n")) -1
        #Ataque do PC
        pc_attack = random.choice(pc.get_attack)

        #Aplicar o dano depois da escolha dos ataques 
        player_damage = player.damage(pc, choice)
        pc_damage = pc.damage(player, pc.get_attack.index(pc_attack))
        #Mostra o golpe e o dano que vai ser ser aplicado.
        print(f"\n O Lutador {player.get_name}, usou o {player.get_attack[choice].nome}, e causou {player_damage}")
        print(f"\n O Lutador {pc.get_name}, usou o {pc_attack.nome}, e causou {pc_damage}")
        
        if player.get_hp <= 0:
            print(f"O pc usando o personagem:{pc.get_name} Venceu!!")
            break        
        elif pc.get_hp <= 0:
            print(f"Você player usando o personagem:{player.get_name} Venceu!!")
            break
        else:
            turn += 1
            print(f"Roud - {turn}")



battle(player, pc)

if __name__ == "__main__":
    test = Mage()
    #print(test.get_attack)
    #print(test.get_habilities)
    pass
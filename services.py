#Battle System. | Somente com variaveis.
"""
Dentro desse arquivo eu foi o primeiro prototipo de como eu conseguiria criar um sistema de batalhas simples. 
A ideia aqui foi seguir com duas variaveis e nao com duas intancias, porem agora o foco e trabalhar com as instancias.
"""

import random

def luta():
    while pc["hp"] >= 0 or jogador["hp"] >= 0:
        print(f'{moves} \n')
        turn = input("Esse é o seu turno faça a sua jogada:\n")
        if turn == "soco":
            pc["hp"] -= 10
        elif turn == "chute":
            pc["hp"] -= 10
        elif turn == "especial":
            pc["hp"] -= 30
        else:
            print('golpe nao encontrado')

        if pc["hp"] <= 0:
            print("O JOGADOR ganhou!!")
            break
        elif jogador["hp"] <= 0:
            print("O PC ganhou!!")
            break
        else:
            choice_pc = random.choice(list(moves.values()))
            jogador["hp"] -= choice_pc
            print(f'Jogador_HP:{jogador["hp"]} <---> PC_HP:{pc["hp"]}')

if __name__ == "__main__":
    luta()
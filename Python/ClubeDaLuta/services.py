#Battle System.
import random
from lutadores import Lutadores

primeiro = Lutadores("Gabriel")
segundo = Lutadores("João")


soco = 10
chute = 10 
especial = 30
moves = {"soco":10, "chute":10, "especial":30}

jogador = {"Nome":'Gabriel','hp':100, "Golpes":moves}
pc = {"Nome":'Vitor','hp':100, "Golpes":moves}

status = f'{jogador["Nome"]}, HP:{jogador["hp"]} < ------------------------ > {pc["Nome"]}, HP:{pc["hp"]}'

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
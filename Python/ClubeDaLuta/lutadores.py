class Lutadores:
    
    def __init__(self, name, hp =100):
        self.name = name
        self.hp = hp

    def moves(self):
        soco = 10
        chute = 10 
        especial = 30
        moves = [soco, chute, especial]
        return moves
    
    def get_hp(self):
        hp = self.hp
        hp = 150
    
    def __str__(self):
        return f"Meu nome é {self.name}, eu estou com {self.hp} de vida"


"""
primeiro = Lutadores("Gabriel")
print(primeiro.moves)
segundo = Lutadores("João")
print(segundo)
"""
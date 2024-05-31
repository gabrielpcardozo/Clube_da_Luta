import sys
from pathlib import Path # if you haven't already done so
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))


import time
import random

from models.fighters import Fighters
from models.mage import Mage
from models.warrior import Warrior
from models.dps import Dps
from models.attacks import Attack, WeakAttack

attack = WeakAttack("Fireball")

#print(attack.get_name())
#print(attack.get_damage())

player = Mage()
pc = Warrior()
print(random.choice(player.get_attacks["dano"]))

#print(player.get_habilitie_names)
#print(player.get_habilitie_damages)

#player_damage = player.damage(pc, 1)
#pc_damage = pc.damage(player, pc.get_attack.index(1))

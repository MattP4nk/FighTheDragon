##Generic Fight The Dragon text game
import DragonClass, PlayerClass
from random import randint
dragon = DragonClass.Dragon("Ancient Dragon", 1500, 30, 30, 60, 50)


def DObjetive(player): #Here it's defined the Dragon Attack objective 
    if player.aCompanion == 1:
        a = randint(1, 6)
        if a<3 or player.taunt == 1:
            objetive = bear
        else:
            objetive = player
    else:
            objetive = player
    return objetive


juego()


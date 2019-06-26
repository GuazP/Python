from random import randint
from math import floor
class Player():
    def __init__(self, name, SW, PWW):
        self.HP = 4
        modifier = 2
        self.name = name
        self.atak = (1+floor(modifier*SW), 100+floor(modifier*SW))
        self.obrona = (50+floor(modifier*PWW))

    def __str__(self):
        return self.name

    def hit(self, Enemy):
        roll = randint(*self.atak)
        if roll < self.atak[0]+5:   #Fail
            return "Fail"
        elif roll > self.atak[1]-5: #Crit
            Enemy.HP -= 2
            return "Crit"
        elif roll > Enemy.obrona:   #Hit
            Enemy.HP -= 1
            return "Hit"
        else:                       #Miss
            return "Miss"

    def reset(self):
        self.HP = 4

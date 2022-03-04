import random

randint = random.randint


def rand(x, y=None):
    if type(x) == list:
        return randint(*x)
    if not y:
        y = x
    return randint(x, y)


class Enemy:
    def __init__(self, name, strength, agility, hitpoints, sleep_resist, stopspell_resist,
                 hurt_resist, dodge, experience, gold, pattern=""):
        self.name = name
        self.strength = strength
        self.agility = agility
        self.hitpoints = rand(hitpoints)
        self.sleep_resist = sleep_resist
        self.stopspell_resist = stopspell_resist
        self.hurt_resist = hurt_resist
        self.dodge = dodge
        self.experience = experience
        self.gold = rand(gold)
        self.pattern = pattern


enemies = [
    ["Slime", 5, 3, 3, 0, 15/16, 0, 1/64, 1, 1],
    ["Red Slime", 7, 3, 4, 0, 15/16, 0, 1/64, 1, 2],
    ["Drakee", 9, 6, [5, 6], 0, 15/16, 0, 1/64, 2, 2],
    ["Ghost", 11, 8, [6, 7], 0, 15/16, 0, 4/64, 3, [3, 4]],
    ["Magician", 11, 12, [10, 13], 0, 0, 0, 1 / 64, 4, [9, 11]],
    ["Magidrakee", 14, 14, [12, 15], 0, 0, 0, 1 / 64, 5, [9, 11]],
    ["Scorpian", 18, 16, [16, 20], 0, 15 / 16, 0, 1 / 64, 6, [12, 15]],
    ["Druin", 20, 18, [17, 22], 0, 15 / 16, 0, 2 / 64, 7, [12, 15]],
    ["Poltergeist", 18, 20, [18, 23], 0, 0, 0, 6 / 64, 8, [13, 17]],
    ["Droll", 24, 24, [19, 25], 0, 14 / 16, 0, 2 / 64, 10, [18, 24]],
    ["Drakeema", 22, 26, [16, 20], 2/16, 0, 0, 6 / 64, 11, [15, 19]],
    ["Skeleton", 28, 22, [23, 30], 0, 15 / 16, 0, 4 / 64, 11, [22, 29]]

]

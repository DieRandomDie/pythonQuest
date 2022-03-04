class Hero:
    def __init__(self, name="Link", health=15, strength=4, agility=4, magic=0):
        self.name = name
        self.max_health = health
        self.current_health = health
        self.strength = strength
        self.agility = agility
        self.magic = magic
        self.x = 3
        self.y = 6

    def change_hp(self, hp):
        if self.current_health+hp >= self.max_health:
            self.current_health = self.max_health
        elif self.current_health+hp <= 0:
            self.current_health = 0
        else:
            self.current_health = self.current_health+hp

    def move(self, x, y):
        self.x = x
        self.y = y



print()

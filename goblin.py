import entity
import random

class Goblin(entity.Entity):
    '''Goblin class, can attack and take damage. Part of the expert factory. Hp: 6-10. Dmg: 4-8'''
    def __init__(self):
        super().__init__('Grievous Goblin', random.randint(6,10))

    def attack(self, ent):
        try:
            dmg = random.randint(4,8)
            ent.take_damage(dmg)
            print(f'{super().get_name()} attacked {ent.get_name()} for {dmg}.')
        except:
            raise TypeError


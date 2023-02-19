import entity
import random

class Troll(entity.Entity):
    '''Troll class, can attack and take damage. Part of the expert factory. Hp: 10-14. Dmg: 8-12'''
    def __init__(self):
        super().__init__('Terrible Troll', random.randint(10,14))

    def attack(self, ent):
        try:
            dmg = random.randint(8,12)
            ent.take_damage(dmg)
            print(f'{super().get_name()} attacked {ent.get_name()} for {dmg}.')
        except:
            raise TypeError


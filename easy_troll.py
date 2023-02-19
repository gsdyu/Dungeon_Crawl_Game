import entity
import random

class EasyTroll(entity.Entity):
    '''Easy Troll class, can attack and take damage. Part of the beginner factory. Hp: 4-5. Dmg: 1-5'''
    def __init__(self):
        super().__init__('Internet Troll', random.randint(4,5))

    def attack(self, ent):
        try:
            dmg = random.randint(1,5)
            ent.take_damage(dmg)
            print(f'{super().get_name()} attacked {ent.get_name()} for {dmg}.')
        except:
            raise TypeError


import entity
import random

class EasyOgre(entity.Entity):
    '''Easy Ogre class, can attack and take damage. Part of the beginner  factory. Hp: 3-5. Dmg: 1-4'''
    def __init__(self):
        super().__init__('Old Ogre', random.randint(3,5))

    def attack(self, ent):
        try:
            dmg = random.randint(1,4)
            ent.take_damage(dmg)
            print(f'{super().get_name()} attacked {ent.get_name()} for {dmg}.')
        except:
            raise TypeError


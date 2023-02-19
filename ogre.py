import entity
import random

class Ogre(entity.Entity):
    '''Ogre class, can attack and take damage. Part of the expert factory. Hp: 8-12. Dmg: 6-10'''
    def __init__(self):
        super().__init__('Ominious Ogre', random.randint(8,12))

    def attack(self, ent):
        try:
            dmg = random.randint(6,10)
            ent.take_damage(dmg)
            print(f'{super().get_name()} attacked {ent.get_name()} for {dmg}.')
        except:
            raise TypeError


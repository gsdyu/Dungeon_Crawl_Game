import entity
import random

class EasyGoblin(entity.Entity):
    '''Easy Goblin class, can attack and take damage. Part of the beginner factory. Hp: 3-4. Dmg: 1-3'''
    def __init__(self):
        super().__init__('Gullible Goblin', random.randint(3,4))

    def attack(self, ent):
        try:
            dmg = random.randint(1,3)
            ent.take_damage(dmg)
            print(f'{super().get_name()} attacked {ent.get_name()} for {dmg}.')
        except:
            raise TypeError


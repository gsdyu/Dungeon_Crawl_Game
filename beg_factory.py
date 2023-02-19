import enemy_factory
import random
import easy_troll
import easy_ogre
import easy_goblin

class BeginnerFactory(enemy_factory.EnemyFactory):
    '''Beginner Factory class, constructs and returns a random enemy with different health pool and damage. Enemy is either an Easy Troll, Easy Ogre, or Easy Goblin'''
    def create_random_enemy(self):
        choice = random.randint(0,2)
        if choice == 0:
            return easy_troll.EasyTroll()
        elif choice == 1:
            return easy_ogre.EasyOgre()
        elif choice == 2:
            return easy_goblin.EasyGoblin()

            


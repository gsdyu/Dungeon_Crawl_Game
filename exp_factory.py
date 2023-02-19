import enemy_factory
import random
import troll
import ogre
import goblin

class ExpertFactory(enemy_factory.EnemyFactory):
    '''Expert Factory class, constructs and returns a random enemy with different health pool and damage. Enemy is either Troll, Ogre, or Goblin'''
    def create_random_enemy(self):
        choice = random.randint(0,2)
        if choice == 0:
            return troll.Troll()
        elif choice == 1:
            return ogre.Ogre()
        elif choice == 2:
            return goblin.Goblin()

            


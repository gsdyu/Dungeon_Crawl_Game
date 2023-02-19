import abc
class EnemyFactory(abc.ABC):
    '''Enemy Factory abstract class, abstract class for beginner and expert factory'''
    @abc.abstractmethod
    def create_random_enemy(self):
        pass
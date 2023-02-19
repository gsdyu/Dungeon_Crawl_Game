import entity
import random
import map

class Hero(entity.Entity):
    '''Hero class, has a name and a location of the hero on the map
    This is what the user will play as in the dungeon game'''
    
    def __init__(self, name):
        '''initializes the Hero object
        var:
            name: string, name of the hero
            loc: int[], location of the hero on the map'''
        super().__init__(name, 25)
        self.loc = [0,0]

    def attack(self, enemy):
        '''abstract, attacks the given entity. gives an error if given is not of type entity
        var: entity, class, entity chosen to be attack
        '''
        if not isinstance(enemy, entity.Entity):
            raise ValueError("Must be an entity to attack.")
        
        dmg = random.randint(2,5)
        enemy.take_damage(dmg)
        return(f'The hero slashed the {enemy.get_name()} for {dmg} damage.')

    def get_loc(self):
        '''returns the curent location of the hero'''
        return self.loc

    def go_north(self):
        '''hero goes north and shows map unless out of bound'''
        if self.loc[0] == 0:
            return 'x'
        self.loc[0] -= 1
        return self.loc
        pass

    def go_south(self):
        '''hero goes south and shows map unless out of bound'''
        if self.loc[0] == len(map.Map()) - 1:
            return 'x'
        self.loc[0] += 1
        return self.loc
        pass

    def go_east(self):
        '''hero goes east and shows map unless out of bound.'''
        if self.loc[1]==len(map.Map()[0]) - 1:
            return 'x'
        self.loc[1] += 1
        return self.loc
        pass

    def go_west(self):
        '''hero goes west and shows map unless out of bound'''
        if self.loc[1] == 0:
            return 'x'
        self.loc[1] -= 1
        return self.loc
        pass

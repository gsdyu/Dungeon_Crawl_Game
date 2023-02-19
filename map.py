class Map:
    '''class Map, singleton, this will be the map of the dungeon the 
    hero explores. There will be a map and a revealed map. The difference is 
    that map will show all the event and revealed map shows what part
    of the map is explored. Not explored parts are hidden with an x'''
    _instance = None
    _initialized = False

    def __new__(cls):
        '''makes a new map object if does not exist. Else, returns the existing
        map'''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        '''initalizes the map and the revealed map if does not exist already
        var: _map: str[][], map with all the events in the dungeon

        '''
        if not Map._initialized:
            self.load_map(0)
            Map._initialized = True




    def __getitem__(self,row):
        '''returns the row in the map if index is in range
        '''
        try:
            return self._map[row]
        except:
            raise Exception

    def __len__(self):
        '''makes it so that it returns the length of the map, also accessible 
        as a column
        '''
        return len(self._map)

    def show_map(self, loc):
        '''Shows a 5x5 diagram of the map with the areas that are revealed, not revealed, and the location
        of the hero.
        var:
            loc: intp[], current location of the hero
        '''
        map = ''
        for x in range(len(self._revealed)):
            for y in range(len(self._revealed[x])):
                if self._revealed[x][y] == False and not ((x == loc[0] and y == loc[1])):
                    map += 'x '
                elif (x == loc[0] and y == loc[1]):
                    map += '* '
                else:
                    map += f'{self._map[x][y]} '
            map += '\n'
        return map
        pass

    def reveal(self, loc):
        '''makes a location on the revealed map reveal
        var:
            loc, int[], location that should be revealed
        '''
        try:
            self._revealed[loc[0]][loc[1]] = True
        except:
            raise Exception

    def remove_at_loc(self,loc):
        '''changes the status of the given coordinate to n
        var: loc, int[], coordinate of where to change
        '''
        self._map[loc[0]][loc[1]] = 'n'

    def load_map(self, map_num):
        '''loads into the map chosen by the number
        var: map_num, int, chosen number for map'''
        maps = ['map1.txt','map2.txt','map3.txt']
        try:
            txt = open(maps[map_num%3], 'r')
        except:
            raise Exception
        self._map = []
        i = 0
        for line in txt:
            line = line.strip()
            self._map.append([])
            for letter in line:
                self._map[i].append(letter)
            i+=1
        txt.close()
        self._revealed = [[False for x in range(len(self._map))] for y in range(len(self._map[0]))]

    pass
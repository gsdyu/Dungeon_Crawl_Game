"""
This program simulates a game where a hero travels through a dungeon until
they find the exit to win. They will fight through variety of monsters and
they can heal from item rooms containing a potion. The map class  
"""
import hero
import beg_factory
import exp_factory
import map
import check_input
import random

def main():
    '''Deals with the user interface of the game: getting the name for the hero
    traveling through the dungeon, getting the difficulty of the monsters, fighting the monster if exist, continuing to the next level
    after finding the exit, ending the game when the hero dies.'''
    name = input("Enter the name of your Hero: ")
    diff = check_input.get_int_range("Difficulty:\n1.Beginner\n2.Expert\n",1, 2)
    if diff == 1:
        factory = beg_factory.BeginnerFactory()
        pass
    elif diff == 2:
        factory = exp_factory.ExpertFactory()
    m = map.Map()
    mcount = 0
    h = hero.Hero(name)
    m.reveal(h.get_loc())
    while h.get_hp() > 0:
        print()
        print(h)
        print(m.show_map(h.get_loc()))
        choice = check_input.get_int_range('\n1. Go North\n2. Go South\n3. Go East\n4. Go West\n5. Quit\nEnter choice: ', 1, 5)
        if choice == 5:
            break
        if choice == 1:
            move = h.go_north()
        elif choice == 2:
            move = h.go_south()
        elif choice == 3:
            move = h.go_east()
        elif choice == 4:
            move = h.go_west()
        if move == 'x':
            print('You cannot go that way...')
            continue
        print(m.show_map(move))
        m.reveal(h.get_loc())
        if m[h.get_loc()[0]][h.get_loc()[1]] == 'm':
            monster = factory.create_random_enemy()
            print(f'You encounter a {monster}')
            while monster.get_hp() > 0:
                fight = check_input.get_int_range(f'1. Attack {monster.get_name()}\n2. Run Away\nEnter choice: ',1, 2)
                if fight == 1:
                    print(h.attack(monster))
                    if monster.get_hp() == 0:
                        print(f"{h.get_name()} have slain a {monster.get_name()}")
                        m.remove_at_loc(h.get_loc())
                        break
                    monster.attack(h)
                    if h.get_hp() == 0:
                        break
                elif fight == 2:
                    while True:
                        rint = random.randint(1,4)
                        if rint == 1:
                            ran = h.go_north()
                        elif rint == 2:
                            ran = h.go_south()
                        elif rint == 3:
                            ran = h.go_east()
                        elif rint == 4:
                            ran = h.go_west()
                        if ran != 'x':
                            m.reveal(h.get_loc())
                            break
                    break
            continue
        if m[h.get_loc()[0]][h.get_loc()[1]] == 'n':
            print("The room is empty.")
            continue
        if m[h.get_loc()[0]][h.get_loc()[1]] == 's':
            print("You landed back where you started")
            continue
        if m[h.get_loc()[0]][h.get_loc()[1]] == 'i':
            print("You found a health potion.")
            if h.get_hp() == h.get_max_hp():
                print("You are already max health.")
                continue
            h.heal()
            m.remove_at_loc(h.get_loc())
            print(f"{h.get_name()} healed to full health.")
            continue
        if m[h.get_loc()[0]][h.get_loc()[1]] == 'f':
            print(f'Congratulation! {h.get_name()} found the entrance to the next level!')
            mcount += 1
            mcount = mcount
            m.load_map(mcount)
            m.reveal(h.get_loc())
    print("Game Over")

main()
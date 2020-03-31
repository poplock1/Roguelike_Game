import helpers


def display_board(board):
    '''
    Displays complete game board on the screen


    Returns:
    Nothing
    '''
    for element in board:
        for e in element:
            print(e, end="")
        print()


def print_boss(message):
    """
    message is a list of 8 strings
    """
    helpers.clear_screen()
    WIDHT_OF_SCREEN = 80
    print("*" * WIDHT_OF_SCREEN)
    for element in message:
        a = element.center(WIDHT_OF_SCREEN)
        b = '(' + a + ')'
        print(b)
    print("*" * WIDHT_OF_SCREEN)
    with open('Levels/boss_image.txt', 'r') as boss:
        boss = boss.readlines()
    for line in boss:
        print(line, end='')
    print(end='\n')


def display_inventory(player):
    inventory = f"Level:{player['level']} HP:{player['HP']} Attack:{player['attack']} Armor:{player['armor']} Weapon:{player['weapon']} Capacity:{player['capacity']}"
    print(inventory)

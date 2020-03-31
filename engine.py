import ui
import random
import helpers
from datetime import time


def create_board(filename):
    '''
    Creates game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    with open(filename, 'r') as board_file:
        board = []
        for lines in board_file:
            elements = []
            for char in lines:
                if char == "\n":
                    break
                elements.append(char)
            board.append(elements)

    return board


def put_player_on_board(board, player):
    '''
    Puts the player icon on the board on player coordinates.

    Args:
    list: The game board
    dictionary: The player information - the icon and coordinates

    Returns:
    list: The game board with the player sign on it
    '''
    board[player['y']][player['x']] = player['icon']

    return board


def player_coordinates_change(movement, player, board):
    '''
    Changes player coordinates depending on user input

    Args:
    string: Key pressed by user
    dictionary: The player information - the icon and coordinates
    list: The game board

    Returns:
    dictionary: Updated player information
    '''
    x = player['x']
    y = player['y']

    if movement == "w" and board[y-1][x] != "#":
        y -= 1
    elif movement == "s" and board[y+1][x] != "#":
        y += 1
    elif movement == "a" and board[y][x-1] != "#":
        x -= 1
    elif movement == "d" and board[y][x+1] != "#":
        x += 1
    # else:
    #     pass

    player['x'] = x
    player['y'] = y

    return player


def put_enemies_on_board(board, enemy):
    '''
    Puts the enemy icon on the board on enemy coordinates.

    Args:
    list: The game board
    dictionary: The enemy information - the icon and coordinates

    Returns:
    list: The game board with the enemies signs on it
    '''
    board[enemy['y']][enemy['x']] = enemy['icon']

    return board


def enemy_movement(board, enemy):
    '''
    Moves enemy around board

    Args:
    list: The game board
    dictionary: The enemy information - the icon and coordinates

    Returns:
    dictionary: Updated player information
    '''

    x = enemy['x']
    y = enemy['y']

    if enemy['type'] == "x_axis":
        if board[y][x+1] == "#":
            enemy['direction'] = "left"
        elif board[y][x-1] == "#":
            enemy['direction'] = "right"
        if enemy['direction'] == "left":
            x -= 1
        elif enemy['direction'] == "right":
            x += 1
    enemy['x'] = x

    if enemy['type'] == "y_axis":
        if board[y-1][x] == "#":
            enemy['direction'] = "up"
        elif board[y+1][x] == "#":
            enemy['direction'] = "down"
        if enemy['direction'] == "down":
            y -= 1
        elif enemy['direction'] == "up":
            y += 1
    enemy['y'] = y

    return enemy


def put_items_on_board(board, item):
    board[item['y']][item['x']] = item['icon']

    return board


def enemy_board_interaction(board, enemy, player):
    '''
    Checking board interactions between two objects.

    Args:
    list: The game board.
    dictionary: The enemy information - HP, attack, coordinates.
    dictionary: The player information - HP, attack, items, coordinates.
    dictionary: The item information.

    Returns:
    list: List of objects after interaction.
    '''
    player_nearby_x = player['x']
    player_nearby_y = player['y']
    enemy_nearby_x = enemy['x']
    enemy_nearby_y = enemy['y']
    if enemy_nearby_x == player_nearby_x and enemy_nearby_y == player_nearby_y:
        return enemy_interaction(player, enemy)
    return [player, enemy]


def item_board_interaction(board, item, player):
    player_nearby_x = player['x']
    player_nearby_y = player['y']
    item_nearby_x = item['x']
    item_nearby_y = item['y']
    if item_nearby_x == player_nearby_x and item_nearby_y == player_nearby_y:
        player = item_interaction(player, item)
        item['on_board'] = 0
    return [player, item]


def item_interaction(player, item):
    if item['type'] == "clothes":
        player['clothes'] += 1
        player['armor'] = player['armor'] + item['armor']
        lift = player['capacity']
        lift_list = lift.split("/")
        new_weight = int(lift_list[0]) + item['weight']
        player['capacity'] = f"{new_weight}/100"
    elif item['type'] == "weapon":
        player['attack'] = item['damage']
        player['weapon'] = item['name']
        lift = player['capacity']
        lift_list = lift.split("/")
        new_weight = int(lift_list[0]) + item['weight']
        player['capacity'] = f"{new_weight}/100"
    elif item['type'] == "food":
        player['food'] += 1
        player['HP'] = player["HP"] + item["HP"]
        lift = player['capacity']
        lift_list = lift.split("/")
        new_weight = int(lift_list[0]) + item['weight']
        player['capacity'] = f"{new_weight}/100"
    return player


def put_gate(board, player):
    if player['food'] != 4:
        board[28][75] = "#"
    return board


def enemy_interaction(player, enemy):

    while player['HP'] > 0 and enemy['HP'] > 0:
        enemy["HP"] = enemy["HP"] - player["attack"]
        player["HP"] = player["HP"] - enemy["attack"]*((100 - player['armor'])/100)

    return [player, enemy]


def boss(player):
    while True:
        ui.display_board(create_board("messages/message_boss.txt"))
        time.sleep(3)
        key = helpers.key_pressed()
        if key == "s":
            amount_of_numbers = 4
            message = ['', 'HEY', '', 'I\'M GOING TO KILL YOU', '',
                       'YOU HAVE TO GUESS ALL {} NUMBERS'.format(amount_of_numbers), '', '']
            ui.print_boss(message)
            band_of_numbers = 64 // amount_of_numbers
            lives = int(player['HP']/10)
            guessed_numbers = []
            numbers_list = [random.randint(1, band_of_numbers) for number in range(amount_of_numbers)]
            guessed_numbers = main_game(numbers_list, band_of_numbers, lives, guessed_numbers)
            if numbers_list == guessed_numbers:
                player['level'] = 5
            if numbers_list != guessed_numbers:
                player['HP'] = 0
            return player

def main_game(numbers_list, band_of_numbers, lives, guessed_numbers):
    for index in range(len(numbers_list)):
        user_answer = None
        number_to_guess = numbers_list[index]
        guessed_numbers = prompt_user_to_guess(user_answer, number_to_guess, band_of_numbers,
                                               lives, guessed_numbers, numbers_list)
    return guessed_numbers


def prompt_user_to_guess(user_answer, number_to_guess, band_of_numbers, lives, guessed_numbers, numbers_list):
    while (number_to_guess != user_answer or user_answer is None) and lives > 0:
        lives -= 1
        user_answer = int(input("Enter an integer from 1 to {}: ".format(band_of_numbers)))
        guessed_numbers = get_result(user_answer, number_to_guess, guessed_numbers, lives, numbers_list)
    return guessed_numbers


def get_result(user_answer, number_to_guess, guessed_numbers, lives, numbers_list):
    if user_answer < number_to_guess:
        if lives > 0:
            amount_of_numbers_to_guess = len(numbers_list) - len(guessed_numbers)
            if lives > 1:
                message = [' ', 'YOUR ANSER IS TOO LOW!', ' ', 'YOU HAVE {} MORE TRIES'.format(lives), ' ',
                           'YOU HAVE {} NUMBERS LEFT TO GUESS'.format(amount_of_numbers_to_guess), ' ', ' ']
            else:
                message = [' ', 'YOUR ANSER IS TOO LOW!', ' ', 'YOU HAVE {} MORE TRY'.format(lives), ' ',
                           'YOU HAVE {} NUMBERS LEFT TO GUESS'.format(amount_of_numbers_to_guess), ' ', ' ']
            ui.print_boss(message)
        else:
            amount_of_numbers_to_guess = len(numbers_list) - len(guessed_numbers)
            message = [' ', 'YOUR ANSER IS TOO LOW!', ' ', 'YOU FAIL!',
                       'YOU HAVE {} NUMBERS LEFT TO GUESS'.format(amount_of_numbers_to_guess), ' ', ' ']
            ui.print_boss(message)
    elif user_answer > number_to_guess:
        if lives > 0:
            amount_of_numbers_to_guess = len(numbers_list) - len(guessed_numbers)
            if lives > 1:
                message = [' ', 'YOUR ANSER IS TOO HIGH!', ' ', 'YOU HAVE {} MORE TRIES'.format(lives), ' ',
                           'YOU HAVE {} NUMBERS LEFT TO GUESS'.format(amount_of_numbers_to_guess), ' ', ' ']
            else:
                message = [' ', 'YOUR ANSER IS TOO HIGH!', ' ', 'YOU HAVE {} MORE TRY'.format(lives), ' ',
                           'YOU HAVE {} NUMBERS LEFT TO GUESS'.format(amount_of_numbers_to_guess), ' ', ' ']
            ui.print_boss(message)
        else:
            amount_of_numbers_to_guess = len(numbers_list) - len(guessed_numbers)
            message = [' ', 'YOUR ANSER IS TOO HIGH!', ' ', 'YOU FAIL!',
                       'YOU HAVE {} NUMBERS LEFT TO GUESS'.format(amount_of_numbers_to_guess), ' ', ' ']
            ui.print_boss(message)
    else:
        guessed_numbers.append(number_to_guess)
        amount_of_numbers_to_guess = len(numbers_list) - len(guessed_numbers)
        message = [' ', ' ', 'YOU ARE RIGHT!', ' ', ' ',
                   'YOU HAVE {} NUMBERS LEFT TO GUESS'.format(amount_of_numbers_to_guess), ' ', ' ']
        ui.print_boss(message)
    return guessed_numbers

from helpers import *
import engine
import ui
import items
import enemies
import start_screen
import time

PLAYER_ICON = '\033[1;33;1m@\033[1;37;1m'
PLAYER_START_X = 1
PLAYER_START_Y = 1


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!ss

    Returns:
    dictionary
    '''
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON
    player["clothes"] = 0
    player["food"] = 0
    player["weapons"] = 0
    player['weapon'] = "None"
    player["attack"] = 0
    player["HP"] = 50
    player["armor"] = 0
    player["capacity"] = "0/100"
    player["level"] = 1
    return player


def level_one_start(player, enemies_list, file_name):

    # Creating objects and items

    item_one = items.create_apple(10, 1)
    item_two = items.create_banana(23, 6)
    item_three = items.create_knife(15, 14)
    item_four = items.create_shoes(63, 5)
    item_five = items.create_apple(35, 27)
    item_six = items.create_banana(77, 2)

    # Creating interactions

    objects_one = [player, item_one]
    objects_two = [player, item_two]
    objects_three = [player, item_three]
    objects_four = [player, item_four]
    objects_five = [player, item_five]
    objects_six = [player, item_six]

    is_running = True
    ui.display_board(engine.create_board("Messages/message_lvl1.txt"))
    time.sleep(1)

    while is_running:
        key = key_pressed()
        clear_screen()
        if key == 'q':
            assert False
        board = engine.create_board(file_name)
        lift = player['capacity']
        lift_list = lift.split("/")
        engine.put_gate(board, player)
        if int(lift_list[0]) < 100:
            player = engine.player_coordinates_change(key, player, board)
        board = engine.put_player_on_board(board, player)
        if player['x'] == 77 and player['y'] == 28:
            player['level'] = 2
            is_running = False
        for index in range(len(enemies_list)):
            enemy = enemies_list[index]
            if enemy['HP'] > 0:
                enemy = engine.enemy_movement(board, enemy)
                board = engine.put_enemies_on_board(board, enemy)
                fight = engine.enemy_board_interaction(board, enemy, player)
                player = fight[0]
                enemy = fight[1]
                enemies_list[index] = enemy
        if item_one['on_board'] == 1:
            board = engine.put_items_on_board(board, item_one)
            player = objects_one[0]
            item_one = objects_one[1]
            objects_one = engine.item_board_interaction(board, item_one, player)
        if item_two['on_board'] == 1:
            board = engine.put_items_on_board(board, item_two)
            player = objects_two[0]
            item_two = objects_two[1]
            objects_two = engine.item_board_interaction(board, item_two, player)
        if item_three['on_board'] == 1:
            board = engine.put_items_on_board(board, item_three)
            player = objects_three[0]
            item_three = objects_three[1]
            objects_three = engine.item_board_interaction(board, item_three, player)
        if item_four['on_board'] == 1:
            board = engine.put_items_on_board(board, item_four)
            player = objects_four[0]
            item_four = objects_four[1]
            objects_four = engine.item_board_interaction(board, item_four, player)
        if item_five['on_board'] == 1:
            board = engine.put_items_on_board(board, item_five)
            player = objects_five[0]
            item_five = objects_five[1]
            objects_five = engine.item_board_interaction(board, item_five, player)
        if item_six['on_board'] == 1:
            board = engine.put_items_on_board(board, item_six)
            player = objects_six[0]
            item_six = objects_six[1]
            objects_six = engine.item_board_interaction(board, item_six, player)
        if player['HP'] <= 0:
            print("Game over")
            return player
        engine.put_gate(board, player)
        ui.display_board(board)
        ui.display_inventory(player)

    return player


def level_two_start(player, enemies_list, file_name):

    # Creating objects and items

    item_one = items.create_apple(10, 1)
    item_two = items.create_grape(73, 6)
    item_three = items.create_axe(2, 28)
    item_four = items.create_jacket(38, 28)

    # Creating interactions

    objects_one = [player, item_one]
    objects_two = [player, item_two]
    objects_three = [player, item_three]
    objects_four = [player, item_four]

    is_running = True
    ui.display_board(engine.create_board("Messages/message_lvl2.txt"))
    time.sleep(3)

    while is_running:
        key = key_pressed()
        clear_screen()
        if key == 'q':
            assert False
        board = engine.create_board(file_name)
        player = engine.player_coordinates_change(key, player, board)
        board = engine.put_player_on_board(board, player)
        if player['x'] == 77 and player['y'] == 1:
            player['level'] = 3
            is_running = False
        for index in range(len(enemies_list)):
            enemy = enemies_list[index]
            if enemy['HP'] > 0:
                enemy = engine.enemy_movement(board, enemy)
                board = engine.put_enemies_on_board(board, enemy)
                fight = engine.enemy_board_interaction(board, enemy, player)
                player = fight[0]
                enemy = fight[1]
                enemies_list[index] = enemy
        if item_one['on_board'] == 1:
            board = engine.put_items_on_board(board, item_one)
            player = objects_one[0]
            item_one = objects_one[1]
            objects_one = engine.item_board_interaction(board, item_one, player)
        if item_two['on_board'] == 1:
            board = engine.put_items_on_board(board, item_two)
            player = objects_two[0]
            item_two = objects_two[1]
            objects_two = engine.item_board_interaction(board, item_two, player)
        if item_three['on_board'] == 1:
            board = engine.put_items_on_board(board, item_three)
            player = objects_three[0]
            item_three = objects_three[1]
            objects_three = engine.item_board_interaction(board, item_three, player)
        if item_four['on_board'] == 1:
            board = engine.put_items_on_board(board, item_four)
            player = objects_four[0]
            item_four = objects_four[1]
            objects_four = engine.item_board_interaction(board, item_four, player)
        if player['HP'] <= 0:
            print("Game over")
            return player
        ui.display_board(board)
        ui.display_inventory(player)

    return player


def level_three_start(player, enemies_list, file_name):

    # Creating objects and items

    item_one = items.create_banana(1, 14)
    item_two = items.create_grape(73, 6)
    item_three = items.create_sword(9, 14)

    # Creating interactions

    objects_one = [player, item_one]
    objects_two = [player, item_two]
    objects_three = [player, item_three]

    is_running = True
    ui.display_board(engine.create_board("Messages/message_lvl3.txt"))
    time.sleep(3)

    while is_running:
        key = key_pressed()
        clear_screen()
        if key == 'q':
            assert False
        board = engine.create_board(file_name)
        player = engine.player_coordinates_change(key, player, board)
        board = engine.put_player_on_board(board, player)
        if player['x'] == 77 and player['y'] == 14:
            player['level'] = 4
            is_running = False
        for index in range(len(enemies_list)):
            enemy = enemies_list[index]
            if enemy['HP'] > 0:
                enemy = engine.enemy_movement(board, enemy)
                board = engine.put_enemies_on_board(board, enemy)
                fight = engine.enemy_board_interaction(board, enemy, player)
                player = fight[0]
                enemy = fight[1]
                enemies_list[index] = enemy
        if item_one['on_board'] == 1:
            board = engine.put_items_on_board(board, item_one)
            player = objects_one[0]
            item_one = objects_one[1]
            objects_one = engine.item_board_interaction(board, item_one, player)
        if item_two['on_board'] == 1:
            board = engine.put_items_on_board(board, item_two)
            player = objects_two[0]
            item_two = objects_two[1]
            objects_two = engine.item_board_interaction(board, item_two, player)
        if item_three['on_board'] == 1:
            board = engine.put_items_on_board(board, item_three)
            player = objects_three[0]
            item_three = objects_three[1]
            objects_three = engine.item_board_interaction(board, item_three, player)
        if player['HP'] <= 0:
            return player
        ui.display_board(board)
        ui.display_inventory(player)

    return player

def restart(player, hp)
    if key == "n":
        return player
    if key == "y":
        player["HP"] = hp

def main():
    global player
    player = create_player()
    while player['level'] == 1 and player['HP'] > 0:
        try:
            file_name = 'Levels/lvl1.txt'
            enemies_list = enemies.create_enemies_list(file_name)
            player = level_one_start(player, enemies_list, file_name)
        except AssertionError:
            break
        if player["HP"] <= 0:
            clear_screen()
            ui.display_board(engine.create_board("Messages/restart.txt"))
            key = key_pressed()
            if key == "n":
                return player
            if key == "y":
                player["HP"] = 50
        player['x'] = 1
        player['y'] = 1
    while player['level'] == 2 and player["HP"] > 0:
        try:
            file_name = 'Levels/lvl2.txt'
            enemies_list = enemies.create_enemies_list(file_name)
            player = level_two_start(player, enemies_list, file_name)
        except AssertionError:
            break
        if player["HP"] <= 0:
            clear_screen()
            ui.display_board(engine.create_board("Messages/restart.txt"))
            if key == "n":
                return player
            if key == "y":
                player["HP"] = 50
        player['x'] = 1
        player['y'] = 1
    while player['level'] == 3 and player['HP'] > 0:
        try:
            file_name = 'Levels/lvl3.txt'
            enemies_list = enemies.create_enemies_list(file_name)
            player = level_three_start(player, enemies_list, file_name)
        except AssertionError:
            break
        if player["HP"] <= 0:
            clear_screen()
            ui.display_board(engine.create_board("Messages/restart.txt"))
            key = key_pressed()
            if key == "n":
                return player
            if key == "y":
                player["HP"] = 50
        player['x'] = 1
        player['y'] = 1
    while player['level'] == 4 and player['HP'] > 0:
        clear_screen()
        player = engine.boss(player)
        if player['HP'] == 0:
            clear_screen()
            ui.display_board(engine.create_board("Messages/restart.txt"))
            key = key_pressed()
            if key == "n":
                return player
            if key == "y":
                player['HP'] = 100
    return player


if __name__ == '__main__':
    while True:
        clear_screen()
        start_screen.main()
        clear_screen()
        player = main()
        clear_screen()
        t_end = time.time() + 5
        if player['level'] == 5:
            ui.display_board(engine.create_board("Messages/win.txt"))
            time.sleep(5)
        if player['level'] != 5:
            ui.display_board(engine.create_board("Messages/lose.txt"))
            time.sleep(5)

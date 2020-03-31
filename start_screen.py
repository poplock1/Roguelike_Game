import helpers
import sys


def main():
    file_name = 'Messages/start_screen.txt'
    START_INDEX = 8
    INSTRUCTION_INDEX = 10
    AUTHORS_INDEX = 12
    EXIT_INDEX = 14
    screen = make_start_board(START_INDEX, file_name)
    while True:
        helpers.clear_screen()
        print_screen(screen)
        key = helpers.key_pressed()
        if key == 'n':
            change_option_to_next(screen, file_name)
            helpers.clear_screen()
            print_screen(screen)
        if key == 'p':
            change_option_to_previous(screen, file_name)
            helpers.clear_screen()
            print_screen(screen)
        if key == 'e':
            chosen_option_index = check_option_true(screen, file_name)
            if chosen_option_index == START_INDEX:
                return
            else:
                make_chosen_option(chosen_option_index, INSTRUCTION_INDEX, AUTHORS_INDEX, EXIT_INDEX)


def make_chosen_option(chosen_option_index, INSTRUCTION_INDEX, AUTHORS_INDEX, EXIT_INDEX):
    if chosen_option_index == INSTRUCTION_INDEX:
        file_to_print = 'messages/instruction.txt'
        screen = make_board(file_to_print)
        helpers.clear_screen()
        print_screen(screen)
        while True:
            key = helpers.key_pressed()
            if key == 'q':
                break
    elif chosen_option_index == AUTHORS_INDEX:
        file_to_print = 'messages/authors.txt'
        screen = make_board(file_to_print)
        helpers.clear_screen()
        print_screen(screen)
        while True:
            key = helpers.key_pressed()
            if key == 'q':
                break
    elif chosen_option_index == EXIT_INDEX:
        sys.exit()


def change_option_to_next(screen, file_name):
    LAST_OPTION_INDEX = 14
    true_option_index = check_option_true(screen, file_name)
    next_option_index = true_option_index + 2
    if true_option_index < LAST_OPTION_INDEX:
        screen = make_option_false(screen, true_option_index, file_name)
        screen = make_option_true(screen, next_option_index)
    return screen


def change_option_to_previous(screen, file_name):
    FIRST_OPTION_INDEX = 8
    true_option_index = check_option_true(screen, file_name)
    previous_option_index = true_option_index - 2
    if true_option_index > FIRST_OPTION_INDEX:
        screen = make_option_false(screen, true_option_index, file_name)
        screen = make_option_true(screen, previous_option_index)


def make_board(file_name):
    with open(file_name, 'r') as rfile:
        board = rfile.readlines()
    return board


def make_start_board(FIRST_OPTION_INDEX, file_name):
    screen = make_board(file_name)
    screen = make_option_true(screen, FIRST_OPTION_INDEX)
    return screen


def make_option_true(board, index):
    OPTION_INDEX = 1
    line_to_change = board[index]
    line_list = line_to_change.split(' ')
    option = line_list[OPTION_INDEX]
    option = '\033[1;32;1m' + option + '\033[1;37;1m'
    line_list[OPTION_INDEX] = option
    board[index] = ' '.join(line_list)
    return board


def make_option_false(board, index, file_name):
    normal_lines = make_board(file_name)
    board[index] = normal_lines[index]
    return board


def check_option_true(board, file_name):
    normal_board = make_board(file_name)
    for index in range(len(board)):
        if not board[index] == normal_board[index]:
            return index


def print_screen(screen):
    for index in range(len(screen)):
        print(screen[index], end='')
    print(end='\n')


def instruction():
    with open('instruction.txt', 'r') as instruction:
        instruction = instruction.readlines()
    helpers.clear_screen()
    print_screen(instruction)
    while True:
        key = helpers.key_pressed()
        if key == 'q':
            break


if __name__ == '__main__':
    main()

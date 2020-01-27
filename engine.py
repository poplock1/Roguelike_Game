def create_board(width, height):

    # list of lists containing board floor
    board = [["." for number in range(width - 2)] for number in range(height)]

    # board frame
    for element in board:  # board frame - sides
        element.insert(0, "#")
        element.append("#")

    board.insert(0, "#" * width)  # board frame - tob and bottom
    board.append("#" * width)
    '''
    Creates game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    return board


def put_player_on_board(board, player):

    # player's movement
    coordinates = coordinates_change(x, y)

    x = coordinates[0]
    y = coordinates[1]
    board[y][x] = player

    print_board(board)

    '''
    Puts the player icon on the board on player coordinates.

    Args:
    list: The game board
    dictionary: The player information - the icon and coordinates

    Returns:
    list: The game board with the player sign on it
    '''
    pass

# controllers definition
def coordinates_change(x, y):
    movement = getch()

    if movement == "w" and y > 1:
        y -= 1

    elif movement == "s" and y < 16:
        y += 1

    elif movement == "a" and x > 1:
        x -= 1

    elif movement == "d" and x < 64:
        x += 1

    else:
        pass

    return [x, y]
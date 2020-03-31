
def create_apple(x_position, y_position):
    item = {}
    item['x'] = x_position
    item['y'] = y_position
    item['icon'] = "\033[1;32;1mA\033[1;37;1m"
    item['type'] = 'food'
    item['HP'] = 5
    item['on_board'] = 1
    item['weight'] = 5
    return item


def create_banana(x_position, y_position):
    item = {}
    item['x'] = x_position
    item['y'] = y_position
    item['icon'] = "\033[1;32;1mB\033[1;37;1m"
    item['type'] = 'food'
    item['HP'] = 10
    item['on_board'] = 1
    item['weight'] = 5
    return item


def create_grape(x_position, y_position):
    item = {}
    item['x'] = x_position
    item['y'] = y_position
    item['icon'] = "\033[1;32;1mG\033[1;37;1m"
    item['type'] = 'food'
    item['HP'] = 15
    item['on_board'] = 1
    item['weight'] = 5
    return item


def create_shoes(x_position, y_position):
    item = {}
    item['x'] = x_position
    item['y'] = y_position
    item['icon'] = "\033[1;32;1mS\033[1;37;1m"
    item['type'] = 'clothes'
    item['armor'] = 25
    item['on_board'] = 1
    item['weight'] = 10
    return item


def create_jacket(x_position, y_position):
    item = {}
    item['x'] = x_position
    item['y'] = y_position
    item['icon'] = "\033[1;32;1mJ\033[1;37;1m"
    item['type'] = 'clothes'
    item['armor'] = 50
    item['on_board'] = 1
    item['weight'] = 25
    return item


def create_knife(x_position, y_position):
    item = {}
    item['x'] = x_position
    item['y'] = y_position
    item['icon'] = "\033[1;32;1mK\033[1;37;1m"
    item['type'] = 'weapon'
    item['name'] = "Knife"
    item['damage'] = 10
    item['on_board'] = 1
    item['weight'] = 10
    return item


def create_axe(x_position, y_position):
    item = {}
    item['x'] = x_position
    item['y'] = y_position
    item['icon'] = "\033[1;32;1mX\033[1;37;1m"
    item['type'] = 'weapon'
    item['name'] = "Axe"
    item['damage'] = 20
    item['on_board'] = 1
    item['weight'] = 20
    return item


def create_sword(x_position, y_position):
    item = {}
    item['x'] = x_position
    item['y'] = y_position
    item['icon'] = "\033[1;32;1mS\033[1;37;1m"
    item['type'] = 'weapon'
    item['name'] = "Sword"
    item['damage'] = 40
    item['on_board'] = 1
    item['weight'] = 25
    return item

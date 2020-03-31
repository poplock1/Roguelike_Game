def create_enemies_list(file_name):
    if file_name == 'Levels/lvl1.txt':
        X_INDEX = 0
        Y_INDEX = 1
        enemy_x_axis_coordinates = [(18, 10)]
        enemy_y_axis_coordinates = [(24, 2), (32, 7), (66, 26), (60, 5), (66, 7)]
        x_enemies = [create_x_enemy(element[X_INDEX], element[Y_INDEX]) for element in enemy_x_axis_coordinates]
        y_enemies = [create_y_enemy(element[X_INDEX], element[Y_INDEX]) for element in enemy_y_axis_coordinates]
        enemies_list = x_enemies + y_enemies
    elif file_name == 'Levels/lvl2.txt':
        X_INDEX = 0
        Y_INDEX = 1
        enemy_x_axis_coordinates = [(6, 8), (13, 19), (37, 22), (77, 17)]
        enemy_y_axis_coordinates = [(24, 28), (32, 7)]
        x_enemies = [create_x_enemy(element[X_INDEX], element[Y_INDEX]) for element in enemy_x_axis_coordinates]
        y_enemies = [create_y_enemy(element[X_INDEX], element[Y_INDEX]) for element in enemy_y_axis_coordinates]
        enemies_list = x_enemies + y_enemies
    elif file_name == 'Levels/lvl3.txt':
        X_INDEX = 0
        Y_INDEX = 1
        enemy_x_axis_coordinates = [(74, 6), (76, 10), (74, 25), (76, 21)]
        enemy_y_axis_coordinates = [(14, 13), (24, 12), (34, 10), (44, 8), (54, 6), (16, 26), (26, 24), (36, 22), (46, 20), (56, 18)]
        x_enemies = [create_x_enemy(element[X_INDEX], element[Y_INDEX]) for element in enemy_x_axis_coordinates]
        y_enemies = [create_y_enemy(element[X_INDEX], element[Y_INDEX]) for element in enemy_y_axis_coordinates]
        enemies_list = x_enemies + y_enemies
    return enemies_list


def create_x_enemy(x_position, y_position):
    enemy = {}
    enemy['x'] = x_position
    enemy['y'] = y_position
    enemy['icon'] = "\033[1;31;1m%\033[1;37;1m"
    enemy['type'] = "x_axis"
    enemy['direction'] = "right"
    enemy['attack'] = 10
    enemy['HP'] = 20
    return enemy


def create_y_enemy(x_position, y_position):
    enemy = {}
    enemy['x'] = x_position
    enemy['y'] = y_position
    enemy['icon'] = "\033[1;31;1m%\033[1;37;1m"
    enemy['type'] = "y_axis"
    enemy['direction'] = "up"
    enemy['attack'] = 10
    enemy['HP'] = 20
    return enemy

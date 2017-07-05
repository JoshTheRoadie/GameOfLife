# Game of Life Program

import random
import copy


def main():
    generations = 10
    cells = parse_gol_seed_txt('gol_seed1.txt')  # initialize matrix
    width = len(cells)
    height = len(cells[0])
    print_cell_grid(cells, width, height)  # print initial matrix state

    while generations > 0:
        cells = iter_generation(cells)
        print_cell_grid(cells, width, height)
        generations -= 1


def parse_gol_seed_txt(filename):
    with open(filename) as f:
        data = f.readlines()

    data_grid = []
    for y in range(len(data[0]) - 1):
        column = []
        for line in data:
            column.append(int(line[y]))

        data_grid.append(column)

    return data_grid


def make_cell_grid(width, height):
    """Makes a grid of width * height size with random 1s and 0s."""
    cell_grid = []
    for x in range(width):
        column = []
        for y in range(height):
            column.append(random.randint(0, 1))
        cell_grid.append(column)
    return cell_grid


def is_valid_position(cells, pos):
    """ Checks to see if the (x, y) position passed is in the bounds of the
    matrix."""
    x, y = pos
    if x < 0 or x >= len(cells):  # x is not in bounds
        return False
    elif y < 0 or y >= len(cells[0]):  # y is not in bounds
        return False
    else:
        return True  # pos is in bounds


def life_or_death(cells, pos):
    """ This function determines if a cell at the given pos lives or dies
    based on the rules given for the Game of Life. The return value is either
    a 1 or a 0 depending on the logic."""
    start_x, start_y = pos
    current_cell = cells[start_x][start_y]
    neighbors = 0

    for x_adjust in range(-1, 2):
        check_x = start_x + x_adjust
        for y_adjust in range(-1, 2):
            check_y = start_y + y_adjust

            if is_valid_position(cells, (check_x, check_y)):
                if (check_x, check_y) == (start_x, start_y):
                    continue
                elif cells[check_x][check_y] == 1:
                    neighbors += 1

    if current_cell == 0 and neighbors == 3:  # checks 'born' conditions
        return 1
    if current_cell == 1:
        if neighbors <= 1 or neighbors >= 4:  # checks 'died' conditions
            return 0

    return current_cell  # if not 'born' or 'died', do nothing


def iter_generation(cells):
    """ This function steps through each position in the cell matrix and checks
    the 'born', 'died', 'unchanged' status of each cell.  It then maps the new
    values to a new matrix that is returned in the end."""

    new_gen = copy.deepcopy(cells)

    for x in range(len(cells)):
        for y in range(len(cells[0])):
            new_cell = life_or_death(cells, (x, y))
            new_gen[x][y] = new_cell
    return new_gen


def print_cell_grid(cells, width, height):
    """ Prints the grid in the proper x,y orientation on the screen."""
    for y in range(height):
        print
        for x in range(width):
            print cells[x][y],
    print


if __name__ == '__main__':
    main()

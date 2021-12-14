
class Octopus:
    def __init__(self, pos_x, pos_y, value):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.value = value
        self.neighbours = list()
        self.already_flashed = False

    def __str__(self):
        return f"pos:({self.pos_x},{self.pos_y}) value={self.value}, neighbours:{self.neighbours}"


def set_neighbours(input_list_data):
    size_x = len(input_list_data)
    size_y = len(input_list_data[0])
    for xx in range(size_x):
        for yy in range(size_y):
            for x2 in range(xx - 1, xx + 2):
                for y2 in range(yy - 1, yy + 2):
                    if -1 < xx < size_x and -1 < yy < size_y and (xx != x2 or yy != y2) and (0 <= x2 < size_x) and (
                            0 <= y2 < size_y):
                        input_list_data[xx][yy].neighbours.append(input_list_data[x2][y2])
    return input_list_data


def load_input(file_name):
    with open(file_name, mode="r") as input_f:
        points_list = list()
        line_counter = 0
        for line in input_f:
            line = line.strip()
            tmp_list = list()
            signs_counter = 0
            for char in line:
                tmp_list.append(Octopus(line_counter, signs_counter, int(char)))
                signs_counter += 1
            line_counter += 1
            points_list.append(tmp_list)
    return points_list


def simulate_flashes(input_list_data, num_of_simulation):
    number_of_flashes = 0
    print(f"Before simulation:")
    print_board(input_list_data)
    print("\n")
    for i in range(num_of_simulation):
        number_of_flashes += increase_octopuses_power(input_list_data)
        input_list_data = check_flashes(input_list_data)
        print(f"Simulation {i}:")
        print_board(input_list_data)
        print("\n")

    for x in range(len(input_list_data)):
        for y in range(len(input_list_data[0])):
            if input_list_data[x][y].already_flashed:
                number_of_flashes += 1
                input_list_data[x][y].already_flashed = False
                input_list_data[x][y].value = 0
    return input_list_data, number_of_flashes


def simulate_flashes_until_all_synchronized(input_list_data):
    print(f"Before simulation:")
    print_board(input_list_data)
    print("\n")
    simulation_number = 0
    while True:
        simulation_number += 1
        increase_octopuses_power(input_list_data)
        input_list_data = check_flashes(input_list_data)
        print(f"Simulation {simulation_number}:")
        print_board(input_list_data)
        print("\n")
        if check_conditions(input_list_data):
            break

    for x in range(len(input_list_data)):
        for y in range(len(input_list_data[0])):
            if input_list_data[x][y].already_flashed:
                input_list_data[x][y].already_flashed = False
                input_list_data[x][y].value = 0
    return input_list_data, simulation_number


def print_board(input_list_data):
    for octopuses in input_list_data:
        line = ""
        for octopus in octopuses:
            line += str(octopus.value)
            line += " "
        print(f"{line}")


def check_conditions(input_list_data):
    for octopuses in input_list_data:
        for octopus in octopuses:
            if not octopus.already_flashed:
                return False
    return True


def increase_octopuses_power(input_list_data):
    number_of_flashes = 0
    for x in range(len(input_list_data)):
        for y in range(len(input_list_data[0])):
            if input_list_data[x][y].already_flashed:
                number_of_flashes += 1
                input_list_data[x][y].already_flashed = False
                input_list_data[x][y].value = 0
            # input_list_data[x][y].already_flashed = False
            input_list_data[x][y].value += 1
    return number_of_flashes


def check_flashes(input_list_data):
    for x in range(len(input_list_data)):
        for y in range(len(input_list_data[0])):
            if input_list_data[x][y].value > 9:
                octopus_flash(input_list_data[x][y])
    return input_list_data


def octopus_flash(octopus):
    if not octopus.already_flashed:
        octopus.already_flashed = True
        octopus.value = 0
        for neighbour in octopus.neighbours:
            neighbour.value += 1
            if neighbour.value > 9:
                octopus_flash(neighbour)


if __name__ == '__main__':
    # #  part1
    # input_list = load_input("input_day11")
    # # input_list = load_input("input_day11_small")
    # # input_list = load_input("input_day11_simple")
    # results = set_neighbours(input_list)
    # final_result, num_of_flashes = simulate_flashes(results, 100)
    # print_board(final_result)
    # print(num_of_flashes)
    # print()

    # part2
    input_list = load_input("input_day11")
    results = set_neighbours(input_list)
    final_result, simulation_number = simulate_flashes_until_all_synchronized(results)
    print_board(final_result)
    print(simulation_number)
    print()

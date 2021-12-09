class Point:
    def __init__(self, pos_x, pos_y, value):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.value = value
        self.neighbours = list()

    def __str__(self):
        return f"pos:({self.pos_x},{self.pos_y}) value={self.value}, neighbours:{self.neighbours}"


def set_neighbours(input_list):
    size_x = len(input_list)
    size_y = len(input_list[0])
    for xx in range(size_x):
        for yy in range(size_y):
            for x2 in range(xx - 1, xx + 2):
                for y2 in range(yy - 1, yy + 2):
                    if -1 < xx < size_x and -1 < yy < size_y \
                            and ((xx == x2 and yy != y2) or (xx != x2 and yy == y2)) \
                            and (0 <= x2 < size_x) and (0 <= y2 < size_y):
                        input_list[xx][yy].neighbours.append(input_list[x2][y2])
            # for x2 in range(xx - 1, xx + 2):
            #     for y2 in range(yy - 1, yy + 2):
            #         if -1 < xx < size_x and -1 < yy < size_y and (xx != x2 or yy != y2) and (0 <= x2 < size_x) and (0 <= y2 < size_y):
            #             input_list[xx][yy].neighbours.append(input_list[x2][y2])
    return input_list


def find_low_points_for_part1(input_list):
    result_list = list()
    for point_list in input_list:
        for point in point_list:
            is_lowest = True
            for neighbour in point.neighbours:
                if point.value >= neighbour.value:
                    is_lowest = False
                    break
            if is_lowest:
                result_list.append(point.value)
    return result_list


def find_low_points(input_list):
    result_list = list()
    for point_list in input_list:
        for point in point_list:
            is_lowest = True
            for neighbour in point.neighbours:
                if point.value >= neighbour.value:
                    is_lowest = False
                    break
            if is_lowest:
                result_list.append(point)
    return result_list


def load_input(file_name):
    with open(file_name, mode="r") as input_f:
        points_list = list()
        line_counter = 0
        for line in input_f:
            line = line.strip()
            tmp_list = list()
            signs_counter = 0
            for char in line:
                tmp_list.append(Point(line_counter, signs_counter, int(char)))
                signs_counter += 1
            line_counter += 1
            points_list.append(tmp_list)
    return points_list


def count_basins(lowest_points_list):
    basins_size_list = list()
    for lowest_point in lowest_points_list:
        dict_of_visited_points = dict()
        basin_size = 1
        dict_of_visited_points[(lowest_point.pos_x, lowest_point.pos_y)] = lowest_point
        basin_size += count_basins_for_neighbours(dict_of_visited_points, lowest_point.neighbours)
        basins_size_list.append(basin_size)
    return basins_size_list


def count_basins_for_neighbours(dict_of_visited_points, neighbour_list):
    basin_size = 0
    for neighbour in neighbour_list:
        pos_tuple = (neighbour.pos_x, neighbour.pos_y)
        if pos_tuple in dict_of_visited_points:
            continue
        else:
            dict_of_visited_points[(neighbour.pos_x, neighbour.pos_y)] = neighbour
        if neighbour.value < 9:
            basin_size += 1
            basin_size += count_basins_for_neighbours(dict_of_visited_points, neighbour.neighbours)
    return basin_size


if __name__ == '__main__':
    input_data = load_input("input_day09")
    # input_data = load_input("input_day09_small")
    # size_x = len(input_data)
    # size_y = len(input_data[0])
    input_data = set_neighbours(input_data)
    # result = find_low_points_for_part1(input_data)
    results = find_low_points(input_data)
    basins_result = count_basins(results)
    print(basins_result)

    three_largest_values = sorted(basins_result, reverse=True)[:3]
    print(three_largest_values[0] * three_largest_values[1] * three_largest_values[2])

    # for point in results:
    #     print(point)

    # final_result = 0
    # for val in results:
    #     final_result += 1 + val
    # print(final_result)


class Board:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.board = [[0 for x in range(size_x)] for y in range(size_y)]
        self.sum = 0

    def __str__(self):
        result_str = str("BOARD:\n")
        for x in range(self.size_x):
            for y in range(self.size_y):
                result_str += str(self.board[y][x])
                result_str += " "
            result_str = result_str[:-1]
            result_str += '\n'
        return result_str

    def fill_vertical(self, origin, length):
        for i in range(length + 1):
            self.board[origin.x][origin.y + i] += 1
            if self.board[origin.x][origin.y + i] == 2:
                self.sum += 1

    def fill_horizontal(self, origin, length):
        for i in range(length + 1):
            self.board[origin.x + i][origin.y] += 1
            if self.board[origin.x + i][origin.y] == 2:
                self.sum += 1


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"


def load_input(file_name):
    coordinates_dict = dict()
    max_x = 0
    max_y = 0
    with open(file_name, mode="r") as input_f:
        for line in input_f:
            coordinates = line.strip().replace("->", ",").split(",")
            x1 = int(coordinates[0])
            y1 = int(coordinates[1])
            x2 = int(coordinates[2])
            y2 = int(coordinates[3])
            max_x = max(max_x, x1, x2)
            max_y = max(max_y, y1, y2)
            coordinates_dict[Coordinates(x1, y1)] = Coordinates(x2, y2)
    return coordinates_dict, max(max_x, max_y)


def fill_board(board_instance, coordinates_dict):
    for origin, end in coordinates_dict.items():
        if origin.x == end.x:
            diff = end.y - origin.y
            absolute_diff = abs(diff)
            if diff > 0:
                board_instance.fill_vertical(origin, absolute_diff)
            else:
                board_instance.fill_vertical(end, absolute_diff)
        elif origin.y == end.y:
            diff = end.x - origin.x
            absolute_diff = abs(diff)
            if diff > 0:
                board_instance.fill_horizontal(origin, absolute_diff)
            else:
                board_instance.fill_horizontal(end, absolute_diff)


if __name__ == '__main__':
    origins_and_ends, max_size = load_input("input_day05")
    board = Board(max_size + 1, max_size + 1)
    fill_board(board, origins_and_ends)
    print(board.sum)


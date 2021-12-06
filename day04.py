class BoardField:
    def __init__(self, input_value):
        self.value = input_value
        self.is_marked = False


class Board:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.board = [[BoardField(0) for x in range(size_x)] for y in range(size_y)]
        self.sum = 0
        self.bingo = False

    def set_values(self, list_of_values, row):
        for y in range(self.size_y):
            current_value = int(list_of_values[y])
            self.board[row][y].value = current_value
            self.sum += current_value

    def check_bingo_in_column(self, x):
        for y in range(self.size_y):
            if not self.board[x][y].is_marked:
                return False
        return True

    def check_bingo_in_row(self, y):
        for x in range(self.size_x):
            if not self.board[x][y].is_marked:
                return False
        return True

    def check_bingo(self):
        for x in range(self.size_x):
            if check_bingo_in_column(x):
                return True
        for y in range(self.size_y):
            if check_bingo_in_row(y):
                return True
        return False

    def marked_number_and_check_bingo(self, number):
        number = int(number)
        for x in range(self.size_x):
            for y in range(self.size_y):
                if self.board[x][y].value == number:
                    self.board[x][y].is_marked = True
                    self.sum -= number
                    if self.check_bingo_in_column(x) or self.check_bingo_in_row(y):
                        self.bingo = True
                        return True
        return False

    def __str__(self):
        result_str = str("BOARD:\n")
        for x in range(self.size_x):
            for y in range(self.size_y):
                result_str += str(self.board[x][y].value)
                result_str += " "
            result_str = result_str[:-1]
            result_str += '\n'
        return result_str


def load_data(file_name):
    with open(file_name, mode="r") as input_f:
        list_of_boards = list()
        first_line = input_f.readline()
        first_line = first_line.strip().split(',')
        current_board = -1
        current_row = 0
        for line in input_f:
            line = line.replace("  ", " ")
            line = line.strip()
            if len(line) > 0:
                line = line.split(' ')
                list_of_boards[current_board].set_values(line, current_row)
                current_row += 1
            else:
                if len(list_of_boards) > 0:
                    print(list_of_boards[current_board])
                list_of_boards.append(Board(5, 5))
                current_board += 1
                current_row = 0
    return list_of_boards, first_line


def play_bingo(list_of_boards, numbers):
    for number in numbers:
        number = int(number)
        for board in list_of_boards:
            if board.marked_number_and_check_bingo(number):
                return number * board.sum


def lose_bingo(list_of_boards, numbers):
    for number in numbers:
        number = int(number)
        filtered_list_of_boards = [board for board in list_of_boards if board.bingo is False]
        for board in filtered_list_of_boards:
            if board.marked_number_and_check_bingo(number):
                if len(filtered_list_of_boards) == 1:
                    return number * board.sum


if __name__ == '__main__':
    boards, bingo_numbers = load_data("input_day04")
    # result = play_bingo(boards, bingo_numbers)
    # print(result)
    # print()
    result = lose_bingo(boards, bingo_numbers)
    print(result)

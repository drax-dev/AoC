
class Submarine:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0

    def change_depth(self, depth):
        self.depth += depth

    def change_horizontal_position(self, horizontal_position):
        self.horizontal_position += horizontal_position


def read_input_and_move_submarine(file_name, submarine):
    with open(file_name, mode="r") as input_f:
        for line in input_f:
            split_result = line.split()
            command = split_result[0]
            value = int(split_result[1])
            print(f"move {command} {value} units")
            if command == "forward":
                submarine.change_horizontal_position(value)
            elif command == "down":
                submarine.change_depth(value)
            else:
                submarine.change_depth(-value)

            print(f"d:{submarine.depth} h:{submarine.horizontal_position}")


def read_input_and_move_advanced_submarine(file_name, submarine):
    with open(file_name, mode="r") as input_f:
        for line in input_f:
            split_result = line.split()
            command = split_result[0]
            value = int(split_result[1])
            print(f"move {command} {value} units")
            if command == "forward":
                submarine.change_horizontal_position(value)
            elif command == "down":
                submarine.change_aim(value)
            else:
                submarine.change_aim(-value)

            print(f"d:{submarine.depth} h:{submarine.horizontal_position} a:{submarine.aim}")


class AdvancedSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def change_aim(self, aim):
        self.aim += aim

    def change_horizontal_position(self, horizontal_position):
        super().change_horizontal_position(horizontal_position)
        super().change_depth(horizontal_position * self.aim)


if __name__ == '__main__':
    submarine_instance = Submarine()
    read_input_and_move_submarine("input_day02", submarine_instance)
    result = submarine_instance.depth * submarine_instance.horizontal_position
    print()
    print(result)

    submarine_instance2 = AdvancedSubmarine()
    read_input_and_move_advanced_submarine("input_day02", submarine_instance2)
    result = submarine_instance2.depth * submarine_instance2.horizontal_position
    print()
    print(result)

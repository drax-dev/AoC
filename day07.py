import sys


def load_input(file_name):
    with open(file_name, mode="r") as input_f:
        file_content = input_f.read()
        list_of_initial_state = file_content.strip().split(',')
        list_of_initial_state = list(map(int, list_of_initial_state))
    return list_of_initial_state


def align_positions(input_positions):
    max_value = 0
    min_value = sys.maxsize
    for pos in input_positions:
        if pos > max_value:
            max_value = pos
        if pos < min_value:
            min_value = pos
    print(f"max {max_value}")
    print(f"min {min_value}")
    mid_result = int(max_value/2)
    min_result = sys.maxsize
    for i in range(min_value, max_value):
        if i == mid_result:
            mid_result = check_fuel(input_positions, i)
            min_result = min(min_result, mid_result)
            break
        beginning_result = check_fuel(input_positions, i)
        end_result = check_fuel(input_positions, i)
        min_result = min(beginning_result, end_result, min_result)
    print(min_result)


def check_fuel(input_positions, initial_value):
    result = 0
    for pos in input_positions:
        abs_value = abs(initial_value - pos)
        result += sum(range(1, abs_value + 1))
    return result


if __name__ == '__main__':
    # crab_positions = load_input("input_day07_small")
    crab_positions = load_input("input_day07")
    align_positions(crab_positions)

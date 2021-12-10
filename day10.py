
open_char_set = {'(', '[', '{', '<'}

close_open_dict = {')': '(', ']': '[', '}': '{', '>': '<'}

error_score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}


def load_input(file_name):
    with open(file_name, mode="r") as input_f:
        input_data_list = list()
        for line in input_f:
            input_data_list.append(line.strip())
        return input_data_list


def parse_input(input_data):
    parse_error = list()
    for line in input_data:
        stack = list()
        for char in line:
            if char in open_char_set:
                stack.append(char)
            else:
                if close_open_dict[char] == stack[-1]:
                    stack = stack[:-1]
                else:
                    parse_error.append(char)
                    break
    return parse_error


if __name__ == '__main__':
    # input_list = load_input("input_day10_small")
    input_list = load_input("input_day10")
    results = parse_input(input_list)

    final_results = 0
    for result in results:
        final_results += error_score_dict[result]
    print(final_results)

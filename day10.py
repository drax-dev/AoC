
open_char_set = {'(', '[', '{', '<'}

close_open_dict = {')': '(', ']': '[', '}': '{', '>': '<'}

open_close_dict = {'(': ')', '[': ']', '{': '}', '<': '>'}

error_score_dict = {')': 3, ']': 57, '}': 1197, '>': 25137}

autocomplete_score_dict = {')': 1, ']': 2, '}': 3, '>': 4}


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


def autocomplete_input(input_data):
    autocomplete_output = list()
    line_counter = 0
    for line in input_data:
        autocomplete_output.append(list())
        stack = list()
        incorrect_line = False
        for char in line:
            if char in open_char_set:
                stack.append(char)
            else:
                if close_open_dict[char] == stack[-1]:
                    stack = stack[:-1]
                else:
                    incorrect_line = True
                    break
        if not incorrect_line:
            for character in stack:
                autocomplete_output[line_counter].append(open_close_dict[character])
        line_counter += 1
    return autocomplete_output


if __name__ == '__main__':
    #  part1
    # input_list = load_input("input_day10_small")
    # input_list = load_input("input_day10")
    # results = parse_input(input_list)

    # final_results = 0
    # for result in results:
    #     final_results += error_score_dict[result]
    # print(final_results)

    # part2
    # input_list = load_input("input_day10_small")
    input_list = load_input("input_day10")
    # results = parse_input(input_list)
    results = autocomplete_input(input_list)

    final_results = list()
    for result in results:
        result.reverse()
        final_result = 0
        if len(result) > 0:
            for char in result:
                final_result *= 5
                final_result += autocomplete_score_dict[char]
            final_results.append(final_result)

    final_results.sort()
    print(final_results[int(len(final_results) / 2)])

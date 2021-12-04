def run_diagnostic_for_power_consumption(file_name):
    with open(file_name, mode="r") as input_f:
        line_number = 0
        first_line = input_f.readline()
        binary_numbers_length = len(first_line.strip())
        results_array = [0] * binary_numbers_length
        for line in input_f:
            line_number += 1
            for i in range(0, binary_numbers_length):
                results_array[i] += int(line[i])

        gamma_rate = ""
        epsilon_rate = ""
        for result in results_array:
            diff = line_number - result
            if diff > result:
                gamma_rate += "0"
                epsilon_rate += "1"
            else:
                gamma_rate += "1"
                epsilon_rate += "0"
        gamma_rate_as_number = int(gamma_rate, 2)
        epsilon_rate_as_number = int(epsilon_rate, 2)

        return gamma_rate_as_number * epsilon_rate_as_number


def run_diagnostic_for_life_support(input_data, limit, condition):
    result_str = ""
    i = 0
    while i < limit:
        zeroes, ones = split_data_to_ones_and_zeroes(input_data, i)
        if condition(len(ones), len(zeroes)):
            result_str += "1"
            input_data = ones
        else:
            result_str += "0"
            input_data = zeroes
        print(f"zeroes {len(zeroes)} vs ones {len(ones)} sum = {len(zeroes) + len(ones)} result = {result_str}")
        if len(input_data) == 1:
            return int(input_data[0], 2)
        i += 1
    return int(result_str, 2)


def oxygen_condition(ones, zeroes):
    return ones >= zeroes > 0


def co2_scrubber_condition(ones, zeroes):
    return zeroes > ones > 0


def split_data_to_ones_and_zeroes(list_of_data, position):
    zeroes = list()
    ones = list()
    for line in list_of_data:
        value_at_position = int(line[position])

        if value_at_position == 1:
            ones.append(line)
        else:
            zeroes.append(line)
    return zeroes, ones


if __name__ == '__main__':
    diagnostic_result = run_diagnostic_for_power_consumption("input_day03")
    print()
    print(diagnostic_result)

    with open("input_day03", mode="r") as input_f:
        first_line = input_f.readline()
        single_data_row_length = len(first_line.strip())

    with open("input_day03", mode="r") as input_f:
        co2_scrubber_result = run_diagnostic_for_life_support(input_f, single_data_row_length, co2_scrubber_condition)
    print()
    with open("input_day03", mode="r") as input_f:
        oxygen_result = run_diagnostic_for_life_support(input_f, single_data_row_length, oxygen_condition)

    final_result = co2_scrubber_result * oxygen_result
    print()
    print(final_result)

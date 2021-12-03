
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


if __name__ == '__main__':
    diagnostic_result = run_diagnostic_for_power_consumption("input_day03")

    print()
    print(diagnostic_result)

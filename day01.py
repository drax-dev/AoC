
def count_larger_measurements_simple(data):
    previous_measurements = -1
    counter = 0

    for line in data:
        current_measurement = int(line)
        if previous_measurements == -1:
            print(f"{previous_measurements} -> {current_measurement} (N/A - no previous measurement)")
            previous_measurements = current_measurement
            continue
        info = f"{previous_measurements} -> {current_measurement}"
        if current_measurement > previous_measurements:
            info += " (increased)"
            counter += 1
        else:
            info += " (decreased)"
        print(info)
        previous_measurements = current_measurement
    return counter


def count_larger_measurements_sliding_window():
    result_list = list()
    with open("input_day01", mode="r") as input_f:
        lines = input_f.read().splitlines()

        for i in range(1, len(lines) - 1):
            sum_of_lines = int(lines[i - 1]) + int(lines[i]) + int(lines[i + 1])
            result_list.append(sum_of_lines)
    return count_larger_measurements_simple(result_list)


if __name__ == '__main__':
    with open("input_day01", mode="r") as input_file:
        result = count_larger_measurements_simple(input_file)
        print()
        print(result)

    result = count_larger_measurements_sliding_window()
    print()
    print(result)

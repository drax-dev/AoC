
def count_larger_measurements():
    previous_measurements = -1
    counter = 0
    with open("input", mode="r") as input_file:
        for line in input_file:
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


if __name__ == '__main__':
    result = count_larger_measurements()
    print()
    print(result)

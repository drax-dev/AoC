
def read_input(file_name):
    with open(file_name, mode="r") as input_f:
        file_content = input_f.read()
        list_of_initial_state = file_content.strip().split(',')
        list_of_initial_state = list(map(int, list_of_initial_state))
    return list_of_initial_state


def simulate_lanternfish(list_of_initial_state, number_of_days):
    print("Initial state: ")
    print(list_of_initial_state)
    for day in range(1, number_of_days + 1):
        print(f"After {day} days: ")
        new_lanternfish_counter = 0
        for i in range(len(list_of_initial_state)):
            if list_of_initial_state[i] > 0:
                list_of_initial_state[i] -= 1
            else:
                list_of_initial_state[i] = 6
                new_lanternfish_counter += 1
        new_lanternfish_list = [8 for x in range(new_lanternfish_counter)]
        list_of_initial_state += new_lanternfish_list
        # print(list_of_initial_state)
        print(len(list_of_initial_state))
    return list_of_initial_state


def simulate_lanternfish_better(list_of_initial_state, number_of_days):
    population = [0] * 9
    for lanternfish in list_of_initial_state:
        population[lanternfish] += 1

    for day in range(number_of_days):
        next_cycle_population = population[0]
        for i in range(0, 8):
            population[i] = population[i + 1]
        population[6] += next_cycle_population
        population[8] = next_cycle_population

    sum_of_population = 0
    for i in range(0, 9):
        sum_of_population += population[i]
    return sum_of_population


if __name__ == '__main__':
    initial_state = read_input("input_day06")
    # initial_state = read_input("input_day06_small")
    final_state = simulate_lanternfish_better(initial_state, 256)
    print(final_state)

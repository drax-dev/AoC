
patterns = {0: ["a", "b", "c", "e", "f", "g"], 1: ["c", "f"], 2: ["a", "c", "d", "e", "g"],
            3: ["a", "c", "d", "f", "g"], 4: ["b", "c", "d", "f"], 5: ["a", "b", "d", "f", "g"],
            6: ["a", "b", "d", "e", "f", "g"], 7: ["a", "c", "f"], 8: ["a", "b", "c", "d", "e", "f", "g"],
            9: ["a", "b", "c", "d", "f", "g"]}


class Entry:
    def __init__(self, input_list, output_list):
        self.input_values = input_list
        self.output_values = output_list
        self.number_to_segments = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
        self.real_segment_to_segment = dict()
        self.occurrences_of_character = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
        self.coded_segments_to_value = dict()

    def decode_segments(self):
        for input_value in self.input_values:
            for char in input_value:
                self.occurrences_of_character[char] += 1

        for input_value in self.input_values:
            length = len(input_value)
            for char in input_value:
                if length == 2:
                    self.number_to_segments[1].update(char)
                elif length == 3:
                    self.number_to_segments[7].update(char)
                elif length == 4:
                    self.number_to_segments[4].update(char)
                elif length == 7:
                    self.number_to_segments[8].update(char)

        self.real_segment_to_segment["a"] = list(self.number_to_segments[7] - self.number_to_segments[1])[0]

        for key, value in self.occurrences_of_character.items():
            if value == 4:
                self.real_segment_to_segment["e"] = key
            elif value == 6:
                self.real_segment_to_segment["b"] = key
            elif value == 8 and key != self.real_segment_to_segment["a"]:
                self.real_segment_to_segment["c"] = key
            elif value == 9:
                self.real_segment_to_segment["f"] = key
            elif value == 7 and key not in list(self.number_to_segments[4]):
                self.real_segment_to_segment["g"] = key
            elif value == 7 and key in list(self.number_to_segments[4]):
                self.real_segment_to_segment["d"] = key

        for number, characters in patterns.items():
            tmp_set = set()
            for char in characters:
                tmp_set.update(self.real_segment_to_segment[char])
            self.number_to_segments[number] = tmp_set

    def decode_outputs(self):
        result = str()
        for output_value in self.output_values:
            tmp_set = set(list(output_value))
            for number, set_of_characters in self.number_to_segments.items():
                if len(tmp_set.symmetric_difference(set_of_characters)) == 0:
                    result += str(number)
                    break
        return result


def load_input(file_name):
    with open(file_name, mode="r") as input_f:
        entries_list = list()
        for line in input_f:
            line_splitted = line.rstrip().split('|')
            input_splitted = line_splitted[0].rstrip().split(" ")
            output_splitted = line_splitted[1].lstrip().split(" ")
            entries_list.append(Entry(input_splitted, output_splitted))
    return entries_list


def process_input(input_list):
    output = 0
    for entry in input_list:
        for output_value in entry.output_values:
            length = len(output_value)
            if length == 2 or length == 4 or length == 3 or length == 7:
                output += 1
    return output


def process_input_smart(input_list):
    result = 0
    for entry in input_list:
        entry.decode_segments()
        tmp_value = entry.decode_outputs()
        result += int(tmp_value)
    return result


if __name__ == '__main__':
    # entries = load_input("input_day08_small")
    entries = load_input("input_day08")
    # result = process_input(entries)
    final_result = process_input_smart(entries)
    print(final_result)

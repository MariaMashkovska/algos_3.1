"""
Functions which build a shift table and find pattern in string
"""


def shift_table_building(pattern):
    if not pattern:
        return "No data"

    patterns_length = len(pattern)
    shift_dict = {}

    for j in range(patterns_length):
        shift_dict[ord(pattern[j])] = j

    return shift_dict


def boyer_moore(string, pattern, shifts_dict):
    patterns_length = len(pattern)
    strings_length = len(string)
    patterns_index = []

    if not pattern or not string:
        return "Put some letters"

    i = 0
    while i <= strings_length - patterns_length:
        shifts = 0
        j = patterns_length - 1

        while j >= 0:
            if pattern[j] != string[i + j]:
                shifts = max(1, j - shifts_dict.get(ord(string[i + j]), -1))
                break
            j -= 1

        if shifts == 0:
            patterns_index.append(i)
            shifts = 1

        i += shifts

    return patterns_index


simple_string: str = "Hello Victoria Secret"
needed_pattern: str = "Victoria"

shifts_table = shift_table_building(needed_pattern)
result = boyer_moore(simple_string, needed_pattern, shifts_table)

print(result)

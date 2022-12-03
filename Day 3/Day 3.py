import string


def get_data():
    data_def = []
    with open("puzzle_input.txt", "r") as file:
        for line in file:
            data_def.append(line)
    return data_def


def treat_data(raw_data_def):
    data_def = []
    for e in range(len(raw_data_def)):
        data_def.append(raw_data_def[e].replace("\n", ""))
    return data_def


def set_priorities():
    priorities_def = {}
    letters = string.ascii_lowercase + string.ascii_uppercase
    letter_prio = 0
    for letter in letters:
        letter_prio += 1
        priorities_def[letter] = letter_prio
    return priorities_def


def is_in_both_halves(half1_def, half2_def, doubled_items_def):
    shit = ""
    for x in half1_def:
        if x in half2_def:
            if x not in shit:
                doubled_items_def.append(x)
                shit += f"{x}"


def get_doubled_items(data_def):
    doubled_items_def = []
    for n in range(len(data_def)):
        half_1 = data_def[n][:len(data_def[n]) // 2]
        half_2 = data_def[n][len(data_def[n]) // 2:]
        is_in_both_halves(half_1, half_2, doubled_items_def)
    return doubled_items_def


def get_sum(prio_def, items_def):
    sum_def = 0
    for x in items_def:
        sum_def += prio_def[x]
    return sum_def


raw_data = get_data()
data = treat_data(raw_data)
priorities = set_priorities()
doubled_items = get_doubled_items(data)
sum_of_priorities = get_sum(priorities, doubled_items)

print(sum_of_priorities)

def is_array(some_data):
    if type(some_data) in [list, tuple, dict, set]:
        return True
    return False


def num_filter(some_value):
    if isinstance(some_value, str):
        return len(some_value)
    return some_value


def calculate_structure_sum(some_massive):
    global total_sum
    for item in some_massive:
        if is_array(item):
            if isinstance(item, dict):
                for k, v in item.items():
                    total_sum += num_filter(k) + num_filter(v)
                    # print(f'key {k} \t-> {num_filter(k)} \tvalue {v} \t-> {num_filter(v)} \t sum {total_sum}')
            else:
                calculate_structure_sum(item)
        else:
            total_sum += num_filter(item)
            # print(f'item {item} \t-> {num_filter(item)} \t sum {total_sum}')
    return total_sum


total_sum = 0

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params('cat', [1, 5])
print_params(*[34, "dog"], 23.15)
print_params()

print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['dodo', 5, 34.1]
values_dict = {'a': 'dront', 'b': 6, 'c': 35.2}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['craft', 56]
print_params(*values_list_2, 42)
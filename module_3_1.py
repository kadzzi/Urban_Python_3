def count_calls() -> None:
    global calls
    calls += 1


def string_info(my_string: str) -> tuple:
    count_calls()
    return len(my_string), my_string.upper(), my_string.lower()


def is_contains(my_string: str, my_list: list) -> bool:
    count_calls()
    return my_string.lower() in [x.lower() for x in my_list]


calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

import functools


def add(number1, number2):
    return number1 + number2


def sum_pair(pair):
    return sum(pair)


def greater_than_five(number):
    return number > 5


def sums_greater_than_five(pairs):
    sums = map(sum_pair, pairs)
    return list(filter(greater_than_five, sums))


def is_numeric(text):
    return text.isdigit()


def total_of_numeric_strings(data):
    numeric_only = filter(is_numeric, data)
    numbers = map(int, numeric_only)
    return reduce(add, numbers)


    print("1.", sums_greater_than_five([(1, 2), (3, 4), (5, 6)]))
    print("2.", total_of_numeric_strings(['123', '456', '789', 'abc', 'def']))




def is_even(number):
    return number % 2 == 0


def is_longer_than_five(word):
    return len(word) > 5


def first_value_greater_than_two(pair):
    return pair[0] > 2


def divisible_by_3_and_5(n):
    return number % 3 == 0 and number % 5 == 0


def is_palindrome(word):
    return word == word[::-1]


def get_even_numbers(numbers):
    return list(filter(is_even, numbers))


def get_long_words(words):
    return list(filter(is_longer_than_five, words))


def filter_tuples(pairs):
    return list(filter(first_value_greater_than_two, pairs))


def get_divisible_by_3_and_5(numbers):
    return list(filter(divisible_by_3_and_5, numbers))


def get_palindromes(words):
    return list(filter(is_palindrome, words))


    print("1.", get_even_numbers(range(1, 21)))
    print("2.", get_long_words(['cat', 'elephant', 'tiger', 'lion']))
    print("3.", filter_tuples([(1, 'A'), (4, 'B'), (2, 'C')]))
    print("4.", get_divisible_by_3_and_5(range(1, 51)))
    print("5.", get_palindromes(['level', 'world', 'madam', 'python']))




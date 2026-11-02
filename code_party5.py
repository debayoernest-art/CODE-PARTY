import functools



def add(number1, number2):
    return number1 + number2


def larger(number1, number2):
    return number1 if number1 > number2 else number2


def join_with_space(number1, number2):
    return number1 + " " + number2


def multiply(number1, number2):
    return number1 * number2


def square(number):
    return number ** 2


def sum_to_50():
    return reduce(add, range(1, 51))


def find_max(numbers):
    return reduce(larger, numbers)


def join_words(words):
    return reduce(join_with_space, words)


def product_of_squares(numbers):
    return reduce(multiply, map(square, numbers))


    print("1.", sum_to_50())
    print("2.", find_max([3, 5, 9, 2, 8]))
    print("3.", join_words(['I', 'love', 'Python']))
    print("4.", product_of_squares([1, 2, 3, 4]))



def to_upper(word):
    return word.upper()


def square(number):
    return number ** 2


def capitalize_name(name):
    return name.capitalize()


def add_tax(price):
    return price * 1.10


def uppercase_all(words):
    return list(map(to_upper, words))


def square_all(numbers):
    return list(map(square, numbers))


def capitalize_all(names):
    return list(map(capitalize_name, names))


def add_tax_to_all(prices):
    return list(map(add_tax, prices))



    print("1.", uppercase_all(['python', 'java', 'c++']))
    print("2.", square_all(range(1, 11)))
    print("3.", capitalize_all(['john', 'mary', 'steve']))
    print("4.", add_tax_to_all([100, 200, 300]))



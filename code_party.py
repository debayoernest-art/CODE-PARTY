def append_to_tuple(tup, value):
    
    return tup + (value,)


def change_nested_value(tup, outer_index, inner_index, new_value):
   
    tup[outer_index][inner_index] = new_value
    return tup


def add_to_tuple_via_list(tup, value):
    
    temp_list = list(tup)
    temp_list.append(value)
    return tuple(temp_list)


def unpack_tuple(tup):
   
    a, b, *rest = tup
    return a, b, rest



    
    original = (1, 2, 3, 4)
    new_tuple = append_to_tuple(original, 5)
    print("1. Original:", original)
    print("   New tuple:", new_tuple)

    
    numbers = (1, 2, [3, 4], 5)
    change_nested_value(numbers, 2, 1, 99)
    print("2.", numbers)

   
    fruits = ('apple', 'banana', 'cherry')
    fruits = add_to_tuple_via_list(fruits, 'mango')
    print("3.", fruits)

   
    a, b, rest = unpack_tuple((10, 20, 30, 40))
    print("4. a =", a, "| b =", b, "| rest =", rest)




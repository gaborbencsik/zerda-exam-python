# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].

def every_second(old_list):
    new_list = []

    if type(old_list) is list:
        for item in old_list:
            if old_list[item-1] % 2 == 0:
                new_list.append(item)
        return new_list
    else:
        raise TypeError ('This is not a list!')

example_list = [1, 2, 3, 4, 5]
print(every_second(example_list))

print(example_list[1::2])

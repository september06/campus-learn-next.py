import functools


def four_dividers(num):
     if num % 4 == 0 : return num


list_of_numbers = [2, 3, 4, 5, 6]
result = map(four_dividers, list_of_numbers)
print(list(result))


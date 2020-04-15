import functools


def double(letter):
    return letter * 2

def double_letter(my_str):
    return "".join(map(double, my_str))

my_str = "python"
print(double_letter(my_str))

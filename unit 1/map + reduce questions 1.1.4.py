import functools
def ctoi(number):
    return int(number)
def total(number1, number2):
    return number1+number2
def our_sum(number):
     number_in_list=map(ctoi,number)
     return functools.reduce(total, list(number_in_list))
def sum_of_digits(number):
   return our_sum(list((str(number))))


print(sum_of_digits(104))


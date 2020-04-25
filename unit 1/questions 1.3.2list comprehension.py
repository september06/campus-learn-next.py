import functools

def is_prime(number):
   return (lambda list : True in list) ([ number%x == 0  for x in range(2,number)])


print(is_prime(42))
print(is_prime(43))
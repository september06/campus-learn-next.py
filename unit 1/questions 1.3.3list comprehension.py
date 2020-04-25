import functools

def is_funny(string):
   return (lambda list : not(True in list)) ([  (x!= 'h' and x != 'a') for x in list(string)])



print(is_funny("hahahahahaha"))
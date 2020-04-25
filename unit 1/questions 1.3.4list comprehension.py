import functools

def find_password(string):
   return ''.join(map(str, [chr(ord(i)+2) if ord(i) > 95 and ord(i) < 123 else i for i in string.lower()]))



password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print(find_password(password))
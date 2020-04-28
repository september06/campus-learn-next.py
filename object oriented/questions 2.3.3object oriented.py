class cats:
   #instance_ammount = 0
   def __init__(self, cat_name="Octavio", cat_age=1):
      self._cat_name = cat_name
      self._c_age = cat_age


   def cat_barthday(self):
       self._c_age+=1

   def set_name(self, name):
     self._cat_name = name

   def get_name(self):
      return self._cat_name

   def printer(self):
      print("Current age is : ",self._c_age )

def main():
   mooe = cats('moe',20)

   moow = cats()

   mooe.cat_barthday()
   print( mooe.get_name())
   print( moow.get_name())
   moow.set_name('cato')
   print(moow.get_name())

main()
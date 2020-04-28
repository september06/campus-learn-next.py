class cats:
   def __init__(self):
      self.c_age = 1

   def cat_barthday(self):
       self.c_age+=1
   def printer(self):
      print("Current age is : ",self.c_age )

def main():
   mooe = cats()
   moow = cats()
   mooe.cat_barthday()
   mooe.printer()
   moow.printer()

main()
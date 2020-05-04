class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hungery = 0):
        self._name = name
        self._hunger =  hungery

    def feed(self):
        self._hunger -= 1

    def is_hungry(self):
        return self._hunger > 0

    def get_name(self):
        return self._name

    def go_to_toilet(self):
         self._hunger += 1

    def talk(self):
        self._sound = " no sound"




class Dog(Animal):
    def __init__(self, name, hungery = 0):
        Animal.__init__(self, name ,hungery )

    def talk(self):
        super().talk()
        self._sound = "woof woof"
        print(self._sound)

    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    def __init__(self, name, hungery = 0):
        Animal.__init__(self, name , hungery )

    def talk(self):
        super().talk()
        self._sound = "meow"
        print(self._sound)

    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    def __init__(self, name, hungery = 0,stink_count = 6):
        Animal.__init__(self, name ,hungery )
        _stink_count = stink_count
    def talk(self):
        super().talk()
        self._sound = "tsssss"
        print(self._sound)

    def stink(self):
        print("Dear lord!")
class Unicorn(Animal):
    def __init__(self, name, hungery = 0):
        Animal.__init__(self, name, hungery )

    def talk(self):
        super().talk()
        self._sound = "Good day, darling"
        print(self._sound)

    def sing(self):
        print("I’m not your toy...")

class Dragon(Animal):

    def __init__(self, name, hungery = 0, color = "green"):
        Animal.__init__(self, name, hungery )
        _color = color

    def talk(self):
        super().talk()
        self._sound = "Raaaawr"
        print(self._sound)

    def breath_fire(self):
        print("$@#$#@$")

def main():

    zoo_dog = Dog("Brownie", 10)
    zoo_cat = Cat("Zelda", 3)
    zoo_skunk = Skunk("Stinky")
    zoo_unicorn = Unicorn("Keith", 7)
    zoo_dragon = Dragon("Lizzy", 1450)
    zoo_lst = [zoo_dog, zoo_cat, zoo_skunk, zoo_unicorn, zoo_dragon]
    zoo_type = [Dog, Cat, Skunk, Unicorn, Dragon]
    special_method = {
        Dog: zoo_dog.fetch_stick,
        Cat: zoo_cat.chase_laser,
        Skunk: zoo_skunk.stink,
        Unicorn: zoo_unicorn.sing,
        Dragon: zoo_dragon.breath_fire,
    }
    for animal in zoo_lst:
        print(animal.__class__.__name__  + " " + animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        for animal_type in zoo_type:
            if isinstance(animal, animal_type):
                special_method[animal_type]()

    print(animal.zoo_name)

if __name__  ==  "__main__":
    main()
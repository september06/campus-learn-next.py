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
        self._stink_count = stink_count
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

    def __init__(self, name, hungery = 0, color = "Green"):
        Animal.__init__(self, name, hungery )
        self._color = color

    def talk(self):
        super().talk()
        self._sound = "Raaaawr"
        print(self._sound)

    def breath_fire(self):
        print("$@#$#@$")








def make_instance():
    zoo_dog = Dog("Brownie", 10)
    zoo_cat = Cat("Zelda", 3)
    zoo_skunk = Skunk("Stinky")
    zoo_unicorn = Unicorn("Keith", 7)
    zoo_dragon = Dragon("Lizzy", 1450)
    inc_list = [zoo_dog, zoo_cat, zoo_skunk, zoo_unicorn, zoo_dragon]
    return inc_list

def add_instance_to_list():
    zoo_dog1 = Dog("Doggo", 80)
    zoo_cat1 = Cat("Kitty", 80)
    zoo_skunk1 = Skunk("Stinky Jr.", 80)
    zoo_unicorn1 = Unicorn("Clair", 80)
    zoo_dragon1 = Dragon("McFly", 80)
    inc_add = [zoo_dog1, zoo_cat1, zoo_skunk1, zoo_unicorn1, zoo_dragon1]
    return inc_add

def feed_and_print(zoo_lst, zoo_type,  special_method ):
    for animal in zoo_lst:
        print(animal.__class__.__name__  + " " + animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        for animal_type in zoo_type:
            if isinstance(animal, animal_type):
                special_method[animal_type]()


    
def main():

    zoo_lst = make_instance()
    zoo_lst.extend(add_instance_to_list())
    zoo_type = [Dog, Cat, Skunk, Unicorn, Dragon]
    special_method = {
        zoo_type[0]: zoo_lst[0].fetch_stick,
        zoo_type[1]: zoo_lst[1].chase_laser,
        zoo_type[2]: zoo_lst[2].stink,
        zoo_type[3]:  zoo_lst[3].sing,
        zoo_type[4]: zoo_lst[4].breath_fire,
    }
    feed_and_print(zoo_lst, zoo_type, special_method )
    print(Animal.zoo_name)


if __name__  ==  "__main__":
    main()
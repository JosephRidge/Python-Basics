"""
OBJECT ORIENTED PROGRAMMING (OOP): 
    - a progrmming paradigm(enabler of resuability throught "blueprints")
    - Concepts:
        - Encapsulation
        - Inheritance
        - Polymorphism

Resource: https://docs.python.org/3/tutorial/classes.html

"""
# creaying a blueprint of a vehicle

class Vehicle: 
# attributes => features or that particular class
    name = "Mercedes"
    yom = 2022
    color = "black"
    engine = "v8"

#  methods  (behaviors ) = > a function inside a class is called a method
    def raceMode(self):
        print("vrrrroooom!")

    def cruiseMode(self):
        print("Swiiish!")

    def offroadMode(self):
        print("You can climb a mountain!")

# vehicle_one = Vehicle() # initialize a classs
# vehicle_two = Vehicle() # initialization but different

# print(vehicle_one.color) # we use a dot operator to access attribute/ methods withing the class
# vehicle_one.raceMode()
# vehicle_two.cruiseMode()



    # yob
    # type ( aquatic, land, air)
    # name

    # behaviors ( eating, runnning, hunting, sleeping)
class Animal:
    #  attributes
    def __init__(self, yob, specie, name): # intialization
        self.__yob = yob # encapsulation
        self.specie = specie
        self.name = name 

    #  methods (behaviors)
    def age(self):
        print(f"{self.name} was born in {self.__yob} and their is {2026 - self.__yob}")

    def eating(self):
        print(f"{self.name} is eating food!") 

    def runnning(self):
        print(f"{self.name} is runnning!") 

    def sleeping(self):
        print(f"{self.name} is sleeping!") 

    def happy(self):
        print(f"{self.name} is happy!") 

#  creating objects of Animals
# cow = Animal(yob=2021, specie="Fresian", name="MODERN Cauw")
# goat = Animal(2020, "Blly Goat", "Thee GOAT")

# cow.eating()
# goat.eating()
# cow.happy()
# goat.happy()

# print(cow.name)
# print(goat.name)
# # print(cow.__yob)
# # print(goat.__yob)
# cow.age()
# goat.age()

# inheritance
class Dog(Animal):
    #  attributes
    def __init__(self, name, yob, color,  specie, size):
        super().__init__(yob, specie, name)
        self.color = color 
        self.size = size
    
    # methods
    def happy(self): # polymorphism
        print(f"{self.name}, Just found the source of food let us go!")
        print(f"{self.name} is happy!") 



class Cow:
    def Speak(self):
        print("Moooooo")


class Cow:
    def Speak(self):
        print('Meau')

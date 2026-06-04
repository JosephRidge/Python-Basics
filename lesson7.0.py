"""
OBJECT ORIENTED PROGRAMMING (OOP): 
    - a progrmming paradigm(enabler of resuability throught "blueprints")
    - Concepts:
        - Encapsulation
        - Inheritance
        - Polymorphism
"""
# creaying a blueprint of a vehicle

class Vehicle:
    #  attributes => features or that particular class
    #  methods (behaviors ) = > a function inside a class is called a method

# attributes
    name = "Mercedes"
    yom = 2022
    color = "black"
    engine = "v8"

#  methods 
    def raceMode(self):
        print("vrrrroooom!")

    def cruiseMode(self):
        print("Swiiish!")

    def offroadMode(self):
        print("You can climb a mountain!")

vehicle_one = Vehicle() # initialize a classs

print(vehicle_one.color) # we use a dot operator to access attribute/ methods withing the class
vehicle_one.raceMode()

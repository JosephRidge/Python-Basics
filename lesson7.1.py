from . import Vehicle, Animal, Dog, Cow

vehicle_one = Vehicle() # initialize a classs
vehicle_two = Vehicle() # initialization but different
cow = Animal(yob=2021, specie="Fresian", name="MODERN Cauw")
goat = Animal(2020, "Blly Goat", "Thee GOAT")

print(cow.name)
print(goat.name)
# print(cow.__yob)
# print(goat.__yob)
cow.age()
goat.age()

print("=================================")
bosco = Dog(
    name="Bosco", 
    yob =2020,
    color= "SPace Brown", 
    specie="Bosoc-hunter", 
    size=64.5)
bosco.happy()
# print(bosco.yob) # returns an exception since yob is encapsulated - private

print("=================================")

cow = Cow()
cow.Speak()
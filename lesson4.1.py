"""
Lists:
    - data structure (how do i store items in an efficient(time & space) manner?)
    - Types:
        - tuples
        - dictionary
        - array/ lists
        - set 
    - each data type has its respective methods 

"""

# Tuples :
    # - immutable (constant)
    # - enclose in parenthesis ()
    # - type: <class 'tuple'>

output = ""

fruits = ("apple", "apple", "mango", "pineapples")

output = type(fruits) # attaining the type
output = fruits[2] #accessing via an index
output = fruits.count("apple") # how many of occurence 
output = fruits.index("pineapples")

# dictionary (you are represenitng real world things eg person)
    # - key : value pair
    # key is often in string form and can be numbers
    # we use the key to access the values

student = {
    "name":"John Doe", 
    "age": 12,
    "course": "SWE1"
}
output = student.get("name") # example of a dictionary method that returns the value of a particular key
output  = student.copy()
# output = student.clear() # delete items
examiner = {"John Doe", "Peter Parker" , "Noir"}
units = 0
output = dict.fromkeys(examiner, units) # returns to us a dictionary combined from a list of items and a value to place in each 
ouput  = output.clear() # delete items
output = student.items() # returns to us a tuple composed of the data key-value pair
output = student.keys() # we get the keys 

print("==============================================")
print(output)
print("==============================================")
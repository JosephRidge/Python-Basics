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
    # Reference: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

student = {
    "name":"John Doe", 
    "age": 12,
    "course": "SWE1"
}
output = student.get("name") # example of a dictionary method that returns the value of a particular key
output  = student.copy()
# output = student.clear() # delete items
examiner = {"John Doe", "Peter Parker" , "Noir"}
units = []
output = dict.fromkeys(examiner, units) # returns to us a dictionary combined from a list of items and a value to place in each 
output  = output.clear() # delete items
output = student.items() # returns to us a tuple composed of the data key-value pair
output = student.keys() # we get the keys 

examiner = {"John Doe", "Peter Parker" , "Noir"}
units = 0
output = dict.fromkeys(examiner, units)  # this creates dictionaries with constant values

hospitalsMed = {"malaria","headcahe", "backache"}
defaultOutcome = "-ve"
output = dict.fromkeys(hospitalsMed, defaultOutcome) # this can be used for default/ intializations eg starting point = 0

output = "John Doe " in examiner # predicate scenario or association (key in diction )
output = dict.fromkeys(hospitalsMed, defaultOutcome) 
output = "+ve" in output.values() # it checks ythe values of the dictionary and returns either True of False t it exists or fails to exist
student = { 
    "name":"Johanna Does",
    "age":100, 
    "yob":1984,
    "career":"Tech"
}

output = "Tech" in student.values() 

# for i in student:
#     return i.value == "Tech"

#  interesting comparison: 
"""
student = { 
    "name":"Johanna Does",
    "age":100, 
    "yob":1984,
    "career":"Tech"
}

output = "Tech" in student.values() 

VS 

simple loop command

Testing:
- speed of outcome/ search 

"""

# SET:
    # - collection of unique elements
    # - you can perfom set operations on them eg union, intersect, disjoint etc
    # - wrapped inside {}
    # - <class 'set'>
    # Refrences: https://www.w3schools.com/python/python_ref_set.asp

uniqueNumbers = {1,11,0,0,0,1,2,3,4,5,6,7,7,7,7,8,8,8,9,9,9,9,10,10,10}

output = uniqueNumbers # composed of unique and organized numbers
# output = uniqueNumbers()
output = type(uniqueNumbers)

# List arrays
    # - enclosed in []
    # - can have different data types
    # - its dedicated methods
    # - accessed via index 

fruits = ["mango", "apple","WaterMelon","WaterMelon","WaterMelon", 12,123,12345]
hospitalsMed = {"malaria","headcahe", "backache","backache","backache","backache","backache","backache","backache"}
output = set(fruits)
output = set(hospitalsMed)
print("==============================================")
print(output)
print("==============================================")
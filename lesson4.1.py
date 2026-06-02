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

print("==============================================")
print(output)
print("==============================================")
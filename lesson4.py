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
output ="" # global variable
"""
Array: 
    - can be composed of different data types
    - enclosed in a square bracket []
    - each item is accessed via an index
    - class type is a list: <class 'list'>
    - lists are mutable in nature
"""

# array
# fruits = ['apple', 'mango', 'pineapple', 1,2,3,4] # not best practice to have multiple data types
fruits = ['apple', 'mango', 'pineapple', 'oranges', 'banana', 'coconut','avocado','tomatoe','dragon fruit', 'kiwi','watermelon','pawpaw', 'lime']
output = fruits

# methods
fruits.pop() # remove last item
fruits.sort() # sorts in ascending
fruits.remove("pawpaw") # removing targeted item from the list 
fruits.append("sweet bananas")
fruits.sort() # sorts in ascending

# loop (used to iterate through lists)
# for fruit in fruits:
#     print(fruit)

output = output[3] # accessing via index

output = fruits 
output = type(output)
fruits[0] = "Green Apples" # lists are mutable in nature

output = fruits

"""
Tuple: 
    - can be composed of different data types
    - enclosed in a square bracket ()
    - class type: <class 'tuple'>
    - immutable in nature (cannot update them)
"""

clouds = ('nimbus', 'cirrus', 'cumulus', 'startus')

output = clouds
output = type(clouds)
# clouds[0]='NIMBUS' # TypeError: 'tuple' object does not support item assignment => immutability
output = clouds[0].upper()

output = clouds.index('cumulus') # index of the item


"""
Set: 
    - composed of unique items
    - enclosed in a curcly braces {}
    - class type: <class 'set'> 
    - methods: (https://www.w3schools.com/python/python_ref_set.asp)
"""
fruits = {'apple', 'apple', 'apple', 'mango','mango','mango','mango','mango', 'pineapple',  'pineapple',  'pineapple',  'pineapple', 'oranges', 'banana',}
output = fruits

print("=======================================")
print(output)
print("=======================================")

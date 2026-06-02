"""
    Control flows: 
        - for loop
        - while loop
        - do.. while loop
    - Functions:
        - parameterized
        - non-parameterized
        - anonymous function (lambda functions)
"""

# loops => running iteration:

fruits = ["apples", "mangoes", "bananas", "water melon", "kiwi", "pineapples"] # array list

# for loop
for fruit in fruits:
    # print(fruit)
    pass # this temporarily sets the process ot have no logic until engineer write it. 

    #  nested loop
for fruit in fruits:
    for letter in fruit.upper():
        # print(letter)
        pass # this temporarily sets the process ot have no logic until engineer write it. 

fruits_two = fruits.copy()

while (len(fruits_two) <= len(fruits)):
    print(fruits)
    print(fruits_two)
    # fruits.pop() # it will pop last item
    fruits_two.append("guavas")
    print(fruits_two)



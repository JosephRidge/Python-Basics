"""    
         - if ... else
        - if ... elif...else
        - match
        - ternary operator ( {True} if condition else {False})
        - for loop
        - while loop  
        """

numOne = 10 
numTwo = 100 

# if numOne == 10:
#     print(f"this is {numOne}")
# else:
#     print(f"this is {numTwo}")
output = ""

if numOne >10 and numOne < 20: 
    output ="greater than 10 but below 20"
else:
    output = "not applicable"


if numOne >= 10 or numOne < 20: 
    output ="greater than 10 but below 20"
else:
    output = "not applicable"

numOne = 10

if numOne  <= 8: 
    output ="less than or equal to 10  "
elif numOne < 15:
    output ="less than 15 "
else:
    output = "not applicable"

#  ternary operator:
color = "blue"
final_color = "BLUE" if color == "blue" else "Not blue!" 

#  Match 
target_card = "Red Joker"

match target_card:
    case "Red Joker":
        output = "We found the red joker"
    case "Black Joker": 
        output = "We found the black joker"
    case _: # default case
        output = "no joker here!"
    
fruits = ["watermelon", "pineapple", "oranges", "bananas"]

# for fruit in fruits:
#     print(fruit)

while (len(fruits) < 5):
    fruits.append("green apples")
    print(fruits)


print("========================================")
print(output)
print("========================================")

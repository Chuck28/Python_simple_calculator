#Charles Cohen
#7/12/22
#Calculator.py
#Create Calculator

operator= input("Please enter: add, subtract, multiply, or divide: ")
print ("You chose " + str(operator) + ".")
number1 = input("What is the first number? ")
number1 = float(number1)
number2 = float(input("What is the second number? "))
if operator .lower() == "add":
        answer = number1 + number2
        print(number1 , "+",number2 , "==",answer) 
elif operator .lower() == "subtract":
        answer = number1 - number2
        print(number1 , "-", number2 , "==", answer)
elif operator .lower() == "multiply":
        answer = number1 * number2
        print(number1 , "*", number2 , "==", answer)
elif operator .lower() == "divide":
        answer = number1 + number2
        print(number1 , "/", number2 , "==", answer)
else:
    print("The option you chose (" + operator + ") is not valid")
    print("Please try this program again")

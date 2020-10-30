import addition
import subtraction 
import multiplication
import division

print("Welcome to the simple calculator, please select from the following options:")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("Please enter your selection:")
user_mathchoice = input()
print("Please enter your first number: ")
user_firstnumber = float(input())

print("Please enter your second number: ")
user_secondnumber = float(input())

if user_mathchoice == "1":
    print("Result:")
    print(addition.addNumbers(user_firstnumber,user_secondnumber))
elif user_mathchoice == "2": 
    print("Result:")
    print(subtraction.subtractNumbers(user_firstnumber,user_secondnumber))
elif user_mathchoice == "3": 
    print("Result:")
    print(multiplication.multiplyNumbers(user_firstnumber,user_secondnumber))
elif user_mathchoice == "4": 
    print("Result:")
    print(division.divideNumbers(user_firstnumber,user_secondnumber))
else:
    print("Something went wrong!")
   
   
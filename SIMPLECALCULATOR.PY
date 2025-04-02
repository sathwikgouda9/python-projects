
#THIS PROJECT IS ABOUT A SIMPLE CALCULATOR FOR ADDITION SUBTRACTION MULTIPLICATION AND DIVISION ALSO SOME FUNCTIONS LIKE SQUARE ROOT AND POWER 
import math
a = int(input("Enter first number: "))
b= int(input("Enter second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Power")
print("7. Exit")
choice = input("Enter choice (1/2/3/4/5/6/7): ")
if choice== '1':
    print("Addition:", a + b)
elif choice== '2':
    print("Subtraction:", a - b)
elif choice== '3':
    print("Multiplication:", a * b)
elif choice== '4':
    print("Division:", a / b)
elif choice== '5':
    print("Square Root:", math.sqrt(a))
elif choice== '6':
    print("Power:", a ** b)
elif choice== '7':
    print("Exiting the calculator. Goodbye!")
else:
    print("Invalid input")
print("Thanks for using the calculator!")
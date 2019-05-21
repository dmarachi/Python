#The calculator excerise from 100 competency

def add(x , y):
	return x + y

def subtract(x , y):
	return x - y

def multiply(x , y):
	return x * y

def divid(x , y):
	return x / y

print("Select operation")
print("Add")
print("Subtract")
print("Multiply")
print("Divid")

choice = input("Enter choice: ")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if choice == "Add":
	print(number1, "+", number2, "=", add(number1,number2))
elif choice == "Subtract":
	print(number1, "-", number2, "=", subtract(number1,number2))
elif choice == "Multiply":
	print(number1, "*", number2, "=", multiply(number1,number2))
elif choice == "Divid":
	print(number1, "/", number2, "=", divid(number1, number2))
else:
	print("Invalid value")


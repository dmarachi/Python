print("Hello Word");

print(2 + 1);
print(1 / 2);
print(1 - 2);
print(3 * 3);
print(2 ** 3);
print(2 + 10 * 10 + 3);
print((2 + 10) * (10 + 3));

a = 10;
print(a);
a = a + a;
print(a);

puppies = 6;
weight =2;
total = puppies * weight;
print(total);
print(len("Hello Word")); # to print the length of "Hello Word" which is 10 char

mystring = "Hello World";

print(mystring[0]);
print(mystring[1]);
print(mystring[-1]); # this is a way to print the last char from a string

thestring = "abcdefghij";

#To slice the string in thestring
print(thestring[0:3])
print(thestring[4:7])
print(thestring[0:7:2])

#to upper / lower /split case all the string
print(mystring.upper());
print(mystring.lower());
print(mystring.split());

username = "Dima";
color = "blue";

print("Dima's favorite color is blue");
print("{}'s favorite color is {}".format(username, color));

# f string literals!!

print(f"{username}'s color is {color}");

mylist = [1,2,3];

print(mylist);
print(len(mylist));

mylist1 = [100, 2,"Hi", 3.5, "hello"];

print(mylist1);
print(len(mylist1));
print(mylist1[2]);
print(mylist1[1:4]);

#to add to the end of the list
# mylist1.append("To you");
# print(mylist1);

#to insert at a certen index in the list
# mylist1.append(0, "GO");
# print(mylist1);

#to remove items from the list
popped_item = mylist1.pop(0)
print(mylist1);

print(popped_item)

#this is the nested list
mylist2 = [0,1,2]
mylist3 = [3,4,5]
mylist4 = [6,7,8]

mega_list = [mylist2 , mylist3, mylist4];
print(mega_list);
print(len(mega_list));
print(mega_list[2][1]);

#the use of dictionary
d = {"Key1" : "Value1", "Key2" : "Value2"}
print(d);
print(d["Key1"])

salaries = {"John":20, "Sally":30, "Sammy":15}
print(salaries["Sally"])
salaries["Cindy"] = 100 #Add to the dictionary
print(salaries["Cindy"])
salaries["John"] = salaries["John"] + 40; #Adjusting one of the already existing parts
print(salaries["John"])

people = {"John": [1,2,3], "Sally":[30,20,40]}
print(people["Sally"][0])

#A nested dictionary
people = {"John": {"salary":10, "age":30}}
print(people["John"]["age"])

s = {"k1": 10, "k2": 20, "k3": 30}
print(s.keys()) #to print only the keys od the dictionary
print(s.values()) # to print only the values
print(s.items()) # to print the tuples

#Tuples
t = (1,2,3,"a", 2.5)
print(t) 
print(t[0]) #using the index

#sets
x = set()
print(x)
x.add(1)
x.add(2)
x.add(3)
print(x)

mylist5 = [1,2,12,3,22,22,5,8,1,2,22,3,8]
print(set(mylist5))

#Booleans
c = True
e = False
g = None #Special keyword
print(1<2, 1>2)

username = "Admin"
check = "Admin"
permission = False
print(username == check)

print(1 == 1 and 2 < 3) #and requires that all options are true
print(1 == 1 or 2 > 3)  # or requires that one option is true

print(username == check and permission)

username = "Admin"
check = "Admin"
logged_in = True
has_permission = True

print(logged_in and has_permission)

#the use of if statment
if 1 < 2:
	print("yep!")

username = "Admin"
check = "Admin"
if username == check and 1 == 1:
	print("Access Granted!")
else:
	print("all above conditions, were not true!")

username = "Admin"
check = "Admin"
if username == check and 1 == 2:
	print("Access Granted!")
else:
	print("all above conditions, were not true!")

username = "Admin"
check = "Admin"
if username == check and 1 == 2:
	print("Access Granted!")
elif 1 == 1:
	print("Middel Condition is correct")
else:
	print("all above conditions, were not true!")

username = "Admin"
permission = True

if username == "Admin" and permission:
	print("Full Access")
elif username == "Admin" and permission == False:
	print("Admin access only, no full permission")
else:
	print("No access")

username = "Admin"
permission = False

if username == "Admin" and permission:
	print("Full Access")
elif username == "Admin" and permission == False:
	print("Admin access only, no full permission")
else:
	print("No access")

username = "Dima"
permission = True

if username == "Admin" and permission:
	print("Full Access")
elif username == "Admin" and permission == False:
	print("Admin access only, no full permission")
else:
	print("No access")

seq = [1,2,3,4,5]

for item in seq:
	print(item)
	print(item**2)
	print("Hello")

mystring = "Hello"

for char in mystring:
	print(char)

salaries = {"John":10, "Sally": 20, "Cindy": 30}

for employee in salaries:
	print(employee)
	print("has a salary of: ")
	print(salaries[employee])

#List of tupels ####### Tuple unpacking
mypairs = [("a",1),("b",2),("c",3)]
print(mypairs)

for item in mypairs:
	print(item)

for letter, number in mypairs:
	print(letter)
	print(number)

i = 1
while i < 5:
	print(f"i is currently: {i}")
	i = i + 1

for x in range(0,5):
	print(x)

for x in range(0,10):
	print(x)

for x in range(0,11,2):
	print(x)

result = list(range(0,11,2))
print(result)

print("a" in "Dima")
print("r" in "Dima")

print("a" in [1,2,3])
print(1 in [1,2,3])


##Now starting with functions def standes for function then the function name
def report_person():
	print("reporting person")

report_person()

def report_person(name):
	print("reporting " + name)

report_person("Cindy")

def report_person(name = "Default"):
	print("reporting " + name)
#if the function have no parameter to pass it will fall back to Default
report_person()

def add_number(number1, number2):
	return number1+number2

result = add_number(2,4)

print(result)
print(result + 10)

#max and min
print(max([2,5,9,1,4,20,45,35]))
print(min([2,5,9,1,4,20,45,35]))

#enumerate
#the list without emumeration
mylist = ["a", "b", "c"]
index = 0
for letter in mylist:
	print(letter)
	print("is at index: {}".format(index))
	index = index + 1

#the list with emumeration
mylist = ["a", "b", "c"]

for letter in enumerate(mylist):
	print(letter)

#enumerate and tupel

mylist = ["a", "b", "c"]

for index,letter in enumerate(mylist):
	print(letter)
	print(f"is at index {index}")

#.join join a list in a single string

mylist = ["a", "b", "c", "d"]

print("".join(mylist))
print("--".join(mylist))
print("-x-".join(mylist))

# write a function that returns a boolean indicating if the word "secret" is in a string.

def secret_check(mystring):
	if "secret" in mystring:
		return True
	else:
		return False
print(secret_check("This is a secret"))
print(secret_check("Hello to you"))

#another way to write the function
def secret_check1(mystring):
	return "secret" in mystring
		
print(secret_check1("This is a secret"))
print(secret_check1("Hello to you"))

# Create a code maker function. this function will take in a string name and replace any vowels with the letter x
def code_maker(mystring):

	output = list(mystring)
	print(output)
	for index,letter in enumerate(mystring):
		for vowel in "aeiou":
			if letter.lower() == vowel:
				output[index] = "x"
				# print(letter)

	output = "".join(output)
	return output

print(code_maker("Sammy"))
print(code_maker("Adam"))

#The calculator excerise from 100 competency

def add(x,y):
	return x + y

def subtract(x,y):
	return x - y

def multiply(x,y):
	return x * y

def divid(x,y):
	return x / y

print("Select operation")

# Scope
x = "outside"

def report():
	x = "inside"
	return x
print(report()) # returns inside
print(x) # returns outside

# LEGB Rule
# Local
def report1():
	#Local Assignment
	x = "Local"
	print(x)
print(report1())
# Enclosing
y = "This is global level"

def enclosing():
	y = "Enclosing level"

	def inside():
		print(y)

	inside()

enclosing()
print(enclosing())
# Global

# Built in

class Sample():
	pass

x = Sample()

print(type(x))

class Dog():
	def __init__(self, breed):
		self.breed = breed

x = Dog("lab")

print(x.breed)
print(type(x.breed)) # prints the type of the attribute
# Write a function called “email”. This function will receive two parameters: first name and last name. 
# It will return a well formatted email. For example:

# Larry Shumlich ⇒  larry.shumlich@evolveu.ca
# Heiko Peters ⇒ heiko.peters@evolveu.ca 

def email(firstName, lastName):
	return firstName + "." + lastName + "@evolveu.ca"

firstName = str(input("Enter first name: "))
lastName = str(input("Enter last name: "))


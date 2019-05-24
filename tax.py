#The tax excerise from 100 competency

def calculate_tax(income):
	
	# income = int(input("Enter income: "))

		if income <= 47630:
			tax = (income - 0) * 0.15 + 0;
		elif income  > 47630 and income <= 95259:
			tax = (income - 47630) * 0.205 + 7145
		elif income  > 95259 and income <= 147667:
			tax = (income - 95259) * 0.26 + 16908
		elif income  > 147667 and income <= 210371:
			tax = (income - 147667) * 0.29 + 30535
		elif income > 210371:
			tax = (income - 210371) * 0.33 + 48719
		else: 
			tax = 0
		print(income, tax)
		return tax

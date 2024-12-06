#TipCalculator
print("Welcome to the Tip Calculator - Don't be Cheap")

#get total bill
bill = input("What is the total Bill? $")

#how is the bill being split
split = int(input("How many people to split the bill? "))

#Percentage of tip
desired_tip_amount = input("How much tip would you like to leave? 12 15 or 20: ")
tip_percentage = int(desired_tip_amount) / 100
tip = tip_percentage + 1

#calculate total bill + tip
totalBill = float(bill) * tip

#calculate final paying amount
each_Pay = round(totalBill / split, 2)

print(f"Each person will pay: {each_Pay}")
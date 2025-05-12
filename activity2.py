print("Electricity bill")
no_units = int(input("Please enter the number of units consumed " ))
if no_units < 50:
    amount = no_units * 2.60
    surcharge = 25
elif 50 < no_units < 100:
    amount = no_units * 3.25
    surcharge = 35
elif  100< no_units < 200:
    amount = no_units * 5.26
    surcharge = 45
else:
    amount = no_units * 8.45
    surcharge = 75
total_bill = amount + surcharge
print("Your total bill is:" , total_bill)
print("Thank you!")
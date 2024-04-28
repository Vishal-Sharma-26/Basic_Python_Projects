rent = int(input("Enter your flat rent = "))
food = int(input("Enter the amount of food = "))
electricity_spends = int(input("Enter the total of elexticity spends = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in flat = "))

total_bill = electricity_spends * charge_per_unit
output = (food + rent + total_bill) // persons

print("Each person will pay = ", output)
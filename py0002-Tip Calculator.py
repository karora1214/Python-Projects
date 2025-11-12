# Tip Calculator

print("Welcome to the tip calculator")
bill = float(input("What is the total bill : "))
tip = float(input("What percentage of tip would you like to give? 10, 12, 15 : "))
mem = float(input("Enter the number of people to split the bill between : "))
total_tip  = bill * (tip/100)
total_bill = bill + total_tip
each_mem_bill = str(total_bill/mem)
print("Each person should pay : "+each_mem_bill)
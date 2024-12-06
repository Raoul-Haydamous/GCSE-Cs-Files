# Write your code below this line
total_spend = round(float(input("How much have you spent in total")),2)

if total_spend > 300:
    print("Discount is 10%")
elif total_spend >0:
    print("No discount")
else:
    print("Invalid input")
# Q03

#  Initialise variables
price_5 = 20.00 #price for 1-5 range
price_9 = 15.00 #price for 6-9 range
price_10 = 12.00 #price for 10+

total_price = 0 #overall price calculated after price bracket has been identified
#  Print prompt and take number of textbooks required
quantity = int(input("How many textbooks do you require? "))

#  Generate and display the price per textbook and the total cost
if quantity >= 1 and quantity <=5:
    total_price = quantity * price_5
    print(f"The cost per book is ${price_5} and your total is ${total_price}")
elif quantity >= 6 and quantity <=9:
    total_price = quantity * price_9
    print(f"The cost per book is ${price_9} and your total is ${total_price}")
elif quantity >=10:
    total_price = quantity * price_10
    print(f"The cost per book is ${price_10} and your total is ${total_price}")
else:
    print("invalid input")
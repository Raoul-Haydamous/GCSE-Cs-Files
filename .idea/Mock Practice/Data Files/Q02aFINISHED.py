# Print prompt and take country from user
country = input("Enter the country you're visiting from: ")
# Tell the user their country
print("You are from: ", country)
# Take number of adults in party from user
adults = int(input("Enter the number of adults in your party: "))
# Take number of children in party from user
children = int(input("Enter the number of children in your party: "))
# Calculate total number in party
total = children + adults
# Tell the user the total number of people in their party
print("The total in your party is: ", total)

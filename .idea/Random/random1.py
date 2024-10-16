scores = [["Hamad", 36, 15, 10],
          ["Cook", 45, 6, 12],
          ["CopeL", 32, 13, 15],
          ["Ahmed", 39, 9, 8],
          ["Moza", 36, 12, 13],
          ["Cutler", 30, 10, 19]]

search = input("What house would you like to search for? ").title()
found = False  # Variable to check if the house is found

# Iterate over the scores
for n in range(len(scores)):
    if scores[n][0] == search:  # Check if the first element (house name) matches the search
        index = n  # Store the index of the match
        found = True  # Mark as found
        break  # Exit the loop once found

if found:
    print(f"The scores for {scores[index][0]} are {scores[index][-3:]}.")
else:
    print(f"House {search} not found.")

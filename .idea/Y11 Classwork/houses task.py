#1. Print Hamad and it's Score2
#2. Print Moza and its score
#3. Print the Total for each house
#4. Print a separate table with House and all of its Score1
#5. Print the whole array as a table
#6. Ask the user which house they want and print it's score (CHALLENGE)

scores=[["Hamad",36,15,10],
        ["Cook",45,6,12],
        ["CopeL",32,13,15],
        ["Ahmed",39,9,8],
        ["Moza",36,12,13],
        ["Cutler",30,10,19]]

total=[0,0,0,0,0,0]
for i in range(6):
        total[i] = sum(scores[i][-3:])
#Task 1
print(scores[0][2])

#Task 2
print(scores[4],"\n")

#Task 3
for i in range(6):
        sumofscores = sum(scores[i][-3:])
        print(scores[i][0], sumofscores)
print("\n")

#Task 4 & 5
for i in range(6):
        sumofscores = sum(scores[i][-3:])
        print(f"{scores[i][0]} {scores[i][-3:]}")

#Task 6
search = input("What house would you like to search for? ").strip()
found = False
while found == False:
        for n in range(len(scores)):
                if scores[n][0].lower() == search.lower():
                        index = n
                        found = True
print(f"The scores for {scores[index][0]} are {scores[index][-3:]} with a total of {total[index]}. ")

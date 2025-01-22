# Q01g

storedLetter = "g"
letter = input("Input a letter ")
# Letter converted to lower case
letter = letter.lower()

# Amend the code by completing the if statement
if (letter) > (storedLetter):
    print(f"{letter} is later {storedLetter} in the alphabet.")
elif (letter) < (storedLetter):
    print(f"{letter} is earlier {storedLetter} in the aplhabet")
else:
    print(f"The inputted letter {letter}, is the same as the stored letter, {storedLetter}")
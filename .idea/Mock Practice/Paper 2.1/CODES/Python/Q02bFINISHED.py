# Q02b

# Write the function here
def checkPrime(pNumber):
    
# Write the main program here
    if pNumber == 1:
        check = False
    else:
        check = True
        for count in range(2, int(pNumber)):
            if int(pNumber) % count == 0:
                check = False
    return check

number = input("Enter a number: ")
result = checkPrime(number)
if result == True:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
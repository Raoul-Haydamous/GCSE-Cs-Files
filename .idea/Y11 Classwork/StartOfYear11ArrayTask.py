#RECAP

# Program 1: Write a program to add 5 names to the list below
def program1():
    names = []
    for i in range(5):
        ask = input('Give me a name. ')
        names.append(ask)
        (ask)
    print(names)



#Program 2: Write a program to add 3 animals to the list:

def program2():
    animals = ["","",""]
    for i in range(3):
        animals[i] = input('Give me an animal.')
    print(animals)

#Program 3: Write a program that adds 100 random numbers (Max value=200) to a list and it prints it
def program3():
    import random
    numbers = []
    for i in range(100):
        numbers.append(random.randint(0,200))
    print(numbers)

#Program 4: Extend program 3 and sort the list in ascending order
def program4():
    import random
    numbers = []
    for i in range(100):
        numbers.append(random.randint(0,200))
    numbers = sorted(numbers)
    print(numbers)

#Program 5: Extend program 3 and search if the number 109 is in the list
def program5():
    import random
    numbers = []
    for i in range(100):
        numbers.append(random.randint(0,200))
    numbers = sorted(numbers)
    print(numbers)
    find = 109 in numbers
    if find == True:
        print('Number',numbers.index(109),"in the sequence")
    else:
        print('109 not in sequence')

#Program6: Extend program 3 to find the Lowest Number
def program6():
    import random
    numbers = []
    for i in range(100):
        numbers.append(random.randint(0,200))
    numbers = sorted(numbers)
    find = 109 in numbers
    if find == True:
        print('Number',numbers.index(109),"in the sequence")
    if find == False:
        print('109 not in sequence')
    print(numbers[0],"is the smallest in sequence.")

#Program7: Extend program 3 to find the Highest Number
def program7():
    import random
    numbers = [109]
    
    for i in range(100):
        numbers.append(random.randint(0,200))
    numbers = sorted(numbers)
    
    num = 109
    if num in numbers:
        print('Number 109 in the sequence')
    else:
        print('109 not in sequence')
    
    print(numbers)
    print(numbers[0],"is the smallest in sequence.")
    print(max(numbers), "is the largest in sequence")

#Program 8: Extend program 3 to find the numbers that have duplicates
def program8():
    import random
    numbers = []
    
    for i in range(100):
        numbers.append(random.randint(0,200))
    numbers = sorted(numbers)
    
    num = 109
    if num in numbers:
        print('Number 109 in the sequence\n')
    else:
        print('109 not in sequence\n')
    
    print(numbers[1],"is the smallest in sequence.")
    print(max(numbers), "is the largest in sequence\n")
    
    dupes = []
    for i in range(1,len(numbers)):
        if numbers[i] == numbers[i-1] and numbers[i] not in dupes:
            dupes.append(numbers[i])
    print(f"These numbers are duplicates:{dupes}. \n \n This is the original array: {numbers}")
program8()
#Program 9:
#The program below allows a user to add temperatures for each month
#Write a program that allows a user to input temperatures for each month in the temperatures array
#Extend the program to print each month and it's related temp
#Find the Highest temperature and it's month
def program9():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    temperatures = [0]*12

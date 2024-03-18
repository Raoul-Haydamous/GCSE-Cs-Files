def task1():
    tt = 2
    count = 0
    while count <= 99:
        count = count+1
        tt2 = tt*count    
        print(tt2)

def task2():
    count = 0
    while count <= 999:
        count = count + 1 
        print('Hey \nBye')

def task3():
    count = 0 
    password = '123'
    while count <=4:
        pcheck = str(input('What is the password? '))
        if pcheck == password:
            print('Correct Password')
            count = count+5 #ends the program/breaks the loop
        if pcheck != password:
            print('incorrect password!')
            count = count +1 
            if count >= 4:
                print('LOCKED') #if statement inside the other if as it should only run when password is wrong
                count = count +5 #ends the program/breaks the loop

def task4():
    flag = False
    password = input("Make a password. ")
    while flag == False: 
        pcheck = input ('What is the password? ')
        if pcheck == password:
            flag = True

def task5():
    lenuser = 0 
    password = ''
    while lenuser < 7:
        username = input('What is your username.\n- Username must be 8 characters or more.')
        lenuser = len(username)
        if lenuser < 7:
            print('Username is less than 8 characters. \n Please input a new username.')
        elif lenuser > 7: 
            print('Your username has been accepted. ')
    while len(password) <8 or len(password) >15:
        password = input('What is your password?\n-Password must be between 8-15 characters.')
        lenpass = len(password)
        if lenpass < 8 or lenpass > 15:
            print('Invalid password, enter another password.')
    print("password has been accepted")

def task6():
    import random
    num = random.randint(1,100)
    ncheck = 0
    while ncheck != num:
        ncheck = int(input("Guess the number. "))
        if ncheck > num:
            print('Too high')
        if ncheck < num:
            print('Too low')
        if ncheck == num:
            print('Well Done')
            ncheck = num


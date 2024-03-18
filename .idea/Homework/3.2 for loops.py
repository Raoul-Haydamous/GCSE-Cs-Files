def t035():
    name = input('What is your name? ')
    for i in range(3):
        print(name)

def t036():
    name = input('What is your name? ')
    num = int(input('How many times do you want it displayed? '))
    for i in range(num):
        print(name)

def t037():
    name = input('What is your name? ')
    namelen = len(name)
    for i in range(0,namelen):
        print(name[i])

def t038():
    name = input('What is your name? ')
    amount = int(input('How many times do you want it printed. '))
    namelen = len(name)
    for n in range(amount):
        for i in range(0,namelen):
            print(name[i])

def t039():
    tt = int(input('What times tables do you want?'))
    tt2 = tt * 13
    for i in range(tt,tt2,6):
        print(i)

def t040():
    num = int(input('Give me a number lower than 50. '))
    if num <50:
        for i in range(50,num-1,-1):
            print(i)

def t041():
    name = input('What is your name? ')
    num = int(input('Give me a number. '))
    if num <10:
        for i in range(num):
            print(name)
    else:
        for i in range(3):
            print('Too high')

def t042():
    print('Total is 0. \nUse y for yes and n for no when answering questions. ')
    total = 0
    for i in range(5):
        num1 = int(input('Give me a number. '))
        veri1 = input(f"Do you want'{num1}to be included in the total?" ).lower()
        if veri1 == 'y':
            total = num1+total
        elif veri1 == 'n':
            pass
    else:
        print('invalid input')
    print(total)

def t043():
    dir = input('Which direction do you want to count up or down? ').lower()
    if dir == 'up':
        num = int(input('Until what number? '))
        for i in range(1,num+1):
            print(i)
    elif dir == 'down':
            num2 = int(input('Give me a num lower than 20. '))
            if num2 < 20:
                for i in range(20,num2-1,-1):
                    print(i)
    else:
        print('I dont understand')

def t044():
    inv = int(input('How many people do you want to invite? '))
    if inv < 10:
        for i in range(inv):
            ppl = input('What are the peoples names? ')
            print(ppl,' has been invited')
    elif inv >=10:
        print("Too many people. ")
    else:
        print('Invalid input')
t044()
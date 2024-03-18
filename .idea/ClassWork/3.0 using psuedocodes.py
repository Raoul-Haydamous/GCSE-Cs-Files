def task1():
    counter = 0
    score = 0 
    avg = 0
    scoresum = 0 

    while score != -1:
        score = int(input("Please enter next score, -1 to end. "))
        if score != -1:
            scoresum = scoresum+score
            counter = counter+1
    avg = scoresum/counter
    print(avg)

def task2():
    counter = 0
    while counter <= 100:
        counter = int(input('Put number bigger 100. '))

def task3():
    user = ''
    passw = ''
    checkU = '.'
    checkP = '.'
    
    while checkU != user or checkP != passw:
            print('They dont match')
    user = input('Username pls')
    while " " in user:
        user = input('username pls bas no space')
    passw = input(' pass pls')
    while " " in passw:
        passw = input('pass pls')
    
    checkU = input('What is ur user')
    checkP = input('What is ur pass')
    
    if checkU == user and checkP == passw:
        print('Match0')

        
            
task3()
import random

def p1():
    names = ['Ben','Thomas','John','Harry','Brian']
    age = [23,45,12,56,78]
    for i in range(len(names)):
        print(names[i],age[i])


def p2():
    names = ['Ben','Thomas','John','Harry','Brian']
    age = [23,45,12,56,78]
    for i in names:
        print(i)


def p3():
    names = ['Ben','Thomas','John','Harry','Brian']
    age = [23,45,12,56,78]
    search = input('Type a name. ')
    for i in range(len(names)):
        if search in names:
            print(True)
            break


def eg1():
    student = []
    for i in range(0,3):
        student.append(input('Enter a name. '))
    print(student)


def eg2():
    array = ['','','']
    for i in range(3):
        array[i]=input('Enter a name.')
    print(array)


def t1():
    array = [4,6,7,8,10]
    find = int(input('Which num would you like to find? '))
    if find in array:
        print("found!")


def t2():
    game = []
    for i in range(4):
        game.append(input('Enter a game.'))
    print(game)


def t3():
    import random
    number = []
    for i in range(0,30):
        number.append(random.randint(0,1000))
    print(number)


def ext1():
    names = ['','','','','']
    score = []
    for i in range(5):
        names[i]=input('Enter a name. \n ')
        score.append(input('What is their score? \n '))
    search = input('Give me a user and ill tell you their score. ')
    for index in range(5):
        if search == names[index]:
            print(names[index], score[index])
    if search not in names:
        print('That is not a listed user.')


def ext2():
    score = 0
    while True:
        array = []

        for i in range(50):
            array.append(random.randint(1,100))
        print(array)
        for n in range(5, 0, -1):
            
            if n == 1:
                search = int(input(f"50 random numbers have been added ranging 1-100, try and guess one of them, you have {n} chance left. "))
            
            else:
                search = int(input(f"50 random numbers have been added ranging 1-100, try and guess one of them, you have {n} chances left. "))
            
            if search not in array:
                print(f"{search} isn\'t in the list.")
            
            else:
                print('You got it right! +1 added to score')
                score += 1
                break

        print('Your total score is', score)
        
        retry = input('Would you like to try again(y/n)? ').lower()
        
        if retry != 'y':
            print('ok')
            break
ext2()
#fully done and cleaned up
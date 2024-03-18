import random
def task2():
    cp = "HC&dt2016"
    numchars = len(cp)
    index1 = int(random.randint(0, numchars - 1))
    index2 = int(random.randint(0, numchars - 1))
    index3 = int(random.randint(0, numchars - 1))
    print(f"please enter characters {index1 + 1},{index2 + 1},{index3 + 1} from your password")
    check1 = input('Press enter after each one.')
    check2 = input('')
    check3 = input('')
    if check1 == cp[index1] and cp[index2] and cp[index3]:
        print('Welcome')
    else:
        print('Retry')
        while True:
            print(f"please enter characters {index1 + 1},{index2 + 1},{index3 + 1} from your password")
            check1 = input('Press enter after each one.')
            check2 = input('')
            check3 = input('')
            if check1 == cp[index1] and cp[index2] and cp[index3]:
                print('Welcome')
                break
#task2()
def task3():
    yr = int(input('Give me any year and ill tell you if its a leap year or not. '))
    if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
        print('Its a leap year. ')
    else:
        print('It is not a leap year')
#task3()

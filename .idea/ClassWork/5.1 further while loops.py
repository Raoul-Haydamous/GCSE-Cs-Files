def task1():
    import random
    flag = False
    num = random.randint(1,10)
    count = 0 
    print(num)
    while flag == False:
        ncheck = int(input("What is the number? "))
        if ncheck != num:
            count += 1 
            print(count)
        if ncheck == num:
            count += 1
            if count == 1:
                print(f'Correct\nIt took you {count} guess.')
                flag = True
            else:
                print(f'Correct\nIt took you {count} guesses.')
                flag = True

def task2():
    print('***Y for yes N for no***')
    hflag = False
    while hflag == False:
        hw = input('Have you done your homework? ').lower()
        if hw == 'y' or hw == 'n':
            hflag = True
        else:
            print('Invalid input, try again. ')
    dflag = False
    while dflag == False:
        dinner = input('Have you ate your dinner? ').lower()
        if dinner == 'y' or dinner == 'n':
            dflag = True
        else:
            print('Invalid input, try again. ')
    if hw == 'y' and dinner == 'y':
        print('You can play Xbox')
    elif hw == 'y' and dinner == 'n':
        print('You must eat dinner first before you can play Xbox. ')
        dflag = False
    elif hw == 'n' and dinner == 'y':
        print('You must do your homework first before you can play Xbox. ')
        hflag = False
    elif hw == 'n' and dinner == 'n':
        print('You must do your homework and eat dinner first then you can play Xbox. ')
        dflag = False
        hflag = False
    else:
        print('invalid input')

def task2_chatgpt():    
    print('***Y for yes N for no***')
    hw_done = False
    dinner_done = False
    while not (hw_done and dinner_done):
        if not hw_done:
            hw = input('Have you done your homework? ').lower()
            if hw == 'y':
                hw_done = True
            elif hw == 'n':
                print('You must do your homework first before you can play Xbox. ')
            else:
                print('Invalid input, try again. ')
        
        if not dinner_done:
            dinner = input('Have you eaten your dinner? ').lower()
            if dinner == 'y':
                dinner_done = True
            elif dinner == 'n':
                print('You must eat dinner first before you can play Xbox. ')
            else:
                print('Invalid input, try again. ')
    print('You can play Xbox')

def task3():
    responce = None
    len = float(input('What is the length of your rectangle? '))
    width = float(input('What is the width of your rectangle? '))
    unit = input('What is your unit of measurement? ')
    while responce not in ('a','A','P','p'):
        responce = input('Do you want perimeter(p) or area(a)? ').lower()
        if responce == 'a':
            area = len*width
            print(f"Area = {area} {unit}")
        elif responce == 'p':
            peri = (len*2)+(width*2)
            print(f"Perimeter = {peri} {unit}")
task3()
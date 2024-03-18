def t1():
    temp = int(input('What is the temp? '))
    if temp >30:
        print('Too Hot')
    elif temp >21 and temp <=30:
        print('Just right')
    else:
        print('Chilly')

def t2():
    price = 0
    size = input('Type size letter or large letter')
    weight = int(input('What is the weight'))
    type = input('Type?')
    if size == 'letter' and weight <=100:
        price = 1.65
        print(price)
        if type == 'first class':
            price = price+2.90
            print(price)
    if size == 'large letter':
        if weight>= 250:
            price = 2.37
            print(price)
            if type == 'first class':
                price = price + 2.90
                print(price)
        elif  weight >= 100:
            price = 1.95
            print(price)
            if type == 'first class':
                price = price + 2.90
                print(price)
        else:
            price = 2.81
            print(price)

def ext():
    import random
    score = 0
    p1dice1 = random.randint(1, 6)
    p1dice2 = random.randint(1, 6)
    p1total = 0
    print('the 2 dice',p1dice1,p1dice2)
    if p1dice1 != p1dice2:
        p1total = p1dice1+p1dice2
        print('the total is',p1total)
    if p1dice1 and p1dice2 == 6:
        p1total = 0
        print('the total is',p1total)
    if p1dice1 == p1dice2:
        p1total == p1total*2
        print('the total is',p1total)

ext()
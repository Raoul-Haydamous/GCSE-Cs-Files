def p1():
    for i in range(5):
        print(i,'salam')
def p2():
    for i in range(2,5):
        print(i,'salam')
def p3():
    for i in range(0,100,5):
        print('Hello',i)
def p4():
    for i in range(100,5,-5):
        print(i,'hello')
def p5():
    for i in range(3):
        name = input("Type name: ")
        print(name)
def p6():
   for i in range(5):
       print('Inside loop...')
       for j in range(3):
           print('Outside loop...')
def p7():
    tt = int(input('Which times tables do you want? '))
    tt2 = int(input('Until which table? ')) # asks until which table e.g 6 times tables up to 12
    tt3 = tt2+1 #makes it give accurate results in python as if the limit is 12 it will only go till 11
    tt_limit = tt * tt3 #gives the maximum number the tt should go up to, i.e 6 x 12 = 72, 72 is max
    for i in range(1,tt3):
            print(f'{tt} x {i} = {tt*i}')
#1/11/23 - After Holiday 3.0
def q1():
    for i in range(1,101):
        print(i)

def q2():
    for i in range(100,0,-1):
        print(i)

def q3():
    tt = int(input('Which times tables do you want? '))
    tt2 = 11
    for i in range(1,tt2):
            print(f'{tt} x {i} = {tt*i}')

def q4():
    hello = int(input('How many times do you want hello to be printed? '))
    for i in range(1,hello+1):
        print('hello')

def q5():
    hello = int(input('How many times do you want y/n to be printed? '))
    name = input("what is your name? ")
    for i in range(1,hello+1):
        print(name)

def q5v2():
    word = input('Enter any word. ')
    for i in word:
        print(word)
q5v2()
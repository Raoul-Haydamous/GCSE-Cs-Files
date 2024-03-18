def p1():
    mystr = input('Please enter the text. ')
    for i in range(0,len(mystr)):
        number = ord(mystr[i])
        print(number)
def p2():
    import random
    mystr = ''
    for i in range(0,250):
        num = int(input('Please enter a number in the range '
              '65 to 90 or in the range 97 to 122. '))
        char = chr(num)
        mystr = mystr+char
        print(mystr)

def p3():
    import random
    mystr = ''
    for i in range(0,1000):
        randomnum = random.randint(35,10000)
        print(chr(randomnum))
    while True:
        finder = input('Find the id of a chr. ')
        finder2 = int(input('Find a chr using the id. '))
        print(ord(finder))
        print(chr(finder2))
p3()
def task1():
    name = input("Type a name. ")
    firstchr = name[0]
    lastchr = name[-1]
    midchr = name[int(len(name)/2)]
    print(firstchr,midchr,lastchr)

def task2():
    name1 = input('What is your first name? ')
    name2 = input('What is your surname? ')
    print(name1,name2)

def task3():
    import random
    animal = input('Name me any animal. ')
    print(animal+str(random.randint(1,99)))
def task4():
    email = input('Give me an email address. ')
    print(email.replace('@'," \n"))

def task5():
    thing = input('Tell me anything. ')
    print(thing[-1::-1])
task1()
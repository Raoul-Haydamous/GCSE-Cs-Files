def task1():
    num1 = int(input('Give me a number. '))
    num2 = int(input('Give me another number. '))
    if num1 > num2:
        print(f'{num1} is bigger. ')
    elif num1 < num2:
        print(f'{num2} is bigger. ')
    else:
        print(f'{num1} is equal to {num2}')

def task2():
    num1 = int(input('Give me a number. '))
    if num1 <= 20:
        num1 = num1*2
        print(num1)
    elif num1 > 20 and num1 <= 30:
        num1 = num1*3
        print(num1)
    elif num1 >30:
        num1 = num1 *4
        print(num1)

def task3():
    count = 0 
    total = 0
    
    for count in range(0,10):
        mark = int(input('What is your mark? '))
        total = total + mark
        count = count + 1
    avg = total/10
    print(f'The average mark is: {avg}')

def task4():
    rate = 25.0
    tax = 0.15
    numberOfHours = 0
    while numberOfHours <= 1:
        numberOfHours = float(input('How many hours did you work? '))
        WageBeforeTax = rate*numberOfHours
        taxAmount = tax*WageBeforeTax
        wageAfterTax = WageBeforeTax-taxAmount
    print(f'The hourly rate is{rate}$ \nYour money wage before tax is {WageBeforeTax}$ \nYour wage after tax is {wageAfterTax}$')
task4()
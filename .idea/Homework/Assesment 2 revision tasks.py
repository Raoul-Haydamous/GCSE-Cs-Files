def t1():
        
    nums = []
    
    for i in range(5):
        appendnum = int(input("Give me 5 numbers to put into the list: "))

        nums.append(appendnum)
    
    total = sum(nums)
    print(total)

    smallest = min(nums)
    print(smallest)

    biggest = max(nums)
    print(biggest)

    print(f"The numbers in the array are {nums}.\nThe total of the nums is {total}\n" 
          f"The smallest number is {smallest}.\nThe biggest number is {biggest}.")

def t1_improved():
    
    nums = []
    add = int(input("How many numbers would you like to add to the list? "))
    for i in range(add):
        if add-i == 1:
            appendnum = int(input(f"Give me {add-i} number to put into the list: "))
        else:
            appendnum = int(input(f"Give me {add-i} numbers to put into the list: "))
        nums.append(appendnum)
    
    total = sum(nums)

    smallest = min(nums)

    biggest = max(nums)

    multi = 1
    for i in nums:
        multi *= i

    
    print(f"The numbers in the array are {nums}.\nThe total of the nums is {total}\n" 
          f"The smallest number is {smallest}.\nThe biggest number is {biggest}."
          f"\nThe numbers multiplied together is {multi}")

def t2():
    
    pay = int(input('How many hours did you work this week? '))
    gpay = pay*12.50
    print(gpay,'gp')
    
    if gpay > 500:
        gpay = gpay*0.8
        rounded = round(gpay,2)
        print(f'Your net pay is {rounded}')
    
    else:
        gpay=gpay*0.85
        rounded = round(gpay,2)
        print(f'Your net pay is {rounded}')

def t3():
    
    adults = int(input('How many adults are there in your party? '))
    kids = int(input('How many children are there in your party? '))
    
    adu_bill = (adults*60)+(adults*210)
    chi_bill = (kids*20)+(kids*110)
    
    holiday_cost = adu_bill+chi_bill
    print(f'The total holiday cost is ${holiday_cost}.')

def t4():
    import random
    
    highest = 0
    
    colors = ['Red','Blue','Green']
    count = ['','','']
    for i in range(3):
        count[i] = random.randint(1,25)
    
        if count[i] > highest:
            highest = count[i]
    
    print(colors)
    print(count)
    print(highest)


t4()
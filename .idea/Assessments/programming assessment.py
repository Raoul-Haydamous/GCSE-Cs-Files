def task1():
    weeknumber = ['-6','-5','-4','-3','-2','-1']
    staffrates = [105,110,115,120,125,130]
    goodinput = False
    
    while goodinput == False:
        currentcount = int(input('Please enter the number of staff on week -7. '))
        if currentcount >= 200:
            goodinput = True
            print("Staff on week -7 is", currentcount)
        else:
            print("invalid input")
    
    for i in range(0,(len(weeknumber)-1)):
        percentage = staffrates[i]/100
        neededstaff = currentcount*percentage
        print(f"Week {i} needs {round(neededstaff,0)} staff. ")

def task2():
    check = True
    weights = []
    while check == True:
        weight = int(input('What is the weight of the item. 0 to quit: '))
        if weight == 0:
            check = False
        if weight != 0 and weight > 0:
            print(weight)
            weights.append(weight)
        if weight < 0:
            print('Invalid weight')
    maximum = max(weights)
    minimum = (min(weights))
    print(f"The heaviest item is {maximum} and the lightest is {minimum}.")

def task3():
    name = ["", "", ""]
    total = [0,0,0]
    averageMark = [0,0,0]
    
    mark = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]]
    for i in range(3):
        name[i] = input("What is the name of your student? ")
        for n in range(5):
            mark[i][n] = int(input("What are the marks for the student? "))
            total[i] = sum(mark[i])
            averageMark[i] = total[i]/5
    print(name)
    print(mark)
    print(total)
    print(averageMark)

def t1():
    total = 0
    count = 0
    for count in range(1000):
        total = total + count
        print(total)

def flowchart2python():
    weeklytot = 0
    mealCost = float(input('What is the the cost of a meal? '))
    drinkCost = float(input('What is the cost of a drink? '))
    weeklytot = ((drinkCost*2)+mealCost)*5
    print(round(weeklytot,2))
flowchart2python()
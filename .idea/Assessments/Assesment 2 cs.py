def task1():
    
    print('Welcome to Qatar Cinema')
    price = 0
    names = input("What is your fullname(first name and surname)? ")
    age = int(input('How old are you? '))

    if age < 12:
        print('You cannot view a movie on your own')


    tickets = int(input('How many tickets do you require? '))

    if age >= 12:
        if age <= 18:
            price = 26    
        else:
            price = 35

    total_tickets = tickets*price
    
    print(f'{ names[:names.index(' ')] }, 1 ticket is {price}QAR, you bought {tickets} ticket(s) and the total price is {total_tickets}QAR')

def task2():
    print('Welcome, this is a house ranking calculator. ')

    houses = ['Hamad','Cutler','Moza','Cook','Ahmed','Copeland']
    
    event1 = []
    event2 = []
    event3 = []
    print(len(houses))
    
    for n in range(len(houses)):
            event1.append(int(input(f'Enter score for {houses[n]} House in Event 1: ')))
            event2.append(int(input(f'Enter score for {houses[n]} House in Event 2: ')))
            event3.append(int(input(f'Enter score for {houses[n]} House in Event 3: ')))
    
    search = input('Type the house you want the scores to be displayed. ')
    find = houses.index(search)

    total = event1[find]+event2[find]+event3[find]
    print(total)
    average = total/3

    print(f'{houses[find]} Scores: \n Event 1: {event1[find]} \n Event 2: {event2[find]} \n Event 3: {event3[find]} \n '
          f'Total = {total} \n Average = {average} ')
    
task1() 
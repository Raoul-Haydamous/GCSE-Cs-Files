def array1():
    simple_array = [[2,3,6],
                    [5,7,8],
                    [7,2,9]]
    print(simple_array[0]) #prints the first array
    print(simple_array[0][1]) #prints the second number in the first array

    row = int(input('Type a row 0-2. '))
    column = int(input('Type a column 0-2. '))
    print(simple_array[row][column])

def array2():
    array = []
    
    for row in range(10):
        array.append([])
        for i in range(10):
            array[row].append(0)
    
    array2 = []
    array2 = [[0 for i in range(10)]for j in range(10)]
    print(array2)

def array3():
    
    #Finding the total and avg scores of these students
    #Name score1 score2 score3 score4 score5
    #Student 1 = 12 14 8 7 17
    
    #Student2 = 15 17 10 5 12
    
    #Student3 = 17 18 3 9 8
    
    #Find the total for each student and append it.
    #Find the avg score of each student
    
    mark = [[12,14,8,7,17],
            [15,17,10,5,12],
            [17,18,3,9,8]]
    
    total = [0,0,0]
    average = [0,0,0]
    
    for row in range(3):
        for column in range(5):
            total[row] = total[row]+mark[row][column]
            average[row] = total[row]/5
    
    print(total)
    print(average)
    

def array4():
    houses=["Hamad","Ahmed","Cutler","Cook","Copeland","Moza"]
    scores=[]
    total=[0,0,0,0,0,0]
    count = 0
    for house in range(6):
        for event in range(3):
            scores.append(int(input(f"What are the scores for {houses[house]}? ")))
            count = count+1
            if count == 3:
                total[house] = sum(scores[-3:])
                count = 0
        print(f"{houses[house]} scores were:{scores[-3:]} ")
                
    print(scores)
    print('The totals are:')
    for i in range(6):
        print(f"{houses[i]}: {total[i]}")

def array4v2():
    houses=["Hamad","Ahmed","Cutler","Cook","Copeland","Moza"]
    scores=[]
    total=[0,0,0,0,0,0]
    count = 0
    #eventscore tracks the last 3 scores inputted so it can be added up to total for each house
    
    for i in range(6):
        scores.append([])
        #adds six arrays, one for each house so each houses event scores can be tracked
        for j in range(3):
            count = int(input(f"What are the scores for {houses[i]} house? "))
            scores[i].append(count)
            #finds the scores and adds it to the array
            total[i] = sum(scores[i])
            #when the scores for the first house are found its added and put into the totals array
        
    for b in range(6):
        print(f"{houses[b]} Total: {total[b]} \n{houses[b]} Scores: {scores[b]}")
        #prints the scores and totals for each house

    search = input("What houses score would you like to search for? ").title()
    index = houses.index(search)
    #finds the number value of the selected house in the array  
    
    print(f"The total for {houses[index]} is {total[index]}. \n The scores for {houses[index]} were {scores[index]}. ")
array4v2()

def multiply(x,y):
    answer = x*y
    return answer 

def add(x,y,z):
    answer = x+y+z
    return answer

def avg(start, end):
    total = 0 
    for i in range(start, end+1):
        total = total + i
        print(total)
    answer = total/((end+1)-start)
    return answer

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(avg(num1, num2))

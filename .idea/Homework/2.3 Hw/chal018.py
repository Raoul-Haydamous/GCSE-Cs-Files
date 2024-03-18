num1 = int(input('Enter a number. '))
if num1 < 10:
    print('Too low.')
elif num1 in range(10,21):
    print('Correct')
else:
    print('Too High')
Q1 = input('Is it raining? ').lower()
if Q1 == 'yes':
    Q2 = input('Is it windy? ').lower()
    if Q2 == 'yes':
        print('Its too windy for an umbrella.')
    elif Q2 == 'no':
        print('Take an umbrella.')
elif Q1 == 'no':
    print('Enjoy your day. ')
else:
    print("That isnt a valid response, I cannot help you. ")
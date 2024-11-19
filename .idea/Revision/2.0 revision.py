def sec21():
    age = 0 
    while age < 18:
        name = input("What is your name? ")
        age = int(input("How old are you? "))
        ID = name[0:2]+str(age)
        if age < 18:
            print("You are underage please re-enter details. ")
        if age >= 18:
            print(f"You are due for an id card \n  Name: {name} \n Age:{age} \n ID:{ID.lower()}")
def sec22():
    count = 0 
    guesses = 3
    correct = "letmein"
    
    while count < 3:
        guess = input(f"Guess the password, you have {guesses} guesses left. ")
        
        if guess == correct:
            print('Correct')
            count = 4
        if guess != correct:
            count += 1
            guesses-=1
            print(f"Wrong! You have {guesses} guesses left.")
            if count >= 3:
                print("Time out")

def sec231():
    print("Weclome! This is a currency converter program! ")
    
    PtQ = 4.45
    QtP = 0.22
    name = input('What is your name?')
    conv = input('What currency do you want to convert into? (GBP/QAR)').lower()
    amt = int(input('How much do you want to convert?'))
    money = 0
    
    correct = ""
    check = input(f'Are all your details correct? (Y/N) \nName: {name} \nNew Currency:{conv} \nAmount:{amt} \n ').lower()
    if check == "n":
        correct = "n"
    if check == "y":
        if conv == "gbp":
            money = amt*QtP
            print(f"Name: {name}\nCurrency From: QAR \nCurrency To: GBP\nCurrency Rate:{QtP}\nAmount:{amt}\nExchange Amount:{money}")
        if conv == "qar":
            money = amt*PtQ
            print(f"Name: {name}\nCurrency From: QAR \nCurrency To: GBP\nCurrency Rate:{PtQ}\nAmount:{amt}\nExchange Amount:{money}")
    
    while correct == "n":
        print('Please re-enter your details. ')
        name = input('What is your name?')
        conv = input('What currency do you want to convert into? (GBP/QAR)')
        amt = int(input('How much do you want to convert?'))
        check = input(f'Are all your details correct? (Y/N) \nName: {name} \nNew Currency:{conv} \nAmount:{amt} \n ').lower()
        if check == 'y':
            correct = " "
    if check == 'y':
        if conv == "gbp":
            money = amt*QtP
            print(f"Name: {name}\nCurrency From: QAR \nCurrency To: GBP\nCurrency Rate:{QtP}\nAmount:{amt}\nExchange Amount:{money}")
    if conv == "qar":
        money = amt*PtQ
        print(f"Name: {name}\nCurrency From: QAR \nCurrency To: GBP\nCurrency Rate:{PtQ}\nAmount:{amt}\nExchange Amount:{money}")
        correct = ""
sec231()
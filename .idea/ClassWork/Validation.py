def lencheck():
    while True:
        password = input('What is your password? ')
        if len(password) < 8:
            print("Too Short")
        if len(password) >= 8:
            print('Valid')
            return False

def presencecheck():
    while True:
        name = input('Give me a name. ')
        if len(name) == 0:
            print("No name entered, try again. ")
        else:
            print("Thanks")
            return False

def typecheck():
    while True:
        try:
            age = int(input("How old are you. "))
        except ValueError:
            print("Not a number, try again. ")
        else:
            print("Thanks")
            return False

def prescheck():
    while True:
        email = input("What is your email. ")
        if "@" in email:
            print("Valid Email")
            return False
        else:
            print("Invalid Email")

def rangecheck():
    while True:
        try:
            charge = int(input("What battery percent is your phone at? "))
        except ValueError:
            print("Invalid Answer. Try again.")
            
        else:
            if charge in range(0,101):
                print('Thank You')
                return False
            else:
                print("Invalid Answer. Try Again. ")

def dividebyzero():
    
    while True:
        nums = []
        try:
            for i in range(2):
                nums.append(int(input("Give me a number. ")))
        except ValueError:
            print("That is not a number. ")
            
        else:
            try:
                result = nums[0]/nums[1]
            except ZeroDivisionError:
                print("I cannot divide by zero, perahps you typed in the second number as zero.")
            else:
                print(result)
                return False

def activityH():

    while True:
        check1 = 0
        check2 = 0
        check3 = 0
        check4 = 0
        names = ["Name",'Email','Age']
        data = []
        
        while check1 == 0:
            name = input("What is your name? ")
            if any(char.isdigit() for char in name) or len(name)== 0:
                print("Invalid. Perhaps you typed in a number? ")
            else:
                data.append(name)
                check1 = 1
        
        while check2 == 0:
            email = input("What is your email. ")
            if "@" not in email:
                print("Invalid Email")
            else:
                data.append(email)
                check2 = 1
        
        while check3 == 0:
            try:
                age = int(input("How old are you. "))
            except ValueError:
                print("Not a number, try again. ")
            else:
                data.append(age)
                check3 = 1
        
        print(f"---------------\nName: {name} \nEmail: {email} \nAge: {age}\n---------------")
        
        while check4 == 0:
            valid = input('Is your data correct?').lower()
            if valid == 'y' or valid == 'yes':
                print("Ok")
                check4 = 1
                return False
            
            elif valid == 'n' or valid == 'no':
                check1 = check2 = check3 = 0
                check4 = 1
            else:
                print('invalid input')

activityH()

def activityH_GPT():
    
    #Put my code into ai to see how it can be improved and to add comments for explination
    
    while True:
        # Initialize checks at the start of each loop
        check1 = check2 = check3 = check4 = 0
        names = ["Name", "Email", "Age"]
        data = []

        # Collect and validate the name
        while check1 == 0:
            name = input("What is your name? ")
            if any(char.isdigit() for char in name) or len(name) == 0:
                print("Invalid. Perhaps you typed in a number?")
            else:
                data.append(name)
                check1 = 1

        # Collect and validate the email
        while check2 == 0:
            email = input("What is your email? ")
            if "@" not in email:
                print("Invalid Email")
            else:
                data.append(email)
                check2 = 1

        # Collect and validate the age
        while check3 == 0:
            try:
                age = int(input("How old are you? "))
            except ValueError:
                print("Not a number, try again.")
            else:
                data.append(age)
                check3 = 1

        # Print the collected data
        print(f"---------------\nName: {data[0]} \nEmail: {data[1]} \nAge: {data[2]}\n---------------")

        # Confirm the correctness of the data
        while check4 == 0:
            valid = input("Is your data correct? (y/n): ").lower()
            if valid in ('y', 'yes'):
                print("Ok")
                return  # Exit the function when data is confirmed
            elif valid in ('n', 'no'):
                # Reset checks to re-enter the information
                check1 = check2 = check3 = 0
                check4 = 1  # Break out of the confirmation loop
            else:
                print("Invalid input. Please type 'y' or 'n'.")



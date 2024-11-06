def activityH():
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

activityH()

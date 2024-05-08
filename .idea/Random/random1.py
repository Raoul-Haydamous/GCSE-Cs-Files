import keyboard

def perform_action():
    print("Enter was pressed!")
    # Perform your action here

while True:
    if keyboard.is_pressed('enter'):
        perform_action()
        # Optional: You can break the loop if you only want the action to occur once
        # break

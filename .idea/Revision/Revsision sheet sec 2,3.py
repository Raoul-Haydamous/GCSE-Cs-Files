import keyboard

player = input('What do you want your name to be?')
def sec23():
    import random
    import time
    #sets a basic standard for future variables
    skills = ["Pace","Shot","Pass","Dribble","Defending","Physique"]
    Pscore = 0
    CPUscore = 0
    #stats of the computer
    cpuskills = ["Pace","Shot","Pass","Dribble","Defending","Physique"]
    cpustats = []
    #stats of the player
    pskills = ["Pace","Shot","Pass","Dribble","Defending","Physique"]
    pstats = []
    
    
    cpu = "CPU"
    #generates a random critera for each skill for the cpu
    for i in range(len(cpuskills)):
        rand = random.randint(50,100)
        cpustats.insert(i,rand)
    
    #generates a random critera for each skill for the player*
    for i in range(len(pskills)):
        rand = random.randint(50,100)
        pstats.insert(i,rand)
    
    #randomly picks one of the skills to judge
    rand = random.choice(skills)
    jskill = skills.index(rand)
    
    #compares the stats
    currentPstat = (pstats[jskill])
    currentCPUstat = (cpustats[jskill])
    if currentCPUstat > currentPstat:
        CPUscore = CPUscore + 1
        if currentCPUstat < currentPstat:
            Pscore = Pscore + 1
    if currentCPUstat == currentCPUstat:
        CPUscore = CPUscore + 0
        Pscore = Pscore + 0
    if rounds == 0:
        print("---------------------------------------------------------------------------------------------------------------------------")
    
    print(f"{currentPstat} is your {rand} score.")
    time.sleep(1)
    
    print(f"{currentCPUstat} is the CPUs {rand} score. ")
    time.sleep(1)
    
    print("---------------------------------------------------------------------------------------------------------------------------")

    
    
    
    if rounds >= 9:
        if CPUscore > Pscore:
            print(f"The CPU wins with {CPUscore} points total!!")
        elif CPUscore < Pscore:
            print(f"{player} wins with {Pscore} points total!!")
        else:
            print('Its a draw!')
rounds = 0
print("Press enter to start!")
while True:
    if keyboard.is_pressed('enter'):
        while rounds <=9:
            sec23()
            rounds+=1
    if rounds >= 9:
        break
#PROGRAM DOSENT WORK
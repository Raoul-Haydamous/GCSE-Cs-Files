def game1():
    import random
    print("Welcome to blackjack! I'm the dealer. \n The Rules: \n 21 Means Black Jack \n Over 21 and you Lose \n If nobody gets 21, the closest one wins. ")
    phand = [] #Cards of the player
    bhand = [] #Cards of the bot
    
    for cards in range(2):
        phand.append(random.randint(1,11))
        bhand.append(random.randint(1,11))
    
    print(f'This is your hand:{phand} \n My hand is {bhand[1]},{hidden}, I have {bhlen} cards total. ')
    #assigns the first two numbers to each player
    
    check = 'hit'
    hos = ''
    #hit or stand
    
    while check == 'hit'.lower():
        hos = input("Hit or stand? ").lower()
        if hos == 'hit':
            phand.append(random.randint(1,11))
    #asks the player if they want a card or not and adds it to their cards
    
        pht = sum(phand) 
        bht = sum(bhand)
    #player/bot hand total, finds the total of the cards
    
        hlen = len(bhand[1:])
        hidden = []
    #calculates how many of the bots cards should be hidden from the player
    
        bhlen = len(bhand)
        phlen = len(phand)
    #finds the total amount of cards each player has
    
        for i in range(hlen):
            hidden.append("?")
    #displays the hidden cards as ?
    
        print(f'This is your hand:{phand} \n My hand is {bhand[1]},{hidden}, I have {bhlen} cards total. ')
    


game1()
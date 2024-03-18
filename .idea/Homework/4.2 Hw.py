def t1():
    div7 = []
    div5 = []
    div75 = []

    for i in range(1500,2701):
        if i%7 == 0:
            div7.append(i)
        elif i%5 == 0:
            div5.append(i)
    div75 = div7,div5
    print(div75)

def t2():
    patterntop = '* '
    for i in range(0,5,1):
        print(patterntop*i)
            
    patterntop = '* '
    for i in range(5,0,-1):
        print(patterntop*i)

def t3():
    while True:
        word = input('Give me a word. ')
        leng = len(word)
        print(word[::-1])

def t4():
    wordList = ["tension", "hiccup", "faint", "pile", "behave", "freeze", "trend",
                 "minister", "fax", "average", "suburb", "provision", "recover", "rider",
                   "revenge", "constant", "pupil", "brave", "test", "liberal", "runner", "race", "heart", "cow"]
    letter = str(input('Give me a letter: '))
    count = 0
    for i in wordList:
        if letter in i[0]:
            count += 1
            print(i)
    print(count)

def t4ext():
    wordList = ["tension", "hiccup", "faint", "pile", "behave", "freeze", "trend",
                 "minister", "fax", "average", "suburb", "provision", "recover", "rider",
                   "revenge", "constant", "pupil", "brave", "test", "liberal", "runner", 
                   "race", "heart", "cow"]
    word = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    consonants = [
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
    'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'
    ]
    print(wordList)
    
    search = input('Pick a word from the list: ')
    
    if search in wordList:
        for i in search:
            if i in vowels:
                print(f'{i} is a vowel.')
            elif i in consonants:
                print(f'{i} is a consonant. ')
    else:
        print('Thats not in the list. ')

def t5():
    word = input('Type any word/phrase: ')
    if word[0:] == word[::-1]:
        print('This word/phrase is a palindrome. ')
    else:
        print('This word/phrase is not a palindrome. ')

def t6():
    import random

    array = []
    even = []
    odd = []
    
    for i in range(50):
        array.append(random.randint(0,1000))
    
    for i in array:
        if i%2 ==0:
            even.append(i)
        if i%2 !=0:
            odd.append(i)
    total = sum(array)
    print(f'Evens: {even}\n Odds: {odd}\n Total: {total} \n Original array: {array}')
    search = int(input('Give me a number from the sequence and ill tell you its position. '))
    print(array.index(search))
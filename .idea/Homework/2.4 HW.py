def chal20():
    name = input('What is your name? ')
    print(len(name))
def chal21():
    name1= input('What is your first name?')
    surname = input('What is your surname?')
    print(name1,surname,len(surname+name1))

def chal22():
    name1 = input('Type your first name in lower case.')
    surname = input('Type your surname in lowe case.')
    print(name1.title(),surname.title())

def chal23():
    nurse = input('Give me the first line of any nursey rhyme.')
    nurselen = len(nurse)
    print(nurselen)
    nurselen2 = int(input('Give me a starting number within the range 0 to '+str(nurselen)+'.'))
    nurselen3 = int(input('Give me a ending number within the range 0 to '+str(nurselen)+'.'))
    print(nurse[nurselen2:nurselen3])

def chal24():
    wrd = input('Type any word.')
    print(wrd.upper())

def chal25():
    name1 = input('What is your first name?')
    name12 = len(name1)
    if name12 < 5:
        surname = input('What is your surname?')
        print(name1.upper()+surname.upper())
    elif name12 >= 5:
        print(name1.lower())

def chal26():
    wrd = input('Give me a word.')
    consonants = 'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'
    if wrd[0] in consonants:
        print(wrd[1:]+wrd[0]+"ay")
    else:
        print(wrd+'way')

def chal27():
    password = input('Make a password.\n It must include the following: \n Atleast 1 uppercase letter \n Atleast 1 lowercase letter \n be a minimum of 8 characters. ')
    upper = 0
    lower = 0
    if upper >=1 in password:
        print('dddd')
def chal28():
    print()

chal28()
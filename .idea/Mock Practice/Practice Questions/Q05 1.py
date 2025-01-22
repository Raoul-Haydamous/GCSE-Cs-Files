#Q05FINISHED

libraryRecord =  [
["105MS" , "Marcus" , "Smith" , 25 ],
["103AZ" , "Anthony" , "Zarrent" , 5 ],
["108MW" , "Matt" , "White" , 12 ],
["112DB" , "Denise" , "Bilton" , 58 ],
["124MK" , "Malcolm" , "Kelly" , 26 ],
["116UK" , "Uzere" , "Kevill" , 29 ],
["127AL" , "Abduraheim" , "Leahy" , 94 ],
["124LS" , "Laura" , "Sampras" , 50 ],
["121AP" , "Azra" , "Potter" , 61 ],
["115AC" , "Anthony" , "Calik" , 10 ],
["117PI" , "Pablo" , "Iilyas" , 49 ],
["113MM" , "Mark" , "Montgomerie" , 68 ],
["130FH" , "Felicity" , "Heath" , 11 ],
["132JA" , "Jill" , "Alexander" , 61 ],
["123SG" , "Sara" , "Grimstow" , 9 ],
["134KD" , "Kevin" , "Dawson" , 74 ],
["122AB" , "Andrew" , "Bertwistle" , 42 ],
["125JF" , "Jaide" , "Feehily" , 55 ],
["128JS" , "Justin" , "Slater" , 68 ],
["126CG" , "Colleen" , "Grohl" , 39 ]
]
# ----------------------------------------------
# Write your code below this line

# Stores the number of books read and num of books read <10:
books = []
less_than_10 = []

#Stores the winners of gold silver and bronze 
gold = []
silver = []
bronze = []

for i in range(len(libraryRecord)):
    #calculates the total amount of books:
    count = libraryRecord[i][3]
    books.append(count)
    
    #finds which students have read <10 books:
    if libraryRecord[i][3] <10:
        less_than_10.append(libraryRecord[i][0])

#sorts the books in ascending order
books_in_order = sorted(books)

#finds the highest scores for bronze/silver/gold:
for i in range(len(libraryRecord)):
    if books_in_order[-1] == libraryRecord[i][3]:
        gold.append(libraryRecord[i])
    if books_in_order[-2] == libraryRecord[i][3]:
        silver.append(libraryRecord[i])
    if books_in_order[-3] == libraryRecord[i][3]:
        bronze.append(libraryRecord[i])


total = sum(books)
avg = round(total/len(books),0)

print(f'The total number of books read is {total} and the average is {avg} per person.')
print(f'Gold: {gold}\nSilver: {silver}\nBronze: {bronze}')

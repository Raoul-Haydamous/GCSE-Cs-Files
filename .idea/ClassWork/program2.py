# Question 1
mysub = ("Computer Science")
print('1',len(mysub))#i
print("2",mysub[-7:-1])#ii
print('3',mysub[::2])#iii
print('4',mysub[len(mysub)-1])#iv
print('5',mysub*2)#v
print('6',mysub[::-2])#vi
print("7",mysub[:3]+mysub[3:])#vii
print('8',mysub.swapcase())#viii
print('9',mysub.startswith('Comp'))#ix
print('10',mysub.isalpha())
# Question 2
myadd = 'WZ-1, New Gana Nagar, New Delhi'
print('1',myadd.lower())#i
print('2',myadd.upper())#ii
print('3',myadd.count('New'))#iii
print('4',myadd.find('New'))#iv (finds the first instance of "New" which is the 6th caracter
print('5',myadd.rfind("New"))#v
print('6',myadd.split(','))#vi
print('7',myadd.split(' '))#vii
print('8', myadd.replace('New', 'Old'))#viii
print('9',myadd.partition(','))
print('10',myadd.index("Agra"))
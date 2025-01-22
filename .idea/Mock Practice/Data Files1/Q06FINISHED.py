
theArtists = [["Andy", "Warhol", 1928],
              ["Pablo", "Picasso", 1881],
              ["Salvador", "Dali", 1904],
              ["Lavinia", "Fontana", 1552],
              ["Jackson", "Pollock", 1912],
              ["Henri", "Matisse", 1869],
              ["Frida", "Kahlo", 1907],
              ["Georgia", "O'Keeffe", 1887],
              ["Kara", "Walker", 1969],
              ["Yayoi", "Kusama", 1929]
             ]

theLabels = []   # Put the new user labels into this structure

# Add your code here
years = []
for i in range(len(theArtists)):
    for n in range(len(theArtists[i])):
        #creating the labels:
        selection = theArtists[i]
        label = selection[1][0]+ selection[0][0] + str(selection[2])
    theLabels.append(label)
        
        #finding the youngest artist:
    years.append(selection[2])
postion_index = years.index(max(years)) #finds where in the list the youngest artist is 
youngest = theArtists[postion_index] 
print(f'The youngest artist is:{youngest[0]+" "+youngest[1]} Born in {max(years)}')

#printing the lables:
for c in range(len(theLabels)):
    print(theLabels[c])



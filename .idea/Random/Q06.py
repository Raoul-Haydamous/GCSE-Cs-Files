#   Q6

#   Structure of sales record is
#   StaffID, First name, Last name, January sales, February sales,
#   March sales, April sales, May sales, June sales

staffSales = [
["101TGY" , "George" , "Taylor" , 6009 , 5262 , 3745 , 7075 , 1943 , 4432],
["103FCY" , "Fehlix" , "Chayne" , 8717 , 2521 , 5777 , 6189 , 5089 , 6957],
["102SBY" , "Sumren" , "Bergen" , 5012 , 1063 , 7937 , 9560 , 1115 , 5499],
["104SBK" , "Samira" , "Beckle" , 1140 , 9206 , 3898 , 8544 , 5937 , 8705],
["105NBT" , "Nellie" , "Bogart" , 3017 , 3342 , 5939 , 2479 , 3374 , 2297],
["106CGT" , "Cheryl" , "Grouth" , 9620 , 7160 , 5113 , 4803 , 5492 , 2195],
["107DGT" , "Danuta" , "Graunt" , 1583 , 7450 , 1026 , 7463 , 2390 , 6509],
["108JDN" , "Jaiden" , "Deckle" , 4064 , 4978 , 2984 , 3159 , 1464 , 4858],
["109JCK" , "Jimran" , "Caliks" , 6253 , 7962 , 2732 , 7504 , 2771 , 5193],
["110DDN" , "Deynar" , "Derran" , 6305 , 8817 , 5200 , 3647 , 3365 , 1256]]


#--------------------------------------------------------------------------
#   Write your code below this line
total_per_member = []
total = []

for i in range(len(staffSales)):
    total_per_member.append(sum(staffSales[i][-6:]))
print(f"The total per member is {total_per_member}")

total.append(sum(total_per_member))
print(f"The total for all staff is {total}.")

totals_in_order = sorted(total_per_member)
print(f"Totals in order: {totals_in_order}")


index1 = (total_per_member).index(totals_in_order[-1])
index2 = (total_per_member).index(totals_in_order[-2])
print(f"Location of 1st place {index1}\nLocation of 2nd place {index2}")

first_place = [staffSales[index1][1:3],totals_in_order[-1]]
second_place = [staffSales[index2][1:3],totals_in_order[-2]]

print(f"First place is {first_place}\nSecond Place is {second_place}")

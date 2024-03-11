density=5 #the original density is 5%
day=1 #the initial day is marked as day1
while density<=90: #Once the density passes 90% the cells will die
    density=2*density 
    day+=1 #This cell line doubles in density every 24 hrs
print("I can stay away lab for",day,"days")
print("On day",day,"the cell density is larger than 90%")

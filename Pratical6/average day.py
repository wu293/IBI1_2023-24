import matplotlib.pyplot as plt 
#24-total of the rest=others
dic = {'Sleeping': 8, 'Classes': 6, 'Studying': 3.5, 'TV': 2, 'Music': 1,'other':3.5} 
# create a dictionary to record the data
labels = dic.keys()  
sizes = dic.values() 
print(dic)
print("The time spent on",'TV',"is 2hours per day")
#print the time spent on one of the activities 
plt.figure()
plt.pie(sizes,labels=labels)
plt.title("The average day of a university student")
plt.show()
plt.clf()#close the figures

import matplotlib.pyplot as plt
import numpy as np

#as the initial data
uk_cities=[0.56,0.62,0.04,9.7]
china_cities=[0.58,8.4,29.9,22.2]
uk_citynames=['Edinburgh','Glasgow','Stirling','London']
china_citynames=['Haining','Hangzhou','Shanghai','Beijing']

#create a bar plot for the population of uk cities
plt.figure()
plt.bar(uk_citynames,uk_cities)
plt.ylabel(uk_cities)
plt.title("Population of UK cities")
plt.xticks(rotation=30)
plt.show()
plt.clf()

#create a bar plot for the population of china cities
plt.figure()
plt.bar(china_citynames,china_cities)
plt.ylabel(china_cities)
plt.title("Population of China cities")
plt.xticks(rotation=30)
plt.show()
plt.clf()

#sort the data for the population of cities
uk_cities.sort()
china_cities.sort()
print(uk_cities)
print(china_cities)

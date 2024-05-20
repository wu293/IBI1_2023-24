import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/Users/yun/Desktop/IBInotes")  

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

print(dalys_data.head(5))

print(dalys_data.info())

print(dalys_data.describe())

print(dalys_data.iloc[0, 3]) 

my_columns = [True, True, False, True]  
print(dalys_data.iloc[0:3, my_columns])

print(dalys_data.loc[0:29, "DALYs"])  

afghanistan_data = dalys_data[dalys_data['Entity'] == 'Afghanistan']

china_data = dalys_data[dalys_data['Entity'] == 'China']
mean_dalys_china = china_data['DALYs'].mean()
print(f"Mean DALYs in China: {mean_dalys_china}")
print(f"2019 DALYs in China: {china_data.loc[china_data['Year'] == 2019, 'DALYs'].values[0]}")

plt.plot(china_data['Year'], china_data['DALYs'], 'b+')
plt.xticks(rotation=-90)  
plt.show()

year_2019_data = dalys_data[dalys_data['Year'] == 2019]
plt.boxplot(year_2019_data['DALYs'])
plt.show()

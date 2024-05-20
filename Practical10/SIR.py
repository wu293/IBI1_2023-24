mport numpy as np  
import matplotlib.pyplot as plt  

N=10000
I=1
R=0
S=N-I-R
beta = 0.3
gamma =0.05

S_array = np.zeros(1000)
I_array = np.zeros(1000)
R_array = np.zeros(1000)

S_array[0] = S
I_array[0] = I
R_array[0] = R

for t in range(1, 1000):  
    Newly_infected_people = np.random.binomial(S_array[t-1], beta * I_array[t-1] / N)  
    New_recovered_people = np.random.binomial(I_array[t-1], gamma)  
    S_array[t] = S_array[t-1] - Newly_infected_people  
    I_array[t] = I_array[t-1] + Newly_infected_people - New_recovered_people  
    R_array[t] = R_array[t-1] + New_recovered_people  
  
plt.plot(S_array, label='Susceptible')  
plt.plot(I_array, label='Infected')  
plt.plot(R_array, label='Recovered')  
plt.xlabel('Time')
plt.ylabel('Number')
plt.title('SIR Model')
plt.legend()  
plt.show()
plt.clf

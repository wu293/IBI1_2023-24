import numpy as np
import matplotlib.pyplot as plt

population = np.zeros((100, 100), dtype=int)

# Randomly select a point as the starting point of the outbreak
outbreak = np.random.choice(range(100), size=2, replace=False)
population[outbreak[0], outbreak[1]] = 1  

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.show()
plt.clf()

beta = 0.3  # infection rate
gamma = 0.05  # recovery rate

# Simulate 100 time points
for t in range(100):
    # Find the location of all the infected
    infected_positions = np.argwhere(population == 1)
    
    for x, y in infected_positions:
        neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1)]
        for nx, ny in neighbors:
            if 0 <= nx < 100 and 0 <= ny < 100 and population[nx, ny] == 0:
                # Infecting neighbors with probability of 0.3
                if np.random.rand() < beta:
                    population[nx, ny] = 1  
                    
    population[population == 1] = 2 if np.random.rand() < gamma else 1
    
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title(f"Time: {t}")
    plt.show()
    plt.clf()

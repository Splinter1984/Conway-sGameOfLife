import math
import random as rand 
from array import array
import matplotlib.pylab as plt

RADIUS = 1024
TOTAL = 50000  
pi_numbers = [] 

def MonteCarloMethod(point_value):
    INSIDE = 0 
    for _ in range(0, TOTAL):
        x = rand.uniform(0, RADIUS)
        y = rand.uniform(0, RADIUS)
        if x * x + y * y < RADIUS * RADIUS:
            INSIDE += 1
            pi_numbers.append((INSIDE / TOTAL * 4 - math.pi) / INSIDE)
        else:
            pi_numbers.append(0)
    return pi_numbers       
            

x = [i for i in range(0, TOTAL)]
y = MonteCarloMethod(TOTAL)
plt.xlabel("X")
plt.ylabel("Y")
plt.xscale("log")
plt.grid(True, linestyle='-', color='0.75')
plt.plot(x, y, 'b-')
plt.show()
# print(pi_number)
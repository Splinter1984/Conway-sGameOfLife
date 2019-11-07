import math
import numpy as np
import random as rand 
from array import array
import matplotlib.pylab as plt

RADIUS = 10
TOTAL = 155300
points_cor_x = []
points_cor_y = []

outside_points_cor_x = []
outside_points_cor_y = []


# fig, ax = plt.subplots()
# ax.add_patch(plt.Circle((0, 0), RADIUS, color='g', alpha=0.05))
# ax.plot()
plt.xlim(0, RADIUS)
plt.ylim(0, RADIUS)

INSIDE = 0 
pi_number = 0
for _ in range(0, TOTAL):
    x = rand.uniform(0, RADIUS)
    y = rand.uniform(0, RADIUS)
    if x * x + y * y < RADIUS * RADIUS:
        points_cor_x.append(x)
        points_cor_y.append(y)
        INSIDE += 1
        pi_number = INSIDE / TOTAL * 4
    else:
        outside_points_cor_x.append(x)
        outside_points_cor_y.append(y) 

plt.scatter(points_cor_x, points_cor_y,s = 0.08, c='g')
plt.scatter(outside_points_cor_x, outside_points_cor_y,s = 0.08, c='b')

plt.title(pi_number)
print(pi_number)    

plt.show()
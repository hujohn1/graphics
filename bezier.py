# P(t)=P0+(1-t)P1, for 0<=t<=1
# P(t)=(1-t^2)P0+2t(1-t)P1+t^2P2
# generalize to Bezier using Bernstein basis coefficients
# Imports
import numpy as np
import math
import matplotlib.pyplot as plt

def combi(n, k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def bernstein(n, i, t):
    return combi(n, i) * (t ** i) * ((1-t) ** (n-i))


# CONSTANTS
# polynomial Bezier degree
N = 4
Pi = np.random.random_sample((N+1, 3))
x, y, z = [], [], []
for ti in np.arange(0, 1+1e-4, 1e-4):
    B = np.zeros(3)
    for c in range(N+1):
        B += bernstein(N, c, ti) * Pi[c]
    x.append(B[0])
    y.append(B[1])
    z.append(B[2])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x, y, z)
ax.scatter(Pi[:, 0], Pi[:, 1], Pi[:, 2], c='black', label='Control Points')
ax.set_title(f'Bezier curve for{N} ')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()

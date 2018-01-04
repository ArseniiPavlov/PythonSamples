from __future__ import division
import numpy as np
import scipy.linalg
from matplotlib import pyplot as plt


def f(x):
    res = np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)
    return res


"""
x = np.linspace(1, 15, num=150)
y = f(x)
plt.plot(x, y)
plt.show()
"""

A1 = np.array([[1, 1], [1, 15]])
b1 = f(np.array([1, 15]))
weights1 = scipy.linalg.solve(A1, b1)
print(weights1)

A2 = np.array([[1, 1, 1], [1, 8, 8 ** 2], [1, 15, 15 ** 2]])
b2 = f(np.array([1, 8, 15]))
weights2 = scipy.linalg.solve(A2, b2)
print(weights2)

A3 = np.array([[1, 1, 1, 1],
               [1, 4, 4 ** 2, 4 ** 3],
               [1, 10, 10 ** 2, 10 ** 3],
               [1, 15, 15 ** 2, 15 ** 3]])
b3 = f(np.array([1, 4, 10, 15]))
weights3 = scipy.linalg.solve(A3, b3)
print(weights3)


def f1(x, w):
    res = w[0] + w[1] * x
    return res


def f2(x, w):
    res = w[0] + w[1] * x + w[2] * (x ** 2)
    return res


def f3(x, w):
    res = w[0] + w[1] * x + w[2] * (x ** 2) + w[3] * (x ** 3)
    return res


x0 = np.linspace(1, 15, num=150)
y0 = f(x0)

x1 = np.linspace(1, 15, num=150)
y1 = f1(x1, weights1)

x2 = np.linspace(1, 15, num=150)
y2 = f2(x2, weights2)

x3 = np.linspace(1, 15, num=150)
y3= f3(x3, weights3)

plt.plot(x0, y0)
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.show()

f = open('submission-2.txt', 'w')
for i in xrange(len(weights3)):
    if i == (len(weights3)-1):
        f.write(str(weights3[i]))
    else:
        f.write(str(weights3[i]) + ' ')

f.close()

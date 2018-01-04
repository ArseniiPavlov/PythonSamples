from __future__ import division
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import math


def f(x):
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)


def fplt(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)


def h(x):
    return int(f(x))


def hplt(x):
    res = np.array([int(np.sin(t / 5) * np.exp(t / 10) + 5 * np.exp(-t / 2)) for t in x])
    return res


print round(opt.minimize(f, [2], method='BFGS').fun, 4), round(opt.minimize(f, [30], method='BFGS').fun, 4)
fl = open('optim1.txt', 'w')
fl.write(str(round(opt.minimize(f, [2], method='BFGS').fun, 2)) + ' '
         + str(round(opt.minimize(f, [30], method='BFGS').fun, 2)))
fl.close()

print round(opt.differential_evolution(f, [(0, 30)]).fun, 2)
fl = open('optim2.txt', 'w')
fl.write(str(round(opt.differential_evolution(f, [(0, 30)]).fun, 2)))
fl.close()

print 'h(x) BFGS\n', str(opt.minimize(h, [30], method='BFGS').fun)
print 'h(x) DF\n', str(opt.differential_evolution(h, [(0, 30)]).fun)

fl = open('optim3.txt', 'w')
fl.write(str(opt.minimize(h, [30], method='BFGS').fun) + ' '
         + str(opt.differential_evolution(h, [(0, 30)]).fun))
fl.close()

xp = np.linspace(1, 30, 500, endpoint=True)
y = hplt(xp)
plt.plot(xp, y)
plt.show()

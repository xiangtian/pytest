"""
   Just for odeint usage
   2017-5-26
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def sir(w, t, a, b):
    s, i, r = w
    ds = -a*s*i
    dr = b*i
    di = -ds-dr
    return np.array([ds, dr, di])

t = np.arange(0, 0.3, 0.1)
print(t)
track = odeint(sir,(0.999,0.001,0), t, args=(1,0.3))
plt.plot(t, track[:,0], t, track[:,1], t, track[:,2])
plt.show()


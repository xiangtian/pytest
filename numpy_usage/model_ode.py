from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
def sir(w, t, a, b):
    s, i, r = w
    ds = -a*s*i
    dr = b*i
    di = -ds-dr
    return np.array([ds, di, dr])
"""
t = np.arange(0, 50, 0.1)
print t
track = odeint(sir,(0.999,0.001,0), t, args=(1,0.3))
plt.plot(t, track[:,0], t, track[:,1], t, track[:,2])
plt.show()
"""

class Node(object):

    def __init__(self, name, init_value, equation):
        self.name = name
        self.init_value = init_value
        self.equation = equation


class Param(object):

    def __init__(self, name, value):
        self.name = name
        self.value = value


def s_equation(param_a, node_s, node_i):
    return -param_a * node_s * node_i

def i_equation(param_a, param_b, node_s, node_i):
    return param_a * node_s * node_i - param_b * node_i

def r_equation(param_b, node_i):
    return param_b * node_i

node_s = Node("S", 0.999, s_equation)
node_i= Node("I", 0.001, i_equation)
node_r = Node("R", 0, r_equation)

param_a = Param("a", 1)
param_b = Param("b", 0.3)

def sir_equation(w, t, a, b):
    s, i, r = w
    ds = node_s.equation(a, s, i)
    di = node_i.equation(a, b, s, i)
    dr = node_r.equation(b, i)
    return np.array([ds, di, dr])
        
t = np.arange(0, 30, 0.1)
track = odeint(sir_equation,\
        (node_s.init_value,node_i.init_value, node_r.init_value),\
        t,\
        args=(param_a.value,param_b.value))
plt.plot(t, track[:,0], t, track[:,1], t, track[:,2])
plt.show()


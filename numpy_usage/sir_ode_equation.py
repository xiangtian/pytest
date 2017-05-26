"""
    Learning How to using odeint calculate ode equation
    2017-5-26
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# All param in this model
param_a = 1
param_b = 0.3

node_s = 0.999
node_i = 0.001
node_r = 0


def sir(w, t):
    node_s, node_i, node_r = w
    local_node_s = -param_a * node_s * node_i
    local_node_i = param_a * node_s * node_i - param_b * node_i
    local_node_r = param_b * node_i
    return np.array([local_node_s, local_node_i, local_node_r])

node_init_values = (node_s, node_i, node_r)

t = np.arange(0, 30, 0.1)
track = odeint(sir, node_init_values, t)
track = odeint(sir, (node_s, node_i, node_r), t)
plt.plot(t, track[:, 0], t, track[:, 1], t, track[:, 2])
plt.show()


from __future__ import division
from scipy import integrate
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

# K channel
alpha_n = vectorize(lambda v: 0.01*(-v + 10)/(exp((-v + 10)/10) - 1) if v != 10 else 0.1)
beta_n  = lambda v: 0.125*exp(-v/80)
n_inf   = lambda v: alpha_n(v)/(alpha_n(v) + beta_n(v))

# Na channel (activating)
alpha_m = vectorize(lambda v: 0.1*(-v + 25)/(exp((-v + 25)/10) - 1) if v != 25 else 1)
beta_m  = lambda v: 4*exp(-v/18)
m_inf   = lambda v: alpha_m(v)/(alpha_m(v) + beta_m(v))

# Na channel (inactivating)
alpha_h = lambda v: 0.07*exp(-v/20)
beta_h  = lambda v: 1/(exp((-v + 30)/10) + 1)
h_inf   = lambda v: alpha_h(v)/(alpha_h(v) + beta_h(v))



## HH Parameters
V_rest  = -55      # mV
Cm      = 1      # uF/cm2
gbar_Na = 120    # mS/cm2
gbar_K  = 36     # mS/cm2
gbar_l  = 0.3    # mS/cm2
E_Na    = 115    # mV
E_K     = -12    # mV
E_l     = 10.613 # mV

I = 10

m       = m_inf(V_rest)
h       = h_inf(V_rest)
n       = n_inf(V_rest)

## setup parameters and state variables
T     = 300    # ms
dt    = 0.01 # ms
time  = arange(0,T+dt,dt)


Vm      = zeros(len(time)) # mV
Vm[0]   = V_rest


## Simulate Model
for i in range(1,len(time)):
	g_Na = gbar_Na*(m**3)*h
	g_K  = gbar_K*(n**4)
	g_l  = gbar_l
	m += (alpha_m(Vm[i-1])*(1 - m) - beta_m(Vm[i-1])*m) * dt
	h += (alpha_h(Vm[i-1])*(1 - h) - beta_h(Vm[i-1])*h) * dt
	n += (alpha_n(Vm[i-1])*(1 - n) - beta_n(Vm[i-1])*n) * dt
	Vm[i] = Vm[i-1] + (I - g_Na*(Vm[i-1] - E_Na) - g_K*(Vm[i-1] - E_K) - g_l*(Vm[i-1] - E_l)) / Cm * dt

## plot membrane potential trace
plt.plot(time, Vm)
plt.title('Hodgkin-Huxley Neuron Simulation')
plt.ylabel('Membrane Potential in mV')
plt.xlabel('Time in Miliseconds')
plt.show()



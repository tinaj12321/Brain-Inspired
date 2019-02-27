import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from pylab import *

#parameters to change as necessary
#taken from paper referenced in assignment

a = 0.02
b = 0.2
c = -65
d = 4
u = 0.0 #membrane potential
v = -80 #resting potential


I = 10
T = 500
dT = 0.1 #threshold

potential_array = zeros(int((T/dT)+1)) 
recovery_array = zeros(int(T/dT+1))
current_time = arange(0, T+dT, dT)
for i in range(len(current_time)):
	v += ((0.04*v**2)+5*v+140-u+I)*dT
	u += (a*((b*v)-u))*dT
	if(v >= 30):
		potential_array[i] = 30
		v = c
		u += d
	else:
		potential_array[i] = v
		recovery_array[i] = u

plt.plot(current_time, potential_array)
plt.plot(current_time, recovery_array)
plt.title("Izhikevich Neuron Simulation")
plt.xlabel("Time in Miliseconds")
plt.ylabel("Membrane Potential in Volts")
plt.show()


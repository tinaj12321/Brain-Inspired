import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from pylab import *

I = 1.0 #input current in Amps

T = 200 #simulation time in miliseconds
dT = 0.1 #dT time step
membranePotentials = zeros((T/dT +1)) #array of membrane potentials to plot
Vt = 1 #threshold in Volts
Vr = 0 #reset potential
intiialPotential = 0.0 #initial membrane potential
R = 1.0 #membrane resistance 
C = 10 #capitance in uF
tau = R*C

currPotentialChange = float(10.0) #change in membrane potential

for i in range(0, len(membranePotentials)):
	currPotentialChange = (-1*membranePotentials[i-1] + R*I)
	membranePotentials[i] = membranePotentials[i-1] + currPotentialChange/tau*dT
	if(membranePotentials[i] >= Vt): #there is a spike
		membranePotentials[i] = Vr #reset neuron

#Plotting

currTime = arange(0,T+dT, dT)
plt.plot(currTime, membranePotentials, '')
plt.xlabel('Time in miliseconds')
plt.ylabel('Membrane Potential in Volts')
plt.title('LIF Neuron Simulation')
plt.ylim([0,4])
plt.show()


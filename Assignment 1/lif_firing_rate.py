import numpy as numpy
import matplotlib.pyplot as plt
from pylab import *

interval = 0.01
inputCurr = arange(1.01, 10+interval, interval)
firing_rate = range(900)

R = 1.0 #membrane resistance
C = 10 #capitance
tau = R*C
Vt = 1 #threshold in volds


for i in range(len(inputCurr)):
	T = tau * (np.log(inputCurr[i]/(inputCurr[i]-Vt)))
	firing_rate[i] = (1/T)*1000

plt.plot(inputCurr, firing_rate)
plt.title('Firing Rate with LIF Neuron')
plt.xlabel('Input Current in Volts')
plt.ylabel('Firing Rate')
plt.show()


#Under modulation, critical modulation, over modulation
import numpy as np
import matplotlib.pyplot as plt
from math import pi as p

Ac = eval(input('Enter carrier Amplitude: '))
Am = eval(input('Enter the message signal amplitude: '))
fc = eval(input('Enter carrier signal frequency: '))
fm = eval(input('Enter message signal frequency: '))

t = np.arange(-0.25,0.25,0.0001)
mu = Am/Ac
s = Ac*(1+mu*np.cos(2*p*fm*t))*np.cos(2*p*fc*t)

plt.plot(t,s,'r')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Amplitude modulated signal')

plt.show()
plt.grid()
#End
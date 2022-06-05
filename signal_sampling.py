#Sampling with python
#Nyquist rate: fs >= 2*fm, fs = 1/Ts, Ts <= 1/2fm
import numpy as np
import matplotlib.pyplot as plt
from math import pi as p

#Generating a 50 Hz sampled freq. signal.
fm = eval(input('Enter the frequency of the sinusoid: '))
fs = eval(input('Enter the sampling frequency: ')) #sampling frequemcy
t = np.arange(0,0.05,0.0005)
ts = np.arange(0,0.05, (1/fs))#sampling time
x = np.cos(2*p*fm*t)
samp_signal = np.cos(2*p*fm*ts)
plt.plot(t,x, 'g')
plt.stem(ts,samp_signal,'r*')
plt.show()
plt.grid()

#Sampling generated signal




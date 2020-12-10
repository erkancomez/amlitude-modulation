import numpy as np
import matplotlib.pyplot as plt
import numpy
from scipy import signal

A_c = 1
f_c = 200
A_m = 5
f_m = 10
modulation_index = 8000



t = np.linspace(0, 1, 1000)

carrier = A_c*np.cos(2*np.pi*f_c*t)
modulator = A_m*np.cos(2*np.pi*f_m*t)
product = A_c*(np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_c*t)

#############################################
# noise tanımlanan kısım
#############################################

noise = np.random.normal (0 , np.sqrt(0.01) , len( product ))

#############################################

plt.subplot(6,1,1)
plt.title('Amplitude Modulation')
plt.plot(modulator,'b')
plt.ylabel('Amplitude')
plt.xlabel('Message signal')

plt.subplot(6,1,2)
plt.plot(carrier, 'y')
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')

plt.subplot(6,1,3)
plt.plot(product, color="g")
plt.ylabel('Signal')
plt.xlabel('AM signal')


#######################
# Noise eklenen kısım ve demodule edilen kısım
#######################

modulation = noise + product

demodulation = modulation * carrier

#####################

plt.subplot(6,1,4)
plt.plot(modulation, color="r")
plt.ylabel('Noise + Signal')
plt.xlabel('Signal With Noise')


#######################
#Filtre uygulanan kısım
#######################

b, a = signal.butter(6 , 0.02, btype ='lowpass')
filtered = signal.lfilter (b, a, demodulation )

#######################

plt.subplot(6,1,5)
plt.plot(demodulation, color="orange")
plt.ylabel('Convolve - Noise')
plt.xlabel('Demodulation')


######################

plt.subplot(6,1,6)
plt.plot(filtered, color="b")
plt.ylabel('Convolve - Noise')
plt.xlabel('Filtered')


plt.subplots_adjust(hspace=1)
plt.rc('font', size=15)
fig = plt.gcf()
fig.set_size_inches(32, 15)

fig.savefig('Amplitude Modulation.png', dpi=100)
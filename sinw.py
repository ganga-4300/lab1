import matplotlib.pyplot as plt
import numpy as np
Fs=2500
f=200
n=50
p=np.arange(n)
A=np.sin(2*np.pi*f/Fs*p)
plt.plot(p,A)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

plt.show()

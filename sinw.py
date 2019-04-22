import matplotlib.pyplot as plt
import numpy as np
fs=1000
fr1=200
fr2=100
n=100
x=np.arange(n)
a=np.cos(2*np.pi*fr1/fs*x)
plt.subplot(212)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

d=np.cos(2*np.pi*fr2/fs*x)
plt.subplot(211)
plt.plot(x,d)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show()


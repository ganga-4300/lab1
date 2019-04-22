import matplotlib.pyplot as plt
import numpy as np
fs=10000
f1=100
f2=100
n=200
ampli1=10
ampli2=10
x=np.arange(n)
a=ampli1*np.cos(2*np.pi*f1/fs*x)
plt.subplot(311)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

c=ampli2*np.cos(2*np.pi*f2/fs*x)
plt.subplot(312)
plt.plot(x,c)
d=a+b
plt.subplot(313)
plt.plot(x,d)
plt.title('addition of two waves')
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show()


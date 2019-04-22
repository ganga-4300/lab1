import matplotlib.pyplot as plt
import numpy as np
fs=10000
fr1=150
fr2=100
n=200
x=np.arange(n)
a=np.cos(2*np.pi*fr1/fs*x)
plt.subplot(311)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

c=np.cos(2*np.pi*fr2/fs*x)
plt.subplot(312)
plt.plot(x,c)
d=a+b
plt.subplot(313)
plt.plot(x,d)
plt.title('addition of two waves')
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show()


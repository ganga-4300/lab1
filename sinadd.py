import matplotlib.pyplot as plt
import numpy as np

sample =2000
f=100
Fs=1000
n=np.arange(sample)
a=np.sin(2*np.pi*n*f/Fs)
f=50
Fs=4000
b=np.sin(2*np.pi*n*f/Fs)
c=a+b
plt.subplot(311)
plt.plot(n,a)
plt.subplot(312)
plt.plot(n,b)
plt.subplot(313)
plt.plot(n,c)


plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()


import matplotlib.pyplot as plt
import numpy as np
fs=10000
fr1=100
fr2=100
n=200
amp1=10
amp2=10
r1=0
r2=90
x=np.arange(n)
a=amp1*np.cos(2*np.pi*fr1/fs*x+r1)
plt.subplot(311)
plt.plot(x,a)
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')

c=amp2*np.cos(2*np.pi*fr2/fs*x+r2)
plt.subplot(312)
plt.plot(x,c)
d=a+b
plt.subplot(313)
plt.plot(x,d)
plt.title('addition of two waves')
plt.xlabel('samples(n)')
plt.ylabel('amplitude(v)')
plt.show()


import numpy as np
import matplotlib.pyplot as plt
N=400
#x=np.arange(0,N)
F=100
Fs=4000
l=np.arange(0,400,1)
x=np.sin((2*np.pi*F*l)/Fs)
c=complex(0,-1)
y=[]
for k in range(0,N-1):
	s=0
	for n in range(0,N-1):
		s=s+(x[n]*(np.exp(c*2*np.pi*k*n/N)))
	y.append(s)
print(y)
m=np.abs(y)
#p=np.angle(y)
#plt.subplot(141)
#plt.stem(x)
#plt.subplot(142)
plt.plot(y)
#plt.subplot(143)
#plt.stem(m)
#plt.subplot(144)
#plt.stem(p)
plt.show()

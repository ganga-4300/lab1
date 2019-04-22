import numpy as np
import matplotlib.pyplot as plt
#w=np.linspace(-180,180,1)
x=np.arange(0,6,1)
N=100
w=np.linspace(-np.pi,np.pi,N)
k=complex(0,-1)
y=[]
for n in range(0,N):
	sum=0
	for i in range(0,len(x)):
		sum=sum+(x[i]*(np.exp(k*w[n]*n)))
	y.append(sum)	
print("y",y)
ph=np.angle(y)
ma=np.abs(y)
#plt.subplot(141)
#plt.stem(x)
#plt.subplot(142)
plt.plot(y)
#plt.subplot(143)
#plt.stem(w,ma)
#plt.subplot(144)
#plt.stem(ph)
plt.show()

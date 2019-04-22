import numpy as np
import matplotlib.pyplot as plt
w=np.arange(-180,180,1)
n=np.arange(-200,200,1)
fs=100.0
x=np.sin(2*np.pi*20.0*n/fs)
w=np.arange(-1.0*np.pi,np.pi,np.pi/500.0)
w=int(w)
k=complex(0,-1)
y=[]
for i in range (w):
	sum=0
	p=0
	for j in range(n):
		sum=sum+(x[p]*(np.exp(k*i*j)))
	p=p+1
	y=np.append(x,sum)	
print("y",y)
ph=np.angle(y)
ma=np.abs(y)
plt.subplot(141)
plt.stem(x)
plt.subplot(142)
plt.stem(y)
plt.subplot(143)
plt.stem(w,ma)
plt.subplot(144)
plt.stem(ph)
plt.show()


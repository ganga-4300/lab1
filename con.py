import numpy as np
from matplotlib import pyplot as plt
lx=int(input("enter length of x"))
lh=int(input("enter length of h"))
x=[1,2,3,4]
h=[1.2,3]
y=[]
for n in range(0,lx+lh-1):
	sum=0
	for k in range(0,lx):
		if (n-k<lh and n-k>=0):
			sum=sum+x[k]*h[n-k]
	y=np.append(y,sum)
print (y)
def time_rev(x):
	lx=len(x)
	y=[]
	for i in range(0,lx):
		y=np.append(y,x[lx-i-1])
	return y
#e=np.array(input("enter seg1"))
#f=np.array(input("enter seg2"))


print("convolute=",np.convolve(x,h))
print(convolute(x,time_rev(h)))
n=np.arange(0,500)
x=np.sin(2*np.pi*20.0/400.0*n)
N=np.sin(2*np.pi*50.0/400.0*n)
N1=np.random.rand(x_shape[0])
x_N=x+N+N1
h=[1.0/3.0,1.0/3.0,1.0/3.0]
y1=convolute(h,x_N)
y2=convolute(x,time_rev(x))
y3=convolute(x_N,time_rev(x_N))
a1=plt.subplot(611)
a1=plt.plot(x)
a2=plt.subplot(612,share+a1)
a2=plot(N1)
a3=plt.subplot(613,share+a1)
a3=plot(x_N)
a4=plt.subplot(614,share+a1)
a4=plot(y1)
a5=plt.subplot(615,share_a1)
a5=plt.plot(y2)
a6=plt.subplot(616,share+a1)
a6=plot(y3)
plt.show()

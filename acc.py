import numpy as np
import matplotlib.pyplot as plt
p=int(input("enter the number"))
Fs=2000
f1=50
f2=500
y=np.zeros(100)
#t=np.linspace(0,40,10)
sum=0
q=p-1
for i in range(0,100,1):
	for k in range(0,q,1):
		sum=sum+p
	y[i]=sum
	sum=0
print (y)
plt.plot(y)
plt.show()

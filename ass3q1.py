import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    if (x!=0):
        return np.sin(x)/x
    else:
        return 1
def g(k):
    if (-1<k<1):
        return np.sqrt(np.pi/2)
    else:
        return 0
xmin=-50
xmax=50
n=256
dx=(xmax-xmin)/(n-1)
sampled_data=np.zeros(n)
xarr=np.zeros(n)

for i in range(n):
    sampled_data[i]=f(xmin+i*dx)
    xarr[i]=xmin+i*dx
nft=np.fft.fft(sampled_data,norm='ortho')
karr=np.fft.fftfreq(n,d=dx)
karr=2*np.pi*karr
factor=np.exp(-1j*karr*xmin)
aft=dx*np.sqrt(n/(2.0*np.pi))*factor*nft

#Analytical FT
analytical_result=np.zeros(n)

for j in range(n):
    analytical_result[j]=g(karr[j])         

plt.plot(karr,aft,'r',label=r'numerical solution')                    
plt.plot(karr,analytical_result,'g',label=r'analytical solution')         
plt.xlabel('k')
plt.ylabel('FT of the sinc function')
plt.legend()
plt.show()

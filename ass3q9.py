import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    if(abs(x)<1):
        return(1.0)
    else:
        return(0.0)
    
def f2(x):
    if(abs(x)<1):
        return(1.0)
    else:
        return(0.0)
    
xmin=-5.0
xmax=5.0

numpoints=1024
dx=(xmax-xmin)/(numpoints-1)

sampled_data1=np.zeros(numpoints)
sampled_data2=np.zeros(numpoints)
xarr=np.zeros(numpoints)

for i in range(numpoints):
    sampled_data1[i]=f1(xmin+i*dx)
    sampled_data2[i]=f2(xmin+i*dx)
    xarr[i]=xmin+i*dx
    
nft1=np.fft.fft(sampled_data1,norm='ortho')
nft2=np.fft.fft(sampled_data2,norm='ortho')

karr=np.fft.fftfreq(numpoints,d=dx)
karr=2*np.pi*karr
dk=karr[1]-karr[0]

nft=nft1*nft2

convo_prime=np.fft.ifft(nft,norm='ortho')

convo=dx*np.sqrt(numpoints)*convo_prime

xarr_prime=np.fft.fftfreq(numpoints,d=dk)
xarr_prime=2*np.pi*xarr_prime

plt.plot(xarr,sampled_data1,label=r'box function')
plt.plot(xarr_prime,convo,'.',label=r'convo with itself')
plt.legend()
plt.show()

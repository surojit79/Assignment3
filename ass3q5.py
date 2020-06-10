import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
import math

#Direct method

def dft(n):
    w_p=np.arange(n)
    w_q=np.zeros(n,complex)
    t1=timer()
    for i in range(n):
        for k in range(n):
            w_q[k]=(w_q[k] + w_p[k]*np.exp(-1j*2*np.pi*i*k/n))/np.sqrt(n)
    t2=timer()
    time_taken1=t2-t1
    return time_taken1

#Using numpy

def fft(n):
    w_p=np.arange(n)
    t3=timer()
    w_q=np.fft.fft(w_p,norm='ortho')  
    t4=timer()
    time_taken2=t4-t3
    return time_taken2

#variation of n
n=[]
DFT=[]
FFT=[]

#varing n 
for j in range(1,100):
    n.append(j)
    DFT.append(dft(j))  
    FFT.append(fft(j))
    
plt.plot(n,DFT,'r',label=r'DFT')   
plt.plot(n,FFT,'g',label=r'FFT')            
plt.xlabel('n')
plt.ylabel('t')
plt.legend()
plt.show()





    

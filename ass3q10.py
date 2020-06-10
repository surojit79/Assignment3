import numpy as np
import matplotlib.pyplot as plt

#Given data 
file=open('noise.txt','r')      
data=[]
for line in file:
    data.append(float(line))
data=np.array(data)
n=len(data)
print(n)

dft=np.fft.fft(data)
karr=np.fft.fftfreq(n,d=1)
k_max, k_min = max(karr), min(karr)

Power_spectrum=(dft)**2/n
       
plt.subplots()
plt.plot(data)
plt.xlabel('n')
plt.ylabel('nth measurement')
plt.show()

plt.subplots()
plt.plot(karr,dft)
plt.xlabel('k')
plt.ylabel('dft')
plt.show()

plt.subplots()
plt.plot(karr,Power_spectrum)
plt.xlabel('k')
plt.ylabel('Power spectrum')
plt.show()

plt.subplots()
plt.hist(Power_spectrum,range=(k_min,k_max),bins=10,density=True,label=r'Binned power spectrum')
plt.xlabel('k')
plt.legend()
plt.show()

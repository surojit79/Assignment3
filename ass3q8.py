import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
from pylab import rcParams
rcParams['figure.figsize'] = 5, 5

def f(x, y):
    return np.exp(-x*x-y*y)

xmin=-50
xmax=50
ymin=-50
ymax=50
n=256
dx=(xmax-xmin)/(n-1)
dy=(ymax-ymin)/(n-1)
sampled_data=np.zeros((n,n))
xarr=np.zeros(n)
yarr=np.zeros(n)

for i in range(n):
    for j in range(n):
        sampled_data[i,j]=f(xmin+i*dx,ymin+j*dy)
        xarr[i]=xmin+i*dx
        yarr[j]=ymin+j*dx
        
nft=np.fft.fft2(sampled_data,norm='ortho')
karr_x=np.fft.fftfreq(n,d=dx)
karr_x=2*np.pi*karr_x
karr_y=np.fft.fftfreq(n,d=dy)
karr_y=2*np.pi*karr_y
factor_x=np.exp(-1j*karr_x*xmin)
factor_y=np.exp(-1j*karr_y*xmin)

aft=dx*dy*(n/(2.0*np.pi))*factor_x*factor_y*nft

kx,ky=np.meshgrid(karr_x,karr_y)

fig = plt.figure()
axes = fig.gca(projection='3d')    
p=axes.plot_surface(kx,ky,np.abs(aft),rstride=4,cstride=4,cmap=cm.RdBu,linewidth=0)
axes.set_xlabel('kx')
axes.set_ylabel('ky')
axes.set_zlabel('f(k)')
plt.title('numerical solution')
plt.tight_layout();
plt.show()

#analytical solution 

Z=0.5*np.exp(0.25*(-kx**2-ky**2))#analytical sol

fig = plt.figure()
axes = fig.gca(projection='3d')
p=axes.plot_surface(kx,ky,Z,rstride=4,cstride=4,cmap=cm.hot,linewidth=0)    
axes.set_xlabel('kx')
axes.set_ylabel('ky')
axes.set_zlabel('f(k)')
plt.title('analytical solution')
plt.tight_layout();
plt.show()

























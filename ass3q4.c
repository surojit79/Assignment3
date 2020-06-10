#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<fftw3.h>
#define x_max 50.0
#define x_min -50.0
#define numpoints 256
#define real 0
#define imag 1


void generate_data (fftw_complex* sdata,double delta)
{
  int i;
  double x;
  while (i<numpoints)
  {
    x=x_min+i*delta;		
    if(x!=0)
    {
        sdata[i][0]=exp(-pow(x,2));
    }
    else
        sdata[i][0]=1; 
    sdata[i][1]=0;
    i++;
  }
}

int main()
{        
	FILE *mptr;
    	mptr=fopen("fourier_4.txt","w");		/*opening file to write mode*/
	fftw_complex *sdata;
	fftw_complex *result;		/*initiallzing arrays to store initial and final data*/
	double k,freq;
	double delta=(x_max-x_min)/(numpoints-1);
	double aft_real,aft_imag;

	sdata  = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * numpoints);    /*allocating memory*/
	result = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * numpoints);
	
  	fftw_plan p;    /*algorithm for fftw*/
	
	p = fftw_plan_dft_1d(numpoints, sdata, result, FFTW_FORWARD, FFTW_ESTIMATE);

	generate_data(sdata,delta);

  	fftw_execute(p); 		/*creates the DFT*/

	int i;
	for (i=0;i<numpoints;i++)
  	{
	   if (i<=numpoints/2-1)
	   {
		freq=(2*M_PI/(numpoints*delta))*(i);
	   }
	   else
	   {
		freq=(2*M_PI/(numpoints*delta))*(i-numpoints);
	   }
	   aft_real=(1/sqrt(numpoints))*result[i][real];   /*making FT by proper normalisation factor*/
   	   aft_imag=(1/sqrt(numpoints))*result[i][imag];
	   aft_real= delta*sqrt(numpoints/(2*M_PI))*(cos(freq*x_min)*aft_real+sin(freq*x_min)*aft_imag);
	   aft_imag= delta*sqrt(numpoints/(2*M_PI))*(cos(freq*x_min)*aft_imag-sin(freq*x_min)*aft_real);
	   fprintf(mptr,"%e\t%e\t%e\n",freq,aft_real,aft_imag);
	  
 	}
	
	fftw_destroy_plan(p);
	fftw_free(sdata); 
	fftw_free(result);
	return (0);
}



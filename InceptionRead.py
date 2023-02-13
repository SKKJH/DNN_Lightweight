import numpy as np
import pandas as pd
import h5py
#import openpmd_api

hdf = h5py.File('inception_v3_weights_tf_dim_ordering_tf_kernels.h5','r')

f = open('mean.txt','w')
u = open('variance.txt','w')
c = open('beta.txt','w')
cv = open('ConvKernel.txt','w')
bia = open('Prediction_bias.txt','w')
ker = open('Prediction_kernel.txt','w')

kernel5 = hdf.get('/predictions/predictions/bias:0')
kernel6 = hdf.get('/predictions/predictions/kernel:0')

if kernel5 is not None:
	view = np.array(kernel5)
	Kernel5 = view.tolist()
	#print(Kernel)
	kernel5 = ",".join(map(str,Kernel5))
	bia.write(kernel5)
	bia.write("\n")

if kernel6 is not None:
	view = np.array(kernel6)
	Kernel6 = view.tolist()
	#print(Kernel)
	kernel6 = ",".join(map(str,Kernel6))
	ker.write(kernel6)
	ker.write("\n")


for k in range(94):
	K = str(k+1)
	kernel = hdf.get('/batch_normalization_'+K+'/batch_normalization_'+K+'/moving_mean:0')
	if kernel is not None:
		view = np.array(kernel)
		Kernel = view.tolist()
		#print(Kernel)
		kernel = ",".join(map(str,Kernel))
		f.write(kernel)
		f.write("\n")
	kernel2 = hdf.get('/batch_normalization_'+K+'/batch_normalization_'+K+'/moving_variance:0')
	if kernel2 is not None:
		view = np.array(kernel2)
		Kernel2 = view.tolist()
		#print(Kernel)
		kernel2 = ",".join(map(str,Kernel2))
		u.write(kernel2)
		u.write("\n")
	kernel3 = hdf.get('/batch_normalization_'+K+'/batch_normalization_'+K+'/beta:0')
	if kernel3 is not None:
		view = np.array(kernel3)
		Kernel3 = view.tolist()
		#print(Kernel)
		kernel3 = ",".join(map(str,Kernel3))
		c.write(kernel3)
		c.write("\n")

	kernel4 = hdf.get('/conv2d_'+K+'/conv2d_'+K+'/kernel:0')
	if kernel4 is not None:
		view = np.array(kernel4)
		Kernel4 = view.tolist()
		#print(Kernel)
		kernel4 = ",".join(map(str,Kernel4))
		cv.write(kernel4)
		
f.close()
u.close()
c.close()
cv.close()
ker.close()
bia.close()


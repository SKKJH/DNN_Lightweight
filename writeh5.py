import numpy as np
import pandas as pd
import h5py
#import openpmd_api

hdf = h5py.File('copy.h5','a')
f = open('shiftbeta.txt','r')
for k in range(94):
	K = str(k+1)
	kernel3 = hdf.get('/batch_normalization_'+K+'/batch_normalization_'+K+'/beta:0')
	if kernel3 is not None:
		del hdf['/batch_normalization_'+K+'/batch_normalization_'+K+'/beta:0']
		string = f.readline()
		new_str = string.replace("\n", "")
		list_a = new_str.split(',')
		npy = np.array(list_a)
		floatnpy = np.asarray(npy, dtype = float)
		print(floatnpy)
		hdf['/batch_normalization_'+K+'/batch_normalization_'+K+'/beta:0'] = floatnpy

import numpy as np


data = np.loadtxt(fname='../data/inflammation-01.csv',delimiter=',')

if data.max(axis=0)[0] == 0 and data.max(axis=0)[20] == 20:
	print 'suspicious'

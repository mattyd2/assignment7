import numpy as np

class arraybuilder:
	def __init__(self):
		self.self = self

def twoDArray():
	arr = np.arange(1,16).reshape((5,3), order='F')
	arrtwo = arr[1]
	arrfour = arr[3]
	arr2 = np.stack((arrtwo, arrfour))
	arrcol = arr[:,[1]]
	arrcords = arr[1:4,:]
	arrvales = arr[np.where(np.logical_and(arr>3,arr<11))]
	print 'Question 1','\n', arr, '\n', 'Question 1.a','\n', arr2, '\n', 'Question 1.b','\n', arrcol, '\n', 'Question 1.c','\n', arrcords, '\n','Question 1.d','\n', arrvales, '\n'
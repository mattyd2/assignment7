import numpy as np

class arraybuilder:
	def __init__(self):
		self.self = self

def twoDArray():
	
	""" add comments
	"""

	arr = np.arange(1,16).reshape((5,3), order='F')
	arrtwo = arr[1]
	arrfour = arr[3]
	arr2 = np.stack((arrtwo, arrfour))
	arrcol = arr[:,[1]]
	arrcords = arr[1:4,:]
	arrvales = arr[np.where(np.logical_and(arr>3,arr<11))]
	print 'Question 1','\n', arr, '\n', 'Question 1.a','\n', arr2, '\n', 'Question 1.b','\n', arrcol, '\n', 'Question 1.c','\n', arrcords, '\n','Question 1.d','\n', arrvales, '\n'

def thedivider():

	"""this function takes an array numpy array with shape (5,5)
	and divides it by [1.,5,10,15,20] along the columns"""

	a = np.arange(25).reshape(5,5)
	b = np.array([1.,5,10,15,20])
	result = np.divide(a, b)
	print 'Question 2','\n', result

# Credits: http://stackoverflow.com/questions/7845165/how-to-take-input-in-an-array-python

def arraymath():

	"""add comments"""

	x = np.random.random((10,3))
	y = np.where()


	print 'Question 2','\n', result
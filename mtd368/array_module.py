import numpy as np
import unittest
import matplotlib.pyplot as plt


class arraybuilder:
	def __init__(self):
		self.self = self

def twoDArray():	
	
	"""The twoDArray() method takes no arguments. It generates
	four outputs that answer questions for DSGA-1007 HW 7.
	"""

	initial = np.arange(1,16).reshape((5,3), order='F')
	initialRowTwo = initial[1]
	initialRowFour = initial[3]
	initialRowsTwoAndFour = np.stack((initialRowTwo, initialRowFour))
	initialSecondColumn = initial[:,[1]]
	initialBetweenCoordinates = initial[1:4,:]
	initialElementsValuesRange = initial[np.where(np.logical_and(initial>3,initial<11))]  #Values from the initial that are between 3 and 11.
	print 'Question 1','\n', initial, '\n', 'Question 1.a','\n', initialRowsTwoAndFour, '\n', 'Question 1.b','\n', initialSecondColumn, '\n', 'Question 1.c','\n', initialBetweenCoordinates,'\n' ,'Question 1.d','\n', initialElementsValuesRange, '\n'
	return initial, initialRowsTwoAndFour, initialSecondColumn, initialBetweenCoordinates, initialElementsValuesRange

def thedivider():

	"""this function takes an array numpy array with shape (5,5)
	and divides it by [1.,5,10,15,20] along the columns"""

	initial = np.arange(25).reshape(5,5)
	divisorValues = np.array([1.,5,10,15,20])
	divisionResult = np.divide(initial, divisorValues)
	print 'Question 2','\n', divisionResult,'\n'
	return divisionResult
	

# Credits: http://stackoverflow.com/questions/7845165/how-to-take-input-in-an-array-python

def arraymath():

	"""The arraymath() method takes no arguments. It generates
	an array which is the values closest to 0.5 from a randomly
	generated array with shape 10,3."""

	randomOutput = np.random.random((10,3))
	differenceBetweenRandomOutputAnd = np.subtract(0.5,randomOutput) #calculate difference between random output and 0.5
	absolutevalueOfDifference = np.absolute(differenceBetweenRandomOutputAnd)
	sortedClosest = np.argsort(absolutevalueOfDifference, axis=-1)
	valuesClosestTo = randomOutput[(sortedClosest==0)] #returns values from randomOutput that are closest to 0.5
	print 'Question 3', '\n', valuesClosestTo, '\n'
	return valuesClosestTo

#Credit: http://www.scipy-lectures.org/plot_directive/intro/numpy/solutions/2_4_mandelbrot.py

def generate_mandelbrot():

	"""This is a function that takes no arguments and returns a
	Mandelbrot image into the program file."""

	nx,ny = (1000,1000)
	N_max = 50
	some_threshold = 50
	x = np.linspace(-2,1, nx)
	y = np.linspace(-1.5,1.5, ny)
	c = x[:,np.newaxis] + 1j*y[np.newaxis,:]
	z = c
	with np.errstate(over='ignore', invalid='ignore'):
		for v in range(N_max):
			z = z**2 + c
	
		mandelbrot_set = (abs(z) < some_threshold)
	finalMandelbrotset = mandelbrot_set
	plt.imshow(finalMandelbrotset.T, extent=[-2, 1, -1.5, 1.5])
	plt.gray()
	plt.savefig('mandelbrot.png')
	print "\n 'mandelbrot.png' is saved in the current directory."

if __name__ == '__main__':
    unittest.main()



import numpy as np
# import matplotlib as plt

def mandelbrot():

	"""comments"""
	N_max = 50
	some_threshold = 50
	x = np.linspace(-2,1, num=10)
	y = np.linspace(-1.5,1.5, num=10)
	c = x[:,np.newaxis] + 1j*y[np.newaxis,:]
	z = c
	with np.errstate(over='ignore', invalid='ignore'):
		for v in range(N_max):
			z = z**2 + c
	
		mandelbrot_set = (abs(z) < some_threshold)
	print mandelbrot_set


	# plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
	# plt.gray()
	# plt.savefig('mandelbrot.png')


	return mandelbrot_set
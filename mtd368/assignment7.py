#Program Purpose: execute a number of functions using Numpy.
#Author: Matthew T. Dunn
#Date: 11/1/15

import sys
import matplotlib.pyplot as plt
import array_module
from array_module import arraybuilder, twoDArray, thedivider, arraymath, generate_mandelbrot


try:
	question1 = twoDArray()
	question2 = thedivider()
	question3 = arraymath()
	question4 = generate_mandelbrot()
except KeyboardInterrupt, ValueError:
     print "\n Interrupted!"
except EOFError:
     print "\n Interrupted!"
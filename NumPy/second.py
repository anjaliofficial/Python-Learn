#Reshape and Random Number generator 
# numpy.random.random() is one of the function for doing random sampling in numpy. It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0).

# Syntax : numpy.random.random(size=None)

# Parameters :
# size : [int or tuple of ints, optional] Output shape. If the given shape is, e.g., (m, n, k), then m * n * k samples are drawn. Default is None, in which case a single value is returned.

# Return : Array of random floats in the interval [0.0, 1.0). or a single such random float if size not provided.
# Python program explaining
# numpy.random.random() function
  
# importing numpy
import numpy as geek
  
  
# output array
out_arr = geek.random.random(3)
print ("Output 1D Array filled with random floats : ", out_arr)
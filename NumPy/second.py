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


# --------------------------------------
# The arange([start,] stop[, step,][, dtype]) : Returns an array with evenly spaced elements as per the interval. The interval mentioned is half-opened i.e. [Start, Stop) 
# Parameters : 

# start : [optional] start of interval range. By default start = 0
# stop  : end of interval range
# step  : [optional] step size of interval. By default step size = 1,  
# For any output out, this is the distance between two adjacent values, out[i+1] - out[i]. 
# dtype : type of output array

# Array of evenly spaced values.
# Length of array being generated  = Ceil((Stop - Start) / Step) 

#Example  
#python programming illustrating 
#numpy.arange method 
import numpy as geek 

print("A\n", geek.arange(4).reshape(2,2), "\n")
print("A\n", geek.arange(4, 10), "\n")
print("A\n", geek.arange(4, 20, 3), "\n")


#The numpy.linspace() function returns number spaces evenly w.r.t interval. Similar to numpy.arange() function but instead of step it uses sample number. 
# Syntax :

#  numpy.linspace(start,
#                stop,
#                num = 50,
#                endpoint = True,
#                retstep = False,
#                dtype = None)
# Parameters : 

# -> start  : [optional] start of interval range. By default start = 0
# -> stop   : end of interval range
# -> restep : If True, return (samples, step). By default restep = False
# -> num    : [int, optional] No. of samples to generate
# -> dtype  : type of output array
# Return : 
 

# -> ndarray
# -> step : [float, optional], if restep = True
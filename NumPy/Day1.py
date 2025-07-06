import numpy as np
a = [2,3,4,5]
print(a)

print(type(a))
print()
arr = np.array(a)
print(arr)
print(type(arr))



#numpy.ndarray.ndim() function return the number of dimensions of an array.
#The .ndim attribute (not function) returns the number of dimensions (also called axes or rank) of a NumPy array.



a = np.array([1,2,3,4])
b = np.array([[1,2,3,4], [5,6,7,8,]])
c = np.array([[1,2,3,4], [5,6,7,8,], [9,10, 11, 12]])

print(a.ndim)
print(b.ndim)
print(c.ndim)

#return which types of array is 1d or 2d 

#Now we have few more functions such as np.array.shape, np.array.size and np.array.dtype
#shape will basically return us the total number of rows and columns of the array in a tuple format (number of rows, number of columns)
#size will tell us the total number of elements or values present in the array
#dtype will tell us the data type of values which the array is containing


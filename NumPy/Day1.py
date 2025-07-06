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

#return which types of array is 1d or 2d \

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

b=np.array([[1,2,3,4],[5,6,7,8]])
print(b.shape)
print(b.size)
print(b.dtype)


#output of it 
#So we have 2 rows and 4 columns in the array b
#We have 8 elements present in the array
#The data type of the elements present in the array is int



# The numpy.zeros() function returns a new array of given shape and type, with zeros. Syntax:
# numpy.zeros(shape, dtype = None, order = 'C')
# Parameters :

 

# shape : integer or sequence of integers
# order  : C_contiguous or F_contiguous
        #  C-contiguous order in memory(last index varies the fastest)
        #  C order means that operating row-rise on the array will be slightly quicker
        #  FORTRAN-contiguous order in memory (first index varies the fastest).
        #  F order means that column-wise operations will be faster. 
# dtype : [optional, float(byDeafult)] Data type of returned array.  


#Return 
# ndarray of zeros having given shape, order and datatype.

# Python Program illustrating
# numpy.zeros method
 
import numpy as geek
 
b = geek.zeros(2, dtype = int)
print("Matrix b : \n", b)
 
a = geek.zeros([2, 2], dtype = int)
print("\nMatrix a : \n", a)
 
c = geek.zeros([3, 3])
print("\nMatrix c : \n", c)
import numpy as np
import matplotlib.pyplot as plt


#NETED ARRAY = arrays that have arrays as there element

arr = np.array([1,2,3,4,5,6])   #The numbers 1,2,3.... are the elements of this array
print(arr)
print(type(arr))

#ARRAY TYPES
#0D ARRAY --> SCALARS --> Each element in an array is a 0D array
arr_0d = np.array(18)
print(arr_0d)
print(arr_0d.ndim , "Dimension Array\n")             #HOW TO CHECK NUMBER OF DIRECTION = array_name.ndim()

#1D ARRAY --> Arrays that have 0D ARRAYS as there element
arr_1d = np.array([1,2,3,4,5,6,7,8,9])
print(arr_1d)
print(arr_1d.ndim , "Dimension Array\n")

#2D ARRAY --> Arrays that have 1D ARRAYS as there element
arr_2d = np.array([[1,2,3], [4,5,6]])
print(arr_2d)
print(arr_2d.ndim , "Dimension Array\n")

#3D ARRAY --> Arrays that have 2D ARRAYS as there element
arr_3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])
print(arr_3d)
print(arr_3d.ndim , "Dimension Array\n")

# CREATIN n-number of Dimensions ARRAY

arr_n = np.array([1,2,3,4], ndmin= 5)   # "nidimn" -- For asigning number of dimensions
                                        # "ndim"   -- For counting number of dimensions 
print(arr_n, "Number of Dimenions = ", arr_n.ndim)

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()
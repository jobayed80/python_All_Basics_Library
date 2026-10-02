
import numpy as np

# Create a NumPy ndarray Object
arr = np.array([2,3,4,5,65,67,66])
print(arr)
print(type(arr))


# Create a 0-D array with value 42
arr0D = np.array(42)
print("\n", arr0D)

# Create a 1-D array containing the values 1,2,3,4,5:
arr1D = np.array([1,2,3,4,5,6])
print("\n", arr1D)

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
arr2D = np.array([[1,2,3], [4,5,6]])
print("\n", arr2D)

# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:
arr3D = np.array ([[ [8,2,0], [4,5,6], [17,8,49] ]])
print("\n", arr3D)

# Here ndim that means number of Arrays Dimensions like arr@d.ndim that means 2 arrays
print("\n", arr0D.ndim)
print("\n", arr1D.ndim)
print("\n", arr2D.ndim)
print("\n", arr3D.ndim)


arrHigherDim = np.array([55,56,57,58], ndmin=5)
print(arrHigherDim)
import numpy as np

# print(np.__version__)

# a = np.array([1,2,3])
# print(a) #[1 2 3]
# print(a.shape) #(3,) - this means one dimensional with three elements
# print(a.dtype) #int64
# print(a.ndim) # 1 - here it is one dimension
# print(a.size) # 3 - returns the number of elements
# print(a.itemsize) # 8 - returns the size of each element in bytes

# print(a[0])
# a[0] = 7
# print(a)

# b = np.array([4,5,6])
# dot = np.dot(a,b)
# print(dot)

# dot = a @ b
# print(dot)

# Multidimensional arrays
# a = np.array([[1,2,3],[3,2,4]])
# print(a) # [[1 2 3]
#          #  [3 2 4]]
# print(a.shape) # (2, 3) - 2 rows and 3 columns

# Access elements
# print(a[1][2]) # 4 - first row and second column...indexing starts from 0, that's why second row and third column
# print(a[1,2]) # 4 - the same result, maybe the shortest version
# print(a[:,0]) # [1 3] - returns all rows in column 0
# print(a[0,:]) # [1 2 3] - returns all columns in row 0

# Transpos
# print(a.T) 

# Inverse
# a = np.array([[1,2],[3,2]])
# print(np.linalg.inv(a)) # [[-0.5   0.5 ]
                        #  [ 0.75 -0.25]]

# Determinant
# print(np.linalg.det(a)) # -4.000000000000001

# Diagonal of a matrix
# print(np.diag(a)) # [1 2]

# Slicing
# a = np.array([[1,2,3,4],[5,6,7,8]])
# print(a[0,:]) # [1 2 3 4] - returns the first row
# print(a[0,1:3]) # [2 3] - returns from the row 0 elements in the index 1 and 2 (3 not inclusive)
# print(a[-1,-1]) # 8 - returns element from the last row and last column
# print(a[-1,-2]) # 7

# a = np.array([[1,2],[3,4],[5,6]])
# bool_idx = a > 2
# print(bool_idx) # [[False False]
                #  [ True  True]
                #  [ True  True]]

# print(a[bool_idx]) # [3 4 5 6] - 1d array
# print(a[a > 2]) # [3 4 5 6] - the same result and meaning
# b = np.where(a > 2, a, -1) # every False element replace by -1
# print(b) # [[-1 -1] 
         #  [ 3  4]
         #  [ 5  6]]

# fancy indexing
a = np.array([13,42,45,23,55,12])
# b = [1,3,5]
# print(a[b]) # [42 23 12] - elements in an array a which corresponds to the indexes 1, 3 and 5

even = np.argwhere(a%2==0).flatten()
print(a[even]) # [42 12]

# without flatten it looks like this
even = np.argwhere(a%2==0)
print(a[even]) # [[42]
               #  [12]]
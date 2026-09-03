import numpy as np

# copy()

A = np.array([1, 2, 3, 4, 5, 6])
print(A)

B = A.copy()
B[0] = 200

print(B)
print(A)
# copy() creates a separate copy.
# Changes in B will not affect A.


# view()

A = np.array([1, 2, 3, 4, 5, 6])
print(A)

B = A.view()
B[0] = 200

print(B)
print(A)
# view() shares the same data with the original array.
# Changes in B will also affect A.


# append()

A = np.array([1, 2, 3, 4, 5, 6])
print(A)

B = A.view()
B = np.append(B, 345)

print(B)
print(A)
# append() adds elements and returns a new array.
# Original array is not changed.


# add(), subtract(), multiply(), divide()

A = np.array([1, 2, 3, 4, 5, 6])

B = A.view()

print(np.add(B, 2))
print(np.subtract(B, 2))
print(np.multiply(B, 2))
print(np.divide(B, 2))

# Arithmetic operations are applied element-wise.


# insert()

A = np.array([1, 2, 3, 4, 5, 6])

B = np.insert(A, 5, 455)

print(B)
# insert() adds an element at the given index.
# It returns a new array.


# random.choice()

A = np.random.choice([1, 2, 3, 4, 5, 6], size=[2, 3, 2])
print(A)

B = np.random.choice([1, 2, 3, 4, 5, 6], size=[2, 3])
C = np.random.choice([1, 2, 3, 4, 5, 6], size=[2])

print(B)
print(C)
# random.choice() randomly selects values from the given array
# according to the specified size.


# sort()

A = np.array([1, 2, 34, 12, 65, 34])

B = np.sort(A)
print(B)

C = np.sort(A)[::-1]
print(C)
# sort() returns the sorted array.
# [::-1] is used for descending order.


# argsort()

A = np.array([1, 2, 34, 12, 65, 34])

B = np.argsort(A)

print(B)
# argsort() returns the indices that would sort the array.


# argmax() and argmin()

A = np.array([1, 2, 34, 12, 65, 34])

print(np.argmax(A))
print(np.argmin(A))
# argmax() returns the index of the maximum value.
# argmin() returns the index of the minimum value.


# array_split()

A = np.array([1, 2, 34, 12, 65, 32, 32])

B = np.array_split(A, 2)

print(B)
print(B[0])
print(B[1])
# array_split() splits an array into multiple sub-arrays.


# array_split() on 2D array

D2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

D22 = np.array_split(D2, 2)

print(D22)
print(D22[0])
print(D22[1])


# concatenate()

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

C = np.concatenate((A, B))

print(C)
# concatenate() joins two or more arrays.


# concatenate() on 2D array

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(np.concatenate((A, B), axis=0))
print(np.concatenate((A, B), axis=1))

# axis=0 -> row-wise
# axis=1 -> column-wise


# vstack()

A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8])

C = np.vstack((A, B))

print(C)
print(C.ndim)
# vstack() joins arrays vertically.
# It adds rows.


# hstack()

A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8])

C = np.hstack((A, B))

print(C)
# hstack() joins arrays horizontally.


# dstack()

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

B = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

C = np.dstack((A, B))

print(C)
# dstack() stacks arrays along the third axis.


# stack()

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print(np.stack((A, B)))
print(np.stack((A, B), axis=1))
# stack() joins arrays along a new axis.


# transpose()

A = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(A)

B = np.transpose(A)

print(B)
# transpose() converts rows into columns
# and columns into rows.


# delete() on 1D array

A = np.array([1, 2, 3, 4, 5, 6])

B = np.delete(A, 2)
print(B)

B = np.delete(A, 0)
print(B)

C = np.delete(A, np.where(A == 6))
print(C)
# delete() removes elements and returns a new array.


# Boolean masking

A = np.array([1, 2, 3, 4, 5, 6])

B = A[A != 5]

print(B)
# Boolean masking filters elements based on a condition.


# delete() on 2D array

A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

B = np.delete(A, 1, axis=0)
print(B)

C = np.delete(A, 2, axis=1)
print(C)

# axis=0 -> delete row
# axis=1 -> delete column


# delete() with multiple indices

A = np.arange(0, 12).reshape(3, 4)

print(A)

B = np.delete(A, [1, 3], axis=1)

print(B)
# Multiple rows or columns can be deleted using indices.


# setflags()

X = np.array([1, 2, 3, 4, 5, 6])

X.setflags(write=False)

print(X)

# X[0] = 34
# This will give an error because the array is read-only.

Y = np.append(X, 213)

print(Y)
# setflags(write=False) makes the array read-only.


# intersect1d()

B = np.array([1, 2, 3, 4, 4])
C = np.array([4, 5, 6, 7, 8])

print(np.intersect1d(B, C))
# intersect1d() returns common elements from two arrays.


# union1d()

print(np.union1d(B, C))
# union1d() returns unique elements from both arrays.


# unique()

A = np.array([1, 2, 2, 3, 3, 3, 4, 5])

B = np.unique(A)

print(B)
# unique() returns unique elements from an array.


# where()

A = np.array([10, 20, 30, 40, 50])

B = np.where(A > 25)

print(B)
# where() returns indices where the condition is True.


# where() with replacement

A = np.array([10, 20, 30, 40, 50])

B = np.where(A > 25, 100, A)

print(B)
# Values greater than 25 are replaced with 100.


# clip()

A = np.array([10, 20, 30, 40, 50, 60])

B = np.clip(A, 20, 50)

print(B)
# clip() limits values between minimum and maximum range.


# flip()

A = np.array([1, 2, 3, 4, 5])

B = np.flip(A)

print(B)
# flip() reverses the elements of an array.


# flip() on 2D array

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(np.flip(A))
# flip() reverses the complete array.


# flip() with axis

print(np.flip(A, axis=0))
print(np.flip(A, axis=1))

# axis=0 -> reverse rows
# axis=1 -> reverse columns
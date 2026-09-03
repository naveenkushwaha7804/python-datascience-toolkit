import numpy as np

# Statistical Functions

b = np.array([10, 20, 30, 40, 50])

a = b.astype(int)

# Mean = average of all values
print(np.mean(b))

# Median = middle value
print(np.median(a))

# Standard Deviation = data spread from mean
print(np.std(a))

# Variance = square of standard deviation
print(np.var(a))

# Power of each element
print(np.power(a, 2))


# Sum, Minimum and Maximum

print(np.sum(a))
print(np.min(a))
print(np.max(a))

# Index of minimum and maximum value
print(np.argmin(a))
print(np.argmax(a))


# Statistical Functions with 2D Array

b = np.array([[1, 2, 3],
              [4, 5, 6]])

print(np.mean(b, axis=0))  # Column average
print(np.mean(b, axis=1))  # Row average

print(np.sum(b))
print(np.sum(b, axis=0))  # Column-wise sum
print(np.sum(b, axis=1))  # Row-wise sum

print(np.min(b, axis=0))
print(np.max(b, axis=1))


# Flatten and Ravel

a = np.array([[1, 2, 3, 4]])

print(a.flatten())
print(b.ravel())

# flatten() and ravel() convert multidimensional array into 1D array


# Resize

a.resize(2, 2)
print(a)

# resize() changes the shape of the array


# Transpose

b = np.array([[1, 2],
              [3, 4]])

print(np.transpose(b))

# transpose() converts rows into columns and columns into rows


# Concatenation

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.concatenate((a, b)))

# concatenate() joins two or more arrays


# 2D Concatenation

x = np.array([[1, 2],
              [3, 4]])

y = np.array([[5, 6],
              [7, 8]])

print(np.concatenate((x, y), axis=0))  # Row-wise
print(np.concatenate((x, y), axis=1))  # Column-wise


# Zeros

a = np.zeros((2, 3))
print(a)

b = a.astype(int)
print(b)


# Ones

a = np.ones((2, 3))
print(a)


# Full

a = np.full((2, 3), 7)
print(a)


# Identity Matrix

a = np.eye(3)
print(a)


# Array Creation using arange

a = np.arange(1, 11)
print(a)

a = np.arange(1, 11, 2)
print(a)


# Reshape

a = np.arange(1, 7)
print(a.reshape(2, 3))


# Sorting

a = np.array([50, 10, 40, 20, 30])

print(np.sort(a))


# Unique Values

a = np.array([10, 20, 10, 30, 20, 40])

print(np.unique(a))


# Conditional Filtering

a = np.array([10, 20, 30, 40, 50])

print(a[a > 25])
print(a[a % 2 == 0])


# Comparison Operations

a = np.array([10, 20, 30, 40, 50])

print(a > 25)
print(a == 30)


# Any and All

a = np.array([10, 20, 30, 40, 50])

print(np.any(a > 40))
print(np.all(a > 0))


# Split Array

a = np.array([10, 20, 30, 40, 50, 60])

print(np.split(a, 3))


# Horizontal and Vertical Stack

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.hstack((a, b)))
print(np.vstack((a, b)))


# Mathematical Operations

a = np.array([1, 4, 9, 16, 25])

print(np.sqrt(a))
print(np.square(a))
print(np.power(a, 2))


# Absolute Value

a = np.array([-10, -20, 30, -40])

print(np.abs(a))


# Trigonometric Functions

a = np.array([0, 30, 60, 90])

print(np.sin(np.deg2rad(a)))
print(np.cos(np.deg2rad(a)))


# Random Numbers

print(np.random.rand(3))
print(np.random.randint(1, 10, 5))


# Random 2D Array

print(np.random.randint(1, 100, (3, 3)))


# Copy

a = np.array([10, 20, 30])

b = a.copy()

b[0] = 100

print(a)
print(b)


# View

a = np.array([10, 20, 30])

b = a.view()

b[0] = 100

print(a)
print(b)
import numpy as np

# 1D

# np.arange(start, stop, step)

d = np.arange(1, 10, 2)
print(d)

a = d.reshape(1, 5)
print(a)

for i in range(len(d)):
    print(d[i], i)

# arange() -> range ke according NumPy array banata hai
# reshape() -> array ka shape change karta hai
# len() -> array ki length batata hai
# range() -> loop ke liye sequence provide karta hai


# 1D for loop value based

d = np.arange(1, 10, 2)

for i in d:
    print(i)

# Directly array ke elements ko access karta hai


# 1D indexed based loop

for i in range(len(d)):
    print("Index:", i, "Value:", d[i])


# NumPy nditer()

for i in np.nditer(d):
    print(i)

# nditer() array ke elements ko one by one iterate karta hai


# NumPy ndenumerate()

for i in np.ndenumerate(d):
    print(i)

# ndenumerate() index aur value dono return karta hai


# 1D loop with condition

d = np.array([10, 20, 30, 40, 50])

for i in d:
    if i > 25:
        print(i)

# Loop ke andar condition bhi apply kar sakte hain


# 1D loop with index and condition

for i in range(len(d)):
    if d[i] > 25:
        print("Index:", i, "Value:", d[i])


# 2D array

d2 = np.array([
    [1, 2, 3],
    [5, 6, 7]
])

print(d2)


# 2D nested loop

for r in d2:
    for c in r:
        print(c)

# Outer loop -> rows
# Inner loop -> columns


# 2D indexed based loop

for i in range(len(d2)):
    for j in range(len(d2[i])):
        print("Index:", i, j, "Value:", d2[i][j])

# i -> row index
# j -> column index


# 2D nditer()

for i in np.nditer(d2):
    print(i)

# nditer() multidimensional array ke har element ko iterate karta hai


# 2D ndenumerate()

for i in np.ndenumerate(d2):
    print(i)

# ndenumerate() index tuple aur value return karta hai


# 2D loop with condition

for r in d2:
    for c in r:
        if c % 2 == 0:
            print(c)

# Even elements print honge


# 2D loop with index and condition

for i in range(d2.shape[0]):
    for j in range(d2.shape[1]):
        if d2[i, j] > 3:
            print("Index:", i, j, "Value:", d2[i, j])

# shape[0] -> number of rows
# shape[1] -> number of columns


# 2D loop using shape

for i in range(d2.shape[0]):
    for j in range(d2.shape[1]):
        print(d2[i, j])


# 3D array

d3 = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
])

print(d3)


# 3D nested loop

for t in d3:
    for r in t:
        for c in r:
            print(c)

# First loop -> blocks
# Second loop -> rows
# Third loop -> columns


# 3D indexed based loop

for i in range(d3.shape[0]):
    for j in range(d3.shape[1]):
        for k in range(d3.shape[2]):
            print("Index:", i, j, k, "Value:", d3[i, j, k])


# 3D nditer()

for i in np.nditer(d3):
    print(i)

# nditer() all dimensions ke elements ko iterate karta hai


# 3D ndenumerate()

for i in np.ndenumerate(d3):
    print(i)

# ndenumerate() complete index aur value return karta hai


# 3D loop with condition

for i in range(d3.shape[0]):
    for j in range(d3.shape[1]):
        for k in range(d3.shape[2]):
            if d3[i, j, k] % 2 == 0:
                print(d3[i, j, k])


# nditer() with modification

A = np.array([1, 2, 3, 4, 5])

for x in np.nditer(A, op_flags=['readwrite']):
    x[...] = x * 2

print(A)

# readwrite -> array elements ko modify karne ki permission
# x[...] -> original element ko update karta hai


# nditer() with flags

A = np.array([
    [1, 2],
    [3, 4]
])

for x in np.nditer(A, flags=['external_loop']):
    print(x)

# external_loop -> elements ko chunks mein iterate karta hai


# for loop with enumerate()

A = np.array([10, 20, 30, 40])

for index, value in enumerate(A):
    print(index, value)

# enumerate() index aur value dono provide karta hai


# for loop with zip()

A = np.array([10, 20, 30])
B = np.array([1, 2, 3])

for x, y in zip(A, B):
    print(x, y)

# zip() multiple arrays ke corresponding elements ko pair karta hai


# Loop with mathematical operation

A = np.array([1, 2, 3, 4, 5])

for x in A:
    print(x ** 2)

# Har element ka square calculate hoga


# Loop with sum

A = np.array([10, 20, 30, 40])

total = 0

for x in A:
    total += x

print("Sum:", total)


# Loop with maximum value

A = np.array([10, 50, 20, 80, 30])

maximum = A[0]

for x in A:
    if x > maximum:
        maximum = x

print("Maximum:", maximum)


# Loop with minimum value

minimum = A[0]

for x in A:
    if x < minimum:
        minimum = x

print("Minimum:", minimum)


# Loop with break

A = np.array([10, 20, 30, 40, 50])

for x in A:
    if x == 30:
        break
    print(x)

# break -> loop ko immediately stop karta hai


# Loop with continue

for x in A:
    if x == 30:
        continue
    print(x)

# continue -> current iteration skip karta hai


# Loop with else

for x in A:
    print(x)
else:
    print("Loop completed")

# else -> loop normally complete hone ke baad execute hota hai


# Loop with condition and else

for x in A:
    if x == 100:
        print("Value found")
        break
else:
    print("Value not found")

# Agar break execute nahi hua to else execute hoga


# Quick Summary

# for i in array
# -> value based iteration

# for i in range(len(array))
# -> index based iteration

# np.nditer(array)
# -> multidimensional array ke values iterate karta hai

# np.ndenumerate(array)
# -> index + value iterate karta hai

# enumerate(array)
# -> index + value deta hai

# zip(array1, array2)
# -> multiple arrays ke elements ko pair karta hai

# array.shape[0]
# -> rows / first dimension

# array.shape[1]
# -> columns / second dimension

# array.shape[2]
# -> third dimension

# break
# -> loop stop

# continue
# -> current iteration skip

# else
# -> loop complete hone ke baad execute
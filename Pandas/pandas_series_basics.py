# Series is called 1D
# Series can be generated using list, tuple, dictionary, numpy array, or scalar value
# Data can be int or String

import numpy as np
import pandas as pd

# Using List
A = ["sun", "mon", "tue", "wed"]
S = pd.Series(A)
print(S)

# Using Tuple
T = (12, 23, 34, 45, 56)
S2 = pd.Series(T)
print(S2)

# Using Dictionary
D = {"Name": "Naveen", "Age": 22, "Sub": "AIML"}
S3 = pd.Series(D)
print(S3)

# Using Numpy Array
Arr = np.array([10, 20, 30, 40])
S4 = pd.Series(Arr)
print(S4)

# Using Scalar Value (single value repeated with custom index)
S5 = pd.Series(5, index=[0, 1, 2, 3])
print(S5)

# Series with Custom Index
A2 = ["sun", "mon", "tue", "wed"]
S6 = pd.Series(A2, index=["a", "b", "c", "d"])
print(S6)

# Accessing elements of a Series
print(S6["a"])      # by custom index label
print(S6[0])         # by default position (0-based)

# Basic Attributes of Series
print(S6.values)     # returns values as numpy array
print(S6.index)      # returns index (RangeIndex or custom Index)
print(S6.dtype)      # returns data type of Series
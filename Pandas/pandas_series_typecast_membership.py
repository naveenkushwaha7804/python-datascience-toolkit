import pandas as pd

d = [12, 23, 43, 56, 67, 67]

print(d)
print(tuple(d))
print(list(d))
print(set(d))   # set removes duplicate values (67 appears once)

# Not work on Dictionary
# Reason: dict needs key-value pairs, tuple()/list()/set() on a
# plain list can't create keys automatically, so dict(d) will throw error
# dt2 = dict(d)   # this will raise ValueError

dt = [1.2, 3.4, 2.6, 7.4]
print(dt)

S = pd.Series(dt)
print(S)

# Type Conversion using astype
J = S.astype(int)
print(J)

K = S.astype(str)   # convert float Series to string
print(K)

# Membership Check
print(2.6 in dt)   # Core Python me values ko check karega -> True
print(7 in S)       # Series me index ko check karega -> False (index 0-3 hi hai)
print(2.6 in S.values)  # Series ke values check karne ke liye .values use karo -> True

# Basic Info
print(S.size)    # total number of elements
print(S.shape)   # shape of Series (rows,)
import pandas as pd

d = [12, 23, 43, 56, 67, 67]

print(d)
print(tuple(d))
print(list(d))
print(set(d))

# Not work on Dictionary

dt = [1.2, 3.4, 2.6, 7.4]
print(dt)

S = pd.Series(dt)
print(S)

J = S.astype(int)
print(J)

print(2.6 in dt)  # Core Python me values ko check karega
print(7 in S)     # Series me index ko check karega
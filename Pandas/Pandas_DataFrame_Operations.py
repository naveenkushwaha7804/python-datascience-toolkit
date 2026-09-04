import numpy as np
import pandas as pd


# Series Updating

d = [1, 2, 5, 4, 23, 56, 34, 43]
F = pd.Series(d)

# Updating the Series
a = 0

for i in F:
    i = i + 1
    F[a] = i
    a += 1

print(F)


# While loop se

# a = 0
# while a < len(F):
#     F[a] = F[a] + 1
#     a += 1
# print(F)


# DataFrame

dt = [12, 2, 334, 546, 566, 757, 32, 44, 64]

df = pd.DataFrame(dt)
print(df)

# Column ko name denge

df = pd.DataFrame(dt, columns=["marks"])
print(df)


# Apply

# print(df.apply(min))
# print(df.apply(lambda x: x + 10))


# def even(n):
#     if n % 2 == 0:
#         return n


# print(even(31))
# df["marks"].apply(even)


# isin()

dt = [12, 2, 334, 546, 566, 757, 32, 44, 64]

df = pd.DataFrame(dt)

# print(df)

# print(df.isin([44, 22, 45]))

print(df.isin([22, 33, 44, 55]).count())

# df[df.isin([44, 33])].values
# df[df.isin([44, 33]).values]


# GroupBy

d = pd.read_csv("car_type - car_type.csv")

print(d)

# Groupby for group the value

f = d.groupby("Model")
print(f)

for i, r in f:
    print(i)
    print(r)


# GroupBy

d = pd.read_csv("myrgroup - myrgroup.csv")

# print(d)

dc = d.groupby("city")

# for i, v in dc:
#     print(i, v)

# print(dc.max())
# print(dc.describe())

print(dc.agg({
    "temp": "min",
    "windspeed": "max"
}))

print(dc.max())


# Concat

A1 = {
    "A": [10, 20],
    "B": [30, 40]
}

A2 = {
    "C": [100, 200],
    "D": [300, 400]
}

print(A1)
print(A2)

D1 = pd.DataFrame(A1)
D2 = pd.DataFrame(A2)

print(D1)

print(pd.concat([D1, D2]))


# Concat

A1 = {
    "A": [10, 20, 30, 35],
    "B": [40, 50, 60, 70]
}

A2 = {
    "X": [100, 200, 300, 400],
    "Y": [500, 600, 700, 800]
}

df1 = pd.DataFrame(
    A1,
    index=["a", "b", "c", "d"]
)

df2 = pd.DataFrame(
    A2,
    index=["a", "b", "x", "y"]
)

print(df1)
print(df2)

print(pd.concat([df1, df2]))

print(pd.concat(
    [df1, df2],
    ignore_index=True
))

print(pd.concat(
    [df1, df2],
    axis=1
))


# JOIN

# Index base pr add karta hai

print(df1.join(df2, how="left"))
print(df1.join(df2, how="right"))

# By default left join karta hai
# Axis ki jaroorat nahi hai or index ignore ki v nahi hai
# Join types of joining allow karta hai

# Inner join - dono dataframe me common column hona chahiye
# Or jo values same hongi un column ka data print hoga

print(df1.join(df2, how="inner"))


# MERGE

# Column base pr add karta hai
# Ek column same hota hai jo jo values same hoti hain
# unka data show karta hai
# By default inner merge work karta hai

A1 = {
    "A": [10, 20, 30, 35],
    "B": [40, 50, 60, 70]
}

A2 = {
    "X": [100, 200, 300, 400],
    "A": [10, 20, 30, 35]
}

df1 = pd.DataFrame(A1)
df2 = pd.DataFrame(A2)

print(pd.merge(
    df1,
    df2,
    on="A"
))

# Blank kyuki same column ki values same nahi hai
# Ek v ab same karenge

print(pd.merge(
    df1,
    df2,
    on="A",
    how="left"
))

print(pd.merge(
    df1,
    df2,
    on="A",
    how="right"
))


# Value Counts

ar = [10, 11, 6, 7, 6, 60, 6, 0]

arr = pd.Series(ar)

print(arr.value_counts())
import numpy as np
import pandas as pd

data = pd.read_csv('myrgroup - myrgroup.csv')
# print(data)

# ---------------- DataFrame with Missing Values (NaN) ----------------
data2 = [[12, np.nan, 13, 5, np.nan],
         [36, 78, 34, 22, 35],
         [np.nan, np.nan, np.nan, 50, 77],
         [98, 78, np.nan, 20, 80]]

data3 = pd.DataFrame(data2)
print(data2)
print(data3)

# ---------------- Filling Missing Values ----------------
print(data3.ffill())   # upar wali value se fill karega (forward fill)
print(data3.bfill())   # niche wali value se fill karega (backward fill)

# Naming columns properly
data4 = pd.DataFrame(data3.values, columns=["A", "B", "C", "D", "E"])
print(data4)

print(data4["A"].fillna(100))            # NaN ko 100 se fill karo
print(data4["B"].fillna(value=60))       # NaN ko 60 se fill karo

# Fill using median of column A (fixed: correct syntax data3["A"].median())
print(data4.fillna(value=data4["A"].median()))

# ---------------- apply() function practice ----------------
data1 = [89, 57, 45, 66, 77, 34, 90]
df = pd.DataFrame(data1, columns=['Marks'])
print(df)

print(df.apply(max))              # apply() ke andar ek function hi dena hai without () ke
print(df.apply(lambda x: x + 10))  # sabhi values me 10 add karo

# ---------------- apply() with custom function ----------------
def even(n):
    if n % 2 == 0:
        return n
    else:
        return np.nan   # odd numbers ko NaN bana do

print(df['Marks'].apply(even))
print(df['Marks'].apply(lambda x: x * 2))   # sabhi marks double karo
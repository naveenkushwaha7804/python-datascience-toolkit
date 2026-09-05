import numpy as np
import pandas as pd
import seaborn as sns

# ---------------- DataFrame from a List of lists ----------------
list1 = [[20, 33, 22, 90], [20, 33, 22, 90], [20, 33, 22, 90]]

dt = pd.DataFrame(list1, columns=['Marks', 'roll', 'avg', 'rrr'])
print(dt)

# ---------------- DataFrame from a Dictionary ----------------
dict1 = {"roll": ["101", "102", "103", "104"], "marks": [20, 33, 22, 90]}
dt1 = pd.DataFrame(dict1)
print(dt1)

# ---------------- Seaborn Dataset ----------------
s = sns.load_dataset('tips')
print(s.head())      # pehle 5 rows dikhata hai
print(s.shape)        # (rows, columns)
print(s.columns)      # sabhi column names
print(s.info())       # dataset ki summary/info

# ---------------- Reading CSV with nrows & usecols ----------------
c = pd.read_csv('car_type - car_type.csv', nrows=10)
print(c)

# this will only load 10 rows from that db to prevent system loading of extra data sets.
# usecols will extract given columns
c_cols = pd.read_csv('car_type - car_type.csv', nrows=10, usecols=['Car', 'Model'])
print(c_cols)

# ---------------- Full CSV EDA ----------------
c = pd.read_csv('car_type - car_type.csv')

print(c.columns)                  # columns name de dega
print(c.values)                    # values de dega array format me
print(c.shape)                     # (rows, columns)
print(c.info())                     # information de deta h table ki
print(c.describe())                # sirf numerical values pe work karega
print(c.describe(include='all'))   # sabhi columns (numeric + object) ka summary
print(c.duplicated().sum())        # kitni duplicate rows hai

c['Model'][0] = 'go'               # ek value update karna
print(c)